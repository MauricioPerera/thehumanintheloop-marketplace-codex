---
name: supabase-policy-security-auditor
description: Audita RLS, políticas de Storage, Auth/JWT y Edge Functions/Realtime de Supabase self-hosted en modo lectura sin mutar la base de datos ni revelar secretos.
---

# Supabase Policy Security Auditor

Usa esta skill cuando el usuario quiera revisar la postura de seguridad de las políticas de una instancia Supabase self-hosted: Row Level Security, Storage, Auth/JWT y Edge Functions/Realtime. Confirma host, usuario, alcance y ventana antes de inspeccionar.

## Alcance

Cubre cuatro dominios de políticas, siempre en modo lectura:

1. **Row Level Security (RLS)**: tablas con y sin RLS, políticas por tabla, comandos (`SELECT`/`INSERT`/`UPDATE`/`DELETE`), roles, condiciones `USING`/`WITH CHECK`, funciones `SECURITY DEFINER` y políticas `force`/`permissive`.
2. **Storage**: buckets públicos/privados, políticas de Storage, reglas MIME/tamaño y permisos por objeto.
3. **Auth/JWT**: proveedores habilitados, expiración y algoritmo de JWT, claves de firma (nombre, nunca valor), roles `anon`/`authenticated`/`service_role` y sesiones.
4. **Edge Functions/Realtime**: funciones desplegadas, secrets/config (nombre, nunca valor), permisos JWT de Edge Functions y políticas de Realtime.

## Reglas de seguridad

- Solo ejecuta consultas `SELECT` de lectura contra catálogos (`pg_catalog`, `information_schema`, `pg_policies`, `storage.buckets`, `storage.policies`, vistas de `supabase_functions`).
- No ejecutes `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `DROP`, `TRUNCATE`, `GRANT`, `REVOKE`, `CREATE POLICY`, `DROP POLICY`, ni `supabase` CLI que cree/modifique/borre recursos.
- No leas valores de secretos, JWT firmados, claves de firma (`JWT_SECRET`, `anon key`, `service_role key`), contraseñas ni `Authorization`. Reporta solo la presencia/nombre y la expiración cuando sea observable.
- Redacta tokens, contraseñas, URLs con credenciales, headers `Authorization` y cualquier `secret`/`config` de Edge Functions.
- No reinicies servicios, no edites `.env`, Compose, migraciones, ni políticas durante una auditoría.
- Marca como `WARNING`/`CRITICAL` cualquier valor no verificable sin convertirlo en un secreto visible.
- No consulta datos reales de tablas de usuario; solo metadatos de políticas y buckets.

## Flujo

1. Verifica el alias SSH, usuario, cliente `psql`/`ssh`, clave y `known_hosts` mediante el plugin VPS SSH Manager; identifica el contenedor de Postgres y el rol de conexión de solo lectura.
2. Lista tablas del esquema `public` y `auth` y determina cuáles tienen RLS habilitado.
3. Inspecciona `pg_policies` y catálogos para obtener políticas por tabla, comando, rol, `qual`/`with_check` y función `SECURITY DEFINER`.
4. Inspecciona `storage.buckets` y `storage.policies` para buckets públicos y reglas; reporta exposición sin leer objetos.
5. Verifica proveedores de Auth, presencia de `JWT_SECRET`/claves (nombre, no valor) y algoritmos/expiración cuando sea observable sin firmar tokens.
6. Lista Edge Functions desplegadas y su `config`/`secrets` (nombres), y políticas de Realtime; no invocas funciones ni publicas eventos.
7. Resume hallazgos por dominio con timestamp UTC, recurso, control, evidencia redactada, severidad y remediación propuesta. Para remediar, genera un plan separado y pide confirmación explícita.

## Consultas permitidas

```sql
SELECT n.nspname, c.relname, c.relrowsecurity, c.relforcerowsecurity
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname IN ('public','auth') AND c.relkind = 'r';

SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check
FROM pg_policies WHERE schemaname IN ('public','auth');

SELECT n.nspname AS schema, p.proname, p.prosecdef
FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE n.nspname IN ('public','auth','storage') AND p.prosecdef = true;

SELECT id, name, public, file_size_limit, allowed_mime_types FROM storage.buckets;
SELECT policyname, tablename, policyname AS storage_policy, cmd, qual FROM storage.policies;
```

No ejecutes `docker exec` contra PostgreSQL para leer `.env`, no uses `supabase functions deploy/serve`, no firmes ni valides JWT con claves reales y no alteres políticas desde esta skill.

## Validación

Ejecuta `python scripts/validate_policy_security_scope.py --command-file <archivo>` cuando se prepare una lista de comandos/SQL. Debe terminar con `PASSED`; cualquier sentencia mutante, secreto en texto plano o CLI que cree/modifique/borre queda bloqueado.