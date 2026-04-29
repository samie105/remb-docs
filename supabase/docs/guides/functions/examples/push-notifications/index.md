---
title: "Sending Push Notifications"
source: "https://supabase.com/docs/guides/functions/examples/push-notifications"
canonical_url: "https://supabase.com/docs/guides/functions/examples/push-notifications"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:38.060Z"
content_hash: "b43e049d35e1d284aaaf12511dded60113435252823065a31aed8155f0d4055e"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Sending Push Notifications","Sending Push Notifications"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Sending Push Notifications","Sending Push Notifications"]
nav_prev: {"path": "../og-image/index.md", "title": "Generating OG Images"}
nav_next: {"path": "../rate-limiting/index.md", "title": "Rate Limiting Edge Functions"}
---

# 

Sending Push Notifications

* * *

Push notifications are an important part of any mobile app. They allow you to send notifications to your users even when they are not using your app. This guide will show you how to send push notifications to different mobile app frameworks from your Supabase edge functions.

[Expo](https://docs.expo.dev/push-notifications/overview/) makes implementing push notifications easy. All the hassle with device information and communicating with Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNs) is done behind the scenes. This allows you to treat Android and iOS notifications in the same way and save time both on the frontend and backend.

Find the example code on [GitHub](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/).

## Supabase setup[#](#supabase-setup)

*   [Create a new Supabase project](https://database.new).
*   Link your project: `supabase link --project-ref your-supabase-project-ref`
*   Start Supabase locally: `supabase start`
*   Push up the schema: `supabase db push` (schema is defined in [supabase/migrations](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/supabase/migrations/))

## Expo setup[#](#expo-setup)

To utilize Expo's push notification service, you must configure your app by installing a set of libraries, implementing functions to handle notifications, and setting up credentials for Android and iOS. Follow the official [Expo Push Notifications Setup Guide](https://docs.expo.dev/push-notifications/push-notifications-setup/) to get the credentials for Android and iOS. This project uses [Expo's EAS build](https://docs.expo.dev/build/introduction/) service to simplify this part.

1.  Install the dependencies: `npm i`
2.  Create a [new Expo project](https://expo.dev/accounts/_/projects)
3.  Link this app to your project: `npm install --global eas-cli && eas init --id your-expo-project-id`
4.  [Create a build for your physical device](https://docs.expo.dev/develop/development-builds/create-a-build/#create-a-build-for-the-device)
5.  Start the development server for your project: `npx expo start --dev-client`
6.  Scan the QR code shown in the terminal with your physical device.
7.  Sign up/in to create a user in Supabase Auth.

## Enhanced security for push notifications[#](#enhanced-security-for-push-notifications)

1.  Navigate to your [Expo Access Token Settings](https://expo.dev/accounts/_/settings/access-tokens).
2.  Create a new token for usage in Supabase Edge Functions.
3.  Toggle on "Enhanced Security for Push Notifications".
4.  Create the local `.env` file: `cp .env.local.example .env.local`
5.  In the newly created `.env.local` file, set your `EXPO_ACCESS_TOKEN` value.

## Deploy the Supabase Edge Function[#](#deploy-the-supabase-edge-function)

The database webhook handler to send push notifications is located in [supabase/functions/push/index.ts](https://github.com/supabase/supabase/blob/master/examples/user-management/expo-push-notifications/supabase/functions/push/index.ts). Deploy the function to your linked project and set the `EXPO_ACCESS_TOKEN` secret.

1.  `supabase functions deploy push`
2.  `supabase secrets set --env-file .env.local`

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23console.log('Hello from Functions!')45interface Notification {6  id: string7  user_id: string8  body: string9}1011interface WebhookPayload {12  type: 'INSERT' | 'UPDATE' | 'DELETE'13  table: string14  record: Notification15  schema: 'public'16  old_record: null | Notification17}1819const supabase = createClient(20  Deno.env.get('SUPABASE_URL')!,21  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!22)2324Deno.serve(async (req) => {25  const payload: WebhookPayload = await req.json()26  const { data } = await supabase27    .from('profiles')28    .select('expo_push_token')29    .eq('id', payload.record.user_id)30    .single()3132  const res = await fetch('https://exp.host/--/api/v2/push/send', {33    method: 'POST',34    headers: {35      'Content-Type': 'application/json',36      Authorization: `Bearer ${Deno.env.get('EXPO_ACCESS_TOKEN')}`,37    },38    body: JSON.stringify({39      to: data?.expo_push_token,40      sound: 'default',41      body: payload.record.body,42    }),43  }).then((res) => res.json())4445  return new Response(JSON.stringify(res), {46    headers: { 'Content-Type': 'application/json' },47  })48})
```

## Create the database webhook[#](#create-the-database-webhook)

Navigate to the [Database Webhooks settings](/dashboard/project/_/integrations/webhooks/overview) in your Supabase Dashboard.

1.  Enable and create a new hook.
2.  Conditions to fire webhook: Select the `notifications` table and tick the `Insert` event.
3.  Webhook configuration: Supabase Edge Functions.
4.  Edge Function: Select the `push` edge function and leave the method as `POST` and timeout as `1000`.
5.  HTTP Headers: Click "Add new header" > "Add auth header with service key" and leave Content-type: `application/json`.
6.  Click "Create webhook".

## Send push notification[#](#send-push-notification)

1.  Navigate to the [table editor](/dashboard/project/_/editor) in your Supabase Dashboard.
2.  In your `notifications` table, insert a new row.
3.  Watch the magic happen 🪄
