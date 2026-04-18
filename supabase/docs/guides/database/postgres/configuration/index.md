---
title: "Database configuration"
source: "https://supabase.com/docs/guides/database/postgres/configuration"
canonical_url: "https://supabase.com/docs/guides/database/postgres/configuration"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:26.522Z"
content_hash: "74253a9bc610253d432bcd6610a40b247e5c9335ad502470776869fbdda6e8de"
menu_path: ["Database","Database","Configuration, optimization, and testing","Configuration, optimization, and testing","Database configuration","Database configuration"]
section_path: ["Database","Database","Configuration, optimization, and testing","Configuration, optimization, and testing","Database configuration","Database configuration"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/cascade-deletes/index.md", "title": "Cascade Deletes"}
nav_next: {"path": "supabase/docs/guides/database/postgres/data-deletion/index.md", "title": "Deleting data and dropping objects safely"}
---

# 

Database configuration

## 

Updating the default configuration for your Postgres database.

* * *

Postgres provides a set of sensible defaults for you database size. In some cases, these defaults can be updated. We do not recommend changing these defaults unless you know what you're doing.

## Timeouts[#](#timeouts)

See the [Timeouts](/docs/guides/database/postgres/timeouts) section.

## Statement optimization[#](#statement-optimization)

All Supabase projects come with the [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html) extension installed, which tracks planning and execution statistics for all statements executed against it. These statistics can be used in order to diagnose the performance of your project.

This data can further be used in conjunction with the [`explain`](https://www.postgresql.org/docs/current/using-explain.html) functionality of Postgres to optimize your usage.

## Managing timezones[#](#managing-timezones)

Every Supabase database is set to UTC timezone by default. We strongly recommend keeping it this way, even if your users are in a different location. This is because it makes it much easier to calculate differences between timezones if you adopt the mental model that everything in your database is in UTC time.

### Change timezone[#](#change-timezone)

```
1alter database postgres2set timezone to 'America/New_York';
```

### Full list of timezones[#](#full-list-of-timezones)

Get a full list of timezones supported by your database. This will return the following columns:

*   `name`: Time zone name
*   `abbrev`: Time zone abbreviation
*   `utc_offset`: Offset from UTC (positive means east of Greenwich)
*   `is_dst`: True if currently observing daylight savings

```
1select name, abbrev, utc_offset, is_dst2from pg_timezone_names()3order by name;
```

### Search for a specific timezone[#](#search-for-a-specific-timezone)

Use `ilike` (case insensitive search) to find specific timezones.

```
1select *2from pg_timezone_names()3where name ilike '%york%';
```

