---
title: "Add methods to Prisma Client"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/client"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/client"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:59.376Z"
content_hash: "06ede3ef6417d774d4f742877150fe8b66a1b5b6826719820b4de5e4a9f8bbee"
menu_path: ["Add methods to Prisma Client"]
section_path: []
content_language: "en"
---
Client Extensions

## Add methods to Prisma Client

Extend the functionality of Prisma Client, client component

You can use the `client` [Prisma Client extensions](https://www.prisma.io/docs/orm/prisma-client/client-extensions) component to add top-level methods to Prisma Client.

Use the `$extends` [client-level method](https://www.prisma.io/docs/orm/reference/prisma-client-reference#client-methods) to create an _extended client_. An extended client is a variant of the standard Prisma Client that is wrapped by one or more extensions. Use the `client` extension component to add top-level methods to Prisma Client.

To add a top-level method to Prisma Client, use the following structure:

```
const prisma = new PrismaClient().$extends({
  client?: { ... }
})
```

### [Example](#example)

The following example uses the `client` component to add two methods to Prisma Client:

-   `$log` outputs a message.
-   `$totalQueries` returns the number of queries executed by the current client instance.

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
