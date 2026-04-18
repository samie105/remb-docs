---
title: "Deploy to Deno Deploy"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:48.743Z"
content_hash: "f43f436bd4c0f25f8361fab149a40e085b024454c1d4f19c0ef2358e82a84455"
menu_path: ["Deploy to Deno Deploy"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare/index.md", "title": "Deploy to Cloudflare Workers & Pages"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/edge/deploy-to-vercel/index.md", "title": "Deploy to Vercel Edge Functions & Middleware"}
---

# Get API info
curl http://localhost:8000/

# Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Prisma", "description": "Complete the Deno guide"}'

# List all tasks
curl http://localhost:8000/tasks

# Update a task (mark as completed)
curl -X PATCH http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete a task
curl -X DELETE http://localhost:8000/tasks/1
```

You should see JSON responses for each request. The task ID will increment with each new task created.

You need a GitHub repository to deploy to Deno Deploy.

Create a `.gitignore` file:

```
.env
node_modules/
generated/
deno.lock
```

Initialize and push your repository:

```
git init -b main
git remote add origin https://github.com/<username>/prisma-deno-deploy
git add .
git commit -m "Initial commit"
git push -u origin main
```

1.  Go to [https://dash.deno.com/](https://dash.deno.com/)
2.  Click **New Project** and select your GitHub repository
3.  Configure the deployment:
    *   **Framework preset**: No Preset
    *   **Install command**: `deno install`
    *   **Build command**: `deno run -A npm:prisma generate`
    *   **Entrypoint**: `index.ts`
4.  Click **Create & Deploy**

The first deployment will fail because you need to add the database connection string.

### [Add environment variables](#add-environment-variables)

1.  Go to your project's **Settings** > **Environment Variables**
2.  Add a new variable:
    *   **Key**: `DATABASE_URL`
    *   **Value**: Your Prisma Postgres connection string (copy from your `.env` file)
3.  Click **Save**

Trigger a new deployment by clicking **Redeploy** or pushing a new commit.

Once deployed, test your API at your Deno Deploy URL:

```
# Replace with your actual Deno Deploy URL
curl https://your-project.deno.dev/

# Create a task
curl -X POST https://your-project.deno.dev/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Deploy to production"}'

# List tasks
curl https://your-project.deno.dev/tasks
```

You successfully deployed a REST API to Deno Deploy using:

*   **Deno** as the runtime with native TypeScript support
*   **Prisma ORM** with the Postgres adapter for type-safe database access
*   **Prisma Postgres** as the managed database

Your project structure should look like this:

```
prisma-deno-deploy/
├── deno.json
├── index.ts
├── prisma/
│   └── schema.prisma
├── prisma.config.ts
├── generated/
│   └── prisma/
│       └── ...
└── .env
```

### [Next steps](#next-steps)

*   Add authentication using [Deno KV](https://docs.deno.com/deploy/reference/deno_kv/) for sessions
*   Add request validation with [Zod](https://zod.dev/)
*   Explore [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) for custom functionality
*   Set up [Prisma Migrate](prisma/docs/orm/prisma-migrate/index.md) for schema versioning in production

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy.mdx)


