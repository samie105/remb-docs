---
title: "PostgreSQL: Documentation: 18: 53.15. pg_policies"
source: "https://www.postgresql.org/docs/current/view-pg-policies.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-policies.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:46:09.532Z"
content_hash: "67219634e54c5978bee0fbd27d73720f6b8c406a252ccede55498079dc7021ff"
menu_path: ["PostgreSQL: Documentation: 18: 53.15. pg_policies"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-matviews.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.14.\u00a0pg_matviews"}
nav_next: {"path": "../view-pg-prepared-statements.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.16.\u00a0pg_prepared_statements"}
---

The view `pg_policies` provides access to useful information about each row-level security policy in the database.

**Table 53.15. `pg_policies` Columns**

| 
Column Type

Description

 |
| --- |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table policy is on

 |
| 

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table policy is on

 |
| 

`policyname` `name` (references [`pg_policy`](https://www.postgresql.org/docs/current/catalog-pg-policy.html "52.38. pg_policy").`polname`)

Name of policy

 |
| 

`permissive` `text`

Is the policy permissive or restrictive?

 |
| 

`roles` `name[]`

The roles to which this policy applies

 |
| 

`cmd` `text`

The command type to which the policy is applied

 |
| 

`qual` `text`

The expression added to the security barrier qualifications for queries that this policy applies to

 |
| 

`with_check` `text`

The expression added to the WITH CHECK qualifications for queries that attempt to add rows to this table

 |
