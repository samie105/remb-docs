---
title: "Deploy to Fly.io"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-flyio"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-flyio"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:24.343Z"
content_hash: "1883eba565f11f1f1c4404751d85145790e07f587c3fc5d865289bd19d23b29d"
menu_path: ["Deploy to Fly.io"]
section_path: []
---
Deployment

Traditional

Learn how to deploy a Node.js server that uses Prisma ORM to Fly.io

This guide explains how to deploy a Node.js server that uses Prisma ORM and PostgreSQL to Fly.io.

The [Prisma Render deployment example](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render) contains an Express.js application with REST endpoints and a simple frontend. This app uses Prisma Client to fetch, create, and delete records from its database. This guide will show you how to deploy the same application, without modification, on Fly.io.

[fly.io](https://fly.io/) is a cloud application platform that lets developers easily deploy and scale full-stack applications that start on request near on machines near to users. For this example, it's helpful to know:

*   Fly.io lets you deploy long-running, "serverful" full-stack applications in [35 regions around the world](https://fly.io/docs/reference/regions/). By default, applications are configured to to [auto-stop](https://fly.io/docs/launch/autostop-autostart/) when not in use, and auto-start as needed as requests come in.
*   Fly.io natively supports a wide variety of [languages and frameworks](https://fly.io/docs/languages-and-frameworks/), including Node.js and Bun. In this guide, we'll use the Node.js runtime.
*   Fly.io can [launch apps directly from GitHub](https://fly.io/speedrun). When run from the CLI, `fly launch` will automatically configure applications hosted on GitHub to deploy on push.

*   Sign up for a [Fly.io](https://fly.io/docs/getting-started/launch/) account

Download the [example code](https://github.com/prisma/prisma-examples/tree/latest/deployment-platforms/render) to your local machine.

```
curl https://codeload.github.com/prisma/prisma-examples/tar.gz/latest | tar -xz --strip=2 prisma-examples-latest/deployment-platforms/render
cd render
```

Before we deploy the app, let's take a look at the example code.

### [Web application](#web-application)

The logic for the Express app is in two files:

*   `src/index.js`: The API. The endpoints use Prisma Client to fetch, create, and delete data from the database.
*   `public/index.html`: The web frontend. The frontend calls a few of the API endpoints.

### [Prisma schema and migrations](#prisma-schema-and-migrations)

The Prisma components of this app are in three files:

*   `prisma/schema.prisma`: The data model of this app. This example defines two models, `User` and `Post`. The format of this file follows the [Prisma schema](https://www.prisma.io/docs/orm/prisma-schema/overview).
*   `prisma/migrations/<migration name>/migration.sql`: The SQL commands that construct this schema in a PostgreSQL database. You can auto-generate migration files like this one by running [`prisma migrate dev`](https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/mental-model#what-is-prisma-migrate).
*   `prisma/seed.js`: defines some test users and postsPrisma, used to [seed the database](https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding) with starter data.

### [1\. Run `fly launch` and accept the defaults](#1-run-fly-launch-and-accept-the-defaults)

That’s it. Your web service will be live at its `fly.dev` URL as soon as the deploy completes. Optionally [scale](https://fly.io/docs/launch/scale-count/) the size, number, and placement of machines as desired. [`fly console`](https://fly.io/docs/flyctl/console/) can be used to ssh into a new or existing machine.

More information can be found on in the [fly.io documentation](https://fly.io/docs/js/prisma/).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/traditional/deploy-to-flyio.mdx)
