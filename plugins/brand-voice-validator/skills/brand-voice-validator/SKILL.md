---
name: brand-voice-validator
description: Valida tono, vocabulario, claims, claridad y consistencia editorial contra una guía de marca. Úsala antes de publicar páginas, campañas o documentación externa.
---
# Brand Voice Validator

Convierte una guía editorial en reglas observables y separa incumplimientos de preferencias subjetivas.

## Flujo
1. Lee la guía de voz y el texto objetivo.
2. Ejecuta `python plugins/brand-voice-validator/scripts/check_voice.py guia.md texto.md`.
3. Revisa longitud de frases, palabras prohibidas, claims sin soporte y consistencia de persona verbal.
4. Propón cambios mínimos preservando significado.

## Salida
Entrega regla, fragmento, estado, razón y sustitución sugerida.
