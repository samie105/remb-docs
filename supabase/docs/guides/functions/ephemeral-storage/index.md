---
title: "File Storage"
source: "https://supabase.com/docs/guides/functions/ephemeral-storage"
canonical_url: "https://supabase.com/docs/guides/functions/ephemeral-storage"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:30.714Z"
content_hash: "38c835e70ac8718cf58d7121dc166d1e618d5dbe8b0bebafe42646da4cc7e167"
menu_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","File Storage","File Storage"]
section_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","File Storage","File Storage"]
nav_prev: {"path": "supabase/docs/guides/functions/development-tips/index.md", "title": "Development tips"}
nav_next: {"path": "supabase/docs/guides/functions/error-handling/index.md", "title": "Error Handling"}
---

# 

File Storage

## 

Use persistent and ephemeral file storage

* * *

Edge Functions provides two flavors of file storage:

*   Persistent - backed by S3 protocol, can read/write from any S3 compatible bucket, including Supabase Storage
*   Ephemeral - You can read and write files to the `/tmp` directory. Only suitable for temporary operations

You can use file storage to:

*   Handle complex file transformations and workflows
*   Do data migrations between projects
*   Process user uploaded files and store them
*   Unzip archives and process contents before saving to database

* * *

## Persistent Storage[#](#persistent-storage)

The persistent storage option is built on top of the S3 protocol. It allows you to mount any S3-compatible bucket, including Supabase Storage Buckets, as a directory for your Edge Functions. You can perform operations such as reading and writing files to the mounted buckets as you would in a POSIX file system.

To access an S3 bucket from Edge Functions, you must set the following for environment variables in Edge Function Secrets.

*   `S3FS_ENDPOINT_URL`
*   `S3FS_REGION`
*   `S3FS_ACCESS_KEY_ID`
*   `S3FS_SECRET_ACCESS_KEY`

[Follow this guide](/docs/guides/storage/s3/authentication) to enable and create an access key for Supabase Storage S3.

To access a file path in your mounted bucket from your Edge Function, use the prefix `/s3/YOUR-BUCKET-NAME`.

```
1// read from S3 bucket2const data = await Deno.readFile('/s3/my-bucket/results.csv')34// make a directory5await Deno.mkdir('/s3/my-bucket/sub-dir')67// write to S3 bucket8await Deno.writeTextFile('/s3/my-bucket/demo.txt', 'hello world')
```

## Ephemeral storage[#](#ephemeral-storage)

Ephemeral storage will reset on each function invocation. This means the files you write during an invocation can only be read within the same invocation.

You can use [Deno File System APIs](https://docs.deno.com/api/deno/file-system) or the [`node:fs`](https://docs.deno.com/api/node/fs/) module to access the `/tmp` path.

```
1Deno.serve(async (req) => {2  if (req.headers.get('content-type') !== 'application/zip') {3    return new Response('file must be a zip file', {4      status: 400,5    })6  }78  const uploadId = crypto.randomUUID()9  await Deno.writeFile('/tmp/' + uploadId, req.body)1011  // E.g. extract and process the zip file12  const zipFile = await Deno.readFile('/tmp/' + uploadId)13  // You could use a zip library to extract contents14  const extracted = await extractZip(zipFile)1516  // Or process the file directly17  console.log(`Processing zip file: ${uploadId}, size: ${zipFile.length} bytes`)18})
```

* * *

## Common use cases[#](#common-use-cases)

### Archive processing with background tasks[#](#archive-processing-with-background-tasks)

You can use ephemeral storage with [Background Tasks](/docs/guides/functions/background-tasks) to handle large file processing operations that exceed memory limits.

Imagine you have a Photo Album application that accepts photo uploads as zip files. A streaming implementation will run into memory limit errors with zip files exceeding 100MB, as it retains all archive files in memory simultaneously.

You can write the zip file to ephemeral storage first, then use a background task to extract and upload files to Supabase Storage. This way, you only read parts of the zip file to the memory.

```
1import { BlobWriter, ZipReader } from 'https://deno.land/x/zipjs/index.js'2import { createClient } from 'jsr:@supabase/supabase-js@2'34const supabase = createClient(5  Deno.env.get('SUPABASE_URL'),6  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')7)89async function processZipFile(uploadId: string, filepath: string) {10  const file = await Deno.open(filepath, { read: true })11  const zipReader = new ZipReader(file.readable)12  const entries = await zipReader.getEntries()1314  await supabase.storage.createBucket(uploadId, { public: false })1516  await Promise.all(17    entries.map(async (entry) => {18      if (entry.directory) return1920      // Read file entry from temp storage21      const blobWriter = new BlobWriter()22      const blob = await entry.getData(blobWriter)2324      // Upload to permanent storage25      await supabase.storage.from(uploadId).upload(entry.filename, blob)2627      console.log('uploaded', entry.filename)28    })29  )3031  await zipReader.close()32}3334Deno.serve(async (req) => {35  const uploadId = crypto.randomUUID()36  const filepath = `/tmp/${uploadId}.zip`3738  // Write zip to ephemeral storage39  await Deno.writeFile(filepath, req.body)4041  // Process in background to avoid memory limits42  EdgeRuntime.waitUntil(processZipFile(uploadId, filepath))4344  return new Response(JSON.stringify({ uploadId }), {45    headers: { 'Content-Type': 'application/json' },46  })47})
```

### Image manipulation[#](#image-manipulation)

Custom image manipulation workflows using [`magick-wasm`](/docs/guides/functions/examples/image-manipulation).

```
1Deno.serve(async (req) => {2  // Save uploaded image to temp storage3  const imagePath = `/tmp/input-${crypto.randomUUID()}.jpg`4  await Deno.writeFile(imagePath, req.body)56  // Process image with magick-wasm7  const processedPath = `/tmp/output-${crypto.randomUUID()}.jpg`8  // ... image manipulation logic910  // Read processed image and return11  const processedImage = await Deno.readFile(processedPath)12  return new Response(processedImage, {13    headers: { 'Content-Type': 'image/jpeg' },14  })15})
```

* * *

## Using synchronous file APIs[#](#using-synchronous-file-apis)

You can safely use the following synchronous Deno APIs (and their Node counterparts) _during initial script evaluation_:

*   Deno.statSync
*   Deno.removeSync
*   Deno.writeFileSync
*   Deno.writeTextFileSync
*   Deno.readFileSync
*   Deno.readTextFileSync
*   Deno.mkdirSync
*   Deno.makeTempDirSync
*   Deno.readDirSync

**Keep in mind** that the sync APIs are available only during initial script evaluation and aren’t supported in callbacks like HTTP handlers or `setTimeout`.

```
1Deno.statSync('...') // ✅23setTimeout(() => {4  Deno.statSync('...') // 💣 ERROR! Deno.statSync is blocklisted on the current context5})67Deno.serve(() => {8  Deno.statSync('...') // 💣 ERROR! Deno.statSync is blocklisted on the current context9})
```

* * *

## Limits[#](#limits)

There are no limits on S3 buckets you mount for Persistent storage.

Ephemeral Storage:

*   Free projects: Up to 256MB of ephemeral storage
*   Paid projects: Up to 512MB of ephemeral storage
