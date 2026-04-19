---
title: "PostgreSQL: Documentation: 18: REFRESH MATERIALIZED VIEW"
source: "https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:17.627Z"
content_hash: "ab000522707db9a5eceb33bf9c1ae1b4c07dcf34e7f4b2e6a16d1b620cb23609"
menu_path: ["PostgreSQL: Documentation: 18: REFRESH MATERIALIZED VIEW"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-reassign-owned.html/index.md", "title": "PostgreSQL: Documentation: 18: REASSIGN OWNED"}
nav_next: {"path": "postgres/docs/current/sql-reindex.html/index.md", "title": "PostgreSQL: Documentation: 18: REINDEX"}
---

REFRESH MATERIALIZED VIEW — replace the contents of a materialized view

## Synopsis

REFRESH MATERIALIZED VIEW \[ CONCURRENTLY \] _`name`_
    \[ WITH \[ NO \] DATA \]

## Description

`REFRESH MATERIALIZED VIEW` completely replaces the contents of a materialized view. To execute this command you must have the `MAINTAIN` privilege on the materialized view. The old contents are discarded. If `WITH DATA` is specified (or defaults) the backing query is executed to provide the new data, and the materialized view is left in a scannable state. If `WITH NO DATA` is specified no new data is generated and the materialized view is left in an unscannable state.

`CONCURRENTLY` and `WITH NO DATA` may not be specified together.

## Parameters

`CONCURRENTLY`

Refresh the materialized view without locking out concurrent selects on the materialized view. Without this option a refresh which affects a lot of rows will tend to use fewer resources and complete more quickly, but could block other connections which are trying to read from the materialized view. This option may be faster in cases where a small number of rows are affected.

This option is only allowed if there is at least one `UNIQUE` index on the materialized view which uses only column names and includes all rows; that is, it must not be an expression index or include a `WHERE` clause.

This option can only be used when the materialized view is already populated.

Even with this option only one `REFRESH` at a time may run against any one materialized view.

_`name`_

The name (optionally schema-qualified) of the materialized view to refresh.

## Notes

If there is an `ORDER BY` clause in the materialized view's defining query, the original contents of the materialized view will be ordered that way; but `REFRESH MATERIALIZED VIEW` does not guarantee to preserve that ordering.

While `REFRESH MATERIALIZED VIEW` is running, the [search\_path](postgres/docs/current/runtime-config-client.html/index.md#GUC-SEARCH-PATH) is temporarily changed to `pg_catalog, pg_temp`.

## Examples

This command will replace the contents of the materialized view called `order_summary` using the query from the materialized view's definition, and leave it in a scannable state:

REFRESH MATERIALIZED VIEW order\_summary;

This command will free storage associated with the materialized view `annual_statistics_basis` and leave it in an unscannable state:

REFRESH MATERIALIZED VIEW annual\_statistics\_basis WITH NO DATA;

## Compatibility

`REFRESH MATERIALIZED VIEW` is a PostgreSQL extension.
