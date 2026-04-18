---
title: "Copy Objects"
source: "https://supabase.com/docs/guides/storage/management/copy-move-objects"
canonical_url: "https://supabase.com/docs/guides/storage/management/copy-move-objects"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:18.727Z"
content_hash: "12ad762704a68569b1f3ca0475f080abd0aeea381695126a179a18fc68528138"
menu_path: ["Storage","Storage","More","More","More","Management","Management","Copy / Move Objects","Copy / Move Objects"]
section_path: ["Storage","Storage","More","More","More","Management","Management","Copy / Move Objects","Copy / Move Objects"]
nav_prev: {"path": "supabase/docs/guides/storage/debugging/logs/index.md", "title": "Logs"}
nav_next: {"path": "supabase/docs/guides/storage/management/delete-objects/index.md", "title": "Delete Objects"}
---

# 

Copy Objects

## 

Learn how to copy and move objects

* * *

## Copy objects[#](#copy-objects)

You can copy objects between buckets or within the same bucket. Currently only objects up to 5 GB can be copied using the API.

When making a copy of an object, the owner of the new object will be the user who initiated the copy operation.

### Copying objects within the same bucket[#](#copying-objects-within-the-same-bucket)

To copy an object within the same bucket, use the `copy` method.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5await supabase.storage.from('avatars').copy('public/avatar1.png', 'private/avatar2.png')
```

### Copying objects across buckets[#](#copying-objects-across-buckets)

To copy an object across buckets, use the `copy` method and specify the destination bucket.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5await supabase.storage.from('avatars').copy('public/avatar1.png', 'private/avatar2.png', {6  destinationBucket: 'avatars2',7})
```

## Move objects[#](#move-objects)

You can move objects between buckets or within the same bucket. Currently only objects up to 5GB can be moved using the API.

When moving an object, the owner of the new object will be the user who initiated the move operation. Once the object is moved, the original object will no longer exist.

### Moving objects within the same bucket[#](#moving-objects-within-the-same-bucket)

To move an object within the same bucket, you can use the `move` method.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5const { data, error } = await supabase.storage6  .from('avatars')7  .move('public/avatar1.png', 'private/avatar2.png')
```

### Moving objects across buckets[#](#moving-objects-across-buckets)

To move an object across buckets, use the `move` method and specify the destination bucket.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5await supabase.storage.from('avatars').move('public/avatar1.png', 'private/avatar2.png', {6  destinationBucket: 'avatars2',7})
```

## Permissions[#](#permissions)

To **copy** objects, users need `select` permission on the source object and `insert` permission on the destination object. If the user also has `update` permission, the copy can be performed as an upsert, which will overwrite the destination object if it already exists.

To **move** objects, users need `select` and `update` permissions on the object.

For example:

```
1create policy "User can select their own objects (in any buckets)"2on storage.objects3for select4to authenticated5using (6    owner_id = (select auth.uid())7);89create policy "User can insert in their own folders (in any buckets)"10on storage.objects11for insert12to authenticated13with check (14    (storage.folder(name))[1] = (select auth.uid())15);1617create policy "User can update their own objects (in any buckets)"18on storage.objects19for update20to authenticated21using (22    owner_id = (select auth.uid())23);
```
