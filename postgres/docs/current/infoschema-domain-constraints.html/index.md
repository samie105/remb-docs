---
title: "PostgreSQL: Documentation: 18: 35.21. domain_constraints"
source: "https://www.postgresql.org/docs/current/infoschema-domain-constraints.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-domain-constraints.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:14.688Z"
content_hash: "c5225f8f3c30b95b3c4f81df308160e3f8b6486b08ed2a984d2167bac2be31e4"
menu_path: ["PostgreSQL: Documentation: 18: 35.21. domain_constraints"]
section_path: []
nav_prev: {"path": "postgres/docs/current/logical-replication-row-filter.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.4.\u00a0Row Filters"}
nav_next: {"path": "postgres/docs/current/sql-createdomain.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE DOMAIN"}
---

The view `domain_constraints` contains all constraints belonging to domains defined in the current database. Only those domains are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.19. `domain_constraints` Columns**

Column Type

Description

`constraint_catalog` `sql_identifier`

Name of the database that contains the constraint (always the current database)

`constraint_schema` `sql_identifier`

Name of the schema that contains the constraint

`constraint_name` `sql_identifier`

Name of the constraint

`domain_catalog` `sql_identifier`

Name of the database that contains the domain (always the current database)

`domain_schema` `sql_identifier`

Name of the schema that contains the domain

`domain_name` `sql_identifier`

Name of the domain

`is_deferrable` `yes_or_no`

`YES` if the constraint is deferrable, `NO` if not

`initially_deferred` `yes_or_no`

`YES` if the constraint is deferrable and initially deferred, `NO` if not
