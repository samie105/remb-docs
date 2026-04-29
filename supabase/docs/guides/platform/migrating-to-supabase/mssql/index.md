---
title: "Migrate from MSSQL to Supabase"
source: "https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql"
canonical_url: "https://supabase.com/docs/guides/platform/migrating-to-supabase/mssql"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:33.066Z"
content_hash: "7fc74ab85fe7825a26195e5bd59508a5a64b8e14ae7319b150a5b36bb804cfae"
menu_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","MSSQL","MSSQL"]
section_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","MSSQL","MSSQL"]
nav_prev: {"path": "supabase/docs/guides/platform/migrating-to-supabase/heroku/index.md", "title": "Migrate from Heroku to Supabase"}
nav_next: {"path": "supabase/docs/guides/platform/migrating-to-supabase/mysql/index.md", "title": "Migrate from MySQL to Supabase"}
---

# 

Migrate from MSSQL to Supabase

## 

Migrate your Microsoft SQL Server database to Supabase.

* * *

This guide aims to demonstrate the process of transferring your Microsoft SQL Server database to Supabase's Postgres database. Supabase is a powerful and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MSSQL database to Supabase's Postgres enables you to leverage Postgres's capabilities and access all the features you need for your project.

## Retrieve your MSSQL database credentials[#](#retrieve-your-mssql-database-credentials)

Before you begin the migration, you need to collect essential information about your MSSQL database. Follow these steps:

1.  Log in to your MSSQL database provider.
2.  Locate and note the following database details:
    *   Hostname or IP address
    *   Database name
    *   Username
    *   Password

## Retrieve your Supabase host [#](#retrieve-supabase-host)

1.  If you're new to Supabase, [create a project](/dashboard). Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).
    
2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true&method=session)
    
3.  Under the Session pooler, click on the View parameters under the connect string. Note your Host (`$SUPABASE_HOST`).
    

![Finding Supabase host address](/docs/img/guides/resources/migrating-to-supabase/mssql/database-settings-host.png)

## Migrate the database[#](#migrate-the-database)

The fastest way to migrate your database is with the Supabase migration tool on [Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb).

Alternatively, you can use [pgloader](https://github.com/dimitri/pgloader), a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

1.  Select the Database Engine from the Source database in the dropdown.
2.  Set the environment variables (`HOST`, `USER`, `SOURCE_DB`,`PASSWORD`, `SUPABASE_URL`, and `SUPABASE_PASSWORD`) in the Colab notebook.
3.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb) in order. The first sets engine and installs the necessary files.
4.  Run the third step to start the migration. This will take a few minutes.

*   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.
    
*   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](../../compute-and-disk/index.md#disk) documentation.
    

## Enterprise[#](#enterprise)

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
