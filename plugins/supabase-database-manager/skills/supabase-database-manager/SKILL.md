---
name: supabase-database-manager
description: Diagnostica y administra PostgreSQL de Supabase self-hosted por SSH con consultas seguras, control de alcance, migraciones y confirmación antes de mutaciones.
---

# Supabase Database Manager

Usa esta skill para inspeccionar PostgreSQL, revisar conexiones, extensiones, locks, espacio y migraciones de una instancia Supabase self-hosted.

## Reglas de seguridad

- No muestres contraseñas, connection strings, JWTs, `service_role`, datos de tablas ni resultados completos de usuarios.
- Empieza por metadata y conteos: versión, bases, esquemas, extensiones, conexiones, locks y tamaño por tabla.
- Clasifica cada consulta como `READ_ONLY`, `DDL` o `DML`. Las dos últimas requieren plan, impacto, backup/rollback y confirmación inmediata.
- No ejecutes `DROP`, `TRUNCATE`, `DELETE`, `UPDATE`, `ALTER`, `CREATE EXTENSION`, `VACUUM FULL` ni migraciones automáticamente.
- Usa el contenedor `supabase-db` y el mecanismo de autenticación ya configurado; nunca inventes credenciales.

## Flujo

1. Confirma instancia, base y objetivo.
2. Ejecuta diagnóstico read-only con `psql` y límites (`LIMIT`, `pg_stat_activity` sin query text sensible).
3. Presenta hallazgos y una consulta reproducible redactada.
4. Para cambios, genera un plan con SQL exacto, impacto, backup, rollback y validación posterior.
5. Ejecuta solo después de confirmación explícita y reporta evidencia resumida.

Valida cualquier lote SQL con `python scripts/validate_sql_request.py --sql-file <archivo>` antes de usarlo.
