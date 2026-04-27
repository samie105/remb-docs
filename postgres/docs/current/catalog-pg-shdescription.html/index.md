---
title: "PostgreSQL: Documentation: 18: 52.49. pg_shdescription"
source: "https://www.postgresql.org/docs/current/catalog-pg-shdescription.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-shdescription.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:40.586Z"
content_hash: "bf2baaccfdb6ef1bdaa4970f175a094d8282c0cbb8de951f4e676e567b03303a"
menu_path: ["PostgreSQL: Documentation: 18: 52.49. pg_shdescription"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-shdescription.html "PostgreSQL devel - 52.49. pg_shdescription")

The catalog `pg_shdescription` stores optional descriptions (comments) for shared database objects. Descriptions can be manipulated with the [`COMMENT`](https://www.postgresql.org/docs/current/sql-comment.html "COMMENT") command and viewed with psql's `\d` commands.

See also [`pg_description`](https://www.postgresql.org/docs/current/catalog-pg-description.html "52.19. pg_description"), which performs a similar function for descriptions involving objects within a single database.

Unlike most system catalogs, `pg_shdescription` is shared across all databases of a cluster: there is only one copy of `pg_shdescription` per cluster, not one per database.

**Table 52.49. `pg_shdescription` Columns**

| 
Column Type

Description

 |
| --- |
| 

`objoid` `oid` (references any OID column)

The OID of the object this description pertains to

 |
| 

`classoid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

The OID of the system catalog this object appears in

 |
| 

`description` `text`

Arbitrary text that serves as the description of this object

 |
