# remb-docs

Clean, markdown-formatted snapshots of developer documentation. Crawled, extracted, and normalized for use with AI tools, search indexes, and offline reference.

Each top-level directory is one source — fully crawled with a `manifest.json` (crawl metadata) and `toc.json` (navigation structure). Every page is a standalone markdown file with YAML frontmatter.

## Sources

| Source | Pages | Path |
|--------|-------|------|
| Next.js | 400 | [`nextjs/`](./nextjs) |
| PostgreSQL | 498 | [`postgres/`](./postgres) |
| Supabase | 499 | [`supabase/`](./supabase) |
| Astro | 385 | [`astro/`](./astro) |
| Redis | 400 | [`redis/`](./redis) |
| Bun | 312 | [`bun/`](./bun) |
| Drizzle ORM | 247 | [`drizzle/`](./drizzle) |
| tRPC | 250 | [`trpc/`](./trpc) |
| Deno | 225 | [`deno/`](./deno) |
| Tailwind CSS | 194 | [`tailwind/`](./tailwind) |
| Prisma | 140 | [`prisma/`](./prisma) |
| Svelte | 84 | [`svelte/`](./svelte) |
| Hono | 82 | [`hono/`](./hono) |
| React | 51 | [`react/`](./react) |
| Fastify | 42 | [`fastify/`](./fastify) |
| Vite | 38 | [`vite/`](./vite) |

**Total: 3,847 pages across 16 sources**

## File format

Each page is saved at `<source>/docs/<url-path>/index.md` with frontmatter:

```yaml
---
title: "Page Title"
source: "https://original-url.com/docs/page"
canonical_url: "https://original-url.com/docs/page"
docset: "nextjs"
last_crawled_at: "2026-04-18T16:00:00.000Z"
content_hash: "sha256..."
---
```

## Use cases

- Feed docs into an AI assistant as context
- Build a local search index (e.g. with Pagefind or Lunr)
- Diff documentation between crawl dates to track API changes
- Offline reference when working without internet

## Structure

```
<source>/
  docs/             # URL hierarchy mirrored as .md files
  SKILL.md          # structured guide for AI context loading
  manifest.json     # crawl metadata (page count, dates, source URL)
  toc.json          # table of contents / navigation tree
  llms.txt          # flat index for LLM context injection
```
