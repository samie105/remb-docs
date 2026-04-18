---
title: "Upgrade to Postgres 17"
source: "https://supabase.com/docs/guides/self-hosting/postgres-upgrade-17"
canonical_url: "https://supabase.com/docs/guides/self-hosting/postgres-upgrade-17"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:30.775Z"
content_hash: "d8f5fab7241f5d71d489499851a4e68e17a008690c01b8c74377dbcc1f781be9"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Upgrade to Postgres 17","Upgrade to Postgres 17"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Upgrade to Postgres 17","Upgrade to Postgres 17"]
nav_prev: {"path": "supabase/docs/guides/self-hosting/docker/index.md", "title": "Self-Hosting with Docker"}
nav_next: {"path": "supabase/docs/guides/self-hosting/restore-from-platform/index.md", "title": "Restore a Platform Project to Self-Hosted"}
---

# 

Upgrade to Postgres 17

## 

Start a new self-hosted Supabase deployment with Postgres 17, or upgrade an existing Postgres 15 installation.

* * *

Self-hosted Supabase ships with Postgres 15 by default. This guide covers two scenarios:

*   **New deployment** - start fresh with Postgres 17 (no existing data)
*   **Upgrade existing deployment** - migrate from Postgres 15 to Postgres 17 using `pg_upgrade`

## Before you begin[#](#before-you-begin)

*   Complete the [Self-Hosting with Docker](/docs/guides/self-hosting/docker) setup
*   Your current database image should be `supabase/postgres:15.x` (check with `docker inspect supabase-db --format '{{.Config.Image}}'`)

## New deployment with Postgres 17[#](#new-deployment-with-postgres-17)

If you are starting a new self-hosted Supabase instance with **no existing data**, use the Postgres 17 compose override:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml up -d
```

This uses the `docker-compose.pg17.yml` override file which swaps the database image:

```
1services:2  db:3    image: supabase/postgres:17.6.1.084
```

Always include both compose files when running commands. If you omit the override, Docker Compose falls back to the Postgres 15 image defined in `docker-compose.yml`.

The rest of the setup is the same as the standard Docker guide. All init scripts (`roles.sql`, `jwt.sql`, `webhooks.sql`, etc.) are compatible with Postgres 17.

If the new Postgres 17 container fails to start, make sure to check for an old `db-config` Docker volume. See [Postgres 17 fails to start with a leftover db-config volume](#postgres-17-fails-to-start-with-a-leftover-db-config-volume) for details.

## Upgrade an existing Postgres 15 deployment[#](#upgrade-an-existing-postgres-15-deployment)

Upgrading an existing deployment uses `pg_upgrade` to migrate data in place. The included upgrade scripts automates the full process.

### What the upgrade does[#](#what-the-upgrade-does)

1.  Pulls a specific Postgres 17 image and extracts upgrade binaries
2.  Pulls supplemental upgrade scripts from Supabase's [Postgres](https://github.com/supabase/postgres) repository
3.  Stops all self-hosted Supabase containers
4.  Runs `pg_upgrade` inside a temporary Postgres 15 container
5.  Runs additional tasks inside a temporary Postgres 17 container (re-enables extensions, applies patches, runs `VACUUM ANALYZE`)
6.  Swaps data directories (the original is kept as a backup)
7.  Starts self-hosted Supabase with Postgres 17
8.  Applies additional role migrations (new in Postgres 17)

### Create a backup[#](#create-a-backup)

##### Back up your data before upgrading

You should create your own independent backup in case of disk failure or other issues.

The upgrade script automatically preserves the pgsodium key and original data directory as `./volumes/db/data.bak.pg15` as the final step. However, it is recommended to **always** create your own independent backup before starting:

Back up the database data directory:

```
1cp -a ./volumes/db/data ./volumes/db/data-manual-backup
```

Back up the pgsodium encryption key (stored in a Docker named volume):

```
1docker compose run --rm db cat /etc/postgresql-custom/pgsodium_root.key > ./pgsodium_root.key.backup
```

The `db-config` Docker named volume contains the pgsodium root encryption key. If you lose this key and have vault secrets, they become unrecoverable. The `cp -a` above backs up the data directory but NOT the named volume.

Optionally, take a logical backup too:

```
1docker exec supabase-db pg_dumpall -h localhost -U supabase_admin > ./pg15_dump.sql
```

### Requirements[#](#requirements)

*   At least **2x your current database size + 5 GB** of free disk space (`pg_upgrade` copies the data directory; the upgrade tarball is ~1.2 GB compressed)
*   The script prompts for confirmation at each major step (use `--yes` to skip prompts)
*   All self-hosted Supabase containers must be running before starting the upgrade
*   Requires `bash`
*   Must be run as root or using `sudo`

### Extensions removed in Postgres 17[#](#extensions-removed-in-postgres-17)

The following extensions are **not available** in Postgres 17 builds. The upgrade script will prompt you to drop them if any of these are found:

Extension

Notes

`timescaledb`

Not built for Postgres 17

`plv8`

Not built for Postgres 17

`plcoffee`

Companion to plv8

`plls`

Companion to plv8

None of the above extensions are installed by default in the self-hosted Supabase setup. If you have installed any of them manually and need to keep them, **do not proceed** with the upgrade.

### Run the upgrade[#](#run-the-upgrade)

```
1sudo bash utils/upgrade-pg17.sh
```

The script might require your confirmation at some steps (e.g., while checking for disk space, or whether to disable extensions, or remove previous backups).

### After the upgrade[#](#after-the-upgrade)

After a successful upgrade, always use both compose files:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml up -d
```

To verify that Postgres 17 is running:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml exec db psql -U postgres -c "SELECT version();"
```

The original Postgres 15 data is preserved at `./volumes/db/data.bak.pg15`. The pgsodium root key is saved as `./volumes/db/pgsodium_root.key.bak.pg15`. The upgrade binaries tarball is cached at `./volumes/db/pg17_upgrade_bin_*.tar.gz`. Once you have verified that everything works, you can reclaim disk space:

```
1rm -rf ./volumes/db/data.bak.pg15 ./volumes/db/pgsodium_root.key.bak.pg15 ./volumes/db/pg17_upgrade_bin_*.tar.gz
```

Do not delete `data.bak.pg15` until you have verified the upgrade. Rollback is only possible while the backup exists.

### Rollback[#](#rollback)

If you need to revert to Postgres 15 (run the following commands as root):

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml down && \2rm -rf ./volumes/db/data && \3mv ./volumes/db/data.bak.pg15 ./volumes/db/data && \4docker compose run --rm db chown -R postgres:postgres /etc/postgresql-custom/ && \5docker compose up -d
```

This restores the original data directory, fixes file ownership on the `db-config` volume (Supabase's Postgres 15 and 17 images use different user IDs), and starts with the old Postgres 15 image.

### Custom Postgres configuration[#](#custom-postgres-configuration)

The Postgres 17 image loads any `.conf` files from `/etc/postgresql-custom/conf.d/` on startup. This directory is on the `db-config` named volume, so changes persist across restarts.

This is a Supabase Postgres 17 image feature. The Postgres 15 image does not load files from `conf.d/`.

To add custom Postgres settings, create a `.conf` file in the volume. Since `conf.d/` is on a Docker named volume (not a bind mount), you need to write through the container:

```
1docker exec supabase-db bash -c 'cat > /etc/postgresql-custom/conf.d/custom.conf << EOF2max_connections = 2003EOF'
```

Restart to apply (`max_connections` requires a full restart):

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml restart db
```

Verify the new settings:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml exec db psql -U postgres -c "SHOW max_connections;"
```

### Upgrade process details[#](#upgrade-process-details)

The upgrade script delegates the core migration work to two scripts from the [supabase/postgres](https://github.com/supabase/postgres) repository (`ansible/files/admin_api_scripts/pg_upgrade_scripts/`).

**Phase 1 - Migrate data (Postgres 15 container):**

1.  Disables extensions that are incompatible with `pg_upgrade` (`pg_graphql`, `pg_stat_monitor`, `pg_backtrace`, `wrappers`, `pgrouting`) and generates SQL to re-enable them after the upgrade
2.  Temporarily grants superuser to the `postgres` role (required by `pg_upgrade`)
3.  Extracts the previously saved Postgres 17 binaries tarball and runs `initdb` to create a new empty database
4.  Runs `pg_upgrade --check` to verify the upgrade can succeed before making changes
5.  Stops Postgres 15 and runs `pg_upgrade` to migrate all data to the new database
6.  Copies Postgres configuration and the SQL scripts generated by `pg_upgrade` to a staging directory for the next phase

**Phase 2 - Finalize (Postgres 17 container):**

1.  Moves the upgraded data directory into place and starts Postgres 17
2.  Applies extension compatibility patches for Wrappers, `pg_net`, `pg_cron`, and Vault (fixes ownership, grants, and foreign server options)
3.  Runs the SQL scripts generated by `pg_upgrade` to update system catalogs and extension versions
4.  Re-enables the extensions that were disabled in phase 1
5.  Grants predefined roles (`pg_monitor`, `pg_read_all_data`, `pg_signal_backend`, and on Postgres 16+ also `pg_create_subscription`) and revokes the temporary superuser grant
6.  Restarts Postgres and runs `vacuumdb --all --analyze-in-stages` to rebuild optimizer statistics

After both phases complete, the upgrade script preserves the original Postgres 15 data directory as a backup and starts the full Supabase stack with Postgres 17.

## Troubleshooting[#](#troubleshooting)

### pg\_upgrade fails with replication slot errors[#](#pgupgrade-fails-with-replication-slot-errors)

`pg_upgrade` cannot proceed if there are active replication slots. Default self-hosted installs don't have any, but if you set up logical replication or have custom replication configurations, drop the slots before upgrading:

```
1docker exec supabase-db psql -h localhost -U supabase_admin -d postgres -c "2    SELECT pg_drop_replication_slot(slot_name)3    FROM pg_replication_slots;4"
```

Then re-run the upgrade script. Replication slots will need to be manually recreated after the upgrade.

### "Permission denied" on the data directory[#](#permission-denied-on-the-data-directory)

The upgrade script fixes file ownership automatically (Postgres 15 and 17 use different UIDs). If you still see permission errors, run:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml run --rm db \2chown -R postgres:postgres /var/lib/postgresql/data
```

### pgsodium / Supabase Vault errors[#](#pgsodium--supabase-vault-errors)

The `db-config` named volume contains the pgsodium root encryption key at `/etc/postgresql-custom/pgsodium_root.key`. This volume is preserved during the upgrade. Never run `docker compose down -v` as this destroys named volumes and makes vault secrets unrecoverable.

### Services fail to connect after upgrade[#](#services-fail-to-connect-after-upgrade)

Restart all services to pick up the new database:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml down && \2docker compose -f docker-compose.yml -f docker-compose.pg17.yml up -d
```

### Disk space issues during upgrade[#](#disk-space-issues-during-upgrade)

The upgrade needs space for:

*   The upgrade tarball (~1.2 GB compressed, cached for re-runs)
*   A full copy of your database (created by `pg_upgrade`)
*   The original data (kept as backup)

The script uses `/tmp` (or `TMPDIR` if set) for its staging directory, which holds the downloaded tarball and upgrade scripts. If your `/tmp` filesystem is small or mounted with limited space, you can point it to a different location, e.g.:

```
1sudo TMPDIR=/mnt/my-tmp bash utils/upgrade-pg17.sh
```

If you run out of space mid-upgrade, the safest path is to roll back and free up disk space before retrying.

### Postgres 17 fails to start with a leftover db-config volume[#](#postgres-17-fails-to-start-with-a-leftover-db-config-volume)

If you are starting a **fresh** Postgres 17 deployment (not upgrading from Postgres 15) and the container fails to start, the most likely cause is a leftover `db-config` volume from a previous Postgres 15 installation. Try to start the containers without the `-d` option and/or check the logs for errors about `postgresql.conf` or other configuration mismatch.

To fix, remove the old volume and let Postgres 17 initialize a clean configuration:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml down && \2docker volume rm $(docker volume ls --filter "name=db-config" --format '{{.Name}}') && \3docker compose -f docker-compose.yml -f docker-compose.pg17.yml up -d
```

Removing the `db-config` volume destroys any custom Postgres configuration and the pgsodium root key. Only do this for fresh installations with no existing data or vault secrets.

### Restoring from a manual backup[#](#restoring-from-a-manual-backup)

If the upgrade fails and the script's built-in rollback isn't sufficient, restore from the manual backups created in the [Create a backup](#create-a-backup) step:

Restore the data:

```
1docker compose -f docker-compose.yml -f docker-compose.pg17.yml down && \2rm -rf ./volumes/db/data && \3cp -a ./volumes/db/data-manual-backup ./volumes/db/data
```

Restore the pgsodium key to the `db-config` volume:

```
1docker compose run --rm db \2  sh -c 'cat > /etc/postgresql-custom/pgsodium_root.key' < ./pgsodium_root.key.backup && \3docker compose run --rm db \4  chown postgres:postgres /etc/postgresql-custom/pgsodium_root.key && \5docker compose run --rm db \6  chmod 600 /etc/postgresql-custom/pgsodium_root.key
```

Start Postgres 15:

```
1docker compose up -d
```

