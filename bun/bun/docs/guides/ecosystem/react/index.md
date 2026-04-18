---
title: "Build a React app with Bun"
source: "https://bun.com/docs/guides/ecosystem/react"
canonical_url: "https://bun.com/docs/guides/ecosystem/react"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:46.563Z"
content_hash: "05b5fbaed564016a81e411bc75cc4ec04911c43518f745448d4c5b1eddccb558"
menu_path: ["Build a React app with Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/qwik/index.md", "title": "Build an app with Qwik and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/prisma-postgres/index.md", "title": "Use Prisma Postgres with Bun"}
---

# Create a new React app
bun init --react

# Run the app in development mode
bun dev

# Build as a static site for production
bun run build

# Run the server in production
bun start
```

* * *

### Hot Reloading

Run `bun dev` to start the app in development mode. This will start the API server and the React app with hot reloading.

### Full-Stack App

Run `bun start` to start the API server and frontend together in one process.

### Static Site

Run `bun run build` to build the app as a static site. This will create a `dist` directory with the built app and all the assets.

File Tree

```
├── src/
│   ├── index.tsx       # Server entry point with API routes
│   ├── frontend.tsx    # React app entry point with HMR
│   ├── App.tsx         # Main React component
│   ├── APITester.tsx   # Component for testing API endpoints
│   ├── index.html      # HTML template
│   ├── index.css       # Styles
│   └── *.svg           # Static assets
├── package.json        # Dependencies and scripts
├── tsconfig.json       # TypeScript configuration
├── bunfig.toml         # Bun configuration
└── bun.lock            # Lock file
```
