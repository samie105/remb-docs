---
title: "Fullstack dev server"
source: "https://bun.com/docs/bundler/fullstack"
canonical_url: "https://bun.com/docs/bundler/fullstack"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:32.050Z"
content_hash: "9653c13d4469e45216009acb4c922d5a72f56639b0021ead2842836aab01ef1d"
menu_path: ["Fullstack dev server"]
section_path: []
---
To get started, import HTML files and pass them to the `routes` option in `Bun.serve()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import { serve } from "bun";
import dashboard from "./dashboard.html";
import homepage from "./index.html";

const server = serve({
  routes: {
    // ** HTML imports **
    // Bundle & route index.html to "/". This uses HTMLRewriter to scan
    // the HTML for `<script>` and `<link>` tags, runs Bun's JavaScript
    // & CSS bundler on them, transpiles any TypeScript, JSX, and TSX,
    // downlevels CSS with Bun's CSS parser and serves the result.
    "/": homepage,
    // Bundle & route dashboard.html to "/dashboard"
    "/dashboard": dashboard,

    // ** API endpoints ** (Bun v1.2.3+ required)
    "/api/users": {
      async GET(req) {
        const users = await sql`SELECT * FROM users`;
        return Response.json(users);
      },
      async POST(req) {
        const { name, email } = await req.json();
        const [user] = await sql`INSERT INTO users (name, email) VALUES (${name}, ${email})`;
        return Response.json(user);
      },
    },
    "/api/users/:id": async req => {
      const { id } = req.params;
      const [user] = await sql`SELECT * FROM users WHERE id = ${id}`;
      return Response.json(user);
    },
  },

  // Enable development mode for:
  // - Detailed error messages
  // - Hot reloading (Bun v1.2.3+ required)
  development: true,
});

console.log(`Listening on ${server.url}`);
```

terminal

```
bun run app.ts
```

## HTML Routes

### HTML Imports as Routes

The web starts with HTML, and so does Bun’s fullstack dev server. To specify entrypoints to your frontend, import HTML files into your JavaScript/TypeScript/TSX/JSX files.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import dashboard from "./dashboard.html";
import homepage from "./index.html";
```

These HTML files are used as routes in Bun’s dev server you can pass to `Bun.serve()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
Bun.serve({
  routes: {
    "/": homepage,
    "/dashboard": dashboard,
  },

  fetch(req) {
    // ... api requests
  },
});
```

When you make a request to `/dashboard` or `/`, Bun automatically bundles the `<script>` and `<link>` tags in the HTML files, exposes them as static routes, and serves the result.

### HTML Processing Example

An `index.html` file like this:

index.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
    <link rel="stylesheet" href="./reset.css" />
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="./sentry-and-preloads.ts"></script>
    <script type="module" src="./my-app.tsx"></script>
  </body>
</html>
```

Becomes something like this:

index.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>Home</title>
    <link rel="stylesheet" href="/index-[hash].css" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/index-[hash].js"></script>
  </body>
</html>
```

## React Integration

To use React in your client-side code, import `react-dom/client` and render your app.

## Development Mode

When building locally, enable development mode by setting `development: true` in `Bun.serve()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
import homepage from "./index.html";
import dashboard from "./dashboard.html";

Bun.serve({
  routes: {
    "/": homepage,
    "/dashboard": dashboard,
  },

  development: true,

  fetch(req) {
    // ... api requests
  },
});
```

### Development Mode Features

When `development` is `true`, Bun will:

*   Include the SourceMap header in the response so that devtools can show the original source code
*   Disable minification
*   Re-bundle assets on each request to a `.html` file
*   Enable hot module reloading (unless `hmr: false` is set)
*   Echo console logs from browser to terminal

### Advanced Development Configuration

`Bun.serve()` supports echoing console logs from the browser to the terminal. To enable this, pass `console: true` in the development object in `Bun.serve()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
import homepage from "./index.html";

Bun.serve({
  // development can also be an object.
  development: {
    // Enable Hot Module Reloading
    hmr: true,

    // Echo console logs from the browser to the terminal
    console: true,
  },

  routes: {
    "/": homepage,
  },
});
```

When `console: true` is set, Bun will stream console logs from the browser to the terminal. This reuses the existing WebSocket connection from HMR to send the logs.

### Development vs Production

Feature

Development

Production

**Source maps**

✅ Enabled

❌ Disabled

**Minification**

❌ Disabled

✅ Enabled

**Hot reloading**

✅ Enabled

❌ Disabled

**Asset bundling**

🔄 On each request

💾 Cached

**Console logging**

🖥️ Browser → Terminal

❌ Disabled

**Error details**

📝 Detailed

🔒 Minimal

## Production Mode

Hot reloading and `development: true` helps you iterate quickly, but in production, your server should be as fast as possible and have as few external dependencies as possible.

### Ahead of Time Bundling (Recommended)

As of Bun v1.2.17, you can use `Bun.build` or `bun build` to bundle your full-stack application ahead of time.

terminal

```
bun build --target=bun --production --outdir=dist ./src/index.ts
```

When Bun’s bundler sees an HTML import from server-side code, it will bundle the referenced JavaScript/TypeScript/TSX/JSX and CSS files into a manifest object that `Bun.serve()` can use to serve the assets.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
import { serve } from "bun";
import index from "./index.html";

serve({
  routes: { "/": index },
});
```

### Runtime Bundling

When adding a build step is too complicated, you can set `development: false` in `Bun.serve()`. This will:

*   Enable in-memory caching of bundled assets. Bun will bundle assets lazily on the first request to an `.html` file, and cache the result in memory until the server restarts.
*   Enable `Cache-Control` headers and `ETag` headers
*   Minify JavaScript/TypeScript/TSX/JSX files

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
import { serve } from "bun";
import homepage from "./index.html";

serve({
  routes: {
    "/": homepage,
  },

  // Production mode
  development: false,
});
```

## API Routes

### HTTP Method Handlers

Define API endpoints with HTTP method handlers:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
import { serve } from "bun";

serve({
  routes: {
    "/api/users": {
      async GET(req) {
        // Handle GET requests
        const users = await getUsers();
        return Response.json(users);
      },

      async POST(req) {
        // Handle POST requests
        const userData = await req.json();
        const user = await createUser(userData);
        return Response.json(user, { status: 201 });
      },

      async PUT(req) {
        // Handle PUT requests
        const userData = await req.json();
        const user = await updateUser(userData);
        return Response.json(user);
      },

      async DELETE(req) {
        // Handle DELETE requests
        await deleteUser(req.params.id);
        return new Response(null, { status: 204 });
      },
    },
  },
});
```

### Dynamic Routes

Use URL parameters in your routes:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
serve({
  routes: {
    // Single parameter
    "/api/users/:id": async req => {
      const { id } = req.params;
      const user = await getUserById(id);
      return Response.json(user);
    },

    // Multiple parameters
    "/api/users/:userId/posts/:postId": async req => {
      const { userId, postId } = req.params;
      const post = await getPostByUser(userId, postId);
      return Response.json(post);
    },

    // Wildcard routes
    "/api/files/*": async req => {
      const filePath = req.params["*"];
      const file = await getFile(filePath);
      return new Response(file);
    },
  },
});
```

### Request Handling

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)src/backend.ts

```
serve({
  routes: {
    "/api/data": {
      async POST(req) {
        // Parse JSON body
        const body = await req.json();

        // Access headers
        const auth = req.headers.get("Authorization");

        // Access URL parameters
        const { id } = req.params;

        // Access query parameters
        const url = new URL(req.url);
        const page = url.searchParams.get("page") || "1";

        // Return response
        return Response.json({
          message: "Data processed",
          page: parseInt(page),
          authenticated: !!auth,
        });
      },
    },
  },
});
```

## Plugins

Bun’s bundler plugins are also supported when bundling static routes. To configure plugins for `Bun.serve`, add a `plugins` array in the `[serve.static]` section of your `bunfig.toml`.

### TailwindCSS Plugin

You can use TailwindCSS by installing and adding the `tailwindcss` package and `bun-plugin-tailwind` plugin.

terminal

```
bun add tailwindcss bun-plugin-tailwind
```

bunfig.toml

```
[serve.static]
plugins = ["bun-plugin-tailwind"]
```

This will allow you to use TailwindCSS utility classes in your HTML and CSS files. Import `tailwindcss` somewhere in your project:

index.html

```
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="tailwindcss" />
  </head>
  <!-- the rest of your HTML... -->
</html>
```

Alternatively, you can import TailwindCSS in your CSS file:

style.css

```
@import "tailwindcss";

.custom-class {
  @apply bg-red-500 text-white;
}
```

index.html

```
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="./style.css" />
  </head>
  <!-- the rest of your HTML... -->
</html>
```

### Custom Plugins

Any JS file or module which exports a valid bundler plugin object (essentially an object with a `name` and `setup` field) can be placed inside the plugins array:

bunfig.toml

```
[serve.static]
plugins = ["./my-plugin-implementation.ts"]
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)my-plugin-implementation.ts

```
import type { BunPlugin } from "bun";

const myPlugin: BunPlugin = {
  name: "my-custom-plugin",
  setup(build) {
    // Plugin implementation
    build.onLoad({ filter: /\.custom$/ }, async args => {
      const text = await Bun.file(args.path).text();
      return {
        contents: `export default ${JSON.stringify(text)};`,
        loader: "js",
      };
    });
  },
};

export default myPlugin;
```

Bun will lazily resolve and load each plugin and use them to bundle your routes.

## Inline Environment Variables

Bun can replace `process.env.*` references in your frontend JavaScript and TypeScript with their actual values at build time. Configure the `env` option in your `bunfig.toml`:

bunfig.toml

```
[serve.static]
env = "PUBLIC_*"  # only inline env vars starting with PUBLIC_ (recommended)
# env = "inline"  # inline all environment variables
# env = "disable" # disable env var replacement (default)
```

See the [HTML & static sites documentation](https://bun.com/docs/bundler/html-static#inline-environment-variables) for more details on build-time configuration and examples.

## How It Works

Bun uses `HTMLRewriter` to scan for `<script>` and `<link>` tags in HTML files, uses them as entrypoints for Bun’s bundler, generates an optimized bundle for the JavaScript/TypeScript/TSX/JSX and CSS files, and serves the result.

### Processing Pipeline

1

2

3

4

5

## Complete Example

Here’s a complete fullstack application example:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { serve } from "bun";
import { Database } from "bun:sqlite";
import homepage from "./public/index.html";
import dashboard from "./public/dashboard.html";

// Initialize database
const db = new Database("app.db");
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);

const server = serve({
  routes: {
    // Frontend routes
    "/": homepage,
    "/dashboard": dashboard,

    // API routes
    "/api/users": {
      async GET() {
        const users = db.query("SELECT * FROM users").all();
        return Response.json(users);
      },

      async POST(req) {
        const { name, email } = await req.json();

        try {
          const result = db.query("INSERT INTO users (name, email) VALUES (?, ?) RETURNING *").get(name, email);

          return Response.json(result, { status: 201 });
        } catch (error) {
          return Response.json({ error: "Email already exists" }, { status: 400 });
        }
      },
    },

    "/api/users/:id": {
      async GET(req) {
        const { id } = req.params;
        const user = db.query("SELECT * FROM users WHERE id = ?").get(id);

        if (!user) {
          return Response.json({ error: "User not found" }, { status: 404 });
        }

        return Response.json(user);
      },

      async DELETE(req) {
        const { id } = req.params;
        const result = db.query("DELETE FROM users WHERE id = ?").run(id);

        if (result.changes === 0) {
          return Response.json({ error: "User not found" }, { status: 404 });
        }

        return new Response(null, { status: 204 });
      },
    },

    // Health check endpoint
    "/api/health": {
      GET() {
        return Response.json({
          status: "ok",
          timestamp: new Date().toISOString(),
        });
      },
    },
  },

  // Enable development mode
  development: {
    hmr: true,
    console: true,
  },

  // Fallback for unmatched routes
  fetch(req) {
    return new Response("Not Found", { status: 404 });
  },
});

console.log(`🚀 Server running on ${server.url}`);
```

public/index.html

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Fullstack Bun App</title>
    <link rel="stylesheet" href="../src/styles.css" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="../src/main.tsx"></script>
  </body>
</html>
```

src/main.tsx

```
import { createRoot } from "react-dom/client";
import { App } from "./App";

const container = document.getElementById("root")!;
const root = createRoot(container);
root.render(<App />);
```

src/App.tsx

```
import { useState, useEffect } from "react";

interface User {
  id: number;
  name: string;
  email: string;
  created_at: string;
}

export function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchUsers = async () => {
    const response = await fetch("/api/users");
    const data = await response.json();
    setUsers(data);
  };

  const createUser = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch("/api/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email }),
      });

      if (response.ok) {
        setName("");
        setEmail("");
        await fetchUsers();
      } else {
        const error = await response.json();
        alert(error.error);
      }
    } catch (error) {
      alert("Failed to create user");
    } finally {
      setLoading(false);
    }
  };

  const deleteUser = async (id: number) => {
    if (!confirm("Are you sure?")) return;

    try {
      const response = await fetch(`/api/users/${id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        await fetchUsers();
      }
    } catch (error) {
      alert("Failed to delete user");
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="container">
      <h1>User Management</h1>

      <form onSubmit={createUser} className="form">
        <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} required />
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required />
        <button type="submit" disabled={loading}>
          {loading ? "Creating..." : "Create User"}
        </button>
      </form>

      <div className="users">
        <h2>Users ({users.length})</h2>
        {users.map(user => (
          <div key={user.id} className="user-card">
            <div>
              <strong>{user.name}</strong>
              <br />
              <span>{user.email}</span>
            </div>
            <button onClick={() => deleteUser(user.id)} className="delete-btn">
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

src/styles.css

```
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  background: #f5f5f5;
  color: #333;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  color: #2563eb;
  margin-bottom: 2rem;
}

.form {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.form input {
  flex: 1;
  min-width: 200px;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form button {
  padding: 0.75rem 1.5rem;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.form button:hover {
  background: #1d4ed8;
}

.form button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.users {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.user-card:last-child {
  border-bottom: none;
}

.delete-btn {
  padding: 0.5rem 1rem;
  background: #dc2626;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn:hover {
  background: #b91c1c;
}
```

## Best Practices

### Project Structure

```
my-app/
├── src/
│   ├── components/
│   │   ├── Header.tsx
│   │   └── UserList.tsx
│   ├── styles/
│   │   ├── globals.css
│   │   └── components.css
│   ├── utils/
│   │   └── api.ts
│   ├── App.tsx
│   └── main.tsx
├── public/
│   ├── index.html
│   ├── dashboard.html
│   └── favicon.ico
├── server/
│   ├── routes/
│   │   ├── users.ts
│   │   └── auth.ts
│   ├── db/
│   │   └── schema.sql
│   └── index.ts
├── bunfig.toml
└── package.json
```

### Environment-Based Configuration

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server/config.ts

```
export const config = {
  development: process.env.NODE_ENV !== "production",
  port: process.env.PORT || 3000,
  database: {
    url: process.env.DATABASE_URL || "./dev.db",
  },
  cors: {
    origin: process.env.CORS_ORIGIN || "*",
  },
};
```

### Error Handling

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server/middleware.ts

```
export function errorHandler(error: Error, req: Request) {
  console.error("Server error:", error);

  if (process.env.NODE_ENV === "production") {
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }

  return Response.json(
    {
      error: error.message,
      stack: error.stack,
    },
    { status: 500 },
  );
}
```

### API Response Helpers

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server/utils.ts

```
export function json(data: any, status = 200) {
  return Response.json(data, { status });
}

export function error(message: string, status = 400) {
  return Response.json({ error: message }, { status });
}

export function notFound(message = "Not found") {
  return error(message, 404);
}

export function unauthorized(message = "Unauthorized") {
  return error(message, 401);
}
```

### Type Safety

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)types/api.ts

```
export interface User {
  id: number;
  name: string;
  email: string;
  created_at: string;
}

export interface CreateUserRequest {
  name: string;
  email: string;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
}
```

## Deployment

### Production Build

terminal

```
# Build for production
bun build --target=bun --production --outdir=dist ./server/index.ts

# Run production server
NODE_ENV=production bun dist/index.js
```

### Docker Deployment

Dockerfile

```
FROM oven/bun:1 as base
WORKDIR /usr/src/app

# Install dependencies
COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile

# Copy source code
COPY . .

# Build application
RUN bun build --target=bun --production --outdir=dist ./server/index.ts

# Production stage
FROM oven/bun:1-slim
WORKDIR /usr/src/app
COPY --from=base /usr/src/app/dist ./
COPY --from=base /usr/src/app/public ./public

EXPOSE 3000
CMD ["bun", "index.js"]
```

### Environment Variables

.env.production

```
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost:5432/myapp
CORS_ORIGIN=https://myapp.com
```

## Migration from Other Frameworks

### From Express + Webpack

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
// Before (Express + Webpack)
app.use(express.static("dist"));
app.get("/api/users", (req, res) => {
  res.json(users);
});

// After (Bun fullstack)
serve({
  routes: {
    "/": homepage, // Replaces express.static
    "/api/users": {
      GET() {
        return Response.json(users);
      },
    },
  },
});
```

### From Next.js API Routes

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
// Before (Next.js)
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.json(users);
  }
}

// After (Bun)
"/api/users": {
  GET() { return Response.json(users); }
}
```

## Limitations and Future Plans

### Current Limitations

*   `bun build` CLI integration is not yet available for fullstack apps
*   Auto-discovery of API routes is not implemented
*   Server-side rendering (SSR) is not built-in

### Planned Features

*   Integration with `bun build` CLI
*   File-based routing for API endpoints
*   Built-in SSR support
*   Enhanced plugin ecosystem
