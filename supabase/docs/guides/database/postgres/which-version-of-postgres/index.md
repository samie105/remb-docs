---
title: "Print Postgres version"
source: "https://supabase.com/docs/guides/database/postgres/which-version-of-postgres"
canonical_url: "https://supabase.com/docs/guides/database/postgres/which-version-of-postgres"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:49.114Z"
content_hash: "2ec400d0a53406b00a37226232bd518945a62f99cd38ca314c2ef3c86346e57f"
menu_path: ["Database","Database","Examples","Examples","Print Postgres Version","Print Postgres Version"]
section_path: ["Database","Database","Examples","Examples","Print Postgres Version","Print Postgres Version"]
nav_prev: {"path": "../triggers/index.md", "title": "Postgres Triggers"}
nav_next: {"path": "../../prisma/index.md", "title": "Prisma"}
---

# 

Print Postgres version

* * *

It's important to know which version of Postgres you are running as each major version has different features and may cause breaking changes. You may also need to update your schema when [upgrading](https://www.postgresql.org/docs/current/pgupgrade.html) or downgrading to a major Postgres version.

Run the following query using the [SQL Editor](/dashboard/project/_/sql) in the Supabase Dashboard:

```
1select2  version();
```

Which should return something like:

```
1PostgreSQL 15.1 on aarch64-unknown-linux-gnu, compiled by gcc (Ubuntu 10.3.0-1ubuntu1~20.04) 10.3.0, 64-bit
```

This query can also be executed via `psql` or any other query editor if you prefer to [connect directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).
