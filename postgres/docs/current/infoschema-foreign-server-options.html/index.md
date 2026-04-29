---
title: "PostgreSQL: Documentation: 18: 35.28. foreign_server_options"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-server-options.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-server-options.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:45.294Z"
content_hash: "cb1e9316dd387ad38be44ba998ddf0cf44e4dfc5c51fb9c1597dc10617865361"
menu_path: ["PostgreSQL: Documentation: 18: 35.28. foreign_server_options"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-foreign-data-wrappers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.27.\u00a0foreign_data_wrappers"}
nav_next: {"path": "postgres/docs/current/infoschema-foreign-servers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.29.\u00a0foreign_servers"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/infoschema-foreign-server-options.html "PostgreSQL devel - 35.28. foreign_server_options")

The view `foreign_server_options` contains all the options defined for foreign servers in the current database. Only those foreign servers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.26. `foreign_server_options` Columns**

| 
Column Type

Description

 |
| --- |
| 

`foreign_server_catalog` `sql_identifier`

Name of the database that the foreign server is defined in (always the current database)

 |
| 

`foreign_server_name` `sql_identifier`

Name of the foreign server

 |
| 

`option_name` `sql_identifier`

Name of an option

 |
| 

`option_value` `character_data`

Value of the option

 |
