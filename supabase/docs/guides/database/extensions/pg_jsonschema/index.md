---
title: "pg_jsonschema: JSON Schema Validation"
source: "https://supabase.com/docs/guides/database/extensions/pg_jsonschema"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_jsonschema"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:40.166Z"
content_hash: "32408151b67ce7ab64fd370aadabb5c1c713d892c63b8881bbfed1fd23437ec0"
menu_path: ["Database","Database","Extensions","Extensions","pg_jsonschema: JSON Schema Validation","pg_jsonschema: JSON Schema Validation"]
section_path: ["Database","Database","Extensions","Extensions","pg_jsonschema: JSON Schema Validation","pg_jsonschema: JSON Schema Validation"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pg_hashids/index.md", "title": "pg_hashids: Short UIDs"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pg_net/index.md", "title": "pg_net: Async Networking"}
---

# 

pg\_jsonschema: JSON Schema Validation

* * *

[JSON Schema](https://json-schema.org) is a language for annotating and validating JSON documents. [`pg_jsonschema`](https://github.com/supabase/pg_jsonschema) is a Postgres extension that adds the ability to validate Postgres's built-in `json` and `jsonb` data types against JSON Schema documents.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `pg_jsonschema` and enable the extension.

## Functions[#](#functions)

*   [`json_matches_schema(schema json, instance json)`](https://github.com/supabase/pg_jsonschema#api): Checks if a `json` _instance_ conforms to a JSON Schema _schema_.
*   [`jsonb_matches_schema(schema json, instance jsonb)`](https://github.com/supabase/pg_jsonschema#api): Checks if a `jsonb` _instance_ conforms to a JSON Schema _schema_.

## Usage[#](#usage)

Since `pg_jsonschema` exposes its utilities as functions, we can execute them with a select statement:

```
1select2  extensions.json_matches_schema(3    schema := '{"type": "object"}',4    instance := '{}'5  );
```

`pg_jsonschema` is generally used in tandem with a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) as a way to constrain the contents of a json/b column to match a JSON Schema.

```
1create table customer(2    id serial primary key,3    ...4    metadata json,56    check (7        json_matches_schema(8            '{9                "type": "object",10                "properties": {11                    "tags": {12                        "type": "array",13                        "items": {14                            "type": "string",15                            "maxLength": 1616                        }17                    }18                }19            }',20            metadata21        )22    )23);2425-- Example: Valid Payload26insert into customer(metadata)27values ('{"tags": ["vip", "darkmode-ui"]}');28-- Result:29--   INSERT 0 13031-- Example: Invalid Payload32insert into customer(metadata)33values ('{"tags": [1, 3]}');34-- Result:35--   ERROR:  new row for relation "customer" violates check constraint "customer_metadata_check"36--   DETAIL:  Failing row contains (2, {"tags": [1, 3]}).
```

## Resources[#](#resources)

*   Official [`pg_jsonschema` documentation](https://github.com/supabase/pg_jsonschema)


