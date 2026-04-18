---
title: "Roles, superuser access and unsupported operations"
source: "https://supabase.com/docs/guides/database/postgres/roles-superuser"
canonical_url: "https://supabase.com/docs/guides/database/postgres/roles-superuser"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:37.624Z"
content_hash: "8961ac40b6877c6c4dba7e30d5ba287ab708431a66cfc4f06d84ac32936d2e8e"
menu_path: ["Database","Database","Access and security","Access and security","Superuser Access and Unsupported Operations","Superuser Access and Unsupported Operations"]
section_path: ["Database","Database","Access and security","Access and security","Superuser Access and Unsupported Operations","Superuser Access and Unsupported Operations"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/indexes/index.md", "title": "Managing Indexes in Postgres"}
nav_next: {"path": "supabase/docs/guides/database/postgres/roles/index.md", "title": "Postgres Roles"}
---

# 

Roles, superuser access and unsupported operations

* * *

Supabase provides the default `postgres` role to all instances deployed. Superuser access is not given as it allows destructive operations to be performed on the database.

To ensure you are not impacted by this, additional privileges are granted to the `postgres` user to allow it to run some operations that are normally restricted to superusers.

However, this does mean that some operations, that typically require `superuser` privileges, are not available on Supabase. These are documented below:

## Unsupported operations[#](#unsupported-operations)

*   `COPY ... FROM PROGRAM`
*   `ALTER USER ... WITH SUPERUSER`

