---
title: "The Storage Schema"
source: "https://supabase.com/docs/guides/storage/schema/design"
canonical_url: "https://supabase.com/docs/guides/storage/schema/design"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:29.237Z"
content_hash: "6bab5bb4905cea7c7557f4ca3031466bc7f7406c9fc36a3459d3117e12ca8671"
menu_path: ["Storage","Storage","More","More","More","Schema","Schema","Database Design","Database Design"]
section_path: ["Storage","Storage","More","More","More","Schema","Schema","Database Design","Database Design"]
---
# 

The Storage Schema

## 

Learn about the storage schema

* * *

Storage uses Postgres to store metadata regarding your buckets and objects. Users can use RLS (Row-Level Security) policies for access control. This data is stored in a dedicated schema within your project called `storage`.

When working with SQL, it's crucial to consider all records in Storage tables as read-only. All operations, including uploading, copying, moving, and deleting, should **exclusively go through the API**.

This is important because the storage schema only stores the metadata and the actual objects are stored in a provider like S3. Deleting the metadata doesn't remove the object in the underlying storage provider. This results in your object being inaccessible, but you'll still be billed for it.

Here is the schema that represents the Storage service:

![Storage schema design](/docs/img/storage/schema-design.png)

You have the option to query this table directly to retrieve information about your files in Storage without the need to go through our API.

## Modifying the schema[#](#modifying-the-schema)

We strongly recommend refraining from making any alterations to the `storage` schema and treating it as read-only. This approach is important because any modifications to the schema on your end could potentially clash with our future updates, leading to downtime.

However, we encourage you to add custom indexes as they can significantly improve the performance of the RLS policies you create for enforcing access control.
