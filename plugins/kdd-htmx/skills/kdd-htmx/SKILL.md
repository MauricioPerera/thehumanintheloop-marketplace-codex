---
name: kdd-htmx
description: 'Verifica HTML, capturas HTTP y plantillas contra 6 tecnicas medibles de la documentacion de htmx: mejora progresiva, indicador de carga, token CSRF, cabecera Vary, Content-Security-Policy y escapado de interpolaciones. Usala cuando el usuario pida revisar o auditar una integracion de htmx.'
---

# KDD htmx Checker

Extraido de la documentacion de htmx (52 paginas, 59 titulos de seccion) con el metodo
[Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). Es
documentacion de referencia -describe una API, no cataloga tecnicas-, y ese genero predice un
corpus mas debil que el de un libro de estilo: casi la mitad de los 59 items cae en pila C por
definicion. Familia nueva en tres artefactos distintos (HTML, capturas HTTP, plantillas) porque
ninguna de las familias que leen codigo Python sirve para una fuente sobre hipermedia.

## Flujo

1. **Encontrá el artefacto relevante para cada regla** -no todas miran lo mismo-:
   - `progresivo`, `indicador`, `csrf`: HTML servido o generado por la app.
   - `vary`, `csp`: capturas de intercambios HTTP reales (formato `METODO /ruta` + cabeceras +
     linea en blanco + `codigo` + cabeceras + linea en blanco + cuerpo, en un archivo `.http`).
     El instrumento no hace peticiones de red -las capturas las provee el proyecto (un test, un
     `curl -v`, un proxy)-.
   - `escapado`: la plantilla sin renderizar.
2. **Corré las 6 reglas**:

   ```bash
   python scripts/html_checks.py --rule progresivo <archivo.html> [...]
   python scripts/html_checks.py --rule indicador <archivo.html> [...]
   python scripts/html_checks.py --rule csrf --token X-CSRF-TOKEN <archivo.html> [...]
   python scripts/http_checks.py --rule vary <capturas/>
   python scripts/http_checks.py --rule csp --exige default-src --exige connect-src <capturas/>
   python scripts/template_checks.py --rule escapado --motor jinja2 --autoescape on <plantilla.html>
   python scripts/template_checks.py --rule escapado --motor handlebars <plantilla.hbs>
   ```

   `csrf` exige `--token` (el nombre del header, p. ej. `X-CSRF-TOKEN`); `csp` exige `--exige`
   (una o más directivas, repetible); `escapado` exige `--motor` (`jinja2`, `django`,
   `handlebars`, `mustache`) y, solo para `jinja2`/`django`, `--autoescape on|off` -en esos dos el
   escapado se decide en la aplicación, no en la plantilla, y es invisible sin el dato-. Ningún
   valor se adivina: adivinar la convención del proyecto inventaría el resultado. Exit `0`
   (cumple), `1` (no cumple, con detalle) o `2` (no se pudo verificar).
3. **Reportá las 6 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de la documentación** (53 de los 59 títulos), consultá `scripts/knowledge.json`
   antes de responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral,
   `C`=referencia) y, si es `B`, un `why_not`. **No inventes una regla para lo que el nodo dice
   que es referencia o requiere juicio.**

## Reglas medibles (pila A)

| Regla | Artefacto | Qué mide |
|---|---|---|
| `progresivo` | HTML | Quien emite un `hx-get`/`hx-post`/etc. (o hereda `hx-boost`) sigue funcionando sin JavaScript: es un `<a href>` o un `<form action>`, o está dentro de uno |
| `indicador` | HTML | Quien emite una petición da señal (`hx-indicator` en alcance, o un descendiente con la clase `htmx-indicator`) |
| `csrf` | HTML | El token viaja en un elemento que de verdad lo lleva (`hx-headers` en alcance, o un input oculto); detecta también el caso donde `hx-boost` no actualiza `<html>`/`<body>` y el token queda viejo |
| `vary` | Capturas HTTP | La respuesta que cambia según `HX-Request` (demostrado comparando dos capturas de la misma ruta) declara `Vary: HX-Request` |
| `csp` | Capturas HTTP | La respuesta HTML trae `Content-Security-Policy` (cabecera o `<meta>`) con las directivas exigidas |
| `escapado` | Plantilla | Toda interpolación con contenido de usuario sale escapada, según la convención del motor declarado |

## Límite declarado, sin excepciones

`escapado` mide escape para HTML: no cubre contextos donde ese escape no alcanza (dentro de un
`<script>`, un atributo sin comillas, un `href` que termina en `javascript:`) -eso es escapado
sensible al contexto, otra técnica, y exigiría parsear el HTML que la plantilla todavía no genera.
`vary` no adivina si una respuesta varía: sin dos capturas comparables de la misma ruta (una con
`HX-Request`, otra sin), es `NO VERIFICABLE`, no un verde barato.

## Reporte

| Regla | Estado | Archivo/Ruta | Detalle |
|---|---|---|---|
| progresivo | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| indicador | ... | ... | ... |
| csrf | ... | ... | ... |
| vary | ... | ... | ... |
| csp | ... | ... | ... |
| escapado | ... | ... | ... |

## Recursos incluidos

- `scripts/html_checks.py`, `scripts/http_checks.py`, `scripts/template_checks.py` -sin
  dependencias externas, extraídos y verificados (41 pruebas propias) en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -los 59 títulos de la documentación, triados en pila A/B/C con su
  `why_not` cuando corresponde.
