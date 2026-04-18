---
title: "Database polyfills"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/database-polyfills"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/database-polyfills"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:19.158Z"
content_hash: "7a37d99f236a93e4eb8956a2e5d366d3205157a66f3a0435b473c8d2036c432a"
menu_path: ["Database polyfills"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names/index.md", "title": "Custom model and field names"}
nav_next: {"path": "prisma/docs/orm/prisma-client/queries/transactions/index.md", "title": "Transactions and batch queries"}
---

Setup and Configuration

Prisma Client provides features that are not achievable with relational databases. These features are referred to as "polyfills" and explained on this page.

Prisma Client provides features that are typically either not achievable with particular databases or require extensions. These features are referred to as _polyfills_. For all databases, this includes:

*   Initializing [ID](prisma/docs/orm/prisma-schema/data-model/models/index.md#defining-an-id-field) values with `cuid` and `uuid` values
*   Using [`@updatedAt`](prisma/docs/orm/prisma-schema/data-model/models/index.md#defining-attributes) to store the time when a record was last updated

For relational databases, this includes:

*   [Implicit many-to-many relations](prisma/docs/orm/prisma-schema/data-model/relations/many-to-many-relations/index.md#implicit-many-to-many-relations)

For MongoDB, this includes:

*   [Relations in general](prisma/docs/orm/prisma-schema/data-model/relations/index.md) - foreign key relations between documents are not enforced in MongoDB

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/database-polyfills.mdx)


