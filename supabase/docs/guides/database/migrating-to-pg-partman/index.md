---
title: "Migrate from TimescaleDB to pg_partman"
source: "https://supabase.com/docs/guides/database/migrating-to-pg-partman"
canonical_url: "https://supabase.com/docs/guides/database/migrating-to-pg-partman"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:33.390Z"
content_hash: "77298fe5b4e212d3c074f6083f90070d1e05198e4d773676c02be4a7085332dd"
menu_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Migrating to pg_partman","Migrating to pg_partman"]
section_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Migrating to pg_partman","Migrating to pg_partman"]
nav_prev: {"path": "../metabase/index.md", "title": "Connecting to Metabase"}
nav_next: {"path": "../orioledb/index.md", "title": "OrioleDB Overview"}
---

# 

Migrate from TimescaleDB to pg\_partman

* * *

Starting from Postgres 17, Supabase projects do not have the `timescaledb` extension available. If your project relies on TimescaleDB hypertables, you will need to migrate to standard Postgres tables before upgrading.

This guide shows one approach to migrate a hypertable to a native Postgres partitioned table and optionally configure `pg_partman` to automate ongoing partition maintenance. The approach outlined in this guide can also be used for traditional partitioned tables.

## Before you begin[#](#before-you-begin)

*   Test the migration path in a staging environment (for example by creating a copy of your production project or using branching).
*   Review your application for TimescaleDB-specific SQL usage (for example `time_bucket()`, compression policies). Those features are not provided by `pg_partman`.

## Migration overview[#](#migration-overview)

1.  Create a new partitioned table.
2.  Copy data from the hypertable to the new table.
3.  Swap over and drop the hypertable.
4.  Configure `pg_partman` (optional) and schedule maintenance.

## Example: Migrate `messages` from hypertable to native partitions[#](#example-migrate-messages-from-hypertable-to-native-partitions)

This example assumes a `messages` hypertable partitioned by `sent_at`.

### 1\. Rename the existing hypertable[#](#1-rename-the-existing-hypertable)

This keeps the original data in place while you create a new partitioned table with the original name.

```
1alter table public.messages rename to ht_messages;
```

### 2\. Create a new partitioned table[#](#2-create-a-new-partitioned-table)

When using native partitioning, the partitioning column must be included in any unique index (including the primary key).

```
1create table public.messages (2  like public.ht_messages including all,3  primary key (sent_at, id)4)5partition by range (sent_at);
```

### 3\. Copy data into the new table[#](#3-copy-data-into-the-new-table)

For large tables, consider copying in batches (for example by time range) during a maintenance window.

```
1insert into public.messages2select *3from public.ht_messages;
```

### 4\. Drop the old hypertable (and TimescaleDB)[#](#4-drop-the-old-hypertable-and-timescaledb)

Only drop the extension once you’ve migrated all hypertables and no other objects depend on it.

```
1drop table public.ht_messages;23drop extension if exists timescaledb;
```

### 5\. Configure `pg_partman` (optional)[#](#5-configure-pgpartman-optional)

Enable `pg_partman` and register your table so partitions are created ahead of time.

```
1create schema if not exists partman;2create extension if not exists pg_partman with schema partman;34select partman.create_parent(5  p_parent_table := 'public.messages',6  p_control := 'sent_at',7  p_type := 'range',8  p_interval := '7 days',9  p_premake := 7,10  p_start_partition := '2025-01-01 00:00:00'11);
```

## Keep partitions up to date[#](#keep-partitions-up-to-date)

`pg_partman` requires running maintenance to pre-make partitions and apply retention policies.

```
1call partman.run_maintenance_proc();
```

To automate this, schedule it with `pg_cron`.

```
1create extension if not exists pg_cron;23select cron.schedule('@daily', $$call partman.run_maintenance_proc()$$);
```

## Additional resources[#](#additional-resources)

*   [Partitioning your tables](/docs/guides/database/partitions).
*   [`pg_partman` documentation](/docs/guides/database/extensions/pg_partman)
*   [`pg_partman` migration guides](https://github.com/pgpartman/pg_partman/blob/development/doc/migrate_to_partman.md)
