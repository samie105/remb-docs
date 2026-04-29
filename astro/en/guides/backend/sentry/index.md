---
title: "Monitor your Astro Site with Sentry"
source: "https://docs.astro.build/en/guides/backend/sentry/"
canonical_url: "https://docs.astro.build/en/guides/backend/sentry/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:43.411Z"
content_hash: "1ca113ccc20f4d4371484563553df67e82fd4d5f95fde48f35dac562b92e33c9"
menu_path: ["Monitor your Astro Site with Sentry"]
section_path: []
nav_prev: {"path": "../scalekit/index.md", "title": "Scalekit & Astro"}
nav_next: {"path": "../supabase/index.md", "title": "Supabase & Astro"}
---

# Monitor your Astro Site with Sentry

[Sentry](https://sentry.io) offers a comprehensive application monitoring and error tracking service designed to help developers identify, diagnose, and resolve issues in real-time.

Read more on our blog about [Astro’s partnership with Sentry](https://astro.build/blog/sentry-official-monitoring-partner/) and Sentry’s Spotlight dev toolbar app that brings a rich debug overlay into your Astro development environment. Spotlight shows errors, traces, and important context right in your browser during local development.

Sentry’s Astro SDK enables automatic reporting of errors and tracing data in your Astro application.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

A full list of prerequisites can be found in [the Sentry guide for Astro](https://docs.sentry.io/platforms/javascript/guides/astro/#prerequisites).

## Install

[Section titled “Install”](#install)

Sentry captures data by using an SDK within your application’s runtime.

Install the SDK by running the following command for the package manager of your choice in the Astro CLI:

*   [npm](#tab-panel-1453)
*   [pnpm](#tab-panel-1454)
*   [Yarn](#tab-panel-1455)

```
npx astro add @sentry/astro
```

The astro CLI installs the SDK package and adds the Sentry integration to your `astro.config.mjs` file.

## Configure

[Section titled “Configure”](#configure)

To configure the Sentry integration, you need to provide the following credentials in your `astro.config.mjs` file.

1.  **Client key (DSN)** - You can find the DSN in your Sentry project settings under _Client keys (DSN)_.
2.  **Project name** - You can find the project name in your Sentry project settings under _General settings_.
3.  **Auth token** - You can create an auth token in your Sentry organization settings under _Auth tokens_.

```
import { defineConfig } from 'astro/config';import sentry from '@sentry/astro';
export default defineConfig({  integrations: [    sentry({      dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',      sourceMapsUploadOptions: {        project: 'example-project',        authToken: process.env.SENTRY_AUTH_TOKEN,      },    }),  ],});
```

Once you’ve configured your `sourceMapsUploadOptions` and added your `dsn`, the SDK will automatically capture and send errors and performance events to Sentry.

## Test your setup

[Section titled “Test your setup”](#test-your-setup)

Add the following `<button>` element to one of your `.astro` pages. This will allow you to manually trigger an error so you can test the error reporting process.

```
<button onclick="throw new Error('This is a test error')">Throw test error</button>
```

To view and resolve the recorded error, log into [sentry.io](https://sentry.io/) and open your project.

## More backend service guides

*   ![](/logos/appwriteio.svg)
    
    ### [Appwrite](/en/guides/backend/appwrite/)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](/en/guides/backend/firebase/)
    
*   ![](/logos/neon.svg)
    
    ### [Neon](/en/guides/backend/neon/)
    
*   ![](/logos/prisma-postgres.svg)
    
    ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)
    
*   ![](/logos/scalekit.svg)
    
    ### [Scalekit](/en/guides/backend/scalekit/)
    
*   ![](/logos/sentry.svg)
    
    ### [Sentry](/en/guides/backend/sentry/)
    
*   ![](/logos/supabase.svg)
    
    ### [Supabase](/en/guides/backend/supabase/)
    
*   ![](/logos/turso.svg)
    
    ### [Turso](/en/guides/backend/turso/)
    
*   ![](/logos/xata.svg)
    
    ### [Xata](/en/guides/backend/xata/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
