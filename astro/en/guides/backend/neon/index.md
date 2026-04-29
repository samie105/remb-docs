---
title: "Neon Postgres & Astro"
source: "https://docs.astro.build/en/guides/backend/neon/"
canonical_url: "https://docs.astro.build/en/guides/backend/neon/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:32.903Z"
content_hash: "3d41820780e6c8a880e7f2c64dbdf5b6db9ec1bef78d77d3011678dd93b6eb63"
menu_path: ["Neon Postgres & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/backend/firebase/index.md", "title": "Firebase & Astro"}
nav_next: {"path": "astro/en/guides/backend/prisma-postgres/index.md", "title": "Prisma Postgres & Astro"}
---

# Neon Postgres & Astro

[Neon](https://neon.tech) is a fully managed serverless Postgres database. It separates storage and compute to offer autoscaling, branching, and bottomless storage.

## Adding Neon to your Astro project

[Section titled “Adding Neon to your Astro project”](#adding-neon-to-your-astro-project)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   A [Neon](https://console.neon.tech/signup) account with a created project
*   Neon database connection string
*   An Astro project with [on-demand rendering (SSR)](../../on-demand-rendering/index.md) enabled

### Environment configuration

[Section titled “Environment configuration”](#environment-configuration)

To use Neon with Astro, you will need to set a Neon environment variable. Create or edit the `.env` file in your project root, and add the following code, replacing your own project details:

```
NEON_DATABASE_URL="postgresql://<user>:<password>@<endpoint_hostname>.neon.tech:<port>/<dbname>?sslmode=require"
```

For better TypeScript support, define environment variables in a `src/env.d.ts` file:

```
interface ImportMetaEnv {  readonly NEON_DATABASE_URL: string;}
interface ImportMeta {  readonly env: ImportMetaEnv;}
```

Learn more about [environment variables](../../environment-variables/index.md) and `.env` files in Astro.

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Install the `@neondatabase/serverless` package to connect to Neon:

```
npm install @neondatabase/serverless
```

### Creating a Neon client

[Section titled “Creating a Neon client”](#creating-a-neon-client)

Create a new file `src/lib/neon.ts` with the following code to initialize your Neon client:

```
import { neon } from '@neondatabase/serverless';
export const sql = neon(import.meta.env.NEON_DATABASE_URL);
```

## Querying your Neon database

[Section titled “Querying your Neon database”](#querying-your-neon-database)

You can now use the Neon client to query your database from any `.astro` component. The following example fetches the current time from the Postgres database:

```
---import { sql } from '../lib/neon';
const response =  await  sql`SELECT NOW() as current_time`;const currentTime = response[0].current_time;---
<h1>Current Time</h1><p>The time is: {currentTime}</p>
```

## Database branching with Neon

[Section titled “Database branching with Neon”](#database-branching-with-neon)

Neon’s branching feature lets you create copies of your database for development or testing. Use this in your Astro project by creating different environment variables for each branch:

```
NEON_DATABASE_URL=your_development_branch_url
```

```
NEON_DATABASE_URL=your_production_branch_url
```

## Resources

[Section titled “Resources”](#resources)

*   [Neon documentation](https://neon.tech/docs/introduction)
*   [Neon serverless driver GitHub](https://github.com/neondatabase/serverless)
*   [Connect an Astro site or application to Neon Postgres](https://neon.tech/docs/guides/astro)

## More backend service guides

*   ![](/logos/appwriteio.svg)
    
    ### [Appwrite](../appwrite/index.md)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](../firebase/index.md)
    
*   ![](/logos/neon.svg)
    
    ### [Neon](index.md)
    
*   ![](/logos/prisma-postgres.svg)
    
    ### [Prisma Postgres](../prisma-postgres/index.md)
    
*   ![](/logos/scalekit.svg)
    
    ### [Scalekit](../scalekit/index.md)
    
*   ![](/logos/sentry.svg)
    
    ### [Sentry](../sentry/index.md)
    
*   ![](/logos/supabase.svg)
    
    ### [Supabase](../supabase/index.md)
    
*   ![](/logos/turso.svg)
    
    ### [Turso](../turso/index.md)
    
*   ![](/logos/xata.svg)
    
    ### [Xata](../xata/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
