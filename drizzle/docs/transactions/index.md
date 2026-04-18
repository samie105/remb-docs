---
title: "Transactions"
source: "https://orm.drizzle.team/docs/transactions"
canonical_url: "https://orm.drizzle.team/docs/transactions"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:22:18.854Z"
content_hash: "e5a6ff3598776bdc4f486de081a20a3e52484011cbc0adf7c8b3bfa1be393373"
menu_path: ["Transactions"]
section_path: []
nav_prev: {"path": "drizzle/docs/generated-columns/index.md", "title": "Generated Columns"}
nav_next: {"path": "drizzle/docs/batch-api/index.md", "title": "Batch API"}
---

SQL transaction is a grouping of one or more SQL statements that interact with a database. A transaction in its entirety can commit to a database as a single logical unit or rollback (become undone) as a single logical unit.

Drizzle ORM provides APIs to run SQL statements in transactions:

```
const db = drizzle(...)

await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));
});
```

Drizzle ORM supports `savepoints` with nested transactions API:

```
const db = drizzle(...)

await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));

  await tx.transaction(async (tx2) => {
    await tx2.update(users).set({ name: "Mr. Dan" }).where(eq(users.name, "Dan"));
  });
});
```

You can embed business logic to the transaction and rollback whenever needed:

```
const db = drizzle(...)

await db.transaction(async (tx) => {
  const [account] = await tx.select({ balance: accounts.balance }).from(accounts).where(eq(users.name, 'Dan'));
  if (account.balance < 100) {
    // This throws an exception that rollbacks the transaction.
    tx.rollback()
  }

  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));
});
```

You can return values from the transaction:

```
const db = drizzle(...)

const newBalance: number = await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));

  const [account] = await tx.select({ balance: accounts.balance }).from(accounts).where(eq(users.name, 'Dan'));
  return account.balance;
});
```

You can use transactions with **[relational queries](drizzle/docs/rqb/index.md)**:

```
const db = drizzle({ schema })

await db.transaction(async (tx) => {
  await tx.query.users.findMany({
    with: {
      accounts: true
    }
  });
});
```

We provide dialect-specific transaction configuration APIs:

PostgreSQL

MySQL

SQLite

SingleStore

MSSQL

CockroachDB

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    deferrable: true,
  }
);

interface PgTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  deferrable?: boolean;
}
```

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    withConsistentSnapshot: true,
  }
);

interface MySqlTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  withConsistentSnapshot?: boolean;
}
```

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    behavior: "deferred",
  }
);

interface SQLiteTransactionConfig {
    behavior?: 'deferred' | 'immediate' | 'exclusive';
}
```

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    withConsistentSnapshot: true,
  }
);

interface SingleStoreTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  withConsistentSnapshot?: boolean;
}
```

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
  }
);

interface MsSqlTransactionConfig {
  isolationLevel?: 'read uncommitted' | 'read committed' | 'repeatable read' | 'serializable' | 'snapshot';
}
```

```
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    deferrable: true,
  }
);

interface CockroachTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  deferrable?: boolean;
}
```


