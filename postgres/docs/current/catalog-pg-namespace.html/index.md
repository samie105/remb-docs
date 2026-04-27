---
title: "PostgreSQL: Documentation: 18: 52.32. pg_namespace"
source: "https://www.postgresql.org/docs/current/catalog-pg-namespace.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-namespace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:47:23.802Z"
content_hash: "b30cadeee0e8e8967945beb66c90c5be0ae8ebad8f3a0b5eb3e636be4a7d0834"
menu_path: ["PostgreSQL: Documentation: 18: 52.32. pg_namespace"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-namespace.html "PostgreSQL devel - 52.32. pg_namespace")

The catalog `pg_namespace` stores namespaces. A namespace is the structure underlying SQL schemas: each namespace can have a separate collection of relations, types, etc. without name conflicts.

**Table 52.32. `pg_namespace` Columns**

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

`nspname` `name`

Name of the namespace

 |
| 

`nspowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the namespace

 |
| 

`nspacl` `aclitem[]`

Access privileges; see [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges") for details

 |
