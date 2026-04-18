---
title: "Restore a Platform Project to Self-Hosted"
source: "https://supabase.com/docs/guides/self-hosting/restore-from-platform"
canonical_url: "https://supabase.com/docs/guides/self-hosting/restore-from-platform"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:31.214Z"
content_hash: "75a78a0563094b6ba87cfb4fcc0e9c6f52202d03ac1321e67ced12fa9f6ad969"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Restore Project from Platform","Restore Project from Platform"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Restore Project from Platform","Restore Project from Platform"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/postgres-upgrade-17/index.md", "title": "Upgrade to Postgres 17"}
nav_next: {"path": "supabase/docs/guides/self-hosting/self-hosted-auth-keys/index.md", "title": "New API Keys and Asymmetric Authentication"}
---

# 

Restore a Platform Project to Self-Hosted

## 

Restore your database from the Supabase platform to a self-hosted instance.

* * *

This guide walks you through restoring your database from a Supabase platform project to a [self-hosted Docker instance](/docs/guides/self-hosting/docker). Storage objects transfer or redeploying edge functions is not covered here.

## Before you begin[#](#before-you-begin)

You need:

*   A new self-hosted Supabase instance ([Docker setup guide](/docs/guides/self-hosting/docker))
*   [Supabase CLI](/docs/guides/local-development/cli/getting-started) installed (or use `npx supabase`)
*   [Docker Desktop](https://docs.docker.com/get-started/get-docker/) installed (required by the CLI)
*   `psql` installed ([official installation guide](https://www.postgresql.org/download/))
*   Your Supabase database passwords (for platform and self-hosted)

## Step 1: Get your platform connection string[#](#step-1-get-your-platform-connection-string)

On your managed Supabase project dashboard, click [**Connect**](/dashboard/project/_?showConnect=true) and copy the connection string (use the session pooler or direct connection).

## Step 2: Back up your platform database[#](#step-2-back-up-your-platform-database)

Export roles, schema, and data as three separate SQL files:

```
1supabase db dump --db-url "[CONNECTION_STRING]" -f roles.sql --role-only
```

```
1supabase db dump --db-url "[CONNECTION_STRING]" -f schema.sql
```

```
1supabase db dump --db-url "[CONNECTION_STRING]" -f data.sql --use-copy --data-only
```

This produces SQL files that are compatible across Postgres versions.

Using `supabase db dump` executes `pg_dump` under the hood but applies Supabase-specific filtering - it excludes internal schemas, strips reserved roles, and adds idempotent `IF NOT EXISTS` clauses. Using raw `pg_dump` directly will include Supabase internals and cause permission errors during restore. CLI requires Docker because it runs `pg_dump` inside a container from the Supabase Postgres image rather than requiring a local Postgres installation.

## Step 3: Prepare your self-hosted instance[#](#step-3-prepare-your-self-hosted-instance)

Before restoring, check the following on your self-hosted instance:

*   **Extensions**: Enable any non-default extensions your Supabase project uses. You can check which extensions are active by querying `select * from pg_extension;` on your managed database (or check Database Extensions in Dashboard).

## Step 4: Restore to your self-hosted database[#](#step-4-restore-to-your-self-hosted-database)

Connect to your self-hosted Postgres and restore the dump files. The [default](/docs/guides/self-hosting/docker#accessing-postgres) connection string for self-hosted Supabase is:

```
1postgres://postgres.your-tenant-id:[POSTGRES_PASSWORD]@[your-domain]:5432/postgres
```

Where `[POSTGRES_PASSWORD]` is the value of `POSTGRES_PASSWORD` in your self-hosted `.env` file.

Use your domain name, your server IP, or localhost for `[your-domain]` depending on whether you are running self-hosted Supabase on a VPS, or locally.

Run `psql` to restore:

```
1psql \2  --single-transaction \3  --variable ON_ERROR_STOP=1 \4  --file roles.sql \5  --file schema.sql \6  --command 'SET session_replication_role = replica' \7  --file data.sql \8  --dbname "postgres://postgres.your-tenant-id:[POSTGRES_PASSWORD]@[your-domain]:5432/postgres"
```

Setting `session_replication_role` to `replica` disables triggers during the data import, preventing issues like double-encryption of columns.

## Step 5: Verify the restore[#](#step-5-verify-the-restore)

Connect to your self-hosted database and run a few checks:

```
1psql "postgres://postgres.your-tenant-id:[POSTGRES_PASSWORD]@[your-domain]:5432/postgres"
```

```
1-- Check your tables are present2\dt public.*34-- Verify row counts on key tables5SELECT count(*) FROM auth.users;67-- Check extensions8SELECT * FROM pg_extension;
```

## What's included in the restore and what's not[#](#whats-included-in-the-restore-and-whats-not)

The database dump includes your schema, data, roles, RLS policies, database functions, triggers, and `auth.users`. However, several things require separate configuration on your self-hosted instance:

Requires manual setup

How to configure

JWT secrets and API keys

Generate new ones and update `.env`

Auth provider settings (OAuth, Apple, etc.)

Configure `GOTRUE_EXTERNAL_*` variables in `.env`

Edge functions

Manually copy to your self-hosted instance

Storage objects

Transfer separately (not covered in this guide)

SMTP / email settings

Configure `SMTP_*` variables in `.env`

Custom domains and DNS

Point your DNS to the self-hosted server

## Auth considerations[#](#auth-considerations)

Your `auth.users` table and related data are included in the database dump, so user accounts are preserved. However:

*   **JWT secrets differ** between your platform and self-hosted instances. Existing tokens issued by the platform project will not be valid. Users will need to re-authenticate.
*   **Social auth providers** (Apple, Google, GitHub, etc.) need to be configured in your self-hosted `.env` file. Set the relevant `GOTRUE_EXTERNAL_*` variables. See the Auth repository [README](https://github.com/supabase/auth) for all available options.
*   **Redirect URLs** in your OAuth provider consoles (Apple Developer, Google Cloud Console, etc.) must be updated to point to your self-hosted hostname instead of `*.supabase.co`.

## Postgres version compatibility[#](#postgres-version-compatibility)

Managed Supabase may run a newer Postgres version (Postgres 17) than the self-hosted Docker image (currently Postgres 15). The `supabase db dump` command produces plain SQL files that work across major Postgres versions.

Keep in mind:

*   The data dump may include Postgres 17-only settings or reference tables/columns from newer Auth and Storage versions that don't exist on self-hosted yet. See [Version mismatches](#version-mismatches-between-platform-and-self-hosted) in the troubleshooting section.
*   Run the restore on a test self-hosted instance first to identify any incompatibilities.
*   Check that all extensions you use are available on the self-hosted Postgres version.

## Troubleshooting[#](#troubleshooting)

### Version mismatches between platform and self-hosted[#](#version-mismatches-between-platform-and-self-hosted)

The platform may run a newer Postgres version (17 vs 15) and newer Auth service versions than self-hosted. The data dump can contain settings, tables, or columns that don't exist on your new self-hosted instance.

**Common issues in `data.sql`:**

*   `SET transaction_timeout = 0` - a Postgres 17-only setting that fails on Postgres 15
*   `COPY` statements for tables that don't exist on self-hosted (e.g., `auth.oauth_clients`, `storage.buckets_vectors`, `storage.vector_indexes`)
*   `COPY` statements with columns added in newer Auth versions (e.g., `auth.flow_state` with `oauth_client_state_id`, `linking_target_id`)

**Workaround:** Edit `data.sql` before restoring:

```
1# Comment out PG17-only transaction_timeout2sed -i 's/^SET transaction_timeout/-- &/' data.sql
```

For missing tables or column mismatches, comment out the relevant `COPY ... FROM stdin;` line and its corresponding `\.` terminator. Run the restore without `--single-transaction` first to identify all failures, then fix them and run the final restore with `--single-transaction`.

Keeping your self-hosted configuration [up to date](https://github.com/supabase/supabase/blob/master/docker/CHANGELOG.md) will minimize these gaps.

### Extension not available[#](#extension-not-available)

If the restore fails because an extension isn't available, check whether it's supported on your self-hosted Postgres version. You can list available extensions with:

```
1select * from pg_available_extensions;
```

### Connection refused[#](#connection-refused)

Make sure your self-hosted Postgres port is accessible. In the default [self-hosted Supabase](/docs/guides/self-hosting/docker#accessing-postgres) setup, the user is `postgres.your-tenant-id` with Supavisor on port `5432`.

### Legacy Studio configuration[#](#legacy-studio-configuration)

Studio in self-hosted Supabase historically used `supabase_admin` role (superuser) instead of `postgres`. Objects created via Studio UI were owned by `supabase_admin`. Check your `docker-compose.yml` [configuration](https://github.com/supabase/supabase/blob/2cb5befaa377a42b6d6ca152b98105b59054f2f4/docker/docker-compose.yml#L30) to see if `POSTGRES_USER_READ_WRITE` is set to `postgres`.

### Custom roles missing passwords[#](#custom-roles-missing-passwords)

If you created custom database roles with the `LOGIN` attribute on your platform project, their passwords are not included in the dump. Set them manually after restore:

```
1ALTER ROLE your_custom_role WITH PASSWORD 'new-password';
```

### Additional resources[#](#additional-resources)

*   [Backup and Restore using the CLI](/docs/guides/platform/migrating-within-supabase/backup-restore)
*   [Restore Dashboard backup](/docs/guides/platform/migrating-within-supabase/dashboard-restore)
