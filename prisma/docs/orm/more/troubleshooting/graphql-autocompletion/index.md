---
title: "GraphQL autocompletion"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/graphql-autocompletion"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/graphql-autocompletion"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:40.629Z"
content_hash: "1bf6d04816ce24225951a3b31654e9c4b6bab8be545b57c760ee724398e8ff2c"
menu_path: ["GraphQL autocompletion"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/more/troubleshooting/check-constraints/index.md", "title": "Check constraints"}
nav_next: {"path": "prisma/docs/orm/more/troubleshooting/many-to-many-relations/index.md", "title": "Many-to-many relations"}
---

Troubleshooting

Get autocompletion for Prisma Client queries in GraphQL resolvers with plain JavaScript

When using GraphQL with TypeScript, you get autocompletion for the Prisma Client instance in your GraphQL resolvers because the `context` object can be typed. In plain JavaScript, this needs a little more effort.

In a resolver like this:

```
filterPosts: (parent, args, ctx) => {
  return ctx.prisma.post.findMany({
    where: {
      OR: [
        { title: { contains: args.searchString } },
        { content: { contains: args.searchString } },
      ],
    },
  });
};
```

VS Code doesn't know the type of the `context` object so it can't provide any intellisense.

Add a [JSDoc](https://jsdoc.app/) comment named `typedef` to "import" the correct type:

```
// Add this to the top of the file
/**
 * @typedef { import("../prisma/generated/client").PrismaClient } Prisma
 */
```

Then type your resolver arguments:

```
/**
 * @param {any} parent
 * @param {{ searchString: string }} args
 * @param {{ prisma: Prisma }} ctx
 */
filterPosts: (parent, args, ctx) => {
  return ctx.prisma.post.findMany({
    where: {
      OR: [
        { title: { contains: args.searchString } },
        { content: { contains: args.searchString } },
      ],
    },
  });
};
```

This tells VS Code that `context` has a property named `prisma` with type `Prisma`, enabling autocompletion.

```
/**
 * @typedef { import("../prisma/generated/client").PrismaClient } Prisma
 * @typedef { import("../prisma/generated/client").UserCreateArgs } UserCreateArgs
 */

const { makeExecutableSchema } = require("graphql-tools");

const resolvers = {
  Query: {
    /**
     * @param {any} parent
     * @param {any} args
     * @param {{ prisma: Prisma }} ctx
     */
    feed: (parent, args, ctx) => {
      return ctx.prisma.post.findMany({
        where: { published: true },
      });
    },
    /**
     * @param {any} parent
     * @param {{ searchString: string }} args
     * @param {{ prisma: Prisma }} ctx
     */
    filterPosts: (parent, args, ctx) => {
      return ctx.prisma.post.findMany({
        where: {
          OR: [
            { title: { contains: args.searchString } },
            { content: { contains: args.searchString } },
          ],
        },
      });
    },
  },
};
```
