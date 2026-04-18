---
title: "Joins [SQL]"
source: "https://orm.drizzle.team/docs/joins"
canonical_url: "https://orm.drizzle.team/docs/joins"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:38.471Z"
content_hash: "8685e931e1270bc9e6eeb90dc5a3c8aba36eb8af424e266bccecea93314ab013"
menu_path: ["Joins [SQL]"]
section_path: []
nav_prev: {"path": "drizzle/docs/query-utils/index.md", "title": "Drizzle query utils"}
nav_next: {"path": "drizzle/docs/sql/index.md", "title": "Magical sql operator \ud83e\ude84"}
---

## Joins \[SQL\]

Join clause in SQL is used to combine 2 or more tables, based on related columns between them. Drizzle ORM joins syntax is a balance between the SQL-likeness and type safety.

## Join types[](#join-types)

Drizzle ORM has APIs for `INNER JOIN [LATERAL]`, `FULL JOIN`, `LEFT JOIN [LATERAL]`, `RIGHT JOIN`, `CROSS JOIN [LATERAL]`. Lets have a quick look at examples based on below table schemas:

```
export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
});

export const pets = pgTable('pets', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  ownerId: integer('owner_id').notNull().references(() => users.id),
})
```

### Left Join[](#left-join)

```
const result = await db.select().from(users).leftJoin(pets, eq(users.id, pets.ownerId))
```

```
select ... from "users" left join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    pets: {
        id: number;
        name: string;
        ownerId: number;
    } | null;
}[];
```

### Left Join Lateral[](#left-join-lateral)

```
const subquery = db.select().from(pets).where(gte(users.age, 16)).as('userPets')
const result = await db.select().from(users).leftJoinLateral(subquery, sql`true`)
```

```
select ... from "users" left join lateral (select ... from "pets" where "users"."age" >= 16) "userPets" on true
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    userPets: {
        id: number;
        name: string;
        ownerId: number;
    } | null;
}[];
```

### Right Join[](#right-join)

```
const result = await db.select().from(users).rightJoin(pets, eq(users.id, pets.ownerId))
```

```
select ... from "users" right join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    } | null;
    pets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```

### Inner Join[](#inner-join)

```
const result = await db.select().from(users).innerJoin(pets, eq(users.id, pets.ownerId))
```

```
select ... from "users" inner join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    pets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```

### Inner Join Lateral[](#inner-join-lateral)

```
const subquery = db.select().from(pets).where(gte(users.age, 16)).as('userPets')
const result = await db.select().from(users).innerJoinLateral(subquery, sql`true`)
```

```
select ... from "users" inner join lateral (select ... from "pets" where "users"."age" >= 16) "userPets" on true
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    userPets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```

### Full Join[](#full-join)

```
const result = await db.select().from(users).fullJoin(pets, eq(users.id, pets.ownerId))
```

```
select ... from "users" full join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    } | null;
    pets: {
        id: number;
        name: string;
        ownerId: number;
    } | null;
}[];
```

### Cross Join[](#cross-join)

```
const result = await db.select().from(users).crossJoin(pets)
```

```
select ... from "users" cross join "pets"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    pets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```

### Cross Join Lateral[](#cross-join-lateral)

```
const subquery = db.select().from(pets).where(gte(users.age, 16)).as('userPets')
const result = await db.select().from(users).crossJoinLateral(subquery)
```

```
select ... from "users" cross join lateral (select ... from "pets" where "users"."age" >= 16) "userPets"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    userPets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```

## Partial select[](#partial-select)

If you need to select a particular subset of fields or to have a flat response type, Drizzle ORM supports joins with partial select and will automatically infer return type based on `.select({ ... })` structure.

```
await db.select({
  userId: users.id,
  petId: pets.id,
}).from(user).leftJoin(pets, eq(users.id, pets.ownerId))
```

```
select "users"."id", "pets"."id" from "users" left join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
  userId: number;
  petId: number | null;
}[];
```

You might’ve noticed that `petId` can be null now, it’s because we’re left joining and there can be users without a pet.

It’s very important to keep in mind when using `sql` operator for partial selection fields and aggregations when needed, you should to use `sql<type | null>` for proper result type inference, that one is on you!

```
const result = await db.select({
  userId: users.id,
  petId: pets.id,
  petName1: sql`upper(${pets.name})`,
  petName2: sql<string | null>`upper(${pets.name})`,
  //˄we should explicitly tell 'string | null' in type, since we're left joining that field
}).from(user).leftJoin(pets, eq(users.id, pets.ownerId))
```

```
select "users"."id", "pets"."id", upper("pets"."name")... from "users" left join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
  userId: number;
  petId: number | null;
  petName1: unknown;
  petName2: string | null;
}[];
```

To avoid plethora of nullable fields when joining tables with lots of columns we can utilise our **nested select object syntax**, our smart type inference will make whole object nullable instead of making all table fields nullable!

```
await db.select({
  userId: users.id,
  userName: users.name,
  pet: {
    id: pets.id,
    name: pets.name,
    upperName: sql<string>`upper(${pets.name})`
  }
}).from(user).fullJoin(pets, eq(users.id, pets.ownerId))
```

```
select ... from "users" full join "pets" on "users"."id" = "pets"."owner_id"
```

```
// result type
const result: {
    userId: number | null;
    userName: string | null;
    pet: {
        id: number;
        name: string;
        upperName: string;
    } | null;
}[];
```

## Aliases & Selfjoins[](#aliases--selfjoins)

Drizzle ORM supports table aliases which comes really handy when you need to do selfjoins.

Lets say you need to fetch users with their parents:

index.ts

schema.ts

```
import { user } from "./schema";

const parent = alias(user, "parent");
const result = db
  .select()
  .from(user)
  .leftJoin(parent, eq(parent.id, user.parentId));
```

```
select ... from "user" left join "user" "parent" on "parent"."id" = "user"."parent_id"
```

```
// result type
const result: {
    user: {
        id: number;
        name: string;
        parentId: number;
    };
    parent: {
        id: number;
        name: string;
        parentId: number;
    } | null;
}[];
```

```
export const user = pgTable("user", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  name: text("name").notNull(),
  parentId: integer("parent_id").notNull().references((): AnyPgColumn => user.id)
});
```

## Aggregating results[](#aggregating-results)

Drizzle ORM delivers name-mapped results from the driver without changing the structure.

You’re free to operate with results the way you want, here’s an example of mapping many-one relational data:

```
type User = typeof users.$inferSelect;
type Pet = typeof pets.$inferSelect;

const rows = db.select({
    user: users,
    pet: pets,
  }).from(users).leftJoin(pets, eq(users.id, pets.ownerId)).all();

const result = rows.reduce<Record<number, { user: User; pets: Pet[] }>>(
  (acc, row) => {
    const user = row.user;
    const pet = row.pet;

    if (!acc[user.id]) {
      acc[user.id] = { user, pets: [] };
    }

    if (pet) {
      acc[user.id].pets.push(pet);
    }

    return acc;
  },
  {}
);

// result type
const result: Record<number, {
    user: User;
    pets: Pet[];
}>;
```

## Many-to-one example[](#many-to-one-example)

```
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';
import { drizzle } from 'drizzle-orm/better-sqlite3';

const cities = sqliteTable('cities', {
  id: integer('id').primaryKey(),
  name: text('name'),
});

const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name'),
  cityId: integer('city_id').references(() => cities.id)
});

const db = drizzle();

const result = db.select().from(cities).leftJoin(users, eq(cities.id, users.cityId)).all();
```

## Many-to-many example[](#many-to-many-example)

```
const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name'),
});

const chatGroups = sqliteTable('chat_groups', {
  id: integer('id').primaryKey(),
  name: text('name'),
});

const usersToChatGroups = sqliteTable('usersToChatGroups', {
  userId: integer('user_id').notNull().references(() => users.id),
  groupId: integer('group_id').notNull().references(() => chatGroups.id),
});

// querying user group with id 1 and all the participants(users)
db.select()
  .from(usersToChatGroups)
  .leftJoin(users, eq(usersToChatGroups.userId, users.id))
  .leftJoin(chatGroups, eq(usersToChatGroups.groupId, chatGroups.id))
  .where(eq(chatGroups.id, 1))
  .all();
```


