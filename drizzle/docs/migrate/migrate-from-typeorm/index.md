---
title: "Migrate from TypeORM to Drizzle"
source: "https://orm.drizzle.team/docs/migrate/migrate-from-typeorm"
canonical_url: "https://orm.drizzle.team/docs/migrate/migrate-from-typeorm"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:17:27.993Z"
content_hash: "dd15d247599e455c6b0f18b571d10f18ed6e54b3f1e5da656c5cca7c7f6a58f7"
menu_path: ["Migrate from TypeORM to Drizzle"]
section_path: []
nav_prev: {"path": "drizzle/docs/migrate/migrate-from-sequelize/index.md", "title": "Migrate from Sequelize to Drizzle"}
nav_next: {"path": "drizzle/docs/tutorials/bun-railway-pg/index.md", "title": "Drizzle with Bun and PostgreSQL on Railway"}
---

This guide provides a straightforward approach to migrating a basic **TypeORM** project to **Drizzle ORM**. Although the example focuses on `PostgreSQL`, the process is similar for other supported databases.

Regardless of your application type or API layer, the steps to transition from **TypeORM** to **Drizzle ORM** remain consistent:

These steps are applicable whether you’re developing a REST API (for example, with Express, Koa, or NestJS) or any other type of application that utilizes **TypeORM** for database interactions.

For this guide, we’ll use a REST API built with `Express` as a sample project to migrate to **Drizzle ORM**. It has four entities:

For `many-to-many` relation we will create a join table `order_details`, so `Order` and `Product` entities will have `one-to-many` relations with `OrderDetail` entity.

The corresponding tables have been created using a generated TypeORM migration.

#### Install Drizzle ORM & Drizzle Kit[](#install-drizzle-orm--drizzle-kit)

The first step is to install **Drizzle ORM** and `pg` package which we will use as a driver. The second step is to install **Drizzle Kit** and types for `pg`. [Drizzle Kit](drizzle/docs/kit-overview/index.md) - CLI companion for automatic SQL migrations generation and rapid prototyping.

npm

yarn

pnpm

bun

```
npm i drizzle-orm pg
npm i -D drizzle-kit @types/pg
```

```
yarn add drizzle-orm pg
yarn add -D drizzle-kit @types/pg
```

```
pnpm add drizzle-orm pg
pnpm add -D drizzle-kit @types/pg
```

```
bun add drizzle-orm pg
bun add -D drizzle-kit @types/pg
```

#### Setup Drizzle config file[](#setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by **Drizzle Kit** and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import 'dotenv/config'; // make sure to install dotenv package
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  dialect: 'postgresql',
  out: './src/drizzle',
  schema: './src/drizzle/schema.ts',
  dbCredentials: {
    host: process.env.DB_HOST!,
    port: Number(process.env.DB_PORT!),
    user: process.env.DB_USERNAME!,
    password: process.env.DB_PASSWORD!,
    database: process.env.DB_NAME!,
  },
  // Print all statements
  verbose: true,
  // Always ask for confirmation
  strict: true,
});
```

#### Introspect your database[](#introspect-your-database)

**Drizzle Kit** provides a CLI command to introspect your database and generate a schema file. The schema file contains all the information about your database tables, columns, relations, and indices.

```
npx drizzle-kit introspect
```

This command will generate a schema.ts file, along with snapshots and migrations in the src/drizzle folder.

```
import {
  pgTable,
  serial,
  bigint,
  varchar,
  text,
  foreignKey,
  integer,
  numeric,
  date,
  primaryKey,
} from 'drizzle-orm/pg-core';
import { sql } from 'drizzle-orm';

export const migrations = pgTable('migrations', {
  id: serial('id').primaryKey().notNull(),
  // You can use { mode: "bigint" } if numbers are exceeding js number limitations
  timestamp: bigint('timestamp', { mode: 'number' }).notNull(),
  name: varchar('name').notNull(),
});

export const suppliers = pgTable('suppliers', {
  id: serial('id').primaryKey().notNull(),
  companyName: text('companyName').notNull(),
  city: text('city'),
  country: text('country').notNull(),
});

export const products = pgTable('products', {
  id: serial('id').primaryKey().notNull(),
  name: text('name').notNull(),
  supplierId: integer('supplierId')
    .notNull()
    .references(() => suppliers.id),
  unitPrice: numeric('unitPrice', { precision: 10, scale: 4 }).notNull(),
  unitsInStock: integer('unitsInStock').notNull(),
});

export const orders = pgTable('orders', {
  id: serial('id').primaryKey().notNull(),
  orderDate: date('orderDate').notNull(),
  shippedDate: date('shippedDate'),
  shipAddress: text('shipAddress').notNull(),
  shipPostalCode: text('shipPostalCode'),
  shipCountry: text('shipCountry').notNull(),
});

export const orderDetails = pgTable(
  'order_details',
  {
    orderId: integer('orderId')
      .notNull()
      .references(() => orders.id),
    productId: integer('productId')
      .notNull()
      .references(() => products.id),
    quantity: integer('quantity').notNull(),
  },
  (table) => [
    primaryKey({
      columns: [table.orderId, table.productId],
      name: 'PK_e08ee153eb9c98ee497c1d1287e',
    })
  ],
);
```

Expand

```
-- Current sql file was generated after introspecting the database

CREATE TABLE IF NOT EXISTS "migrations" (
	"id" serial PRIMARY KEY NOT NULL,
	"timestamp" bigint NOT NULL,
	"name" varchar NOT NULL
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "suppliers" (
	"id" serial PRIMARY KEY NOT NULL,
	"companyName" text NOT NULL,
	"city" text,
	"country" text NOT NULL
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "products" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"supplierId" integer NOT NULL,
	"unitPrice" numeric(10, 4) NOT NULL,
	"unitsInStock" integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "orders" (
	"id" serial PRIMARY KEY NOT NULL,
	"orderDate" date NOT NULL,
	"shippedDate" date,
	"shipAddress" text NOT NULL,
	"shipPostalCode" text,
	"shipCountry" text NOT NULL
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "order_details" (
	"orderId" integer NOT NULL,
	"productId" integer NOT NULL,
	"quantity" integer NOT NULL,
	CONSTRAINT PK_e08ee153eb9c98ee497c1d1287e PRIMARY KEY("orderId","productId")
);
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "products" ADD CONSTRAINT "FK_c143cbc0299e1f9220c4b5debd8" FOREIGN KEY ("supplierId") REFERENCES "suppliers"("id") ON DELETE no action ON UPDATE no action;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "order_details" ADD CONSTRAINT "FK_147bc15de4304f89a93c7eee969" FOREIGN KEY ("orderId") REFERENCES "orders"("id") ON DELETE no action ON UPDATE no action;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "order_details" ADD CONSTRAINT "FK_c67ebaba3e5085b6401911acc70" FOREIGN KEY ("productId") REFERENCES "products"("id") ON DELETE no action ON UPDATE no action;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
```

Expand

Also, if you want to use relational queries, you have to update your schema file with relational tables:

```
// ...other imports
import { relations } from 'drizzle-orm';

// ...other tables 
export const suppliersRelations = relations(suppliers, ({ many }) => ({
  products: many(products),
}));

export const productsRelations = relations(products, ({ one, many }) => ({
  supplier: one(suppliers, { fields: [products.supplierId], references: [suppliers.id] }),
  orderDetails: many(orderDetails),
}));

export const ordersRelations = relations(orders, ({ many }) => ({
  orderDetails: many(orderDetails),
}));

export const orderDetailsRelations = relations(orderDetails, ({ one }) => ({
  order: one(orders, { fields: [orderDetails.orderId], references: [orders.id] }),
  product: one(products, { fields: [orderDetails.productId], references: [products.id] }),
}));
```

Now we have the following file structure:

```
📦 <project root>
 ├ 📂 src
 │  ├ 📂 drizzle
 │  │  ├ 📂 meta
 |  |  |  ├ 📜 _journal.json
 │  │  │  └ 📜 0000_snapshot.json
 │  │  ├ 📜 0000_lush_lenny_balinger.sql
 │  │  └ 📜 schema.ts
 │  ├ 📂 routers
 │  │  ├ 📜 order.router.ts
 │  │  ├ 📜 product.router.ts
 │  │  └ 📜 supplier.router.ts
 │  ├ 📂 controllers
 │  │  ├ 📜 order.controller.ts
 │  │  ├ 📜 product.controller.ts
 │  │  └ 📜 supplier.controller.ts
 │  ├ 📜 index.ts
 │  └ 📜 server.ts
 ├ 📜 package.json
 ├ 📜 drizzle.config.ts
 └ 📜 tsconfig.json
```

#### Connect Drizzle ORM to your database[](#connect-drizzle-orm-to-your-database)

Create a `db.ts` file in the `src/drizzle` folder and set up your database configuration:

```
import { drizzle } from 'drizzle-orm/node-postgres';
import { Client } from 'pg';
import * as schema from './schema';

export const client = new Client({
  host: process.env.DB_HOST!,
  port: Number(process.env.DB_PORT!),
  user: process.env.DB_USERNAME!,
  password: process.env.DB_PASSWORD!,
  database: process.env.DB_NAME!,
});

// { schema } is used for relational queries
export const db = drizzle({ client, schema });
```

```
import 'dotenv/config';
import { client, db } from './drizzle/db';
import { resolve } from 'node:path';
import { migrate } from 'drizzle-orm/node-postgres/migrator';

(async () => {
  await client.connect();

  // This command run all migrations from the migrations folder and apply changes to the database
  await migrate(db, { migrationsFolder: resolve(__dirname, './drizzle') });

  // ... start your application
})();
```

#### Transition your TypeORM queries to Drizzle ORM queries[](#transition-your-typeorm-queries-to-drizzle-orm-queries)

In this section, we will show you how to replace several queries from **TypeORM** with **Drizzle ORM**.

##### Replace insert queries[](#replace-insert-queries)

We will show how to insert new rows into `suppliers` and `products` tables.

1.  `POST /suppliers`

```
import dataSource from '../db/typeorm.config';
import { Supplier } from '../entities/supplier.entity';

const repository = dataSource.getRepository(Supplier);

const suppliers = repository.create([
  {
    companyName: 'TestCompanyName1',
    city: 'TestCity1',
    country: 'TestCountry1',
  },
  {
    companyName: 'TestCompanyName2',
    city: 'TestCity2',
    country: 'TestCountry2',
  },
]);

await repository.save(suppliers);
```

With **Drizzle ORM**, the query is implemented as follows:

```
import { db } from '../drizzle/db';
import { suppliers } from '../drizzle/schema';

await db.insert(suppliers).values([
  {
    companyName: 'TestCompanyName1',
    city: 'TestCity1',
    country: 'TestCountry1',
  },
  {
    companyName: 'TestCompanyName2',
    city: 'TestCity2',
    country: 'TestCountry2',
  },
]);
```

2.  `POST /products`

```
import dataSource from '../db/typeorm.config';
import { Product } from '../entities/product.entity';

const repository = dataSource.getRepository(Product);

const products = repository.create([
  {
    name: 'TestProductName1',
    supplierId: 1,
    unitPrice: 10,
    unitsInStock: 20,
  },
  {
    name: 'TestProductName2',
    supplierId: 1,
    unitPrice: 25,
    unitsInStock: 7,
  },
  {
    name: 'TestProductName3',
    supplierId: 2,
    unitPrice: 50,
    unitsInStock: 17,
  },
  {
    name: 'TestProductName4',
    supplierId: 2,
    unitPrice: 100,
    unitsInStock: 2,
  },
]);

await repository.save(products);
```

With **Drizzle ORM**, the query is implemented as follows:

Be careful with the `unitPrice` field. In **TypeORM** it’s a `number` type, but in **Drizzle ORM** it’s a `string` type, which can handle more than 16383 digits after the decimal point, unlike the `number` type.

```
await db.insert(products).values([
  {
    name: 'TestProductName1',
    supplierId: 1,
    unitPrice: '10',
    unitsInStock: 20,
  },
  {
    name: 'TestProductName2',
    supplierId: 1,
    unitPrice: '25',
    unitsInStock: 7,
  },
  {
    name: 'TestProductName3',
    supplierId: 2,
    unitPrice: '50',
    unitsInStock: 17,
  },
  {
    name: 'TestProductName4',
    supplierId: 2,
    unitPrice: '100',
    unitsInStock: 2,
  },
]);
```

##### Replace select queries[](#replace-select-queries)

In this section we will show how to select one row, multiple rows, count rows, filter rows, join tables and paginate results.

1.  `GET /products/:id`

In **TypeORM**, the response type is not strictly typed. For example, if you choose to include a relation or select only a few fields instead of all, these modifications will not be reflected in the response type.

```
import dataSource from '../db/typeorm.config';
import { Product } from '../entities/product.entity';

const { id } = req.params;

const repository = dataSource.getRepository(Product);

const response = await repostitory.findOne({
  where: { id },
  relations: ['supplier'],
});
```

In **Drizzle ORM**, the query is implemented as follows:

```
import { eq } from 'drizzle-orm';
import { db } from '../drizzle/db';
import { products, suppliers } from '../drizzle/schema';

const { id } = req.params;

const response = await db
  .select({
    product: products,
    supplier: suppliers,
  })
  .from(products)
  .where(eq(products.id, id))
  .leftJoin(suppliers, eq(suppliers.id, products.supplierId));

// or you can use relational queries
const response = await db.query.products.findFirst({
  where: (products, { eq }) => eq(products.id, id),
  with: {
    supplier: true,
  },
});
```

In **Drizzle ORM**, the response type will match precisely what is specified in the select object, so including the `supplier` relation is fully type-safe.

```
// response type
const response: {
  product: {
    name: string;
    id: number;
    supplierId: number;
    unitPrice: string;
    unitsInStock: number;
  };
  supplier: {
    id: number;
    companyName: string;
    city: string | null;
    country: string;
  } | null;
}[]
```

2.  `GET /products`

In **TypeORM**, the result is not type-safe as it doesn’t specify the fields you want to select.

```
import { ILike } from 'typeorm';
import dataSource from '../db/typeorm.config';
import { Product } from '../entities/product.entity';

const repository = dataSource.getRepository(Product);

const response = await repostitory.findAndCount({
  skip: 0,
  take: 10,
  where: {
    name: ILike(`%test%`),
  },
  select: ['id', 'name', 'unitPrice', 'unitsInStock'],
});
```

In **Drizzle ORM**, the query is implemented as follows:

```
import { ilike, sql } from 'drizzle-orm';
import { db } from '../drizzle/db';
import { products } from '../drizzle/schema';

const whereOptions = ilike(products.name, `%test%`);

const [response, count] = await Promise.all([
  db
    .select({
      id: products.id,
      name: products.name,
      unitPrice: products.unitPrice,
      unitsInStock: products.unitsInStock,
    })
    .from(products)
    .where(whereOptions)
    .offset(0)
    .limit(10),
  db
    .select({ count: sql<number>`cast(count(${products.id}) as integer)` })
    .from(products)
    .where(whereOptions),
]);

// or you can use relational queries
const whereOptions = ilike(products.name, `%test%`);

const [response, count] = await Promise.all([
  db.query.products.findMany({
    where: whereOptions,
    columns: {
      id: true,
      name: true,
      unitPrice: true,
      unitsInStock: true,
    },
    offset: 0,
    limit: 10,
  }),
  db
    .select({ count: sql<number>`cast(count(${products.id}) as integer)` })
    .from(products)
    .where(whereOptions),
]);
```

Expand

In **Drizzle ORM**, the result is strictly type-safe, meaning the fields you select are explicitly defined.

```
// response type
const response: {
  id: number;
  name: string;
  unitPrice: string;
  unitsInStock: number;
}[]
```

3.  `GET /orders/:id`

In **TypeORM** you can’t use `aggregation functions` with relations and select specific fields using method `findOne`. So, you have to use `querybuilder`, which is not type-safe as well.

We want to select `id`, `orderDate` and `shipCountry` fields from `orders` table and by using `aggregation functions` sum `totalPrice` of order, `totalQuantity` of products in the order and count `totalProducts` in the order.

```
import dataSource from '../db/typeorm.config';
import { Order } from '../entities/order.entity';

const { id } = req.params;

const orderRepository = dataSource.getRepository(Order);

const orderQueryBuilder = orderRepository.createQueryBuilder('order');

const response = await orderQueryBuilder
  .select([
    'order.id as id',
    'order.orderDate as "orderDate"',
    'order.shipCountry as "shipCountry"',
    'SUM(product.unitPrice * detail.quantity)::float as "totalPrice"',
    'SUM(detail.quantity)::int as "totalQuantity"',
    'COUNT(detail.productId)::int as "totalProducts"',
  ])
  .leftJoin('order.orderDetails', 'detail')
  .leftJoin('detail.product', 'product')
  .groupBy('order.id')
  .where('order.id = :id', { id })
  .getRawOne();
```

In **Drizzle ORM**, the query is implemented as follows:

```
import { eq, sql } from 'drizzle-orm';
import { db } from '../drizzle/db';
import { orders, orderDetails, products } from '../drizzle/schema';

const { id } = req.params;

const response = await db
      .select({
        id: orders.id,
        shipCountry: orders.shipCountry,
        orderDate: orders.orderDate,
        totalPrice: sql<number>`cast(sum(${orderDetails.quantity} * ${products.unitPrice}) as float)`,
        totalQuantity: sql<number>`cast(sum(${orderDetails.quantity}) as int)`,
        totalProducts: sql<number>`cast(count(${orderDetails.productId}) as int)`,
      })
      .from(orders)
      .where(eq(orders.id, id))
      .groupBy(orders.id)
      .leftJoin(orderDetails, eq(orderDetails.orderId, orders.id))
      .leftJoin(products, eq(products.id, orderDetails.productId));
```

In **Drizzle ORM**, the result will be type-safe with aggregations too.

```
// response type
const response: {
  id: number;
  shipCountry: string;
  orderDate: string;
  totalPrice: number;
  totalQuantity: number;
  totalProducts: number;
}[]
```

**Note:** as of now aggregations are not supported in relational queries, so you have to use `core queries`.

##### Replace update queries[](#replace-update-queries)

In this section, we will show you how to update multiple rows.

1.  `PATCH /suppliers/:id`

```
import dataSource from '../db/typeorm.config';
import { Supplier } from '../entities/supplier.entity';

const { id } = req.params;

const repository = dataSource.getRepository(Supplier);

const supplier = await repository.findOneBy({ id });
if (!supplier) {
  throw new Error('Supplier not found');
}

supplier.city = 'TestCity1Updated';
supplier.country = 'TestCountry1Updated';

await repository.save(supplier);
```

In **Drizzle ORM**, the query is implemented as follows:

```
import { eq } from 'drizzle-orm';
import { db } from '../drizzle/db';
import { suppliers } from '../drizzle/schema';

const { id } = req.params;

await db
    .update(suppliers)
    .set({
      city: 'TestCity1Updated',
      country: 'TestCountry1Updated',
    })
    .where(eq(suppliers.id, id));
```

##### Replace delete queries[](#replace-delete-queries)

In this section, we will show you how to delete a single row and multiple rows using transactions.

1.  `DELETE /orders/:id`

```
import dataSource from '../db/typeorm.config';
import { OrderDetail } from '../entities/order-detail.entity';
import { Order } from '../entities/order.entity';

const { id } = req.params;

const queryRunner = dataSource.createQueryRunner();

await queryRunner.connect();

await queryRunner.startTransaction();

try {
  await queryRunner.manager.delete(OrderDetail, { orderId: id });

  await queryRunner.manager.delete(Order, { id });

  await queryRunner.commitTransaction();
} catch (e) {
  await queryRunner.rollbackTransaction();

  console.error(e);
} finally {
  await queryRunner.release();
}
```

In **Drizzle ORM**, the query is implemented as follows:

```
import { eq } from 'drizzle-orm';
import { db } from '../drizzle/db';
import { orderDetails, orders } from '../drizzle/schema';

const { id } = req.params;

try {
  await db.transaction(async (tx) => {
    await tx.delete(orderDetails).where(eq(orderDetails.orderId, id));

    await tx.delete(orders).where(eq(orders.id, id));
  });
} catch (e) {
  console.error(e);
}
```
