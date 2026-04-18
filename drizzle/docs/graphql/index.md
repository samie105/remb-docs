---
title: "drizzle-graphql"
source: "https://orm.drizzle.team/docs/graphql"
canonical_url: "https://orm.drizzle.team/docs/graphql"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:13.583Z"
content_hash: "e05fb13bc56236fe36752898b6925dcde0874b34d5c7a451f7ceaed391a7556c"
menu_path: ["drizzle-graphql"]
section_path: []
nav_prev: {"path": "drizzle/docs/eslint-plugin/index.md", "title": "ESLint Drizzle Plugin"}
nav_next: {"path": "drizzle/docs/column-types/mssql/index.md", "title": "MSSQL column types"}
---

Create a GraphQL server from a Drizzle schema in one line, and easily enhance it with custom queries and mutations.

## Quick start[](#quick-start)

Make sure your `drizzle-orm` version is at least `0.30.9`, and update if needed:

npm

yarn

pnpm

bun

```
npm i drizzle-orm@latest
```

```
yarn add drizzle-orm@latest
```

```
pnpm add drizzle-orm@latest
```

```
bun add drizzle-orm@latest
```

### Apollo Server[](#apollo-server)

npm

yarn

pnpm

bun

```
npm i drizzle-graphql @apollo/server graphql
```

```
yarn add drizzle-graphql @apollo/server graphql
```

```
pnpm add drizzle-graphql @apollo/server graphql
```

```
bun add drizzle-graphql @apollo/server graphql
```

server.ts

schema.ts

```
import { buildSchema } from 'drizzle-graphql';
import { drizzle } from 'drizzle-orm/...';
import client from './db';
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

import * as dbSchema from './schema';

const db = drizzle({ client, schema: dbSchema });

const { schema } = buildSchema(db);

const server = new ApolloServer({ schema });
const { url } = await startStandaloneServer(server);

console.log(`🚀 Server ready at ${url}`);
```

### GraphQL Yoga[](#graphql-yoga)

npm

yarn

pnpm

bun

```
npm i drizzle-graphql graphql-yoga graphql
```

```
yarn add drizzle-graphql graphql-yoga graphql
```

```
pnpm add drizzle-graphql graphql-yoga graphql
```

```
bun add drizzle-graphql graphql-yoga graphql
```

server.ts

schema.ts

```
import { buildSchema } from 'drizzle-graphql';
import { drizzle } from 'drizzle-orm/...';
import { createYoga } from 'graphql-yoga';
import { createServer } from 'node:http';

import * as dbSchema from './schema';

const db = drizzle({ schema: dbSchema });

const { schema } = buildSchema(db);

const yoga = createYoga({ schema });
const server = createServer(yoga);

server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql');
});
```

## Customizing schema[](#customizing-schema)

`buildSchema()` produces schema and types using standard `graphql` SDK, so its output is compatible with any library that supports it.

If you want to customize your schema, you can use `entities` object to build your own new schema:

server.ts

schema.ts

```
import { buildSchema } from 'drizzle-graphql';
import { drizzle } from 'drizzle-orm/...';
import { GraphQLList, GraphQLNonNull, GraphQLObjectType, GraphQLSchema } from 'graphql';
import { createYoga } from 'graphql-yoga';
import { createServer } from 'node:http';

import * as dbSchema from './schema';

const db = drizzle({ schema: dbSchema });

const { entities } = buildSchema(db);

// You can customize which parts of queries or mutations you want
const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'Query',
    fields: {
      // Select only wanted queries out of all generated
      users: entities.queries.users,
      customer: entities.queries.customersSingle,

      // Create a custom one
      customUsers: {
        // You can reuse and customize types from original schema
        type: new GraphQLList(new GraphQLNonNull(entities.types.UsersItem)),
        args: {
          // You can reuse inputs as well
          where: {
            type: entities.inputs.UsersFilters
          },
        },
        resolve: async (source, args, context, info) => {
          // Your custom logic goes here...
          const result = await db.select(schema.users).where()...

          return result;
        },
      },
    },
  }),
  // Same rules apply to mutations
  mutation: new GraphQLObjectType({
    name: 'Mutation',
    fields: entities.mutations,
  }),
  // In case you need types inside your schema
  types: [...Object.values(entities.types), ...Object.values(entities.inputs)],
});

const yoga = createYoga({
  schema,
});

const server = createServer(yoga);

server.listen(4000, () => {
  console.info('Server is running on http://localhost:4000/graphql');
})
```
