---
title: "Edge Functions"
source: "https://supabase.com/docs/guides/functions"
canonical_url: "https://supabase.com/docs/guides/functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:14.412Z"
content_hash: "1e5755e02faa6a1f3361b0bdfba2a60d0362a7f55148c597a547fbd5ee1e9705"
menu_path: ["Edge Functions","Edge Functions","Overview","Overview"]
section_path: ["Edge Functions","Edge Functions","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/deployment/shared-responsibility-model/index.md", "title": "Shared Responsibility Model"}
nav_next: {"path": "supabase/docs/guides/functions/ai-models/index.md", "title": "Running AI Models"}
---

# 

Edge Functions

## 

Globally distributed TypeScript functions.

* * *

Edge Functions are server-side TypeScript functions, distributed globally at the edge—close to your users. They can be used for listening to webhooks or integrating your Supabase project with third-parties [like Stripe](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/stripe-webhooks). Edge Functions are developed using [Deno](https://deno.com), which offers a few benefits to you as a developer:

*   It is open source.
*   It is portable. Supabase Edge Functions run locally, and on any other Deno-compatible platform (including self-hosted infrastructure).
*   It is TypeScript first and supports WASM.
*   Edge Functions are globally distributed for low-latency.

## How it works[#](#how-it-works)

*   **Request enters an edge gateway (relay)** — the gateway routes traffic, handles auth headers/JWT validation, and applies routing/traffic rules.
*   **Auth & policies are applied** — the gateway (or your function) can validate Supabase JWTs, apply rate-limits, and centralize security checks before executing code.
*   **[Edge runtime](https://github.com/supabase/edge-runtime) executes your function** — the function runs on a regionally-distributed Edge Runtime node closest to the user for minimal latency.
*   **Integrations & data access** — functions commonly call Supabase APIs (Auth, Postgres, Storage) or third-party APIs. For Postgres, prefer connection strategies suited for edge/serverless environments (see the `connect-to-postgres` guide).
*   **Observability and logs** — invocations emit logs and metrics you can explore in the dashboard or downstream monitoring (Sentry, etc.).
*   **Response returns via the gateway** — the gateway forwards the response back to the client and records request metadata.

## Quick technical notes[#](#quick-technical-notes)

*   **Runtime:** Supabase Edge Runtime (Deno compatible runtime with TypeScript first). Functions are simple `.ts` files that export a handler.
*   **Local dev parity:** Use Supabase CLI for a local runtime similar to production for faster iteration (`supabase functions serve` command).
*   **Global deployment:** Deploy your Edge Functions via Supabase Dashboard, CLI or MCP.
*   **Cold starts & concurrency:** cold starts are possible — design for short-lived, idempotent operations. Heavy long-running jobs should be moved to [background workers](/docs/guides/functions/background-tasks).
*   **Database connections:** treat Postgres like a remote, pooled service — use connection pools or serverless-friendly drivers.
*   **Secrets:** store credentials in Supabase [project secrets](/docs/reference/cli/supabase-secrets) and access them via environment variables.

## When to use Edge Functions[#](#when-to-use-edge-functions)

*   Authenticated or public HTTP endpoints that need low latency.
*   Webhook receivers (Stripe, GitHub, etc.).
*   On-demand image or Open Graph generation.
*   Small AI inference tasks or orchestrating calls to external LLM APIs (like OpenAI)
*   Sending transactional emails.
*   Building messaging bots for Slack, Discord, etc.

[Get started](/docs/guides/functions/quickstart)

## Examples[#](#examples)

Check out the [Edge Function Examples](https://github.com/supabase/supabase/tree/master/examples/edge-functions) in our GitHub repository.

[

![With supabase-js](/docs/img/icons/github-icon-light.svg)

With supabase-js

Use the Supabase client inside your Edge Function.

](/docs/guides/functions/auth)

[

![Type-Safe SQL with Kysely](/docs/img/icons/github-icon-light.svg)

Type-Safe SQL with Kysely

Combining Kysely with Deno Postgres gives you a convenient developer experience for interacting directly with your Postgres database.

](/docs/guides/functions/kysely-postgres)

[

![Monitoring with Sentry](/docs/img/icons/github-icon-light.svg)

Monitoring with Sentry

Monitor Edge Functions with the Sentry Deno SDK.

](/docs/guides/functions/examples/sentry-monitoring)

[

![With CORS headers](/docs/img/icons/github-icon-light.svg)

With CORS headers

Send CORS headers for invoking from the browser.

](/docs/guides/functions/cors)

[

![React Native with Stripe](/docs/img/icons/github-icon-light.svg)

React Native with Stripe

Full example for using Supabase and Stripe, with Expo.

](https://github.com/supabase-community/expo-stripe-payments-with-supabase-functions)

[

![Flutter with Stripe](/docs/img/icons/github-icon-light.svg)

Flutter with Stripe

Full example for using Supabase and Stripe, with Flutter.

](https://github.com/supabase-community/flutter-stripe-payments-with-supabase-functions)

[

![Building a RESTful Service API](/docs/img/icons/github-icon-light.svg)

Building a RESTful Service API

Learn how to use HTTP methods and paths to build a RESTful service for managing tasks.

](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/restful-tasks/index.ts)

[

![Working with Supabase Storage](/docs/img/icons/github-icon-light.svg)

Working with Supabase Storage

An example on reading a file from Supabase Storage.

](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/read-storage/index.ts)

[

![Open Graph Image Generation](/docs/img/icons/github-icon-light.svg)

Open Graph Image Generation

Generate Open Graph images with Deno and Supabase Edge Functions.

](/docs/guides/functions/examples/og-image)

[

![OG Image Generation & Storage CDN Caching](/docs/img/icons/github-icon-light.svg)

OG Image Generation & Storage CDN Caching

Cache generated images with Supabase Storage CDN.

](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/og-image-with-storage-cdn)

[

![Get User Location](/docs/img/icons/github-icon-light.svg)

Get User Location

Get user location data from user's IP address.

](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/location)

[

![Cloudflare Turnstile](/docs/img/icons/github-icon-light.svg)

Cloudflare Turnstile

Protecting Forms with Cloudflare Turnstile.

](/docs/guides/functions/examples/cloudflare-turnstile)

[

![Connect to Postgres](/docs/img/icons/github-icon-light.svg)

Connect to Postgres

Connecting to Postgres from Edge Functions.

](/docs/guides/functions/connect-to-postgres)

[

![GitHub Actions](/docs/img/icons/github-icon-light.svg)

GitHub Actions

Deploying Edge Functions with GitHub Actions.

](/docs/guides/functions/examples/github-actions)

[

![Oak Server Middleware](/docs/img/icons/github-icon-light.svg)

Oak Server Middleware

Request Routing with Oak server middleware.

](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/oak-server)

[

![Hugging Face](/docs/img/icons/github-icon-light.svg)

Hugging Face

Access 100,000+ Machine Learning models.

](/docs/guides/ai/examples/huggingface-image-captioning)

[

![Amazon Bedrock](/docs/img/icons/github-icon-light.svg)

Amazon Bedrock

Amazon Bedrock Image Generator

](/docs/guides/functions/examples/amazon-bedrock-image-generator)

[

![OpenAI](/docs/img/icons/github-icon-light.svg)

OpenAI

Using OpenAI in Edge Functions.

](/docs/guides/ai/examples/openai)

[

![Stripe Webhooks](/docs/img/icons/github-icon-light.svg)

Stripe Webhooks

Handling signed Stripe Webhooks with Edge Functions.

](/docs/guides/functions/examples/stripe-webhooks)

[

![Send emails](/docs/img/icons/github-icon-light.svg)

Send emails

Send emails in Edge Functions with Resend.

](/docs/guides/functions/examples/send-emails)

[

![Web Stream](/docs/img/icons/github-icon-light.svg)

Web Stream

Server-Sent Events in Edge Functions.

](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/streams)

[

![Puppeteer](/docs/img/icons/github-icon-light.svg)

Puppeteer

Generate screenshots with Puppeteer.

](/docs/guides/functions/examples/screenshots)

[

![Discord Bot](/docs/img/icons/github-icon-light.svg)

Discord Bot

Building a Slash Command Discord Bot with Edge Functions.

](/docs/guides/functions/examples/discord-bot)

[

![Telegram Bot](/docs/img/icons/github-icon-light.svg)

Telegram Bot

Building a Telegram Bot with Edge Functions.

](/docs/guides/functions/examples/telegram-bot)

[

![Upload File](/docs/img/icons/github-icon-light.svg)

Upload File

Process multipart/form-data.

](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/file-upload-storage)

[

![Upstash Redis](/docs/img/icons/github-icon-light.svg)

Upstash Redis

Build an Edge Functions Counter with Upstash Redis.

](/docs/guides/functions/examples/upstash-redis)

[

![Rate Limiting](/docs/img/icons/github-icon-light.svg)

Rate Limiting

Rate Limiting Edge Functions with Upstash Redis.

](/docs/guides/functions/examples/rate-limiting)

[

![Slack Bot Mention Edge Function](/docs/img/icons/github-icon-light.svg)

Slack Bot Mention Edge Function

Slack Bot handling Slack mentions in Edge Function

](/docs/guides/functions/examples/slack-bot-mention)
