---
title: "Add Sentry to a Bun app"
source: "https://bun.com/docs/guides/ecosystem/sentry"
canonical_url: "https://bun.com/docs/guides/ecosystem/sentry"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:10.854Z"
content_hash: "a9927e817f2f56a78ec2ce604ecfe7382e57797cb8e260c7099d3d5aff479bd9"
menu_path: ["Add Sentry to a Bun app"]
section_path: []
nav_prev: {"path": "bun/docs/guides/ecosystem/remix/index.md", "title": "Build an app with Remix and Bun"}
nav_next: {"path": "bun/docs/guides/ecosystem/solidstart/index.md", "title": "Build an app with SolidStart and Bun"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](../../../index.md)[Package Manager

](../../../pm/cli/install/index.md)[Bundler

](../../../bundler/index.md)[Test Runner

](../../../test/index.md)[Guides

](../../index.md)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](../../../feedback/index.md)

[Sentry](https://sentry.io) is a developer-first error tracking and performance monitoring platform. Sentry has a first-class SDK for Bun, `@sentry/bun`, that instruments your Bun application to automatically collect error and performance data. Don’t already have an account and Sentry project established? Head over to [sentry.io](https://sentry.io/signup/), then return to this page.

* * *

To start using Sentry with Bun, first install the Sentry Bun SDK.

terminal

```
bun add @sentry/bun
```

* * *

Then, initialize the Sentry SDK with your Sentry DSN in your app’s entry file. You can find your DSN in your Sentry project settings.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)sentry.ts

```
import * as Sentry from "@sentry/bun";

// Ensure to call this before importing any other modules!
Sentry.init({
  dsn: "__SENTRY_DSN__",

  // Add Performance Monitoring by setting tracesSampleRate
  // We recommend adjusting this value in production
  tracesSampleRate: 1.0,
});
```

* * *

You can verify that Sentry is working by capturing a test error:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)sentry.ts

```
setTimeout(() => {
  try {
    foo();
  } catch (e) {
    Sentry.captureException(e);
  }
}, 99);
```

To view and resolve the recorded error, log into [sentry.io](https://sentry.io/) and open your project. Clicking on the error’s title will open a page where you can see detailed information and mark it as resolved.

* * *

To learn more about Sentry and using the Sentry Bun SDK, view the [Sentry documentation](https://docs.sentry.io/platforms/javascript/guides/bun).

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/sentry.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/sentry>)

[

Use TanStack Start with Bun

Previous

](../tanstack-start/index.md)[

Build an app with SolidStart and Bun

Next

](../solidstart/index.md)
