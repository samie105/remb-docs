---
title: "Prisma Postgres & Astro"
source: "https://docs.astro.build/en/guides/backend/prisma-postgres/"
canonical_url: "https://docs.astro.build/en/guides/backend/prisma-postgres/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:39.652Z"
content_hash: "6d9cb58d0dea63cb3f341ddee9dff6071a1772c6247be6571489dee3e9d1c61e"
menu_path: ["Prisma Postgres & Astro"]
section_path: []
---
# Prisma Postgres & Astro

[Prisma Postgres](https://www.prisma.io/) is a fully managed, serverless Postgres database built for modern web apps.

## Connect with Prisma ORM (Recommended)

[Section titled “Connect with Prisma ORM (Recommended)”](#connect-with-prisma-orm-recommended)

[Prisma ORM](https://www.prisma.io/orm) is the recommended way to connect to your Prisma Postgres database. It provides type-safe queries, migrations, and global performance.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   An Astro project with an adapter installed to enable [on-demand rendering (SSR)](/en/guides/on-demand-rendering/).

### Install dependencies and initialize Prisma

[Section titled “Install dependencies and initialize Prisma”](#install-dependencies-and-initialize-prisma)

Run the following commands to install the necessary Prisma dependencies:

```
npm install prisma tsx --save-devnpm install @prisma/adapter-pg @prisma/client
```

Once installed, initialize Prisma in your project with the following command:

```
npx prisma init --db --output ./generated
```

You’ll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database, like “My Astro Project.”

This will create:

*   A `prisma/` directory with a `schema.prisma` file
*   A `.env` file with a `DATABASE_URL` already set

### Define a Model

[Section titled “Define a Model”](#define-a-model)

Even if you don’t need any specific data models yet, Prisma requires at least one model in the schema in order to generate a client and apply migrations.

The following example defines a `Post` model as a placeholder. Add the model to your schema to get started. You can safely delete or replace it later with models that reflect your actual data.

```
generator client {  provider = "prisma-client"  output   = "./generated"}
datasource db {  provider = "postgresql"  url      = env("DATABASE_URL")}
model Post {  id        Int     @id @default(autoincrement())  title     String  content   String?  published Boolean @default(false)}
```

Learn more about configuring your Prisma ORM setup in the [Prisma schema reference](https://www.prisma.io/docs/concepts/components/prisma-schema).

### Generate client

[Section titled “Generate client”](#generate-client)

Run the following command to generate the Prisma Client from your schema:

```
npx prisma generate
```

### Generate migration files

[Section titled “Generate migration files”](#generate-migration-files)

Run the following command to create the database tables and generate the Prisma Client from your schema. This will also create a `prisma/migrations/` directory with migration history files.

```
npx prisma migrate dev --name init
```

### Create a Prisma Client

[Section titled “Create a Prisma Client”](#create-a-prisma-client)

Inside of `/src/lib`, create a `prisma.ts` file. This file will initialize and export your Prisma Client instance so you can query your database throughout your Astro project.

```
import { PrismaPg } from '@prisma/adapter-pg';import { PrismaClient } from '../../prisma/generated/client';
const connectionString = import.meta.env.DATABASE_URL;const adapter = new PrismaPg({ connectionString });const prisma = new PrismaClient({ adapter });
export default prisma;
```

### Querying and displaying data

[Section titled “Querying and displaying data”](#querying-and-displaying-data)

The following example shows fetching only your published posts with the Prisma Client sorted by `id`, and then displaying titles and post content in your Astro template:

```
---import prisma from '../lib/prisma';
const posts = await prisma.post.findMany({  where: { published: true },  orderBy: { id: 'desc' }});---
<html>  <head>    <title>Published Posts</title>  </head>  <body>    <h1>Published Posts</h1>    <ul>      {posts.map((post) => (        <li>          <h2>{post.title}</h2>          {post.content && <p>{post.content}</p>}        </li>      ))}    </ul>  </body></html>
```

It is best practice to handle queries in an API route. For more information on how to use Prisma ORM in your Astro project, see the [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro).

## Connect with Other ORMs and Libraries

[Section titled “Connect with Other ORMs and Libraries”](#connect-with-other-orms-and-libraries)

You can connect to Prisma Postgres via direct TCP using any other ORM, database library, or tool of your choice. Create a direct connection string in your Prisma Console to get started.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

*   An Astro project with an adapter installed to enable [on-demand rendering (SSR)](/en/guides/on-demand-rendering/).
*   A [Prisma Postgres](https://pris.ly/ppg) database with a TCP enabled connection string

### Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

This example uses [`pg`, a PostgreSQL client for Node.js](https://github.com/brianc/node-postgres) to make a direct TCP connection.

Run the following command to install the `pg` package:

```
npm install pg
```

### Query your database client

[Section titled “Query your database client”](#query-your-database-client)

Provide your connection string to the `pg` client to communicate with your SQL server and fetch data from your database.

The following example of creating a table and inserting data can be used to validate your query URL and TCP connection:

```
---import { Client } from 'pg';const client = new Client({  connectionString: import.meta.env.DATABASE_URL,  ssl: { rejectUnauthorized: false }});await client.connect();
await client.query(`  CREATE TABLE IF NOT EXISTS posts (    id SERIAL PRIMARY KEY,    title TEXT UNIQUE,    content TEXT  );
  INSERT INTO posts (title, content)  VALUES ('Hello', 'World')  ON CONFLICT (title) DO NOTHING;`);
const { rows } = await client.query('SELECT * FROM posts');await client.end();---
<h1>Posts</h1><p>{rows[0].title}: {rows[0].content}</p>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

*   [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro)

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
