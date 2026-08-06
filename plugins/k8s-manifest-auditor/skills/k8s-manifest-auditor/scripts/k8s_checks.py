#!/usr/bin/env python3
"""Instrumentos deterministas para 11 controles de los Kubernetes Pod Security
Standards (Baseline + Restricted) sobre un manifiesto YAML puntual.

Fuente: https://kubernetes.io/docs/concepts/security/pod-security-standards/
(CC BY 4.0). Cada regla corresponde a un control textual de esa tabla oficial,
no a una opinion de "buena practica" inventada aparte.

Controles Baseline (el campo debe estar ausente o en su valor seguro):
  hostnetwork, hostpid, hostipc, privileged, capsadd, hostpath, hostport

Controles Restricted (ademas de Baseline; el campo debe estar presente y en
su valor exigido):
  privesc, nonroot, seccomp, capsdropall

Deliberadamente fuera de alcance (documentado, no fingido como cubierto):
HostProcess (solo Windows), AppArmor, SELinux, procMount, Sysctls, Host
Probes/Lifecycle Hooks host field, Volume Types — cada uno requiere leer una
lista de valores permitidos mas larga o codigo especifico de plataforma que
un heuristico de texto no puede aplicar con la misma confianza que las 11
reglas de arriba.

Sin dependencias externas: Python no trae un parser YAML en su libreria
estandar, asi que esto NO es un parser YAML real. Es un escaneo del texto
completo del documento buscando los nombres de campo exactos de la tabla
oficial (que son unicos dentro de un manifiesto de Pod/Deployment/etc. y no
tienen otro significado legitimo), mas un extractor liviano de listas YAML
por indentacion para `add:`/`drop:` bajo `capabilities:`. No distingue un
manifiesto con multiples documentos (`---`) recurso por recurso: reporta
sobre el archivo completo. Por eso cada hit imprime la linea exacta.

Exit codes (convencion KDD):
  0  la propiedad se cumple
  1  no se cumple
  2  no se pudo verificar

Uso:
    python k8s_checks.py --rule privileged <manifiesto.yaml> [...]
    python k8s_checks.py --list
"""
import argparse
import json
import re
import sys
from pathlib import Path

__all__ = [
    "check_hostnetwork", "check_hostpid", "check_hostipc", "check_privileged",
    "check_capsadd", "check_hostpath", "check_hostport", "check_privesc",
    "check_nonroot", "check_seccomp", "check_capsdropall",
]

BASELINE_CAPS = {
    "AUDIT_WRITE", "CHOWN", "DAC_OVERRIDE", "FOWNER", "FSETID", "KILL", "MKNOD",
    "NET_BIND_SERVICE", "SETFCAP", "SETGID", "SETPCAP", "SETUID", "SYS_CHROOT",
}


def _hit(path, lineno, line, detail):
    return {"file": str(path), "line": lineno, "text": line.strip(), "detail": detail}


def _read(path):
    return Path(path).read_text(encoding="utf-8").splitlines()


def _scan_true(path, key, detail):
    """Falla si `key: true` aparece en el documento (control Baseline: debe estar ausente o false)."""
    hits = []
    pattern = re.compile(rf"(?<![.\w$]){re.escape(key)}\s*:\s*true\b")
    for lineno, line in enumerate(_read(path), start=1):
        if pattern.search(line):
            hits.append(_hit(path, lineno, line, detail))
    return hits


def _scan_present(path, pattern, detail):
    """Falla si el patron aparece en el documento (control Baseline: la clave debe estar ausente)."""
    hits = []
    rx = re.compile(pattern)
    for lineno, line in enumerate(_read(path), start=1):
        if rx.search(line):
            hits.append(_hit(path, lineno, line, detail))
    return hits


def _scan_required_value(path, key, required, detail):
    """Falla si la clave nunca aparece con el valor exigido (control Restricted: debe estar presente y en ese valor)."""
    pattern = re.compile(rf"(?<![.\w$]){re.escape(key)}\s*:\s*{re.escape(required)}\b")
    lines = _read(path)
    for line in lines:
        if pattern.search(line):
            return []
    return [{"file": str(path), "line": None, "text": None,
              "detail": f"'{key}: {required}' no aparece en el documento (Restricted lo exige explicito)"}]


def _yaml_list_items(lines, start_idx, base_indent):
    """Extrae los items '- ITEM' de una lista YAML que empieza despues de start_idx,
    indentados mas que base_indent, hasta que la indentacion vuelve a <= base_indent."""
    items = []
    for line in lines[start_idx + 1:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= base_indent:
            break
        m = re.match(r"-\s*([A-Za-z_][\w]*)", line.strip())
        if m:
            items.append(m.group(1))
        else:
            break
    return items


def check_hostnetwork(path):
    return _scan_true(path, "hostNetwork", "spec.hostNetwork debe estar ausente o en false (Baseline: Host Namespaces)")


def check_hostpid(path):
    return _scan_true(path, "hostPID", "spec.hostPID debe estar ausente o en false (Baseline: Host Namespaces)")


def check_hostipc(path):
    return _scan_true(path, "hostIPC", "spec.hostIPC debe estar ausente o en false (Baseline: Host Namespaces)")


def check_privileged(path):
    return _scan_true(path, "privileged", "securityContext.privileged debe estar ausente o en false (Baseline: Privileged Containers)")


def check_hostpath(path):
    return _scan_present(path, r"(?<![.\w$])hostPath\s*:", "volumes[*].hostPath debe estar ausente (Baseline: HostPath Volumes)")


def check_hostport(path):
    hits = []
    pattern = re.compile(r"(?<![.\w$])hostPort\s*:\s*(\d+)")
    for lineno, line in enumerate(_read(path), start=1):
        m = pattern.search(line)
        if m and m.group(1) != "0":
            hits.append(_hit(path, lineno, line, "containers[*].ports[*].hostPort debe estar ausente o en 0 (Baseline: Host Ports)"))
    return hits


def check_capsadd(path):
    hits = []
    lines = _read(path)
    for idx, line in enumerate(lines):
        if re.match(r"^\s*add\s*:\s*$", line) and "capabilities" not in line:
            indent = len(line) - len(line.lstrip(" "))
            for cap in _yaml_list_items(lines, idx, indent):
                if cap.upper() not in BASELINE_CAPS:
                    hits.append(_hit(path, idx + 1, line, f"capability '{cap}' agregada fuera de la lista permitida por Baseline ({', '.join(sorted(BASELINE_CAPS))})"))
        m = re.match(r"^\s*add\s*:\s*\[(.*)\]\s*$", line)
        if m:
            for cap in [c.strip().strip("'\"") for c in m.group(1).split(",") if c.strip()]:
                if cap.upper() not in BASELINE_CAPS:
                    hits.append(_hit(path, idx + 1, line, f"capability '{cap}' agregada fuera de la lista permitida por Baseline"))
    return hits


def check_privesc(path):
    hits = _scan_true(path, "allowPrivilegeEscalation", "allowPrivilegeEscalation debe ser false explicito (Restricted: Privilege Escalation)")
    if hits:
        return hits
    return _scan_required_value(path, "allowPrivilegeEscalation", "false", "Restricted exige allowPrivilegeEscalation: false explicito")


def check_nonroot(path):
    return _scan_required_value(path, "runAsNonRoot", "true", "Restricted exige runAsNonRoot: true explicito (Running as Non-root)")


def check_seccomp(path):
    lines = _read(path)
    for lineno, line in enumerate(lines, start=1):
        if re.search(r"(?<![.\w$])type\s*:\s*(RuntimeDefault|Localhost)\b", line):
            for back in lines[max(0, lineno - 4):lineno - 1]:
                if "seccompProfile" in back:
                    return []
    return [{"file": str(path), "line": None, "text": None,
              "detail": "seccompProfile.type con RuntimeDefault o Localhost no aparece (Restricted exige que Seccomp este configurado)"}]


def check_capsdropall(path):
    lines = _read(path)
    for idx, line in enumerate(lines):
        if re.match(r"^\s*drop\s*:\s*$", line):
            indent = len(line) - len(line.lstrip(" "))
            if "ALL" in _yaml_list_items(lines, idx, indent):
                return []
        if re.match(r"^\s*drop\s*:\s*\[(.*ALL.*)\]\s*$", line):
            return []
    return [{"file": str(path), "line": None, "text": None,
              "detail": "capabilities.drop con ALL no aparece (Restricted exige soltar todas las capabilities por defecto)"}]


RULES = {
    "hostnetwork": check_hostnetwork,
    "hostpid": check_hostpid,
    "hostipc": check_hostipc,
    "privileged": check_privileged,
    "capsadd": check_capsadd,
    "hostpath": check_hostpath,
    "hostport": check_hostport,
    "privesc": check_privesc,
    "nonroot": check_nonroot,
    "seccomp": check_seccomp,
    "capsdropall": check_capsdropall,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule", choices=sorted(RULES))
    parser.add_argument("--list", action="store_true")
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    if args.list:
        print("\n".join(sorted(RULES)))
        return 0

    if not args.rule or not args.files:
        parser.error("--rule y al menos un archivo son requeridos (o usa --list)")

    check = RULES[args.rule]
    all_hits = []
    unverifiable = []
    for f in args.files:
        p = Path(f)
        if not p.exists() or p.suffix not in (".yaml", ".yml"):
            unverifiable.append(str(p))
            continue
        all_hits.extend(check(p))

    result = {
        "rule": args.rule,
        "status": "NO VERIFICABLE" if (unverifiable and len(unverifiable) == len(args.files)) else ("FAILED" if all_hits else "PASSED"),
        "hits": all_hits,
        "unverifiable_files": unverifiable,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["status"] == "NO VERIFICABLE":
        return 2
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main())
