---
title: "PostgreSQL: Documentation: 18: 52.41. pg_publication_namespace"
source: "https://www.postgresql.org/docs/current/catalog-pg-publication-namespace.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-publication-namespace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:23.740Z"
content_hash: "f4b04820a5f2d8d6d574f752aad2197403679b59c147630cdd9ab53f146be63e"
menu_path: ["PostgreSQL: Documentation: 18: 52.41. pg_publication_namespace"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-deallocate-descriptor.html/index.md", "title": "PostgreSQL: Documentation: 18: DEALLOCATE DESCRIPTOR"}
nav_next: {"path": "postgres/docs/current/view-pg-locks.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.13.\u00a0pg_locks"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-publication-namespace.html "PostgreSQL devel - 52.41. pg_publication_namespace")

52.41. `pg_publication_namespace`

[Prev](https://www.postgresql.org/docs/current/catalog-pg-publication.html "52.40. pg_publication") 

[Up](https://www.postgresql.org/docs/current/catalogs.html "Chapter 52. System Catalogs")

Chapter 52. System Catalogs

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/catalog-pg-publication-rel.html "52.42. pg_publication_rel")

* * *

The catalog `pg_publication_namespace` contains the mapping between schemas and publications in the database. This is a many-to-many mapping.

**Table 52.41. `pg_publication_namespace` Columns**

Column Type

Description

`oid` `oid`

Row identifier

`pnpubid` `oid` (references [`pg_publication`](https://www.postgresql.org/docs/current/catalog-pg-publication.html "52.40. pg_publication").`oid`)

Reference to publication

`pnnspid` `oid` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`oid`)

Reference to schema

  

* * *

[Prev](https://www.postgresql.org/docs/current/catalog-pg-publication.html "52.40. pg_publication") 

[Up](https://www.postgresql.org/docs/current/catalogs.html "Chapter 52. System Catalogs")

 [Next](https://www.postgresql.org/docs/current/catalog-pg-publication-rel.html "52.42. pg_publication_rel")

52.40. `pg_publication` 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 52.42. `pg_publication_rel`


