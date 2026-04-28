---
title: "PostgreSQL: Documentation: 18: 35.34. referential_constraints"
source: "https://www.postgresql.org/docs/current/infoschema-referential-constraints.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-referential-constraints.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:47:15.064Z"
content_hash: "bb58494e43283dd1fbb05f418ce7930e1d0402704324f13274f926d7bd17a674"
menu_path: ["PostgreSQL: Documentation: 18: 35.34. referential_constraints"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-parameters.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.33.\u00a0parameters"}
nav_next: {"path": "postgres/docs/current/infoschema-role-column-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.35.\u00a0role_column_grants"}
---

The view `referential_constraints` contains all referential (foreign key) constraints in the current database. Only those constraints are shown for which the current user has write access to the referencing table (by way of being the owner or having some privilege other than `SELECT`).

**Table 35.32. `referential_constraints` Columns**

| 
Column Type

Description

 |
| --- |
| 

`constraint_catalog` `sql_identifier`

Name of the database containing the constraint (always the current database)

 |
| 

`constraint_schema` `sql_identifier`

Name of the schema containing the constraint

 |
| 

`constraint_name` `sql_identifier`

Name of the constraint

 |
| 

`unique_constraint_catalog` `sql_identifier`

Name of the database that contains the unique or primary key constraint that the foreign key constraint references (always the current database)

 |
| 

`unique_constraint_schema` `sql_identifier`

Name of the schema that contains the unique or primary key constraint that the foreign key constraint references

 |
| 

`unique_constraint_name` `sql_identifier`

Name of the unique or primary key constraint that the foreign key constraint references

 |
| 

`match_option` `character_data`

Match option of the foreign key constraint: `FULL`, `PARTIAL`, or `NONE`.

 |
| 

`update_rule` `character_data`

Update rule of the foreign key constraint: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, or `NO ACTION`.

 |
| 

`delete_rule` `character_data`

Delete rule of the foreign key constraint: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, or `NO ACTION`.

 |
