---
title: "domain - Node documentation"
source: "https://docs.deno.com/api/node/domain/"
canonical_url: "https://docs.deno.com/api/node/domain/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:06:10.297Z"
content_hash: "89944bfbebb5727ecad4fa6e6efa891ea38c398d5c40b47e1d53987dd19bf167"
menu_path: ["domain - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/dns/promises/index.md", "title": "dns/promises - Node documentation"}
nav_next: {"path": "deno/api/node/events/index.md", "title": "events - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:domain";
```

Deprecated

Deno compatibility

All exports are non-functional stubs. This is a deprecated Node module.

**This module is pending deprecation.** Once a replacement API has been finalized, this module will be fully deprecated. Most developers should **not** have cause to use this module. Users who absolutely must have the functionality that domains provide may rely on it for the time being but should expect to have to migrate to a different solution in the future.

Domains provide a way to handle multiple different IO operations as a single group. If any of the event emitters or callbacks registered to a domain emit an `'error'` event, or throw an error, then the domain object will be notified, rather than losing the context of the error in the `process.on('uncaughtException')` handler, or causing the program to exit immediately with an error code.

c

[Domain](.././domain/~/Domain "Domain")

No documentation available

-   [add](.././domain/~/Domain#method_add_0)
-   [bind](.././domain/~/Domain#method_bind_0)
-   [enter](.././domain/~/Domain#method_enter_0)
-   [exit](.././domain/~/Domain#method_exit_0)
-   [intercept](.././domain/~/Domain#method_intercept_0)
-   [members](.././domain/~/Domain#property_members)
-   [remove](.././domain/~/Domain#method_remove_0)
-   [run](.././domain/~/Domain#method_run_0)

f

[create](.././domain/~/create "create")

No documentation available
