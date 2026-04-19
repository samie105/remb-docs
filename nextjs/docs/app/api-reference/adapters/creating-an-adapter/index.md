---
title: "Creating an Adapter"
source: "https://nextjs.org/docs/app/api-reference/adapters/creating-an-adapter"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters/creating-an-adapter"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:05:44.518Z"
content_hash: "f754db1430d76d77f2f69d6079c97602ceda7af1129518852cf341755471d30f"
menu_path: ["Creating an Adapter"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/adapters/configuration/index.md", "title": "Configuration"}
nav_next: {"path": "nextjs/docs/app/api-reference/adapters/api-reference/index.md", "title": "API Reference"}
---

# Creating an Adapter

Last updated April 15, 2026

An adapter is a module that exports an object implementing the `NextAdapter` interface.

The interface can be imported from the `next` package:

```
import type { NextAdapter } from 'next'
```

The interface is defined as follows:

```
type Route = {
  source?: string
  sourceRegex: string
  destination?: string
  headers?: Record<string, string>
  has?: RouteHas[]
  missing?: RouteHas[]
  status?: number
  priority?: boolean
}
 
export interface AdapterOutputs {
  pages: Array<AdapterOutput['PAGES']>
  middleware?: AdapterOutput['MIDDLEWARE']
  appPages: Array<AdapterOutput['APP_PAGE']>
  pagesApi: Array<AdapterOutput['PAGES_API']>
  appRoutes: Array<AdapterOutput['APP_ROUTE']>
  prerenders: Array<AdapterOutput['PRERENDER']>
  staticFiles: Array<AdapterOutput['STATIC_FILE']>
}
 
export interface NextAdapter {
  name: string
  modifyConfig?: (
    config: NextConfigComplete,
    ctx: {
      phase: PHASE_TYPE
      nextVersion: string
    }
  ) => Promise<NextConfigComplete> | NextConfigComplete
  onBuildComplete?: (ctx: {
    routing: {
      beforeMiddleware: Array<Route>
      beforeFiles: Array<Route>
      afterFiles: Array<Route>
      dynamicRoutes: Array<Route>
      onMatch: Array<Route>
      fallback: Array<Route>
      shouldNormalizeNextData: boolean
      rsc: RoutesManifest['rsc']
    }
    outputs: AdapterOutputs
    projectDir: string
    repoRoot: string
    distDir: string
    config: NextConfigComplete
    nextVersion: string
    buildId: string
  }) => Promise<void> | void
}
```

## Basic Adapter Structure[](#basic-adapter-structure)

Here's a minimal adapter example:

my-adapter.js

```
/** @type {import('next').NextAdapter} */
const adapter = {
  name: 'my-custom-adapter',
 
  async modifyConfig(config, { phase }) {
    // Modify the Next.js config based on the build phase
    if (phase === 'phase-production-build') {
      return {
        ...config,
        // Add your modifications
      }
    }
    return config
  },
 
  async onBuildComplete({
    routing,
    outputs,
    projectDir,
    repoRoot,
    distDir,
    config,
    nextVersion,
    buildId,
  }) {
    // Process the build output
    console.log('Build completed with', outputs.pages.length, 'pages')
    console.log('Build ID:', buildId)
    console.log('Dynamic routes:', routing.dynamicRoutes.length)
 
    // Access emitted output entries
    for (const page of outputs.pages) {
      console.log('Page:', page.pathname, 'at', page.filePath)
    }
 
    for (const apiRoute of outputs.pagesApi) {
      console.log('API Route:', apiRoute.pathname, 'at', apiRoute.filePath)
    }
 
    for (const appPage of outputs.appPages) {
      console.log('App Page:', appPage.pathname, 'at', appPage.filePath)
    }
 
    for (const prerender of outputs.prerenders) {
      console.log('Prerendered:', prerender.pathname)
    }
  },
}
 
module.exports = adapter
```

[Previous

Configuration

](/docs/app/api-reference/adapters/configuration)

[Next

API Reference

](/docs/app/api-reference/adapters/api-reference)

Was this helpful?

supported.

Send
