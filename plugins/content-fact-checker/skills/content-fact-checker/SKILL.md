---
name: content-fact-checker
description: Audita afirmaciones verificables en artículos, páginas y documentos, exigiendo fuentes nombradas, fechas, enlaces y atribuciones. Úsala antes de publicar contenido factual, SEO o GEO.
---

# Content Fact Checker

Identifica afirmaciones que pueden comprobarse y separa hechos, opiniones, predicciones y lenguaje promocional. No inventes fuentes: marca lo que requiera investigación o confirmación humana.

## Flujo

1. Lee el documento completo y clasifica afirmaciones cuantitativas, históricas, médicas, legales, técnicas o comparativas.
2. Ejecuta `python plugins/content-fact-checker/scripts/check_claims.py documento.md` como cribado inicial.
3. Para cada afirmación importante exige fuente nombrada, fecha y enlace cuando exista.
4. Comprueba que la fuente realmente respalde la afirmación y que no se confunda correlación con causalidad.
5. Separa hechos confirmados, afirmaciones sin evidencia, contradicciones y opiniones atribuidas.
6. Reporta `[PASSED]`, `[FAILED]` o `[NEEDS REVIEW]` por afirmación.

## Reglas

- No conviertas una estadística sin fuente en un hecho.
- No uses una fecha de publicación como fecha del dato si la fuente distingue ambas.
- Las citas textuales requieren autor, cargo o contexto y enlace a la fuente.
- Para temas de alto riesgo, exige revisión experta y no presentes el resultado como asesoría profesional.
- El script es un detector inicial; no sustituye la verificación semántica de la fuente.

## Salida

Entrega una tabla de afirmaciones con texto, tipo, fuente, fecha, estado, nivel de confianza y acción correctiva.
