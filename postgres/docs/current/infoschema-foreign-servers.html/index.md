---
title: "PostgreSQL: Documentation: 18: 35.29. foreign_servers"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-servers.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-servers.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:49.106Z"
content_hash: "3594b072db3737744b12f3e6a2d5e62f08263600575e7084af55267f1773e381"
menu_path: ["PostgreSQL: Documentation: 18: 35.29. foreign_servers"]
section_path: []
content_language: "en"
---
The view `foreign_servers` contains all foreign servers defined in the current database. Only those foreign servers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.27. `foreign_servers` Columns**

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

`foreign_data_wrapper_catalog` `sql_identifier`

Name of the database that contains the foreign-data wrapper used by the foreign server (always the current database)

 |
| 

`foreign_data_wrapper_name` `sql_identifier`

Name of the foreign-data wrapper used by the foreign server

 |
| 

`foreign_server_type` `character_data`

Foreign server type information, if specified upon creation

 |
| 

`foreign_server_version` `character_data`

Foreign server version information, if specified upon creation

 |
| 

`authorization_identifier` `sql_identifier`

Name of the owner of the foreign server

 |
