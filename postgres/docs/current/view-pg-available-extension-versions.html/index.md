---
title: "PostgreSQL: Documentation: 18: 53.4. pg_available_extension_versions"
source: "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:11.416Z"
content_hash: "be29c95f7529c7d3d8502394ab18ff59315c5088e1531cc10410f9b4ffe16f4e"
menu_path: ["PostgreSQL: Documentation: 18: 53.4. pg_available_extension_versions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-close.html/index.md", "title": "PostgreSQL: Documentation: 18: CLOSE"}
nav_next: {"path": "postgres/docs/current/color-when.html/index.md", "title": "PostgreSQL: Documentation: 18: N.1.\u00a0When Color is Used"}
---

The `pg_available_extension_versions` view lists the specific extension versions that are available for installation. See also the [`pg_extension`](https://www.postgresql.org/docs/current/catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.4. `pg_available_extension_versions` Columns**

Column Type

Description

`name` `name`

Extension name

`version` `text`

Version name

`installed` `bool`

True if this version of this extension is currently installed

`superuser` `bool`

True if only superusers are allowed to install this extension (but see `trusted`)

`trusted` `bool`

True if the extension can be installed by non-superusers with appropriate privileges

`relocatable` `bool`

True if extension can be relocated to another schema

`schema` `name`

Name of the schema that the extension must be installed into, or `NULL` if partially or fully relocatable

`requires` `name[]`

Names of prerequisite extensions, or `NULL` if none

`comment` `text`

Comment string from the extension's control file

The `pg_available_extension_versions` view is read-only.


