---
title: "Handling exceptions and errors"
source: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/handling-exceptions-and-errors"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/handling-exceptions-and-errors"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:38:24.693Z"
content_hash: "e21b0744f824ab0f8d45155cef0cfdec4e64aad3fc7c73b13478a3c1fae5e059"
menu_path: ["Handling exceptions and errors"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/debugging-and-troubleshooting/debugging/index.md", "title": "Debugging"}
nav_next: {"path": "prisma/docs/orm/prisma-client/deployment/caveats-when-deploying-to-aws-platforms/index.md", "title": "Caveats when deploying to AWS platforms"}
---

Debugging and Troubleshooting

This page covers how to handle exceptions and errors

In order to handle different types of errors you can use `instanceof` to check what the error is and handle it accordingly.

The following example tries to create a user with an already existing email record. This will throw an error because the `email` field has the `@unique` attribute applied to it.

schema.prisma

```
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
```

Use the `Prisma` namespace to access the error type. The [error code](prisma/docs/orm/reference/error-reference/index.md#error-codes) can then be checked and a message can be printed.

```
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, Prisma } from "../generated/prisma/client";

const connectionString = `${process.env.DATABASE_URL}`;
const adapter = new PrismaPg({ connectionString });
const prisma = new PrismaClient({ adapter });

try {
  await client.user.create({ data: { email: "alreadyexisting@mail.com" } });
} catch (e) {
  if (e instanceof Prisma.PrismaClientKnownRequestError) {
    // The .code property can be accessed in a type-safe manner
    if (e.code === "P2002") {
      console.log(
        "There is a unique constraint violation, a new user cannot be created with this email",
      );
    }
  }
  throw e;
}
```

See [Errors reference](prisma/docs/orm/reference/error-reference/index.md) for a detailed breakdown of the different error types and their codes.
