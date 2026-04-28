---
title: "Drizzle ORM - Seeding Partially Exposed Tables with Foreign Key"
source: "https://orm.drizzle.team/docs/guides/seeding-with-partially-exposed-tables"
canonical_url: "https://orm.drizzle.team/docs/guides/seeding-with-partially-exposed-tables"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:02:35.329Z"
content_hash: "92df43a8f59f64ffca5f6ddb7b309eb31f8306a48dcdcb521b54e62a7b52855d"
menu_path: ["Drizzle ORM - Seeding Partially Exposed Tables with Foreign Key"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/guides/seeding-using-with-option/index.md", "title": "Drizzle ORM - Seeding using 'with' option"}
nav_next: {"path": "drizzle/docs/guides/select-parent-rows-with-at-least-one-related-child-row/index.md", "title": "Drizzle ORM - Select parent rows with at least one related child row"}
---

Drizzle | Seeding Partially Exposed Tables with Foreign Key

## Example 1[](#example-1)

Let’s assume you are trying to seed your database using the seeding script and schema shown below.

```ts
import { bloodPressure } from './schema.ts';

async function main() {
  const db = drizzle(...);
  await seed(db, { bloodPressure });
}
main();
```

If the `bloodPressure` table has a not-null constraint on the `userId` column, running the seeding script will cause an error.

```plaintext
Error: Column 'userId' has not null constraint, 
and you didn't specify a table for foreign key on column 'userId' in 'bloodPressure' table.
```

What does it mean?

This means we can’t fill the `userId` column with Null values due to the not-null constraint on that column. Additionally, you didn’t expose the `users` table to the `seed` function schema, so we can’t generate `users.id` to populate the `userId` column with these values.

At this point, you have several options to resolve the error:

-   You can remove the not-null constraint from the `userId` column;
-   You can expose `users` table to `seed` function schema

```ts
await seed(db, { bloodPressure, users });
```

-   You can [refine](drizzle/docs/guides/seeding-with-partially-exposed-tables/index.md#refining-the-userid-column-generator) the `userId` column generator;

## Example 2[](#example-2)

```ts
import { bloodPressure } from './schema.ts';

async function main() {
  const db = drizzle(...);
  await seed(db, { bloodPressure });
}
main();
```

By running the seeding script above you will see a warning

```plaintext
Column 'userId' in 'bloodPressure' table will be filled with Null values
because you specified neither a table for foreign key on column 'userId' 
nor a function for 'userId' column in refinements.
```

What does it mean?

This means you neither provided the `users` table to the `seed` function schema nor refined the `userId` column generator. As a result, the `userId` column will be filled with Null values.

Then you will have two choices:

-   If you’re okay with filling the `userId` column with Null values, you can ignore the warning;
    
-   Otherwise, you can [refine](drizzle/docs/guides/seeding-with-partially-exposed-tables/index.md#refining-the-userid-column-generator) the `userId` column generator.
    

## Refining the `userId` column generator[](#refining-the-userid-column-generator)

Doing so requires the `users` table to already have IDs such as 1 and 2 in the database.

```ts
import { bloodPressure } from './schema.ts';

async function main() {
  const db = drizzle(...);
  await seed(db, { bloodPressure }).refine((funcs) => ({
    bloodPressure: {
      columns: {
        userId: funcs.valuesFromArray({ values: [1, 2] })
      }
    }
  }));
}
main();
```
