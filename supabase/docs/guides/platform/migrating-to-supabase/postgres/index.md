---
title: "Migrate from Postgres to Supabase"
source: "https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres"
canonical_url: "https://supabase.com/docs/guides/platform/migrating-to-supabase/postgres"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:39.439Z"
content_hash: "6e0e83433dc06a659d1035be1c41af32b5d2746d134dd6afa03f88a098a48b4d"
menu_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","Postgres","Postgres"]
section_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","Postgres","Postgres"]
nav_prev: {"path": "supabase/docs/guides/platform/migrating-to-supabase/render/index.md", "title": "Migrate from Render to Supabase"}
nav_next: {"path": "supabase/docs/guides/platform/migrating-to-supabase/vercel-postgres/index.md", "title": "Migrate from Vercel Postgres to Supabase"}
---

# 

Migrate from Postgres to Supabase

## 

Migrate your existing Postgres database to Supabase.

* * *

This is a guide for migrating your Postgres database to [Supabase](https://supabase.com). Supabase is a robust and open-source platform. Supabase provides all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security, and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate your Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

This guide provides three methods for migrating your Postgres database to Supabase:

1.  **Google Colab** - Guided notebook with copy-paste workflow
2.  **Manual Dump/Restore** - CLI approach, works for all versions
3.  **Logical Replication** - Minimal downtime, requires Postgres 10+

## Connection modes[#](#connection-modes)

Supabase provides the following connection modes:

*   Direct connection
*   Supavisor session mode
*   Supavisor transaction mode

Use Supavisor session mode for the database migration tasks (pg\_dump/restore and logical replication).

## Method 1: Google Colab (easiest)[#](#method-1-google-colab-easiest)

Supabase provides a Google Colab migration notebook for a guided migration experience: [Supabase Migration Colab Notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb)

This is ideal if you prefer a step-by-step, copy-paste workflow with minimal setup.

## Method 2: Manual dump/restore[#](#method-2-manual-dumprestore)

This method works for all Postgres versions using CLI tools.

### Prerequisites[#](#prerequisites)

#### Source Postgres requirements[#](#source-postgres-requirements)

*   Connection string with rights to run `pg_dump`
*   No special settings required for dump/restore
*   Network access from migration VM

#### Migration environment[#](#migration-environment)

*   Cloud VM running Ubuntu in the same region as source or target database
*   Postgres client tools matching your source database version
*   tmux for session persistence
*   Sufficient disk space (usually ~50% of source database size is enough, but varies case by case)

### Pre-Migration checklist[#](#pre-migration-checklist)

```
1-- Check database size2select pg_size_pretty(pg_database_size(current_database())) as size;34-- Check Postgres version5select version();67-- List installed extensions8select * from pg_extension order by extname;910-- Check active connections11select count(*) from pg_stat_activity;
```

#### Check available extensions in Supabase[#](#check-available-extensions-in-supabase)

```
1-- Connect to your Supabase database and check available extensions2SELECT name, comment FROM pg_available_extensions ORDER BY name;34-- Compare with source database extensions5SELECT extname FROM pg_extension ORDER BY extname;67-- Install needed extensions8CREATE EXTENSION IF NOT EXISTS extension_name;
```

### Step 1: Set up migration VM[#](#step-1-set-up-migration-vm)

For optimal performance, run the migration from a cloud VM, not your local machine. The VM should be in the same region as either your source or target database to optimize network performance. See the Resource Requirements table in Step 2 for VM sizing recommendations.

#### Set up Ubuntu VM[#](#set-up-ubuntu-vm)

```
1# Install Postgres client and tools2sudo apt update3sudo apt install software-properties-common4sudo sh -c 'echo "deb http://apt.Postgres.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'5wget --quiet -O - https://www.Postgres.org/media/keys/ACCC4CF8.asc | sudo apt-key add -6sudo apt update7sudo apt install Postgres-client-17 tmux htop iotop moreutils89# Start or attach to tmux session10tmux a -t migration || tmux new -s migration
```

### Step 2: Prepare Supabase project[#](#step-2-prepare-supabase-project)

1.  Create a Supabase project at [supabase.com/dashboard](/dashboard)
2.  Note your database password
3.  Install required extensions via SQL or Dashboard
4.  Get your connection string:
    *   Go to **Project → Settings → Database → Connection Pooling**
    *   Select **Session pooler** (port 5432) and copy the connection string
    *   Connection format: `Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres`

**Important Notes**:

*   **Users/roles are not migrated** - You'll need to recreate roles and privileges after import ([Supabase Roles Guide](/blog/postgres-roles-and-privileges))
*   **Row Level Security (RLS) status on tables is not migrated** - You'll need to enable RLS for tables after migration.

**Resource Requirements**:

Database Size

Recommended Compute

Recommended VM

Action Required

< 10 GB

Default

2 vCPUs, 4 GB RAM

None

10-100 GB

Default-Small

4 vCPUs, 8 GB RAM

Consider compute upgrade

100-500 GB

Large compute

8 vCPUs, 16 GB RAM, NVMe

Upgrade compute before restore

500 GB - 1 TB

XL compute

16 vCPUs, 32 GB RAM, NVMe

Upgrade compute before restore

\> 1 TB

Custom

Custom

[Contact support](/dashboard/support/new) first

Also, you can temporarily increase compute size and/or disk IOPS and throughput via Settings → Compute and Disk if you want faster database restore (you can use larger -j for pg\_restore if you do so).

### Step 3: Create database dump[#](#step-3-create-database-dump)

#### Set source database to read only mode for production migration[#](#set-source-database-to-read-only-mode-for-production-migration)

If doing a maintenance window migration, prevent data changes:

```
1-- Connect to source database and run:2ALTER DATABASE your_database_name SET default_transaction_read_only = true;
```

For testing without a maintenance window, skip this step but use lower -j values.

#### Dump the database[#](#dump-the-database)

```
1# Determine number of parallel jobs based on:2# - Source database CPU cores (don't saturate production)3# - VM CPU cores4# - For testing without maintenance window: use lower values to be gentle5# - For production with maintenance window: can use higher values67DUMP_JOBS=4  # Adjust based on your setup89# Check available cores on VM10nproc1112# Create dump with progress logging13pg_dump \14  --host=<source_host> \15  --port=<source_port> \16  --username=<source_username> \17  --dbname=<source_database> \18  --jobs=$DUMP_JOBS \19  --format=directory \20  --no-owner \21  --no-privileges \22  --no-subscriptions \23  --verbose \24  --file=./db_dump 2>&1 | ts | tee -a dump.log
```

**Notes about dump flags**:

*   `--no-owner --no-privileges`: Applied at dump time to prevent Supabase user management conflicts. While these could be used in pg\_restore instead, applying them during dump keeps the dump file cleaner and more portable.
*   `--no-subscriptions`: Logical replication subscriptions won't work in the target
*   The dump captures all data and schema but excludes ownership/privileges that would conflict with Supabase's managed environment
*   To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
*   To exclude a schema: `--exclude-schema=PATTERN`.
*   To only migrate a single table: `--table=PATTERN`.
*   To exclude a table: `--exclude-table=PATTERN`.

Run `pg_dump --help` for a full list of options.

#### Recommended parallelization (-j values)[#](#recommended-parallelization--j-values)

Database Size

Testing (no maintenance window)

Production (with maintenance window)

Limiting Factor

< 10 GB

2

4

Source CPU

10-100 GB

2-4

8

Source CPU

100-500 GB

4

16

Disk IOPS

500 GB - 1 TB

4-8

16-32

Disk IOPS + CPU

**Note**: For testing without a maintenance window, use lower -j values to avoid impacting production performance.

### Step 4: Restore to Supabase[#](#step-4-restore-to-supabase)

#### Set connection and restore[#](#set-connection-and-restore)

```
1# Set Supabase connection (Session Pooler on port 5432 or direct connection)2export SUPABASE_DB_URL="Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres"34# Determine restore parallelization based on your Supabase compute size:5# Free tier: 2 cores → use -j 26# Small compute: 2 cores → use -j 27# Medium compute: 4 cores → use -j 48# Large compute: 8 cores → use -j 89# XL compute: 16 cores → use -j 161011RESTORE_JOBS=8  # Adjust based on your Supabase compute size1213# Restore the dump (parallel mode)14# Note: -j cannot be used with --single-transaction15pg_restore \16  --dbname="$SUPABASE_DB_URL" \17  --jobs=$RESTORE_JOBS \18  --format=directory \19  --no-owner \20  --no-privileges \21  --verbose \22  ./db_dump 2>&1 | ts | tee -a restore.log
```

If restore fails with extension errors, check that errors are only extension-related.

### Step 5: Post-Migration tasks[#](#step-5-post-migration-tasks)

#### Update statistics (important)[#](#update-statistics-important)

```
1psql "$SUPABASE_DB_URL" -c "VACUUM VERBOSE ANALYZE;"
```

For Postgres 18+, pg\_dump includes statistics with `--with-statistics`, but you should still run VACUUM for optimal performance.

#### Verify migration[#](#verify-migration)

```
1-- Check row counts2select schemaname, tablename, n_live_tup3from pg_stat_user_tables4order by n_live_tup desc5limit 20;6-- Verify data with application-specific queries
```

#### Re-enable writes on source (if keeping it)[#](#re-enable-writes-on-source-if-keeping-it)

```
1ALTER DATABASE your_database_name SET default_transaction_read_only = false;
```

### Migration time estimates[#](#migration-time-estimates)

Database Size

Dump Time

Restore Time

Total Time

10 GB

~5 min

~10 min

~15 min

100 GB

~30 min

~45 min

~1.5 hours

500 GB

~2 hours

~3 hours

~5 hours

1 TB

~4 hours

~6 hours

~10 hours

_Times vary based on hardware, network, and parallelization settings_

### Important notes[#](#important-notes)

1.  **Region proximity matters**: VM should be in the same region as the source or target for best performance
2.  **Downgrade migrations**: While technically possible in some cases, highly not recommended
3.  **Testing without downtime**: Use lower `-j` values for pg\_dump to avoid impacting production
4.  **For pg\_restore**: Can use full parallelization regardless of production impact
5.  **Monitor resources**: Watch CPU, disk I/O with `htop`, `iotop`
6.  **Disk I/O**: Often the bottleneck before network bandwidth

* * *

## Method 3: Logical replication[#](#method-3-logical-replication)

This method allows migration with minimal downtime using Postgres's logical replication feature. Requires Postgres 10+ on both source and target.

### When to use logical replication[#](#when-to-use-logical-replication)

*   You need minimal downtime (minutes instead of hours)
*   Source database is Postgres 10 or higher
*   You can configure logical replication on the source
*   Database has high write activity that can't be paused for long

### Source Postgres prerequisites[#](#source-postgres-prerequisites)

#### Access & privileges[#](#access--privileges)

*   Connection string with rights to CREATE PUBLICATION and read tables
*   Superuser or replication privileges recommended

#### Required settings for logical replication[#](#required-settings-for-logical-replication)

*   `wal_level = logical`
*   `max_wal_senders ≥ 1`
*   `max_replication_slots ≥ 1`
*   Sufficient `max_connections` (current + 1 for subscription)

#### Replica identity[#](#replica-identity)

Every table receiving UPDATE/DELETE must have a replica identity (typically a PRIMARY KEY). For tables without one:

```
1ALTER TABLE schema.table_name REPLICA IDENTITY FULL;
```

#### Non-Replicated items[#](#non-replicated-items)

*   **DDL changes** (schema modifications)
*   **Sequences** (need manual sync)
*   **Large Objects (LOBs)** (use dump/restore or store in regular bytea columns)

Plan a schema freeze, sequence sync before cutover, and handle LOBs separately.

### Step 1: Configure source database[#](#step-1-configure-source-database)

Edit Postgres configuration files:

#### Postgres.conf[#](#postgresconf)

```
1# Set Supabase connection (Session Pooler on port 5432 or direct connection)2export SUPABASE_DB_URL="Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres"34# Set WAL level to logical5wal_level = logical67# Ensure sufficient replication slots8max_replication_slots = 10910# Ensure sufficient WAL senders11max_wal_senders = 101213# Set appropriate max_connections (current connections + 1 for subscription)14max_connections = 200  # Adjust based on your needs1516# Optional: Enable SSL for secure replication17ssl = on1819# Allow connections from Supabase20listen_addresses = '*'  # Or specific IP addresses
```

#### pg\_hba.conf[#](#pghbaconf)

```
1# Allow replication connections from Supabase2# Replace <supabase_ip_range> with actual Supabase IP range3host    replication     all     <supabase_ip_range>    md54host    all            all     <supabase_ip_range>    md556# With SSL:7hostssl replication     all     <supabase_ip_range>    md58hostssl all            all     <supabase_ip_range>    md5
```

Restart Postgres:

```
1sudo systemctl restart Postgres2sudo systemctl status Postgres
```

### Step 2: Verify configuration[#](#step-2-verify-configuration)

```
1-- Should return 'logical'2SHOW wal_level;34-- Check other parameters5SHOW max_replication_slots;6SHOW max_wal_senders;78-- Check current connections9SELECT count(*) FROM pg_stat_activity;
```

### Step 3: Check and set replica identity[#](#step-3-check-and-set-replica-identity)

```
1-- Find tables without primary keys2SELECT n.nspname, c.relname3FROM pg_class c4JOIN pg_namespace n ON n.oid = c.relnamespace5LEFT JOIN pg_constraint pk ON pk.conrelid = c.oid AND pk.contype = 'p'6WHERE c.relkind = 'r'7  AND pk.oid IS NULL8  AND n.nspname NOT IN ('pg_catalog','information_schema');910-- For tables without a primary key, set REPLICA IDENTITY FULL11ALTER TABLE my_schema.my_table REPLICA IDENTITY FULL;
```

### Step 4: Export and restore schema only[#](#step-4-export-and-restore-schema-only)

```
1# Export schema from source2pg_dump \3  -h <source_host> \4  -U <source_user> \5  -p <source_port> \6  -d <source_database> \7  --schema-only \8  --no-privileges \9  --no-subscriptions \10  --format=directory \11  -f ./schema_dump1213# Restore schema to Supabase (use Session Pooler)14pg_restore \15  --dbname="$SUPABASE_DB_URL" \16  --format=directory \17  --schema-only \18  --no-privileges \19  --single-transaction \20  --verbose \21  ./schema_dump
```

### Step 5: Create publication on source[#](#step-5-create-publication-on-source)

```
1-- Create publication for all tables2CREATE PUBLICATION supabase_migration FOR ALL TABLES;34-- Or for specific tables only (doesn't require superuser)5CREATE PUBLICATION supabase_migration FOR TABLE6  schema1.table1,7  schema1.table2,8  public.table3;910-- Verify publication was created11SELECT * FROM pg_publication;
```

### Step 6: Create subscription on Supabase[#](#step-6-create-subscription-on-supabase)

Connect to your Supabase database:

```
1-- Create subscription with SSL (recommended)2CREATE SUBSCRIPTION supabase_subscription3CONNECTION 'host=<source_host> port=<source_port> user=<source_user> password=<source_password> dbname=<source_database> sslmode=require'4PUBLICATION supabase_migration;56-- Or without SSL (if source doesn't support it)7CREATE SUBSCRIPTION supabase_subscription8CONNECTION 'host=<source_host> port=<source_port> user=<source_user> password=<source_password> dbname=<source_database> sslmode=disable'9PUBLICATION supabase_migration;
```

### Step 7: Monitor replication status[#](#step-7-monitor-replication-status)

```
1-- On Supabase (subscriber) - check subscription status2select * from pg_subscription_rel;34-- srsubstate = 'r' means ready (synchronized)5-- srsubstate = 'i' means initializing6-- srsubstate = 'd' means data is being copied78-- Overall subscription status9select * from pg_stat_subscription;1011-- On source database - check replication status12select * from pg_stat_replication;1314-- Check replication lag15select16  slot_name,17  pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) as lag_size18from pg_replication_slots;
```

Wait until all tables show `srsubstate = 'r'` (ready) status.

### Step 8: Synchronize sequences[#](#step-8-synchronize-sequences)

After initial data sync is complete, but BEFORE switching to Supabase:

```
1# Set source to read-only2psql -h <source_host> -c "ALTER DATABASE <source_database> SET default_transaction_read_only = true;"34# Export sequences from source5pg_dump \6  -h <source_host> \7  -U <source_user> \8  -p <source_port> \9  -d <source_database> \10  --data-only \11  --table='*_seq' \12  --table='*_id_seq' > sequences.sql1314# Import sequences to Supabase15psql "$SUPABASE_DB_URL" -f sequences.sql
```

### Step 9: Switch to Supabase[#](#step-9-switch-to-supabase)

1.  Ensure replication lag is zero:

```
1-- On Supabase2select * from pg_stat_subscription;3-- Check that latest_end_lsn is current
```

2.  Stop writes to the source database (if not already read-only)
    
3.  Drop subscription on Supabase:
    

```
1DROP SUBSCRIPTION supabase_subscription;
```

4.  Update application connection strings to point to Supabase
    
5.  Verify application functionality
    

### Step 10: Cleanup[#](#step-10-cleanup)

On source database (after successful migration):

```
1-- Remove publication2DROP PUBLICATION supabase_migration;34-- Check and remove any remaining replication slots5SELECT * FROM pg_replication_slots;6DROP REPLICATION SLOT slot_name;  -- if any remain78-- The source database should remain read-only or be decommissioned9-- Do NOT re-enable writes to avoid a split-brain scenario!
```

### Troubleshooting logical replication[#](#troubleshooting-logical-replication)

Issue

Solution

"could not connect to the publisher"

Check network connectivity, firewall rules, pg\_hba.conf

"role does not exist"

Ensure replication user exists on source with REPLICATION privilege

"publication does not exist"

Verify publication name and that it was created successfully

Replication lag growing

Check network bandwidth, source database load, add more WAL senders

Tables stuck in `i` state

Check for locks on source tables, verify table structure matches

"out of replication slots"

Increase max\_replication\_slots in Postgres.conf

### Important limitations[#](#important-limitations)

*   **DDL changes**: Schema modifications are not replicated - freeze schema during migration
*   **Sequences**: Need manual synchronization before cutover
*   **Large Objects (LOBs)**: Not replicated - use dump/restore or store in regular bytea columns
*   **Custom types**: May need special handling
*   **Users and roles**: Must be recreated manually on Supabase

For detailed restrictions, see [Postgres Logical Replication Restrictions](https://www.Postgres.org/docs/current/logical-replication-restrictions.html)

### When to use which method[#](#when-to-use-which-method)

**Use Dump/Restore when:**

*   Downtime window is acceptable
*   Source is Postgres < 10
*   Simpler process preferred
*   Cannot configure logical replication on the source

**Use Logical Replication when:**

*   Minimal downtime required
*   Postgres 10+ on both sides
*   Can modify source configuration
*   Have replication privileges

## Getting help[#](#getting-help)

*   For databases > 150 GB: [Contact Supabase support](/dashboard/support/new) before starting
*   [Supabase Dashboard Support](/dashboard/support/new)
*   [Supabase Discord](https://discord.supabase.com)
*   [Postgres Roles and Privileges Guide](/blog/postgres-roles-and-privileges)
*   [Row Level Security Guide](/docs/guides/database/postgres/row-level-security)
