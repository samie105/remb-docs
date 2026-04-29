---
title: "pg_graphql: GraphQL for Postgres"
source: "https://supabase.com/docs/guides/database/extensions/pg_graphql"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_graphql"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:35.868Z"
content_hash: "864b447079f63e6f21c90e8a6c3b2ca032743285bd1af4acebd8dd390aae28fe"
menu_path: ["Database","Database","Extensions","Extensions","pg_graphql: GraphQL Support","pg_graphql: GraphQL Support"]
section_path: ["Database","Database","Extensions","Extensions","pg_graphql: GraphQL Support","pg_graphql: GraphQL Support"]
nav_prev: {"path": "../pg_cron/index.md", "title": "pg_cron: Schedule Recurring Jobs with Cron Syntax in Postgres"}
nav_next: {"path": "../pg_hashids/index.md", "title": "pg_hashids: Short UIDs"}
---

# 

pg\_graphql: GraphQL for Postgres

* * *

[pg\_graphql](https://supabase.github.io/pg_graphql/) is Postgres extension for interacting with the database using [GraphQL](https://graphql.org) instead of SQL.

The extension reflects a GraphQL schema from the existing SQL schema and exposes it through a SQL function, `graphql.resolve(...)`. This enables any programming language that can connect to Postgres to query the database via GraphQL with no additional servers, processes, or libraries.

The `pg_graphql` resolve method is designed to interop with [PostgREST](https://postgrest.org/en/stable/index.html), the tool that underpins the Supabase API, such that the `graphql.resolve` function can be called via RPC to safely and performantly expose the GraphQL API over HTTP/S.

For more information about how the SQL schema is reflected into a GraphQL schema, see the [pg\_graphql API docs](https://supabase.github.io/pg_graphql/api/).

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "pg\_graphql" and enable the extension.

## Usage[#](#usage)

Given a table

```
1create table "Blog"(2  id serial primary key,3  name text not null,4  description text5);67insert into "Blog"(name)8values ('My Blog');
```

The reflected GraphQL schema can be queried immediately as

```
1select2  graphql.resolve($$3    {4      blogCollection(first: 1) {5        edges {6          node {7            id,8            name9          }10        }11      }12    }13  $$);
```

returning the JSON

```
1{2  "data": {3    "blogCollection": {4      "edges": [5        {6          "node": {7            "id": 18            "name": "My Blog"9          }10        }11      ]12    }13  }14}
```

Note that `pg_graphql` fully supports schema introspection so you can connect any GraphQL IDE or schema inspection tool to see the full set of fields and arguments available in the API.

## API[#](#api)

*   [`graphql.resolve`](https://supabase.github.io/pg_graphql/sql_interface/): A SQL function for executing GraphQL queries.

## Resources[#](#resources)

*   Official [`pg_graphql` documentation](https://github.com/supabase/pg_graphql)
