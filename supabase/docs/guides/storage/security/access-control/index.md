---
title: "Storage Access Control"
source: "https://supabase.com/docs/guides/storage/security/access-control"
canonical_url: "https://supabase.com/docs/guides/storage/security/access-control"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:33.401Z"
content_hash: "321a437115ab03a4d21977a534c2eb1667a91251addd1678ca13cabaab03c337"
menu_path: ["Storage","Storage","More","More","More","Security","Security","Access Control","Access Control"]
section_path: ["Storage","Storage","More","More","More","Security","Security","Access Control","Access Control"]
nav_prev: {"path": "supabase/docs/guides/storage/schema/helper-functions/index.md", "title": "Storage Helper Functions"}
nav_next: {"path": "supabase/docs/guides/storage/security/ownership/index.md", "title": "Ownership"}
---

# 

Storage Access Control

* * *

Supabase Storage is designed to work perfectly with Postgres [Row Level Security](../../../database/postgres/row-level-security/index.md) (RLS).

You can use RLS to create [Security Access Policies](https://www.postgresql.org/docs/current/sql-createpolicy.html) that are incredibly powerful and flexible, allowing you to restrict access based on your business needs.

## Access policies[#](#access-policies)

By default Storage does not allow any uploads to buckets without RLS policies. You selectively allow certain operations by creating RLS policies on the `storage.objects` table.

You can find the documentation for the storage schema [here](../../schema/design/index.md) , and to simplify the process of crafting your policies, you can utilize these [helper functions](../../schema/helper-functions/index.md) .

The RLS policies required for different operations are documented [here](/docs/reference/javascript/storage-createbucket)

For example, the only RLS policy required for [uploading](/docs/reference/javascript/storage-from-upload) objects is to grant the `INSERT` permission to the `storage.objects` table.

To allow overwriting files using the `upsert` functionality you will need to additionally grant `SELECT` and `UPDATE` permissions.

## Policy examples[#](#policy-examples)

An easy way to get started would be to create RLS policies for `SELECT`, `INSERT`, `UPDATE`, `DELETE` operations and restrict the policies to meet your security requirements. For example, one can start with the following `INSERT` policy:

```
1create policy "policy_name"2ON storage.objects3for insert with check (4  true5);
```

and modify it to only allow authenticated users to upload assets to a specific bucket by changing it to:

```
1create policy "policy_name"2on storage.objects for insert to authenticated with check (3    -- restrict bucket4    bucket_id = 'my_bucket_id'5);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called `private` inside `my_bucket_id`:

```
1create policy "Allow authenticated uploads"2on storage.objects3for insert4to authenticated5with check (6  bucket_id = 'my_bucket_id' and7  (storage.foldername(name))[1] = 'private'8);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called with their `users.id` inside `my_bucket_id`:

```
1create policy "Allow authenticated uploads"2on storage.objects3for insert4to authenticated5with check (6  bucket_id = 'my_bucket_id' and7  (storage.foldername(name))[1] = (select auth.jwt()->>'sub')8);
```

Allow a user to access a file that was previously uploaded by the same user:

```
1create policy "Individual user Access"2on storage.objects for select3to authenticated4using ( (select auth.jwt()->>'sub') = owner_id );
```

* * *

## Bypassing access controls[#](#bypassing-access-controls)

If you exclusively use Storage from trusted clients, such as your own servers, and need to bypass the RLS policies, you can use the `service key` in the `Authorization` header. Service keys entirely bypass RLS policies, granting you unrestricted access to all Storage APIs.

Remember you should not share the service key publicly.
