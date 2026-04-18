---
title: "Turso & Astro"
source: "https://docs.astro.build/en/guides/backend/turso/"
canonical_url: "https://docs.astro.build/en/guides/backend/turso/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:47.024Z"
content_hash: "71cb11e72d0397b9c4ef8bfa0b072ca8fd949ad58f70bd483f61a84e0c883f91"
menu_path: ["Turso & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/backend/supabase/index.md", "title": "Supabase & Astro"}
nav_next: {"path": "astro/en/guides/backend/xata/index.md", "title": "Xata & Astro"}
---

# Turso & Astro

[Turso](https://turso.tech) is a distributed database built on libSQL, a fork of SQLite. It is optimized for low query latency, making it suitable for global applications.

## Initializing Turso in Astro

[Section titled “Initializing Turso in Astro”](#initializing-turso-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   The [Turso CLI](https://docs.turso.tech/cli/introduction) installed and signed in
*   A [Turso](https://turso.tech) Database with schema
*   Your Database URL
*   An Access Token

### Configure environment variables

[Section titled “Configure environment variables”](#configure-environment-variables)

Obtain your database URL using the following command:

```
turso db show <database-name> --url
```

Create an auth token for the database:

```
turso db tokens create <database-name>
```

Add the output from both commands above into your `.env` file at the root of your project. If this file does not exist, create one.

```
TURSO_DATABASE_URL=libsql://...TURSO_AUTH_TOKEN=
```

### Install LibSQL Client

[Section titled “Install LibSQL Client”](#install-libsql-client)

Install the `@libsql/client` to connect Turso to Astro:

*   [npm](#tab-panel-1459)
*   [pnpm](#tab-panel-1460)
*   [Yarn](#tab-panel-1461)

```
npm install @libsql/client
```

### Initialize a new client

[Section titled “Initialize a new client”](#initialize-a-new-client)

Create a file `turso.ts` in the `src` folder and invoke `createClient`, passing it `TURSO_DATABASE_URL` and `TURSO_AUTH_TOKEN`:

```
import { createClient } from "@libsql/client/web";
export const turso = createClient({  url: import.meta.env.TURSO_DATABASE_URL,  authToken: import.meta.env.TURSO_AUTH_TOKEN,});
```

## Querying your database

[Section titled “Querying your database”](#querying-your-database)

To access information from your database, import `turso` and [execute a SQL query](https://docs.turso.tech/sdk/ts/reference#simple-query) inside any `.astro` component.

The following example fetches all `posts` from your table, then displays a list of titles in a `<BlogIndex />` component:

```
---import { turso } from '../turso'
const { rows } = await turso.execute('SELECT * FROM posts')---
<ul>  {rows.map((post) => (    <li>{post.title}</li>  ))}</ul>
```

### SQL Placeholders

[Section titled “SQL Placeholders”](#sql-placeholders)

The `execute()` method can take [an object to pass variables to the SQL statement](https://docs.turso.tech/sdk/ts/reference#placeholders), such as `slug`, or pagination.

The following example fetches a single entry from the `posts` table `WHERE` the `slug` is the retrieved value from `Astro.params`, then displays the title of the post.

```
---import { turso } from '../turso'
const { slug } = Astro.params
const { rows } = await turso.execute({  sql: 'SELECT * FROM posts WHERE slug = ?',  args: [slug!]})---
<h1>{rows[0].title}</h1>
```

## Turso Resources

[Section titled “Turso Resources”](#turso-resources)

*   [Turso Docs](https://docs.turso.tech)
*   [Turso on GitHub](https://github.com/tursodatabase)
*   [Using Turso to serve a Server-side Rendered Astro blog’s content](https://blog.turso.tech/using-turso-to-serve-a-server-side-rendered-astro-blogs-content-58caa6188bd5)

## More backend service guides

*   ![](/logos/appwriteio.svg)
    
    ### [Appwrite](/en/guides/backend/appwrite/)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](/en/guides/backend/firebase/)
    
*   ![](/logos/neon.svg)
    
    ### [Neon](/en/guides/backend/neon/)
    
*   ![](/logos/prisma-postgres.svg)
    
    ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)
    
*   ![](/logos/scalekit.svg)
    
    ### [Scalekit](/en/guides/backend/scalekit/)
    
*   ![](/logos/sentry.svg)
    
    ### [Sentry](/en/guides/backend/sentry/)
    
*   ![](/logos/supabase.svg)
    
    ### [Supabase](/en/guides/backend/supabase/)
    
*   ![](/logos/turso.svg)
    
    ### [Turso](/en/guides/backend/turso/)
    
*   ![](/logos/xata.svg)
    
    ### [Xata](/en/guides/backend/xata/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
