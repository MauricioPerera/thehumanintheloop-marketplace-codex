---
name: cv-job-tailor
description: Adapta un CV real a una oferta laboral concreta usando únicamente la información autorizada por el usuario. Úsala cuando el usuario pida reescribir, optimizar o personalizar un CV para una vacante, preparar una versión ATS o comparar su experiencia con una oferta.
---

# CV Job Tailor

Adapta el CV del usuario a una oferta específica sin fabricar experiencia, títulos, fechas, tecnologías, idiomas, certificaciones ni métricas. Trata el CV y la oferta como fuentes separadas: el CV aporta evidencia y la oferta aporta requisitos, vocabulario y prioridades.

## Flujo obligatorio

1. Recibir el CV base y el texto completo de la oferta. Si falta uno, solicitarlo antes de redactar.
2. Identificar idioma, país, seniority, formato solicitado y restricciones de longitud.
3. Construir una matriz de evidencia: requisito de la oferta → experiencia o frase exacta del CV → estado `evidenced`, `partial` o `missing`.
4. Reorganizar y reescribir solo contenido respaldado por el CV. Se permite condensar, ordenar y mejorar claridad; no se permite crear logros.
5. Preservar nombres de empresas, cargos, fechas y tecnologías. Si hay contradicciones, detener la afirmación y marcarla como `NEEDS USER CONFIRMATION`.
6. Ejecutar el validador antes de entregar la versión final:

   ```powershell
   python plugins/cv-job-tailor/scripts/validate_cv_tailoring.py --cv cv-base.md --job oferta.md --output cv-adaptado.md --json cv-report.json
   ```

7. Entregar cuatro bloques: CV adaptado, matriz de evidencia, keywords cubiertas/ausentes y alertas.

## Reglas anti-fabricación

- No inventar números, porcentajes, impacto, herramientas, responsabilidades o niveles de idioma.
- No convertir una responsabilidad en un logro cuantificado sin evidencia explícita.
- No copiar requisitos de la oferta como si fueran experiencia del candidato.
- Mantener una lista de cambios trazable; cada cambio sustantivo debe apuntar a una sección del CV base.
- Preguntar antes de completar huecos con información no proporcionada.

## Reglas ATS y redacción

- Usar encabezados simples: `Summary`, `Experience`, `Skills`, `Education`, `Certifications` según el idioma del CV.
- Priorizar términos de la oferta solo cuando sean verdaderos para el candidato.
- Evitar tablas, columnas, iconos, barras de nivel, gráficos, foto y texto dentro de imágenes.
- Mantener viñetas breves con verbo, contexto y resultado únicamente si el resultado está respaldado.
- No prometer que un ATS concreto aceptará el documento; reportar compatibilidad estructural.

## Salida mínima

```text
CV adaptado
Matriz de evidencia
Keywords cubiertas y ausentes
Alertas de verificación del usuario
Resultado del validador: PASSED / FAILED
```
