---
title: "Bundler issues"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/bundler-issues"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/bundler-issues"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:12.664Z"
content_hash: "31c5419181eda0753cfb3087922e651f14a25f88417f5cd0d3ca8bddf12420f2"
menu_path: ["Bundler issues"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/dev-environment/environment-variables/index.md", "title": "Environment variables"}
nav_next: {"path": "prisma/docs/orm/more/troubleshooting/check-constraints/index.md", "title": "Check constraints"}
---

Troubleshooting

Solve ENOENT package error with vercel/pkg and other bundlers

If you use [vercel/pkg](https://github.com/vercel/pkg) to package your Node.js project, you might encounter an `ENOENT` error like:

```
spawn /snapshot/enoent-problem/node_modules/.prisma/client/query-engine-debian-openssl-1.1.x ENOENT
```

Add your Prisma query engine binary path to the `pkg/assets` section of your `package.json` file:

```
{
  "pkg": {
    "assets": ["node_modules/.prisma/client/*.node"]
  }
}
```

See [this Github issue](https://github.com/prisma/prisma/issues/8449) for further discussion.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/more/troubleshooting/bundler-issues.mdx)

