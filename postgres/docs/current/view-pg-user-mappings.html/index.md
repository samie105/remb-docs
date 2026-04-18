---
title: "PostgreSQL: Documentation: 18: 53.36. pg_user_mappings"
source: "https://www.postgresql.org/docs/current/view-pg-user-mappings.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-user-mappings.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:59.525Z"
content_hash: "c74cd8d554eaf2cb398b81268356e78a46ff9afcfda95c37483d4204728d64ab"
menu_path: ["PostgreSQL: Documentation: 18: 53.36. pg_user_mappings"]
section_path: []
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-user-mappings.html "PostgreSQL devel - 53.36. pg_user_mappings")

The view `pg_user_mappings` provides access to information about user mappings. This is essentially a publicly readable view of [`pg_user_mapping`](https://www.postgresql.org/docs/current/catalog-pg-user-mapping.html "52.65. pg_user_mapping") that leaves out the options field if the user has no rights to use it.

**Table 53.36. `pg_user_mappings` Columns**

Column Type

Description

`umid` `oid` (references [`pg_user_mapping`](https://www.postgresql.org/docs/current/catalog-pg-user-mapping.html "52.65. pg_user_mapping").`oid`)

OID of the user mapping

`srvid` `oid` (references [`pg_foreign_server`](https://www.postgresql.org/docs/current/catalog-pg-foreign-server.html "52.24. pg_foreign_server").`oid`)

The OID of the foreign server that contains this mapping

`srvname` `name` (references [`pg_foreign_server`](https://www.postgresql.org/docs/current/catalog-pg-foreign-server.html "52.24. pg_foreign_server").`srvname`)

Name of the foreign server

`umuser` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

OID of the local role being mapped, or zero if the user mapping is public

`usename` `name`

Name of the local user to be mapped

`umoptions` `text[]`

User mapping specific options, as “keyword=value” strings

To protect password information stored as a user mapping option, the `umoptions` column will read as null unless one of the following applies:

*   current user is the user being mapped, and owns the server or holds `USAGE` privilege on it
    
*   current user is the server owner and mapping is for `PUBLIC`
    
*   current user is a superuser
