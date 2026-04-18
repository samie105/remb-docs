---
title: "PostgreSQL: Documentation: 18: 35.46. schemata"
source: "https://www.postgresql.org/docs/current/infoschema-schemata.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-schemata.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:37.156Z"
content_hash: "22ac73105fa353dec3669737e728c3f997c47e3d6a7e550684128fcc799e19fc"
menu_path: ["PostgreSQL: Documentation: 18: 35.46. schemata"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-available-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.3.\u00a0pg_available_extensions"}
nav_next: {"path": "postgres/docs/current/spi-spi-getvalue.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getvalue"}
---

The view `schemata` contains all schemas in the current database that the current user has access to (by way of being the owner or having some privilege).

**Table 35.44. `schemata` Columns**

Column Type

Description

`catalog_name` `sql_identifier`

Name of the database that the schema is contained in (always the current database)

`schema_name` `sql_identifier`

Name of the schema

`schema_owner` `sql_identifier`

Name of the owner of the schema

`default_character_set_catalog` `sql_identifier`

Applies to a feature not available in PostgreSQL

`default_character_set_schema` `sql_identifier`

Applies to a feature not available in PostgreSQL

`default_character_set_name` `sql_identifier`

Applies to a feature not available in PostgreSQL

`sql_path` `character_data`

Applies to a feature not available in PostgreSQL


