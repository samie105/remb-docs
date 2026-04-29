---
title: "Generate Images with Amazon Bedrock"
source: "https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator"
canonical_url: "https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:16.692Z"
content_hash: "64a548c43db8e779d1203df8897fdb6903a7ed1b561d821dfee82f63af1d435a"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Generating AI images","Generating AI images"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Generating AI images","Generating AI images"]
nav_prev: {"path": "../../error-handling/index.md", "title": "Error Handling"}
nav_next: {"path": "../cloudflare-turnstile/index.md", "title": "CAPTCHA support with Cloudflare Turnstile"}
---

# 

Generate Images with Amazon Bedrock

* * *

[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using the Amazon Bedrock JavaScript SDK in Supabase Edge Functions to generate images using the [Amazon Titan Image Generator G1](https://aws.amazon.com/blogs/machine-learning/use-amazon-titan-models-for-image-generation-editing-and-searching/) model.

## Setup[#](#setup)

*   In your AWS console, navigate to Amazon Bedrock and under "Request model access", select the Amazon Titan Image Generator G1 model.
*   In your Supabase project, create a `.env` file in the `supabase` directory with the following contents:

```
1AWS_DEFAULT_REGION="<your_region>"2AWS_ACCESS_KEY_ID="<replace_your_own_credentials>"3AWS_SECRET_ACCESS_KEY="<replace_your_own_credentials>"4AWS_SESSION_TOKEN="<replace_your_own_credentials>"56# Mocked config files7AWS_SHARED_CREDENTIALS_FILE="./aws/credentials"8AWS_CONFIG_FILE="./aws/config"
```

### Configure Storage[#](#configure-storage)

*   \[locally\] Run `supabase start`
*   Open Studio URL: [locally](http://127.0.0.1:54323/project/default/storage/buckets) | [hosted](https://app.supabase.com/project/_/storage/buckets)
*   Navigate to Storage
*   Click "New bucket"
*   Create a new public bucket called "images"

## Code[#](#code)

Create a new function in your project:

```
1supabase functions new amazon-bedrock
```

And add the code to the `index.ts` file:

```
1// We need to mock the file system for the AWS SDK to work.2import { prepareVirtualFile } from 'https://deno.land/x/mock_file@v1.1.2/mod.ts'34import { BedrockRuntimeClient, InvokeModelCommand } from 'npm:@aws-sdk/client-bedrock-runtime'5import { createClient } from 'npm:@supabase/supabase-js'6import { decode } from 'npm:base64-arraybuffer'78console.log('Hello from Amazon Bedrock!')910Deno.serve(async (req) => {11  prepareVirtualFile('./aws/config')12  prepareVirtualFile('./aws/credentials')1314  const client = new BedrockRuntimeClient({15    region: Deno.env.get('AWS_DEFAULT_REGION') ?? 'us-west-2',16    credentials: {17      accessKeyId: Deno.env.get('AWS_ACCESS_KEY_ID') ?? '',18      secretAccessKey: Deno.env.get('AWS_SECRET_ACCESS_KEY') ?? '',19      sessionToken: Deno.env.get('AWS_SESSION_TOKEN') ?? '',20    },21  })2223  const { prompt, seed } = await req.json()24  console.log(prompt)25  const input = {26    contentType: 'application/json',27    accept: '*/*',28    modelId: 'amazon.titan-image-generator-v1',29    body: JSON.stringify({30      taskType: 'TEXT_IMAGE',31      textToImageParams: { text: prompt },32      imageGenerationConfig: {33        numberOfImages: 1,34        quality: 'standard',35        cfgScale: 8.0,36        height: 512,37        width: 512,38        seed: seed ?? 0,39      },40    }),41  }4243  const command = new InvokeModelCommand(input)44  const response = await client.send(command)45  console.log(response)4647  if (response.$metadata.httpStatusCode === 200) {48    const { body, $metadata } = response4950    const textDecoder = new TextDecoder('utf-8')51    const jsonString = textDecoder.decode(body.buffer)52    const parsedData = JSON.parse(jsonString)53    console.log(parsedData)54    const image = parsedData.images[0]5556    const supabaseClient = createClient(57      // Supabase API URL - env var exported by default.58      Deno.env.get('SUPABASE_URL')!,59      // Supabase API ANON KEY - env var exported by default.60      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!61    )6263    const { data: upload, error: uploadError } = await supabaseClient.storage64      .from('images')65      .upload(`${$metadata.requestId ?? ''}.png`, decode(image), {66        contentType: 'image/png',67        cacheControl: '3600',68        upsert: false,69      })70    if (!upload) {71      return Response.json(uploadError)72    }73    const { data } = supabaseClient.storage.from('images').getPublicUrl(upload.path!)74    return Response.json(data)75  }7677  return Response.json(response)78})
```

## Run the function locally[#](#run-the-function-locally)

1.  Run `supabase start` (see: [https://supabase.com/docs/reference/cli/supabase-start](https://supabase.com/docs/reference/cli/supabase-start))
2.  Start with env: `supabase functions serve --env-file supabase/.env`
3.  Make an HTTP request:

```
1curl -i --location --request POST 'http://127.0.0.1:54321/functions/v1/amazon-bedrock' \2    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0' \3    --header 'Content-Type: application/json' \4    --data '{"prompt":"A beautiful picture of a bird"}'
```

4.  Navigate back to your storage bucket. You might have to hit the refresh button to see the uploaded image.

## Deploy to your hosted project[#](#deploy-to-your-hosted-project)

```
1supabase link2supabase functions deploy amazon-bedrock3supabase secrets set --env-file supabase/.env
```

You've now deployed a serverless function that uses AI to generate and upload images to your Supabase storage bucket.
