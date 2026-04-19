---
title: "PostgreSQL: Documentation: 18: 52.38. pg_policy"
source: "https://www.postgresql.org/docs/current/catalog-pg-policy.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-policy.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:24.961Z"
content_hash: "5c08a42748f21e87a72014a72c88e5ccc02b810eb4c11a944cc965be1ab802ef"
menu_path: ["PostgreSQL: Documentation: 18: 52.38. pg_policy"]
section_path: []
nav_prev: {"path": "postgres/docs/current/catalog-pg-operator.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.34.\u00a0pg_operator"}
nav_next: {"path": "postgres/docs/current/catalog-pg-proc.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.39.\u00a0pg_proc"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-policy.html "PostgreSQL devel - 52.38. pg_policy")

The catalog `pg_policy` stores row-level security policies for tables. A policy includes the kind of command that it applies to (possibly all commands), the roles that it applies to, the expression to be added as a security-barrier qualification to queries that include the table, and the expression to be added as a `WITH CHECK` option for queries that attempt to add new records to the table.

**Table 52.38. `pg_policy` Columns**

Column Type

Description

`oid` `oid`

Row identifier

`polname` `name`

The name of the policy

`polrelid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

The table to which the policy applies

`polcmd` `char`

The command type to which the policy is applied: `r` for [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT"), `a` for [INSERT](https://www.postgresql.org/docs/current/sql-insert.html "INSERT"), `w` for [UPDATE](https://www.postgresql.org/docs/current/sql-update.html "UPDATE"), `d` for [DELETE](https://www.postgresql.org/docs/current/sql-delete.html "DELETE"), or `*` for all

`polpermissive` `bool`

Is the policy permissive or restrictive?

`polroles` `oid[]` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

The roles to which the policy is applied; zero means `PUBLIC` (and normally appears alone in the array)

`polqual` `pg_node_tree`

The expression tree to be added to the security barrier qualifications for queries that use the table

`polwithcheck` `pg_node_tree`

The expression tree to be added to the WITH CHECK qualifications for queries that attempt to add rows to the table

  

### Note

Policies stored in `pg_policy` are applied only when [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relrowsecurity` is set for their table.
