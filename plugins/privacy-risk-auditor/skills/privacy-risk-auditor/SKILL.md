---
name: privacy-risk-auditor
description: Detecta PII, secretos, credenciales y riesgos de privacidad en código, documentos y configuraciones. Úsala antes de compartir, publicar o desplegar un repositorio.
---
# Privacy Risk Auditor

Busca señales de riesgo sin exponer secretos encontrados. Redacta valores sensibles en el informe.

## Flujo
1. Ejecuta `python plugins/privacy-risk-auditor/scripts/scan_privacy.py .`.
2. Clasifica credenciales, PII, datos de producción, logs y configuraciones peligrosas.
3. Comprueba `.gitignore`, historial si fue solicitado y documentación de retención.
4. Recomienda revocar, rotar o eliminar secretos; no los copies al reporte.

## Salida
Entrega estado, archivo, línea aproximada, tipo de riesgo, severidad y corrección segura.
