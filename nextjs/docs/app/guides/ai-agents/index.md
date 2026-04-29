---
title: "How to set up your Next.js project for AI coding agents"
source: "https://nextjs.org/docs/app/guides/ai-agents"
canonical_url: "https://nextjs.org/docs/app/guides/ai-agents"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:12:45.330Z"
content_hash: "16334c1e335edcc9b146a8985439c8156895c0c4fc620531da6202e7c9e03ae4"
menu_path: ["How to set up your Next.js project for AI coding agents"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/index.md", "title": "Guides"}
nav_next: {"path": "nextjs/docs/app/guides/analytics/index.md", "title": "How to add analytics to your Next.js application"}
---

# How to set up your Next.js project for AI coding agents

Last updated April 23, 2026

Next.js ships version-matched documentation inside the `next` package, allowing AI coding agents to reference accurate, up-to-date APIs and patterns. An `AGENTS.md` file at the root of your project directs agents to these bundled docs instead of their training data.

## How it works[](#how-it-works)

When you install `next`, the Next.js documentation is bundled at `node_modules/next/dist/docs/`. The bundled docs mirror the structure of the [Next.js documentation site](../../../index.md):

```
node_modules/next/dist/docs/
├── 01-app/
│   ├── 01-getting-started/
│   ├── 02-guides/
│   └── 03-api-reference/
├── 02-pages/
├── 03-architecture/
└── index.mdx
```

This means agents always have access to docs that match your installed version — no network request or external lookup required.

The `AGENTS.md` file at the root of your project tells agents to read these bundled docs before writing any code. Most AI coding agents — including Claude Code, Cursor, GitHub Copilot, and others — automatically read `AGENTS.md` when they start a session.

## Getting started[](#getting-started)

### New projects[](#new-projects)

[`create-next-app`](../../api-reference/cli/create-next-app/index.md) generates `AGENTS.md` and `CLAUDE.md` automatically. No additional setup is needed:

#### pnpm

pnpm

#### npm

npm

#### yarn

yarn

#### bun

bun

Terminal

```
pnpm create next-app@canary
```

If you don't want the agent files, pass `--no-agents-md`:

```
npx create-next-app@canary --no-agents-md
```

### Existing projects[](#existing-projects)

Ensure you are on Next.js `v16.2.0-canary.37` or later, then add the following files to the root of your project.

`AGENTS.md` contains the instructions that agents will read:

AGENTS.md

```
<!-- BEGIN:nextjs-agent-rules -->
 
# Next.js: ALWAYS read docs before coding
 
Before any Next.js work, find and read the relevant doc in `node_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.
 
<!-- END:nextjs-agent-rules -->
```

`CLAUDE.md` uses the `@` import syntax to include `AGENTS.md`, so [Claude Code](https://docs.anthropic.com/en/docs/claude-code) users get the same instructions without duplicating content:

CLAUDE.md

```
@AGENTS.md
```

**For earlier versions**

On version 16.1 and earlier, use the codemod to generate these files automatically:

```
npx @next/codemod@latest agents-md
```

The codemod outputs the bundled docs to `.next-docs/` in the project root instead of `node_modules/next/dist/docs/`, and the generated agent files will point to that directory.

## Understanding AGENTS.md[](#understanding-agentsmd)

The default `AGENTS.md` contains a single, focused instruction: **read the bundled docs before writing code**. This is intentionally minimal — the goal is to redirect agents from stale training data to the accurate, version-matched documentation in `node_modules/next/dist/docs/`.

The `<!-- BEGIN:nextjs-agent-rules -->` and `<!-- END:nextjs-agent-rules -->` comment markers delimit the Next.js-managed section. You can add your own project-specific instructions outside these markers without worrying about them being overwritten by future updates.

The bundled docs include guides, API references, and file conventions for the App Router and Pages Router. When an agent encounters a task involving routing, data fetching, or any other Next.js feature, it can look up the correct API in the bundled docs rather than relying on potentially outdated training data.

> **Good to know:** To see how bundled docs and `AGENTS.md` improve agent performance on real-world Next.js tasks, visit the [benchmark results](https://nextjs.org/evals).

## Next Steps

[

### Next.js MCP Server

Learn how to use Next.js MCP support to allow coding agents access to your application state

](../mcp/index.md)

Was this helpful?
