---
title: "Batch API"
source: "https://orm.drizzle.team/docs/batch-api"
canonical_url: "https://orm.drizzle.team/docs/batch-api"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:24:30.059Z"
content_hash: "3a73b9f33a735642ebbb5cbfc60681b790fe9f6e58d2a398c5e868542f57ff6d"
menu_path: ["Batch API"]
section_path: []
content_language: "en"
nav_prev: {"path": "../transactions/index.md", "title": "Transactions"}
nav_next: {"path": "../cache/index.md", "title": "Cache"}
---

## Batch API

**LibSQL Batch API explanation**: _[source](https://docs.turso.tech/sdk/ts/reference#batch-transactions)_

> With the libSQL client library, a batch is one or more SQL statements executed in order in an implicit transaction. The transaction is controlled by the libSQL backend. If all of the statements are successful, the transaction is committed. If any of the statements fail, the entire transaction is rolled back and no changes are made.

**D1 Batch API explanation**: _[source](https://developers.cloudflare.com/d1/worker-api/d1-database/#batch)_

> Batching sends multiple SQL statements inside a single call to the database. This can have a huge performance impact as it reduces latency from network round trips to D1. D1 operates in auto-commit. Our implementation guarantees that each statement in the list will execute and commit, sequentially, non-concurrently. Batched statements are SQL transactions. If a statement in the sequence fails, then an error is returned for that specific statement, and it aborts or rolls back the entire sequence.

Drizzle ORM provides APIs to run SQL statements in batch for `LibSQL`, `Neon` and `D1`:

```ts
const batchResponse: BatchResponse = await db.batch([
	db.insert(usersTable).values({ id: 1, name: 'John' }).returning({ id: usersTable.id }),
	db.update(usersTable).set({ name: 'Dan' }).where(eq(usersTable.id, 1)),
	db.query.usersTable.findMany({}),
	db.select().from(usersTable).where(eq(usersTable.id, 1)),
	db.select({ id: usersTable.id, invitedBy: usersTable.invitedBy }).from(usersTable),
]);
```

Type for `batchResponse` in this example would be:

```ts
type BatchResponse = [
	{
		id: number;
	}[],
	ResultSet,
	{
		id: number;
		name: string;
		verified: number;
		invitedBy: number | null;
	}[],
	{
		id: number;
		name: string;
		verified: number;
		invitedBy: number | null;
	}[],
	{
		id: number;
		invitedBy: number | null;
	}[],
]
```

```ts
type BatchResponse = [
	{
		id: number;
	}[],
	NeonHttpQueryResult,
	{
		id: number;
		name: string;
		verified: number;
		invitedBy: number | null;
	}[],
	{
		id: number;
		name: string;
		verified: number;
		invitedBy: number | null;
	}[],
	{
		id: number;
		invitedBy: number | null;
	}[],
]
```

```ts
type BatchResponse = [
  {
    id: number;
  }[],
  D1Result,
  {
    id: number;
    name: string;
    verified: number;
    invitedBy: number | null;
  }[],
  {
    id: number;
    name: string;
    verified: number;
    invitedBy: number | null;
  }[],
  {
    id: number;
    invitedBy: number | null;
  }[],
]
```

All possible builders that can be used inside `db.batch`:

```ts
db.all(),
db.get(),
db.values(),
db.run(),
db.execute(),
db.query.<table>.findMany(),
db.query.<table>.findFirst(),
db.select()...,
db.update()...,
db.delete()...,
db.insert()...,
```
