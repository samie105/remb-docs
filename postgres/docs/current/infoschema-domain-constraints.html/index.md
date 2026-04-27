---
title: "PostgreSQL: Documentation: 18: 35.21. domain_constraints"
source: "https://www.postgresql.org/docs/current/infoschema-domain-constraints.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-domain-constraints.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:42:28.954Z"
content_hash: "9df57c67be565186cf4e798e42b2eb6893f7e05ee952bbc83d65c20cb7f3f032"
menu_path: ["PostgreSQL: Documentation: 18: 35.21. domain_constraints"]
section_path: []
content_language: "en"
---
The view `domain_constraints` contains all constraints belonging to domains defined in the current database. Only those domains are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.19. `domain_constraints` Columns**

| 
Column Type

Description

 |
| --- |
| 

`constraint_catalog` `sql_identifier`

Name of the database that contains the constraint (always the current database)

 |
| 

`constraint_schema` `sql_identifier`

Name of the schema that contains the constraint

 |
| 

`constraint_name` `sql_identifier`

Name of the constraint

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
| 

`is_deferrable` `yes_or_no`

`YES` if the constraint is deferrable, `NO` if not

 |
| 

`initially_deferred` `yes_or_no`

`YES` if the constraint is deferrable and initially deferred, `NO` if not

 |
