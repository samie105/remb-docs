---
title: "Use Supabase with RedwoodJS"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:24.302Z"
content_hash: "8e217222465c084bccab1ee667dacfb578285e23b4ca71e30082ae734d0ffb66"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","RedwoodJS","RedwoodJS"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","RedwoodJS","RedwoodJS"]
---
# 

Use Supabase with RedwoodJS

## 

Learn how to create a Supabase project, add some sample data to your database using Prisma migration and seeds, and query the data from a RedwoodJS app.

* * *

1

### Setup your new Supabase Project

[Create a new project](/dashboard) in the Supabase Dashboard.

Be sure to make note of the Database Password you used as you will need this later to connect to your database.

![New project for redwoodjs](/docs/img/guides/getting-started/quickstarts/redwoodjs/new-project.png)

2

### Gather Database Connection Strings

Open the project [**Connect** panel](/dashboard/project/_?showConnect=true). This quickstart connects using the [**Transaction pooler**](/dashboard/project/_?showConnect=true&method=transaction) and [**Session pooler**](/dashboard/project/_?showConnect=true&method=session) mode. Transaction mode is used for application queries and Session mode is used for running migrations with Prisma.

To do this, set the connection mode to `Transaction` in the [Database Settings page](/dashboard/project/_/database/settings) and copy the connection string and append `?pgbouncer=true&&connection_limit=1`. `pgbouncer=true` disables Prisma from generating prepared statements. This is required since our connection pooler does not support prepared statements in transaction mode yet. The `connection_limit=1` parameter is only required if you are using Prisma from a serverless environment. This is the Transaction mode connection string.

To get the Session mode connection pooler string, change the port of the connection string from the dashboard to 5432.

You will need the Transaction mode connection string and the Session mode connection string to setup environment variables in Step 5.

You can copy and paste these connection strings from the Supabase Dashboard when needed in later steps.

![pooled connection for redwoodjs](/docs/img/guides/getting-started/quickstarts/redwoodjs/pooled-connection-strings.png)

3

### Create a RedwoodJS app

Create a RedwoodJS app with TypeScript.

The [`yarn` package manager](https://yarnpkg.com) is required to create a RedwoodJS app. You will use it to run RedwoodJS commands later.

While TypeScript is recommended, If you want a JavaScript app, omit the `--ts` flag.

###### Terminal

```
1yarn create redwood-app my-app --ts
```

4

### Open your RedwoodJS app in VS Code

You'll develop your app, manage database migrations, and run your app in VS Code.

###### Terminal

```
1cd my-app2code .
```

5

### Configure Environment Variables

In your `.env` file, add the following environment variables for your database connection:

*   The `DATABASE_URL` should use the Transaction mode connection string you copied in Step 1.
    
*   The `DIRECT_URL` should use the Session mode connection string you copied in Step 1.
    

###### .env

```
1# Transaction mode connection string used for migrations2DATABASE_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:6543/postgres?pgbouncer=true&connection_limit=1"34# Session mode connection string — used by Prisma Client5DIRECT_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:5432/postgres"
```

6

### Update your Prisma Schema

By default, RedwoodJS ships with a SQLite database, but we want to use Postgres.

Update your Prisma schema file `api/db/schema.prisma` to use your Supabase Postgres database connection environment variables you setup in Step 5.

###### api/db/schema.prisma

```
1datasource db {2  provider  = "postgresql"3  url       = env("DATABASE_URL")4  directUrl = env("DIRECT_URL")5}
```

7

### Create the Instrument model and apply a schema migration

Create the Instrument model in `api/db/schema.prisma` and then run `yarn rw prisma migrate dev` from your terminal to apply the migration.

###### api/db/schema.prisma

```
1model Instrument {2  id   Int    @id @default(autoincrement())3  name String @unique4}
```

8

### Update seed script

Let's seed the database with a few instruments.

Update the file `scripts/seeds.ts` to contain the following code:

###### scripts/seed.ts

```
1import type { Prisma } from '@prisma/client'2import { db } from 'api/src/lib/db'34export default async () => {5  try {6    const data: Prisma.InstrumentCreateArgs['data'][] = [7      { name: 'dulcimer' },8      { name: 'harp' },9      { name: 'guitar' },10    ]1112    console.log('Seeding instruments ...')1314    const instruments = await db.instrument.createMany({ data })1516    console.log('Done.', instruments)17  } catch (error) {18    console.error(error)19  }20}
```

9

### Seed your database

Run the seed database command to populate the `Instrument` table with the instruments you just created.

The reset database command `yarn rw prisma db reset` will recreate the tables and will also run the seed script.

###### Terminal

```
1yarn rw prisma db seed
```

10

### Scaffold the Instrument UI

Now, we'll use RedwoodJS generators to scaffold a CRUD UI for the `Instrument` model.

###### Terminal

```
1yarn rw g scaffold instrument
```

11

### Start the app

Start the app via `yarn rw dev`. A browser will open to the RedwoodJS Splash page.

![RedwoodJS Splash Page](/docs/img/redwoodjs-qs-splash.png)

12

### View Books UI

Click on `/instruments` to visit [http://localhost:8910/instruments](http://localhost:8910/instruments) where should see the list of instruments.

You may now edit, delete, and add new books using the scaffolded UI.
