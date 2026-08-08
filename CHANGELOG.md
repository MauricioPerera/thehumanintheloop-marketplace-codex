# Changelog

## Unreleased

- `n8n-workflow-manager`, `n8n-credential-manager`: correccion de documentacion (SKILL.md, sin cambio de version ni comportamiento). El caveat de `transfer` decia "requiere licencia" -- impreciso. Confirmado via `search_projects` del MCP oficial de n8n (`n8n-workflow-builder`) que el campo real es `teamProjectsEnabled: false` a nivel instancia, no un tema de permisos de la API key. Ademas, `n8n-workflow-manager` ahora recomienda `n8n-workflow-builder` para `update` cuando el usuario tenga token MCP, porque sus operaciones atomicas por nodo son mas seguras que el reemplazo completo que fuerza el `PUT` de la REST API.

- `n8n-workflow-builder` (N8N Workflow Builder): nuevo plugin (categoria Developer Tools). Cliente JSON-RPC generico (sin dependencias externas) para el MCP oficial de n8n (`/mcp-server/http`), protocolo y token de auth distintos de la REST API (`N8N_MCP_TOKEN`, audiencia `mcp-server-api`, vs `N8N_API_KEY`, audiencia `public-api`). Expone las 33 tools del servidor via `list-tools`/`call --tool <nombre> --args-file <json>`, con dry-run por defecto en las mutantes (creacion/actualizacion de workflows, publish/archive, ejecutar, tablas de datos) y `--apply` explicito para aplicar. `update_workflow` usa operaciones atomicas (`addNode`, `updateNodeParameters`, `renameNode`, etc.) en vez del reemplazo completo que fuerza la REST API. `test_workflow` se clasifica como mutante pese al nombre: nodos `Execute Command` y lectura/escritura de archivos corren de verdad incluso en modo test, solo se simulan credenciales/HTTP/triggers. Verificado stateless (sin handshake `initialize` previo a `tools/call`). Encontro y corrigio un bug real: en Windows, `stdout` es `cp1252` por defecto y crashea con los caracteres Unicode que trae `get_sdk_reference`; se fuerza UTF-8. Verificado end-to-end contra una instancia real: `list-tools`, `search_nodes`, `get_sdk_reference`, `validate_workflow` (codigo valido confirmado), `create_workflow_from_code` (workflow creado de verdad), `update_workflow` con `renameNode` (primer intento fallo por nombre de campo incorrecto -`nodeName` en vez de `oldName`-, error real propagado correctamente, corregido y confirmado), `get_workflow_history` (2 versiones reales). Limpieza final via `n8n-workflow-manager` (REST API), porque este MCP no tiene tool de borrado definitivo, solo `archive_workflow`.

- `n8n-community-package-manager` (N8N Community Package Manager): nuevo plugin (categoria Security & Privacy). Gestiona `list`/`install`/`update`/`uninstall` de paquetes de nodos de comunidad via REST API. La verificacion contra la lista vetada de n8n esta activa por defecto (`--allow-unverified` para saltarla explicitamente); dry-run por defecto, `uninstall` exige repetir el nombre exacto del paquete. Verificado end-to-end contra una instancia real: `install` sin `--allow-unverified` bloqueado correctamente por la lista vetada (confirma que la barrera funciona), ciclo completo `install --allow-unverified` -> `list` -> `uninstall` con un paquete real y publicamente verificable (`n8n-nodes-serpapi`), instancia confirmada exactamente igual que antes al terminar.
- `n8n-credential-manager` (N8N Credential Manager): nuevo plugin (categoria Security & Privacy). Gestiona `schema`/`create`/`rename`/`rotate`/`delete`/`test`/`transfer` de credenciales via REST API. El valor del secreto (`data`) se lee siempre de un archivo JSON local, nunca de un argumento de CLI ni del chat, y el script solo imprime los nombres de los campos, nunca los valores. `rename` no toca el secreto; `rotate` sí, con reemplazo completo por defecto o merge parcial opcional (`--partial`). `delete` exige `--confirm-name` verificado contra el nombre real. Verificado end-to-end contra una instancia real: create/rename/rotate/delete completos sobre una credencial descartable sin exponer ningun valor; `schema` y `test` verificados en formato de request/respuesta (`test` documentado con un caveat real: puede fallar con error interno de n8n segun el tipo de credencial y los nodos disponibles en la instancia, no es bug del script); `transfer` verificado en formato de request y manejo de error (404 ante proyecto inexistente), no en una transferencia exitosa real por limitacion de licencia de la instancia de prueba (Community/single-project, sin soporte para multiples proyectos).
- `n8n-workflow-manager` (N8N Workflow Manager): version 0.1.0 -> 0.2.0. Agrega `archive`/`unarchive` (soft-delete idempotente, mismo patron que activate/deactivate) y `transfer` (mover a otro proyecto). Verificado end-to-end contra una instancia real: archive/unarchive completos con idempotencia confirmada; `transfer` verificado en formato de request y manejo de error (404 ante proyecto inexistente), no en una transferencia exitosa real por la misma limitacion de licencia mencionada arriba (`POST /projects` tambien bloqueado por la misma licencia, asi que no hay forma de crear un segundo proyecto de prueba en esta instancia).
- `n8n-workflow-manager` (N8N Workflow Manager): nuevo plugin (categoria Developer Tools, separado de `n8n-workflow-auditor` que sigue siendo solo lectura). Gestiona `create`/`activate`/`deactivate`/`update`/`delete` de workflows via REST API con dry-run por defecto (requiere `--apply` explicito para mutar) y `update` siempre basado en get->merge->diff (nunca acepta un JSON parcial directo, porque `PUT /workflows/{id}` en n8n es reemplazo completo). `delete` exige `--confirm-name` verificado contra el nombre real del workflow. Verificado end-to-end contra una instancia real (create, activate, update con diff, deactivate, delete, mas los casos de error: nombre de confirmacion incorrecto, campo no editable, workflow sin trigger valido para activar). Encontro y corrigio dos comportamientos reales de la API no documentados igual en su OpenAPI: `PUT` rechaza campos fuera de un allowlist estricto (el `GET` real trae campos internos como `sourceWorkflowId`/`activeVersionId`/`versionCounter` no documentados) y rechaza `description: null` aunque el propio `GET` lo devuelva asi.
- `n8n-workflow-auditor` (N8N Workflow Auditor): version 0.5.0 -> 0.6.0. Agrega `--credentials`: inventario via `/api/v1/credentials` (nombre, tipo, fecha, con que proyecto esta compartida y con que rol). El endpoint nunca devuelve valores de credenciales por diseno de n8n, y requiere que la API key sea de owner/admin (scope `credential:list`). Complementa sin duplicar el "Credentials Risk Report" de `--native-audit` (ese detecta riesgo, este es inventario plano). Verificado contra una instancia real (16 credenciales, agrupadas por tipo, sin exponer valores).
- `n8n-workflow-auditor` (N8N Workflow Auditor): version 0.4.0 -> 0.5.0. Agrega `--executions`: pagina `/api/v1/executions` y agrega por workflow total/OK/error/tasa de error/ultimo status/ultimo error, cruzando nombres via `/api/v1/workflows`. Filtrable con `--status` y `--workflow-id` (reusa el flag existente). El endpoint no soporta filtro de fecha y una instancia real puede tener millones de ejecuciones historicas, asi que el script trae como maximo `--max-executions` (default 500, ajustable) y nunca hace un crawl completo por defecto; marca `truncated: true` cuando corta antes de agotar el cursor, sin ocultarlo. Verificado contra una instancia real con 1.5M+ ejecuciones historicas (`--status error` con 500 de muestra, `--workflow-id` con cero ejecuciones confirmado contra la API directa, validacion de status invalido).
- `n8n-workflow-auditor` (N8N Workflow Auditor): version 0.3.0 -> 0.4.0. Agrega `--native-audit`: envuelve el endpoint nativo `POST /api/v1/audit` de n8n (credenciales sin usar, nodos riesgosos/comunitarios, webhooks desprotegidos, instancia desactualizada), con filtros `--audit-categories` y `--days-abandoned`. Es la unica llamada no-GET del script, pero es un generador de reporte de solo lectura (no muta nada). Verificado contra una instancia real. Tambien endurece el manejo de errores HTTP (incluye el cuerpo de la respuesta en el mensaje de error) y agrega el `securityAudit:generate` scope como requisito documentado.
- `n8n-workflow-auditor` (N8N Workflow Auditor): version 0.2.0 -> 0.3.0. Agrega `--export-dir` para descargar cada workflow (JSON completo tal cual la API) a una carpeta local, sin requests adicionales (reusa lo ya traido por `--summary`/auditoria). Sigue siendo estrictamente lectura: no hace `POST`/`PUT`/`PATCH`/`DELETE`. Verificado contra una instancia real (992 workflows exportados en ~9s).
- `n8n-workflow-auditor` (N8N Workflow Auditor): version 0.1.0 -> 0.2.0. Elimina el GET redundante por workflow (la lista ya trae nodes/connections/settings completos), agrega `--summary` para inventario rápido (total/activos/inactivos sin correr las 7 reglas) y agrega `User-Agent` explícito para evitar bloqueos de WAF (Cloudflare Error 1010) en instancias reales. Verificado end-to-end contra una instancia n8n real con ~1000 workflows.
- `n8n-workflow-auditor` (N8N Workflow Auditor): nuevo plugin, audita workflows de n8n vía REST API en modo lectura (webhooks sin autenticación, credenciales hardcodeadas, nodos de alto riesgo, manejo de errores, reintentos, nodos huérfanos, trigger alcanzable).
- `kdd-dockerfile` (KDD Dockerfile Checker): nuevo plugin, verifica 11 reglas duras de Dockerfile best practices extraidas con Knowledge-Driven Development.
- `k8s-manifest-auditor` (K8s Manifest Auditor): nuevo plugin, audita manifiestos Kubernetes contra los Pod Security Standards oficiales (Baseline + Restricted).
- `kdd-typescript` (KDD TypeScript Checker): nuevo plugin, verifica 17 reglas duras del Google TypeScript Style Guide extraidas con Knowledge-Driven Development.
- `terraform-plan-auditor` (Terraform Plan Auditor): nuevo plugin, audita planes de Terraform antes de aplicarlos sin ejecutar apply/destroy.
- `vps-backup-suite`, `vps-container-security-suite`, `vps-network-exposure-suite`, `vps-observability-suite`, `vps-deployment-readiness-suite`, `vps-incident-security-suite`: version 0.1.0 -> 0.2.0 (estructura multi-skill instalada y verificada end-to-end tras la consolidación).
- Tabla de migración para los 21 plugins `vps-*` consolidados en 6 plugins multi-skill: ver [`README.md#migración-de-plugins-vps-consolidados`](README.md#migración-de-plugins-vps-consolidados).
- Consolidacion de 21 plugins `vps-*` de superficie unica en 6 plugins multi-skill (vps-ssh-manager queda standalone).
- `vps-backup-suite` (VPS Backup Suite): consolida 3 plugins VPS anteriores en un plugin multi-skill (vps-backup-job-monitor, vps-backup-manager, vps-backup-restore-verifier).
- `vps-container-security-suite` (VPS Container Security Suite): consolida 5 plugins VPS anteriores en un plugin multi-skill (vps-container-security-auditor, vps-docker-network-isolation-auditor, vps-docker-resource-limits-auditor, vps-image-provenance-auditor, vps-image-vulnerability-sbom-auditor).
- `vps-network-exposure-suite` (VPS Network Exposure Suite): consolida 4 plugins VPS anteriores en un plugin multi-skill (vps-dns-email-auth-auditor, vps-network-diagnostics, vps-service-exposure-auditor, vps-tls-renewal-monitor).
- `vps-observability-suite` (VPS Observability Suite): consolida 4 plugins VPS anteriores en un plugin multi-skill (vps-cost-capacity-auditor, vps-observability-auditor, vps-resource-monitor, vps-log-retention-auditor).
- `vps-deployment-readiness-suite` (VPS Deployment Readiness Suite): consolida 3 plugins VPS anteriores en un plugin multi-skill (vps-configuration-drift-auditor, vps-deployment-readiness-auditor, vps-dependency-topology-auditor).
- `vps-incident-security-suite` (VPS Incident & Security Suite): consolida 2 plugins VPS anteriores en un plugin multi-skill (vps-incident-responder, vps-security-auditor).

- `github-security-suite`, `github-cicd-governance`, `github-repo-governance`, `github-collab-activity`, `github-branch-release-ops`, `github-org-lifecycle`: version 0.1.0 -> 0.2.0 (validador de scripts restaurado y estructura multi-skill instalada y verificada end-to-end tras la consolidación).
- Tabla de migración para los 43 plugins `github-*` consolidados en 6 plugins multi-skill: ver [`README.md#migración-de-plugins-github-consolidados`](README.md#migración-de-plugins-github-consolidados).
- Consolidacion de 43 plugins `github-*` de superficie unica en 6 plugins multi-skill (misma cobertura, menos entradas instalables).
- `github-security-suite` (GitHub Security Suite): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-security-manager, github-code-scanning-manager, github-secret-scanning-manager, github-security-advisory-manager, github-dependency-review-manager, github-dependabot-manager, github-private-reporting-manager, github-secret-manager).
- `github-cicd-governance` (GitHub CI/CD Governance): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-action-permissions-manager, github-checks-manager, github-environment-manager, github-merge-queue-manager, github-oidc-manager, github-runner-manager, github-variable-manager, github-workflow-dispatch-manager).
- `github-repo-governance` (GitHub Repository Governance): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-repository-manager, github-codeowners-manager, github-template-manager, github-label-manager, github-milestone-manager, github-funding-manager, github-pages-manager, github-ruleset-manager).
- `github-collab-activity` (GitHub Collaboration & Activity): consolida 7 plugins GitHub anteriores en un plugin multi-skill (github-discussion-manager, github-notifications-manager, github-contributor-manager, github-team-manager, github-activity-manager, github-traffic-manager, github-audit-log-manager).
- `github-branch-release-ops` (GitHub Branch & Release Ops): consolida 5 plugins GitHub anteriores en un plugin multi-skill (github-branch-manager, github-commit-signing-manager, github-deployment-manager, github-merge-conflict-manager, github-package-manager).
- `github-org-lifecycle` (GitHub Org & Lifecycle): consolida 7 plugins GitHub anteriores en un plugin multi-skill (github-organization-settings-manager, github-archive-manager, github-migration-manager, github-fork-manager, github-webhook-manager, github-api-manager, github-project-manager).

- Documentación de contribución para plugins y Design System Analyses.
- Validación automática de metadata SEO, JSON-LD y sitemap para previews.
- `cv-job-tailor`: adaptación de CVs a ofertas con trazabilidad y validadores anti-fabricación.
- `commercial-proposal-builder`: propuestas comerciales basadas en requerimientos con control de alcance, precios y supuestos.
- `rfp-response-builder`: respuestas de RFP y licitaciones con matriz de cumplimiento, evidencia y pendientes.
- `github-issue-manager`: gestión de Issues con `gh` CLI y confirmación antes de acciones mutables.
- `github-pr-manager`: preparación y revisión de Pull Requests con checklist y evidencia.
- `github-release-manager`: preparación de releases, tags y notas de versión con `gh` CLI.
- `github-actions-manager`: diagnóstico de workflows, ejecuciones y logs de GitHub Actions.
- `github-project-manager`: organización de Projects y tareas con plan de mutaciones trazable.
- `github-code-search`: búsqueda reproducible de código, commits, Issues y Pull Requests.
- `github-security-manager`: auditoría de alertas de seguridad y planes de remediación.
- `github-dependabot-manager`: revisión de alertas y actualizaciones Dependabot.
- `github-notifications-manager`: digest y triage de notificaciones de GitHub.
- `github-discussion-manager`: gestión de Discussions con respuestas trazables.
- `github-label-manager`: taxonomía y mantenimiento de labels con plan previo.
- `github-repository-manager`: inspección y configuración de repositorios con confirmación.
- `github-milestone-manager`: planificación de hitos con objetivos, fechas y trazabilidad.
- `github-branch-manager`: gestión segura de ramas y operaciones remotas.
- `github-template-manager`: validación y mantenimiento de templates de Issues y PRs.
- `github-api-manager`: consultas GitHub API con controles GET-first y evidencia estructurada.
- `github-codeowners-manager`: validación de CODEOWNERS, ownership y cobertura.
- `github-contributor-manager`: análisis de contribuciones y planes de reviewers.
- `github-activity-manager`: reportes temporales de actividad con evidencia y límites.
- `github-traffic-manager`: análisis de tráfico de repositorios con retención y agregación explícitas.
- `github-webhook-manager`: planes y auditoría de webhooks con secretos redactados.
- `github-environment-manager`: auditoría y planes de environments y gates de despliegue.
- `github-variable-manager`: auditoría de variables sin lectura de valores secretos.
- `github-package-manager`: revisión de paquetes, versiones y planes de retención.
- `github-secret-manager`: auditoría de secretos con valores redactados y planes de rotación.
- `github-ruleset-manager`: auditoría y diseño de reglasets con bypass, checks y rollback.
- `github-checks-manager`: análisis de checks, annotations y resultados de CI con evidencia.
- `github-audit-log-manager`: análisis de actividad administrativa con filtros y datos redactados.
- `github-runner-manager`: auditoría de runners, labels, alcance y aislamiento.
- `github-deployment-manager`: análisis operativo de despliegues y planes de rollback.
- `github-team-manager`: auditoría de equipos, membresías y permisos efectivos.
- `github-merge-queue-manager`: diagnóstico de merge queues, checks y cuellos de botella.
- `github-fork-manager`: auditoría de forks, sincronización y políticas de visibilidad.
- `github-commit-signing-manager`: auditoría de firmas, estados verificados y cobertura.
- `github-migration-manager`: planes de migración con inventario, validación y rollback.
- `github-archive-manager`: evaluación de archivado, retención y recuperación.
- `github-code-scanning-manager`: auditoría de alertas, severidad, reglas y remediación.
- `github-secret-scanning-manager`: análisis seguro de alertas con valores siempre redactados.
- `github-security-advisory-manager`: borradores de advisories con mitigación y divulgación responsable.
- `github-dependency-review-manager`: revisión de dependencias nuevas, licencias y supply chain.
- `github-private-reporting-manager`: reportes privados con evidencia mínima y segura.
- `github-organization-settings-manager`: auditoría de políticas globales y permisos de organización.
- `github-pages-manager`: auditoría de fuentes, dominios y despliegues de GitHub Pages.
- `github-funding-manager`: revisión de FUNDING.yml, sponsors y enlaces públicos.
- `github-workflow-dispatch-manager`: preparación segura de ejecuciones manuales con inputs.
- `github-oidc-manager`: auditoría de subjects, audiences y trust de proveedores cloud.
- `github-action-permissions-manager`: revisión de scopes y mínimo privilegio de GITHUB_TOKEN.
- `github-merge-conflict-manager`: diagnóstico de conflictos y planes de resolución revisables.
- `mercadopago-payment-manager`: contrato y validador para enlaces Checkout Preference con confirmación previa.

## 2026-08-02

- Marketplace dual para Claude Code y Codex.
- Catálogo público con 16 plugins y ocho categorías.
- GitHub Page navegable con búsqueda, filtros, instalación y previews embebidos.
- Publicación de análisis KDD, Mercado Libre y TheHumanInTheLoop Marketplace.
- Licencia MIT.
