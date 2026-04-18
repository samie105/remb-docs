---
title: "PostgreSQL: Documentation: 18: 29.8. Restrictions"
source: "https://www.postgresql.org/docs/current/logical-replication-restrictions.html"
canonical_url: "https://www.postgresql.org/docs/current/logical-replication-restrictions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:20.535Z"
content_hash: "718bc3c554e5db97edf450f980d1b924c1b5ed79e4bdcede0adf4b947604f5c5"
menu_path: ["PostgreSQL: Documentation: 18: 29.8. Restrictions"]
section_path: []
---
February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/logical-replication-restrictions.html "PostgreSQL 18 - 29.8. Restrictions") ([18](/docs/18/logical-replication-restrictions.html "PostgreSQL 18 - 29.8. Restrictions")) / [17](/docs/17/logical-replication-restrictions.html "PostgreSQL 17 - 29.8. Restrictions") / [16](/docs/16/logical-replication-restrictions.html "PostgreSQL 16 - 29.8. Restrictions") / [15](/docs/15/logical-replication-restrictions.html "PostgreSQL 15 - 29.8. Restrictions") / [14](/docs/14/logical-replication-restrictions.html "PostgreSQL 14 - 29.8. Restrictions")

Development Versions: [devel](/docs/devel/logical-replication-restrictions.html "PostgreSQL devel - 29.8. Restrictions")

Unsupported versions: [13](/docs/13/logical-replication-restrictions.html "PostgreSQL 13 - 29.8. Restrictions") / [12](/docs/12/logical-replication-restrictions.html "PostgreSQL 12 - 29.8. Restrictions") / [11](/docs/11/logical-replication-restrictions.html "PostgreSQL 11 - 29.8. Restrictions") / [10](/docs/10/logical-replication-restrictions.html "PostgreSQL 10 - 29.8. Restrictions")

## 29.8. Restrictions [#](#LOGICAL-REPLICATION-RESTRICTIONS)

Logical replication currently has the following restrictions or missing functionality. These might be addressed in future releases.

*   The database schema and DDL commands are not replicated. The initial schema can be copied by hand using `pg_dump --schema-only`. Subsequent schema changes would need to be kept in sync manually. (Note, however, that there is no need for the schemas to be absolutely the same on both sides.) Logical replication is robust when schema definitions change in a live database: When the schema is changed on the publisher and replicated data starts arriving at the subscriber but does not fit into the table schema, replication will error until the schema is updated. In many cases, intermittent errors can be avoided by applying additive schema changes to the subscriber first.
    
*   Sequence data is not replicated. The data in serial or identity columns backed by sequences will of course be replicated as part of the table, but the sequence itself would still show the start value on the subscriber. If the subscriber is used as a read-only database, then this should typically not be a problem. If, however, some kind of switchover or failover to the subscriber database is intended, then the sequences would need to be updated to the latest values, either by copying the current data from the publisher (perhaps using `pg_dump`) or by determining a sufficiently high value from the tables themselves.
    
*   Replication of `TRUNCATE` commands is supported, but some care must be taken when truncating groups of tables connected by foreign keys. When replicating a truncate action, the subscriber will truncate the same group of tables that was truncated on the publisher, either explicitly specified or implicitly collected via `CASCADE`, minus tables that are not part of the subscription. This will work correctly if all affected tables are part of the same subscription. But if some tables to be truncated on the subscriber have foreign-key links to tables that are not part of the same (or any) subscription, then the application of the truncate action on the subscriber will fail.
    
*   Large objects (see [Chapter 33](largeobjects.html "Chapter 33. Large Objects")) are not replicated. There is no workaround for that, other than storing data in normal tables.
    
*   Replication is only supported by tables, including partitioned tables. Attempts to replicate other types of relations, such as views, materialized views, or foreign tables, will result in an error.
    
*   When replicating between partitioned tables, the actual replication originates, by default, from the leaf partitions on the publisher, so partitions on the publisher must also exist on the subscriber as valid target tables. (They could either be leaf partitions themselves, or they could be further subpartitioned, or they could even be independent tables.) Publications can also specify that changes are to be replicated using the identity and schema of the partitioned root table instead of that of the individual leaf partitions in which the changes actually originate (see [`publish_via_partition_root`](sql-createpublication.html#SQL-CREATEPUBLICATION-PARAMS-WITH-PUBLISH-VIA-PARTITION-ROOT) parameter of `CREATE PUBLICATION`).
    
*   When using [`REPLICA IDENTITY FULL`](sql-altertable.html#SQL-ALTERTABLE-REPLICA-IDENTITY-FULL) on published tables, it is important to note that the `UPDATE` and `DELETE` operations cannot be applied to subscribers if the tables include attributes with datatypes (such as point or box) that do not have a default operator class for B-tree or Hash. However, this limitation can be overcome by ensuring that the table has a primary key or replica identity defined for it.
    

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/logical-replication-restrictions.html/) to report a documentation issue.
