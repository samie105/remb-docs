---
title: "PostgreSQL: Documentation: 18: 35.22. domain_udt_usage"
source: "https://www.postgresql.org/docs/current/infoschema-domain-udt-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-domain-udt-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:43:07.531Z"
content_hash: "c02789a57292f8dd6406aba89b4c2d2592f8f5e135c355239e8bb03121b73ca8"
menu_path: ["PostgreSQL: Documentation: 18: 35.22. domain_udt_usage"]
section_path: []
content_language: "en"
nav_prev: {"path": "../infoschema-domain-constraints.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.21.\u00a0domain_constraints"}
nav_next: {"path": "../infoschema-domains.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.23.\u00a0domains"}
---

The view `domain_udt_usage` identifies all domains that are based on data types owned by a currently enabled role. Note that in PostgreSQL, built-in data types behave like user-defined types, so they are included here as well.

**Table 35.20. `domain_udt_usage` Columns**

| 
Column Type

Description

 |
| --- |
| 

`udt_catalog` `sql_identifier`

Name of the database that the domain data type is defined in (always the current database)

 |
| 

`udt_schema` `sql_identifier`

Name of the schema that the domain data type is defined in

 |
| 

`udt_name` `sql_identifier`

Name of the domain data type

 |
| 

`domain_catalog` `sql_identifier`

Name of the database that contains the domain (always the current database)

 |
| 

`domain_schema` `sql_identifier`

Name of the schema that contains the domain

 |
| 

`domain_name` `sql_identifier`

Name of the domain

 |
