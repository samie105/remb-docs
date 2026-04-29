---
title: "PostgreSQL: Documentation: 18: 53.4. pg_available_extension_versions"
source: "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:00.448Z"
content_hash: "3edb202d8515c8899659480c6fd7dd94936ca0b0159a79cc8cfb3cf473a5e89b"
menu_path: ["PostgreSQL: Documentation: 18: 53.4. pg_available_extension_versions"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-aios.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.2.\u00a0pg_aios"}
nav_next: {"path": "../view-pg-available-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.3.\u00a0pg_available_extensions"}
---

The `pg_available_extension_versions` view lists the specific extension versions that are available for installation. See also the [`pg_extension`](https://www.postgresql.org/docs/current/catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.4. `pg_available_extension_versions` Columns**

| 
Column Type

Description

 |
| --- |
| 

`name` `name`

Extension name

 |
| 

`version` `text`

Version name

 |
| 

`installed` `bool`

True if this version of this extension is currently installed

 |
| 

`superuser` `bool`

True if only superusers are allowed to install this extension (but see `trusted`)

 |
| 

`trusted` `bool`

True if the extension can be installed by non-superusers with appropriate privileges

 |
| 

`relocatable` `bool`

True if extension can be relocated to another schema

 |
| 

`schema` `name`

Name of the schema that the extension must be installed into, or `NULL` if partially or fully relocatable

 |
| 

`requires` `name[]`

Names of prerequisite extensions, or `NULL` if none

 |
| 

`comment` `text`

Comment string from the extension's control file

 |

The `pg_available_extension_versions` view is read-only.
