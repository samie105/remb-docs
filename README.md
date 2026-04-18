# remb-docs

Clean, AI-agent-friendly markdown harvest of developer documentation.

Each top-level directory is one source — fully crawled, normalized to markdown, with a `manifest.json` (crawl metadata) and `toc.json` (table of contents).

## Sources

| Source | Pages | Path |
|--------|-------|------|
| Next.js | 400 | [`nextjs/`](./nextjs) |

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
- Offline reference for Next.js / React / Vite / etc.

## Adding more sources

Crawled with [remb-docs harvester](https://github.com/legendcodingkiller/remb-docs) (private repo for the crawler). New sources land here as `<name>/` directories.
