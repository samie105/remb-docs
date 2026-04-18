---
title: "PostgreSQL: Documentation: 18: 35.34. referential_constraints"
source: "https://www.postgresql.org/docs/current/infoschema-referential-constraints.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-referential-constraints.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:55.028Z"
content_hash: "0ef971e223d1d5b8f0386a3fc9cfab205b3b2cb535f1bda14ea01ba3f3e016eb"
menu_path: ["PostgreSQL: Documentation: 18: 35.34. referential_constraints"]
section_path: []
nav_prev: {"path": "postgres/docs/current/catalog-pg-statistic-ext.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.52.\u00a0pg_statistic_ext"}
nav_next: {"path": "postgres/docs/current/tutorial-advanced-intro.html/index.md", "title": "PostgreSQL: Documentation: 18: 3.1.\u00a0Introduction"}
---

The view `referential_constraints` contains all referential (foreign key) constraints in the current database. Only those constraints are shown for which the current user has write access to the referencing table (by way of being the owner or having some privilege other than `SELECT`).

**Table 35.32. `referential_constraints` Columns**

Column Type

Description

`constraint_catalog` `sql_identifier`

Name of the database containing the constraint (always the current database)

`constraint_schema` `sql_identifier`

Name of the schema containing the constraint

`constraint_name` `sql_identifier`

Name of the constraint

`unique_constraint_catalog` `sql_identifier`

Name of the database that contains the unique or primary key constraint that the foreign key constraint references (always the current database)

`unique_constraint_schema` `sql_identifier`

Name of the schema that contains the unique or primary key constraint that the foreign key constraint references

`unique_constraint_name` `sql_identifier`

Name of the unique or primary key constraint that the foreign key constraint references

`match_option` `character_data`

Match option of the foreign key constraint: `FULL`, `PARTIAL`, or `NONE`.

`update_rule` `character_data`

Update rule of the foreign key constraint: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, or `NO ACTION`.

`delete_rule` `character_data`

Delete rule of the foreign key constraint: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, or `NO ACTION`.
