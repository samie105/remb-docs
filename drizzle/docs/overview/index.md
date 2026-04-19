---
title: "Drizzle ORM"
source: "https://orm.drizzle.team/docs/overview"
canonical_url: "https://orm.drizzle.team/docs/overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:35.761Z"
content_hash: "8951abfabbeebf652b39e7d83831c621b2ca54e19d99fa69895209e3a673c886"
menu_path: ["Drizzle ORM"]
section_path: []
nav_next: {"path": "drizzle/docs/get-started/index.md", "title": "Get started with Drizzle"}
---

Drizzle ORM is a headless TypeScript ORM with a head. 🐲

> Drizzle is a good friend who’s there for you when necessary and doesn’t bother when you need some space.

It looks and feels simple, performs on day _1000_ of your project,  
lets you do things your way, and is there when you need it.

**It’s the only ORM with both [relational](drizzle/docs/rqb/index.md) and [SQL-like](drizzle/docs/select/index.md) query APIs**, providing you the best of both worlds when it comes to accessing your relational data. Drizzle is lightweight, performant, typesafe, non-lactose, gluten-free, sober, flexible and **serverless-ready by design**. Drizzle is not just a library, it’s an experience. 🤩

[![Drizzle bestofjs](https://orm.drizzle.team/_astro/bestofjs.Dmfq7AUp_26yiDJ.webp)](https://bestofjs.org/projects/drizzle-orm)

## Headless ORM?[](#headless-orm)

First and foremost, Drizzle is a library and a collection of complementary opt-in tools.

**ORM** stands for _object relational mapping_, and developers tend to call Django-like or Spring-like tools an ORM. We truly believe it’s a misconception based on legacy nomenclature, and we call them **data frameworks**.

WARNING

With data frameworks you have to build projects **around them** and not **with them**.

**Drizzle** lets you build your project the way you want, without interfering with your project or structure.

Using Drizzle you can define and manage database schemas in TypeScript, access your data in a SQL-like or relational way, and take advantage of opt-in tools to push your developer experience _through the roof_. 🤯

## Why SQL-like?[](#why-sql-like)

**If you know SQL, you know Drizzle.**

Other ORMs and data frameworks tend to deviate/abstract you away from SQL, which leads to a double learning curve: needing to know both SQL and the framework’s API.

Drizzle is the opposite. We embrace SQL and built Drizzle to be SQL-like at its core, so you can have zero to no learning curve and access to the full power of SQL.

We bring all the familiar **[SQL schema](drizzle/docs/sql-schema-declaration/index.md)**, **[queries](drizzle/docs/select/index.md)**, **[automatic migrations](drizzle/docs/migrations/index.md)** and **[one more thing](drizzle/docs/rqb/index.md)**. ✨

index.ts

schema.ts

migration.sql

```
// Access your data
await db
	.select()
	.from(countries)
	.leftJoin(cities, eq(cities.countryId, countries.id))
	.where(eq(countries.id, 10))
```

```
// manage your schema
export const countries = pgTable('countries', {
  id: serial('id').primaryKey(),
  name: varchar('name', { length: 256 }),
});

export const cities = pgTable('cities', {
  id: serial('id').primaryKey(),
  name: varchar('name', { length: 256 }),
  countryId: integer('country_id').references(() => countries.id),
});
```

```
-- generate migrations
CREATE TABLE IF NOT EXISTS "countries" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" varchar(256)
);

CREATE TABLE IF NOT EXISTS "cities" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" varchar(256),
	"country_id" integer
);

ALTER TABLE "cities" ADD CONSTRAINT "cities_country_id_countries_id_fk" FOREIGN KEY ("country_id") REFERENCES "countries"("id") ON DELETE no action ON UPDATE no action;
```

## Why not SQL-like?[](#why-not-sql-like)

We’re always striving for a perfectly balanced solution, and while SQL-like does cover 100% of the needs, there are certain common scenarios where you can query data in a better way.

We’ve built the **[Queries API](drizzle/docs/rqb/index.md)** for you, so you can fetch relational nested data from the database in the most convenient and performant way, and never think about joins and data mapping.

**Drizzle always outputs exactly 1 SQL query.** Feel free to use it with serverless databases and never worry about performance or roundtrip costs!

```
const result = await db.query.users.findMany({
	with: {
		posts: true
	},
});
```

## Serverless?[](#serverless)

The best part is no part. **Drizzle has exactly 0 dependencies!**

![Drizzle is slim an Serverless ready](https://orm.drizzle.team/_astro/drizzle31kb.6Mn-oJyX_ZHNm12.webp)

Drizzle ORM is dialect-specific, slim, performant and serverless-ready **by design**.

We’ve spent a lot of time to make sure you have best-in-class SQL dialect support, including Postgres, MySQL, and others.

Drizzle operates natively through industry-standard database drivers. We support all major **[PostgreSQL](drizzle/docs/get-started-postgresql/index.md)**, **[MySQL](drizzle/docs/get-started-mysql/index.md)**, **[SQLite](drizzle/docs/get-started-sqlite/index.md)** or **[SingleStore](drizzle/docs/get-started-singlestore/index.md)** drivers out there, and we’re adding new ones **[really fast](https://twitter.com/DrizzleORM/status/1653082492742647811?s=20)**.

## Welcome on board![](#welcome-on-board)

More and more companies are adopting Drizzle in production, experiencing immense benefits in both DX and performance.

**We’re always there to help, so don’t hesitate to reach out. We’ll gladly assist you in your Drizzle journey!**

We have an outstanding **[Discord community](https://driz.link/discord)** and welcome all builders to our **[Twitter](https://twitter.com/drizzleorm)**.

Now go build something awesome with Drizzle and your **[PostgreSQL](drizzle/docs/get-started-postgresql/index.md)**, **[MySQL](drizzle/docs/get-started-mysql/index.md)** or **[SQLite](drizzle/docs/get-started-sqlite/index.md)** database. 🚀

### Video Showcase[](#video-showcase)
