---
title: "PostgreSQL: Documentation: 18: 35.48. sql_features"
source: "https://www.postgresql.org/docs/current/infoschema-sql-features.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-sql-features.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:28.537Z"
content_hash: "7e76268651f49b260d9d127ee226059d53f6d3b99826cbd01d595e72d7840df6"
menu_path: ["PostgreSQL: Documentation: 18: 35.48. sql_features"]
section_path: []
nav_prev: {"path": "postgres/docs/current/extend-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.17.\u00a0Packaging Related Objects into an Extension"}
nav_next: {"path": "postgres/docs/current/view-pg-timezone-abbrevs.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.33.\u00a0pg_timezone_abbrevs"}
---

The table `sql_features` contains information about which formal features defined in the SQL standard are supported by PostgreSQL. This is the same information that is presented in [Appendix D](https://www.postgresql.org/docs/current/features.html "Appendix D. SQL Conformance"). There you can also find some additional background information.

**Table 35.46. `sql_features` Columns**

Column Type

Description

`feature_id` `character_data`

Identifier string of the feature

`feature_name` `character_data`

Descriptive name of the feature

`sub_feature_id` `character_data`

Identifier string of the subfeature, or a zero-length string if not a subfeature

`sub_feature_name` `character_data`

Descriptive name of the subfeature, or a zero-length string if not a subfeature

`is_supported` `yes_or_no`

`YES` if the feature is fully supported by the current version of PostgreSQL, `NO` if not

`is_verified_by` `character_data`

Always null, since the PostgreSQL development group does not perform formal testing of feature conformance

`comments` `character_data`

Possibly a comment about the supported status of the feature


