---
title: "Database"
source: "https://supabase.com/docs/guides/database/overview"
canonical_url: "https://supabase.com/docs/guides/database/overview"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:43.311Z"
content_hash: "3cb395b2eff7d61cc996e2dbdcb027a5b1d9409b33ff9a3893be0bd86b98d289"
menu_path: ["Database","Database","Overview","Overview"]
section_path: ["Database","Database","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/database/orioledb/index.md", "title": "OrioleDB Overview"}
nav_next: {"path": "supabase/docs/guides/database/partitions/index.md", "title": "Partitioning tables"}
---

# 

Database

* * *

Every Supabase project comes with a full [Postgres](https://www.postgresql.org/) database, a free and open source database which is considered one of the world's most stable and advanced databases.

## Features[#](#features)

### Table view[#](#table-view)

You don't have to be a database expert to start using Supabase. Our table view makes Postgres as easy to use as a spreadsheet.

![Table View.](/docs/img/table-view.png)

### Relationships[#](#relationships)

Dig into the relationships within your data.

### Clone tables[#](#clone-tables)

You can duplicate your tables, just like you would inside a spreadsheet.

### The SQL editor[#](#the-sql-editor)

Supabase comes with a SQL Editor. You can also save your favorite queries to run later!

### Additional features[#](#additional-features)

*   Supabase extends Postgres with realtime functionality using our [Realtime Server](https://github.com/supabase/realtime).
*   Every project is a full Postgres database, with `postgres` level access.
*   Supabase manages your database backups.
*   Import data directly from a CSV or excel spreadsheet.

Database backups **do not** include objects stored via the Storage API, as the database only includes metadata about these objects. Restoring an old backup does not restore objects that have been deleted since then.

### Extensions[#](#extensions)

To expand the functionality of your Postgres database, you can use extensions. You can enable Postgres extensions with the click of a button within the Supabase dashboard.

[Learn more](../extensions/index.md) about all the extensions provided on Supabase.

## Terminology[#](#terminology)

### Postgres or PostgreSQL?[#](#postgres-or-postgresql)

PostgreSQL the database was derived from the POSTGRES Project, a package written at the University of California at Berkeley in 1986. This package included a query language called "PostQUEL".

In 1994, Postgres95 was built on top of POSTGRES code, adding an SQL language interpreter as a replacement for PostQUEL.

Eventually, Postgres95 was renamed to PostgreSQL to reflect the SQL query capability. After this, many people referred to it as Postgres since it's less prone to confusion. Supabase is all about simplicity, so we also refer to it as Postgres.

## Tips[#](#tips)

Read about resetting your database password [here](/docs/guides/database/managing-passwords) and changing the timezone of your server [here](/docs/guides/database/managing-timezones).

## Next steps[#](#next-steps)

*   Read more about [Postgres](https://www.postgresql.org/about/)
*   Sign in: [supabase.com/dashboard](/dashboard)
