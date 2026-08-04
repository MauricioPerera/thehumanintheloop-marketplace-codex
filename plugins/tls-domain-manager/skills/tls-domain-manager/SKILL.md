---
name: tls-domain-manager
description: Audita dominios, certificados TLS, SNI, redirecciones y reverse proxies de un VPS sin renovar ni modificar configuración.
---
# TLS Domain Manager
Usa `openssl s_client` y lecturas de Nginx/Traefik sin imprimir secretos. Verifica expiración, cadena, SAN, protocolo, SNI, HTTP→HTTPS y puertos públicos. No renueva certificados ni edita proxy; cualquier cambio debe incluir dominio exacto, impacto, backup y confirmación.
