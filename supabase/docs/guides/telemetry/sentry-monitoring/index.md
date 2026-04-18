---
title: "Sentry integration"
source: "https://supabase.com/docs/guides/telemetry/sentry-monitoring"
canonical_url: "https://supabase.com/docs/guides/telemetry/sentry-monitoring"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:19.164Z"
content_hash: "37b0f23b86f6672664d712a35cdbc5bba89cf3b3510e97fe83907341eb76296c"
menu_path: ["Telemetry","Telemetry","Logging & observability","Logging & observability","Sentry integration","Sentry integration"]
section_path: ["Telemetry","Telemetry","Logging & observability","Logging & observability","Sentry integration","Sentry integration"]
nav_prev: {"path": "supabase/docs/guides/telemetry/reports/index.md", "title": "Reports"}
nav_next: {"path": "supabase/docs/guides/ai/examples/headless-vector-search/index.md", "title": "Adding generative Q&A for your documentation"}
---

# 

Sentry integration

## 

Integrate Sentry to monitor errors from a Supabase client

* * *

You can use [Sentry](https://sentry.io/welcome/) to monitor errors thrown from a Supabase JavaScript client. Install the [Supabase Sentry integration](https://github.com/supabase-community/sentry-integration-js) to get started.

The Sentry integration supports browser, Node, and edge environments.

## Installation[#](#installation)

Install the Sentry integration using your package manager:

```
1npm install @supabase/sentry-js-integration
```

## Use[#](#use)

If you are using Sentry JavaScript SDK v7, reference [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README-v7.md) instead.

To use the Supabase Sentry integration, add it to your `integrations` list when initializing your Sentry client.

You can supply either the Supabase Client constructor or an already-initiated instance of a Supabase Client.

```
1import * as Sentry from '@sentry/browser'2import { SupabaseClient } from '@supabase/supabase-js'3import { supabaseIntegration } from '@supabase/sentry-js-integration'45Sentry.init({6  dsn: SENTRY_DSN,7  integrations: [8    supabaseIntegration(SupabaseClient, Sentry, {9      tracing: true,10      breadcrumbs: true,11      errors: true,12    }),13  ],14})
```

All available configuration options are available in our [`supabase-community/sentry-integration-js` repository](https://github.com/supabase-community/sentry-integration-js/blob/master/README.md#options).

## Deduplicating spans[#](#deduplicating-spans)

If you're already monitoring HTTP errors in Sentry, for example with the HTTP, Fetch, or Undici integrations, you will get duplicate spans for Supabase calls. You can deduplicate the spans by skipping them in your other integration:

```
1import * as Sentry from '@sentry/browser'2import { SupabaseClient } from '@supabase/supabase-js'3import { supabaseIntegration } from '@supabase/sentry-js-integration'45Sentry.init({6  dsn: SENTRY_DSN,7  integrations: [8    supabaseIntegration(SupabaseClient, Sentry, {9      tracing: true,10      breadcrumbs: true,11      errors: true,12    }),1314    // @sentry/browser15    Sentry.browserTracingIntegration({16      shouldCreateSpanForRequest: (url) => {17        return !url.startsWith(`${SUPABASE_URL}/rest`)18      },19    }),2021    // or @sentry/node22    Sentry.httpIntegration({23      tracing: {24        ignoreOutgoingRequests: (url) => {25          return url.startsWith(`${SUPABASE_URL}/rest`)26        },27      },28    }),2930    // or @sentry/node with Fetch support31    Sentry.nativeNodeFetchIntegration({32      ignoreOutgoingRequests: (url) => {33        return url.startsWith(`${SUPABASE_URL}/rest`)34      },35    }),3637    // or @sentry/WinterCGFetch for Next.js Proxy & Edge Functions38    Sentry.winterCGFetchIntegration({39      breadcrumbs: true,40      shouldCreateSpanForRequest: (url) => {41        return !url.startsWith(`${SUPABASE_URL}/rest`)42      },43    }),44  ],45})
```

## Example Next.js configuration[#](#example-nextjs-configuration)

See this example for a setup with Next.js to cover browser, server, and edge environments. First, run through the [Sentry Next.js wizard](https://docs.sentry.io/platforms/javascript/guides/nextjs/#install) to generate the base Next.js configuration. Then add the Supabase Sentry Integration to all your `Sentry.init` calls with the appropriate filters.

```
1import * as Sentry from '@sentry/nextjs'2import { SupabaseClient } from '@supabase/supabase-js'3import { supabaseIntegration } from '@supabase/sentry-js-integration'45Sentry.init({6  dsn: SENTRY_DSN,7  integrations: [8    supabaseIntegration(SupabaseClient, Sentry, {9      tracing: true,10      breadcrumbs: true,11      errors: true,12    }),13    Sentry.browserTracingIntegration({14      shouldCreateSpanForRequest: (url) => {15        return !url.startsWith(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest`)16      },17    }),18  ],1920  // Adjust this value in production, or use tracesSampler for greater control21  tracesSampleRate: 1,2223  // Setting this option to true will print useful information to the console while you're setting up Sentry.24  debug: true,25})
```

Afterwards, build your application (`npm run build`) and start it locally (`npm run start`). You will now see the transactions being logged in the terminal when making supabase-js requests.
