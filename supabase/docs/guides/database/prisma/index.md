---
title: "Prisma"
source: "https://supabase.com/docs/guides/database/prisma"
canonical_url: "https://supabase.com/docs/guides/database/prisma"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:06.388Z"
content_hash: "8862d2bdec5f0f10a2cef4a4fed733ae98111c299022aa8d7995a8094ea9c657"
menu_path: ["Database","Database","More","More","More","Prisma","Prisma","Connecting with Prisma","Connecting with Prisma"]
section_path: ["Database","Database","More","More","More","Prisma","Prisma","Connecting with Prisma","Connecting with Prisma"]
nav_prev: {"path": "../postgres/which-version-of-postgres/index.md", "title": "Print Postgres version"}
nav_next: {"path": "prisma-troubleshooting/index.md", "title": "Troubleshooting prisma errors"}
---

# 

Prisma

* * *

This quickly shows how to connect your Prisma application to Supabase Postgres. If you encounter any problems, reference the [Prisma troubleshooting docs](/docs/guides/database/prisma/prisma-troubleshooting).

If you plan to solely use Prisma instead of the Supabase Data API (PostgREST), turn it off in the [API Settings](/dashboard/project/_/settings/api).

1

### Create a custom user for Prisma

*   In the [SQL Editor](/dashboard/project/_/sql/new), create a Prisma DB user with full privileges on the public schema.
*   This gives you better control over Prisma's access and makes it easier to monitor using Supabase tools like the [Query Performance Dashboard](/dashboard/project/_/advisors/query-performance) and [Log Explorer](/dashboard/project/_/logs/explorer).

##### password manager

For security, consider using a [password generator](https://bitwarden.com/password-generator/) for the Prisma role.

```
1-- Create custom user2create user "prisma" with password 'custom_password' bypassrls createdb;34-- extend prisma's privileges to postgres (necessary to view changes in Dashboard)5grant "prisma" to "postgres";67-- Grant it necessary permissions over the relevant schemas (public)8grant usage on schema public to prisma;9grant create on schema public to prisma;10grant all on all tables in schema public to prisma;11grant all on all routines in schema public to prisma;12grant all on all sequences in schema public to prisma;13alter default privileges for role postgres in schema public grant all on tables to prisma;14alter default privileges for role postgres in schema public grant all on routines to prisma;15alter default privileges for role postgres in schema public grant all on sequences to prisma;
```

```
1-- alter prisma password if needed2alter user "prisma" with password 'new_password';
```

2

### Create a Prisma Project

Create a new Prisma Project on your computer

Create a new directory

```
1mkdir hello-prisma2cd hello-prisma
```

Initiate a new Prisma project

```
1npm init -y2npm install prisma typescript ts-node @types/node --save-dev34npx tsc --init56npx prisma init
```

3

### Add your connection information to your .env file

*   On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true)
*   Find your Supavisor Session pooler string. It should end with 5432. It will be used in your `.env` file.

If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

*   If you plan on deploying Prisma to a serverless or auto-scaling environment, you'll also need your Supavisor transaction mode string.
*   The string is identical to the session mode string but uses port 6543 at the end.

In your .env file, set the DATABASE\_URL variable to your connection string

```
1# Used for Prisma Migrations and within your application2DATABASE_URL="postgres://[DB-USER].[PROJECT-REF]:[PRISMA-PASSWORD]@[DB-REGION].pooler.supabase.com:5432/postgres"
```

Change your string's `[DB-USER]` to `prisma` and add the password you created in step 1

```
1postgres://prisma.[PROJECT-REF]...
```

4

### Create your migrations

If you have already modified your Supabase database, synchronize it with your migration file. Otherwise create new tables for your database

Create new tables in your prisma.schema file

```
1model Post {2  id        Int     @id @default(autoincrement())3  title     String4  content   String?5  published Boolean @default(false)6  author    User?   @relation(fields: [authorId], references: [id])7  authorId  Int?8}910model User {11  id    Int     @id @default(autoincrement())12  email String  @unique13  name  String?14  posts Post[]15}
```

commit your migration

```
1npx prisma migrate dev --name first_prisma_migration
```

5

### Install the prisma client

Install the Prisma client and generate its model

```
1npm install @prisma/client2npx prisma generate
```

6

### Test your API

Create a index.ts file and run it to test your connection

```
1const { PrismaClient } = require('@prisma/client');23const prisma = new PrismaClient();45async function main() {6  //change to reference a table in your schema7  const val = await prisma.<SOME_TABLE_NAME>.findMany({8    take: 10,9  });10  console.log(val);11}1213main()14  .then(async () => {15    await prisma.$disconnect();16  })17  .catch(async (e) => {18    console.error(e);19    await prisma.$disconnect();20  process.exit(1);21});
```
