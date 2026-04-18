---
title: "API patterns"
source: "https://www.prisma.io/docs/orm/core-concepts/api-patterns"
canonical_url: "https://www.prisma.io/docs/orm/core-concepts/api-patterns"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:07.080Z"
content_hash: "73f6e181716aa3f1502a0e6cb97159290966003fe06139424ea0a22ffb2d8743"
menu_path: ["API patterns"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/core-concepts/data-modeling/index.md", "title": "Data modeling"}
nav_next: {"path": "prisma/docs/orm/prisma-schema/introspection/index.md", "title": "What is introspection?"}
---

How to use Prisma ORM with REST APIs, GraphQL servers, and fullstack frameworks

Prisma Client can be used to query your database from any server-side JavaScript or TypeScript application. This page covers common patterns for REST APIs, GraphQL servers, and fullstack frameworks.

When building REST APIs, use Prisma Client inside your route controllers to execute database queries.

### [Supported frameworks](#supported-frameworks)

*   [Express](https://expressjs.com/)
*   [Fastify](https://fastify.dev/)
*   [hapi](https://hapi.dev/)
*   [koa](https://koajs.com/)
*   [NestJS](https://nestjs.com/)
*   [Next.js API Routes](https://nextjs.org/)

### [Example routes](#example-routes)

```
// GET /feed - fetch published posts
app.get("/feed", async (req, res) => {
  const posts = await prisma.post.findMany({
    where: { published: true },
    include: { author: true },
  });
  res.json(posts);
});

// POST /post - create a post
app.post("/post", async (req, res) => {
  const { title, content, authorEmail } = req.body;
  const result = await prisma.post.create({
    data: {
      title,
      content,
      author: { connect: { email: authorEmail } },
    },
  });
  res.json(result);
});

// PUT /publish/:id - publish a post
app.put("/publish/:id", async (req, res) => {
  const post = await prisma.post.update({
    where: { id: Number(req.params.id) },
    data: { published: true },
  });
  res.json(post);
});

// DELETE /post/:id - delete a post
app.delete("/post/:id", async (req, res) => {
  const post = await prisma.post.delete({
    where: { id: Number(req.params.id) },
  });
  res.json(post);
});
```

Prisma ORM works with any GraphQL library. Use Prisma Client inside your resolvers to read and write data.

### [Supported tools](#supported-tools)

Library

Purpose

`graphql-yoga`

HTTP server

`apollo-server`

HTTP server

`pothos`

Schema builder

`nexus`

Schema builder

`type-graphql`

Schema builder

### [Framework integrations](#framework-integrations)

*   [Redwood.js](https://rwsdk.com/) - Built on Prisma ORM

### [Prisma's role](#prismas-role)

Prisma ORM is used inside GraphQL resolvers the same way you'd use any other ORM:

*   **Queries**: Read data from the database to return in the response
*   **Mutations**: Write data to the database (create, update, delete)

Modern fullstack frameworks blur server/client boundaries. Use Prisma Client in the server-side portion of your application.

### [Supported frameworks](#supported-frameworks-1)

*   [Next.js](https://nextjs.org/)
*   [Remix](https://remix.run/)
*   [SvelteKit](https://svelte.dev/)
*   [Nuxt](https://nuxt.com/)
*   [Redwood](https://rwsdk.com/)
*   [Wasp](https://wasp-lang.dev/)

### [Supported runtimes](#supported-runtimes)

*   [Node.js](https://nodejs.org/)
*   [Bun](https://bun.sh/)
*   [Deno](https://deno.com/)

### [Next.js example](#nextjs-example)

```
// In getServerSideProps or API routes
export const getServerSideProps = async () => {
  const feed = await prisma.post.findMany({
    where: { published: true },
  });
  return { props: { feed } };
};
```

Find ready-to-run examples in the [`prisma-examples`](https://github.com/prisma/prisma-examples/) repository:

Example

Type

Description

[Next.js](https://pris.ly/e/orm/nextjs)

Fullstack

Next.js 15 app

[Express](https://pris.ly/e/ts/rest-express)

REST

Express REST API

[Fastify](https://pris.ly/e/ts/rest-fastify)

REST

Fastify REST API

[GraphQL Yoga](https://pris.ly/e/ts/graphql)

GraphQL

GraphQL server with Pothos

[NestJS](https://pris.ly/e/ts/rest-nestjs)

REST

NestJS REST API

[Remix](https://pris.ly/e/ts/remix)

Fullstack

Remix with actions and loaders

[SvelteKit](https://pris.ly/e/ts/sveltekit)

Fullstack

SvelteKit app

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/core-concepts/api-patterns.mdx)


