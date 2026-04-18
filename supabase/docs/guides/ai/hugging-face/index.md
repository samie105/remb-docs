---
title: "Hugging Face Inference API"
source: "https://supabase.com/docs/guides/ai/hugging-face"
canonical_url: "https://supabase.com/docs/guides/ai/hugging-face"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:48.366Z"
content_hash: "44ca7c40d5d906c555b4d32d1b0bef980ed926c0996692a21d3492d1d70155cf"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Hugging Face","Hugging Face"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Hugging Face","Hugging Face"]
nav_prev: {"path": "supabase/docs/guides/ai/google-colab/index.md", "title": "Google Colab"}
nav_next: {"path": "supabase/docs/guides/ai/hybrid-search/index.md", "title": "Hybrid search"}
---

# 

Hugging Face Inference API

* * *

[Hugging Face](https://huggingface.co) is an open source hub for AI/ML models and tools. With over 100,000 machine learning models available, Hugging Face provides a great way to integrate specialized AI & ML tasks into your application.

There are 3 ways to use Hugging Face models in your application:

1.  Use the [Transformers](https://huggingface.co/docs/transformers/index) Python library to perform inference in a Python backend.
2.  [Generate embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) directly in Edge Functions using Transformers.js.
3.  Use Hugging Face's hosted [Inference API](https://huggingface.co/inference-api) to execute AI tasks remotely on Hugging Face servers. This guide will walk you through this approach.

## AI tasks[#](#ai-tasks)

Below are some of the types of tasks you can perform with Hugging Face:

### Natural language[#](#natural-language)

*   [Summarization](https://huggingface.co/tasks/summarization)
*   [Text classification](https://huggingface.co/tasks/text-classification)
*   [Text generation](https://huggingface.co/tasks/text-generation)
*   [Translation](https://huggingface.co/tasks/translation)
*   [Fill in the blank](https://huggingface.co/tasks/fill-mask)

### Computer vision[#](#computer-vision)

*   [Image to text](https://huggingface.co/tasks/image-to-text)
*   [Text to image](https://huggingface.co/tasks/text-to-image)
*   [Image classification](https://huggingface.co/tasks/image-classification)
*   [Video classification](https://huggingface.co/tasks/video-classification)
*   [Object detection](https://huggingface.co/tasks/object-detection)
*   [Image segmentation](https://huggingface.co/tasks/image-segmentation)

### Audio[#](#audio)

*   [Text to speech](https://huggingface.co/tasks/text-to-speech)
*   [Speech to text](https://huggingface.co/tasks/automatic-speech-recognition)
*   [Audio classification](https://huggingface.co/tasks/audio-classification)

See a [full list of tasks](https://huggingface.co/tasks).

## Access token[#](#access-token)

First generate a Hugging Face access token for your app:

[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

Name your token based on the app its being used for and the environment. For example, if you are building an image generation app you might create 2 tokens:

*   "Image Generator (Dev)"
*   "Image Generator (Prod)"

Since we will be using this token for the inference API, choose the `read` role.

Though it is possible to use the Hugging Face inference API today without an access token, [you may be rate limited](https://huggingface.co/docs/huggingface.js/inference/README#usage).

To ensure you don't experience any unexpected downtime or errors, we recommend creating an access token.

## Edge Functions[#](#edge-functions)

Edge Functions are server-side TypeScript functions that run on-demand. Since Edge Functions run on a server, you can safely give them access to your Hugging Face access token.

You will need the `supabase` CLI [installed](/docs/guides/cli) for the following commands to work.

To create a new Edge Function, navigate to your local project and initialize Supabase if you haven't already:

```
1supabase init
```

Then create an Edge Function:

```
1supabase functions new text-to-image
```

Create a file called `.env.local` to store your Hugging Face access token:

```
1HUGGING_FACE_ACCESS_TOKEN=<your-token-here>
```

Let's modify the Edge Function to import Hugging Face's inference client and perform a `text-to-image` request:

```
1import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'2import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'34const hf = new HfInference(Deno.env.get('HUGGING_FACE_ACCESS_TOKEN'))56serve(async (req) => {7  const { prompt } = await req.json()89  const image = await hf.textToImage(10    {11      inputs: prompt,12      model: 'stabilityai/stable-diffusion-2',13    },14    {15      use_cache: false,16    }17  )1819  return new Response(image)20})
```

1.  This function creates a new instance of `HfInference` using the `HUGGING_FACE_ACCESS_TOKEN` environment variable.
    
2.  It expects a POST request that includes a JSON request body. The JSON body should include a parameter called `prompt` that represents the text-to-image prompt that we will pass to Hugging Face's inference API.
    
3.  Next we call `textToImage()`, passing in the user's prompt along with the model that we would like to use for the image generation. Today Hugging Face recommends `stabilityai/stable-diffusion-2`, but you can change this to any other text-to-image model. You can see a list of which models are supported for each task by navigating to their [models page](https://huggingface.co/models?pipeline_tag=text-to-image) and filtering by task.
    
4.  We set `use_cache` to `false` so that repeat queries with the same prompt will produce new images. If the task and model you are using is deterministic (will always produce the same result based on the same input), consider setting `use_cache` to `true` for faster responses.
    
5.  The `image` result returned from the API will be a `Blob`. We can pass the `Blob` directly into a `new Response()` which will automatically set the content type and body of the response from the `image`.
    

Finally let's serve the Edge Function locally to test it:

```
1supabase functions serve --env-file .env.local --no-verify-jwt
```

Remember to pass in the `.env.local` file using the `--env-file` parameter so that the Edge Function can access the `HUGGING_FACE_ACCESS_TOKEN`.

For demo purposes we set `--no-verify-jwt` to make it easy to test the Edge Function without passing in a JWT token. In a real application you will need to pass the JWT as a `Bearer` token in the `Authorization` header.

At this point, you can make an API request to your Edge Function using your preferred frontend framework (Next.js, React, Expo, etc). We can also test from the terminal using `curl`:

```
1curl --output result.jpg --location --request POST 'http://localhost:54321/functions/v1/text-to-image' \2  --header 'Content-Type: application/json' \3  --data '{"prompt":"Llama wearing sunglasses"}'
```

In this example, your generated image will save to `result.jpg`:

![Llama wearing sunglasses example](/docs/img/ai/hugging-face/llama-sunglasses-example.png)

## Next steps[#](#next-steps)

You can now create an Edge Function that invokes a Hugging Face task using your model of choice.

Try running some other [AI tasks](#ai-tasks).

## Resources[#](#resources)

*   Official [Hugging Face site](https://huggingface.co/).
*   Official [Hugging Face JS docs](https://huggingface.co/docs/huggingface.js).
*   [Generate image captions](/docs/guides/ai/examples/huggingface-image-captioning) using Hugging Face.
