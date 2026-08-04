---
name: docker-log-diagnostics
description: Investiga fallos de contenedores Docker por SSH con logs acotados, eventos, reinicios y healthchecks sin exponer secretos.
---

# Docker Log Diagnostics

Correlaciona `docker ps -a`, `docker inspect`, `docker events` acotado y `docker logs --since` con timestamps. Pide nombre del servicio y ventana temporal; limita líneas y redacta tokens, cookies, URLs firmadas y variables sensibles.

Entrega hipótesis separadas de hechos, comandos reproducibles y pruebas siguientes. No reinicies ni alteres contenedores durante el diagnóstico.
