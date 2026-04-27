---
title: "PostgreSQL: Documentation: 18: 52.56. pg_tablespace"
source: "https://www.postgresql.org/docs/current/catalog-pg-tablespace.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-tablespace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:52:02.335Z"
content_hash: "1d5cbfe90977701bc718fa528c1116cc530437cd8b748e2f759bebc32548c07a"
menu_path: ["PostgreSQL: Documentation: 18: 52.56. pg_tablespace"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-tablespace.html "PostgreSQL devel - 52.56. pg_tablespace")

The catalog `pg_tablespace` stores information about the available tablespaces. Tables can be placed in particular tablespaces to aid administration of disk layout.

Unlike most system catalogs, `pg_tablespace` is shared across all databases of a cluster: there is only one copy of `pg_tablespace` per cluster, not one per database.

**Table 52.56. `pg_tablespace` Columns**

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

`spcname` `name`

Tablespace name

 |
| 

`spcowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the tablespace, usually the user who created it

 |
| 

`spcacl` `aclitem[]`

Access privileges; see [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges") for details

 |
| 

`spcoptions` `text[]`

Tablespace-level options, as “keyword=value” strings

 |
