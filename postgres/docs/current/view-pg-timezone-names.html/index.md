---
title: "PostgreSQL: Documentation: 18: 53.34. pg_timezone_names"
source: "https://www.postgresql.org/docs/current/view-pg-timezone-names.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-timezone-names.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:34.476Z"
content_hash: "b7cd39f80018d8148819d8f79944936244359f2ed8876c05cf43246154dc541f"
menu_path: ["PostgreSQL: Documentation: 18: 53.34. pg_timezone_names"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-timezone-abbrevs.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.33.\u00a0pg_timezone_abbrevs"}
nav_next: {"path": "postgres/docs/current/view-pg-user-mappings.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.36.\u00a0pg_user_mappings"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-timezone-names.html "PostgreSQL devel - 53.34. pg_timezone_names")

The view `pg_timezone_names` provides a list of time zone names that are recognized by `SET TIMEZONE`, along with their associated abbreviations, UTC offsets, and daylight-savings status. (Technically, PostgreSQL does not use UTC because leap seconds are not handled.) Unlike the abbreviations shown in [`pg_timezone_abbrevs`](https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html "53.33. pg_timezone_abbrevs"), many of these names imply a set of daylight-savings transition date rules. Therefore, the associated information changes across local DST boundaries. The displayed information is computed based on the current value of `CURRENT_TIMESTAMP`.

**Table 53.34. `pg_timezone_names` Columns**

| 
Column Type

Description

 |
| --- |
| 

`name` `text`

Time zone name

 |
| 

`abbrev` `text`

Time zone abbreviation

 |
| 

`utc_offset` `interval`

Offset from UTC (positive means east of Greenwich)

 |
| 

`is_dst` `bool`

True if currently observing daylight savings

 |
