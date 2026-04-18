---
title: "PostgreSQL: Documentation: 18: 53.15. pg_policies"
source: "https://www.postgresql.org/docs/current/view-pg-policies.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-policies.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:18.923Z"
content_hash: "35e78bacd87ff6c92088a36ff3fd2d480043c3efe7095f025709a4ee0a1c8557"
menu_path: ["PostgreSQL: Documentation: 18: 53.15. pg_policies"]
section_path: []
nav_prev: {"path": "postgres/docs/current/libpq-copy.html/index.md", "title": "PostgreSQL: Documentation: 18: 32.10.\u00a0Functions Associated with the COPY Command"}
nav_next: {"path": "postgres/docs/current/pgstatstatements.html/index.md", "title": "PostgreSQL: Documentation: 18: F.32.\u00a0pg_stat_statements \u2014 track statistics of SQL planning and execution"}
---

The view `pg_policies` provides access to useful information about each row-level security policy in the database.

**Table 53.15. `pg_policies` Columns**

Column Type

Description

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table policy is on

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table policy is on

`policyname` `name` (references [`pg_policy`](https://www.postgresql.org/docs/current/catalog-pg-policy.html "52.38. pg_policy").`polname`)

Name of policy

`permissive` `text`

Is the policy permissive or restrictive?

`roles` `name[]`

The roles to which this policy applies

`cmd` `text`

The command type to which the policy is applied

`qual` `text`

The expression added to the security barrier qualifications for queries that this policy applies to

`with_check` `text`

The expression added to the WITH CHECK qualifications for queries that attempt to add rows to this table
