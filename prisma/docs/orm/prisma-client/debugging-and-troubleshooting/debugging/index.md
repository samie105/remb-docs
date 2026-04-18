---
title: "Debugging"
source: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:28.695Z"
content_hash: "6791935c78e247069cc2ee87e8f13a181f0482159894797873c994c2e2929758"
menu_path: ["Debugging"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/client-extensions/query/index.md", "title": "Create custom Prisma Client queries"}
nav_next: {"path": "prisma/docs/orm/prisma-client/debugging-and-troubleshooting/handling-exceptions-and-errors/index.md", "title": "Handling exceptions and errors"}
---

# enable only `prisma:engine`-level debugging output
export DEBUG="prisma:engine"

# enable only `prisma:client`-level debugging output
export DEBUG="prisma:client"

# enable both `prisma-client`- and `engine`-level debugging output
export DEBUG="prisma:client,prisma:engine"
```

To enable all `prisma` debugging options, set `DEBUG` to `prisma*`:

```
export DEBUG="prisma*"
```

On Windows, use `set` instead of `export`:

```
set DEBUG="prisma*"
```

To enable _all_ debugging options, set `DEBUG` to `*`:

```
export DEBUG="*"
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/debugging-and-troubleshooting/debugging.mdx)


