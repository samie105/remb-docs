---
title: "PostgreSQL: Documentation: 18: 35.22. domain_udt_usage"
source: "https://www.postgresql.org/docs/current/infoschema-domain-udt-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-domain-udt-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:19.385Z"
content_hash: "bbc0bd7088528a587d241808528ad948fcbf33b3fe2a6f3a955172f34d2011f3"
menu_path: ["PostgreSQL: Documentation: 18: 35.22. domain_udt_usage"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-execute-immediate.html/index.md", "title": "PostgreSQL: Documentation: 18: EXECUTE IMMEDIATE"}
nav_next: {"path": "postgres/docs/current/catalog-pg-policy.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.38.\u00a0pg_policy"}
---

The view `domain_udt_usage` identifies all domains that are based on data types owned by a currently enabled role. Note that in PostgreSQL, built-in data types behave like user-defined types, so they are included here as well.

**Table 35.20. `domain_udt_usage` Columns**

Column Type

Description

`udt_catalog` `sql_identifier`

Name of the database that the domain data type is defined in (always the current database)

`udt_schema` `sql_identifier`

Name of the schema that the domain data type is defined in

`udt_name` `sql_identifier`

Name of the domain data type

`domain_catalog` `sql_identifier`

Name of the database that contains the domain (always the current database)

`domain_schema` `sql_identifier`

Name of the schema that contains the domain

`domain_name` `sql_identifier`

Name of the domain

