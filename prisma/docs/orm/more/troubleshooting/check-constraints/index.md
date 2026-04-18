---
title: "Check constraints"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/check-constraints"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/check-constraints"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:21.145Z"
content_hash: "eaff84a9df727fd52b9f1d092070a9458a8d531cff895c535c4c825d8073b852"
menu_path: ["Check constraints"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/troubleshooting/bundler-issues/index.md", "title": "Bundler issues"}
nav_next: {"path": "prisma/docs/orm/more/troubleshooting/graphql-autocompletion/index.md", "title": "GraphQL autocompletion"}
---

Troubleshooting

Learn how to configure CHECK constraints for data validation with Prisma ORM and PostgreSQL

This page explains how to configure [check constraints](https://www.postgresql.org/docs/9.4/ddl-constraints.html#DDL-CONSTRAINTS-CHECK-CONSTRAINTS) in a PostgreSQL database. A check constraint is a condition that must be satisfied before a value can be saved to a table - for example, the discounted price of a product must always be less than the original price.

Check constraints can be added when you create the table (using `CREATE TABLE`) or to a table that already exists (using `ALTER TABLE`).

*   A [PostgreSQL](https://www.postgresql.org/) database server running
*   The [`psql`](https://www.postgresql.org/docs/13/app-psql.html) command line client
*   [Node.js](https://nodejs.org/) installed

Create a table with a check constraint on a single column:

```
CREATE TABLE "public"."product" (
  price NUMERIC CONSTRAINT price_value_check CHECK (price > 0.01 AND price <> 1240.00)
);
ALTER TABLE "public"."product"
  ADD COLUMN "productid" serial,
  ADD PRIMARY KEY ("productid");
```

This ensures the price is never less than 0.01 and never equal to 1240.00.

Create a table with a check constraint that compares values of two columns:

```
CREATE TABLE "public"."anotherproduct" (
  reducedprice NUMERIC CONSTRAINT reduced_price_check CHECK (price > reducedprice),
  price NUMERIC
);
ALTER TABLE "public"."anotherproduct"
  ADD COLUMN "productid" serial,
  ADD PRIMARY KEY ("productid");
```

This ensures `reducedprice` is always less than `price`.

```
CREATE TABLE "public"."secondtolastproduct" (
  reducedprice NUMERIC CONSTRAINT reduced_price_check CHECK (price > reducedprice),
  price NUMERIC,
  tags TEXT[] CONSTRAINT tags_contains_product CHECK ('product' = ANY(tags))
);
ALTER TABLE "public"."secondtolastproduct"
  ADD COLUMN "productid" serial,
  ADD PRIMARY KEY ("productid");
```

```
CREATE TABLE "public"."lastproduct" (
  category TEXT
);

ALTER TABLE "public"."lastproduct"
  ADD CONSTRAINT "category_not_clothing" CHECK (category <> 'clothing');
```

After introspection, your Prisma schema will include the models but the check constraints are enforced at the database level:

```
model product {
  price     Float?
  productid Int    @id
}

model anotherproduct {
  price        Float?
  productid    Int    @id
  reducedprice Float?
}
```

Generate Prisma Client and test:

```
const { PrismaClient } = require("../prisma/generated/client");

const prisma = new PrismaClient();

async function main() {
  // This will fail due to the check constraint
  const newProduct = await prisma.product.create({
    data: {
      price: 0.0, // violates price > 0.01
    },
  });
}

main();
```

The script throws an error indicating the `price_check_value` check constraint was not met:

```
Error: new row for relation "product" violates check constraint "price_value_check"
```

Check constraints are resolved in alphabetical order, and only the first constraint to fail appears in the error message.

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/more/troubleshooting/check-constraints.mdx)

