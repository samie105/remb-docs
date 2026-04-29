---
title: "Sending Emails"
source: "https://supabase.com/docs/guides/functions/examples/send-emails"
canonical_url: "https://supabase.com/docs/guides/functions/examples/send-emails"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:44.433Z"
content_hash: "82270cc1fc99e5280d28db5166e63694f79e7fe8c6a3e7b9501091be299dca8e"
menu_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Sending Emails with Resend","Sending Emails with Resend"]
section_path: ["Edge Functions","Edge Functions","Third-Party Tools","Third-Party Tools","Sending Emails with Resend","Sending Emails with Resend"]
nav_prev: {"path": "../semantic-search/index.md", "title": "Semantic Search"}
nav_next: {"path": "../sentry-monitoring/index.md", "title": "Monitoring with Sentry"}
---

# 

Sending Emails

* * *

Sending emails from Edge Functions using the [Resend API](https://resend.com/).

### Prerequisites[#](#prerequisites)

To get the most out of this guide, you’ll need to:

*   [Create an API key](https://resend.com/api-keys)
*   [Verify your domain](https://resend.com/domains)

Make sure you have the latest version of the [Supabase CLI](/docs/guides/cli#installation) installed.

### 1\. Create Supabase function[#](#1-create-supabase-function)

Create a new function locally:

```
1supabase functions new resend
```

Store the `RESEND_API_KEY` in your `.env` file.

### 2\. Edit the handler function[#](#2-edit-the-handler-function)

Paste the following code into the `index.ts` file:

```
1const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY')23const handler = async (_request: Request): Promise<Response> => {4  const res = await fetch('https://api.resend.com/emails', {5    method: 'POST',6    headers: {7      'Content-Type': 'application/json',8      Authorization: `Bearer ${RESEND_API_KEY}`,9    },10    body: JSON.stringify({11      from: 'onboarding@resend.dev',12      to: 'delivered@resend.dev',13      subject: 'hello world',14      html: '<strong>it works!</strong>',15    }),16  })1718  const data = await res.json()1920  return new Response(JSON.stringify(data), {21    status: 200,22    headers: {23      'Content-Type': 'application/json',24    },25  })26}2728Deno.serve(handler)
```

### 3\. Deploy and send email[#](#3-deploy-and-send-email)

Run function locally:

```
1supabase start2supabase functions serve --no-verify-jwt --env-file .env
```

Test it: [http://localhost:54321/functions/v1/resend](http://localhost:54321/functions/v1/resend)

Deploy function to Supabase:

```
1supabase functions deploy resend --no-verify-jwt
```

When you deploy to Supabase, make sure that your `RESEND_API_KEY` is set in [Edge Function Secrets Management](/dashboard/project/_/functions/secrets)

Open the endpoint URL to send an email:

### 4\. Try it yourself[#](#4-try-it-yourself)

Find the complete example on [GitHub](https://github.com/resendlabs/resend-supabase-edge-functions-example).
