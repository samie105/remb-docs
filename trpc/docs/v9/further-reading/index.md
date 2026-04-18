---
title: "Further Reading"
source: "https://trpc.io/docs/v9/further-reading"
canonical_url: "https://trpc.io/docs/v9/further-reading"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:06.508Z"
content_hash: "a84a8ebd7c387e495dcbcdbdbec477ea16e7929ec2fe6e453b0a1b91655f62d8"
menu_path: ["Further Reading"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/header/index.md", "title": "Custom header"}
nav_next: {"path": "trpc/docs/v9/infer-types/index.md", "title": "Inferring Types"}
---

## Who is this for?[​](#who-is-this-for "Direct link to Who is this for?")

*   tRPC is for full-stack javascripters. It makes it dead easy to write "endpoints" which you safely use in your app.
*   It's designed for monorepos as you need to export/import the type definitions from/to your server.
*   If you're already in a team where you're mixing languages or have third party consumers that you have no control of, you're better off with making a [GraphQL](https://graphql.org/)\-API which is language-agnostic.

## Relationship to GraphQL[​](#relationship-to-graphql "Direct link to Relationship to GraphQL")

If you already have a custom GraphQL-server for your project, you may not want to use tRPC. GraphQL is amazing; it's great to be able to make a flexible API where each consumer can pick just the data they need.

The thing is, GraphQL isn't that easy to get right - [ACL](https://en.wikipedia.org/wiki/Access-control_list) is needed to be solved on a per-type basis, complexity analysis, and performance are all non-trivial things.

We've taken a lot of inspiration from GraphQL. If you've made GraphQL-servers before, you'll be familiar with the concept of input types and resolvers.

tRPC is a lot simpler and couples your server & website/app more tightly together (for good and for bad). It makes it easy to move quickly, do changes without updating a schema & there's no thinking about the ever-traversable graph.
