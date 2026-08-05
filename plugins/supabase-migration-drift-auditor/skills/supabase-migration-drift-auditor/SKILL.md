---
name: supabase-migration-drift-auditor
description: Audita en modo lectura el sistema de migraciones de Supabase self-hosted comparando migraciones aplicadas, archivos en disco y catálogos PostgreSQL para detectar drift de schema sin aplicar, revertir ni crear migraciones y sin leer datos de usuario ni secretos.
---

# Supabase Migration Drift Auditor

Usa esta skill cuando el usuario quiera saber si el schema vivo de una instancia Supabase self-hosted coincide con las migraciones aplicadas y con los archivos `supabase/migrations/*.sql` en disco, **sin aplicar nada**. Es la causa #1 de upgrades fallidos en self-hosted: ediciones manuales al DB que bypassan el sistema de migraciones. Confirma host, usuario, contenedor Postgres, DB y ventana antes de inspeccionar.

## Alcance

Compara tres fuentes, siempre en modo lectura:

1. **Migraciones aplicadas** (`supabase_migrations.schema_migrations`): `version`, `name` y metadatos de `statements` (longitud y hash, no contenido crudo si contiene literales sensibles).
2. **Migraciones en disco** (`supabase/migrations/*.sql`): nombre, tamaño, mtime y `sha256`.
3. **Schema vivo** (catálogos PostgreSQL): tablas/vistas/materializadas/secuencias/foreign tables en `public`/`auth`/`storage`/`_realtime`, índices, funciones y triggers.

Reporta **pendientes** (archivo existe, no aplicado), **faltantes** (aplicado, sin archivo), **duplicadas** (misma `version` repetida), **fuera de orden** (gaps en secuencia de `version`) y **drift de schema heurístico** (objetos del schema vivo no explicables por el conjunto de migraciones aplicadas, por diferencia de conjuntos nombre+tipo, sin ejecutar las migraciones).

## Reglas de seguridad

- Solo `SELECT` contra `supabase_migrations.schema_migrations` y catálogos (`pg_catalog`, `information_schema`, `pg_indexes`, `pg_proc`, `pg_class`).
- No ejecutes `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `ALTER`, `DROP`, `CREATE`, `GRANT`, `REVOKE` ni `SET ROLE`, ni contra tablas de usuario ni contra `supabase_migrations.schema_migrations`.
- No apliques, reviertas, crees, repares ni reordenes migraciones: `supabase db push`, `supabase migration up/new/repair/squash`, `supabase db reset/pull/diff/commit`.
- No ejecutes `supabase functions deploy/serve/delete`, `supabase secrets set/unset`, `supabase start/stop/restart`, `supabase link` con tokens.
- No reinicies contenedores: `docker restart`, `docker compose up/down/restart`.
- `docker exec` permitido **solo** como `psql ... -c "SELECT ..."` contra catálogos/migraciones; no `docker exec` para leer archivos ni `cat` de `.env`/`config.toml`/`pg_hba.conf` dentro del contenedor.
- No leas ni imprimas secretos (`JWT_SECRET`, `anon`/`service_role` key, passwords, tokens, `PGPASSWORD`); solo reporta presencia/nombre. Variables de entorno del contenedor: nombres, nunca valores.
- No hagas `pg_dump` de tablas de aplicación ni `SELECT *` sobre tablas de usuario; solo catálogos y `supabase_migrations.*`.
- Los `statements` de migraciones: reporta longitud y `sha256`, no contenido crudo, si se detectan literales que parezcan secretos.
- No edites `.env`, Compose, `migrations/` ni catálogos durante la auditoría; no contactes a Supabase cloud/Studio.
- Toda remediación es un plan separado que requiere confirmación explícita; esta skill no la aplica.

## Flujo

1. Verifica el alias SSH, usuario, cliente `psql`/`ssh`, clave y `known_hosts` mediante el plugin VPS SSH Manager; identifica el contenedor Postgres y la DB. No procede sin `known_hosts` y clave verificada.
2. Detecta automáticamente el contenedor Postgres (`docker ps`) y el rol de conexión read-only; si no existe, reporta `WARNING` y usa el de menor privilegio disponible, nunca `service_role`.
3. Lista migraciones aplicadas desde `supabase_migrations.schema_migrations` (`version`, `name`).
4. Lista archivos en disco bajo `supabase/migrations/*.sql` (nombre, tamaño, mtime, `sha256`).
5. Compara por `version`: pendientes, faltantes, duplicadas; detecta fuera de orden (gaps en secuencia numérica/timestamp).
6. Inspecciona catálogos (tablas, índices, funciones, triggers) y compara el schema esperado (derivado del conjunto de migraciones aplicadas) vs el observado para hallar drift heurístico, sin ejecutar migraciones.
7. Resume hallazgos con timestamp UTC, alcance, fuentes, hashes de archivos, diferencias, severidades (`CRITICAL` para aplicadas sin archivo / drift de schema; `WARNING` para pendientes, duplicadas, fuera de orden; `INFO` para sólo metadatos) y remediación propuesta por separado (nunca aplicada desde la skill).

## Consultas y comandos permitidos

```bash
command -v psql ssh sha256sum awk sed grep find || true
docker ps --format '{{.Names}} {{.Image}}'
docker inspect --format '{{.Config.Image}}' <pg_container>
find <repo>/supabase/migrations -maxdepth 1 -type f -name '*.sql' -printf '%f %s %T@\n'
sha256sum <repo>/supabase/migrations/*.sql
docker exec <pg_container> psql -U <user> -d <db> -At -c "SELECT ..."
```

```sql
SELECT version, name, statements FROM supabase_migrations.schema_migrations ORDER BY version;
SELECT n.nspname, c.relname, c.relkind FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
 WHERE n.nspname IN ('public','auth','storage','_realtime') AND c.relkind IN ('r','v','m','S','f');
SELECT schemaname, indexname, indexdef FROM pg_indexes WHERE schemaname IN ('public','auth','storage');
SELECT n.nspname, p.proname FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace
 WHERE n.nspname IN ('public','auth','storage');
SELECT event_object_table, trigger_name, action_statement FROM information_schema.triggers
 WHERE trigger_schema IN ('public','auth','storage');
```

## Validación

Ejecuta `python scripts/validate_migration_drift_scope.py --command-file <archivo>` cuando se prepare una lista de comandos/SQL. Debe terminar con `PASSED`; cualquier sentencia mutante (DDL/DML, `supabase db push/reset/migration up/...`), CLI que muta (`docker restart/compose up`), `pg_dump`, secreto en texto plano (`cat .env`, `JWT_SECRET=`, `password=`, `Authorization: Bearer`), `docker exec` distinto de `psql ... -c "SELECT ..."` o cualquier línea fuera de los prefijos de inspección queda bloqueado y etiquetado por categoría (`[mutation/cli]`, `[secret-token]`, `[secret-value]`, `[out-of-scope]`).