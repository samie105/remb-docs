---
title: "Migrate from Render to Supabase"
source: "https://supabase.com/docs/guides/platform/migrating-to-supabase/render"
canonical_url: "https://supabase.com/docs/guides/platform/migrating-to-supabase/render"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:39.030Z"
content_hash: "92d93660650fac38149e3b6a79f6e88f1f912db97946b1b0b6998c5a035c56de"
menu_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","Render","Render"]
section_path: ["Platform","Platform","More","More","More","Migrating to Supabase","Migrating to Supabase","Render","Render"]
nav_prev: {"path": "../postgres/index.md", "title": "Migrate from Postgres to Supabase"}
nav_next: {"path": "../vercel-postgres/index.md", "title": "Migrate from Vercel Postgres to Supabase"}
---

# 

Migrate from Render to Supabase

## 

Migrate your Render Postgres database to Supabase.

* * *

Render is a popular Web Hosting service in the online services category that also has a managed Postgres service. Render has a great developer experience, allowing users to deploy straight from GitHub or GitLab. This is the core of their product and they do it really well. However, when it comes to Postgres databases, it may not be the best option.

Supabase is one of the best free alternative to Render Postgres. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate from Render to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

## Retrieve your Render database credentials [#](#retrieve-render-credentials)

1.  Log in to your [Render account](https://render.com) and select the project you want to migrate.
2.  Click **Dashboard** in the menu and click in your **Postgres** database.
3.  Scroll down in the **Info** tab.
4.  Click on **PSQL Command** and edit it adding the content after `PSQL_COMMAND=`.

![Copying PSQL command from Render dashboard](/docs/img/guides/resources/migrating-to-supabase/render/render_dashboard.png) Example:

```
1%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
```

## Retrieve your Supabase connection string [#](#retrieve-supabase-connection-string)

1.  If you're new to Supabase, [create a project](/dashboard). Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).
    
2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true&method=session)
    
3.  Under Session pooler, Copy the connection string and replace the password placeholder with your database password.
    
    If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
    

## Migrate the database[#](#migrate-the-database)

The fastest way to migrate your database is with the Supabase migration tool on [Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb). Alternatively, you can use the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

1.  Set the environment variables (`PSQL_COMMAND`, `SUPABASE_HOST`, `SUPABASE_PASSWORD`) in the Colab notebook.
2.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb) in order. The first sets the variables and the second installs PSQL and the migration script.
3.  Run the third step to start the migration. This will take a few minutes.

*   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.
    
*   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
    

## Enterprise[#](#enterprise)

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
