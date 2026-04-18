---
title: "PostgreSQL: Documentation: 18: 53.9. pg_group"
source: "https://www.postgresql.org/docs/current/view-pg-group.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-group.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:31.139Z"
content_hash: "4b4a8116fe15a8ea6e45601264e673d8bb72ece9c669c0bb9342b7b8d6a9a62d"
menu_path: ["PostgreSQL: Documentation: 18: 53.9. pg_group"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-file-settings.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.8.\u00a0pg_file_settings"}
nav_next: {"path": "postgres/docs/current/view-pg-hba-file-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.10.\u00a0pg_hba_file_rules"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-group.html "PostgreSQL devel - 53.9. pg_group")

The view `pg_group` exists for backwards compatibility: it emulates a catalog that existed in PostgreSQL before version 8.1. It shows the names and members of all roles that are marked as not `rolcanlogin`, which is an approximation to the set of roles that are being used as groups.

**Table 53.9. `pg_group` Columns**

Column Type

Description

`groname` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of the group

`grosysid` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

ID of this group

`grolist` `oid[]` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

An array containing the IDs of the roles in this group
