---
title: "PostgreSQL: Documentation: 18: 52.32. pg_namespace"
source: "https://www.postgresql.org/docs/current/catalog-pg-namespace.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-namespace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:17.335Z"
content_hash: "9c8704f41ae983b35fa1b996dbbf8202678e833a179ef3715b27208db8892fdb"
menu_path: ["PostgreSQL: Documentation: 18: 52.32. pg_namespace"]
section_path: []
nav_prev: {"path": "postgres/docs/current/btree.html/index.md", "title": "PostgreSQL: Documentation: 18: 65.1.\u00a0B-Tree Indexes"}
nav_next: {"path": "postgres/docs/current/catalog-pg-operator.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.34.\u00a0pg_operator"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-namespace.html "PostgreSQL devel - 52.32. pg_namespace")

52.32. `pg_namespace`

[Prev](https://www.postgresql.org/docs/current/catalog-pg-largeobject-metadata.html "52.31. pg_largeobject_metadata") 

[Up](https://www.postgresql.org/docs/current/catalogs.html "Chapter 52. System Catalogs")

Chapter 52. System Catalogs

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/catalog-pg-opclass.html "52.33. pg_opclass")

* * *

The catalog `pg_namespace` stores namespaces. A namespace is the structure underlying SQL schemas: each namespace can have a separate collection of relations, types, etc. without name conflicts.

**Table 52.32. `pg_namespace` Columns**

Column Type

Description

`oid` `oid`

Row identifier

`nspname` `name`

Name of the namespace

`nspowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the namespace

`nspacl` `aclitem[]`

Access privileges; see [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges") for details

  

* * *

[Prev](https://www.postgresql.org/docs/current/catalog-pg-largeobject-metadata.html "52.31. pg_largeobject_metadata") 

[Up](https://www.postgresql.org/docs/current/catalogs.html "Chapter 52. System Catalogs")

 [Next](https://www.postgresql.org/docs/current/catalog-pg-opclass.html "52.33. pg_opclass")

52.31. `pg_largeobject_metadata` 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 52.33. `pg_opclass`
