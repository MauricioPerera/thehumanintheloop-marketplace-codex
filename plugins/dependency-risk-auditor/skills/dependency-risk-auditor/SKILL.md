---
name: dependency-risk-auditor
description: Detecta dependencias obsoletas, vulnerables, sin lockfile o con procedencia incierta. Úsala antes de publicar paquetes, desplegar servicios o actualizar runtimes.
---
# Dependency Risk Auditor

Analiza manifests y lockfiles sin instalar paquetes ni ejecutar scripts no confiables.

## Flujo
1. Ejecuta `python plugins/dependency-risk-auditor/scripts/check_dependencies.py .`.
2. Comprueba lockfiles, rangos abiertos, dependencias directas y scripts de instalación.
3. Usa el gestor o scanner de seguridad disponible para vulnerabilidades actuales.
4. Clasifica riesgo, alcance y acción de actualización.

## Salida
Entrega dependencia, versión, origen, riesgo, evidencia y recomendación de actualización.
