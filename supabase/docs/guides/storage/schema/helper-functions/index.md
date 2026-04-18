---
title: "Storage Helper Functions"
source: "https://supabase.com/docs/guides/storage/schema/helper-functions"
canonical_url: "https://supabase.com/docs/guides/storage/schema/helper-functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:30.474Z"
content_hash: "a1cd1c0988b829b2bc2a9d668c1e240fcbf24bfcf3991c1374f1ee9ced2cbea5"
menu_path: ["Storage","Storage","More","More","More","Schema","Schema","Helper Functions","Helper Functions"]
section_path: ["Storage","Storage","More","More","More","Schema","Schema","Helper Functions","Helper Functions"]
nav_prev: {"path": "supabase/docs/guides/storage/schema/design/index.md", "title": "The Storage Schema"}
nav_next: {"path": "supabase/docs/guides/storage/security/access-control/index.md", "title": "Storage Access Control"}
---

# 

Storage Helper Functions

## 

Learn the storage schema

* * *

Supabase Storage provides SQL helper functions which you can use to write RLS policies.

### `storage.filename()`[#](#storagefilename)

Returns the name of a file. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `'avatar.png'`

**Usage**

This example demonstrates how you would allow any user to download a file called `favicon.ico`:

```
1create policy "Allow public downloads"2on storage.objects3for select4to public5using (6  storage.filename(name) = 'favicon.ico'7);
```

### `storage.foldername()`[#](#storagefoldername)

Returns an array path, with all of the subfolders that a file belongs to. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `[ 'public', 'subfolder' ]`

**Usage**

This example demonstrates how you would allow authenticated users to upload files to a folder called `private`:

```
1create policy "Allow authenticated uploads"2on storage.objects3for insert4to authenticated5with check (6  (storage.foldername(name))[1] = 'private'7);
```

### `storage.extension()`[#](#storageextension)

Returns the extension of a file. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `'png'`

**Usage**

This example demonstrates how you would allow restrict uploads to only PNG files inside a bucket called `cats`:

```
1create policy "Only allow PNG uploads"2on storage.objects3for insert4to authenticated5with check (6  bucket_id = 'cats' and storage.extension(name) = 'png'7);
```
