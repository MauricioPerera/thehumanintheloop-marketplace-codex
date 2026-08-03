---
name: commercial-proposal-builder
description: Redacta propuestas comerciales basadas en requerimientos reales del cliente, capacidades autorizadas, precios y plazos proporcionados por el usuario. Usala cuando el usuario pida crear, estructurar, responder o validar una propuesta comercial, RFP, SOW o oferta de servicios.
---

# Commercial Proposal Builder

Construye propuestas comerciales claras y trazables a partir de requerimientos del cliente y datos autorizados de la empresa. No inventes capacidades, precios, plazos, clientes, certificaciones, casos de éxito ni garantías.

## Flujo obligatorio

1. Recibir los requerimientos del cliente, el contexto de la empresa y la información comercial autorizada.
2. Separar hechos, restricciones, supuestos y preguntas abiertas.
3. Construir una matriz requisito → respuesta propuesta → evidencia o pendiente.
4. Redactar una propuesta con alcance incluido, exclusiones, entregables, cronograma, inversión, supuestos, riesgos y próximos pasos.
5. Mantener precios, descuentos, impuestos, monedas y plazos exactamente como fueron proporcionados.
6. Ejecutar el validador:

   ```powershell
   python plugins/commercial-proposal-builder/scripts/validate_commercial_proposal.py --requirements requisitos.md --source empresa.md --output propuesta.md --json proposal-report.json
   ```

7. Entregar la propuesta, la matriz de cobertura, las preguntas pendientes y el reporte `PASSED` o `FAILED`.

## Reglas de integridad comercial

- No presentar como capacidad propia algo que solo aparece como requerimiento del cliente.
- No crear precios, porcentajes, descuentos, fechas, duraciones ni condiciones legales.
- No afirmar que existen clientes, resultados o certificaciones sin una fuente autorizada.
- Separar claramente `INCLUIDO`, `EXCLUIDO`, `SUPUESTO` y `REQUIERE CONFIRMACIÓN`.
- No usar garantías absolutas como "sin riesgo", "garantizado" o "100% asegurado".
- Marcar cualquier requisito sin respuesta como `OPEN ITEM`.

## Estructura mínima

Usar estos encabezados, adaptando el idioma:

1. Resumen ejecutivo
2. Entendimiento de los requerimientos
3. Solución propuesta
4. Alcance y exclusiones
5. Entregables
6. Cronograma
7. Inversión y condiciones
8. Supuestos, riesgos y preguntas abiertas
9. Próximos pasos

## Principios de redacción

- Responder cada requerimiento con lenguaje concreto y verificable.
- No sobreprometer ni ocultar dependencias del cliente.
- Evitar jerga innecesaria y frases comerciales vacías.
- Mantener una relación visible entre problema, solución, entregable y criterio de aceptación.
