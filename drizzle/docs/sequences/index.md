---
title: "Sequences"
source: "https://orm.drizzle.team/docs/sequences"
canonical_url: "https://orm.drizzle.team/docs/sequences"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:21:08.894Z"
content_hash: "e9351c909ddf4335c988674b59cc05b2ce4364a176b6333923e50b70b6661595"
menu_path: ["Sequences"]
section_path: []
nav_prev: {"path": "drizzle/docs/indexes-constraints/index.md", "title": "Indexes & Constraints"}
nav_next: {"path": "drizzle/docs/views/index.md", "title": "Views"}
---

PostgreSQL

SQLite

MySQL

SingleStore

MSSQL

CockroachDB

Sequences in PostgreSQL and CockroachDB are special single-row tables created to generate unique identifiers, often used for auto-incrementing primary key values. They provide a thread-safe way to generate unique sequential values across multiple sessions.

PostgreSQL

CockroachDB

```
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

```
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


