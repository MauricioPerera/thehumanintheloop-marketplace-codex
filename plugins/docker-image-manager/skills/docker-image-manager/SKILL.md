---
name: docker-image-manager
description: Audita y gestiona imágenes Docker en un VPS por SSH con digests, espacio recuperable y guardas contra limpieza destructiva.
---

# Docker Image Manager

Empieza siempre en modo lectura con `docker image ls`, `docker system df -v` e inspección de referencias y digests.

Clasifica imágenes activas, huérfanas, dangling y potencialmente recuperables. Antes de `pull`, `tag`, `rmi` o `image prune`, muestra el conjunto exacto, riesgos, espacio esperado y rollback posible; exige confirmación. Nunca borres imágenes usadas por contenedores ni expongas credenciales de registries.
