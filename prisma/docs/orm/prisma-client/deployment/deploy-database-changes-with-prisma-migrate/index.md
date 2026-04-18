---
title: "Deploying database changes with Prisma Migrate"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:48.535Z"
content_hash: "31d75ff5386e72003610d15782b2d5086e0c11d0254349618906beb3d4420309"
menu_path: ["Deploying database changes with Prisma Migrate"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/caveats-when-deploying-to-aws-platforms/index.md", "title": "Caveats when deploying to AWS platforms"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/deploy-migrations-from-a-local-environment/index.md", "title": "Deploy migrations from a local environment"}
---

Deployment

Learn how to deploy database changes with Prisma Migrate

To apply pending migrations to staging, testing, or production environments, run the `migrate deploy` command as part of your CI/CD pipeline:

Exactly when to run `prisma migrate deploy` depends on your platform. For example, a simplified [Heroku](prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-heroku/index.md) workflow includes:

1.  Ensuring the `./prisma/migration` folder is in source control
2.  Running `prisma migrate deploy` during the [release phase](https://devcenter.heroku.com/articles/release-phase)

Ideally, `migrate deploy` should be part of an automated CI/CD pipeline, and we do not generally recommend running this command locally to deploy changes to a production database (for example, by temporarily changing the `DATABASE_URL` environment variable). It is not generally considered good practice to store the production database URL locally.

Beware that in order to run the `prisma migrate deploy` command, you need access to the `prisma` dependency that is typically added to the `devDependencies`. Some platforms like Vercel, prune development dependencies during the build, thereby preventing you from calling the command. This can be worked around by making the `prisma` a production dependency, by moving it to `dependencies` in your `package.json`. For more information about the `migrate deploy` command, see:

*   [`migrate deploy` reference](prisma/docs/orm/reference/prisma-cli-reference/index.md#migrate-deploy)
*   [How `migrate deploy` works](prisma/docs/orm/prisma-migrate/workflows/development-and-production/index.md#production-and-testing-environments)
*   [Production troubleshooting](prisma/docs/orm/prisma-migrate/workflows/patching-and-hotfixing/index.md)

As part of your CI/CD, you can run `prisma migrate deploy` as part of your pipeline to apply pending migrations to your production database.

Here is an example action that will run your migrations against your database:

```
name: Deploy
on:
  push:
    paths:
      - prisma/migrations/**
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3
      - name: Setup Node
        uses: actions/setup-node@v3
      - name: Install dependencies
        run: npm install
      - name: Apply all pending migrations to the database
        run: npx prisma migrate deploy
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

The highlighted line shows that this action will only run if there is a change in the `prisma/migrations` directory, so `npx prisma migrate deploy` will only run when migrations are updated.

Ensure you have the `DATABASE_URL` variable [set as a secret in your repository](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions), without quotes around the connection string.

Before running `prisma migrate deploy`, you can analyze your migration SQL files for potentially dangerous patterns using a migration safety tool like [pgfence](https://www.prisma.io/docs/guides/integrations/pgfence). pgfence detects operations that acquire heavy locks (such as `CREATE INDEX` without `CONCURRENTLY` or `ALTER COLUMN TYPE`), reports risk levels, and provides safe rewrite recipes.

To add pgfence as a pre-deploy step in your GitHub Actions workflow:

```
- name: Run migration safety check
  run: npx @flvmnt/pgfence analyze --ci --max-risk medium prisma/migrations/**/migration.sql

- name: Apply all pending migrations to the database
  run: npx prisma migrate deploy
  env:
    DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

For a full setup guide, see the [pgfence integration guide](https://www.prisma.io/docs/guides/integrations/pgfence).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate.mdx)


