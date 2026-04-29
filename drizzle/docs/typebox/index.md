---
title: "typebox"
source: "https://orm.drizzle.team/docs/typebox"
canonical_url: "https://orm.drizzle.team/docs/typebox"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:30:27.379Z"
content_hash: "367bdd24db01292f4ea9a722a4512d99ca1907602bf4f9772d4b18d61ab26963"
menu_path: ["typebox"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/valibot/index.md", "title": "valibot"}
nav_next: {"path": "drizzle/docs/arktype/index.md", "title": "arktype"}
---

```ts
import { pgEnum, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';
import { createInsertSchema, createSelectSchema, createUpdateSchema } from 'drizzle-orm/typebox';
import { Type } from 'typebox';
import { Value } from 'typebox/value';

const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name').notNull(),
	email: text('email').notNull(),
	role: text('role', { enum: ['admin', 'user'] }).notNull(),
	createdAt: timestamp('created_at').notNull().defaultNow(),
});

// Schema for inserting a user - can be used to validate API requests
const insertUserSchema = createInsertSchema(users);

// Schema for updating a user - can be used to validate API requests
const updateUserSchema = createUpdateSchema(users);

// Schema for selecting a user - can be used to validate API responses
const selectUserSchema = createSelectSchema(users);

// Overriding the fields
const insertUserSchema = createInsertSchema(users, {
	role: Type.String(),
});

// Refining the fields - useful if you want to change the fields before they become nullable/optional in the final schema
const insertUserSchema = createInsertSchema(users, {
	id: (schema) => Type.Number({ ...schema, minimum: 0 }),
	role: Type.String(),
});

// Usage

const isUserValid: boolean = Value.Check(insertUserSchema, {
	name: 'John Doe',
	email: 'johndoe@test.com',
	role: 'admin',
});
```
