---
title: "PostgreSQL: Documentation: 18: 35.48. sql_features"
source: "https://www.postgresql.org/docs/current/infoschema-sql-features.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-sql-features.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:51.971Z"
content_hash: "c0d4a43fc8a416f0a85ac0147cc4aa9f2c444b96a77571a492e2691f870352a2"
menu_path: ["PostgreSQL: Documentation: 18: 35.48. sql_features"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-sequences.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.47.\u00a0sequences"}
nav_next: {"path": "postgres/docs/current/infoschema-sql-implementation-info.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.49.\u00a0sql_implementation_info"}
---

The table `sql_features` contains information about which formal features defined in the SQL standard are supported by PostgreSQL. This is the same information that is presented in [Appendix D](https://www.postgresql.org/docs/current/features.html "Appendix D. SQL Conformance"). There you can also find some additional background information.

**Table 35.46. `sql_features` Columns**

| 
Column Type

Description

 |
| --- |
| 

`feature_id` `character_data`

Identifier string of the feature

 |
| 

`feature_name` `character_data`

Descriptive name of the feature

 |
| 

`sub_feature_id` `character_data`

Identifier string of the subfeature, or a zero-length string if not a subfeature

 |
| 

`sub_feature_name` `character_data`

Descriptive name of the subfeature, or a zero-length string if not a subfeature

 |
| 

`is_supported` `yes_or_no`

`YES` if the feature is fully supported by the current version of PostgreSQL, `NO` if not

 |
| 

`is_verified_by` `character_data`

Always null, since the PostgreSQL development group does not perform formal testing of feature conformance

 |
| 

`comments` `character_data`

Possibly a comment about the supported status of the feature

 |
