---
title: "PostgreSQL: Documentation: 18: DROP INDEX"
source: "https://www.postgresql.org/docs/current/sql-dropindex.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropindex.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:47.530Z"
content_hash: "4a75963754b0a269426bfe786d1de786c7957558717c107f44ceef9bed2aa06d"
menu_path: ["PostgreSQL: Documentation: 18: DROP INDEX"]
section_path: []
nav_prev: {"path": "postgres/docs/current/contrib-dblink-fetch.html/index.md", "title": "PostgreSQL: Documentation: 18: dblink_fetch"}
nav_next: {"path": "postgres/docs/current/passwordcheck.html/index.md", "title": "PostgreSQL: Documentation: 18: F.24.\u00a0passwordcheck \u2014 verify password strength"}
---

DROP INDEX — remove an index

## Synopsis

DROP INDEX \[ CONCURRENTLY \] \[ IF EXISTS \] _`name`_ \[, ...\] \[ CASCADE | RESTRICT \]

## Description

`DROP INDEX` drops an existing index from the database system. To execute this command you must be the owner of the index.

## Parameters

`CONCURRENTLY`

Drop the index without locking out concurrent selects, inserts, updates, and deletes on the index's table. A normal `DROP INDEX` acquires an `ACCESS EXCLUSIVE` lock on the table, blocking other accesses until the index drop can be completed. With this option, the command instead waits until conflicting transactions have completed.

There are several caveats to be aware of when using this option. Only one index name can be specified, and the `CASCADE` option is not supported. (Thus, an index that supports a `UNIQUE` or `PRIMARY KEY` constraint cannot be dropped this way.) Also, regular `DROP INDEX` commands can be performed within a transaction block, but `DROP INDEX CONCURRENTLY` cannot. Lastly, indexes on partitioned tables cannot be dropped using this option.

For temporary tables, `DROP INDEX` is always non-concurrent, as no other session can access them, and non-concurrent index drop is cheaper.

`IF EXISTS`

Do not throw an error if the index does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of an index to remove.

`CASCADE`

Automatically drop objects that depend on the index, and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the index if any objects depend on it. This is the default.

## Examples

This command will remove the index `title_idx`:

DROP INDEX title\_idx;

## Compatibility

`DROP INDEX` is a PostgreSQL language extension. There are no provisions for indexes in the SQL standard.

