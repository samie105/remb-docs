---
title: "PostgreSQL: Documentation: 18: 52.40. pg_publication"
source: "https://www.postgresql.org/docs/current/catalog-pg-publication.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-publication.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:24.188Z"
content_hash: "e1a1bb2dae0d1492106864bf80432f2c0ee73de48c2106b93ef46878615a93b5"
menu_path: ["PostgreSQL: Documentation: 18: 52.40. pg_publication"]
section_path: []
content_language: "en"
---
The catalog `pg_publication` contains all publications created in the database. For more on publications see [Section 29.1](https://www.postgresql.org/docs/current/logical-replication-publication.html "29.1. Publication").

**Table 52.40. `pg_publication` Columns**

| 
Column Type

Description

 |
| --- |
| 

`oid` `oid`

Row identifier

 |
| 

`pubname` `name`

Name of the publication

 |
| 

`pubowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the publication

 |
| 

`puballtables` `bool`

If true, this publication automatically includes all tables in the database, including any that will be created in the future.

 |
| 

`pubinsert` `bool`

If true, [INSERT](https://www.postgresql.org/docs/current/sql-insert.html "INSERT") operations are replicated for tables in the publication.

 |
| 

`pubupdate` `bool`

If true, [UPDATE](https://www.postgresql.org/docs/current/sql-update.html "UPDATE") operations are replicated for tables in the publication.

 |
| 

`pubdelete` `bool`

If true, [DELETE](https://www.postgresql.org/docs/current/sql-delete.html "DELETE") operations are replicated for tables in the publication.

 |
| 

`pubtruncate` `bool`

If true, [TRUNCATE](https://www.postgresql.org/docs/current/sql-truncate.html "TRUNCATE") operations are replicated for tables in the publication.

 |
| 

`pubviaroot` `bool`

If true, operations on a leaf partition are replicated using the identity and schema of its topmost partitioned ancestor mentioned in the publication instead of its own.

 |
| 

`pubgencols` `char`

Controls how to handle generated column replication when there is no publication column list: `n` = generated columns in the tables associated with the publication should not be replicated, `s` = stored generated columns in the tables associated with the publication should be replicated.

 |
