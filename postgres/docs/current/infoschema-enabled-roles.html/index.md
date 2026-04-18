---
title: "PostgreSQL: Documentation: 18: 35.25. enabled_roles"
source: "https://www.postgresql.org/docs/current/infoschema-enabled-roles.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-enabled-roles.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:51.797Z"
content_hash: "8eb6f2dba645bd6fd0f58c5fd9210594e7bd3f3f10fd5ce18012990afc806632"
menu_path: ["PostgreSQL: Documentation: 18: 35.25. enabled_roles"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-set-transaction.html/index.md", "title": "PostgreSQL: Documentation: 18: SET TRANSACTION"}
nav_next: {"path": "postgres/docs/current/ddl-rowsecurity.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.9.\u00a0Row Security Policies"}
---

The view `enabled_roles` identifies the currently “enabled roles”. The enabled roles are recursively defined as the current user together with all roles that have been granted to the enabled roles with automatic inheritance. In other words, these are all roles that the current user has direct or indirect, automatically inheriting membership in.

For permission checking, the set of “applicable roles” is applied, which can be broader than the set of enabled roles. So generally, it is better to use the view `applicable_roles` instead of this one; See [Section 35.5](https://www.postgresql.org/docs/current/infoschema-applicable-roles.html "35.5. applicable_roles") for details on `applicable_roles` view.

**Table 35.23. `enabled_roles` Columns**

Column Type

Description

`role_name` `sql_identifier`

Name of a role


