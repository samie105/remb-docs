---
title: "PostgreSQL: Documentation: 18: 9.14. UUID Functions"
source: "https://www.postgresql.org/docs/current/functions-uuid.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-uuid.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:37.700Z"
content_hash: "4bb29162aa976be67dbe2abd2b990251d2e80f4e47b9ad4798da9b411de1b064"
menu_path: ["PostgreSQL: Documentation: 18: 9.14. UUID Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/catalog-pg-operator.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.34.\u00a0pg_operator"}
nav_next: {"path": "postgres/docs/current/earthdistance.html/index.md", "title": "PostgreSQL: Documentation: 18: F.14.\u00a0earthdistance \u2014 calculate great-circle distances"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/functions-uuid.html "PostgreSQL devel - 9.14. UUID Functions")

[Table 9.45](https://www.postgresql.org/docs/current/functions-uuid.html#FUNC_UUID_GEN_TABLE "Table 9.45. UUID Generation Functions") shows the PostgreSQL functions that can be used to generate UUIDs.

**Table 9.45. UUID Generation Functions**

Function

Description

Example(s)

`gen_random_uuid` ( ) → `uuid`

`uuidv4` ( ) → `uuid`

Generates a version 4 (random) UUID

`gen_random_uuid()` → `5b30857f-0bfa-48b5-ac0b-5c64e28078d1`

`uuidv4()` → `b42410ee-132f-42ee-9e4f-09a6485c95b8`

`uuidv7` ( \[ _`shift`_ `interval` \] ) → `uuid`

Generates a version 7 (time-ordered) UUID. The timestamp is computed using UNIX timestamp with millisecond precision + sub-millisecond timestamp + random. The optional parameter _`shift`_ will shift the computed timestamp by the given `interval`.

`uuidv7()` → `019535d9-3df7-79fb-b466-fa907fa17f9e`

  

### Note

The [uuid-ossp](https://www.postgresql.org/docs/current/uuid-ossp.html "F.49. uuid-ossp — a UUID generator") module provides additional functions that implement other standard algorithms for generating UUIDs.

[Table 9.46](https://www.postgresql.org/docs/current/functions-uuid.html#FUNC_UUID_EXTRACT_TABLE "Table 9.46. UUID Extraction Functions") shows the PostgreSQL functions that can be used to extract information from UUIDs.

PostgreSQL also provides the usual comparison operators shown in [Table 9.1](https://www.postgresql.org/docs/current/functions-comparison.html#FUNCTIONS-COMPARISON-OP-TABLE "Table 9.1. Comparison Operators") for UUIDs.

See [Section 8.12](https://www.postgresql.org/docs/current/datatype-uuid.html "8.12. UUID Type") for details on the data type `uuid` in PostgreSQL.


