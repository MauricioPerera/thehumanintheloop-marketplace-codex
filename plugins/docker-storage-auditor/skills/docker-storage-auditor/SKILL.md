---
name: docker-storage-auditor
description: Audita volúmenes, redes, mounts y exposición de Docker en un VPS por SSH sin revelar secretos ni modificar recursos.
---

# Docker Storage Auditor

Relaciona contenedores, volúmenes, bind mounts, redes y puertos publicados usando `docker inspect`, `docker volume ls` y `docker network inspect` con salida minimizada. Señala mounts del host, redes compartidas, puertos 0.0.0.0 y volúmenes sin consumidor.

No leas archivos de datos ni secretos. No elimines volúmenes o redes; entrega un plan separado con respaldo, dependencias y confirmación explícita.
