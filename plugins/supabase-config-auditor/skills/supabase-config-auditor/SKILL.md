---
name: supabase-config-auditor
description: Audita configuración de Supabase self-hosted, Docker Compose, variables requeridas y exposición de servicios sin revelar valores secretos.
---

# Supabase Config Auditor

Usa esta skill para revisar configuración, drift entre Compose y `.env`, exposición de puertos, permisos de archivos y riesgos de secretos.

## Reglas

- Solo enumera nombres de variables, nunca valores.
- Redacta tokens, contraseñas, JWTs, URLs con credenciales, certificados y claves privadas.
- Compara nombres esperados y presentes, tipos de servicio, puertos publicados, volúmenes y permisos.
- No edites `.env`, Compose, proxies ni firewall durante una auditoría.
- Marca como `WARNING` cualquier valor no verificable sin convertirlo en un secreto visible.

## Flujo

1. Identifica el proyecto Compose y archivos de configuración sin imprimirlos completos.
2. Lista nombres de variables con `awk`, PowerShell o un parser seguro.
3. Inspecciona puertos y mounts con formatos explícitos y sin `Config.Env`.
4. Reporta exposición, drift, permisos y variables ausentes.
5. Para remediar, genera un plan separado y pide confirmación.

Valida el reporte con `python scripts/validate_env_report.py --report <archivo>`.
