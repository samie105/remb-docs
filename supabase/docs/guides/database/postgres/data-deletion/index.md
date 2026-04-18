---
title: "Deleting data and dropping objects safely"
source: "https://supabase.com/docs/guides/database/postgres/data-deletion"
canonical_url: "https://supabase.com/docs/guides/database/postgres/data-deletion"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:29.101Z"
content_hash: "3ba542de60ae3a0a73e7dbfdacb6512ad3fed66231a13542aff4543fcd68e5c7"
menu_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Deleting data and dropping objects safely","Deleting data and dropping objects safely"]
section_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Deleting data and dropping objects safely","Deleting data and dropping objects safely"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/configuration/index.md", "title": "Database configuration"}
nav_next: {"path": "supabase/docs/guides/database/postgres/dropping-all-tables-in-schema/index.md", "title": "Drop all tables in a Postgres schema"}
---

# 

Deleting data and dropping objects safely

* * *

Deleting rows and dropping database objects are routine operations, but on a live database they can lock tables, block queries, and cause downtime. This guide covers practical strategies for keeping these operations safe and fast.

## Preparing to delete[#](#preparing-to-delete)

*   Test in a staging environment
*   Ensure you have a recent backup
*   Confirm the table dependencies and foreign key constraints
*   Drop dependent objects explicitly, use [CASCADE](/docs/guides/database/postgres/cascade-deletes) with caution
*   Choose a low traffic time to run the operation
*   Run operations inside a [migration](/docs/guides/deployment/database-migrations)
*   Set timeouts, such as `lock_timeout` and `statement_timeout`

### Identifying dependencies[#](#identifying-dependencies)

The system catalog tables `pg_class`, `pg_constraint`, and `pg_depend` can be used to identify dependencies:

```
1-- Find tables that depend on a specific table2select3  d.classid::regclass as dependent_object,4  d.objid::regclass as dependent_object_id,5  d.refclassid::regclass as referenced_object,6  d.refobjid::regclass as referenced_object_id7from pg_depend d8where d.refobjid = 'public.logs'::regclass;
```

If the object you want to delete has dependencies, you'll need to drop those first or use `CASCADE` which will automatically drop all related objects.

## Data deletion strategies[#](#data-deletion-strategies)

There are several ways to delete data from a table and the approach you choose depends on how much you want to delete.

### Small deletes[#](#small-deletes)

For tables with less than a few thousand rows, a `DELETE` operation is fine:

```
1delete from logs2where created_at < now() - interval '90 days';
```

This acquires a `ROW EXCLUSIVE` lock on the table, which still allows other `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements to run concurrently. For small row counts, the operation completes quickly and has minimal impact.

### Large deletes[#](#large-deletes)

Deleting millions of rows in a single statement can hold locks for a long time, generate WAL (Write-Ahead Log) traffic, and impact replication. Instead, delete in batches:

```
1-- Delete 5,000 rows at a time2DELETE FROM logs3WHERE id IN (4  SELECT id5  FROM logs6  WHERE created_at < now() - interval '90 days'7  LIMIT 50008);
```

This approach has the benefit of controlling when it runs, locking for a shorter period of time and minimising impact on other transactions.

If you know in advance that such large deletes will have to happen in the business cycle of your database, then you should seriously think about using (table parititioning)\[/docs/guides/database/partitions\] as a management tool.

### Soft deletes[#](#soft-deletes)

If you need to "delete" data but want the option to recover it, consider a soft-delete pattern:

```
1alter table orders2add column deleted_at timestamptz;34-- "Delete" a row5update orders6set deleted_at = now()7where id = 42;
```

Then exclude soft-deleted rows in your queries or views:

```
1create view active_orders as2  select * from orders where deleted_at is null;
```

Combine soft deletes with a scheduled hard-delete job (using [pg\_cron](/docs/guides/database/extensions/pg_cron)) to permanently remove old soft-deleted rows in batches during low-traffic periods.

### Deleting all data[#](#deleting-all-data)

If you need to delete all data from a table, consider using `TRUNCATE` instead of `DELETE`:

```
1truncate table logs;
```

`TRUNCATE` is much faster than `DELETE` because it doesn't generate individual row-level WAL entries and doesn't scan the table. It also resets any auto-incrementing sequences.

## Object deletion strategies[#](#object-deletion-strategies)

### Dropping tables[#](#dropping-tables)

Dropping a table removes it and all its data permanently. Always use `IF EXISTS` to avoid errors in migrations:

```
1drop table if exists old_analytics;
```

`DROP TABLE` acquires an `ACCESS EXCLUSIVE` lock, which blocks **all** other operations on the table, including reads. On a busy table, this can queue up behind long-running queries. See [Monitoring locks](#monitoring-locks) below.

### Dropping columns[#](#dropping-columns)

Dropping a column is a metadata-only operation in Postgres — it doesn't rewrite the table. However, it still requires an `ACCESS EXCLUSIVE` lock:

```
1alter table users2drop column if exists legacy_field;
```

Since the lock is brief (metadata-only), this is generally safe. But on a table with many concurrent transactions, even a brief `ACCESS EXCLUSIVE` lock can queue behind long-running queries. Use a lock timeout to avoid waiting indefinitely:

```
1set local lock_timeout = '5s';2alter table users drop column if exists legacy_field;
```

If the statement times out, retry during a quieter period.

### Dropping indexes[#](#dropping-indexes)

Dropping a regular index takes an `ACCESS EXCLUSIVE` lock on the index but **not** on the table, so reads and writes to the table continue uninterrupted:

```
1drop index if exists idx_users_legacy_field;
```

The `inspect` command in the [Supabase CLI](/docs/reference/cli/supabase-inspect-db-index-stats) can help you identify unused indexes:

```
1supabase inspect db index-stats
```

## Monitoring[#](#monitoring)

### Check for blocked queries[#](#check-for-blocked-queries)

Query `pg_locks` and `pg_stat_activity` to see currently active queries and queries waiting for locks.

The [Supabase CLI](/docs/reference/cli/supabase-inspect-db-locks) provides commands to view these metrics:

```
1supabase inspect db locks2supabase inspect db blocking
```

### Monitor table bloat after large deletes[#](#monitor-table-bloat-after-large-deletes)

When deleting a large number of rows, the space is not always reclaimed and available for use. In normal cases, the rows are marked as deleted but the space is not immediately freed. You can monitor table bloat to see if the space is being reclaimed:

```
1supabase inspect db bloat
```

## Reclaiming disk space[#](#reclaiming-disk-space)

To reclaim the disk space freed by deleted rows, Postgres' autovacuum process runs automatically to mark deleted rows as reusable, but it may not always keep up with large deletes.

If autovacuum is not keeping up, you can trigger a manual vacuum:

```
1vacuum (verbose) logs;
```

For reclaiming disk space (not just marking tuples as reusable), use `VACUUM FULL` — but be aware this rewrites the entire table and takes an `ACCESS EXCLUSIVE` lock:

```
1-- This locks the table for the duration — use during maintenance windows only2vacuum full logs;
```

The most efficient way to reclaim disk space, without locks, is to use [pg\_repack](/docs/guides/database/extensions/pg_repack).

## Related links[#](#related-links)

*   [Safe Cascading Deletes](/docs/guides/database/postgres/cascade-deletes)
*   [Inspecting your Database](/docs/guides/database/inspect)
*   [Understanding Database and Disk Size](/docs/guides/platform/database-size)
*   [Bloat in Postgres](/docs/blog/postgres-bloat)

