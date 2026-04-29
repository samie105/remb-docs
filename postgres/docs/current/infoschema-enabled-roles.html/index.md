---
title: "PostgreSQL: Documentation: 18: 35.25. enabled_roles"
source: "https://www.postgresql.org/docs/current/infoschema-enabled-roles.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-enabled-roles.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:43:52.943Z"
content_hash: "7ce922b87545bb69e0efefc9215ea5a4a440aa17ed592cc7e5a14677bb9dfcac"
menu_path: ["PostgreSQL: Documentation: 18: 35.25. enabled_roles"]
section_path: []
content_language: "en"
nav_prev: {"path": "../infoschema-element-types.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.24.\u00a0element_types"}
nav_next: {"path": "../infoschema-foreign-data-wrapper-options.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.26.\u00a0foreign_data_wrapper_options"}
---

The view `enabled_roles` identifies the currently “enabled roles”. The enabled roles are recursively defined as the current user together with all roles that have been granted to the enabled roles with automatic inheritance. In other words, these are all roles that the current user has direct or indirect, automatically inheriting membership in.

For permission checking, the set of “applicable roles” is applied, which can be broader than the set of enabled roles. So generally, it is better to use the view `applicable_roles` instead of this one; See [Section 35.5](https://www.postgresql.org/docs/current/infoschema-applicable-roles.html "35.5. applicable_roles") for details on `applicable_roles` view.

**Table 35.23. `enabled_roles` Columns**

| 
Column Type

Description

 |
| --- |
| 

`role_name` `sql_identifier`

Name of a role

 |
