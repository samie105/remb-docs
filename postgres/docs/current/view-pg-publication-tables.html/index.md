---
title: "PostgreSQL: Documentation: 18: 53.18. pg_publication_tables"
source: "https://www.postgresql.org/docs/current/view-pg-publication-tables.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-publication-tables.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:34.949Z"
content_hash: "eec0ab34ec2d2911d337ff8af55eb33aef228f02cff78ce21eed5c728d3ffe27"
menu_path: ["PostgreSQL: Documentation: 18: 53.18. pg_publication_tables"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-prepared-xacts.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.17.\u00a0pg_prepared_xacts"}
nav_next: {"path": "postgres/docs/current/view-pg-replication-origin-status.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.19.\u00a0pg_replication_origin_status"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-publication-tables.html "PostgreSQL devel - 53.18. pg_publication_tables")

The view `pg_publication_tables` provides information about the mapping between publications and information of tables they contain. Unlike the underlying catalog [`pg_publication_rel`](https://www.postgresql.org/docs/current/catalog-pg-publication-rel.html "52.42. pg_publication_rel"), this view expands publications defined as [`FOR ALL TABLES`](../sql-createpublication.html/index.md#SQL-CREATEPUBLICATION-PARAMS-FOR-ALL-TABLES) and [`FOR TABLES IN SCHEMA`](../sql-createpublication.html/index.md#SQL-CREATEPUBLICATION-PARAMS-FOR-TABLES-IN-SCHEMA), so for such publications there will be a row for each eligible table.

**Table 53.18. `pg_publication_tables` Columns**

| 
Column Type

Description

 |
| --- |
| 

`pubname` `name` (references [`pg_publication`](https://www.postgresql.org/docs/current/catalog-pg-publication.html "52.40. pg_publication").`pubname`)

Name of publication

 |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table

 |
| 

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table

 |
| 

`attnames` `name[]` (references [`pg_attribute`](https://www.postgresql.org/docs/current/catalog-pg-attribute.html "52.7. pg_attribute").`attname`)

Names of table columns included in the publication. This contains all the columns of the table when the user didn't specify the column list for the table.

 |
| 

`rowfilter` `text`

Expression for the table's publication qualifying condition

 |
