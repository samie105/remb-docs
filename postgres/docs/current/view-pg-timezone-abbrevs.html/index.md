---
title: "PostgreSQL: Documentation: 18: 53.33. pg_timezone_abbrevs"
source: "https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:53.837Z"
content_hash: "bcf1f567c202016009df13de71fe067abb9c546440a2babd5d02141288231731"
menu_path: ["PostgreSQL: Documentation: 18: 53.33. pg_timezone_abbrevs"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.22.\u00a0pg_rules"}
nav_next: {"path": "postgres/docs/current/view-pg-timezone-names.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.34.\u00a0pg_timezone_names"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-timezone-abbrevs.html "PostgreSQL devel - 53.33. pg_timezone_abbrevs")

The view `pg_timezone_abbrevs` provides a list of time zone abbreviations that are currently recognized by the datetime input routines. The contents of this view change when the [TimeZone](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE) or [timezone\_abbreviations](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE-ABBREVIATIONS) run-time parameters are modified.

**Table 53.33. `pg_timezone_abbrevs` Columns**

| 
Column Type

Description

 |
| --- |
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

True if this is a daylight-savings abbreviation

 |

While most timezone abbreviations represent fixed offsets from UTC, there are some that have historically varied in value (see [Section B.4](https://www.postgresql.org/docs/current/datetime-config-files.html "B.4. Date/Time Configuration Files") for more information). In such cases this view presents their current meaning.
