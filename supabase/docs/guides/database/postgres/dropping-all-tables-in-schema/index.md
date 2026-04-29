---
title: "Drop all tables in a Postgres schema"
source: "https://supabase.com/docs/guides/database/postgres/dropping-all-tables-in-schema"
canonical_url: "https://supabase.com/docs/guides/database/postgres/dropping-all-tables-in-schema"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:30.210Z"
content_hash: "8ceb15a8eee1a650e40b009cad0e1dadd655a1a60d13bfcbef4d93616723f52e"
menu_path: ["Database","Database","Examples","Examples","Drop All Tables in Schema","Drop All Tables in Schema"]
section_path: ["Database","Database","Examples","Examples","Drop All Tables in Schema","Drop All Tables in Schema"]
nav_prev: {"path": "../data-deletion/index.md", "title": "Deleting data and dropping objects safely"}
nav_next: {"path": "../enums/index.md", "title": "Managing Enums in Postgres"}
---

# 

Drop all tables in a Postgres schema

* * *

Execute the following query to drop all tables in a given schema. Replace `my-schema-name` with the name of your schema. In Supabase, the default schema is `public`.

This deletes all tables and their associated data. Ensure you have a recent [backup](/docs/guides/platform/backups) before proceeding.

```
1do $$ declare2    r record;3begin4    for r in (select tablename from pg_tables where schemaname = 'my-schema-name') loop5        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';6    end loop;7end $$;
```

This query works by listing out all the tables in the given schema and then executing a `drop table` for each (hence the `for... loop`).

You can run this query using the [SQL Editor](/dashboard/project/_/sql) in the Supabase Dashboard, or via `psql` if you're [connecting directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).
