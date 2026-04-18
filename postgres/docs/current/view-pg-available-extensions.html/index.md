---
title: "PostgreSQL: Documentation: 18: 53.3. pg_available_extensions"
source: "https://www.postgresql.org/docs/current/view-pg-available-extensions.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-available-extensions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:33.799Z"
content_hash: "f1abc28bfaafb6380a4a39c3113918b9a6bbc613d508f8f5a68f27b6e623d57a"
menu_path: ["PostgreSQL: Documentation: 18: 53.3. pg_available_extensions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-pg-ctl.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_ctl"}
nav_next: {"path": "postgres/docs/current/infoschema-schemata.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.46.\u00a0schemata"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-available-extensions.html "PostgreSQL devel - 53.3. pg_available_extensions")

The `pg_available_extensions` view lists the extensions that are available for installation. See also the [`pg_extension`](https://www.postgresql.org/docs/current/catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.3. `pg_available_extensions` Columns**

Column Type

Description

`name` `name`

Extension name

`default_version` `text`

Name of default version, or `NULL` if none is specified

`installed_version` `text`

Currently installed version of the extension, or `NULL` if not installed

`comment` `text`

Comment string from the extension's control file

The `pg_available_extensions` view is read-only.
