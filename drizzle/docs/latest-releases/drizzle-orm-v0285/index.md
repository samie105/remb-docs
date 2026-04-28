---
title: "Drizzle ORM - DrizzleORM v0.28.5 release"
source: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0285"
canonical_url: "https://orm.drizzle.team/docs/latest-releases/drizzle-orm-v0285"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:09:53.944Z"
content_hash: "9eead965871a7a04674ae15d2fec39929b0de6fc1c3f650ff3eca183aec75a93"
menu_path: ["Drizzle ORM - DrizzleORM v0.28.5 release"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0284/index.md", "title": "Drizzle ORM - DrizzleORM v0.28.4 release"}
nav_next: {"path": "drizzle/docs/latest-releases/drizzle-orm-v0286/index.md", "title": "Drizzle ORM - DrizzleORM v0.28.6 release"}
---

DrizzleORM v0.28.5 release

Aug 24, 2023

## Fixes

-   Fixed incorrect OpenTelemetry type import that caused a runtime error

The OpenTelemetry logic currently present in the ORM isn’t meant to be used by Drizzle and no stats have ever been collected by Drizzle using drizzle-orm. OpenTelemetry is simply a protocol. If you take a look at the actual code that utilizes it in drizzle-orm, it simply uses the tracer to collect the query stats and doesn’t send it anywhere. It was designed for the ORM users to be able to send those stats to their own telemetry consumers.

The important thing is - the OpenTelemetry logic is disabled on the current version. It literally does nothing. We experimented with it at some point in the past, but disabled it before the release.

As to the reason of the issue in the last release: it happened because of an incorrect type import on [this line](https://github.com/drizzle-team/drizzle-orm/blob/594e96538e588fee5748e372884dbaf32c331524/drizzle-orm/src/tracing.ts#L1). We’ve used `import { type ... }` syntax instead of `import type { ... }`, which resulted in the `import '@opentelemetry/api'` line leaking to the runtime.
