---
title: "Connecting to Metabase"
source: "https://supabase.com/docs/guides/database/metabase"
canonical_url: "https://supabase.com/docs/guides/database/metabase"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:23.847Z"
content_hash: "35689e0c60b94bb99803f8809b5d0688b8c9961804d3bb5c09d7884851c50a3f"
menu_path: ["Database","Database","GUI quickstarts","GUI quickstarts","Metabase","Metabase"]
section_path: ["Database","Database","GUI quickstarts","GUI quickstarts","Metabase","Metabase"]
nav_prev: {"path": "supabase/docs/guides/database/json/index.md", "title": "Managing JSON and unstructured data"}
nav_next: {"path": "supabase/docs/guides/database/migrating-to-pg-partman/index.md", "title": "Migrate from TimescaleDB to pg_partman"}
---

# 

Connecting to Metabase

* * *

[`Metabase`](https://www.metabase.com/) is an Open Source data visualization tool. You can use it to explore your data stored in Supabase.

1

### Register

Create a [Metabase account](https://store.metabase.com/checkout) or deploy locally with [Docker](https://www.docker.com/products/docker-desktop/)

Deploying with Docker:

```
1docker pull metabase/metabase:latest
```

Then run:

```
1docker run -d -p 3000:3000 --name metabase metabase/metabase
```

The server should be available at [`http://localhost:3000/setup`](http://localhost:3000/setup)

2

### Connect to Postgres

Connect your Postgres server to Metabase.

*   On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true)
*   View parameters under "Session pooler"

##### connection notice

If you're in an [IPv6 environment](../../platform/ipv4-address/index.md#checking-your-network-ipv6-support) or have the [IPv4 Add-On](../../platform/ipv4-address/index.md#understanding-ip-addresses), you can use the direct connection string instead of Supavisor in Session mode.

*   Enter your database credentials into Metabase

Example credentials: ![Name Postgres Server.](/docs/img/guides/database/connecting-to-postgres/metabase/add-pg-server.png)

3

### Explore

Explore your data in Metabase

![explore data](/docs/img/guides/database/connecting-to-postgres/metabase/explore.png)
