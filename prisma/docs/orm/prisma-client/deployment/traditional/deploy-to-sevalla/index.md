---
title: "Deploy to Sevalla"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-sevalla"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/traditional/deploy-to-sevalla"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:42.853Z"
content_hash: "1e4ad1aa44ffb6aeb48428c75f961443d3d8835676e5116458265f891380af3b"
menu_path: ["Deploy to Sevalla"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/traditional/deploy-to-render/index.md", "title": "Deploy to Render"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/connection-management/index.md", "title": "Connection management"}
---

This guide explains how to deploy a Node.js server that uses Prisma ORM and PostgreSQL to [Sevalla](https://sevalla.com/). The app exposes a REST API and uses Prisma Client to query a PostgreSQL database. Both the app and database will be hosted on Sevalla.

Sevalla is a developer-focused PaaS platform designed to simplify application and server deployment. You can easily host your applications, databases, object storage and static sites.

It supports Git-based deployments, Dockerfiles, and Procfiles and runs on Google Kubernetes Engine with global delivery via Cloudflare.

For this example, it's helpful to know:

*   Sevalla supports long-running “serverful” applications with built-in autoscaling and flexible pod sizes.
*   Git-based deployments are integrated with GitHub, GitLab, and Bitbucket.
*   PostgreSQL, MySQL, MariaDB, Redis, and Valkey databases are natively supported.
*   Applications and databases can be securely connected through private networking with automatic environment variable injection.

To get started, all you need is:

*   A [Sevalla account](https://sevalla.com/) (comes with $50 in free credits)
*   A GitHub repository with your application code.

> **Note:** If you don't have a project ready, you can use our [example Prisma project](https://github.com/sevalla-templates/express-prisma-demo). It's a simple Express.js application that uses Prisma ORM and includes a REST API, a frontend for testing endpoints, a defined Prisma schema with migrations, and an optional database seeding script.

First, create a new application on your Sevalla dashboard. Click **Applications** on the sidebar and then click the **Create an app** button, as shown below.

![Sevalla app creation interface](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-app-creation.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Next, select your Git repository. Sevalla supports deploying from both private and public repositories. If you're using our example project, there's no need to fork — simply enter the URL `https://github.com/sevalla-templates/express-prisma-demo`.

![Choose repository interface in Sevalla](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-choose-repository.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Choose the appropriate branch (usually `main` or `master`), set your application's name, select the desired deployment region, and pick your pod size. (You can start with 0.5 CPU / 1GB RAM using your free credits)

![Name application interface in Sevalla](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-name-application.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Click **Create**, but skip the deploy step for now, so it does not fail since we have not added the database.

On your Sevalla dashboard, click **Databases** > **Add database**. Select **PostgreSQL** (or your preferred configured database type), and then provide a database name, username, and password, or simply use the default generated details.

![Create database interface in Sevalla](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-create-database.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Next, give the database a recognizable name for easy identification within your Sevalla dashboard. Ensure you select the **same region** as your application, choose an appropriate database size, and click **Create**.

Once your database has been created, scroll down to the **Connected Applications** section and click **Add Connection**.

Select the application you created previously and enable "Add environment variables". Make sure the variable name is set to `DATABASE_URL` (if it defaults to `DB_URL`, change it accordingly).

![App internal connection interface in Sevalla](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-app-internal-connection.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Finally, click **Add connection**. This securely links your application to your database and configures the necessary environment variable.

Now that your application and database are connected, return to your application's **Deployment** tab and click **Deploy**.

> **Note:** Sevalla automatically builds your application using Nixpacks, detecting your project's `package.json` and `start` script. If you'd rather use a Dockerfile or Buildpacks, navigate to **Settings** > **Build**, and click **Update Settings** under the **Build environment** section to customize your build method.

If your project includes a seed script (typically located at `prisma/seed.js`), you can populate your database with initial or demo data after deploying your application.

To do this, navigate to your application's **Web Terminal** (under **Applications** > **\[Your App\]** > **Web Terminal**) and run the following command:

This is what the web terminal looks like:

![Sevalla web terminal interface](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-web-terminal.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Once this is done, you can manage and interact with your database directly via Sevalla's built-in interactive studio. As shown below, we can see the seeded data:

![Sevalla database studio interface](https://www.prisma.io/docs/img/orm/prisma-client/deployment/traditional/images/sevalla-database-studio.png?dpl=dpl_2TrAJrUt7dXR3AAWNDvwk5WL6VFX)

Congratulations! You've successfully deployed a Node.js application using Prisma ORM to Sevalla. Your app and database are now connected, secure, and production-ready!


