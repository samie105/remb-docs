---
title: "Get Started with Drizzle and SQLite Durable Objects"
source: "https://orm.drizzle.team/docs/get-started/do-new"
canonical_url: "https://orm.drizzle.team/docs/get-started/do-new"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:47.631Z"
content_hash: "339976b15e1ce52c329b7a5bc8c5fd658d0008c159b460cdb1ced4cb9b4603c5"
menu_path: ["Get Started with Drizzle and SQLite Durable Objects"]
section_path: []
nav_prev: {"path": "drizzle/docs/get-started/d1-new/index.md", "title": "Get Started with Drizzle and D1"}
nav_next: {"path": "drizzle/docs/get-started/do-existing/index.md", "title": "Get Started with Drizzle and SQLite Durable Objects in existing project"}
---

# Bind a Durable Object. Durable objects are a scale-to-zero compute primitive based on the actor model.
# Durable Objects can live for as long as needed. Use these when you need a long-running "server", such as in realtime apps.
# Docs: https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects
[[durable_objects.bindings]]
name = "MY_DURABLE_OBJECT"
class_name = "MyDurableObject"

# Durable Object migrations.
# Docs: https://developers.cloudflare.com/workers/wrangler/configuration/#migrations
[[migrations]]
tag = "v1"
new_sqlite_classes = ["MyDurableObject"]

# We need rules so we can import migrations in the next steps
[[rules]] 
type = "Text"
globs = ["**/*.sql"]
fallthrough = true
```

#### Step 3 - Connect Drizzle ORM to the database[](#step-3---connect-drizzle-orm-to-the-database)

```
import { drizzle, type DrizzleSqliteDODatabase } from 'drizzle-orm/durable-sqlite';
import { DurableObject } from 'cloudflare:workers'

export class MyDurableObject extends DurableObject {
	storage: DurableObjectStorage;
	db: DrizzleSqliteDODatabase;

	constructor(ctx: DurableObjectState, env: Env) {
		super(ctx, env);
		this.storage = ctx.storage;
		this.db = drizzle(this.storage, { logger: false });
	}
}
```

#### Step 4 - Generate wrangler types[](#step-4---generate-wrangler-types)

npm

yarn

pnpm

bun

```
npx wrangler types
```

```
yarn wrangler types
```

```
pnpm wrangler types
```

```
bunx wrangler types
```

The output of this command will be a `worker-configuration.d.ts` file.

#### Step 5 - Create a table[](#step-5---create-a-table)

Create a `schema.ts` file in the `src/db` directory and declare your table:

```
import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable("users_table", {
  id: int().primaryKey({ autoIncrement: true }),
  name: text().notNull(),
  age: int().notNull(),
  email: text().notNull().unique(),
});
```

#### Step 6 - Setup Drizzle config file[](#step-6---setup-drizzle-config-file)

**Drizzle config** - a configuration file that is used by [Drizzle Kit](drizzle/docs/kit-overview/index.md) and contains all the information about your database connection, migration folder and schema files.

Create a `drizzle.config.ts` file in the root of your project and add the following content:

```
import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './src/db/schema.ts',
  dialect: 'sqlite',
  driver: 'durable-sqlite',
});
```

#### Step 7 - Applying changes to the database[](#step-7---applying-changes-to-the-database)

Generate migrations:

```
npx drizzle-kit generate
```

You can apply migrations only from Cloudflare Workers. To achieve this, let’s define the migrate functionality in MyDurableObject:

```
import { drizzle, type DrizzleSqliteDODatabase } from 'drizzle-orm/durable-sqlite';
import { DurableObject } from 'cloudflare:workers'
import { migrate } from 'drizzle-orm/durable-sqlite/migrator';
import migrations from '../drizzle/migrations';

export class MyDurableObject extends DurableObject {
	storage: DurableObjectStorage;
	db: DrizzleSqliteDODatabase;

	constructor(ctx: DurableObjectState, env: Env) {
		super(ctx, env);
		this.storage = ctx.storage;
		this.db = drizzle(this.storage, { logger: false });
	}

	async migrate() {
		migrate(this.db, migrations);
	}
}
```

#### Step 8 - Migrate and Query the database[](#step-8---migrate-and-query-the-database)

```
import { drizzle, DrizzleSqliteDODatabase } from 'drizzle-orm/durable-sqlite';
import { DurableObject } from 'cloudflare:workers'
import { migrate } from 'drizzle-orm/durable-sqlite/migrator';
import migrations from '../drizzle/migrations';
import { usersTable } from './db/schema';

export class MyDurableObject extends DurableObject {
	storage: DurableObjectStorage;
	db: DrizzleSqliteDODatabase<any>;

	constructor(ctx: DurableObjectState, env: Env) {
		super(ctx, env);
		this.storage = ctx.storage;
		this.db = drizzle(this.storage, { logger: false });

		// Make sure all migrations complete before accepting queries.
		// Otherwise you will need to run `this.migrate()` in any function
		// that accesses the Drizzle database `this.db`.
		ctx.blockConcurrencyWhile(async () => {
			await this._migrate();
		});
	}

	async insertAndList(user: typeof usersTable.$inferInsert) {
		await this.insert(user);
		return this.select();
	}

	async insert(user: typeof usersTable.$inferInsert) {
		await this.db.insert(usersTable).values(user);
	}

	async select() {
		return this.db.select().from(usersTable);
	}

	async _migrate() {
		migrate(this.db, migrations);
	}
}

export default {
	/**
	 * This is the standard fetch handler for a Cloudflare Worker
	 *
	 * @param request - The request submitted to the Worker from the client
	 * @param env - The interface to reference bindings declared in wrangler.toml
	 * @param ctx - The execution context of the Worker
	 * @returns The response to be sent back to the client
	 */
	async fetch(request: Request, env: Env): Promise<Response> {
		const id: DurableObjectId = env.MY_DURABLE_OBJECT.idFromName('durable-object');
		const stub = env.MY_DURABLE_OBJECT.get(id);

		// Option A - Maximum performance.
		// Prefer to bundle all the database interaction within a single Durable Object call
		// for maximum performance, since database access is fast within a DO.
		const usersAll = await stub.insertAndList({
			name: 'John',
			age: 30,
			email: 'john@example.com',
		});
		console.log('New user created. Getting all users from the database: ', users);

		// Option B - Slow but maybe useful sometimes for debugging.
		// You can also directly call individual Drizzle queries if they are exposed
		// but keep in mind every query is a round-trip to the Durable Object instance.
		await stub.insert({
			name: 'John',
			age: 30,
			email: 'john@example.com',
		});
		console.log('New user created!');
	
		const users = await stub.select();
		console.log('Getting all users from the database: ', users);

		return Response.json(users);
	}
}
```
