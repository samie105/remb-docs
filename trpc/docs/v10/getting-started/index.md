---
title: "Getting Started"
source: "https://trpc.io/docs/v10/getting-started"
canonical_url: "https://trpc.io/docs/v10/getting-started"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:09.530Z"
content_hash: "6abfdd40e8654edfcca7879fda9000c7441737a5084efcb1267d33901c30de83"
menu_path: ["Getting Started"]
section_path: []
nav_prev: {"path": "../further-reading/index.md", "title": "Further Reading"}
nav_next: {"path": "../landing-intro/Step1/index.md", "title": "Step1"}
---

## A quick look at tRPC[​](#a-quick-look-at-trpc "Direct link to A quick look at tRPC")

For a quick video overview of tRPC's concepts, check out the videos below:

*   [tRPC in 100 seconds](https://www.youtube.com/watch?v=0DyAyLdVW0I)
*   [tRPC in 5 minutes](https://www.youtube.com/watch?v=S6rcrkbsDI0)
*   [tRPC in 15 minutes](https://www.youtube.com/watch?v=2LYM8gf184U)

## Give tRPC a try[​](#give-trpc-a-try "Direct link to Give tRPC a try")

The fastest way to try tRPC is in an online REPL. Here are some options you can try out:

*   [Minimal Example](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal?file=server%2Findex.ts&file=client%2Findex.ts&view=editor) - a minimal Node.js http server, and a client that calls a function on the server and logs the request to the console.
*   [Minimal Next.js Example](https://stackblitz.com/github/trpc/trpc/tree/main/examples/next-minimal-starter?file=src%2Fpages%2Fapi%2Ftrpc%2F%5Btrpc%5D.ts&file=src%2Fpages%2Findex.tsx) - the smallest possible Next.js app that uses tRPC. It has a single endpoint that returns a string, and a page that calls that endpoint and displays the result.

If you prefer to get started in your local environment, you can use one of our [example apps](../example-apps/index.md) as a starter project that you can experiment with locally.

## Use tRPC[​](#use-trpc "Direct link to Use tRPC")

"Using tRPC" means different things to different people. The goal of this page is to guide you to the right resources based on your goals.

### Becoming productive in an existing tRPC project[​](#becoming-productive-in-an-existing-trpc-project "Direct link to Becoming productive in an existing tRPC project")

*   Read the [concepts](../concepts/index.md) page.
*   Become familiar with [routers](../server/routers/index.md), [procedures](../server/procedures/index.md), [context](../server/context/index.md), and [middleware](../server/middlewares/index.md).
*   If you are using React, read about [useQuery](../client/react/useQuery/index.md), [useMutation](../client/react/useMutation/index.md) and [useUtils](../client/react/useUtils/index.md).

### Creating a new project[​](#creating-a-new-project "Direct link to Creating a new project")

Since tRPC can live inside of many different frameworks, you will first need to decide where you want to use it.

On the backend, there are [adapters](../server/adapters/index.md) for a range of frameworks as well as vanilla Node.js. On the frontend, you can use our [React](../client/react/index.md) or [Next.js](../client/nextjs/index.md) integrations, a [third-party integration](../community/awesome-trpc/index.md#frontend-frameworks) for a variety of other frameworks, or the [Vanilla Client](../client/vanilla/setup/index.md), which works anywhere JavaScript runs.

After choosing your stack, you can either scaffold your app using a [template](../example-apps/index.md), or start from scratch using the documentation for your chosen backend and frontend integration.

### Adding tRPC to an existing project[​](#adding-trpc-to-an-existing-project "Direct link to Adding tRPC to an existing project")

Adding tRPC to an existing project is not significantly different from starting a new project, so the same resources apply. The main challenge is that it can feel difficult to know how to integrate tRPC with your existing application. Here are some tips:

*   You don't need to port all of your existing backend logic to tRPC. A common migration strategy is to initally only use tRPC for new endpoints, and only later migrate existing endpoints to tRPC.
*   If you're not sure where to start, check the documentation for your backend [adapter](../server/adapters/index.md) and frontend implementation, as well as the [example apps](../example-apps/index.md).
*   If you are looking for some inspiration of how tRPC might look as part of a larger codebase, there are some examples in [Open-source projects using tRPC](../community/awesome-trpc/index.md#-open-source-projects-using-trpc).

Join us in the [tRPC Discord](https://trpc.io/discord) to share your experiences, ask questions, and get help from the community!
