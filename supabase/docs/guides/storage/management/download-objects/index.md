---
title: "Download Objects"
source: "https://supabase.com/docs/guides/storage/management/download-objects"
canonical_url: "https://supabase.com/docs/guides/storage/management/download-objects"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:20.730Z"
content_hash: "3cd52900efea2fae32bf5e018f6b451deddbdfd49aa512d47a9062add304b06a"
menu_path: ["Storage","Storage","More","More","More","Management","Management","Download Objects","Download Objects"]
section_path: ["Storage","Storage","More","More","More","Management","Management","Download Objects","Download Objects"]
nav_prev: {"path": "supabase/docs/guides/storage/management/delete-objects/index.md", "title": "Delete Objects"}
nav_next: {"path": "supabase/docs/guides/storage/production/scaling/index.md", "title": "Storage Optimizations"}
---

# 

Download Objects

## 

Learn about downloading objects

* * *

You can download Supabase Storage files can in a variety of ways depending on your use case.

## From the Dashboard[#](#from-the-dashboard)

You can download individual files directly from the [**Storage > Files**](/dashboard/project/_/storage/buckets) section of the Dashboard by browsing to your bucket and selecting files.

## Using the Supabase CLI[#](#using-the-supabase-cli)

You can use the `supabase storage` commands to list and copy objects from your linked project.

See the [CLI reference](/docs/reference/cli/supabase-storage) for available commands.

## Using an S3-compatible client[#](#using-an-s3-compatible-client)

Supabase Storage exposes an S3-compatible endpoint, which means you can use tools like [Cyberduck](https://cyberduck.io/) (via a connection profile), AWS CLI, or rclone to browse and download your files.

To connect:

1.  Go to [**Storage > Configuration > S3**](/dashboard/project/_/storage/s3) section of the Dashboard.
2.  Enable the S3 protocol and generate an access key + secret key pair (Save it immediately as it is shown once).
3.  Use your S3-compatible tool with the endpoint and credentials from the Dashboard.

See the [S3 authentication doc](/docs/guides/storage/s3/authentication) for full connection details.

For downloading a large number of objects, using an S3-compatible tool like rclone or Cyberduck is significantly more efficient than downloading files individually.

## Using migration scripts[#](#using-migration-scripts)

For bulk downloads or project migrations, you can use the scripts from our migration docs:

*   **Node.js script** — see "Migrating storage objects" in the [migration guide](/docs/guides/platform/migrating-within-supabase/backup-restore)
*   **Google Colab script** — see "Migrate storage objects to new project's S3 storage" in the [dashboard restore guide](/docs/guides/platform/migrating-within-supabase/dashboard-restore)

## File metadata[#](#file-metadata)

File metadata is stored separately from the actual files. It lives in the `storage.buckets` and `storage.objects` tables in your Postgres database. If you need a complete backup (files + metadata), see the [backup and restore guide](/docs/guides/platform/migrating-within-supabase/backup-restore).


