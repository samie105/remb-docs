---
title: "effect-schema"
source: "https://orm.drizzle.team/docs/effect-schema"
canonical_url: "https://orm.drizzle.team/docs/effect-schema"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:57.165Z"
content_hash: "4d726e9f39e9b7f2effaff8433e7e304fc467cb290bd5cf563ba3a8af8f3284c"
menu_path: ["effect-schema"]
section_path: []
nav_prev: {"path": "drizzle/docs/typebox-legacy/index.md", "title": "typebox-legacy"}
nav_next: {"path": "drizzle/docs/prisma/index.md", "title": "Drizzle extension for Prisma"}
---

```
import { pgEnum, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';
import { createInsertSchema, createSelectSchema, createUpdateSchema } from 'drizzle-orm/effect-schema';
import { Schema } from 'effect';

const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name').notNull(),
	email: text('email').notNull(),
	role: text('role', { enum: ['admin', 'user'] }).notNull(),
	createdAt: timestamp('created_at').notNull().defaultNow(),
});

// Schema for inserting a user - can be used to validate API requests
const UserInsert = createInsertSchema(users);

// Schema for updating a user - can be used to validate API requests
const UserUpdate = createUpdateSchema(users);

// Schema for selecting a user - can be used to validate API responses
const UserSelect = createSelectSchema(users);

// Overriding the fields
const UserInsert = createInsertSchema(users, {
	role: Schema.String,
});

// Refining the fields - useful if you want to change the fields before they become nullable/optional in the final schema
const UserInsert = createInsertSchema(users, {
	id: (schema) => schema.pipe(Schema.greaterThanOrEqualTo(0)),
	role: Schema.String,
});

// Usage

const program = Effect.gen(function*() {
	const parsedUser = yield* Schema.validate(UserInsert)({
		name: 'John Doe',
		email: 'johndoe@test.com',
		role: 'admin',
	});
});
```


