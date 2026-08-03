---
name: mercadopago-payment-manager
description: Prepara enlaces de pago de Mercado Pago mediante Checkout Preference. Úsala para validar artículos, cantidades, moneda, precios, referencias, callbacks y vencimientos antes de crear un enlace o llamar a la API.
---

# Mercado Pago Payment Manager

Este plugin convierte una solicitud comercial en un plan seguro de Checkout Preference. No es el nodo n8n original ni pretende ser oficial de Mercado Pago: usa un contrato propio y reutiliza únicamente conceptos públicos de la API. Nunca copies Access Tokens a prompts, archivos, logs o respuestas.

## Flujo obligatorio

1. Recoge país/site, artículos, `title`, `quantity`, `currency_id` y `unit_price`.
2. Valida que exista al menos un artículo, cantidades positivas, precios mayores que cero y moneda explícita.
3. Revisa `external_reference`, URLs HTTPS de notificación y `back_urls` de éxito, pendiente y fallo.
4. Revisa expiración, `auto_return`, `binary_mode`, impuestos y requisitos del negocio; declara supuestos.
5. Genera una vista previa JSON sin credenciales y ejecuta:

```bash
python plugins/mercadopago-payment-manager/scripts/validate_payment_plan.py --input payment-plan.md --json payment-report.json
```

6. Muestra endpoint, método, campos y consecuencias. Solicita confirmación explícita antes de ejecutar una petición `POST` o compartir el enlace resultante.

## Seguridad y operación

Usa `MERCADOPAGO_ACCESS_TOKEN` desde un gestor de secretos o variable de entorno. No lo imprimas ni lo incluyas en una URL. Requiere HTTPS para `notification_url` y callbacks. Guarda solo el identificador de la preferencia y la referencia interna; no almacenes datos de tarjeta.

## Resultado

Entrega: resumen comercial, payload saneado, errores y advertencias, estado del validador, comando o petición propuesta, pasos de confirmación y plan de verificación posterior. Distingue siempre entre `plan preparado` y `enlace creado`.
