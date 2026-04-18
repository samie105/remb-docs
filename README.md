# remb-docs

Clean, AI-agent-friendly markdown harvest of developer documentation.

Each top-level directory is one source — fully crawled, normalized to markdown, with a `manifest.json` (crawl metadata) and `toc.json` (table of contents).

## Sources

| Source | Pages | Path |
|--------|-------|------|
| Next.js | 401 | [`nextjs/`](./nextjs) |
| PostgreSQL | 498 | [`postgres/`](./postgres) |
| Supabase | 500 | [`supabase/`](./supabase) |
| Astro | 385 | [`astro/`](./astro) |
| Redis | 400 | [`redis/`](./redis) |
| Bun | 312 | [`bun/`](./bun) |
| Drizzle ORM | 247 | [`drizzle/`](./drizzle) |
| tRPC | 250 | [`trpc/`](./trpc) |
| Deno | 226 | [`deno/`](./deno) |
| Tailwind CSS | 194 | [`tailwind/`](./tailwind) |
| Prisma | 140 | [`prisma/`](./prisma) |
| Hono | 82 | [`hono/`](./hono) |
| Svelte | 84 | [`svelte/`](./svelte) |
| React | 51 | [`react/`](./react) |
| Fastify | 42 | [`fastify/`](./fastify) |
| Vite | 38 | [`vite/`](./vite) |

**Total: 3,850 pages across 16 sources**

## Layout

```
<source>/
  docs/             # mirrored URL hierarchy as .md files
  manifest.json     # source URL, crawl date, page count
  toc.json          # navigation structure
```

## Use cases

- Build a doc-search UI on top of these markdown trees
- Feed into RAG / agent skill files for AI-driven dev tooling
- Offline reference for popular JS/TS ecosystem tools

## Adding more sources

Crawled with [remb-docs harvester](https://github.com/legendcodingkiller/remb-docs) (private repo for the crawler). New sources land here as `<name>/` directories.
