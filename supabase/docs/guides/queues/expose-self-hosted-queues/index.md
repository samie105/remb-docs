---
title: "Expose Queues for local and self-hosted Supabase"
source: "https://supabase.com/docs/guides/queues/expose-self-hosted-queues"
canonical_url: "https://supabase.com/docs/guides/queues/expose-self-hosted-queues"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:30.528Z"
content_hash: "3623be661e5ae3063fea9bdb96049659fc84ee807e5051fee2f0fe4acd2fab7d"
menu_path: ["Queues","Queues","Getting Started","Getting Started","Expose Queues for local and self-hosted Supabase","Expose Queues for local and self-hosted Supabase"]
section_path: ["Queues","Queues","Getting Started","Getting Started","Expose Queues for local and self-hosted Supabase","Expose Queues for local and self-hosted Supabase"]
nav_prev: {"path": "supabase/docs/guides/queues/consuming-messages-with-edge-functions/index.md", "title": "Consuming Supabase Queue Messages with Edge Functions"}
nav_next: {"path": "supabase/docs/guides/queues/pgmq/index.md", "title": "PGMQ Extension"}
---

# 

Expose Queues for local and self-hosted Supabase

## 

Learn how to expose Queues when running Supabase with Supabase CLI or Docker Compose

* * *

By default, local and self-hosted Supabase instances expose only core schemas like public and graphql\_public. To allow client-side consumers to use your queues, you have to add `pgmq_public` schema to the list of exposed schemas.

Before continuing, complete the step [Expose queues to client-side consumers](/docs/guides/queues/quickstart#expose-queues-to-client-side-consumers) from the Queues Quickstart guide. This creates the `pgmq_public` schema, which must exist before it can be exposed through the API.

You only need to expose the `pgmq_public` schema manually when running Supabase locally with the Supabase CLI or self-hosting using Docker Compose.

## Expose Queues with Supabase CLI[#](#expose-queues-with-supabase-cli)

When running Supabase locally with Supabase CLI, update your project's `config.toml` file. Locate the `[api]` section and add `pgmq_public` to the list of schemas.

```
1[api]2enabled = true3port = 543214schemas = ["public", "graphql_public", "pgmq_public"]
```

Then restart your local Supabase stack.

```
1supabase stop && supabase start
```

## Expose queues with Docker compose[#](#expose-queues-with-docker-compose)

When running Supabase with Docker Compose, locate the `PGRST_DB_SCHEMAS` variable inside your `.env` file and add `pgmq_public` to it. This environment variable is passed to the `rest` service inside `docker-compose.yml`.

```
1PGRST_DB_SCHEMAS=public,graphql_public,pgmq_public
```

Restart your containers for the changes to take effect.

```
1docker compose down2docker compose up -d
```

## Stop exposing queues[#](#stop-exposing-queues)

If you no longer want to expose the `pgmq_public` schema, you can remove it from your configuration.

*   For Supabase CLI, remove `pgmq_public` from the `[api]` schemas list in your `config.toml` file.
*   For Docker Compose, remove `pgmq_public` from the `PGRST_DB_SCHEMAS` variable in your `.env` file.

After updating your configuration, restart your containers for the changes to take effect.

