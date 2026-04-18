---
title: "Connecting with pgAdmin"
source: "https://supabase.com/docs/guides/database/pgadmin"
canonical_url: "https://supabase.com/docs/guides/database/pgadmin"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:50.054Z"
content_hash: "765caa81afef669ae6a8521fb2fe011370dc2577c4adaafadbcfa6b3269758ef"
menu_path: ["Database","Database","GUI quickstarts","GUI quickstarts","pgAdmin","pgAdmin"]
section_path: ["Database","Database","GUI quickstarts","GUI quickstarts","pgAdmin","pgAdmin"]
nav_prev: {"path": "supabase/docs/guides/database/partitions/index.md", "title": "Partitioning tables"}
nav_next: {"path": "supabase/docs/guides/database/postgres-js/index.md", "title": "Postgres.js"}
---

# 

Connecting with pgAdmin

* * *

## What is pgAdmin?[#](#what-is-pgadmin)

[`pgAdmin`](https://www.pgadmin.org/) is a GUI tool for managing Postgres databases. You can use it to connect to your database via SSL.

## Connecting pgAdmin with your Postgres database[#](#connecting-pgadmin-with-your-postgres-database)

1

### Register

Register a new Postgres server.

![Register a new postgres server.](/docs/img/guides/database/connecting-to-postgres/pgadmin/register-server-pgAdmin--light.png)

2

### Name

Name your server.

![Name Postgres Server.](/docs/img/guides/database/connecting-to-postgres/pgadmin/name-pg-server.png)

3

### Connect

Add the connection info. Click the "Connect" button at the top of the page to open the connect Modal. Scroll down to "session pooler", click "view parameters" to toggle the parameters menu open and copy your connection parameters. Fill in your Database password that you made when creating your project (It can be reset in Database Settings above if you don't have it).

![Add Connection Info.](/docs/img/guides/database/connecting-to-postgres/pgadmin/add-pg-server-conn-info.png)

4

### SSL

Download your SSL certificate from Dashboard's [`Database Settings`](/dashboard/project/_/database/settings).

In pgAdmin, navigate to the Parameters tab and select connection parameter as Root Certificate. Next navigate to the Root certificate input, it will open up a file-picker modal. Select the certificate you downloaded earlier and save the server details. pgAdmin should now be able to connect to your Postgres via SSL.

![Add Connection Info.](/docs/img/guides/database/connecting-to-postgres/pgadmin/database-settings-host.png)

## Why connect to pgAdmin[#](#why-connect-to-pgadmin)

Connecting your Postgres instance to `pgAdmin` gives you a free, cross-platform GUI that makes tasks such as browsing objects, writing queries with autocomplete, running backups, and monitoring performance much faster and safer than using `psql` alone.

It acts as a single control panel where you can manage multiple servers, inspect locks and slow queries in real time, and perform maintenance operations with a click.

For scripted migrations or ultra-light remote work you’ll still lean on plain SQL or CLI tools, but most teams find `pgAdmin` invaluable for exploration and routine administration.

