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
nav_prev: {"path": "bun/bun/docs/bundler/executables/index.md", "title": "Single-file executable"}
nav_next: {"path": "bun/bun/docs/bundler/hot-reloading/index.md", "title": "Hot reloading"}
---

# env = "inline"  # inline all environment variables
# env = "disable" # disable env var replacement (default)
```

See the [HTML & static sites documentation](bun/bun/docs/bundler/html-static/index.md#inline-environment-variables) for more details on build-time configuration and examples.

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
