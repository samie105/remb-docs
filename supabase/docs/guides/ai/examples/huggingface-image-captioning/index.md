---
title: "Generate image captions using Hugging Face"
source: "https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning"
canonical_url: "https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:30.558Z"
content_hash: "69d643b328e01cd04cd7d075d049eedda72440b46ed5b6c514dd7d69f895c7a7"
menu_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Generate image captions using Hugging Face","Generate image captions using Hugging Face"]
section_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Generate image captions using Hugging Face","Generate image captions using Hugging Face"]
nav_prev: {"path": "supabase/docs/guides/ai/examples/building-chatgpt-plugins/index.md", "title": "Building ChatGPT plugins"}
nav_next: {"path": "supabase/docs/guides/ai/examples/image-search-openai-clip/index.md", "title": "Image Search with OpenAI CLIP"}
---

# 

Generate image captions using Hugging Face

## 

Use the Hugging Face Inference API to make calls to 100,000+ Machine Learning models from Supabase Edge Functions.

* * *

We can combine Hugging Face with [Supabase Storage](/storage) and [Database Webhooks](/docs/guides/database/webhooks) to automatically caption for any image we upload to a storage bucket.

## About Hugging Face[#](#about-hugging-face)

[Hugging Face](https://huggingface.co/) is the collaboration platform for the machine learning community.

[Huggingface.js](https://huggingface.co/docs/huggingface.js/index) provides a convenient way to make calls to 100,000+ Machine Learning models, making it easy to incorporate AI functionality into your [Supabase Edge Functions](/edge-functions).

## Setup[#](#setup)

*   Open your Supabase project dashboard or [create a new project](/dashboard/projects).
*   [Create a new bucket](/dashboard/project/_/storage/buckets) called `images`.
*   Generate TypeScript types from remote Database.
*   Create a new Database table called `image_caption`.
    *   Create `id` column of type `uuid` which references `storage.objects.id`.
    *   Create a `caption` column of type `text`.
*   Regenerate TypeScript types to include new `image_caption` table.
*   Deploy the function to Supabase: `supabase functions deploy huggingface-image-captioning`.
*   Create the Database Webhook in the [Supabase Dashboard](/dashboard/project/_/database/hooks) to trigger the `huggingface-image-captioning` function anytime a record is added to the `storage.objects` table.

## Generate TypeScript types[#](#generate-typescript-types)

To generate the types.ts file for the storage and public schemas, run the following command in the terminal:

```
1supabase gen types typescript --project-id=your-project-ref --schema=storage,public > supabase/functions/huggingface-image-captioning/types.ts
```

## Code[#](#code)

Find the complete code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/huggingface-image-captioning).

```
1import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'2import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'3import { createClient } from 'npm:@supabase/supabase-js@2'4import { Database } from './types.ts'56console.log('Hello from `huggingface-image-captioning` function!')78const hf = new HfInference(Deno.env.get('HUGGINGFACE_ACCESS_TOKEN'))910type SoRecord = Database['storage']['Tables']['objects']['Row']11interface WebhookPayload {12  type: 'INSERT' | 'UPDATE' | 'DELETE'13  table: string14  record: SoRecord15  schema: 'public'16  old_record: null | SoRecord17}1819serve(async (req) => {20  const payload: WebhookPayload = await req.json()21  const soRecord = payload.record22  const supabaseAdminClient = createClient<Database>(23    // Supabase API URL - env var exported by default when deployed.24    Deno.env.get('SUPABASE_URL') ?? '',25    // Supabase API SERVICE ROLE KEY - env var exported by default when deployed.26    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''27  )2829  // Construct image url from storage30  const { data, error } = await supabaseAdminClient.storage31    .from(soRecord.bucket_id!)32    .createSignedUrl(soRecord.path_tokens!.join('/'), 60)33  if (error) throw error34  const { signedUrl } = data3536  // Run image captioning with Huggingface37  const imgDesc = await hf.imageToText({38    data: await (await fetch(signedUrl)).blob(),39    model: 'nlpconnect/vit-gpt2-image-captioning',40  })4142  // Store image caption in Database table43  await supabaseAdminClient44    .from('image_caption')45    .insert({ id: soRecord.id!, caption: imgDesc.generated_text })46    .throwOnError()4748  return new Response('ok')49})
```

