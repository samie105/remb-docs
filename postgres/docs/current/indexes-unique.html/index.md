---
title: "PostgreSQL: Documentation: 18: 11.6. Unique Indexes"
source: "https://www.postgresql.org/docs/current/indexes-unique.html"
canonical_url: "https://www.postgresql.org/docs/current/indexes-unique.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:58.090Z"
content_hash: "b70bcc533bb90d77db15027c3ffa8e165a783bbd01d7fb08ffd8dab782b29e38"
menu_path: ["PostgreSQL: Documentation: 18: 11.6. Unique Indexes"]
section_path: []
---
Indexes can also be used to enforce uniqueness of a column's value, or the uniqueness of the combined values of more than one column.

CREATE UNIQUE INDEX _`name`_ ON _`table`_ (_`column`_ \[, ...\]) \[ NULLS \[ NOT \] DISTINCT \];

Currently, only B-tree indexes can be declared unique.

When an index is declared unique, multiple table rows with equal indexed values are not allowed. By default, null values in a unique column are not considered equal, allowing multiple nulls in the column. The `NULLS NOT DISTINCT` option modifies this and causes the index to treat nulls as equal. A multicolumn unique index will only reject cases where all indexed columns are equal in multiple rows.

PostgreSQL automatically creates a unique index when a unique constraint or primary key is defined for a table. The index covers the columns that make up the primary key or unique constraint (a multicolumn index, if appropriate), and is the mechanism that enforces the constraint.

### Note

There's no need to manually create indexes on unique columns; doing so would just duplicate the automatically-created index.
