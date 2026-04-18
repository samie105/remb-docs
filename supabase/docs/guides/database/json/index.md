---
title: "Managing JSON and unstructured data"
source: "https://supabase.com/docs/guides/database/json"
canonical_url: "https://supabase.com/docs/guides/database/json"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:26.005Z"
content_hash: "909824026eeae0882a50cd85b054a6c8b177aa48aa59d07015c74e18bfed1cdf"
menu_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","JSON and unstructured data","JSON and unstructured data"]
section_path: ["Database","Database","Working with your database (basics)","Working with your database (basics)","JSON and unstructured data","JSON and unstructured data"]
nav_prev: {"path": "supabase/docs/guides/database/metabase/index.md", "title": "Connecting to Metabase"}
nav_next: {"path": "supabase/docs/guides/database/migrating-to-pg-partman/index.md", "title": "Migrate from TimescaleDB to pg_partman"}
---

# 

Managing JSON and unstructured data

## 

Using the JSON data type in Postgres.

* * *

Postgres supports storing and querying unstructured data.

## JSON vs JSONB[#](#json-vs-jsonb)

Postgres supports two types of JSON columns: `json` (stored as a string) and `jsonb` (stored as a binary). The recommended type is `jsonb` for almost all cases.

*   `json` stores an exact copy of the input text. Database functions must reparse the content on each execution.
*   `jsonb` stores database in a decomposed binary format. While this makes it slightly slower to input due to added conversion overhead, it is significantly faster to process, since no reparsing is needed.

## When to use JSON/JSONB[#](#when-to-use-jsonjsonb)

Generally you should use a `jsonb` column when you have data that is unstructured or has a variable schema. For example, if you wanted to store responses for various webhooks, you might not know the format of the response when creating the table. Instead, you could store the `payload` as a `jsonb` object in a single column.

Don't go overboard with `json/jsonb` columns. They are a useful tool, but most of the benefits of a relational database come from the ability to query and join structured data, and the referential integrity that brings.

## Create JSONB columns[#](#create-jsonb-columns)

`json/jsonb` is just another "data type" for Postgres columns. You can create a `jsonb` column in the same way you would create a `text` or `int` column:

```
1create table books (2  id serial primary key,3  title text,4  author text,5  metadata jsonb6);
```

## Inserting JSON data[#](#inserting-json-data)

You can insert JSON data in the same way that you insert any other data. The data must be valid JSON.

```
1insert into books2  (title, author, metadata)3values4  (5    'The Poky Little Puppy',6    'Janette Sebring Lowrey',7    '{"description":"Puppy is slower than other, bigger animals.","price":5.95,"ages":[3,6]}'8  ),9  (10    'The Tale of Peter Rabbit',11    'Beatrix Potter',12    '{"description":"Rabbit eats some vegetables.","price":4.49,"ages":[2,5]}'13  ),14  (15    'Tootle',16    'Gertrude Crampton',17    '{"description":"Little toy train has big dreams.","price":3.99,"ages":[2,5]}'18  ),19  (20    'Green Eggs and Ham',21    'Dr. Seuss',22    '{"description":"Sam has changing food preferences and eats unusually colored food.","price":7.49,"ages":[4,8]}'23  ),24  (25    'Harry Potter and the Goblet of Fire',26    'J.K. Rowling',27    '{"description":"Fourth year of school starts, big drama ensues.","price":24.95,"ages":[10,99]}'28  );
```

## Query JSON data[#](#query-json-data)

Querying JSON data is similar to querying other data, with a few other features to access nested values.

Postgres support a range of [JSON functions and operators](https://www.postgresql.org/docs/current/functions-json.html). For example, the `->` operator returns values as `jsonb` data. If you want the data returned as `text`, use the `->>` operator.

```
1select2  title,3  metadata ->> 'description' as description, -- returned as text4  metadata -> 'price' as price,5  metadata -> 'ages' -> 0 as low_age,6  metadata -> 'ages' -> 1 as high_age7from books;
```

## Validating JSON data[#](#validating-json-data)

Supabase provides the [`pg_jsonschema` extension](/docs/guides/database/extensions/pg_jsonschema) that adds the ability to validate `json` and `jsonb` data types against [JSON Schema](https://json-schema.org/) documents.

Once you have enabled the extension, you can add a "check constraint" to your table to validate the JSON data:

```
1create table customers (2  id serial primary key,3  metadata json4);56alter table customers7add constraint check_metadata check (8  json_matches_schema(9    '{10        "type": "object",11        "properties": {12            "tags": {13                "type": "array",14                "items": {15                    "type": "string",16                    "maxLength": 1617                }18            }19        }20    }',21    metadata22  )23);
```

## Resources[#](#resources)

*   [Postgres: JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html)
*   [Postgres JSON types](https://www.postgresql.org/docs/current/datatype-json.html)


