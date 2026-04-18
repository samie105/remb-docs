---
title: "Seeding"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:17.760Z"
content_hash: "0fb9cf8c850d7366d3fb4de2656116ada8aa549b8b738157ae1efdb0a64db8ea"
menu_path: ["Seeding"]
section_path: []
---
Workflows

Learn how to seed your database using Prisma ORM's integrated seeding functionality and Prisma Client

Seeding allows you to consistently re-create the same data in your database and can be used to:

*   Populate your database with data that is required for your application to start, such as a default language or currency.
*   Provide basic data for validating and using your application in a development environment. This is particularly useful if you are using Prisma Migrate, which sometimes requires resetting your development database.

Prisma ORM's integrated seeding functionality expects a command in the `"seed"` key in the `migrations` object of your `prisma.config.ts`. This can be any command, `prisma db seed` will just execute it. In this guide and as a default, we recommend writing a seed script inside your project's `prisma/` folder and starting it with the command.

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";
export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx prisma/seed.ts",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Database seeding happens when you run `prisma db seed`. With `prisma db seed`, _you_ decide when to invoke the seed command. It can be useful for a test setup or to prepare a new development environment, for example.

Here we suggest some specific seed scripts for different situations. You are free to customize these in any way, but can also use them as presented here:

### [Seeding your database](#seeding-your-database)

*   Create a new file named `seed.ts`. This can be placed anywhere within your project's folder structure. The example below places it in the `/prisma` folder.
    
*   In the `seed.ts` file, import Prisma Client, initialize it and create some records. As an example, take the following Prisma schema with a `User` and `Post` model:
    

```
model User {
 id    Int    @id @default(autoincrement())
 email String @unique
 name  String
 posts Post[]
}

model Post {
 id        Int     @id @default(autoincrement())
 title     String
 content   String
 published Boolean
 user      User    @relation(fields: [userId], references: [id])
 userId    Int
}
```

Create some new users and posts in your `prisma/seed.ts` file:

```
import "dotenv/config";
import { Pool } from "pg";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../prisma/generated/client";

const connectionString = `${process.env.DATABASE_URL}`;
const pool = new Pool({ connectionString });
const adapter = new PrismaPg(pool);
const prisma = new PrismaClient({ adapter });
async function main() {
  const alice = await prisma.user.upsert({
    where: { email: "alice@prisma.io" },
    update: {},
    create: {
      email: "alice@prisma.io",
      name: "Alice",
      posts: {
        create: {
          title: "Check out Prisma with Next.js",
          content: "https://www.prisma.io/nextjs",
          published: true,
        },
      },
    },
  });
  const bob = await prisma.user.upsert({
    where: { email: "bob@prisma.io" },
    update: {},
    create: {
      email: "bob@prisma.io",
      name: "Bob",
      posts: {
        create: [
          {
            title: "Follow Prisma on Twitter",
            content: "https://twitter.com/prisma",
            published: true,
          },
          {
            title: "Follow Nexus on Twitter",
            content: "https://twitter.com/nexusgql",
            published: true,
          },
        ],
      },
    },
  });
  console.log({ alice, bob });
}
main()
  .then(async () => {
    await prisma.$disconnect();
    await pool.end();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    await pool.end();
    process.exit(1);
  });
```

*   Add `typescript`, `tsx`, `@types/node`, `@prisma/adapter-pg`, `pg`, `@types/pg` and `dotenv` development dependencies:

*   Add the `seed` field to your `prisma.config.ts` file:

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";
export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx prisma/seed.ts", 
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

*   To seed the database, run the `db seed` CLI command:

We're using TypeScript here, but it's possible to do the same thing in vanilla JavaScript. The same steps would be followed, expect with a `prisma/seed.js` file (without types), and calling `node prisma/seed.js` instead of `tsx`.

### [Seeding your database via raw SQL queries](#seeding-your-database-via-raw-sql-queries)

You can also make use of raw SQL queries in order to seed the database with data.

While you can use a plain-text `.sql` file (such as a data dump) for that, it is often easier to place those raw queries, if they're of short size, into the `seed.js` file because it saves you the hassle of working out database connection strings and creating a dependency on a binary like `psql`.

To seed additional data to the `schema.prisma` above, add the following to the `seed.js` (or `seed.ts`) file:

```
async function rawSql() {
  const result =
    await prisma.$executeRaw`INSERT INTO "User" ("id", "email", "name") VALUES (3, 'foo@example.com', 'Foo') ON CONFLICT DO NOTHING;`;
  console.log({ result });
}
```

and chain this function to the promise calls, such as the following change towards the end of the file:

```
main()
  .then(rawSql)
  .then(async () => {
    await prisma.$disconnect();
    await pool.end();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    await pool.end();
    process.exit(1);
  });
```

### [Seeding your database via any language (with a Bash script)](#seeding-your-database-via-any-language-with-a-bash-script)

In addition to TypeScript and JavaScript, you can also use a Bash script (`seed.sh`) to seed your database in another language such as Go, or plain SQL.

The following example runs a Go script in the same folder as `seed.sh`:

```
#!/bin/sh
# -e Exit immediately when a command returns a non-zero status.
# -x Print commands before they are executed
set -ex
# Seeding command go
run ./seed/
```

The following example uses [psql](https://www.postgresql.org/docs/13/app-psql.html) to run a SQL script in the same folder as `seed.sh`:

```
#!/bin/sh
# -e Exit immediately when a command returns a non-zero status.
# -x Print commands before they are executed
set -ex
# Seeding command
psql file.sql
```

### [User-defined arguments](#user-defined-arguments)

`prisma db seed` allows you to define custom arguments in your seed file that you can pass to the `prisma db seed` command. For example, you could define your own arguments to seed different data for different environments or partially seeding data in some tables.

Here is an example seed file that defines a custom argument to seed different data in different environments:

```
import { parseArgs } from "node:util";

const options = {
  environment: { type: "string" },
};

async function main() {
  const {
    values: { environment },
  } = parseArgs({ options });

  switch (environment) {
    case "development":
      /** data for your development */
      break;
    case "test":
      /** data for your test environment */
      break;
    default:
      break;
  }
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
```

You can then provide the `environment` argument when using `prisma db seed` by adding a [delimiter](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02) — `--` —, followed by your custom arguments:

Here's a non-exhaustive list of other tools you can integrate with Prisma ORM in your development workflow to seed your database:

*   [Supabase community project](https://github.com/supabase-community/seed)
*   [Replibyte](https://www.replibyte.com/docs/introduction/)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-migrate/workflows/seeding.mdx)
