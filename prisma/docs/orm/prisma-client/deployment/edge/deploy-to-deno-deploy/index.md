---
title: "Deploy to Deno Deploy"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-deno-deploy"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:43:19.351Z"
content_hash: "861fdad07c50883f543c25f752ad7b3bbec191e1e1e9e44bfa668e7ebffdd62b"
menu_path: ["Deploy to Deno Deploy"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun"]
content_language: "en"
---
With this guide, you can learn how to build and deploy a REST API to [Deno Deploy](https://deno.com/deploy). The application uses Prisma ORM to manage tasks in a [Prisma Postgres](https://www.prisma.io/docs/postgres) database.

This guide covers Deno CLI, Deno Deploy, Prisma Client with the Postgres adapter, and Prisma Postgres.

-   A free [Prisma Data Platform](https://console.prisma.io/login?utm_source=docs&utm_medium=content&utm_content=orm) account
-   A free [Deno Deploy](https://deno.com/deploy) account
-   [Deno](https://docs.deno.com/runtime/#install-deno) v2.0 or later installed
-   (Recommended) [Deno extension for VS Code](https://docs.deno.com/runtime/reference/vscode/)

Create a new directory and initialize your Prisma project:

Enter a name for your project and choose a database region.

This command:

-   Connects to the [Prisma Data Platform](https://console.prisma.io/?utm_source=docs&utm_medium=content&utm_content=orm) (opens browser for authentication)
-   Creates a `prisma/schema.prisma` file for your database models
-   Creates a `.env` file with your `DATABASE_URL`
-   Creates a `prisma.config.ts` configuration file

Create a `deno.json` file with the following configuration:

deno.json

```
{
  "nodeModulesDir": "auto",
  "compilerOptions": {
    "lib": ["deno.window"],
    "types": ["node"]
  },
  "imports": {
    "@prisma/adapter-pg": "npm:@prisma/adapter-pg@^7.0.0",
    "@prisma/client": "npm:@prisma/client@^7.0.0",
    "prisma": "npm:prisma@^7.0.0"
  },
  "tasks": {
    "dev": "deno run -A --env=.env --watch index.ts",
    "db:generate": "deno run -A --env=.env npm:prisma generate",
    "db:push": "deno run -A --env=.env npm:prisma db push",
    "db:migrate": "deno run -A --env=.env npm:prisma migrate dev",
    "db:studio": "deno run -A --env=.env npm:prisma studio"
  }
}
```

Install the dependencies:

```
deno install
deno install --allow-scripts
```

Edit `prisma/schema.prisma` to add the Deno runtime and a `Task` model:

prisma/schema.prisma

```
generator client {
  provider = "prisma-client"
  output   = "../generated/prisma"
  runtime  = "deno"
}

datasource db {
  provider = "postgresql"
}

model Task {
  id          Int      @id @default(autoincrement())
  title       String
  description String?
  completed   Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}
```

Apply the schema to your database and generate Prisma Client:

```
deno task db:push
```

This command:

1.  Creates the `Task` table in your Prisma Postgres database
2.  Generates the Prisma Client with full type safety

Create `index.ts` with a REST API for managing tasks:

index.ts

```
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "./generated/prisma/client.ts";

// Initialize Prisma Client with the Postgres adapter
const connectionString = Deno.env.get("DATABASE_URL")!;
const adapter = new PrismaPg({ connectionString });
const prisma = new PrismaClient({ adapter });

// Helper to create JSON responses
function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

// Request handler
async function handler(request: Request): Promise<Response> {
  const url = new URL(request.url);
  const path = url.pathname;
  const method = request.method;

  try {
    // GET /tasks - List all tasks
    if (method === "GET" && path === "/tasks") {
      const tasks = await prisma.task.findMany({
        orderBy: { createdAt: "desc" },
      });
      return json(tasks);
    }

    // POST /tasks - Create a new task
    if (method === "POST" && path === "/tasks") {
      const body = await request.json();
      const task = await prisma.task.create({
        data: {
          title: body.title,
          description: body.description,
        },
      });
      return json(task, 201);
    }

    // GET /tasks/:id - Get a specific task
    const taskMatch = path.match(/^\/tasks\/(\d+)$/);
    if (taskMatch) {
      const id = parseInt(taskMatch[1]);

      if (method === "GET") {
        const task = await prisma.task.findUnique({ where: { id } });
        if (!task) return json({ error: "Task not found" }, 404);
        return json(task);
      }

      // PATCH /tasks/:id - Update a task
      if (method === "PATCH") {
        const body = await request.json();
        const task = await prisma.task.update({
          where: { id },
          data: body,
        });
        return json(task);
      }

      // DELETE /tasks/:id - Delete a task
      if (method === "DELETE") {
        await prisma.task.delete({ where: { id } });
        return json({ message: "Task deleted" });
      }
    }

    // GET / - API info
    if (method === "GET" && path === "/") {
      return json({
        name: "Prisma + Deno Task API",
        version: "1.0.0",
        endpoints: {
          "GET /tasks": "List all tasks",
          "POST /tasks": "Create a task",
          "GET /tasks/:id": "Get a task",
          "PATCH /tasks/:id": "Update a task",
          "DELETE /tasks/:id": "Delete a task",
        },
      });
    }

    return json({ error: "Not found" }, 404);
  } catch (error) {
    console.error(error);
    return json({ error: "Internal server error" }, 500);
  }
}

// Start the server
Deno.serve({ port: 8000 }, handler);
```

This creates a full CRUD API with the following endpoints:

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | API info |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/:id` | Get a specific task |
| PATCH | `/tasks/:id` | Update a task |
| DELETE | `/tasks/:id` | Delete a task |

Start the development server:

```
deno task dev
```

Test the API with curl:

```
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

.gitignore

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
    -   **Framework preset**: No Preset
    -   **Install command**: `deno install`
    -   **Build command**: `deno run -A npm:prisma generate`
    -   **Entrypoint**: `index.ts`
4.  Click **Create & Deploy**

The first deployment will fail because you need to add the database connection string.

### [Add environment variables](#add-environment-variables)

1.  Go to your project's **Settings** > **Environment Variables**
2.  Add a new variable:
    -   **Key**: `DATABASE_URL`
    -   **Value**: Your Prisma Postgres connection string (copy from your `.env` file)
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

-   **Deno** as the runtime with native TypeScript support
-   **Prisma ORM** with the Postgres adapter for type-safe database access
-   **Prisma Postgres** as the managed database

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

-   Add authentication using [Deno KV](https://docs.deno.com/deploy/reference/deno_kv/) for sessions
-   Add request validation with [Zod](https://zod.dev/)
-   Explore [Prisma Client extensions](https://www.prisma.io/docs/orm/prisma-client/client-extensions) for custom functionality
-   Set up [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate) for schema versioning in production
