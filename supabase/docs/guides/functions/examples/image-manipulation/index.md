---
title: "Image Manipulation"
source: "https://supabase.com/docs/guides/functions/examples/image-manipulation"
canonical_url: "https://supabase.com/docs/guides/functions/examples/image-manipulation"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:32.711Z"
content_hash: "5ca1dd14d570bf26e609fead95319c77b5406c8c387e1b8d8378a73dfc3bc200"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Image Transformation & Optimization","Image Transformation & Optimization"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Image Transformation & Optimization","Image Transformation & Optimization"]
nav_prev: {"path": "supabase/docs/guides/functions/examples/github-actions/index.md", "title": "GitHub Actions"}
nav_next: {"path": "supabase/docs/guides/functions/examples/mcp-server-mcp-lite/index.md", "title": "Building an MCP Server with mcp-lite"}
---

# 

Image Manipulation

* * *

Supabase Storage has [out-of-the-box support](/docs/guides/storage/serving/image-transformations?queryGroups=language&language=js) for the most common image transformations and optimizations you need. If you need to do anything custom beyond what Supabase Storage provides, you can use Edge Functions to write custom image manipulation scripts.

In this example, we will use [`magick-wasm`](https://github.com/dlemstra/magick-wasm) to perform image manipulations. `magick-wasm` is the WebAssembly port of the popular ImageMagick library and supports processing over 100 file formats.

Edge Functions currently doesn't support image processing libraries such as `Sharp`, which depend on native libraries. Only WASM-based libraries are supported.

### Prerequisites[#](#prerequisites)

Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.

### Create the Edge Function[#](#create-the-edge-function)

Create a new function locally:

```
1supabase functions new image-blur
```

### Write the function[#](#write-the-function)

In this example, we are implementing a function allowing users to upload an image and get a blurred thumbnail.

Here's the implementation in `index.ts` file:

```
1// This is an example showing how to use Magick WASM to do image manipulations in Edge Functions.2//3import {4  ImageMagick,5  initializeImageMagick,6  MagickFormat,7} from 'npm:@imagemagick/magick-wasm@0.0.30'89const wasmBytes = await Deno.readFile(10  new URL('magick.wasm', import.meta.resolve('npm:@imagemagick/magick-wasm@0.0.30'))11)12await initializeImageMagick(wasmBytes)1314Deno.serve(async (req) => {15  const formData = await req.formData()16  const content = await formData.get('file').bytes()1718  let result = ImageMagick.read(content, (img): Uint8Array => {19    // resize the image20    img.resize(500, 300)21    // add a blur of 60x522    img.blur(60, 5)2324    return img.write((data) => data)25  })2627  return new Response(result, { headers: { 'Content-Type': 'image/png' } })28})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/image-manipulation/index.ts)

### Test it locally[#](#test-it-locally)

You can test the function locally by running:

```
1supabase start2supabase functions serve --no-verify-jwt
```

Then, make a request using `curl` or your favorite API testing tool.

```
1curl --location '<http://localhost:54321/functions/v1/image-blur>' \\2--form 'file=@"/path/to/image.png"'3--output '/path/to/output.png'
```

If you open the `output.png` file you will find a transformed version of your original image.

### Deploy to your hosted project[#](#deploy-to-your-hosted-project)

Now, let's deploy the function to your Supabase project.

```
1supabase link2supabase functions deploy image-blur
```

Hosted Edge Functions have [limits](/docs/guides/functions/limits) on memory and CPU usage.

If you try to perform complex image processing or handle large images (> 5MB) your function may return a resource limit exceeded error.

