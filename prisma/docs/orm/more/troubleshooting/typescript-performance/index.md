---
title: "TypeScript performance"
source: "https://www.prisma.io/docs/orm/more/troubleshooting/typescript-performance"
canonical_url: "https://www.prisma.io/docs/orm/more/troubleshooting/typescript-performance"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:55.808Z"
content_hash: "e78bd01f96cf7c41410799dd058de1c2feece3a2e7a76d56374e1d9b3b44150e"
menu_path: ["TypeScript performance"]
section_path: []
content_language: "en"
---
Troubleshooting

Optimize TypeScript compilation performance when working with large Prisma schemas

When working with large database schemas, a simple change in type definition strategy can deliver massive performance improvements:

| Approach | Types | Instantiations | Memory | Compile Time |
| --- | --- | --- | --- | --- |
| **Direct Reference** | 269,597 | 2,772,929 | 395MB | 1.86s |
| **typeof technique** | 222 (**99.9% reduction**) | 152 (**99.9% reduction**) | 147MB (**62% reduction**) | 0.41s (**78% reduction**) |

In enterprise applications with extensive database schemas, Prisma's generated types can become enormous. A schema with 50+ tables and deep relationships can lead to:

-   Compilation times exceeding several minutes
-   High memory usage during type checking
-   IDE responsiveness degrading significantly
-   CI/CD pipelines timing out on type checks

Use TypeScript's `typeof` operator instead of direct type references when defining function parameters that accept PrismaClient instances.

### [Problematic approach for large schemas](#problematic-approach-for-large-schemas)

```
import { PrismaClient } from "../prisma/generated/client";

const saveFn = async (prismaClient: PrismaClient) => {
  // Function implementation
};

const client = new PrismaClient();
await saveFn(client);
```

### [Optimized approach with `typeof`](#optimized-approach-with-typeof)

```
import { PrismaClient } from "../prisma/generated/client";

const saveFn = async (prismaClient: typeof client) => {
  // Function implementation
};

const client = new PrismaClient();
await saveFn(client);
```

The `typeof` operator creates a more efficient type resolution path:

1.  **Type Query Reference**: `typeof client` performs a type query that obtains the widened type of the identifier expression, avoiding the need to re-expand the complex `PrismaClient` type definition
2.  **Reduced Type Instantiation**: The compiler avoids expanding the entire Prisma type hierarchy for each type check (resulting in a 99.9% reduction in instantiations)
3.  **Memory Efficiency**: Referencing an existing instance's inferred type requires significantly less memory than expanding complex conditional types and generics

When working with large Prisma schemas, the choice between direct type references and type queries becomes crucial for maintaining development velocity. The 78% compilation time reduction demonstrated here scales exponentially with schema complexity.

The complete benchmark code is available at: [https://github.com/ToyB0x/ts-bench/pull/211](https://github.com/ToyB0x/ts-bench/pull/211)
