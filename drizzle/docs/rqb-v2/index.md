---
title: "Drizzle Queries"
source: "https://orm.drizzle.team/docs/rqb-v2"
canonical_url: "https://orm.drizzle.team/docs/rqb-v2"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:19:58.726Z"
content_hash: "b2fb65d77952549b005987502f145a7f9a609965e3f02d925b1aecbcb57caadf"
menu_path: ["Drizzle Queries"]
section_path: []
nav_prev: {"path": "drizzle/docs/seed-versioning/index.md", "title": "Versioning"}
nav_next: {"path": "drizzle/docs/select/index.md", "title": "SQL Select"}
---

## Drizzle Queries

WARNING

This page explains concepts available on drizzle versions `1.0.0-beta.1` and higher.

npm

yarn

pnpm

bun

```
npm i drizzle-orm@beta
npm i drizzle-kit@beta -D
```

```
yarn add drizzle-orm@beta
yarn add drizzle-kit@beta -D
```

```
pnpm add drizzle-orm@beta
pnpm add drizzle-kit@beta -D
```

```
bun add drizzle-orm@beta
bun add drizzle-kit@beta -D
```

  

PostgreSQL

SQLite

MySQL

SingleStore

Drizzle ORM is designed to be a thin typed layer on top of SQL. We truly believe we’ve designed the best way to operate an SQL database from TypeScript and it’s time to make it better.

Relational queries are meant to provide you with a great developer experience for querying nested relational data from an SQL database, avoiding multiple joins and complex data mappings.

It is an extension to the existing schema definition and query builder. You can opt-in to use it based on your needs. We’ve made sure you have both the best-in-class developer experience and performance.

index.ts

schema.ts

```
import { relations } from './schema';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle({ relations });

const result = await db.query.users.findMany({
	with: {
		posts: true			
	},
});
```

```
[{
	id: 10,
	name: "Dan",
	posts: [
		{
			id: 1,
			content: "SQL is awesome",
			authorId: 10,
		},
		{
			id: 2,
			content: "But check relational queries",
			authorId: 10,
		}
	]
}]
```

```
import { defineRelations } from "drizzle-orm";
import * as p from "drizzle-orm/pg-core";

export const posts = p.pgTable("posts", {
  id: p.integer().primaryKey(),
  content: p.text().notNull(),
  authorId: p.integer("author_id").notNull(),
});

export const users = p.pgTable("users", {
  id: p.integer().primaryKey(),
  name: p.text().notNull(),
});

export const relations = defineRelations({ users, posts }, (r) => ({
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
  },
  users: {
    posts: r.many.users(),
  },
}));
```

Relational queries are an extension to Drizzle’s original **[query builder](drizzle/docs/select/index.md)**. You need to provide all `tables` and `relations` from your schema file/files upon `drizzle()` initialization and then just use the `db.query` API.

index.ts

schema.ts

relations.ts

```
import { relations } from './relations';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle({ relations });

await db.query.users.findMany(...);
```

```
import { type AnyPgColumn, boolean, integer, pgTable, primaryKey, text, timestamp } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
	id: integer().primaryKey(),
	name: text().notNull(),
	invitedBy: integer('invited_by').references((): AnyPgColumn => users.id),
});

export const groups = pgTable('groups', {
	id: integer().primaryKey(),
	name: text().notNull(),
	description: text(),
});

export const usersToGroups = pgTable('users_to_groups', {
	id: integer().primaryKey(),
	userId: integer('user_id').notNull().references(() => users.id),
	groupId: integer('group_id').notNull().references(() => groups.id),
}, (t) => [
	primaryKey(t.userId, t.groupId)
]);

export const posts = pgTable('posts', {
	id: integer().primaryKey(),
	content: text().notNull(),
	authorId: integer('author_id').references(() => users.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});

export const comments = pgTable('comments', {
	id: integer().primaryKey(),
	content: text().notNull(),
	creator: integer().references(() => users.id),
	postId: integer('post_id').references(() => posts.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});

export const commentLikes = pgTable('comment_likes', {
	id: integer().primaryKey(),
	creator: integer().references(() => users.id),
	commentId: integer('comment_id').references(() => comments.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});
```

```
import { defineRelations } from 'drizzle-orm';
import * as schema from './schema';

export const relations = defineRelations(schema, (r) => ({
    users: {
      invitee: r.one.users({
        from: r.users.invitedBy,
        to: r.users.id,
      }),
      groups: r.many.groups({
        from: r.users.id.through(r.usersToGroups.userId),
        to: r.groups.id.through(r.usersToGroups.groupId),
      }),
      posts: r.many.posts(),
    },
    groups: {
      users: r.many.users(),
    },
    posts: {
      author: r.one.users({
        from: r.posts.authorId,
        to: r.users.id,
      }),
      comments: r.many.comments(),
    },
    comments: {
      post: r.one.posts({
        from: r.comments.postId,
        to: r.posts.id,
      }),
      author: r.one.users({
        from: r.comments.creator,
        to: r.users.id,
      }),
      likes: r.many.commentLikes(),
    },
    commentLikes: {
      comment: r.one.comments({
        from: r.commentLikes.commentId,
        to: r.comments.id,
      }),
      author: r.one.users({
        from: r.commentLikes.creator,
        to: r.users.id,
      }),
    },
  })
);
```

Drizzle provides `.findMany()` and `.findFirst()` APIs.

### Find many[](#find-many)

```
const users = await db.query.users.findMany();
```

```
// result type
const result: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
}[];
```

### Find first[](#find-first)

`.findFirst()` will add `limit 1` to the query.

```
const user = await db.query.users.findFirst();
```

```
// result type
const result: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
};
```

### Include relations[](#include-relations)

`With` operator lets you combine data from multiple related tables and properly aggregate results.

**Getting all posts with comments:**

```
const posts = await db.query.posts.findMany({
	with: {
		comments: true,
	},
});
```

**Getting first post with comments:**

```
const post = await db.query.posts.findFirst({
	with: {
		comments: true,
	},
});
```

You can chain nested with statements as much as necessary.  
For any nested `with` queries Drizzle will infer types using [Core Type API](drizzle/docs/goodies/index.md#type-api).

**Get all users with posts. Each post should contain a list of comments:**

```
const users = await db.query.users.findMany({
	with: {
		posts: {
			with: {
				comments: true,
			},
		},
	},
});
```

### Partial fields select[](#partial-fields-select)

`columns` parameter lets you include or omit columns you want to get from the database.

Drizzle performs partial selects on the query level, no additional data is transferred from the database.

Keep in mind that **a single SQL statement is outputted by Drizzle.**

**Get all posts with just `id`, `content` and include `comments`:**

```
const posts = await db.query.posts.findMany({
	columns: {
		id: true,
		content: true,
	},
	with: {
		comments: true,
	}
});
```

**Get all posts without `content`:**

```
const posts = await db.query.posts.findMany({
	columns: {
		content: false,
	},
});
```

When both `true` and `false` select options are present, all `false` options are ignored.

If you include the `name` field and exclude the `id` field, `id` exclusion will be redundant, all fields apart from `name` would be excluded anyways.

**Exclude and Include fields in the same query:**

```
const users = await db.query.users.findMany({
	columns: {
		name: true,
		id: false //ignored
	},
});
```

```
// result type
const users: {
	name: string;
};
```

**Only include columns from nested relations:**

```
const res = await db.query.users.findMany({
	columns: {},
	with: {
		posts: true
	}
});
```

```
// result type
const res: {
	posts: {
		id: number,
		text: string
	}
}[];
```

### Nested partial fields select[](#nested-partial-fields-select)

Just like with **[`partial select`](#partial-select)**, you can include or exclude columns of nested relations:

```
const posts = await db.query.posts.findMany({
	columns: {
		id: true,
		content: true,
	},
	with: {
		comments: {
			columns: {
				authorId: false
			}
		}
	}
});
```

### Select filters[](#select-filters)

Just like in our SQL-like query builder, relational queries API lets you define filters and conditions with the list of our **[`operators`](drizzle/docs/operators/index.md)**.

You can either import them from `drizzle-orm` or use from the callback syntax:

```
const users = await db.query.users.findMany({
	where: {
		id: 1
	}
});
```

```
select * from users where id = 1
```

Find post with `id=1` and comments that were created before particular date:

```
await db.query.posts.findMany({
  where: {
    id: 1,
  },
  with: {
    comments: {
      where: {
        createdAt: { lt: new Date() },
      },
    },
  },
});
```

**List of all filter operators**

```
where: {
    OR: [],
    AND: [],
    NOT: {},
    RAW: (table) => sql`${table.id} = 1`,

    // filter by relations
    [relation]: {},

	  // filter by columns
    [column]: {
      OR: [],
      AND: [],
      NOT: {},
      eq: 1,
      ne: 1,
      gt: 1,
      gte: 1,
      lt: 1,
      lte: 1,
      in: [1],
      notIn: [1],
      like: "",
      ilike: "",
      notLike: "",
      notIlike: "",
      isNull: true,
      isNotNull: true,
      arrayOverlaps: [1, 2],
      arrayContained: [1, 2],
      arrayContains: [1, 2]
    },
},
```

**Examples**

simple eq

using AND

using OR

using NOT

complex example using RAW

```
const response = db.query.users.findMany({
  where: {
    age: 15,
  },
});
```

```
select "users"."id" as "id", "users"."name" as "name"
from "users" 
where ("users"."age" = 15)
```

### Relations Filters[](#relations-filters)

With Drizzle Relations, you can filter not only by the table you’re querying but also by any table you include in the query.

**Example:** Get all `users` whose ID>10 and who have at least one post with content starting with “M”

```
const usersWithPosts = await db.query.usersTable.findMany({
  where: {
    id: {
      gt: 10
    },
    posts: {
      content: {
        like: 'M%'
      }
    }
  },
});
```

**Example:** Get all `users` with posts, only if user has at least 1 post

```
const response = db.query.users.findMany({
  with: {
    posts: true,
  },
  where: {
    posts: true,
  },
});
```

### Limit & Offset[](#limit--offset)

Drizzle ORM provides `limit` & `offset` API for queries and for the nested entities.

**Find 5 posts:**

```
await db.query.posts.findMany({
	limit: 5,
});
```

**Find posts and get 3 comments at most:**

```
await db.query.posts.findMany({
	with: {
		comments: {
			limit: 3,
		},
	},
});
```

IMPORTANT

`offset` now can be used in with tables as well!

```
await db.query.posts.findMany({
	limit: 5,
	offset: 2, // correct ✅
	with: {
		comments: {
			offset: 3, // correct ✅
			limit: 3,
		},
	},
});
```

Find posts with comments from the 5th to the 10th post:

```
await db.query.posts.findMany({
	with: {
		comments: true,
	},
  limit: 5,
  offset: 5,
});
```

### Order By[](#order-by)

Drizzle provides API for ordering in the relational query builder.

You can use same ordering **[core API](drizzle/docs/select/index.md#order-by)** or use `order by` operator from the callback with no imports.

important

When you use multiple `orderBy` statements in the same table, they will be included in the query in the same order in which you added them

```
await db.query.posts.findMany({
  orderBy: {
    id: "asc",
  },
});
```

**Order by `asc` + `desc`:**

```
  await db.query.posts.findMany({
    orderBy: { id: "asc" },
    with: {
      comments: {
        orderBy: { id: "desc" },
      },
    },
  });
```

You can also use custom `sql` in order by statement:

```
await db.query.posts.findMany({
  orderBy: (t) => sql`${t.id} asc`,
  with: {
    comments: {
      orderBy: (t, { desc }) => desc(t.id),
    },
  },
});
```

### Include custom fields[](#include-custom-fields)

Relational query API lets you add custom additional fields. It’s useful when you need to retrieve data and apply additional functions to it.

IMPORTANT

As of now aggregations are not supported in `extras`, please use **[`core queries`](drizzle/docs/select/index.md)** for that.

```
import { sql } from 'drizzle-orm';

await db.query.users.findMany({
	extras: {
		loweredName: sql`lower(${users.name})`,
	},
})
```

```
await db.query.users.findMany({
	extras: {
		loweredName: (users, { sql }) => sql`lower(${users.name})`,
	},
})
```

`lowerName` as a key will be included to all fields in returned object.

IMPORTANT

If you will specify `.as("<alias>")` for any extras field - drizzle will ignore it

To retrieve all users with groups, but with the fullName field included (which is a concatenation of firstName and lastName), you can use the following query with the Drizzle relational query builder.

```
const res = await db.query.users.findMany({
	extras: {
		fullName: (users, { sql }) => sql<string>`concat(${users.name}, " ", ${users.name})`,
	},
	with: {
		usersToGroups: {
			with: {
				group: true,
			},
		},
	},
});
```

```
// result type
const res: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
	fullName: string;
	usersToGroups: {
			group: {
					id: number;
					name: string;
					description: string | null;
			};
	}[];
}[];
```

To retrieve all posts with comments and add an additional field to calculate the size of the post content and the size of each comment content:

```
const res = await db.query.posts.findMany({
	extras: {
		contentLength: (table, { sql }) => sql<number>`length(${table.content})`,
	},
	with: {
		comments: {
			extras: {
				commentSize: (table, { sql }) => sql<number>`length(${table.content})`,
			},
		},
	},
});
```

```
// result type
const res: {
	id: number;
	createdAt: Date;
	content: string;
	authorId: number | null;
	contentLength: number;
	comments: {
			id: number;
			createdAt: Date;
			content: string;
			creator: number | null;
			postId: number | null;
			commentSize: number;
	}[];
};
```

### Include subqueries[](#include-subqueries)

You can also use subqueries within Relational Queries to leverage the power of custom SQL syntax

**Get users with posts and total posts count for each user**

```
import { posts } from './schema';
import { eq } from 'drizzle-orm';

await db.query.users.findMany({
  with: {
    posts: true
  },
  extras: {
    totalPostsCount: (table) => db.$count(posts, eq(posts.authorId, table.id)),
  }
});
```

```
select "d0"."id" as "id", "d0"."name" as "name", "posts"."r" as "posts", 
((select count(*) from "posts" where "posts"."author_id" = "d0"."id")) as "totalPostsCount" 
from "users" as "d0" 
left join lateral(
  select coalesce(json_agg(row_to_json("t".*)), '[]') as "r" 
  from (select "d1"."id" as "id", "d1"."content" as "content", "d1"."author_id" as "authorId" from "posts" as "d1" where "d0"."id" = "d1"."author_id") as "t"
) as "posts" on true
```

### Prepared statements[](#prepared-statements)

Prepared statements are designed to massively improve query performance — [see here.](drizzle/docs/perf-queries/index.md)

In this section, you can learn how to define placeholders and execute prepared statements using the Drizzle relational query builder.

##### **Placeholder in `where`**[](#placeholder-in-where)

PostgreSQL

MySQL

SQLite

```
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
      },
    },
}).prepare("query_name");

const usersWithPosts = await prepared.execute({ id: 1 });
```

```
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ id: 1 });
```

```
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ id: 1 });
```

##### **Placeholder in `limit`**[](#placeholder-in-limit)

PostgreSQL

MySQL

SQLite

```
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
      },
    },
  }).prepare("query_name");

const usersWithPosts = await prepared.execute({ limit: 1 });
```

```
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
      },
    },
  }).prepare();

const usersWithPosts = await prepared.execute({ limit: 1 });
```

```
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
      },
    },
  }).prepare();

const usersWithPosts = await prepared.execute({ limit: 1 });
```

##### **Placeholder in `offset`**[](#placeholder-in-offset)

PostgreSQL

MySQL

SQLite

```
const prepared = db.query.users.findMany({
	offset: sql.placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare('query_name');

const usersWithPosts = await prepared.execute({ offset: 1 });
```

```
const prepared = db.query.users.findMany({
	offset: sql.placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare();

const usersWithPosts = await prepared.execute({ offset: 1 });
```

```
const prepared = db.query.users.findMany({
	offset: sql.placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare();

const usersWithPosts = await prepared.execute({ offset: 1 });
```

##### **Multiple placeholders**[](#multiple-placeholders)

PostgreSQL

MySQL

SQLite

```
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
      },
    },
}).prepare("query_name");

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```

```
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```

```
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```

