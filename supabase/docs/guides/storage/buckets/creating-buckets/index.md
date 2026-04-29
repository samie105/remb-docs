---
title: "Creating Buckets"
source: "https://supabase.com/docs/guides/storage/buckets/creating-buckets"
canonical_url: "https://supabase.com/docs/guides/storage/buckets/creating-buckets"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:07.628Z"
content_hash: "bac327a22902cccab62ac7c87e37874e81ae9cb55470ba13d882c414b09c4cf2"
menu_path: ["Storage","Storage","File Buckets","File Buckets","Creating Buckets","Creating Buckets"]
section_path: ["Storage","Storage","File Buckets","File Buckets","Creating Buckets","Creating Buckets"]
nav_prev: {"path": "supabase/docs/guides/storage/analytics/query-with-postgres/index.md", "title": "Query with Postgres"}
nav_next: {"path": "supabase/docs/guides/storage/buckets/fundamentals/index.md", "title": "Storage Buckets"}
---

# 

Creating Buckets

* * *

You can create a bucket using the Supabase Dashboard. Since storage is interoperable with your Postgres database, you can also use SQL or our client libraries. Here we create a bucket called "avatars":

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)34// ---cut---5// Use the JS library to create a bucket.67const { data, error } = await supabase.storage.createBucket('avatars', {8  public: true, // default: false9})
```

[Reference.](/docs/reference/javascript/storage-createbucket)

## Restricting uploads[#](#restricting-uploads)

When creating a bucket you can add additional configurations to restrict the type or size of files you want this bucket to contain.

For example, imagine you want to allow your users to upload only images to the `avatars` bucket and the size must not be greater than 1MB. You can achieve the following by providing `allowedMimeTypes` and `maxFileSize`:

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)34// ---cut---5// Use the JS library to create a bucket.67const { data, error } = await supabase.storage.createBucket('avatars', {8  public: true,9  allowedMimeTypes: ['image/*'],10  fileSizeLimit: '1MB',11})
```

If an upload request doesn't meet the above restrictions it will be rejected. See [File Limits](/docs/guides/storage/uploads/file-limits) for more information.
