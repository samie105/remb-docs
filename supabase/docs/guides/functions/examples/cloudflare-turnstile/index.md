---
title: "CAPTCHA support with Cloudflare Turnstile"
source: "https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile"
canonical_url: "https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:18.337Z"
content_hash: "f7cecfe2b41b2ad56591849c25c9847b2db16b72cd24f57e25cdfbfa6f052815"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","CAPTCHA support with Cloudflare Turnstile","CAPTCHA support with Cloudflare Turnstile"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","CAPTCHA support with Cloudflare Turnstile","CAPTCHA support with Cloudflare Turnstile"]
nav_prev: {"path": "../amazon-bedrock-image-generator/index.md", "title": "Generate Images with Amazon Bedrock"}
nav_next: {"path": "../discord-bot/index.md", "title": "Building a Discord Bot"}
---

# 

CAPTCHA support with Cloudflare Turnstile

* * *

[Cloudflare Turnstile](https://www.cloudflare.com/application-services/products/turnstile/) is a friendly, free CAPTCHA replacement, and it works seamlessly with Supabase Edge Functions to protect your forms. [View on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/cloudflare-turnstile).

## Setup[#](#setup)

*   Follow these steps to set up a new site: [https://developers.cloudflare.com/turnstile/get-started/](https://developers.cloudflare.com/turnstile/get-started/)
*   Add the Cloudflare Turnstile widget to your site: [https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)

## Code[#](#code)

Create a new function in your project:

```
1supabase functions new cloudflare-turnstile
```

And add the code to the `index.ts` file:

```
1import { corsHeaders } from '@supabase/supabase-js/cors' // v2.95.0+23console.log('Hello from Cloudflare Trunstile!')45function ips(req: Request) {6  return req.headers.get('x-forwarded-for')?.split(/\s*,\s*/)7}89Deno.serve(async (req) => {10  // This is needed if you're planning to invoke your function from a browser.11  if (req.method === 'OPTIONS') {12    return new Response('ok', { headers: corsHeaders })13  }1415  const { token } = await req.json()16  const clientIps = ips(req) || ['']17  const ip = clientIps[0]1819  // Validate the token by calling the20  // "/siteverify" API endpoint.21  let formData = new FormData()22  formData.append('secret', Deno.env.get('CLOUDFLARE_SECRET_KEY') ?? '')23  formData.append('response', token)24  formData.append('remoteip', ip)2526  const url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'27  const result = await fetch(url, {28    body: formData,29    method: 'POST',30  })3132  const outcome = await result.json()33  console.log(outcome)34  if (outcome.success) {35    return new Response('success', { headers: corsHeaders })36  }37  return new Response('failure', { headers: corsHeaders })38})
```

## Deploy the server-side validation Edge Functions[#](#deploy-the-server-side-validation-edge-functions)

*   [https://developers.cloudflare.com/turnstile/get-started/server-side-validation/](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

```
1supabase functions deploy cloudflare-turnstile2supabase secrets set CLOUDFLARE_SECRET_KEY=your_secret_key
```

## Invoke the function from your site[#](#invoke-the-function-from-your-site)

```
1const { data, error } = await supabase.functions.invoke('cloudflare-turnstile', {2  body: { token },3})
```
