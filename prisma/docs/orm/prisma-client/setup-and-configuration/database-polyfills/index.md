---
title: "Database polyfills"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/database-polyfills"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/database-polyfills"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:39:17.241Z"
content_hash: "b9ef0c0452977bb8a80eea3f533682a197cc2497fd0cc4a6a798d2dab5b8e069"
menu_path: ["Database polyfills"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/custom-model-and-field-names/index.md", "title": "Custom model and field names"}
nav_next: {"path": "prisma/docs/orm/prisma-client/setup-and-configuration/databases-connections/index.md", "title": "Database connections"}
---

Setup and Configuration

Prisma Client provides features that are not achievable with relational databases. These features are referred to as "polyfills" and explained on this page.

Prisma Client provides features that are typically either not achievable with particular databases or require extensions. These features are referred to as _polyfills_. For all databases, this includes:

-   Initializing [ID](../../../prisma-schema/data-model/models/index.md#defining-an-id-field) values with `cuid` and `uuid` values
-   Using [`@updatedAt`](../../../prisma-schema/data-model/models/index.md#defining-attributes) to store the time when a record was last updated

For relational databases, this includes:

-   [Implicit many-to-many relations](../../../prisma-schema/data-model/relations/many-to-many-relations/index.md#implicit-many-to-many-relations)

For MongoDB, this includes:

-   [Relations in general](../../../prisma-schema/data-model/relations/index.md) - foreign key relations between documents are not enforced in MongoDB
