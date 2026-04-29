---
title: "Set a time zone in Bun"
source: "https://bun.com/docs/guides/runtime/timezone"
canonical_url: "https://bun.com/docs/guides/runtime/timezone"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:18.912Z"
content_hash: "93cc6388bf2288c6814c6381e1be3f2f01d40fb62816ebcf90577f0071c6afc7"
menu_path: ["Set a time zone in Bun"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/shell/index.md", "title": "Run a Shell Command"}
nav_next: {"path": "bun/docs/guides/runtime/tsconfig-paths/index.md", "title": "Re-map import paths"}
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

Bun supports programmatically setting a default time zone for the lifetime of the `bun` process. To do set, set the value of the `TZ` environment variable to a [valid timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

When running a file with `bun`, the timezone defaults to your system’s configured local time zone.When running tests with `bun test`, the timezone is set to `UTC` to make tests more deterministic.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)process.ts

```
process.env.TZ = "America/New_York";
```

* * *

Alternatively, this can be set from the command line when running a Bun command.

terminal

```
TZ=America/New_York bun run dev
```

* * *

Once `TZ` is set, any `Date` instances will have that time zone. By default all dates use your system’s configured time zone.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)process.ts

```
new Date().getHours(); // => 18

process.env.TZ = "America/New_York";

new Date().getHours(); // => 21
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/runtime/timezone.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/runtime/timezone>)

[

Run a Shell Command

Previous

](../shell/index.md)[

Set environment variables

Next

](../set-env/index.md)
