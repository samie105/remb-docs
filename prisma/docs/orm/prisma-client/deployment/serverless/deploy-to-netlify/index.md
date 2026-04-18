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
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions/index.md", "title": "Deploy to Azure Functions"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/serverless/deploy-to-vercel/index.md", "title": "Deploy to Vercel"}
---

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

For more information on connection management for serverless environments, refer to our [connection management guide](prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md#serverless-environments-faas).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/serverless/deploy-to-netlify.mdx)


