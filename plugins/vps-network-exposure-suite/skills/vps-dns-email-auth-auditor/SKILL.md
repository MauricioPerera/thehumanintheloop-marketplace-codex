---
name: vps-dns-email-auth-auditor
description: Audita zonas DNS, DNSSEC, propagación y autenticación de correo SPF, DKIM y DMARC sin modificar proveedores ni registros.
---
# VPS DNS & Email Auth Auditor

Audita dominios autorizados y entrega evidencia reproducible sobre DNS y autenticación de correo. Confirma dominio, proveedor esperado, resolver, región y alcance antes de consultar.

## Procedimiento

1. Consulta `A`, `AAAA`, `CNAME`, `NS`, `MX`, `TXT`, `CAA` y `SOA` con `dig`/resolver autorizado, separando respuesta autoritativa de caché.
2. Comprueba DNSSEC con `DS`, `DNSKEY`, `RRSIG`, estado `AD` y errores de validación; no inventa seguridad cuando el resolver no valida.
3. Evalúa SPF: existencia de un único registro, mecanismos, `all`, redirects, lookups aproximados y riesgos de autorización demasiado amplia.
4. Evalúa DKIM solo para selectores proporcionados o descubiertos de forma autorizada; verifica clave pública, tipo, longitud observable y coherencia del selector.
5. Evalúa DMARC: política, `rua`/`ruf` redactados, `pct`, `adkim`, `aspf`, subdominios y alineación con SPF/DKIM. No envía correos ni prueba credenciales.
6. Reporta propagación, TTL, inconsistencias entre autoritativos y plan de remediación con proveedor, cambio mínimo, ventana y rollback.

## Salida y límites

Incluye timestamp UTC, dominio, resolver, registro, valor redactado, evidencia, severidad y limitaciones. No cambia DNS, DNSSEC, SPF, DKIM, DMARC, nameservers ni credenciales; cualquier gestión requiere autorización separada.
