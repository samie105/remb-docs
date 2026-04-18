---
title: "Connecting with PSQL"
source: "https://supabase.com/docs/guides/database/psql"
canonical_url: "https://supabase.com/docs/guides/database/psql"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:59.619Z"
content_hash: "c69545160a6b11ec0a69120b15709bbe5f2a34e8d89d23bb21e9aea89b10da38"
menu_path: ["Database","Database","GUI quickstarts","GUI quickstarts","PSQL","PSQL"]
section_path: ["Database","Database","GUI quickstarts","GUI quickstarts","PSQL","PSQL"]
nav_prev: {"path": "supabase/docs/guides/database/postgres-js/index.md", "title": "Postgres.js"}
nav_next: {"path": "supabase/docs/guides/database/prisma/index.md", "title": "Prisma"}
---

# 

Connecting with PSQL

* * *

[`psql`](https://www.postgresql.org/docs/current/app-psql.html) is a command-line tool that comes with Postgres.

## Connecting with SSL[#](#connecting-with-ssl)

You should connect to your database using SSL wherever possible, to prevent snooping and man-in-the-middle attacks.

You can obtain your connection info and Server root certificate from your application's dashboard:

![Connection Info and Certificate.](/docs/img/database/database-settings-ssl.png)

Download your [SSL certificate](#connecting-with-ssl) to `/path/to/prod-supabase.cer`.

Find your connection settings. Go to the project [**Connect** panel](/dashboard/project/_?showConnect=true&method=session) and copy the URL from the `Session pooler` section, and copy the parameters into the connection string:

```
1psql "sslmode=verify-full sslrootcert=/path/to/prod-supabase.cer host=[CLOUD_PROVIDER]-0-[REGION].pooler.supabase.com dbname=postgres user=postgres.[PROJECT_REF]"
```

