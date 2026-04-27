---
title: "Drizzle ORM - Select parent rows with at least one related child row"
source: "https://orm.drizzle.team/docs/guides/select-parent-rows-with-at-least-one-related-child-row"
canonical_url: "https://orm.drizzle.team/docs/guides/select-parent-rows-with-at-least-one-related-child-row"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:03:09.285Z"
content_hash: "a47344e95778cc5560a5a924568e205ffa201ea5641a3e919f45560f517e325f"
menu_path: ["Drizzle ORM - Select parent rows with at least one related child row"]
section_path: []
content_language: "en"
---
Drizzle | Select parent rows with at least one related child row

This guide demonstrates how to select parent rows with the condition of having at least one related child row. Below, there are examples of schema definitions and the corresponding database data:

```ts
import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull(),
});

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  userId: integer('user_id').notNull().references(() => users.id),
});
```

```plaintext
+----+------------+----------------------+
| id |    name    |        email         |
+----+------------+----------------------+
|  1 | John Doe   | john_doe@email.com   |
+----+------------+----------------------+
|  2 | Tom Brown  | tom_brown@email.com  |
+----+------------+----------------------+
|  3 | Nick Smith | nick_smith@email.com |
+----+------------+----------------------+
```

To select parent rows with at least one related child row and retrieve child data you can use `.innerJoin()` method:

```ts
import { eq } from 'drizzle-orm';
import { users, posts } from './schema';

const db = drizzle(...);

await db
  .select({
    user: users,
    post: posts,
  })
  .from(users)
  .innerJoin(posts, eq(users.id, posts.userId));
  .orderBy(users.id);
```

```sql
select users.*, posts.* from users
  inner join posts on users.id = posts.user_id
  order by users.id;
```

```ts
// result data, there is no user with id 2 because he has no posts
[
  {
    user: { id: 1, name: 'John Doe', email: 'john_doe@email.com' },
    post: {
      id: 1,
      title: 'Post 1',
      content: 'This is the text of post 1',
      userId: 1
    }
  },
  {
    user: { id: 1, name: 'John Doe', email: 'john_doe@email.com' },
    post: {
      id: 2,
      title: 'Post 2',
      content: 'This is the text of post 2',
      userId: 1
    }
  },
  {
    user: { id: 3, name: 'Nick Smith', email: 'nick_smith@email.com' },
    post: {
      id: 3,
      title: 'Post 3',
      content: 'This is the text of post 3',
      userId: 3
    }
  }
]
```

To only select parent rows with at least one related child row you can use subquery with `exists()` function like this:

```ts
import { eq, exists, sql } from 'drizzle-orm';

const sq = db
  .select({ id: sql`1` })
  .from(posts)
  .where(eq(posts.userId, users.id));

await db.select().from(users).where(exists(sq));
```

```sql
select * from users where exists (select 1 from posts where posts.user_id = users.id);
```

```ts
// result data, there is no user with id 2 because he has no posts
[
  { id: 1, name: 'John Doe', email: 'john_doe@email.com' },
  { id: 3, name: 'Nick Smith', email: 'nick_smith@email.com' }
]
```
