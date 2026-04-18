---
title: "uuid-ossp: Unique Identifiers"
source: "https://supabase.com/docs/guides/database/extensions/uuid-ossp"
canonical_url: "https://supabase.com/docs/guides/database/extensions/uuid-ossp"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:21.165Z"
content_hash: "ac5fdbc3b36db76f1c750eac61c840893c1b35e864c53eef46e7cc91d866d7b9"
menu_path: ["Database","Database","Extensions","Extensions","uuid-ossp: Unique Identifiers","uuid-ossp: Unique Identifiers"]
section_path: ["Database","Database","Extensions","Extensions","uuid-ossp: Unique Identifiers","uuid-ossp: Unique Identifiers"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/timescaledb/index.md", "title": "timescaledb: Time-Series data"}
nav_next: {"path": "supabase/docs/guides/database/postgres/column-level-security/index.md", "title": "Column Level Security"}
---

# 

uuid-ossp: Unique Identifiers

* * *

The `uuid-ossp` extension can be used to generate a `UUID`.

## Overview[#](#overview)

A `UUID` is a "Universally Unique Identifier" and it is, for practical purposes, unique. This makes them particularly well suited as Primary Keys. It is occasionally referred to as a `GUID`, which stands for "Globally Unique Identifier".

## Enable the extension[#](#enable-the-extension)

**Note**: Currently `uuid-ossp` extension is enabled by default and cannot be disabled.

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `uuid-ossp` and enable the extension.

## The `uuid` type[#](#the-uuid-type)

Once the extension is enabled, you now have access to a `uuid` type.

## `uuid_generate_v1()`[#](#uuidgeneratev1)

Creates a UUID value based on the combination of computer’s MAC address, current timestamp, and a random value.

UUIDv1 leaks identifiable details, which might make it unsuitable for certain security-sensitive applications.

## `uuid_generate_v4()`[#](#uuidgeneratev4)

Creates UUID values based solely on random numbers. You can also use Postgres's built-in [`gen_random_uuid()`](https://www.postgresql.org/docs/current/functions-uuid.html) function to generate a UUIDv4.

## Examples[#](#examples)

### Within a query[#](#within-a-query)

```
1select uuid_generate_v4();
```

### As a primary key[#](#as-a-primary-key)

Automatically create a unique, random ID in a table:

```
1create table contacts (2  id uuid default uuid_generate_v4(),3  first_name text,4  last_name text,5  primary key (id)6);
```

## Resources[#](#resources)

*   [Choosing a Postgres Primary Key](/blog/choosing-a-postgres-primary-key)
*   [The Basics Of Postgres `UUID` Data Type](https://www.pgtutorial.com/postgresql-tutorial/postgresql-uuid/)
