---
name: kdd-zen-of-python
description: 'Consulta honesta de los 19 aforismos del Zen de Python (PEP 20, accesible con `import this`): cada uno con su categoria (medible/juicio/conocimiento) y, si corresponde, por que no es medible. Usala cuando el usuario pregunte que dice el Zen de Python sobre un caso de diseno, o pida justificar una decision de estilo citando el Zen.'
---

# KDD Zen of Python Reference

Este plugin es deliberadamente distinto a los demás de la serie [kdd-book](https://github.com/MauricioPerera/kdd-book):
**no tiene instrumento**. Los 19 aforismos del Zen de Python (PEP 20) son juicio estético de diseño
-"lo simple es mejor que lo complejo", "la legibilidad cuenta"- y ninguno tiene una propiedad binaria
que un script pueda verificar sin ambigüedad. Forzar uno solo por tener "algo ejecutable" habría sido
exactamente el error que este método evita en el resto de sus fuentes.

## Qué hacer con este skill

1. **Consultá `scripts/knowledge.json`** antes de responder cualquier pregunta sobre el Zen de
   Python. Cada uno de los 19 nodos trae:
   - `title`: el aforismo, en español.
   - `pile`: `B` (juicio real, sin umbral) o `C` (conocimiento/referencia). **Ninguno es `A`.**
   - `why_not`, cuando `pile` es `B`: por qué no tiene una propiedad medible.
2. **No inventes una regla ejecutable** para ningún aforismo. Si el usuario pide "verificar" que su
   código sigue el Zen de Python, la respuesta honesta es que eso no es lo que este skill hace — podés
   señalar herramientas reales que sí verifican propiedades relacionadas (por ejemplo, `pep8_checks`
   o linters de Python para forma superficial), pero el Zen en sí es criterio, no regla.

## La decisión más interesante del triaje

El aforismo "Errors should never pass silently. Unless explicitly silenced." (pila `B`) fue evaluado
seriamente para instrumentar reusando una regla existente de detección de `except` demasiado amplios.
Se descartó explícitamente: esa regla marca cualquier `except Exception` amplio, incluso uno que
maneja el error de verdad (que el aforismo permite) — reusarla habría sido un generador sistemático de
falsos positivos, tergiversando al autor para forzar una instrumentación que no le corresponde. Ese
razonamiento está en el `why_not` del nodo correspondiente.

## Recursos incluidos

- `scripts/knowledge.json` — los 19 aforismos, cada uno con su pila y (si es `B`) su `why_not`. No
  hay `scripts/*.py`: no hay nada que ejecutar.
