#!/usr/bin/env python3
"""Read-only security and robustness audit for n8n workflows via the REST API.

No external dependencies. Never mutates workflows, credentials or executions.
Never prints the API key. Prefer passing it via the N8N_API_KEY environment
variable instead of --api-key to keep it out of shell history.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request

TRIGGER_TYPES = {
    "n8n-nodes-base.webhook",
    "n8n-nodes-base.cron",
    "n8n-nodes-base.scheduleTrigger",
    "n8n-nodes-base.errorTrigger",
    "n8n-nodes-base.manualTrigger",
    "n8n-nodes-base.emailReadImap",
    "n8n-nodes-base.mqttTrigger",
}
HIGH_RISK_TYPES = {
    "n8n-nodes-base.executeCommand",
    "n8n-nodes-base.ssh",
    "n8n-nodes-base.code",
    "n8n-nodes-base.function",
    "n8n-nodes-base.functionItem",
}
EXTERNAL_CALL_TYPES = {
    "n8n-nodes-base.httpRequest",
    "n8n-nodes-base.graphql",
    "n8n-nodes-base.webhookResponse",
}
SECRET_KEY_PATTERN = re.compile(
    r"(apikey|api_key|token|password|passwd|secret|authorization|bearer)",
    re.IGNORECASE,
)
SECRET_VALUE_PATTERN = re.compile(
    r"^(sk-[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{12,}|ghp_[A-Za-z0-9]{20,}|Bearer\s+\S+|"
    r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})"
)
EXPRESSION_PREFIX = "={{"


def http_get(base_url, path, api_key):
    req = urllib.request.Request(
        base_url.rstrip("/") + path,
        headers={
            "X-N8N-API-KEY": api_key,
            "Accept": "application/json",
            "User-Agent": "n8n-workflow-auditor/0.1.0 (+https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"[FAILED] HTTP {exc.code} en {path}: {exc.reason}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"[FAILED] No se pudo conectar a {base_url}: {exc.reason}")


def list_workflows(base_url, api_key, only_active):
    workflows = []
    cursor = None
    while True:
        path = "/api/v1/workflows?limit=250"
        if only_active:
            path += "&active=true"
        if cursor:
            path += f"&cursor={cursor}"
        data = http_get(base_url, path, api_key)
        workflows.extend(data.get("data", []))
        cursor = data.get("nextCursor")
        if not cursor:
            break
    return workflows


def get_workflow(base_url, api_key, workflow_id):
    return http_get(base_url, f"/api/v1/workflows/{workflow_id}", api_key)


def scan_params_for_secrets(params, path="parameters"):
    findings = []
    if isinstance(params, dict):
        for key, value in params.items():
            key_path = f"{path}.{key}"
            if isinstance(value, (dict, list)):
                findings.extend(scan_params_for_secrets(value, key_path))
            elif isinstance(value, str):
                if value.startswith(EXPRESSION_PREFIX) or not value.strip():
                    continue
                key_hits_pattern = bool(SECRET_KEY_PATTERN.search(str(key)))
                value_hits_pattern = bool(SECRET_VALUE_PATTERN.match(value.strip()))
                if value_hits_pattern or (key_hits_pattern and len(value) >= 12):
                    findings.append(key_path)
    elif isinstance(params, list):
        for idx, item in enumerate(params):
            findings.extend(scan_params_for_secrets(item, f"{path}[{idx}]"))
    return findings


def check_webhook_auth(nodes):
    offenders = []
    for node in nodes:
        if node.get("type") == "n8n-nodes-base.webhook":
            auth = (node.get("parameters") or {}).get("authentication", "none")
            if auth in ("none", None):
                offenders.append(node.get("name", "?"))
    status = "FAILED" if offenders else "PASSED"
    return {
        "rule": "1. Webhooks sin autenticacion",
        "status": status,
        "evidence": offenders,
        "detail": "Nodos webhook con authentication=none" if offenders else "Todos los webhooks tienen autenticacion configurada",
    }


def check_hardcoded_secrets(nodes):
    offenders = {}
    for node in nodes:
        hits = scan_params_for_secrets(node.get("parameters") or {})
        if hits:
            offenders[node.get("name", "?")] = hits
    status = "FAILED" if offenders else "PASSED"
    return {
        "rule": "2. Credenciales hardcodeadas en parametros",
        "status": status,
        "evidence": offenders,
        "detail": "Valores literales con forma de secreto en parametros de nodo (no via credential manager)" if offenders else "Sin literales con forma de secreto detectados",
    }


def check_high_risk_nodes(nodes):
    offenders = [n.get("name", "?") for n in nodes if n.get("type") in HIGH_RISK_TYPES and not n.get("disabled")]
    status = "WARN" if offenders else "PASSED"
    return {
        "rule": "3. Nodos de alto riesgo (comandos, SSH, codigo)",
        "status": status,
        "evidence": offenders,
        "detail": "Requieren revision manual: ejecutan comandos, SSH o codigo arbitrario" if offenders else "Sin nodos de ejecucion de comandos/codigo activos",
    }


def check_error_workflow(workflow):
    error_wf = (workflow.get("settings") or {}).get("errorWorkflow")
    status = "PASSED" if error_wf else "FAILED"
    return {
        "rule": "4. Workflow de error configurado",
        "status": status,
        "evidence": error_wf,
        "detail": "settings.errorWorkflow definido" if error_wf else "Sin errorWorkflow: fallos silenciosos si nadie mira las ejecuciones",
    }


def check_retry_on_external_calls(nodes):
    offenders = []
    for node in nodes:
        if node.get("type") in EXTERNAL_CALL_TYPES and not node.get("disabled"):
            if not node.get("retryOnFail"):
                offenders.append(node.get("name", "?"))
    status = "FAILED" if offenders else "PASSED"
    return {
        "rule": "5. Reintentos en llamadas externas",
        "status": status,
        "evidence": offenders,
        "detail": "Nodos HTTP/GraphQL sin retryOnFail" if offenders else "Llamadas externas con retryOnFail configurado",
    }


def check_orphan_nodes(nodes, connections):
    connected = set()
    for source_name, outputs in (connections or {}).items():
        connected.add(source_name)
        for output_group in outputs.values():
            for branch in output_group:
                for target in branch:
                    connected.add(target.get("node"))
    offenders = [
        n.get("name", "?")
        for n in nodes
        if n.get("name") not in connected and n.get("type") not in TRIGGER_TYPES and not n.get("disabled")
    ]
    status = "FAILED" if offenders else "PASSED"
    return {
        "rule": "6. Nodos huerfanos o desconectados",
        "status": status,
        "evidence": offenders,
        "detail": "Nodos sin conexion de entrada ni salida, fuera de triggers" if offenders else "Todos los nodos no-trigger estan conectados",
    }


def check_reachable_trigger(nodes, active):
    if not active:
        return {
            "rule": "7. Workflow activo con trigger alcanzable",
            "status": "PASSED",
            "evidence": None,
            "detail": "Workflow inactivo, regla no aplica",
        }
    has_trigger = any(n.get("type") in TRIGGER_TYPES and not n.get("disabled") for n in nodes)
    status = "PASSED" if has_trigger else "FAILED"
    return {
        "rule": "7. Workflow activo con trigger alcanzable",
        "status": status,
        "evidence": has_trigger,
        "detail": "Al menos un trigger activo" if has_trigger else "Workflow marcado activo sin trigger utilizable",
    }


def audit_workflow(workflow):
    nodes = workflow.get("nodes") or []
    connections = workflow.get("connections") or {}
    checks = [
        check_webhook_auth(nodes),
        check_hardcoded_secrets(nodes),
        check_high_risk_nodes(nodes),
        check_error_workflow(workflow),
        check_retry_on_external_calls(nodes),
        check_orphan_nodes(nodes, connections),
        check_reachable_trigger(nodes, workflow.get("active", False)),
    ]
    return {
        "id": workflow.get("id"),
        "name": workflow.get("name"),
        "active": workflow.get("active", False),
        "checks": checks,
    }


def build_summary(workflows):
    active = sum(1 for wf in workflows if wf.get("active"))
    return {
        "total": len(workflows),
        "active": active,
        "inactive": len(workflows) - active,
    }


def render_markdown(report):
    lines = [f"# Auditoria n8n — {report['n8n_url']}", ""]
    summary = report["summary"]
    lines.append(f"Workflows totales: {summary['total']} | activos: {summary['active']} | inactivos: {summary['inactive']}")
    lines.append("")
    if report.get("summary_only"):
        lines.append("| Workflow | ID | Estado | Nodos | Triggers |")
        lines.append("|---|---|---|---|---|")
        for wf in report["workflows"]:
            lines.append(f"| {wf['name']} | `{wf['id']}` | {'activo' if wf['active'] else 'inactivo'} | {wf['node_count']} | {', '.join(wf['trigger_types']) or 'ninguno'} |")
        return "\n".join(lines)
    for wf in report["workflows"]:
        lines.append(f"## {wf['name']} (`{wf['id']}`) — {'activo' if wf['active'] else 'inactivo'}")
        lines.append("")
        lines.append("| Regla | Estado | Detalle |")
        lines.append("|---|---|---|")
        for check in wf["checks"]:
            lines.append(f"| {check['rule']} | [{check['status']}] | {check['detail']} |")
        lines.append("")
    return "\n".join(lines)


def summarize_workflow(workflow):
    nodes = workflow.get("nodes") or []
    return {
        "id": workflow.get("id"),
        "name": workflow.get("name"),
        "active": workflow.get("active", False),
        "node_count": len(nodes),
        "trigger_types": sorted({n.get("type") for n in nodes if n.get("type") in TRIGGER_TYPES and not n.get("disabled")}),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="URL base de n8n, ej: https://n8n.midominio.com")
    parser.add_argument("--api-key", help="API key de n8n. Preferi la variable de entorno N8N_API_KEY.")
    parser.add_argument("--workflow-id", help="Auditar un unico workflow por id")
    parser.add_argument("--all", action="store_true", help="Incluir workflows inactivos (por defecto solo activos)")
    parser.add_argument("--summary", action="store_true", help="Solo inventario (id, nombre, activo, nodos, triggers), sin correr las 7 reglas")
    parser.add_argument("--json", dest="json_out", help="Ruta de salida JSON")
    parser.add_argument("--markdown", dest="md_out", help="Ruta de salida Markdown")
    args = parser.parse_args()

    api_key = args.api_key or __import__("os").environ.get("N8N_API_KEY")
    if not api_key:
        raise SystemExit("[FAILED] Falta API key: pasa --api-key o define N8N_API_KEY")

    if args.workflow_id:
        workflows = [get_workflow(args.url, api_key, args.workflow_id)]
    else:
        # La lista ya trae nodes/connections/settings completos: no hace falta
        # un GET adicional por workflow. En instancias con cientos de workflows,
        # ese N+1 es lo que antes causaba timeouts.
        workflows = list_workflows(args.url, api_key, only_active=not args.all)

    report = {
        "n8n_url": args.url,
        "summary": build_summary(workflows),
        "summary_only": args.summary,
        "workflows": [summarize_workflow(wf) for wf in workflows] if args.summary else [audit_workflow(wf) for wf in workflows],
    }

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
    if args.md_out:
        with open(args.md_out, "w", encoding="utf-8") as fh:
            fh.write(render_markdown(report))

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
