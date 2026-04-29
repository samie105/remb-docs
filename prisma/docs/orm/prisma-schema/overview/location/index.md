---
title: "Schema location"
source: "https://www.prisma.io/docs/orm/prisma-schema/overview/location"
canonical_url: "https://www.prisma.io/docs/orm/prisma-schema/overview/location"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:42:52.659Z"
content_hash: "207d193a30fd320de7e8e1403e04e54dbf6284562d94a57b7d22840b164ada93"
menu_path: ["Schema location"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-schema/overview/generators/index.md", "title": "Generators"}
---

# All files must be inside the `prisma/` directory
# `migrations` and `schema.prisma` must be at the same level
prisma/
├── migrations
├── models
│   ├── posts.prisma
│   └── users.prisma
└── schema.prisma  # Contains generator block
```

### [Tips for multi-file Prisma Schema](#tips-for-multi-file-prisma-schema)

We've found that a few patterns work well with this feature and will help you get the most out of it:

-   Organize your files by domain: group related models into the same file. For example, keep all user-related models in `user.prisma` while post-related models go in `post.prisma`.
-   Use clear naming conventions: schema files should be named clearly and succinctly. Use names like `user.prisma` and `post.prisma` and not `myModels.prisma` or `CommentFeaturesSchema.prisma`.
-   Have an obvious "main" schema file: while you can now have as many schema files as you want, you'll still need a place where you define your `generator` block. We recommend having a single schema file that's obviously the "main" file so that this block is easy to find. `main.prisma`, `schema.prisma`, and `base.prisma` are a few we've seen that work well.
