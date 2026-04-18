---
title: "Delete Objects"
source: "https://supabase.com/docs/guides/storage/management/delete-objects"
canonical_url: "https://supabase.com/docs/guides/storage/management/delete-objects"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:20.190Z"
content_hash: "91e64c9d60a46bb9780227c6209e26a0babaa55cd581c28be9457aead0333768"
menu_path: ["Storage","Storage","More","More","More","Management","Management","Delete Objects","Delete Objects"]
section_path: ["Storage","Storage","More","More","More","Management","Management","Delete Objects","Delete Objects"]
nav_prev: {"path": "supabase/docs/guides/storage/management/copy-move-objects/index.md", "title": "Copy Objects"}
nav_next: {"path": "supabase/docs/guides/storage/management/download-objects/index.md", "title": "Download Objects"}
---

# 

Delete Objects

## 

Learn about deleting objects

* * *

When you delete one or more objects from a bucket, the files are permanently removed and not recoverable. You can delete a single object or multiple objects at once.

Deleting objects should always be done via the **Storage API** and NOT via a **SQL query**. Deleting objects via a SQL query will not remove the object from the bucket and will result in the object being orphaned.

## Delete objects[#](#delete-objects)

To delete one or more objects, use the `remove` method.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5await supabase.storage.from('bucket').remove(['object-path-2', 'folder/avatar2.png'])
```

When deleting objects, there is a limit of 1000 objects at a time using the `remove` method.

## RLS[#](#rls)

To delete an object, the user must have the `delete` permission on the object. For example:

```
1create policy "User can delete their own objects"2on storage.objects3for delete4TO authenticated5USING (6    owner = (select auth.uid()::text)7);
```


