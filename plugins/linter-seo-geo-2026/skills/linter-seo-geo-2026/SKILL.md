---
name: linter-seo-geo-2026
description: 'Analiza artículos de blog en Markdown o HTML con validadores estáticos de SEO híbrido y GEO: profundidad, cápsulas de respuesta, densidad de hechos, FAQ/glosario, enlaces, metadatos y multimedia. Úsala cuando el usuario pida revisar, auditar, validar o preparar un artículo antes de publicarlo.'
---

# Linter SEO/GEO 2026

Ejecuta una auditoría de prepublicación reproducible y entrega un reporte técnico en español. Combina los resultados deterministas del script con una revisión editorial explícita; no inventes fuentes, citas, enlaces ni palabras clave que no estén en el texto.

## Flujo de auditoría

1. Recibe el artículo como texto pegado o archivo Markdown/HTML. Si falta la palabra clave principal, infiere una candidata solo como `inferencia` y marca la comprobación de placement como no verificable.
2. Determina el formato por encabezados y señales léxicas, o acepta `guide`, `standard`, `product` o `faq`. Usa estos rangos: guía completa 2500–5000 palabras; estándar 1500–2500; producto 800–1500; FAQ/definición 300–800.
3. Ejecuta el validador:

   ```powershell
   python "C:\Users\Administrador\.codex\skills\linter-seo-geo-2026\scripts\lint_seo_geo.py" --input articulo.md --keyword "palabra clave"
   ```

   Usa `--format guide|standard|product|faq`, `--json salida.json` y `--markdown reporte.md` cuando corresponda.
4. Revisa manualmente profundidad frente a relleno, exactitud de fuentes, autoridad de las citas, naturalidad de anchors y si las cápsulas responden la intención. Las estadísticas y citas solo pasan si la atribución y fecha aparecen en el artículo; su veracidad externa requiere revisión posterior.
5. Presenta las siete reglas en orden. Cada una debe incluir exactamente `[PASSED]` o `[FAILED]`, valor detectado y justificación. Si algo no puede verificarse, usa `[FAILED]` con `No verificable`.

## Reglas

1. **Longitud y profundidad:** reporta palabras, formato, rango y señales de contenido genérico repetitivo.
2. **Cápsulas:** cada H1/H2 debe abrir con un bloque de 40–75 palabras dentro de sus primeras 100 palabras. Ejecuta `hedging_check` contra `probablemente`, `tal vez`, `podría`, `quizá`, `posiblemente`, `likely`, `perhaps`, `maybe` y `could`; cualquier coincidencia falla la cápsula.
3. **Densidad y E-E-A-T:** exige 3 estadísticas con fuente nombrada y fecha/año, y 2 citas textuales con nombre completo y cargo. Diferencia “detectado” de “verificado”.
4. **FAQ y glosario:** exige sección FAQ final con 5–8 pares Q&A, respuestas de 2–4 oraciones y glosario con al menos 5 definiciones directas.
5. **Topic clusters:** exige 2–3 enlaces internos, al menos 3 externos plausiblemente autoritativos y ningún anchor genérico: `haz clic aquí`, `leer más`, `este enlace`, `click here`.
6. **Metadatos:** exige exactamente un H1; keyword en H1, primeras 100 palabras y algún H2; toda imagen Markdown/HTML debe tener `alt` descriptivo no vacío.
7. **Salida:** cierra con tabla consolidada y “Plan de Acción Técnico”, con cambios concretos antes de JSON-LD o publicación.

## Reporte

Usa esta tabla:

| Regla | Estado | Valor detectado | Justificación |
|---|---|---|---|
| 1. Longitud y profundidad | [PASSED]/[FAILED] | ... | ... |

Después incluye detalles por regla, fallos con ubicación cuando sea posible y un plan accionable. Conserva las advertencias sobre heurísticas y nunca conviertas una coincidencia léxica en prueba de calidad o veracidad.

## Recurso incluido

` scripts/lint_seo_geo.py` es un analizador sin dependencias externas. Lee UTF-8 desde archivo o stdin, reconoce Markdown y HTML, emite JSON para automatización y Markdown para revisión humana. Si el script y la revisión editorial discrepan, conserva ambos datos y explica la discrepancia.
