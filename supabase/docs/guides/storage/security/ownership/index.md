---
title: "Ownership"
source: "https://supabase.com/docs/guides/storage/security/ownership"
canonical_url: "https://supabase.com/docs/guides/storage/security/ownership"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:33.111Z"
content_hash: "4018a560bc2ae70235e0de9b242ca08bf23fe9cb0b87d47feb864e723a98655c"
menu_path: ["Storage","Storage","More","More","More","Security","Security","Ownership","Ownership"]
section_path: ["Storage","Storage","More","More","More","Security","Security","Ownership","Ownership"]
---
# 

Ownership

* * *

When creating new buckets or objects in Supabase Storage, an owner is automatically assigned to the bucket or object. The owner is the user who created the resource and the value is derived from the `sub` claim in the JWT. We store the `owner` in the `owner_id` column.

When using the `service_key` to create a resource, the owner will not be set and the resource will be owned by anyone. This is also the case when you are creating Storage resources via the Dashboard.

The Storage schema has 2 fields to represent ownership: `owner` and `owner_id`. `owner` is deprecated and will be removed. Use `owner_id` instead.

## Access control[#](#access-control)

By itself, the ownership of a resource does not provide any access control. However, you can enforce the ownership by implementing access control against storage resources scoped to their owner.

For example, you can implement a policy where only the owner of an object can delete it. To do this, check the `owner_id` field of the object and compare it with the `sub` claim of the JWT:

```
1create policy "User can delete their own objects"2on storage.objects3for delete4to authenticated5using (6    owner_id = (select auth.uid()::text)7);
```

The use of RLS policies is just one way to enforce access control. You can also implement access control in your server code by following the same pattern.
