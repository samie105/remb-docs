---
title: "Deploy to Netlify"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:14.323Z"
content_hash: "5af30bc8ab96cd1985798bac8263beac7d08a68d01ac11177100a2c8bbfdd6fd"
menu_path: ["Deploy to Netlify"]
section_path: []
---
Deployment

Serverless

Learn how to deploy Node.js and TypeScript applications that are using Prisma Client to Netlify

This guide covers the steps you will need to take in order to deploy your application that uses Prisma ORM to [Netlify](https://www.netlify.com/).

Netlify is a cloud platform for continuous deployment, static sites, and serverless functions. Netlify integrates seamlessly with GitHub for automatic deployments upon commits. When you follow the steps below, you will use that approach to create a CI/CD pipeline that deploys your application from a GitHub repository.

Before you can follow this guide, you will need to set up your application to begin deploying to Netlify. We recommend the ["Get started with Netlify"](https://docs.netlify.com/get-started/) guide for a quick overview and ["Deploy functions"](https://docs.netlify.com/functions/deploy/?fn-language=ts) for an in-depth look at your deployment options.

We recommend keeping `.env` files in your `.gitignore` in order to prevent leakage of sensitive connection strings. Instead, you can use the Netlify CLI to [import values into netlify directly](https://docs.netlify.com/environment-variables/get-started/#import-variables-with-the-netlify-cli).

Assuming you have a file like the following:

```
# Connect to DB
DATABASE_URL="postgresql://postgres:__PASSWORD__@__HOST__:__PORT__/__DB_NAME__"
```

You can upload the file as environment variables using the `env:import` command:

```
netlify env:import .env
```

```
site: my-very-very-cool-site
---------------------------------------------------------------------------------.
                         Imported environment variables                          |
---------------------------------------------------------------------------------|
     Key      |                              Value                               |
--------------|------------------------------------------------------------------|
 DATABASE_URL | postgresql://postgres:__PASSWORD__@__HOST__:__PORT__/__DB_NAME__ |
---------------------------------------------------------------------------------'
```

If you are not using an `.env` file

If you are storing your database connection string and other environment variables in a different method, you will need to manually upload your environment variables to Netlify. These options are [discussed in Netlify's documentation](https://docs.netlify.com/environment-variables/get-started/) and one method, uploading via the UI, is described below.

1.  Open the Netlify admin UI for the site. You can use Netlify CLI as follows:
    
    ```
    netlify open --admin
    ```
    
2.  Click **Site settings**: ![Netlify admin UI](https://www.prisma.io/docs/img/orm/prisma-client/deployment/serverless/images/500-06-deploy-to-netlify-site-settings.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)
3.  Navigate to **Build & deploy** in the sidebar on the left and select **Environment**.
4.  Click **Edit variables** and create a variable with the key `DATABASE_URL` and set its value to your database connection string. ![Netlify environment variables](https://www.prisma.io/docs/img/orm/prisma-client/deployment/serverless/images/500-07-deploy-to-netlify-environment-variables-settings.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)
5.  Click **Save**.

Now start a new Netlify build and deployment so that the new build can use the newly uploaded environment variables.

```
netlify deploy
```

You can now test the deployed application.

When you use a Function-as-a-Service provider, like Netlify, it is beneficial to pool database connections for performance reasons. This is because every function invocation may result in a new connection to your database which can quickly run out of open connections.

You can use [Prisma Postgres](https://www.prisma.io/docs/postgres), which has built-in connection pooling, to reduce your Prisma Client bundle size, and to avoid cold starts.

For more information on connection management for serverless environments, refer to our [connection management guide](https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify.mdx)
