---
title: "Drizzle ORM - Seeding using 'with' option"
source: "https://orm.drizzle.team/docs/guides/seeding-using-with-option"
canonical_url: "https://orm.drizzle.team/docs/guides/seeding-using-with-option"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:02:35.920Z"
content_hash: "6c1110a7d50e81c7109a26ae00397fb49297b0a3ebc0068a8e838b76c76ee3b9"
menu_path: ["Drizzle ORM - Seeding using 'with' option"]
section_path: []
content_language: "en"
nav_prev: {"path": "drizzle/docs/guides/postgresql-local-setup/index.md", "title": "Drizzle ORM - How to setup PostgreSQL locally"}
nav_next: {"path": "drizzle/docs/guides/seeding-with-partially-exposed-tables/index.md", "title": "Drizzle ORM - Seeding Partially Exposed Tables with Foreign Key"}
---

Drizzle | Seeding using 'with' option

Warning

Using `with` implies tables to have a one-to-many relationship.

Therefore, if `one` user has `many` posts, you can use `with` as follows:

```ts
users: {
    count: 2,
    with: {
        posts: 3,
    },
},
```

## Example 1[](#example-1)

```ts
import { users, posts } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users, posts }).refine(() => ({
        users: {
            count: 2,
            with: {
                posts: 3,
            },
        },
    }));
}
main();
```

Running the seeding script above will cause an error.

```plaintext
Error: "posts" table doesn't have a reference to "users" table or
you didn't include your one-to-many relation in the seed function schema.
You can't specify "posts" as parameter in users.with object.
```

You will have several options to resolve an error:

-   You can add reference to the `authorId` column in `posts` table in your schema

```ts
import { users, posts } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users, posts }).refine(() => ({
        users: {
            count: 2,
            with: {
                posts: 3,
            },
        },
    }));
}
main();

// Running the seeding script above will fill you database with values shown below
```

```mdx
`users`

| id |   name   |   
| -- | -------- |
|  1 | 'Melanny' | 
|  2 | 'Elvera' |

`posts`

| id |        content        | author_id |   
| -- | --------------------- | --------- |
|  1 | 'tf02gUXb0LZIdEg6SL'  |     2     |
|  2 | 'j15YdT7Sma'          |     2     |
|  3 | 'LwwvWtLLAZzIpk'      |     1     |
|  4 | 'mgyUnBKSrQw'         |     1     |
|  5 | 'CjAJByKIqilHcPjkvEw' |     2     |
|  6 | 'S5g0NzXs'            |     1     |
```

-   You can add one-to-many relation to your schema and include it in the seed function schema

```ts
import { users, posts, postsRelations } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users, posts, postsRelations }).refine(() => ({
        users: {
            count: 2,
            with: {
                posts: 3,
            },
        },
    }));
}
main();

// Running the seeding script above will fill you database with values shown below
```

```mdx
`users`

| id |   name   |   
| -- | -------- |
|  1 | 'Melanny' | 
|  2 | 'Elvera' |

`posts`

| id |        content        | author_id |   
| -- | --------------------- | --------- |
|  1 | 'tf02gUXb0LZIdEg6SL'  |     2     |
|  2 | 'j15YdT7Sma'          |     2     |
|  3 | 'LwwvWtLLAZzIpk'      |     1     |
|  4 | 'mgyUnBKSrQw'         |     1     |
|  5 | 'CjAJByKIqilHcPjkvEw' |     2     |
|  6 | 'S5g0NzXs'            |     1     |
```

## Example 2[](#example-2)

```ts
import { users, posts } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users, posts }).refine(() => ({
        posts: {
            count: 2,
            with: {
                users: 3,
            },
        },
    }));
}
main();
```

Running the seeding script above will cause an error.

```plaintext
Error: "posts" table doesn't have a reference to "users" table or
you didn't include your one-to-many relation in the seed function schema.
You can't specify "posts" as parameter in users.with object.
```

Why?

You have a `posts` table referencing a `users` table in your schema,

```ts
.
.
.
export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id').notNull().references(() => users.id),
});
```

or in other words, you have one-to-many relation where `one` user can have `many` posts.

However, in your seeding script, you’re attempting to generate 3 (`many`) users for `one` post.

```ts
posts: {
    count: 2,
    with: {
        users: 3,
    },
},
```

To resolve the error, you can modify your seeding script as follows:

```ts
import { users, posts, postsRelations } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users, posts, postsRelations }).refine(() => ({
        users: {
            count: 2,
            with: {
                posts: 3,
            },
        },
    }));
}
main();

// Running the seeding script above will fill you database with values shown below
```

```mdx
`users`

| id |   name   |   
| -- | -------- |
|  1 | 'Melanny' | 
|  2 | 'Elvera' |

`posts`

| id |        content        | author_id |   
| -- | --------------------- | --------- |
|  1 | 'tf02gUXb0LZIdEg6SL'  |     2     |
|  2 | 'j15YdT7Sma'          |     2     |
|  3 | 'LwwvWtLLAZzIpk'      |     1     |
|  4 | 'mgyUnBKSrQw'         |     1     |
|  5 | 'CjAJByKIqilHcPjkvEw' |     2     |
|  6 | 'S5g0NzXs'            |     1     |
```

## Example 3[](#example-3)

```ts
import { users } from './schema.ts';

async function main() {
    const db = drizzle(...);
    await seed(db, { users }).refine(() => ({
        users: {
            count: 2,
            with: {
                users: 3,
            },
        },
    }));
}
main();
```

Running the seeding script above will cause an error.

```plaintext
Error: "users" table has self reference.
You can't specify "users" as parameter in users.with object.
```

Why?

You have a `users` table referencing a `users` table in your schema,

```ts
.
.
.
export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
    reportsTo: integer('reports_to').references((): AnyPgColumn => users.id),
});
```

or in other words, you have one-to-one relation where `one` user can have only `one` user.

However, in your seeding script, you’re attempting to generate 3 (`many`) users for `one` user, which is impossible.

```ts
users: {
    count: 2,
    with: {
        users: 3,
    },
},
```
