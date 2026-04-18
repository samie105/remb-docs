---
title: "PostgreSQL: Documentation: 18: 53.33. pg_timezone_abbrevs"
source: "https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:31.510Z"
content_hash: "3b2336298899d5b2f9a5b08942af1a66390f17dac0c31bbd4857ab5b7fbad471"
menu_path: ["PostgreSQL: Documentation: 18: 53.33. pg_timezone_abbrevs"]
section_path: []
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-timezone-abbrevs.html "PostgreSQL devel - 53.33. pg_timezone_abbrevs")

The view `pg_timezone_abbrevs` provides a list of time zone abbreviations that are currently recognized by the datetime input routines. The contents of this view change when the [TimeZone](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TIMEZONE) or [timezone\_abbreviations](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TIMEZONE-ABBREVIATIONS) run-time parameters are modified.

**Table 53.33. `pg_timezone_abbrevs` Columns**

Column Type

Description

`abbrev` `text`

Time zone abbreviation

`utc_offset` `interval`

Offset from UTC (positive means east of Greenwich)

`is_dst` `bool`

True if this is a daylight-savings abbreviation

While most timezone abbreviations represent fixed offsets from UTC, there are some that have historically varied in value (see [Section B.4](https://www.postgresql.org/docs/current/datetime-config-files.html "B.4. Date/Time Configuration Files") for more information). In such cases this view presents their current meaning.
