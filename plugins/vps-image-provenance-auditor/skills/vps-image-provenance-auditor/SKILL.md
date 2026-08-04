---
name: vps-image-provenance-auditor
description: Audita tags, digests, registry y coherencia de imágenes Docker en un VPS sin hacer pull ni cambiar contenedores.
---
# VPS Image Provenance Auditor

Audita la procedencia observable de imágenes de un VPS autorizado. Confirma host, alcance, registry esperado y baseline antes de inspeccionar.

## Procedimiento

1. Inventaría imagen declarada, imagen en ejecución, repository, tag, digest local, arquitectura, created date y container ID sin consultar credenciales del registry.
2. Compara `docker inspect` acotado con Compose, lockfiles o manifests disponibles; marca tags flotantes (`latest`, ramas o semver sin digest) como `REVIEW`.
3. Marca `HIGH` cuando el contenedor no tenga digest verificable, use un registry no aprobado, mezcle arquitecturas inesperadas o difiera del artefacto declarado.
4. Comprueba si existen labels OCI de source, revision, version y build timestamp; no trata la presencia de labels como prueba criptográfica de autenticidad.
5. Separa evidencia local de verificación remota. No hace pull, no contacta registries privados, no ejecuta scanners que transmitan imágenes y no actualiza el deployment.

## Salida y límites

Incluye timestamp UTC, contenedor, referencia declarada, digest observado, registry, arquitectura, control, severidad y plan de remediación con rollback. No muestra tokens, headers de autenticación ni manifiestos privados, y no firma, retaguea, elimina o reemplaza imágenes sin autorización explícita.
