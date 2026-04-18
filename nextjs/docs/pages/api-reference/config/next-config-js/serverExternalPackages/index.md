---
title: "serverExternalPackages"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:21:26.378Z"
content_hash: "ccab416023ea9a7f87c394bc980c1516de066e646b6796783d654db4bf4dfbc2"
menu_path: ["serverExternalPackages"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/rewrites/index.md", "title": "rewrites"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/trailingSlash/index.md", "title": "trailingSlash"}
---

# serverExternalPackages

Last updated April 15, 2026

Opt-out specific dependencies from being included in the automatic bundling of the [`bundlePagesRouterDependencies`](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies) option.

These pages will then use native Node.js `require` to resolve the dependency.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}
 
module.exports = nextConfig
```

Next.js includes a [short list of popular packages](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.jsonc) that currently are working on compatibility and automatically opt-ed out:

*   `@alinea/generated`
*   `@appsignal/nodejs`
*   `@aws-sdk/client-s3`
*   `@aws-sdk/s3-presigned-post`
*   `@blockfrost/blockfrost-js`
*   `@highlight-run/node`
*   `@huggingface/transformers`
*   `@jpg-store/lucid-cardano`
*   `@libsql/client`
*   `@mikro-orm/core`
*   `@mikro-orm/knex`
*   `@node-rs/argon2`
*   `@node-rs/bcrypt`
*   `@prisma/client`
*   `@react-pdf/renderer`
*   `@sentry/profiling-node`
*   `@sparticuz/chromium`
*   `@sparticuz/chromium-min`
*   `@statsig/statsig-node-core`
*   `@swc/core`
*   `@xenova/transformers`
*   `@zenstackhq/runtime`
*   `argon2`
*   `autoprefixer`
*   `aws-crt`
*   `bcrypt`
*   `better-sqlite3`
*   `canvas`
*   `chromadb-default-embed`
*   `config`
*   `cpu-features`
*   `cypress`
*   `dd-trace`
*   `eslint`
*   `express`
*   `firebase-admin`
*   `htmlrewriter`
*   `import-in-the-middle`
*   `isolated-vm`
*   `jest`
*   `jsdom`
*   `keyv`
*   `libsql`
*   `mdx-bundler`
*   `mongodb`
*   `mongoose`
*   `newrelic`
*   `next-mdx-remote`
*   `next-seo`
*   `node-cron`
*   `node-pty`
*   `node-web-audio-api`
*   `onnxruntime-node`
*   `oslo`
*   `pg`
*   `pino`
*   `pino-pretty`
*   `pino-roll`
*   `playwright`
*   `playwright-core`
*   `postcss`
*   `prettier`
*   `prisma`
*   `puppeteer-core`
*   `puppeteer`
*   `ravendb`
*   `require-in-the-middle`
*   `rimraf`
*   `sharp`
*   `shiki`
*   `sqlite3`
*   `thread-stream`
*   `ts-morph`
*   `ts-node`
*   `typescript`
*   `vscode-oniguruma`
*   `webpack`
*   `websocket`
*   `zeromq`

Was this helpful?

supported.

Send
