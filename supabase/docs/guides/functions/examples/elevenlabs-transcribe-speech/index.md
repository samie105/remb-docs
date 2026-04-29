---
title: "Transcription Telegram Bot"
source: "https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech"
canonical_url: "https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:29.354Z"
content_hash: "055d8bd456b33176b8005617b73ed8c70f772060f9cb9cf73c6f39025c2eeb2f"
menu_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Speech Transcription with ElevenLabs","Speech Transcription with ElevenLabs"]
section_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Speech Transcription with ElevenLabs","Speech Transcription with ElevenLabs"]
nav_prev: {"path": "../elevenlabs-generate-speech-stream/index.md", "title": "Streaming Speech with ElevenLabs"}
nav_next: {"path": "../github-actions/index.md", "title": "GitHub Actions"}
---

# 

Transcription Telegram Bot

## 

Build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript with Deno in Supabase Edge Functions.

* * *

## Introduction[#](#introduction)

In this tutorial you will learn how to build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript and the ElevenLabs Scribe model via the [speech to text API](https://elevenlabs.io/speech-to-text).

To check out what the end result will look like, you can test out the [t.me/ElevenLabsScribeBot](https://t.me/ElevenLabsScribeBot)

Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/speech-to-text/telegram-transcription-bot).

## Requirements[#](#requirements)

*   An ElevenLabs account with an [API key](/app/settings/api-keys).
*   A [Supabase](https://supabase.com) account (you can sign up for a free account via [database.new](https://database.new)).
*   The [Supabase CLI](/docs/guides/local-development) installed on your machine.
*   The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed on your machine and optionally [setup in your favourite IDE](https://docs.deno.com/runtime/getting_started/setup_your_environment).
*   A [Telegram](https://telegram.org) account.

## Setup[#](#setup)

### Register a Telegram bot[#](#register-a-telegram-bot)

Use the [BotFather](https://t.me/BotFather) to create a new Telegram bot. Run the `/newbot` command and follow the instructions to create a new bot. At the end, you will receive your secret bot token. Note it down securely for the next step.

![BotFather](/docs/img/guides/functions/elevenlabs/bot-father.png)

### Create a Supabase project locally[#](#create-a-supabase-project-locally)

After installing the [Supabase CLI](/docs/guides/local-development), run the following command to create a new Supabase project locally:

```
1supabase init
```

### Create a database table to log the transcription results[#](#create-a-database-table-to-log-the-transcription-results)

Next, create a new database table to log the transcription results:

```
1supabase migrations new init
```

This will create a new migration file in the `supabase/migrations` directory. Open the file and add the following SQL:

```
1CREATE TABLE IF NOT EXISTS transcription_logs (2  id BIGSERIAL PRIMARY KEY,3  file_type VARCHAR NOT NULL,4  duration INTEGER NOT NULL,5  chat_id BIGINT NOT NULL,6  message_id BIGINT NOT NULL,7  username VARCHAR,8  transcript TEXT,9  language_code VARCHAR,10  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,11  error TEXT12);1314ALTER TABLE transcription_logs ENABLE ROW LEVEL SECURITY;
```

### Create a Supabase Edge Function to handle Telegram webhook requests[#](#create-a-supabase-edge-function-to-handle-telegram-webhook-requests)

Next, create a new Edge Function to handle Telegram webhook requests:

```
1supabase functions new scribe-bot
```

If you're using VS Code or Cursor, select `y` when the CLI prompts "Generate VS Code settings for Deno? \[y/N\]"!

### Set up the environment variables[#](#set-up-the-environment-variables)

Within the `supabase/functions` directory, create a new `.env` file and add the following variables:

```
1# Find / create an API key at https://elevenlabs.io/app/settings/api-keys2ELEVENLABS_API_KEY=your_api_key34# The bot token you received from the BotFather.5TELEGRAM_BOT_TOKEN=your_bot_token67# A random secret chosen by you to secure the function.8FUNCTION_SECRET=random_secret
```

### Dependencies[#](#dependencies)

The project uses a couple of dependencies:

*   The open-source [grammY Framework](https://grammy.dev/) to handle the Telegram webhook requests.
*   The [@supabase/supabase-js](/docs/reference/javascript) library to interact with the Supabase database.
*   The ElevenLabs [JavaScript SDK](/docs/quickstart) to interact with the speech-to-text API.

Since Supabase Edge Function uses the [Deno runtime](https://deno.land/), you don't need to install the dependencies, rather you can [import](https://docs.deno.com/examples/npm/) them via the `npm:` prefix.

## Code the Telegram bot[#](#code-the-telegram-bot)

In your newly created `scribe-bot/index.ts` file, add the following code:

```
1import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.34.0/mod.ts'2import 'jsr:@supabase/functions-js/edge-runtime.d.ts'3import { createClient } from 'npm:@supabase/supabase-js@2'4import { ElevenLabsClient } from 'npm:elevenlabs@1.50.5'56console.log(`Function "elevenlabs-scribe-bot" up and running!`)78const elevenLabsClient = new ElevenLabsClient({9  apiKey: Deno.env.get('ELEVENLABS_API_KEY') || '',10})1112const supabase = createClient(13  Deno.env.get('SUPABASE_URL') || '',14  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''15)1617async function scribe({18  fileURL,19  fileType,20  duration,21  chatId,22  messageId,23  username,24}: {25  fileURL: string26  fileType: string27  duration: number28  chatId: number29  messageId: number30  username: string31}) {32  let transcript: string | null = null33  let languageCode: string | null = null34  let errorMsg: string | null = null35  try {36    const sourceFileArrayBuffer = await fetch(fileURL).then((res) => res.arrayBuffer())37    const sourceBlob = new Blob([sourceFileArrayBuffer], {38      type: fileType,39    })4041    const scribeResult = await elevenLabsClient.speechToText.convert({42      file: sourceBlob,43      model_id: 'scribe_v1',44      tag_audio_events: false,45    })4647    transcript = scribeResult.text48    languageCode = scribeResult.language_code4950    // Reply to the user with the transcript51    await bot.api.sendMessage(chatId, transcript, {52      reply_parameters: { message_id: messageId },53    })54  } catch (error) {55    errorMsg = error.message56    console.log(errorMsg)57    await bot.api.sendMessage(chatId, 'Sorry, there was an error. Please try again.', {58      reply_parameters: { message_id: messageId },59    })60  }61  // Write log to Supabase.62  const logLine = {63    file_type: fileType,64    duration,65    chat_id: chatId,66    message_id: messageId,67    username,68    language_code: languageCode,69    error: errorMsg,70  }71  console.log({ logLine })72  await supabase.from('transcription_logs').insert({ ...logLine, transcript })73}7475const telegramBotToken = Deno.env.get('TELEGRAM_BOT_TOKEN')76const bot = new Bot(telegramBotToken || '')77const startMessage = `Welcome to the ElevenLabs Scribe Bot\\! I can transcribe speech in 99 languages with super high accuracy\\!78    \nTry it out by sending or forwarding me a voice message, video, or audio file\\!79    \n[Learn more about Scribe](https://elevenlabs.io/speech-to-text) or [build your own bot](https://elevenlabs.io/docs/cookbooks/speech-to-text/telegram-bot)\\!80  `81bot.command('start', (ctx) => ctx.reply(startMessage.trim(), { parse_mode: 'MarkdownV2' }))8283bot.on([':voice', ':audio', ':video'], async (ctx) => {84  try {85    const file = await ctx.getFile()86    const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`87    const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio8889    if (!fileMeta) {90      return ctx.reply('No video|audio|voice metadata found. Please try again.')91    }9293    // Run the transcription in the background.94    EdgeRuntime.waitUntil(95      scribe({96        fileURL,97        fileType: fileMeta.mime_type!,98        duration: fileMeta.duration,99        chatId: ctx.chat.id,100        messageId: ctx.message?.message_id!,101        username: ctx.from?.username || '',102      })103    )104105    // Reply to the user immediately to let them know we received their file.106    return ctx.reply('Received. Scribing...')107  } catch (error) {108    console.error(error)109    return ctx.reply(110      'Sorry, there was an error getting the file. Please try again with a smaller file!'111    )112  }113})114115const handleUpdate = webhookCallback(bot, 'std/http')116117Deno.serve(async (req) => {118  try {119    const url = new URL(req.url)120    if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {121      return new Response('not allowed', { status: 405 })122    }123124    return await handleUpdate(req)125  } catch (err) {126    console.error(err)127  }128})
```

## Deploy to Supabase[#](#deploy-to-supabase)

If you haven't already, create a new Supabase account at [database.new](https://database.new) and link the local project to your Supabase account:

```
1supabase link
```

### Apply the database migrations[#](#apply-the-database-migrations)

Run the following command to apply the database migrations from the `supabase/migrations` directory:

```
1supabase db push
```

Navigate to the [table editor](/dashboard/project/_/editor) in your Supabase dashboard and you should see and empty `transcription_logs` table.

![Empty table](/docs/img/guides/functions/elevenlabs/supa-empty-table.png)

Lastly, run the following command to deploy the Edge Function:

```
1supabase functions deploy --no-verify-jwt scribe-bot
```

Navigate to the [Edge Functions view](/dashboard/project/_/functions) in your Supabase dashboard and you should see the `scribe-bot` function deployed. Make a note of the function URL as you'll need it later, it should look something like `https://<project-ref>.functions.supabase.co/scribe-bot`.

![Edge Function deployed](/docs/img/guides/functions/elevenlabs/supa-edge-function-deployed.png)

### Set up the webhook[#](#set-up-the-webhook)

Set your bot's webhook URL to `https://<PROJECT_REFERENCE>.functions.supabase.co/telegram-bot` (Replacing `<...>` with respective values). In order to do that, run a GET request to the following URL (in your browser, for example):

```
1https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=https://<PROJECT_REFERENCE>.supabase.co/functions/v1/scribe-bot?secret=<FUNCTION_SECRET>
```

Note that the `FUNCTION_SECRET` is the secret you set in your `.env` file.

![Set webhook](/docs/img/guides/functions/elevenlabs/set-webhook.png)

### Set the function secrets[#](#set-the-function-secrets)

Now that you have all your secrets set locally, you can run the following command to set the secrets in your Supabase project:

```
1supabase secrets set --env-file supabase/functions/.env
```

## Test the bot[#](#test-the-bot)

Finally you can test the bot by sending it a voice message, audio or video file.

![Test the bot](/docs/img/guides/functions/elevenlabs/test-bot.png)

After you see the transcript as a reply, navigate back to your table editor in the Supabase dashboard and you should see a new row in your `transcription_logs` table.

![New row in table](/docs/img/guides/functions/elevenlabs/supa-new-row.png)
