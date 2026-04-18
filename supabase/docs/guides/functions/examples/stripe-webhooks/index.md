---
title: "Handling Stripe Webhooks"
source: "https://supabase.com/docs/guides/functions/examples/stripe-webhooks"
canonical_url: "https://supabase.com/docs/guides/functions/examples/stripe-webhooks"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:03.796Z"
content_hash: "fbe6a03d3371be92f06aff4704b321560ae5e1bddbeae13b5861d08cc1d112d6"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Handling Stripe Webhooks","Handling Stripe Webhooks"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Handling Stripe Webhooks","Handling Stripe Webhooks"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/astrojs/index.md", "title": "Use Supabase with Astro"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/expo-react-native/index.md", "title": "Use Supabase with Expo React Native"}
---

# 

Handling Stripe Webhooks

* * *

Handling signed Stripe Webhooks with Edge Functions. [View on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/stripe-webhooks/index.ts).

```
1// Follow this setup guide to integrate the Deno language server with your editor:2// https://deno.land/manual/getting_started/setup_your_environment3// This enables autocomplete, go to definition, etc.45// Import via bare specifier thanks to the import_map.json file.6import Stripe from 'https://esm.sh/stripe@14?target=denonext'78const stripe = new Stripe(Deno.env.get('STRIPE_API_KEY') as string, {9  // This is needed to use the Fetch API rather than relying on the Node http10  // package.11  apiVersion: '2024-11-20',12})13// This is needed in order to use the Web Crypto API in Deno.14const cryptoProvider = Stripe.createSubtleCryptoProvider()1516console.log('Hello from Stripe Webhook!')1718Deno.serve(async (request) => {19  const signature = request.headers.get('Stripe-Signature')2021  // First step is to verify the event. The .text() method must be used as the22  // verification relies on the raw request body rather than the parsed JSON.23  const body = await request.text()24  let receivedEvent25  try {26    receivedEvent = await stripe.webhooks.constructEventAsync(27      body,28      signature!,29      Deno.env.get('STRIPE_WEBHOOK_SIGNING_SECRET')!,30      undefined,31      cryptoProvider32    )33  } catch (err) {34    return new Response(err.message, { status: 400 })35  }36  console.log(`🔔 Event received: ${receivedEvent.id}`)37  return new Response(JSON.stringify({ ok: true }), { status: 200 })38})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/stripe-webhooks/index.ts)

