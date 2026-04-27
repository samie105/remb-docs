---
title: "Deploy to Cloudflare Workers & Pages"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:43:33.073Z"
content_hash: "1c1c39054276c93f97132f4b4dcbb6829b833318fb48563585fd95dce518d00e"
menu_path: ["Deploy to Cloudflare Workers & Pages"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
---
Learn the things you need to know in order to deploy an app that uses Prisma Client for talking to a database to a Cloudflare Worker or to Cloudflare Pages

**Questions answered in this page**

-   How to deploy Prisma to Cloudflare Workers?
-   Which drivers work on Workers/Pages?
-   How to configure DATABASE\_URL and envs?

This section covers _general_ things you need to be aware of when deploying to Cloudflare Workers or Pages and are using Prisma ORM, regardless of the database provider you use.

### [Using Prisma Postgres](#using-prisma-postgres)

You can use Prisma Postgres and deploy to Cloudflare Workers.

After you create a Worker, run:

Enter a name for your project and choose a database region.

This command:

-   Connects your CLI to your [Prisma Data Platform](https://console.prisma.io/?utm_source=docs&utm_medium=content&utm_content=orm) account. If you're not logged in or don't have an account, your browser will open to guide you through creating a new account or signing into your existing one.
-   Creates a `prisma` directory containing a `schema.prisma` file for your database models.
-   Creates a `.env` file with your `DATABASE_URL`.

### [Using an edge-compatible driver](#using-an-edge-compatible-driver)

When deploying a Cloudflare Worker that uses Prisma ORM, you need to use an [edge-compatible driver](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/overview#edge-compatibility-of-database-drivers) and its respective [driver adapter](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers#driver-adapters) for Prisma ORM.

The edge-compatible drivers for Cloudflare Workers and Pages are:

-   [Neon Serverless](https://neon.tech/docs/serverless/serverless-driver) uses HTTP to access the database
-   [PlanetScale Serverless](https://planetscale.com/docs/tutorials/planetscale-serverless-driver) uses HTTP to access the database
-   [`node-postgres`](https://node-postgres.com/) (`pg`) uses Cloudflare's `connect()` (TCP) to access the database
-   [`@libsql/client`](https://github.com/tursodatabase/libsql-client-ts) is used to access Turso databases via HTTP
-   [Cloudflare D1](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare) is used to access D1 databases

There's [also work being done](https://github.com/sidorares/node-mysql2/pull/2289) on the `node-mysql2` driver which will enable access to traditional MySQL databases from Cloudflare Workers and Pages in the future as well.

If your application uses PostgreSQL, we recommend using [Prisma Postgres](https://www.prisma.io/docs/postgres). It is fully supported on edge runtimes and does not require a specialized edge-compatible driver. Review the [Prisma Postgres serverless driver limitations](https://www.prisma.io/docs/postgres/database/serverless-driver#limitations) to understand current constraints.

### [Setting your database connection URL as an environment variable](#setting-your-database-connection-url-as-an-environment-variable)

First, ensure that your `datasource` block in your Prisma schema is configured correctly. Database connection URLs are configured in `prisma.config.ts`:

```
datasource db {
  provider = "postgresql" // this might also be `mysql` or another value depending on your database
}
```

prisma.config.ts

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

#### [Development](#development)

When using your Worker in **development**, you can configure your database connection via the [`.dev.vars` file](https://developers.cloudflare.com/workers/configuration/secrets/#local-development-with-secrets) locally.

Assuming you use the `DATABASE_URL` environment variable from above, you can set it inside `.dev.vars` as follows:

.dev.vars

```
DATABASE_URL="your-database-connection-string"
```

In the above snippet, `your-database-connection-string` is a placeholder that you need to replace with the value of your own connection string, for example:

.dev.vars

```
DATABASE_URL="postgresql://admin:mypassword42@somehost.aws.com:5432/mydb"
```

Note that the `.dev.vars` file is not compatible with `.env` files which are typically used by Prisma ORM.

This means that you need to make sure that Prisma ORM gets access to the environment variable when needed, e.g. when running a Prisma CLI command like `prisma migrate dev`.

There are several options for achieving this:

-   Run your Prisma CLI commands using [`dotenv`](https://www.npmjs.com/package/dotenv-cli) to specify from where the CLI should read the environment variable, for example:
    
    ```
    dotenv -e .dev.vars -- npx prisma migrate dev
    ```
    
-   Create a script in `package.json` that reads `.dev.vars` via [`dotenv`](https://www.npmjs.com/package/dotenv-cli). You can then execute `prisma` commands as follows: `npm run env -- npx prisma migrate dev`. Here's a reference for the script:
    
    package.json
    
    ```
    "scripts":  { "env": "dotenv -e .dev.vars" }
    ```
    
-   Duplicate the `DATABASE_URL` and any other relevant env vars into a new file called `.env` which can then be used by Prisma ORM.

#### [Production](#production)

When deploying your Worker to **production**, you'll need to set the database connection using the `wrangler` CLI:

The command is interactive and will ask you to enter the value for the `DATABASE_URL` env var as the next step in the terminal.

### [Size limits on free accounts](#size-limits-on-free-accounts)

Cloudflare has a [size limit of 3 MB for Workers on the free plan](https://developers.cloudflare.com/workers/platform/limits/). If your application bundle with Prisma ORM exceeds that size, we recommend upgrading to a paid Worker plan.

### [Deploying a Next.js app to Cloudflare Pages with `@cloudflare/next-on-pages`](#deploying-a-nextjs-app-to-cloudflare-pages-with-cloudflarenext-on-pages)

Cloudflare offers an option to run Next.js apps on Cloudflare Pages with [`@cloudflare/next-on-pages`](https://github.com/cloudflare/next-on-pages), see the [docs](https://developers.cloudflare.com/pages/framework-guides/nextjs/ssr/get-started/) for instructions.

Based on some testing, we found the following:

-   You can deploy using the PlanetScale or Neon Serverless Driver.
-   Traditional PostgreSQL deployments using `pg` don't work because `pg` itself currently does not work with `@cloudflare/next-on-pages` (see [here](https://github.com/cloudflare/next-on-pages/issues/605)).

Feel free to reach out to us on [Discord](https://pris.ly/discord?utm_source=docs&utm_medium=inline_text) if you find that anything has changed about this.

This section provides database-specific instructions for deploying a Cloudflare Worker with Prisma ORM.

### [Prerequisites](#prerequisites)

As a prerequisite for the following section, you need to have a Cloudflare Worker running locally and the Prisma CLI installed.

If you don't have that yet, you can run these commands:

You'll further need a database instance of your database provider of choice available. Refer to the respective documentation of the provider for setting up that instance.

We'll use the default `User` model for the example below:

```
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
```

### [PostgreSQL (traditional)](#postgresql-traditional)

If you are using a traditional PostgreSQL database that's accessed via TCP and the `pg` driver, you need to:

-   use the `@prisma/adapter-pg` database adapter (learn more [here](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#using-driver-adapters))
-   set `node_compat = true` in `wrangler.toml` (see the [Cloudflare docs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/))

#### [1\. Configure Prisma schema & database connection](#1-configure-prisma-schema--database-connection)

First, ensure that the database connection is configured properly. Database connection URLs are configured in `prisma.config.ts`:

schema.prisma

```
generator client {
  provider = "prisma-client"
  output   = "./generated"
}

datasource db {
  provider = "postgresql"
}
```

prisma.config.ts

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Next, you need to set the `DATABASE_URL` environment variable to the value of your database connection string. You'll do this in a file called `.dev.vars` used by Cloudflare:

.dev.vars

```
DATABASE_URL="postgresql://admin:mypassword42@somehost.aws.com:5432/mydb"
```

Because the Prisma CLI by default is only compatible with `.env` files, you can adjust your `package.json` with the following script that loads the env vars from `.dev.vars`. You can then use this script to load the env vars before executing a `prisma` command.

Add this script to your `package.json`:

package.json

```
{
  // ...
  "scripts": {
    // ....
    "env": "dotenv -e .dev.vars"
  },
  // ...
}
```

Now you can execute Prisma CLI commands as follows while ensuring that the command has access to the env vars in `.dev.vars`:

#### [2\. Install dependencies](#2-install-dependencies)

Next, install the required packages:

#### [3\. Set `node_compat = true` in `wrangler.toml`](#3-set-node_compat--true-in-wranglertoml)

In your `wrangler.toml` file, add the following line:

wrangler.toml

```
node_compat = true
```

#### [4\. Migrate your database schema (if applicable)](#4-migrate-your-database-schema-if-applicable)

If you ran `npx prisma init` above, you need to migrate your database schema to create the `User` table that's defined in your Prisma schema (if you already have all the tables you need in your database, you can skip this step):

#### [5\. Use Prisma Client in your Worker to send a query to the database](#5-use-prisma-client-in-your-worker-to-send-a-query-to-the-database)

Here is a sample code snippet that you can use to instantiate `PrismaClient` and send a query to your database:

```
import { PrismaClient } from "./generated/client";
import { PrismaPg } from "@prisma/adapter-pg";

export default {
  async fetch(request, env, ctx) {
    const adapter = new PrismaPg({ connectionString: env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });

    const users = await prisma.user.findMany();
    const result = JSON.stringify(users);
    ctx.waitUntil(prisma.$disconnect());
    return new Response(result);
  },
};
```

#### [6\. Run the Worker locally](#6-run-the-worker-locally)

To run the Worker locally, you can run the `wrangler dev` command:

#### [7\. Set the `DATABASE_URL` environment variable and deploy the Worker](#7-set-the-database_url-environment-variable-and-deploy-the-worker)

To deploy the Worker, you first need to the `DATABASE_URL` environment variable [via the `wrangler` CLI](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers):

The command is interactive and will ask you to enter the value for the `DATABASE_URL` env var as the next step in the terminal.

Then you can go ahead then deploy the Worker:

The command will output the URL where you can access the deployed Worker.

### [PlanetScale](#planetscale)

If you are using a PlanetScale database, you need to:

-   use the `@prisma/adapter-planetscale` database adapter (learn more [here](https://www.prisma.io/docs/orm/core-concepts/supported-databases/mysql#planetscale))
    
-   manually remove the conflicting `cache` field:
    
    ```
    export default {
      async fetch(request, env, ctx) {
        const adapter = new PrismaPlanetScale({
          url: env.DATABASE_URL,
          // see https://github.com/cloudflare/workerd/issues/698
          fetch(url, init) {
            delete init["cache"];
            return fetch(url, init);
          },
        });
        const prisma = new PrismaClient({ adapter });
    
        // ...
      },
    };
    ```
    

#### [1\. Configure Prisma schema & database connection](#1-configure-prisma-schema--database-connection-1)

First, ensure that the database connection is configured properly. Database connection URLs are configured in `prisma.config.ts`:

schema.prisma

```
generator client {
  provider = "prisma-client"
  output   = "./generated"
}

datasource db {
  provider     = "mysql"
  relationMode = "prisma" // required for PlanetScale (as by default foreign keys are disabled)
}
```

prisma.config.ts

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Next, you need to set the `DATABASE_URL` environment variable to the value of your database connection string. You'll do this in a file called `.dev.vars` used by Cloudflare:

.dev.vars

```
DATABASE_URL="mysql://32qxa2r7hfl3102wrccj:password@us-east.connect.psdb.cloud/demo-cf-worker-ps?sslaccept=strict"
```

Because the Prisma CLI by default is only compatible with `.env` files, you can adjust your `package.json` with the following script that loads the env vars from `.dev.vars`. You can then use this script to load the env vars before executing a `prisma` command.

Add this script to your `package.json`:

package.json

```
{
  // ...
  "scripts": {
    // ....
    "env": "dotenv -e .dev.vars"
  },
  // ...
}
```

Now you can execute Prisma CLI commands as follows while ensuring that the command has access to the env vars in `.dev.vars`:

#### [2\. Install dependencies](#2-install-dependencies-1)

Next, install the required packages:

#### [3\. Migrate your database schema (if applicable)](#3-migrate-your-database-schema-if-applicable)

If you ran `npx prisma init` above, you need to migrate your database schema to create the `User` table that's defined in your Prisma schema (if you already have all the tables you need in your database, you can skip this step):

#### [4\. Use Prisma Client in your Worker to send a query to the database](#4-use-prisma-client-in-your-worker-to-send-a-query-to-the-database)

Here is a sample code snippet that you can use to instantiate `PrismaClient` and send a query to your database:

```
import { PrismaClient } from "./generated/client";
import { PrismaPlanetScale } from "@prisma/adapter-planetscale";

export default {
  async fetch(request, env, ctx) {
    const adapter = new PrismaPlanetScale({
      url: env.DATABASE_URL,
      // see https://github.com/cloudflare/workerd/issues/698
      fetch(url, init) {
        delete init["cache"];
        return fetch(url, init);
      },
    });
    const prisma = new PrismaClient({ adapter });

    const users = await prisma.user.findMany();
    const result = JSON.stringify(users);
    ctx.waitUntil(prisma.$disconnect());
    return new Response(result);
  },
};
```

#### [6\. Run the Worker locally](#6-run-the-worker-locally-1)

To run the Worker locally, you can run the `wrangler dev` command:

#### [7\. Set the `DATABASE_URL` environment variable and deploy the Worker](#7-set-the-database_url-environment-variable-and-deploy-the-worker-1)

To deploy the Worker, you first need to the `DATABASE_URL` environment variable [via the `wrangler` CLI](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers):

The command is interactive and will ask you to enter the value for the `DATABASE_URL` env var as the next step in the terminal.

Then you can go ahead then deploy the Worker:

The command will output the URL where you can access the deployed Worker.

### [Neon](#neon)

If you are using a Neon database, you need to:

-   use the `@prisma/adapter-neon` database adapter (learn more [here](https://www.prisma.io/docs/orm/core-concepts/supported-databases/postgresql#using-driver-adapters))

#### [1\. Configure Prisma schema & database connection](#1-configure-prisma-schema--database-connection-2)

First, ensure that the database connection is configured properly. Database connection URLs are configured in `prisma.config.ts`:

schema.prisma

```
generator client {
  provider = "prisma-client"
  output   = "./generated"
}

datasource db {
  provider = "postgresql"
}
```

prisma.config.ts

```
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

Next, you need to set the `DATABASE_URL` environment variable to the value of your database connection string. You'll do this in a file called `.dev.vars` used by Cloudflare:

.dev.vars

```
DATABASE_URL="postgresql://janedoe:password@ep-nameless-pond-a23b1mdz.eu-central-1.aws.neon.tech/neondb?sslmode=require"
```

Because the Prisma CLI by default is only compatible with `.env` files, you can adjust your `package.json` with the following script that loads the env vars from `.dev.vars`. You can then use this script to load the env vars before executing a `prisma` command.

Add this script to your `package.json`:

package.json

```
{
  // ...
  "scripts": {
    // ....
    "env": "dotenv -e .dev.vars"
  },
  // ...
}
```

Now you can execute Prisma CLI commands as follows while ensuring that the command has access to the env vars in `.dev.vars`:

#### [2\. Install dependencies](#2-install-dependencies-2)

Next, install the required packages:

#### [3\. Migrate your database schema (if applicable)](#3-migrate-your-database-schema-if-applicable-1)

If you ran `npx prisma init` above, you need to migrate your database schema to create the `User` table that's defined in your Prisma schema (if you already have all the tables you need in your database, you can skip this step):

#### [5\. Use Prisma Client in your Worker to send a query to the database](#5-use-prisma-client-in-your-worker-to-send-a-query-to-the-database-1)

Here is a sample code snippet that you can use to instantiate `PrismaClient` and send a query to your database:

```
import { PrismaClient } from "./generated/client";
import { PrismaNeon } from "@prisma/adapter-neon";

export default {
  async fetch(request, env, ctx) {
    const adapter = new PrismaNeon({ connectionString: env.DATABASE_URL });
    const prisma = new PrismaClient({ adapter });

    const users = await prisma.user.findMany();
    const result = JSON.stringify(users);
    ctx.waitUntil(prisma.$disconnect());
    return new Response(result);
  },
};
```

#### [6\. Run the Worker locally](#6-run-the-worker-locally-2)

To run the Worker locally, you can run the `wrangler dev` command:

#### [7\. Set the `DATABASE_URL` environment variable and deploy the Worker](#7-set-the-database_url-environment-variable-and-deploy-the-worker-2)

To deploy the Worker, you first need to the `DATABASE_URL` environment variable [via the `wrangler` CLI](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-on-deployed-workers):

The command is interactive and will ask you to enter the value for the `DATABASE_URL` env var as the next step in the terminal.

Then you can go ahead then deploy the Worker:

The command will output the URL where you can access the deployed Worker.

### [Cloudflare D1](#cloudflare-d1)
