---
title: "Sequences"
source: "https://orm.drizzle.team/docs/sequences"
canonical_url: "https://orm.drizzle.team/docs/sequences"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:24:05.278Z"
content_hash: "aaa6195dc52f06ad3f111ba7f68dc75da405c703689932daf59e8c88ea676e87"
menu_path: ["Sequences"]
section_path: []
content_language: "en"
nav_prev: {"path": "../indexes-constraints/index.md", "title": "Indexes & Constraints"}
nav_next: {"path": "../views/index.md", "title": "Views"}
---

Sequences in PostgreSQL and CockroachDB are special single-row tables created to generate unique identifiers, often used for auto-incrementing primary key values. They provide a thread-safe way to generate unique sequential values across multiple sessions.

```ts
import { pgSchema, pgSequence } from "drizzle-orm/pg-core";

// No params specified
export const customSequence = pgSequence("name");

// Sequence with params
export const customSequence = pgSequence("name", {
      startWith: 100,
      maxValue: 10000,
      minValue: 100,
      cycle: true,
      cache: 10,
      increment: 2
});

// Sequence in custom schema
export const customSchema = pgSchema('custom_schema');
export const customSequence = customSchema.sequence("name");
```

```ts
import { cockroachSchema, cockroachSequence } from "drizzle-orm/cockroach-core";

// No params specified
export const customSequence = cockroachSequence("name");

// Sequence with params
export const customSequence = cockroachSequence("name", {
      startWith: 100,
      maxValue: 10000,
      minValue: 100,
      cycle: true,
      cache: 10,
      increment: 2
});

// Sequence in custom schema
export const customSchema = cockroachSchema('custom_schema');
export const customSequence = customSchema.sequence("name");
```
