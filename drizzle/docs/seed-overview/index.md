---
title: "Drizzle Seed"
source: "https://orm.drizzle.team/docs/seed-overview"
canonical_url: "https://orm.drizzle.team/docs/seed-overview"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:20:34.789Z"
content_hash: "400463c982b530b5758b25d05f4aa2f03da4d93089ecd7e86a348d63030f699b"
menu_path: ["Drizzle Seed"]
section_path: []
---
## Drizzle Seed

PostgreSQL

SQLite

MySQL

SingleStore

CockroachDB

MS SQL

IMPORTANT

`drizzle-seed` can only be used with `drizzle-orm@0.36.4` or higher. Versions lower than this may work at runtime but could have type issues and identity column issues, as this patch was introduced in `drizzle-orm@0.36.4`

`drizzle-seed` is a TypeScript library that helps you generate deterministic, yet realistic, fake data to populate your database. By leveraging a seedable pseudorandom number generator (pRNG), it ensures that the data you generate is consistent and reproducible across different runs. This is especially useful for testing, development, and debugging purposes.

#### What is Deterministic Data Generation?[](#what-is-deterministic-data-generation)

Deterministic data generation means that the same input will always produce the same output. In the context of `drizzle-seed`, when you initialize the library with the same seed number, it will generate the same sequence of fake data every time. This allows for predictable and repeatable data sets.

#### Pseudorandom Number Generator (pRNG)[](#pseudorandom-number-generator-prng)

A pseudorandom number generator is an algorithm that produces a sequence of numbers that approximates the properties of random numbers. However, because it’s based on an initial value called a seed, you can control its randomness. By using the same seed, the pRNG will produce the same sequence of numbers, making your data generation process reproducible.

#### Benefits of Using a pRNG:[](#benefits-of-using-a-prng)

*   Consistency: Ensures that your tests run on the same data every time.
*   Debugging: Makes it easier to reproduce and fix bugs by providing a consistent data set.
*   Collaboration: Team members can share seed numbers to work with the same data sets.

With drizzle-seed, you get the best of both worlds: the ability to generate realistic fake data and the control to reproduce it whenever needed.

## Installation[](#installation)

npm

yarn

pnpm

bun

```
npm i drizzle-seed
```

```
yarn add drizzle-seed
```

```
pnpm add drizzle-seed
```

```
bun add drizzle-seed
```

## Basic Usage[](#basic-usage)

In this example we will create 10 users with random names and ids

```
import { pgTable, integer, text } from "drizzle-orm/pg-core";
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";

const users = pgTable("users", {
  id: integer().primaryKey(),
  name: text().notNull(),
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);
  await seed(db, { users });
}

main();
```

## Options[](#options)

**`count`**

By default, the `seed` function will create 10 entities. However, if you need more for your tests, you can specify this in the seed options object

```
await seed(db, schema, { count: 1000 });
```

**`seed`**

If you need a seed to generate a different set of values for all subsequent runs, you can define a different number in the `seed` option. Any new number will generate a unique set of values

```
await seed(db, schema, { seed: 12345 });
```

## Reset database[](#reset-database)

With `drizzle-seed`, you can easily reset your database and seed it with new values, for example, in your test suites

```
// path to a file with schema you want to reset
import * as schema from "./schema.ts";
import { reset } from "drizzle-seed";

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);
  await reset(db, schema);
}

main();
```

Different dialects will have different strategies for database resetting

PostgreSQL

MySQL

SQLite

SingleStore

CockroachDB

MS SQL

For PostgreSQL, the `drizzle-seed` package will generate `TRUNCATE` statements with the `CASCADE` option to ensure that all tables are empty after running the reset function

```
TRUNCATE tableName1, tableName2, ... CASCADE;
```

For MySQL, the `drizzle-seed` package will first disable `FOREIGN_KEY_CHECKS` to ensure the next step won’t fail, and then generate `TRUNCATE` statements to empty the content of all tables

```
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE tableName1;
TRUNCATE tableName2;
...
SET FOREIGN_KEY_CHECKS = 1;
```

For SQLite, the `drizzle-seed` package will first disable the `foreign_keys` pragma to ensure the next step won’t fail, and then generate `DELETE FROM` statements to empty the content of all tables

```
PRAGMA foreign_keys = OFF;
DELETE FROM tableName1;
DELETE FROM tableName2;
...
PRAGMA foreign_keys = ON;
```

For SingleStore, the `drizzle-seed` package will first disable `FOREIGN_KEY_CHECKS` to ensure the next step won’t fail, and then generate `TRUNCATE` statements to empty the content of all tables

```
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE tableName1;
TRUNCATE tableName2;
...
SET FOREIGN_KEY_CHECKS = 1;
```

For CockroachDB, the `drizzle-seed` package will generate `TRUNCATE` statements with the `CASCADE` option to ensure that all tables are empty after running the reset function

```
TRUNCATE tableName1, tableName2, ... CASCADE;
```

For MS SQL, the `drizzle-seed` package first gathers information about all foreign key constraints that reference or are contained in the tables specified as the second argument(your schema) to the `reset` function.

It then iterates over those tables, drops all foreign key constraints related to each table, and truncates each table.

Finally, the package recreates the original foreign key constraints for each table.

```
-- gather information about all fk constraints

-- drops all fk constraints related to each table
ALTER TABLE [<schemaName>].[<tableName>] DROP CONSTRAINT [<fkName>];

-- truncates each table
TRUNCATE TABLE [<schemaName>].[<tableName>];

-- recreates the original fk constraints
ALTER TABLE [<schemaName>].[<tableName>] 
ADD CONSTRAINT [<fkName>] 
FOREIGN KEY([<columnName>])
REFERENCES [<refSchemaName>].[<refTableName>] ([<refColumnName>])
ON DELETE <onDeleteAction>
ON UPDATE <onUpdateAction>;
```

## Refinements[](#refinements)

In case you need to change the behavior of the seed generator functions that `drizzle-seed` uses by default, you can specify your own implementation and even use your own list of values for the seeding process

`.refine` is a callback that receives a list of all available generator functions from `drizzle-seed`. It should return an object with keys representing the tables you want to refine, defining their behavior as needed. Each table can specify several properties to simplify seeding your database:

*   `columns`: Refine the default behavior of each column by specifying the required generator function.
*   `count`: Specify the number of rows to insert into the database. By default, it’s 10. If a global count is defined in the `seed()` options, the count defined here will override it for this specific table.
*   `with`: Define how many referenced entities to create for each parent table if you want to generate associated entities.

info

You can also specify a weighted random distribution for the number of referenced values you want to create. For details on this API, you can refer to [Weighted Random docs](#weighted-random) docs section

**API**

```
await seed(db, schema).refine((f) => ({
  users: {
    columns: {},
    count: 10,
    with: {
        posts: 10
    }
  },
}));
```

Let’s check a few examples with an explanation of what will happen:

```
import { pgTable, integer, text } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: integer().primaryKey(),
  name: text().notNull(),
});

export const posts = pgTable("posts", {
  id: integer().primaryKey(),
  description: text(),
  userId: integer().references(() => users.id),
});
```

**Example 1**: Seed only the `users` table with 20 entities and with refined seed logic for the `name` column

```
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";
import * as schema from './schema.ts'

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { users: schema.users }).refine((f) => ({
    users: {
        columns: {
            name: f.fullName(),
        },
        count: 20
    }
  }));
}

main();
```

**Example 2**: Seed the `users` table with 20 entities and add 10 `posts` for each `user` by seeding the `posts` table and creating a reference from `posts` to `users`

```
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";
import * as schema from './schema.ts'

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, schema).refine((f) => ({
    users: {
        count: 20,
        with: {
            posts: 10
        }
    }
  }));
}

main();
```

**Example 3**: Seed the `users` table with 5 entities and populate the database with 100 `posts` without connecting them to the `users` entities. Refine `id` generation for `users` so that it will give any int from `10000` to `20000` and remains unique, and refine `posts` to retrieve values from a self-defined array

```
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";
import * as schema from './schema.ts'

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, schema).refine((f) => ({
    users: {
        count: 5,
        columns: {
            id: f.int({
              minValue: 10000,
              maxValue: 20000,
              isUnique: true,
            }),
        }
    },
    posts: {
        count: 100,
        columns: {
            description: f.valuesFromArray({
            values: [
                "The sun set behind the mountains, painting the sky in hues of orange and purple", 
                "I can't believe how good this homemade pizza turned out!", 
                "Sometimes, all you need is a good book and a quiet corner.", 
                "Who else thinks rainy days are perfect for binge-watching old movies?", 
                "Tried a new hiking trail today and found the most amazing waterfall!",
                // ...
            ],
          })
        }
    }
  }));
}

main();
```

IMPORTANT

There are many more possibilities that we will define in these docs, but for now, you can explore a few sections in this documentation. Check the [Generators](https://orm.drizzle.team/docs/seed-functions) section to get familiar with all the available generator functions you can use.

A particularly great feature is the ability to use weighted randomization, both for generator values created for a column and for determining the number of related entities that can be generated by `drizzle-seed`.

Please check [Weighted Random docs](#weighted-random) for more info.

## Weighted Random[](#weighted-random)

There may be cases where you need to use multiple datasets with a different priority that should be inserted into your database during the seed stage. For such cases, drizzle-seed provides an API called weighted random

The Drizzle Seed package has a few places where weighted random can be used:

*   Columns inside each table refinements
*   The `with` property, determining the amount of related entities to be created

Let’s check an example for both:

```
import { pgTable, integer, text, varchar, doublePrecision } from "drizzle-orm/pg-core";

export const orders = pgTable(
  "orders",
  {
    id: integer().primaryKey(),
    name: text().notNull(),
    quantityPerUnit: varchar().notNull(),
    unitPrice: doublePrecision().notNull(),
    unitsInStock: integer().notNull(),
    unitsOnOrder: integer().notNull(),
    reorderLevel: integer().notNull(),
    discontinued: integer().notNull(),
  }
);

export const details = pgTable(
  "details",
  {
    unitPrice: doublePrecision().notNull(),
    quantity: integer().notNull(),
    discount: doublePrecision().notNull(),

    orderId: integer()
      .notNull()
      .references(() => orders.id, { onDelete: "cascade" }),
  }
);
```

**Example 1**: Refine the `unitPrice` generation logic to generate `5000` random prices, with a 30% chance of prices between 10-100 and a 70% chance of prices between 100-300

```
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";
import * as schema from './schema.ts'

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, schema).refine((f) => ({
    orders: {
       count: 5000,
       columns: {
           unitPrice: f.weightedRandom(
               [
                   {
                       weight: 0.3,
                       value: funcs.int({ minValue: 10, maxValue: 100 })
                   },
                   {
                       weight: 0.7,
                       value: funcs.number({ minValue: 100, maxValue: 300, precision: 100 })
                   }
               ]
           ),
       }
    }
  }));
}

main();
```

**Example 2**: For each order, generate 1 to 3 details with a 60% chance, 5 to 7 details with a 30% chance, and 8 to 10 details with a 10% chance

```
import { drizzle } from "drizzle-orm/node-postgres";
import { seed } from "drizzle-seed";
import * as schema from './schema.ts'

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, schema).refine((f) => ({
    orders: {
       with: {
           details:
               [
                   { weight: 0.6, count: [1, 2, 3] },
                   { weight: 0.3, count: [5, 6, 7] },
                   { weight: 0.1, count: [8, 9, 10] },
               ]
       }
    }
  }));
}

main();
```

## Complex example[](#complex-example)

main.ts

schema.ts

```
import { seed } from "drizzle-seed";
import * as schema from "./schema.ts";

const main = async () => {
    const titlesOfCourtesy = ["Ms.", "Mrs.", "Dr."];
    const unitsOnOrders = [0, 10, 20, 30, 50, 60, 70, 80, 100];
    const reorderLevels = [0, 5, 10, 15, 20, 25, 30];
    const quantityPerUnit = [
        "100 - 100 g pieces",
        "100 - 250 g bags",
        "10 - 200 g glasses",
        "10 - 4 oz boxes",
        "10 - 500 g pkgs.",
        "10 - 500 g pkgs."
    ];
    const discounts = [0.05, 0.15, 0.2, 0.25];

    await seed(db, schema).refine((funcs) => ({
        customers: {
            count: 10000,
            columns: {
                companyName: funcs.companyName(),
                contactName: funcs.fullName(),
                contactTitle: funcs.jobTitle(),
                address: funcs.streetAddress(),
                city: funcs.city(),
                postalCode: funcs.postcode(),
                region: funcs.state(),
                country: funcs.country(),
                phone: funcs.phoneNumber({ template: "(###) ###-####" }),
                fax: funcs.phoneNumber({ template: "(###) ###-####" })
            }
        },
        employees: {
            count: 200,
            columns: {
                firstName: funcs.firstName(),
                lastName: funcs.lastName(),
                title: funcs.jobTitle(),
                titleOfCourtesy: funcs.valuesFromArray({ values: titlesOfCourtesy }),
                birthDate: funcs.date({ minDate: "2010-12-31", maxDate: "2010-12-31" }),
                hireDate: funcs.date({ minDate: "2010-12-31", maxDate: "2024-08-26" }),
                address: funcs.streetAddress(),
                city: funcs.city(),
                postalCode: funcs.postcode(),
                country: funcs.country(),
                homePhone: funcs.phoneNumber({ template: "(###) ###-####" }),
                extension: funcs.int({ minValue: 428, maxValue: 5467 }),
                notes: funcs.loremIpsum()
            }
        },
        orders: {
            count: 50000,
            columns: {
                shipVia: funcs.int({ minValue: 1, maxValue: 3 }),
                freight: funcs.number({ minValue: 0, maxValue: 1000, precision: 100 }),
                shipName: funcs.streetAddress(),
                shipCity: funcs.city(),
                shipRegion: funcs.state(),
                shipPostalCode: funcs.postcode(),
                shipCountry: funcs.country()
            },
            with: {
                details:
                    [
                        { weight: 0.6, count: [1, 2, 3, 4] },
                        { weight: 0.2, count: [5, 6, 7, 8, 9, 10] },
                        { weight: 0.15, count: [11, 12, 13, 14, 15, 16, 17] },
                        { weight: 0.05, count: [18, 19, 20, 21, 22, 23, 24, 25] },
                    ]
            }
        },
        suppliers: {
            count: 1000,
            columns: {
                companyName: funcs.companyName(),
                contactName: funcs.fullName(),
                contactTitle: funcs.jobTitle(),
                address: funcs.streetAddress(),
                city: funcs.city(),
                postalCode: funcs.postcode(),
                region: funcs.state(),
                country: funcs.country(),
                phone: funcs.phoneNumber({ template: "(###) ###-####" })
            }
        },
        products: {
            count: 5000,
            columns: {
                name: funcs.companyName(),
                quantityPerUnit: funcs.valuesFromArray({ values: quantityPerUnit }),
                unitPrice: funcs.weightedRandom(
                    [
                        {
                            weight: 0.5,
                            value: funcs.int({ minValue: 3, maxValue: 300 })
                        },
                        {
                            weight: 0.5,
                            value: funcs.number({ minValue: 3, maxValue: 300, precision: 100 })
                        }
                    ]
                ),
                unitsInStock: funcs.int({ minValue: 0, maxValue: 125 }),
                unitsOnOrder: funcs.valuesFromArray({ values: unitsOnOrders }),
                reorderLevel: funcs.valuesFromArray({ values: reorderLevels }),
                discontinued: funcs.int({ minValue: 0, maxValue: 1 })
            }
        },
        details: {
            columns: {
                unitPrice: funcs.number({ minValue: 10, maxValue: 130 }),
                quantity: funcs.int({ minValue: 1, maxValue: 130 }),
                discount: funcs.weightedRandom(
                    [
                        { weight: 0.5, value: funcs.valuesFromArray({ values: discounts }) },
                        { weight: 0.5, value: funcs.default({ defaultValue: 0 }) }
                    ]
                )
            }
        }
    }));
}

main();
```

## Limitations[](#limitations)

#### Types limitations for `with`[](#types-limitations-for-with)

Due to certain TypeScript limitations and the current API in Drizzle, it is not possible to properly infer references between tables, especially when circular dependencies between tables exist.

This means the `with` option will display all tables in the schema, and you will need to manually select the one that has a one-to-many relationship

warning

The `with` option works for one-to-many relationships. For example, if you have one `user` and many `posts`, you can use users `with` posts, but you cannot use posts `with` users

#### Type limitations for the third parameter in Drizzle tables:[](#type-limitations-for-the-third-parameter-in-drizzle-tables)

Currently, we do not have type support for the third parameter in Drizzle tables. While it will work at runtime, it will not function correctly at the type level
