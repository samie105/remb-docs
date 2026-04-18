---
title: "Add methods to Prisma Client"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/client"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/client"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:25.471Z"
content_hash: "85d310bc90cfbf0f140a58d1866313c0b323639ac68f2a380c1fc5bc2cd6ec6d"
menu_path: ["Add methods to Prisma Client"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/troubleshooting/raw-sql-comparisons/index.md", "title": "Raw SQL comparisons"}
nav_next: {"path": "prisma/docs/orm/prisma-client/client-extensions/model/index.md", "title": "Add custom methods to your models"}
---

Client Extensions

Extend the functionality of Prisma Client, client component

You can use the `client` [Prisma Client extensions](prisma/docs/orm/prisma-client/client-extensions/index.md) component to add top-level methods to Prisma Client.

Use the `$extends` [client-level method](prisma/docs/orm/reference/prisma-client-reference/index.md#client-methods) to create an _extended client_. An extended client is a variant of the standard Prisma Client that is wrapped by one or more extensions. Use the `client` extension component to add top-level methods to Prisma Client.

To add a top-level method to Prisma Client, use the following structure:

```
const prisma = new PrismaClient().$extends({
  client?: { ... }
})
```

### [Example](#example)

The following example uses the `client` component to add two methods to Prisma Client:

*   `$log` outputs a message.
*   `$totalQueries` returns the number of queries executed by the current client instance.

```
let total = 0;
const prisma = new PrismaClient().$extends({
  client: {
    $log: (s: string) => console.log(s),
    async $totalQueries() {
      return total;
    },
  },
  query: {
    $allModels: {
      async $allOperations({ query, args }) {
        total += 1;
        return query(args);
      },
    },
  },
});

async function main() {
  prisma.$log("Hello world");
  const totalQueries = await prisma.$totalQueries();
  console.log(totalQueries);
}
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/client-extensions/client.mdx)


