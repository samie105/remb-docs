---
title: "Run Bun as a daemon with PM2"
source: "https://bun.com/docs/guides/ecosystem/pm2"
canonical_url: "https://bun.com/docs/guides/ecosystem/pm2"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:13.406Z"
content_hash: "d84cddd5dec93fa5d0832267338d62600dcb1aa4b72f7eb174a961055de28a8f"
menu_path: ["Run Bun as a daemon with PM2"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/nuxt/index.md", "title": "Build an app with Nuxt and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/prisma/index.md", "title": "Use Prisma with Bun"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

[PM2](https://pm2.keymetrics.io/) is a popular process manager that manages and runs your applications as daemons (background processes). It offers features like process monitoring, automatic restarts, and scaling. Using a process manager is common when deploying a Bun application on a cloud-hosted virtual private server (VPS), as it:

*   Keeps your application running continuously.
*   Ensures high availability and reliability of your application.
*   Monitors and manages multiple processes.
*   Simplifies the deployment process.

* * *

You can use PM2 with Bun in two ways: as a CLI option or in a configuration file.

### 

[​

](#with-interpreter)

With `--interpreter`

To start your application with PM2 and Bun as the interpreter, open your terminal and run the following command:

terminal

```
pm2 start --interpreter ~/.bun/bin/bun index.ts
```

* * *

### 

[​

](#with-a-configuration-file)

With a configuration file

Alternatively, you can create a PM2 configuration file. Create a file named `pm2.config.js` in your project directory and add the following content.

pm2.config.js

```
module.exports = {
  name: "app", // Name of your application
  script: "index.ts", // Entry point of your application
  interpreter: "bun", // Bun interpreter
  env: {
    PATH: `${process.env.HOME}/.bun/bin:${process.env.PATH}`, // Add "~/.bun/bin/bun" to PATH
  },
};
```

* * *

After saving the file, you can start your application with PM2

terminal

```
pm2 start pm2.config.js
```

* * *

That’s it! Your JavaScript/TypeScript web server is now running as a daemon with PM2 using Bun as the interpreter.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/pm2.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/pm2>)

[

Build an app with Nuxt and Bun

Previous

](/docs/guides/ecosystem/nuxt)[

Use Prisma with Bun

Next

](/docs/guides/ecosystem/prisma)
