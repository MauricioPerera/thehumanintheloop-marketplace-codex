---
name: supabase-pgcron-auditor
description: "Audita jobs pg_cron de Supabase self-hosted en modo estrictamente read-only: lista cron.job, cron.job_run_details y configuracion, detecta jobs fallidos, pausados, duplicados, frecuencias peligrosas y comandos que expongan secretos o muten fuera de alcance. Nunca crea, altera, elimina ni ejecuta jobs."
---

# Supabase pg_cron Auditor

Usa esta skill cuando el usuario quiera revisar los jobs `pg_cron` de una instancia Supabase self-hosted: listar jobs, historial de ejecuciones y configuracion, y detectar jobs fallidos, pausados, duplicados, frecuencias peligrosas y comandos que expongan secretos o muten fuera de alcance. Confirma host, contenedor de Postgres, rol de solo lectura y ventana antes de inspeccionar.

## Alcance

Cubre cuatro dominios, siempre en modo estrictamente read-only:

1. **Jobs (`cron.job`)**: lista `jobid`, `schedule`, `command`, `jobname`, `node`, `database`, `username`, `active`. Detecta jobs inactivos/pausados (`active = false`), duplicados (mismo `command`/`schedule`), frecuencias peligrosas (`* * * * *`, cada segundo, sin cota) y jobs sin `nodename`/`nodeport` explicito.
2. **Historial (`cron.job_run_details`)**: lista `runid`, `jobid`, `job_pid`, `database`, `username`, `command`, `status`, `return_message`, `start_time`, `end_time`. Detecta ejecuciones `failed`/`err` y relaciones job→ultima ejecucion.
3. **Configuracion (`pg_settings`)**: parametros `cron.*` (`cron.database_name`, `cron.use_background_workers`, `cron.host`, `cron.timezone`, etc.) y version de la extension `pg_cron`.
4. **Comandos de los jobs**: inspecciona el texto de `command` de cada job en busca de secretos en texto plano, mutaciones fuera de alcance (`DROP`/`TRUNCATE`/`DELETE` sobre tablas ajenas a la del job) o llamadas a `cron.schedule`/`cron.unschedule`/`cron.alter_job` anidadas.

## Reglas de seguridad

- Solo ejecutas consultas `SELECT` de lectura contra `cron.job`, `cron.job_run_details`, `pg_settings`, `pg_catalog`, `information_schema` y `pg_extension`.
- No ejecutas `cron.schedule`, `cron.unschedule`, `cron.alter_job`, `cron.alterjob` ni ningun `INSERT`/`UPDATE`/`DELETE`/`ALTER`/`DROP`/`CREATE`/`TRUNCATE`/`GRANT`/`REVOKE`.
- No creas, modificas, eliminas ni ejecutas jobs. Tampoco los pausas/reactivas (eso muta `cron.job.active`).
- No reinicias servicios: no `docker restart`, no `docker compose up`/`down`/`restart`, no `docker stop`/`kill`/`rm`.
- No despliegas Edge Functions ni aplicas migraciones: no `supabase functions deploy`, no `supabase db push`, no `supabase migration`, no `supabase secrets set`/`unset`, no `supabase db reset`.
- No vuelcas la base: no `pg_dump`, no `pg_restore`, no `COPY`/`\copy`.
- No lees secretos ni credenciales: no `cat .env`, no imprimir valores de `JWT_SECRET`/`anon key`/`service_role key`/`password`/`api_key`/`Authorization`. Reporta solo la presencia/nombre del secreto, nunca el valor.
- Para inspeccionar archivos de configuracion usa `grep`/`awk`/`sed`/`find` sobre archivos de config (e.g. `config.toml`, `docker-compose.yml`), nunca sobre `.env` ni archivos de credenciales.
- Redacta tokens, contraseñas, URLs con credenciales, headers `Authorization` y cualquier `secret`/`config` que aparezca en el `command` de un job.
- Marca como `WARNING`/`CRITICAL` cualquier valor no verificable sin convertirlo en un secreto visible. Para remediar, genera un plan separado y pide confirmacion explicita; no lo ejecutes desde esta skill.

## Flujo

1. Verifica el alias SSH, usuario, cliente `psql`/`ssh`, clave y `known_hosts` mediante el plugin VPS SSH Manager; identifica el contenedor de Postgres (`docker ps`, `docker inspect`) y el rol de conexion de solo lectura.
2. Lista los jobs de `cron.job` con `jobid`, `schedule`, `command`, `jobname`, `active`, `database`, `username`.
3. Lista el historial reciente de `cron.job_run_details` (estado, `return_message`, `start_time`/`end_time`) y cruza cada `jobid` con su ultima ejecucion para detectar jobs fallidos.
4. Inspecciona `pg_settings` para parametros `cron.*` y `pg_extension` para la version de `pg_cron`.
5. Analiza los `command` de los jobs: frecuencias peligrosas en `schedule`, secretos en texto plano, mutaciones fuera de alcance y llamadas anidadas a `cron.schedule`/`cron.unschedule`/`cron.alter_job`.
6. Resume hallazgos por dominio con timestamp UTC, `jobid`, recurso, control, evidencia redactada, severidad y remediacion propuesta (plan separado, no ejecutado).

## Consultas permitidas

```sql
SELECT jobid, jobname, schedule, command, active, database, username, nodename, nodeport
FROM cron.job ORDER BY jobid;

SELECT runid, jobid, job_pid, database, username, command, status, return_message, start_time, end_time
FROM cron.job_run_details ORDER BY start_time DESC LIMIT 50;

SELECT name, setting, source, context FROM pg_settings WHERE name LIKE 'cron%';

SELECT extname, extversion FROM pg_extension WHERE extname = 'pg_cron';
```

Inspecciona config con `grep -E '^cron\.' /etc/supabase/config.toml`, `awk '/cron/' config.toml`, `sed -n '1,40p' docker-compose.yml` o `find . -name 'config.toml'`. Nunca uses `cat .env` ni leas archivos de credenciales.

## Validacion

Ejecuta `python scripts/validate_pgcron_scope.py --command-file <archivo>` cuando se prepare una lista de comandos/SQL. Debe terminar con `PASSED`; cualquier `cron.schedule`/`cron.unschedule`/`cron.alter_job`, DML/DDL (`INSERT`/`UPDATE`/`DELETE`/`ALTER`/`DROP`/`CREATE`/`TRUNCATE`), `supabase functions deploy`, `docker restart`/`compose up`/`compose down`, `pg_dump`, `cat .env`, credenciales en texto plano o comando fuera de alcance queda bloqueado.