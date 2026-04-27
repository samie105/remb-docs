---
title: "Fields & types"
source: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/special-fields-and-types"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:39:37.103Z"
content_hash: "5f8397c887146c63c78fd6e29cbe1c6447e29cee4a8d5af314c9f2fc30e82724"
menu_path: ["Fields & types"]
section_path: []
content_language: "en"
---
Special Fields and Types

Learn how to use about special fields and types with Prisma Client

This section covers various special fields and types you can use with Prisma Client.

`Decimal` fields are represented by the [`Decimal.js` library](https://mikemcl.github.io/decimal.js/). The following example demonstrates how to import and use `Prisma.Decimal`:

```
import { PrismaClient, Prisma } from "@prisma/client";

const newTypes = await prisma.sample.create({
  data: {
    cost: new Prisma.Decimal(24.454545),
  },
});
```

You can also perform arithmetic operations:

```
import { PrismaClient, Prisma } from "@prisma/client";

const newTypes = await prisma.sample.create({
  data: {
    cost: new Prisma.Decimal(24.454545).plus(1),
  },
});
```

`Prisma.Decimal` uses Decimal.js, see [Decimal.js docs](https://mikemcl.github.io/decimal.js) to learn more.

### [Overview](#overview)

`BigInt` fields are represented by the [`BigInt` type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) (Node.js 10.4.0+ required). The following example demonstrates how to use the `BigInt` type:

```
import { PrismaClient, Prisma } from "@prisma/client";

const newTypes = await prisma.sample.create({
  data: {
    revenue: BigInt(534543543534),
  },
});
```

### [Serializing `BigInt`](#serializing-bigint)

Prisma Client returns records as plain JavaScript objects. If you attempt to use `JSON.stringify` on an object that includes a `BigInt` field, you will see the following error:

```
Do not know how to serialize a BigInt
```

To work around this issue, use a customized implementation of `JSON.stringify`:

```
JSON.stringify(
  this,
  (key, value) => (typeof value === "bigint" ? value.toString() : value), // return everything else unchanged
);
```

`Bytes` fields are represented by the [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) type. The following example demonstrates how to use the `Uint8Array` type:

```
import { PrismaClient, Prisma } from "@prisma/client";

const newTypes = await prisma.sample.create({
  data: {
    myField: new Uint8Array([1, 2, 3, 4]),
  },
});
```

When creating records that have fields of type [`DateTime`](https://www.prisma.io/docs/orm/reference/prisma-schema-reference#datetime), Prisma Client accepts values as [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) objects adhering to the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.

Consider the following schema:

```
model User {
  id        Int       @id @default(autoincrement())
  birthDate DateTime?
}
```

Here are some examples for creating new records:

##### [Jan 01, 1998; 00 h 00 min and 000 ms](#jan-01-1998-00-h-00-min-and-000-ms)

```
await prisma.user.create({
  data: {
    birthDate: new Date("1998"),
  },
});
```

##### [Dec 01, 1998; 00 h 00 min and 000 ms](#dec-01-1998-00-h-00-min-and-000-ms)

```
await prisma.user.create({
  data: {
    birthDate: new Date("1998-12"),
  },
});
```

##### [Dec 24, 1998; 00 h 00 min and 000 ms](#dec-24-1998-00-h-00-min-and-000-ms)

```
await prisma.user.create({
  data: {
    birthDate: new Date("1998-12-24"),
  },
});
```

##### [Dec 24, 1998; 06 h 22 min 33s and 444 ms](#dec-24-1998-06-h-22-min-33s-and-444-ms)

```
await prisma.user.create({
  data: {
    birthDate: new Date("1998-12-24T06:22:33.444Z"),
  },
});
```
