---
name: secrets-exposure-auditor
description: Detecta indicios de secretos expuestos en un VPS sin mostrar valores ni copiar credenciales.
---
# Secrets Exposure Auditor
Busca nombres, permisos, patrones y referencias en rutas explícitamente autorizadas, Compose, procesos y logs; devuelve ubicación redactada, tipo y severidad, nunca el valor. No imprime `.env`, no consulta secretos del gestor ni modifica archivos; toda remediación requiere backup y confirmación.
