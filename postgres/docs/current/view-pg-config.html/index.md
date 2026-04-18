---
title: "PostgreSQL: Documentation: 18: 53.6. pg_config"
source: "https://www.postgresql.org/docs/current/view-pg-config.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-config.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:30.144Z"
content_hash: "645f8eb72e049905444745b3a1c373e036688d6cf1e889ed92709ef6230c7455"
menu_path: ["PostgreSQL: Documentation: 18: 53.6. pg_config"]
section_path: []
---
The view `pg_config` describes the compile-time configuration parameters of the currently installed version of PostgreSQL. It is intended, for example, to be used by software packages that want to interface to PostgreSQL to facilitate finding the required header files and libraries. It provides the same basic information as the [pg\_config](https://www.postgresql.org/docs/current/app-pgconfig.html "pg_config") PostgreSQL client application.

By default, the `pg_config` view can be read only by superusers.

**Table 53.6. `pg_config` Columns**

Column Type

Description

`name` `text`

The parameter name

`setting` `text`

The parameter value
