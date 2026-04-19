---
title: "Deploy migrations from a local environment"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:52.405Z"
content_hash: "83e021b30e11f7561f47bb444b357a751191e5330d38050c18c237843f9f1cd2"
menu_path: ["Deploy migrations from a local environment"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate/index.md", "title": "Deploying database changes with Prisma Migrate"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/deploy-prisma/index.md", "title": "Deploy Prisma ORM"}
---

Deployment

Learn how to deploy Node.js and TypeScript applications that are using Prisma Client locally

There are two scenarios where you might consider deploying migrations directly from a local environment to a production environment.

*   You have a local CI/CD pipeline
*   You are [baselining](prisma/docs/orm/prisma-migrate/workflows/baselining/index.md) a production environment

This page outlines some examples of how you can do that and **why we would generally not recommend it**.

If you do not have an automated CI/CD process, you can technically deploy new migrations from your local environment to production in the following ways:

1.  Make sure your migration history is up to date. You can do this through running `prisma migrate dev`, which will generate a migration history from the latest changes made.
2.  Swap your local connection URL for your production connection URL

```
DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/my_local_database"

DATABASE_URL="postgresql://johndoe:randompassword@prod-db.example.com:5432/my_production_database"
```

3.  Run `prisma migrate deploy`

**⛔ We strongly discourage this solution due to the following reasons**

*   You risk exposing your production database connection URL to version control.
*   You may accidentally use your production connection URL instead and in turn **override or delete your production database**.

**✅ We recommend setting up an automated CI/CD pipeline**

The pipeline should handle deployment to staging and production environments, and use `migrate deploy` in a pipeline step. See the [deployment guides](prisma/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate/index.md) for examples.

When you add Prisma Migrate to an **existing database**, you must [baseline](prisma/docs/orm/prisma-migrate/workflows/baselining/index.md) the production database. Baselining is performed **once**, and can be done from a local instance.

![Baselining production from local with Prisma ORM](https://www.prisma.io/docs/img/orm/baseline-production-from-local.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment.mdx)
