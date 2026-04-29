---
title: "Database Features"
source: "https://www.prisma.io/docs/orm/reference/database-features"
canonical_url: "https://www.prisma.io/docs/orm/reference/database-features"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:34:43.353Z"
content_hash: "014c6aa0fd96c75c8ed8995e0ea6bf52738a4ca9ed6a67c19000809cf98439e2"
menu_path: ["Database Features"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/reference/environment-variables-reference/index.md", "title": "Environment Variables"}
nav_next: {"path": "prisma/docs/orm/reference/supported-databases/index.md", "title": "Supported databases"}
---

Database features supported in Prisma ORM

This page gives an overview of the features which are provided by the databases that Prisma ORM supports. Additionally, it explains how each of these features can be used in Prisma ORM with pointers to further documentation.

This section describes which database features exist on the relational databases that are currently supported by Prisma ORM. The **Prisma schema** column indicates how a certain feature can be represented in the [Prisma schema](../../prisma-schema/overview/index.md) and links to its documentation. Note that database features can be used in **Prisma Client** even though they might not yet be representable in the Prisma schema.

### [Constraints](#constraints)

> \* [Caveats apply when using the `UNIQUE` constraint with Microsoft SQL Server](../../core-concepts/supported-databases/sql-server/index.md#common-considerations) † Only supported in MySQL in [version 8 and higher](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html). ‡ Only supported in PostgreSQL.

### [Referential Actions (Delete and Update behaviors for foreign key references)](#referential-actions-delete-and-update-behaviors-for-foreign-key-references)

| Deletion behavior | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| --- | --- | --- | --- | --- |
| `CASCADE` | ✔️ | ✔️ | ✔️ | ✔️ |
| `RESTRICT` | ✔️\* | ✔️ | ✔️ | ✔️ |
| `NO ACTION` | ✔️ | ✔️ | ✔️ | ✔️ |
| `SET DEFAULT` | ✔️ | ✔️ | ✔️ | ✔️ |
| `SET NULL` | ✔️ | ✔️ | ✔️ | ✔️ |

> \* `RESTRICT` is not supported in Microsoft SQL Server.

### [Indexes](#indexes)

| Index | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| --- | --- | --- | --- | --- |
| `UNIQUE` | ✔️ | [`@unique` and `@@unique`](../../prisma-schema/data-model/models/index.md#defining-a-unique-field) | ✔️ | ✔️ |
| `USING` | PostgreSQL only | [`type`](../../prisma-schema/data-model/indexes/index.md#configuring-the-access-type-of-indexes-with-type-postgresql) | ✔️ | ✔️ |
| `WHERE` | ✔️ | [`where`](../../prisma-schema/data-model/indexes/index.md#configuring-partial-indexes-with-where) (Preview) | ✔️ | ✔️ |
| `(expression)` | ✔️ | Not yet | ✔️ | Not yet |
| `INCLUDE` | PostgreSQL and Microsoft SQL Server only | Not yet | ✔️ | Not yet |

Algorithm specified via `USING`:

| Index type (Algorithm) | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| --- | --- | --- | --- | --- |
| B-tree | ✔️ | ✔️† | ✔️ | Not yet |
| Hash | ✔️ | ✔️† | ✔️ | Not yet |
| GiST | ✔️\* | ✔️† | ✔️\* | Not yet |
| GIN | ✔️\* | ✔️† | ✔️\* | Not yet |
| BRIN | ✔️\* | ✔️† | ✔️\* | Not yet |
| SP-GiST | ✔️\* | ✔️† | ✔️\* | Not yet |

-   \* Not supported for MySQL and SQLite
-   † Available with the PostgreSQL connector only in Prisma ORM versions `4.0.0` and later.

### [Misc](#misc)

| Feature | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| --- | --- | --- | --- | --- |
| Autoincrementing IDs | ✔️ | [`autoincrement()`](../../prisma-schema/data-model/models/index.md#defining-a-default-value) | ✔️ | ✔️ |
| Arrays | PostgreSQL only | [`[]`](https://www.prisma.io/docs/orm/prisma-schema/data-model/models#type-modifiers) | ✔️ | ✔️ |
| Enums | ✔️\*† | [`enum`](../../prisma-schema/data-model/models/index.md#defining-enums) | ✔️ | ✔️ |
| Native database types | ✔️ | ✔️ | ✔️ | Not yet |
| SQL Views | ✔️ | Not yet | Not yet | Not yet |
| JSON support | ✔️† | ✔️ | ✔️ | ✔️ |
| Fuzzy/Phrase full text search | ✔️‡ | Not yet | Not yet | Not yet |
| Table inheritance | PostgreSQL and Microsoft SQL Server only | Not yet | ✔️ | Not yet |
| Authorization and user management | ✔️‡ | Not yet | Not yet | Not yet |

-   \* Not supported by Microsoft SQL Server
-   † JSON and Enum types are supported in SQLite as of Prisma ORM 6.2.0.
-   ‡ Not supported by SQLite

This section describes which database features exist on the NoSQL databases that are currently supported by Prisma ORM.

### [MongoDB](#mongodb)

The following table lists common MongoDB features and describes the level of support offered by Prisma ORM:

| Feature | Supported by Prisma ORM | Notes |
| --- | --- | --- |
| Embedded documents | ✔️ |  |
| Transactions | ✔️ |  |
| Indexes | ✔️ with caveats | Indexes can only be introspected if the field they refer to includes at least some data. |
| Autoincrementing IDs | No |  |
| Compound IDs | No | MongoDB does not support composite IDs (`@@id`) |
| Generated `ObjectId` | ✔️ | See: [Defining IDs for MongoDB](../../prisma-schema/data-model/models/index.md#defining-ids-in-mongodb) |
| Arrays | ✔️ |  |
| Enums | ✔️ | Implemented at Prisma ORM level |
| Native database types | ✔️ | See: [Field mapping reference](../prisma-schema-reference/index.md#model-field-scalar-types) |
| JSON support | ✔️ | Advanced `Json` field filtering is not yet supported. |
| DBrefs | No |  |
| Change streams | No |  |
| Direct access to the aggregation pipeline | No |  |
