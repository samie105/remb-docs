---
title: "Managing Enums in Postgres"
source: "https://supabase.com/docs/guides/database/postgres/enums"
canonical_url: "https://supabase.com/docs/guides/database/postgres/enums"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:30.967Z"
content_hash: "558b853f7cbd1b895855948c0b49cde5ba78282e6bc55f725a47ce03d41a5453"
menu_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing enums","Managing enums"]
section_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing enums","Managing enums"]
---
# 

Managing Enums in Postgres

* * *

Enums in Postgres are a custom data type. They allow you to define a set of values (or labels) that a column can hold. They are useful when you have a fixed set of possible values for a column.

## Creating enums[#](#creating-enums)

You can define a Postgres Enum using the `create type` statement. Here's an example:

```
1create type mood as enum (2  'happy',3  'sad',4  'excited',5  'calm'6);
```

In this example, we've created an Enum called "mood" with four possible values.

## When to use enums[#](#when-to-use-enums)

There is a lot of overlap between Enums and foreign keys. Both can be used to define a set of values for a column. However, there are some advantages to using Enums:

*   Performance: You can query a single table instead of finding the value from a lookup table.
*   Simplicity: Generally the SQL is easier to read and write.

There are also some disadvantages to using Enums:

*   Limited Flexibility: Adding and removing values requires modifying the database schema (i.e.: using migrations) rather than adding data to a table.
*   Maintenance Overhead: Enum types require ongoing maintenance. If your application's requirements change frequently, maintaining enums can become burdensome.

In general you should only use Enums when the list of values is small, fixed, and unlikely to change often. Things like "a list of continents" or "a list of departments" are good candidates for Enums.

## Using enums in tables[#](#using-enums-in-tables)

To use the Enum in a table, you can define a column with the Enum type. For example:

```
1create table person (2  id serial primary key,3  name text,4  current_mood mood5);
```

Here, the `current_mood` column can only have values from the "mood" Enum.

### Inserting data with enums[#](#inserting-data-with-enums)

You can insert data into a table with Enum columns by specifying one of the Enum values:

```
1insert into person2  (name, current_mood)3values4  ('Alice', 'happy');
```

### Querying data with enums[#](#querying-data-with-enums)

When querying data, you can filter and compare Enum values as usual:

```
1select * 2from person 3where current_mood = 'sad';
```

## Managing enums[#](#managing-enums)

You can manage your Enums using the `alter type` statement. Here are some examples:

### Updating enum values[#](#updating-enum-values)

You can update the value of an Enum column:

```
1update person2set current_mood = 'excited'3where name = 'Alice';
```

### Adding enum values[#](#adding-enum-values)

To add new values to an existing Postgres Enum, you can use the `ALTER TYPE` statement. Here's how you can do it:

Let's say you have an existing Enum called `mood`, and you want to add a new value, `content`:

```
1alter type mood add value 'content';
```

### Removing enum values[#](#removing-enum-values)

Even though it is possible, it is unsafe to remove enum values once they have been created. It's better to leave the enum value in place.

Read the [Postgres mailing list](https://www.postgresql.org/message-id/21012.1459434338%40sss.pgh.pa.us) for more information:

There is no `ALTER TYPE DELETE VALUE` in Postgres. Even if you delete every occurrence of an Enum value within a table (and vacuumed away those rows), the target value could still exist in upper index pages. If you delete the `pg_enum` entry you'll break the index.

### Getting a list of enum values[#](#getting-a-list-of-enum-values)

Check your existing Enum values by querying the enum\_range function:

```
1select enum_range(null::mood);
```

## Resources[#](#resources)

*   Official Postgres Docs: [Enumerated Types](https://www.postgresql.org/docs/current/datatype-enum.html)
