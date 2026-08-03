# Política de seguridad

## Alcance

Esta política cubre los plugins, skills, scripts de validación, workflows de GitHub Actions y previews publicados en este repositorio.

Antes de instalar o ejecutar un plugin, revisa su código, sus skills, sus scripts y cualquier integración externa. No incluyas secretos, tokens ni datos personales en prompts, issues o pull requests.

## Reportar una vulnerabilidad

No publiques vulnerabilidades explotables en un issue público. Utiliza la función **Private vulnerability reporting** de GitHub si está habilitada o contacta al mantenedor mediante su perfil: [Mauricio Perera](https://github.com/MauricioPerera).

Incluye, cuando sea posible:

- plugin, archivo y versión afectados;
- pasos mínimos para reproducir el problema;
- impacto observado y alcance potencial;
- evidencia sin credenciales ni información sensible;
- mitigación propuesta, si existe.

## Prácticas del marketplace

- Las validaciones automáticas no sustituyen una revisión humana de seguridad.
- Los plugins no deben exfiltrar datos, leer secretos sin autorización ni ejecutar acciones externas no documentadas.
- Las fuentes y activos de terceros deben conservar su atribución y condiciones de uso.
- Los cambios que afecten workflows, permisos, scripts o integraciones requieren revisión explícita.
- Las actualizaciones de GitHub Actions propuestas por Dependabot deben revisarse antes de incorporarse a `main`.
