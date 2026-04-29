---
title: "Building a Discord Bot"
source: "https://supabase.com/docs/guides/functions/examples/discord-bot"
canonical_url: "https://supabase.com/docs/guides/functions/examples/discord-bot"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:27.324Z"
content_hash: "561ac0e4c411724fb09b393e6b592b7764e71913821e060a10855c9fe47a59d8"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Building a Discord Bot","Building a Discord Bot"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Building a Discord Bot","Building a Discord Bot"]
nav_prev: {"path": "supabase/docs/guides/functions/examples/cloudflare-turnstile/index.md", "title": "CAPTCHA support with Cloudflare Turnstile"}
nav_next: {"path": "supabase/docs/guides/functions/examples/elevenlabs-generate-speech-stream/index.md", "title": "Streaming Speech with ElevenLabs"}
---

# 

Building a Discord Bot

* * *

## Create an application on Discord Developer portal[#](#create-an-application-on-discord-developer-portal)

1.  Go to [https://discord.com/developers/applications](https://discord.com/developers/applications) (login using your discord account if required).
2.  Click on **New Application** button available at left side of your profile picture.
3.  Name your application and click on **Create**.
4.  Go to **Bot** section, click on **Add Bot**, and finally on **Yes, do it!** to confirm.

A new application is created which will hold our Slash Command. Don't close the tab as we need information from this application page throughout our development.

Before we can write some code, we need to curl a discord endpoint to register a Slash Command in our app.

Fill `DISCORD_BOT_TOKEN` with the token available in the **Bot** section and `CLIENT_ID` with the ID available on the **General Information** section of the page and run the command on your terminal.

```
1BOT_TOKEN='replace_me_with_bot_token'2CLIENT_ID='replace_me_with_client_id'3curl -X POST \4-H 'Content-Type: application/json' \5-H "Authorization: Bot $BOT_TOKEN" \6-d '{"name":"hello","description":"Greet a person","options":[{"name":"name","description":"The name of the person","type":3,"required":true}]}' \7"https://discord.com/api/v8/applications/$CLIENT_ID/commands"
```

This will register a Slash Command named `hello` that accepts a parameter named `name` of type string.

## Code[#](#code)

```
1// Sift is a small routing library that abstracts away details like starting a2// listener on a port, and provides a simple function (serve) that has an API3// to invoke a function for a specific path.4import { json, serve, validateRequest } from 'https://deno.land/x/sift@0.6.0/mod.ts'5// TweetNaCl is a cryptography library that we use to verify requests6// from Discord.7import nacl from 'https://cdn.skypack.dev/tweetnacl@v1.0.3?dts'89enum DiscordCommandType {10  Ping = 1,11  ApplicationCommand = 2,12}1314// For all requests to "/" endpoint, we want to invoke home() handler.15serve({16  '/discord-bot': home,17})1819// The main logic of the Discord Slash Command is defined in this function.20async function home(request: Request) {21  // validateRequest() ensures that a request is of POST method and22  // has the following headers.23  const { error } = await validateRequest(request, {24    POST: {25      headers: ['X-Signature-Ed25519', 'X-Signature-Timestamp'],26    },27  })28  if (error) {29    return json({ error: error.message }, { status: error.status })30  }3132  // verifySignature() verifies if the request is coming from Discord.33  // When the request's signature is not valid, we return a 401 and this is34  // important as Discord sends invalid requests to test our verification.35  const { valid, body } = await verifySignature(request)36  if (!valid) {37    return json(38      { error: 'Invalid request' },39      {40        status: 401,41      }42    )43  }4445  const { type = 0, data = { options: [] } } = JSON.parse(body)46  // Discord performs Ping interactions to test our application.47  // Type 1 in a request implies a Ping interaction.48  if (type === DiscordCommandType.Ping) {49    return json({50      type: 1, // Type 1 in a response is a Pong interaction response type.51    })52  }5354  // Type 2 in a request is an ApplicationCommand interaction.55  // It implies that a user has issued a command.56  if (type === DiscordCommandType.ApplicationCommand) {57    const { value } = data.options.find(58      (option: { name: string; value: string }) => option.name === 'name'59    )60    return json({61      // Type 4 responds with the below message retaining the user's62      // input at the top.63      type: 4,64      data: {65        content: `Hello, ${value}!`,66      },67    })68  }6970  // We will return a bad request error as a valid Discord request71  // shouldn't reach here.72  return json({ error: 'bad request' }, { status: 400 })73}7475/** Verify whether the request is coming from Discord. */76async function verifySignature(request: Request): Promise<{ valid: boolean; body: string }> {77  const PUBLIC_KEY = Deno.env.get('DISCORD_PUBLIC_KEY')!78  // Discord sends these headers with every request.79  const signature = request.headers.get('X-Signature-Ed25519')!80  const timestamp = request.headers.get('X-Signature-Timestamp')!81  const body = await request.text()82  const valid = nacl.sign.detached.verify(83    new TextEncoder().encode(timestamp + body),84    hexToUint8Array(signature),85    hexToUint8Array(PUBLIC_KEY)86  )8788  return { valid, body }89}9091/** Converts a hexadecimal string to Uint8Array. */92function hexToUint8Array(hex: string) {93  return new Uint8Array(hex.match(/.{1,2}/g)!.map((val) => parseInt(val, 16)))94}
```

## Deploy the slash command handler[#](#deploy-the-slash-command-handler)

```
1supabase functions deploy discord-bot --no-verify-jwt2supabase secrets set DISCORD_PUBLIC_KEY=your_public_key
```

Navigate to your Function details in the Supabase Dashboard to get your Endpoint URL.

### Configure Discord application to use our URL as interactions endpoint URL[#](#configure-discord-application-to-use-our-url-as-interactions-endpoint-url)

1.  Go back to your application (Greeter) page on Discord Developer Portal
2.  Fill **INTERACTIONS ENDPOINT URL** field with the URL and click on **Save Changes**.

The application is now ready. Let's proceed to the next section to install it.

## Install the slash command on your Discord server[#](#install-the-slash-command-on-your-discord-server)

So to use the `hello` Slash Command, we need to install our Greeter application on our Discord server. Here are the steps:

1.  Go to **OAuth2** section of the Discord application page on Discord Developer Portal
2.  Select `applications.commands` scope and click on the **Copy** button below.
3.  Now paste and visit the URL on your browser. Select your server and click on **Authorize**.

Open Discord, type `/Promise` and press **Enter**.

## Run locally[#](#run-locally)

```
1supabase functions serve discord-bot --no-verify-jwt --env-file ./supabase/.env.local2ngrok http 54321
```
