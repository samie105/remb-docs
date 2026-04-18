---
title: "Further Reading"
source: "https://trpc.io/docs/v10/further-reading"
canonical_url: "https://trpc.io/docs/v10/further-reading"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:04.199Z"
content_hash: "5d006e77c90cf420c10f68ae287dc23691aff731eb3005498cc9bd92f1d4b551"
menu_path: ["Further Reading"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/further/index.md", "title": "Extra Information"}
nav_next: {"path": "trpc/docs/v10/getting-started/index.md", "title": "Getting Started"}
---

## Who is this for?[​](#who-is-this-for "Direct link to Who is this for?")

*   tRPC is for full-stack typescripters. It makes it dead easy to write "endpoints", which you can safely use in your app.
*   It's designed for monorepos, as you need to export/import the type definitions from/to your server.
*   If you already work in a team where languages are mixed or have third-party consumers over whom you have no control, you should create a language-agnostic [GraphQL](https://graphql.org/)\-API.

## Relationship to GraphQL[​](#relationship-to-graphql "Direct link to Relationship to GraphQL")

If you already have a custom GraphQL-server for your project, you may not want to use tRPC. GraphQL is amazing; it's great to be able to make a flexible API where each consumer can pick just the data they need.

The thing is, GraphQL isn't that easy to get right - [ACL](https://en.wikipedia.org/wiki/Access-control_list) is needed to be solved on a per-type basis, complexity analysis, and performance are all non-trivial things.

We've taken a lot of inspiration from GraphQL. If you've previously built GraphQL servers, you'll be familiar with the concepts of input types and resolvers.

tRPC is a lot simpler and couples your server & website/app more tightly together (for good and for bad). It allows you to move quickly, make changes without having to update a schema, and avoid thinking about the ever-traversable graph.

