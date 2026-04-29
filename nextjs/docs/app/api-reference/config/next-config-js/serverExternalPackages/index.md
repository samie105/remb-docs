---
title: "serverExternalPackages"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:07:25.181Z"
content_hash: "961fee0316f84f539c58bb0ac2675e57ebcb3e6e404abeaf7be05a5847427585"
menu_path: ["serverExternalPackages"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache/index.md", "title": "serverComponentsHmrCache"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/staleTimes/index.md", "title": "staleTimes"}
---

# serverExternalPackages

Last updated April 23, 2026

Dependencies used inside [Server Components](../../../../getting-started/server-and-client-components/index.md) and [Route Handlers](../../../file-conventions/route/index.md) will automatically be bundled by Next.js.

If a dependency is using Node.js specific features, you can choose to opt-out specific dependencies from the Server Components bundling and use native Node.js `require`.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}
 
module.exports = nextConfig
```

Next.js includes a [short list of popular packages](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.jsonc) that currently are working on compatibility and automatically opt-ed out:

-   `@alinea/generated`
-   `@appsignal/nodejs`
-   `@aws-sdk/client-s3`
-   `@aws-sdk/s3-presigned-post`
-   `@blockfrost/blockfrost-js`
-   `@highlight-run/node`
-   `@huggingface/transformers`
-   `@jpg-store/lucid-cardano`
-   `@libsql/client`
-   `@mikro-orm/core`
-   `@mikro-orm/knex`
-   `@node-rs/argon2`
-   `@node-rs/bcrypt`
-   `@prisma/client`
-   `@react-pdf/renderer`
-   `@sentry/profiling-node`
-   `@sparticuz/chromium`
-   `@sparticuz/chromium-min`
-   `@statsig/statsig-node-core`
-   `@swc/core`
-   `@xenova/transformers`
-   `@zenstackhq/runtime`
-   `argon2`
-   `autoprefixer`
-   `aws-crt`
-   `bcrypt`
-   `better-sqlite3`
-   `canvas`
-   `chromadb-default-embed`
-   `config`
-   `cpu-features`
-   `cypress`
-   `dd-trace`
-   `eslint`
-   `express`
-   `firebase-admin`
-   `htmlrewriter`
-   `import-in-the-middle`
-   `isolated-vm`
-   `jest`
-   `jsdom`
-   `keyv`
-   `libsql`
-   `mdx-bundler`
-   `mongodb`
-   `mongoose`
-   `newrelic`
-   `next-mdx-remote`
-   `next-seo`
-   `node-cron`
-   `node-pty`
-   `node-web-audio-api`
-   `onnxruntime-node`
-   `oslo`
-   `pg`
-   `pino`
-   `pino-pretty`
-   `pino-roll`
-   `playwright`
-   `playwright-core`
-   `postcss`
-   `prettier`
-   `prisma`
-   `puppeteer-core`
-   `puppeteer`
-   `ravendb`
-   `require-in-the-middle`
-   `rimraf`
-   `sharp`
-   `shiki`
-   `sqlite3`
-   `thread-stream`
-   `ts-morph`
-   `ts-node`
-   `typescript`
-   `vscode-oniguruma`
-   `webpack`
-   `websocket`
-   `zeromq`

| Version | Changes |
| --- | --- |
| `v15.0.0` | Moved from experimental to stable. Renamed from `serverComponentsExternalPackages` to `serverExternalPackages` |

Was this helpful?
