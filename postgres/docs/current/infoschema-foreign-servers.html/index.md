---
title: "PostgreSQL: Documentation: 18: 35.29. foreign_servers"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-servers.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-servers.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:58.077Z"
content_hash: "42e18775f5aff12400ce02b0dcc08f9f5955a7b9276ad55b62cb21065e3d85a4"
menu_path: ["PostgreSQL: Documentation: 18: 35.29. foreign_servers"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-show.html/index.md", "title": "PostgreSQL: Documentation: 18: SHOW"}
nav_next: {"path": "postgres/docs/current/plpgsql-errors-and-messages.html/index.md", "title": "PostgreSQL: Documentation: 18: 41.9.\u00a0Errors and Messages"}
---

The view `foreign_servers` contains all foreign servers defined in the current database. Only those foreign servers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.27. `foreign_servers` Columns**

Column Type

Description

`foreign_server_catalog` `sql_identifier`

Name of the database that the foreign server is defined in (always the current database)

`foreign_server_name` `sql_identifier`

Name of the foreign server

`foreign_data_wrapper_catalog` `sql_identifier`

Name of the database that contains the foreign-data wrapper used by the foreign server (always the current database)

`foreign_data_wrapper_name` `sql_identifier`

Name of the foreign-data wrapper used by the foreign server

`foreign_server_type` `character_data`

Foreign server type information, if specified upon creation

`foreign_server_version` `character_data`

Foreign server version information, if specified upon creation

`authorization_identifier` `sql_identifier`

Name of the owner of the foreign server


