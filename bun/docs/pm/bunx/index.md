---
title: "bunx"
source: "https://bun.com/docs/pm/bunx"
canonical_url: "https://bun.com/docs/pm/bunx"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:03.052Z"
content_hash: "cc110fa0cd70f96f352b068fab205abdec52bd823e8b3ed3829f94dc0f9ddc59"
menu_path: ["bunx"]
section_path: []
nav_prev: {"path": "../../guides/write-file/unlink/index.md", "title": "Delete a file"}
nav_next: {"path": "../catalogs/index.md", "title": "Catalogs"}
---

# Run Prisma migrations
bunx prisma migrate

# Format a file with Prettier
bunx prettier foo.js

# Run a specific version of a package
bunx uglify-js@3.14.0 app.js

# Use --package when binary name differs from package name
bunx -p @angular/cli ng new my-app

# Force running with Bun instead of Node.js, even if the executable contains a Node shebang
bunx --bun vite dev foo.js
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/bunx.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/bunx>)

[

bun update

Previous

](/docs/pm/cli/update)[

bun publish

Next

](/docs/pm/cli/publish)
