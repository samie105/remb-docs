---
title: "PostgreSQL: Documentation: 18: 52.42. pg_publication_rel"
source: "https://www.postgresql.org/docs/current/catalog-pg-publication-rel.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-publication-rel.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:50:41.553Z"
content_hash: "beac235f7a9305fab76b027d3688c6a3d51d25cf5f08579b057eb695d7578c89"
menu_path: ["PostgreSQL: Documentation: 18: 52.42. pg_publication_rel"]
section_path: []
content_language: "en"
nav_prev: {"path": "../catalog-pg-publication-namespace.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.41.\u00a0pg_publication_namespace"}
nav_next: {"path": "../catalog-pg-publication.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.40.\u00a0pg_publication"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-publication-rel.html "PostgreSQL devel - 52.42. pg_publication_rel")

The catalog `pg_publication_rel` contains the mapping between relations and publications in the database. This is a many-to-many mapping. See also [Section 53.18](https://www.postgresql.org/docs/current/view-pg-publication-tables.html "53.18. pg_publication_tables") for a more user-friendly view of this information.

**Table 52.42. `pg_publication_rel` Columns**

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

`prpubid` `oid` (references [`pg_publication`](https://www.postgresql.org/docs/current/catalog-pg-publication.html "52.40. pg_publication").`oid`)

Reference to publication

 |
| 

`prrelid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

Reference to relation

 |
| 

`prqual` `pg_node_tree`

Expression tree (in `nodeToString()` representation) for the relation's publication qualifying condition. Null if there is no publication qualifying condition.

 |
| 

`prattrs` `int2vector` (references [`pg_attribute`](https://www.postgresql.org/docs/current/catalog-pg-attribute.html "52.7. pg_attribute").`attnum`)

This is an array of values that indicates which table columns are part of the publication. For example, a value of `1 3` would mean that the first and the third table columns are published. A null value indicates that all columns are published.

 |
