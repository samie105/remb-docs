---
title: "Streaming Speech with ElevenLabs"
source: "https://supabase.com/docs/guides/functions/examples/elevenlabs-generate-speech-stream"
canonical_url: "https://supabase.com/docs/guides/functions/examples/elevenlabs-generate-speech-stream"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:25.310Z"
content_hash: "fa2025a05ca6690c535fbb59b82482da3fb278f45ea364a3f952a7a7450b7564"
menu_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Text To Speech with ElevenLabs","Text To Speech with ElevenLabs"]
section_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Text To Speech with ElevenLabs","Text To Speech with ElevenLabs"]
---
# 

Streaming Speech with ElevenLabs

## 

Generate and stream speech through Supabase Edge Functions. Store speech in Supabase Storage and cache responses via built-in CDN.

* * *

## Introduction[#](#introduction)

In this tutorial you will learn how to build an edge API to generate, stream, store, and cache speech using Supabase Edge Functions, Supabase Storage, and [ElevenLabs text to speech API](https://elevenlabs.io/text-to-speech).

Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage).

## Requirements[#](#requirements)

*   An ElevenLabs account with an [API key](/app/settings/api-keys).
*   A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
*   The [Supabase CLI](/docs/guides/local-development) installed on your machine.
*   The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your favourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).

## Setup[#](#setup)

### Create a Supabase project locally[#](#create-a-supabase-project-locally)

After installing the [Supabase CLI](/docs/guides/local-development), run the following command to create a new Supabase project locally:

```
1supabase init
```

### Configure the storage bucket[#](#configure-the-storage-bucket)

You can configure the Supabase CLI to automatically generate a storage bucket by adding this configuration in the `config.toml` file:

```
1[storage.buckets.audio]2public = false3file_size_limit = "50MiB"4allowed_mime_types = ["audio/mp3"]5objects_path = "./audio"
```

Upon running `supabase start` this will create a new storage bucket in your local Supabase project. Should you want to push this to your hosted Supabase project, you can run `supabase seed buckets --linked`.

### Configure background tasks for Supabase Edge Functions[#](#configure-background-tasks-for-supabase-edge-functions)

To use background tasks in Supabase Edge Functions when developing locally, you need to add the following configuration in the `config.toml` file:

```
1[edge_runtime]2policy = "per_worker"
```

When running with `per_worker` policy, Function won't auto-reload on edits. You will need to manually restart it by running `supabase functions serve`.

### Create a Supabase Edge Function for speech generation[#](#create-a-supabase-edge-function-for-speech-generation)

Create a new Edge Function by running the following command:

```
1supabase functions new text-to-speech
```

If you're using VS Code or Cursor, select `y` when the CLI prompts "Generate VS Code settings for Deno? \[y/N\]"!

### Set up the environment variables[#](#set-up-the-environment-variables)

Within the `supabase/functions` directory, create a new `.env` file and add the following variables:

```
1# Find / create an API key at https://elevenlabs.io/app/settings/api-keys2ELEVENLABS_API_KEY=your_api_key
```

### Dependencies[#](#dependencies)

The project uses a couple of dependencies:

*   The [@supabase/supabase-js](/docs/reference/javascript) library to interact with the Supabase database.
*   The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the text-to-speech API.
*   The open-source [object-hash](https://www.npmjs.com/package/object-hash) to generate a hash from the request parameters.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.

## Code the Supabase Edge Function[#](#code-the-supabase-edge-function)

In your newly created `supabase/functions/text-to-speech/index.ts` file, add the following code:

```
1// Setup type definitions for built-in Supabase Runtime APIs2import 'jsr:@supabase/functions-js/edge-runtime.d.ts'3import { createClient } from 'npm:@supabase/supabase-js@2'4import { ElevenLabsClient } from 'npm:elevenlabs@1.52.0'5import * as hash from 'npm:object-hash'67const supabase = createClient(8  Deno.env.get('SUPABASE_URL')!,9  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!10)1112const client = new ElevenLabsClient({13  apiKey: Deno.env.get('ELEVENLABS_API_KEY'),14})1516// Upload audio to Supabase Storage in a background task17async function uploadAudioToStorage(stream: ReadableStream, requestHash: string) {18  const { data, error } = await supabase.storage19    .from('audio')20    .upload(`${requestHash}.mp3`, stream, {21      contentType: 'audio/mp3',22    })2324  console.log('Storage upload result', { data, error })25}2627Deno.serve(async (req) => {28  // To secure your function for production, you can for example validate the request origin,29  // or append a user access token and validate it with Supabase Auth.30  console.log('Request origin', req.headers.get('host'))31  const url = new URL(req.url)32  const params = new URLSearchParams(url.search)33  const text = params.get('text')34  const voiceId = params.get('voiceId') ?? 'JBFqnCBsd6RMkjVDRZzb'3536  const requestHash = hash.MD5({ text, voiceId })37  console.log('Request hash', requestHash)3839  // Check storage for existing audio file40  const { data } = await supabase.storage.from('audio').createSignedUrl(`${requestHash}.mp3`, 60)4142  if (data) {43    console.log('Audio file found in storage', data)44    const storageRes = await fetch(data.signedUrl)45    if (storageRes.ok) return storageRes46  }4748  if (!text) {49    return new Response(JSON.stringify({ error: 'Text parameter is required' }), {50      status: 400,51      headers: { 'Content-Type': 'application/json' },52    })53  }5455  try {56    console.log('ElevenLabs API call')57    const response = await client.textToSpeech.convertAsStream(voiceId, {58      output_format: 'mp3_44100_128',59      model_id: 'eleven_multilingual_v2',60      text,61    })6263    const stream = new ReadableStream({64      async start(controller) {65        for await (const chunk of response) {66          controller.enqueue(chunk)67        }68        controller.close()69      },70    })7172    // Branch stream to Supabase Storage73    const [browserStream, storageStream] = stream.tee()7475    // Upload to Supabase Storage in the background76    EdgeRuntime.waitUntil(uploadAudioToStorage(storageStream, requestHash))7778    // Return the streaming response immediately79    return new Response(browserStream, {80      headers: {81        'Content-Type': 'audio/mpeg',82      },83    })84  } catch (error) {85    console.log('error', { error })86    return new Response(JSON.stringify({ error: error.message }), {87      status: 500,88      headers: { 'Content-Type': 'application/json' },89    })90  }91})
```

## Run locally[#](#run-locally)

To run the function locally, run the following commands:

```
1supabase start
```

Once the local Supabase stack is up and running, run the following command to start the function and observe the logs:

```
1supabase functions serve
```

### Try it out[#](#try-it-out)

Navigate to `http://127.0.0.1:54321/functions/v1/text-to-speech?text=hello%20world` to hear the function in action.

Afterwards, navigate to `http://127.0.0.1:54323/project/default/storage/buckets/audio` to see the audio file in your local Supabase Storage bucket.

## Deploy to Supabase[#](#deploy-to-supabase)

If you haven't already, create a new Supabase account at [database.new](https://database.new) and link the local project to your Supabase account:

```
1supabase link
```

Once done, run the following command to deploy the function:

```
1supabase functions deploy
```

### Set the function secrets[#](#set-the-function-secrets)

Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:

```
1supabase secrets set --env-file supabase/functions/.env
```

## Test the function[#](#test-the-function)

The function is designed in a way that it can be used directly as a source for an `<audio>` element.

```
1<audio2  src="https://${SUPABASE_PROJECT_REF}.supabase.co/functions/v1/text-to-speech?text=Hello%2C%20world!&voiceId=JBFqnCBsd6RMkjVDRZzb"3  controls4/>
```

You can find an example frontend implementation in the complete code example on [GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage/src/pages/Index.tsx).
