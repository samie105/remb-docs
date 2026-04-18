---
title: "Storage Quickstart"
source: "https://supabase.com/docs/guides/storage/quickstart"
canonical_url: "https://supabase.com/docs/guides/storage/quickstart"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:06.232Z"
content_hash: "e9b271872773c9d94d48840e99090493af1a4de4df92adc834e112bfceded062"
menu_path: ["Storage","Storage","File Buckets","File Buckets","Quickstart","Quickstart"]
section_path: ["Storage","Storage","File Buckets","File Buckets","Quickstart","Quickstart"]
nav_prev: {"path": "supabase/docs/guides/storage/pricing/index.md", "title": "Pricing"}
nav_next: {"path": "supabase/docs/guides/telemetry/log-drains/index.md", "title": "Log Drains"}
---

# 

Storage Quickstart

## 

Learn how to use Supabase to store and serve files.

* * *

This guide shows the basic functionality of Supabase Storage. Find a full [example application on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management).

## Concepts[#](#concepts)

Supabase Storage consists of Files, Folders, and Buckets.

### Files[#](#files)

Files can be any sort of media file. This includes images, GIFs, and videos. It is best practice to store files outside of your database because of their sizes. For security, HTML files are returned as plain text.

### Folders[#](#folders)

Folders are a way to organize your files (just like on your computer). There is no right or wrong way to organize your files. You can store them in whichever folder structure suits your project.

### Buckets[#](#buckets)

Buckets are distinct containers for files and folders. You can think of them like "super folders". Generally you would create distinct buckets for different Security and Access Rules. For example, you might keep all video files in a "video" bucket, and profile pictures in an "avatar" bucket.

File, Folder, and Bucket names **must follow** [AWS object key naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) and avoid use of any other characters.

## Create a bucket[#](#create-a-bucket)

You can create a bucket using the Supabase Dashboard. Since the storage is interoperable with your Postgres database, you can also use SQL or our client libraries. Here we create a bucket called "avatars":

1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
2.  Click **New Bucket** and enter a name for the bucket.
3.  Click **Create Bucket**.

## Upload a file[#](#upload-a-file)

You can upload a file from the Dashboard, or within a browser using our JS libraries.

1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
2.  Select the bucket you want to upload the file to.
3.  Click **Upload File**.
4.  Select the file you want to upload.

## Download a file[#](#download-a-file)

You can download a file from the Dashboard, or within a browser using our JS libraries.

1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
2.  Select the bucket that contains the file.
3.  Select the file that you want to download.
4.  Click **Download**.

## Add security rules[#](#add-security-rules)

To restrict access to your files you can use either the Dashboard or SQL.

1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
2.  Click **Policies** in the sidebar.
3.  Click **Add Policies** in the `OBJECTS` table to add policies for Files. You can also create policies for Buckets.
4.  Choose whether you want the policy to apply to downloads (SELECT), uploads (INSERT), updates (UPDATE), or deletes (DELETE).
5.  Give your policy a unique name.
6.  Write the policy using SQL.

* * *
