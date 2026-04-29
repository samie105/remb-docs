---
title: "Drizzle Queries + CRUD"
source: "https://orm.drizzle.team/docs/data-querying"
canonical_url: "https://orm.drizzle.team/docs/data-querying"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:34:11.150Z"
content_hash: "9a4d064852101fd2a8b1e2984b82cc5d0b66f1762c02b4ecf45df3e310df318e"
menu_path: ["Drizzle Queries + CRUD"]
section_path: []
content_language: "en"
nav_prev: {"path": "../connect-overview/index.md", "title": "Database connection with Drizzle"}
nav_next: {"path": "../migrations/index.md", "title": "Drizzle migrations fundamentals"}
---

## Drizzle Queries + CRUD

Drizzle gives you a few ways for querying your database and it’s up to you to decide which one you’ll need in your next project. It can be either SQL-like syntax or Relational Syntax. Let’s check them:

## Why SQL-like?[](#why-sql-like)

  
**If you know SQL, you know Drizzle.**

Other ORMs and data frameworks tend to deviate from or abstract away SQL, leading to a double learning curve: you need to learn both SQL and the framework’s API.

Drizzle is the opposite. We embrace SQL and built Drizzle to be SQL-like at its core, so you have little to no learning curve and full access to the power of SQL.

```typescript
// Access your data
await db
  .select()
	.from(posts)
	.leftJoin(comments, eq(posts.id, comments.post_id))
	.where(eq(posts.id, 10))
```

```sql
SELECT * 
FROM posts
LEFT JOIN comments ON posts.id = comments.post_id
WHERE posts.id = 10
```

With SQL-like syntax, you can replicate much of what you can do with pure SQL and know exactly what Drizzle will do and what query will be generated. You can perform a wide range of queries, including select, insert, update, delete, as well as using aliases, WITH clauses, subqueries, prepared statements, and more. Let’s look at more examples

```ts
await db.insert(users).values({ email: 'user@gmail.com' })
```

```sql
INSERT INTO users (email) VALUES ('user@gmail.com')
```

## Why not SQL-like?[](#why-not-sql-like)

We’re always striving for a perfectly balanced solution. While SQL-like queries cover 100% of your needs, there are certain common scenarios where data can be queried more efficiently.

We’ve built the Queries API so you can fetch relational, nested data from the database in the most convenient and performant way, without worrying about joins or data mapping.

**Drizzle always outputs exactly one SQL query**. Feel free to use it with serverless databases, and never worry about performance or roundtrip costs!

```ts
const result = await db.query.users.findMany({
	with: {
		posts: true
	},
});
```

## Advanced[](#advanced)

With Drizzle, queries can be composed and partitioned in any way you want. You can compose filters independently from the main query, separate subqueries or conditional statements, and much more. Let’s check a few advanced examples:

#### Compose a WHERE statement and then use it in a query[](#compose-a-where-statement-and-then-use-it-in-a-query)

```ts
async function getProductsBy({
  name,
  category,
  maxPrice,
}: {
  name?: string;
  category?: string;
  maxPrice?: string;
}) {
  const filters: SQL[] = [];

  if (name) filters.push(ilike(products.name, name));
  if (category) filters.push(eq(products.category, category));
  if (maxPrice) filters.push(lte(products.price, maxPrice));

  return db
    .select()
    .from(products)
    .where(and(...filters));
}
```

#### Separate subqueries into different variables, and then use them in the main query[](#separate-subqueries-into-different-variables-and-then-use-them-in-the-main-query)

```ts
const subquery = db
	.select()
	.from(internalStaff)
	.leftJoin(customUser, eq(internalStaff.userId, customUser.id))
	.as('internal_staff');

const mainQuery = await db
	.select()
	.from(ticket)
	.leftJoin(subquery, eq(subquery.internal_staff.userId, ticket.staffId));
```

#### What’s next?[](#whats-next)
