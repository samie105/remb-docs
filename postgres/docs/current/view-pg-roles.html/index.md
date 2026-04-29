---
title: "PostgreSQL: Documentation: 18: 53.21. pg_roles"
source: "https://www.postgresql.org/docs/current/view-pg-roles.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-roles.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:43:18.032Z"
content_hash: "180c9704209f61bdd33c0b1031252892b3db4c74715b21876d876c453b203372"
menu_path: ["PostgreSQL: Documentation: 18: 53.21. pg_roles"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-replication-slots.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.20.\u00a0pg_replication_slots"}
nav_next: {"path": "postgres/docs/current/view-pg-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.22.\u00a0pg_rules"}
---

The view `pg_roles` provides access to information about database roles. This is simply a publicly readable view of [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid") that blanks out the password field.

**Table 53.21. `pg_roles` Columns**

| 
Column Type

Description

 |
| --- |
| 

`rolname` `name`

Role name

 |
| 

`rolsuper` `bool`

Role has superuser privileges

 |
| 

`rolinherit` `bool`

Role automatically inherits privileges of roles it is a member of

 |
| 

`rolcreaterole` `bool`

Role can create more roles

 |
| 

`rolcreatedb` `bool`

Role can create databases

 |
| 

`rolcanlogin` `bool`

Role can log in. That is, this role can be given as the initial session authorization identifier

 |
| 

`rolreplication` `bool`

Role is a replication role. A replication role can initiate replication connections and create and drop replication slots.

 |
| 

`rolconnlimit` `int4`

For roles that can log in, this sets maximum number of concurrent connections this role can make. -1 means no limit.

 |
| 

`rolpassword` `text`

Not the password (always reads as `********`)

 |
| 

`rolvaliduntil` `timestamptz`

Password expiry time (only used for password authentication); null if no expiration

 |
| 

`rolbypassrls` `bool`

Role bypasses every row-level security policy, see [Section 5.9](https://www.postgresql.org/docs/current/ddl-rowsecurity.html "5.9. Row Security Policies") for more information.

 |
| 

`rolconfig` `text[]`

Role-specific defaults for run-time configuration variables

 |
| 

`oid` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

ID of role

 |
