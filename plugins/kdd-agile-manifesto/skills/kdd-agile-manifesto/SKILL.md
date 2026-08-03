---
name: kdd-agile-manifesto
description: 'Consulta honesta de los 4 valores y 12 principios del Manifiesto Agil: cada uno con su categoria (medible/juicio/conocimiento) y, si corresponde, por que no es medible. Usala cuando el usuario pregunte que dice el Manifiesto Agil sobre una decision de proceso, o pida justificar una practica de equipo citandolo.'
---

# KDD Agile Manifesto Reference

Segundo plugin sin instrumento de la serie [kdd-book](https://github.com/MauricioPerera/kdd-book) —
distinto de [kdd-zen-of-python](https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-zen-of-python)
en género: el Zen es juicio estético sobre código; el Manifiesto Ágil es juicio sobre **cómo trabaja
un equipo** (colaboración, ritmo, auto-organización), ni siquiera del mismo tipo de artefacto que un
instrumento pudiera leer.

## Qué hacer con este skill

1. **Consultá `scripts/knowledge.json`** antes de responder cualquier pregunta sobre el Manifiesto
   Ágil. Cada uno de los 17 nodos (declaración + 4 valores + 12 principios) trae:
   - `title`: el valor o principio, en español.
   - `pile`: `B` (juicio real, sin umbral) o `C` (conocimiento/referencia). **Ninguno es `A`.**
   - `why_not`, cuando `pile` es `B`: por qué no tiene una propiedad medible.
2. **No inventes una métrica de proceso** para ningún principio. Si el usuario pide "verificar" que
   su equipo sigue el Manifiesto Ágil, la respuesta honesta es que eso no es lo que este skill hace.

## La decisión más interesante del triaje

Se evaluó seriamente reusar una regla de cadencia de entregas (basada en tags de git) — ya usada por
la fuente hermana de Scrum y XP — para los principios de "entrega temprana y continua" y "entregar
software funcionando frecuentemente". Se descartó con tres razones documentadas en el `why_not`:
sin repositorio git, la regla no puede verificar nada; mide solo el hueco entre tags, no si lo
entregado es realmente "software funcionando"; y es un subconjunto parcial de una propiedad que en
el fondo pide juicio de equipo, no una cuenta de días.

## Recursos incluidos

- `scripts/knowledge.json` — la declaración, los 4 valores y los 12 principios, cada uno con su
  pila y (si es `B`) su `why_not`. No hay `scripts/*.py`: no hay nada que ejecutar.
