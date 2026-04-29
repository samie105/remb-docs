---
title: "Login with Slack"
source: "https://supabase.com/docs/guides/auth/social-login/auth-slack"
canonical_url: "https://supabase.com/docs/guides/auth/social-login/auth-slack"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:48.825Z"
content_hash: "192e5cb74652d1daba83fbbb917ceca8dbfa40ef8088cb9c639db2521bfc51bb"
menu_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Slack","Slack"]
section_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Slack","Slack"]
nav_prev: {"path": "../auth-notion/index.md", "title": "Login with Notion"}
nav_next: {"path": "../auth-spotify/index.md", "title": "Login with Spotify"}
---

# 

Login with Slack

* * *

To enable Slack Auth for your project, you need to set up a Slack OAuth application and add the application credentials to your Supabase Dashboard.

## Overview[#](#overview)

We will be replacing the existing Slack provider with a new Slack (OIDC) provider. Developers with Slack OAuth Applications created prior to 24th June 2024 should create a new application and migrate their credentials from the Slack provider to the Slack (OIDC) provider. Existing OAuth Applications built with the old Slack provider will continue to work up till 10th October. You can refer to the [**list of supported scopes**](https://api.slack.com/scopes?filter=user) for the new Slack (OIDC) User.

Setting up Slack logins for your application consists of 3 parts:

*   Create and configure a Slack Project and App on the [Slack Developer Dashboard](https://api.slack.com/apps).
*   Add your Slack `API Key` and `API Secret Key` to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).

## Access your Slack Developer account[#](#access-your-slack-developer-account)

*   Go to [api.slack.com](https://api.slack.com/apps).
*   Click on `Your Apps` at the top right to log in.

![Slack Developer Portal.](/docs/img/guides/auth-slack/slack-portal.png)

## Find your callback URL[#](#find-your-callback-url)

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Sign In / Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Slack** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

#### Local development[#](#local-development)

When testing OAuth locally with the Supabase CLI, ensure your OAuth provider is configured with the local Supabase Auth callback URL:

[http://localhost:54321/auth/v1/callback](http://localhost:54321/auth/v1/callback)

If this callback URL is missing or misconfigured, OAuth sign-in may fail or not redirect correctly during local development.

See the [local development docs](/docs/guides/local-development) for more details.

For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/local-development).

## Create a Slack OAuth app[#](#create-a-slack-oauth-app)

*   Go to [api.slack.com](https://api.slack.com/apps).
*   Click on `Create New App`

Under `Create an app...`:

*   Click `From scratch`
*   Type the name of your app
*   Select your `Slack Workspace`
*   Click `Create App`

Under `App Credentials`:

*   Copy and save your newly-generated `Client ID`
*   Copy and save your newly-generated `Client Secret`

Under the sidebar, select `OAuth & Permissions` and look for `Redirect URLs`:

*   Click `Add New Redirect URL`
*   Paste your `Callback URL` then click `Add`
*   Click `Save URLs`

Under `Scopes`:

*   Add the following scopes under the `User Token Scopes`: `profile`, `email`, `openid`. These scopes are the default scopes that Supabase Auth uses to request for user information. Do not add other scopes as [Sign In With Slack only supports `profile`, `email`, `openid`](https://api.slack.com/authentication/sign-in-with-slack#request).

## Enter your Slack credentials into your Supabase project[#](#enter-your-slack-credentials-into-your-supabase-project)

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Slack** from the accordion list to expand and turn **Slack Enabled** to ON
*   Enter your **Slack Client ID** and **Slack Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Slack (OIDC) auth provider using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Configure Slack (OIDC) auth provider6curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8  -H "Content-Type: application/json" \9  -d '{10    "external_slack_oidc_enabled": true,11    "external_slack_oidc_client_id": "your-slack-client-id",12    "external_slack_oidc_secret": "your-slack-client-secret"13  }'
```

## Add login code to your client app[#](#add-login-code-to-your-client-app)

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `slack_oidc` as the `provider`:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signInWithSlack() {7  const { data, error } = await supabase.auth.signInWithOAuth({8    provider: 'slack_oidc',9  })10}
```

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

```
1import { createClient, type Provider } from '@supabase/supabase-js';2const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')3const provider = 'provider' as Provider45// ---cut---6await supabase.auth.signInWithOAuth({7  provider,8  options: {9    redirectTo: `http://example.com/auth/callback`,10  },11})
```

At the callback endpoint, handle the code exchange to save the user session.

Create a new file at `app/auth/callback/route.ts` and populate with the following:

###### app/auth/callback/route.ts

```
1import { NextResponse } from 'next/server'23// The client you created from the Server-Side Auth instructions4import { createClient } from '@/utils/supabase/server'56export async function GET(request: Request) {7  const { searchParams, origin } = new URL(request.url)8  const code = searchParams.get('code')9  // if "next" is in param, use it as the redirect URL10  let next = searchParams.get('next') ?? '/'11  if (!next.startsWith('/')) {12    // if "next" is not a relative URL, use the default13    next = '/'14  }1516  if (code) {17    const supabase = await createClient()18    const { error } = await supabase.auth.exchangeCodeForSession(code)19    if (!error) {20      const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer21      const isLocalEnv = process.env.NODE_ENV === 'development'22      if (isLocalEnv) {23        // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host24        return NextResponse.redirect(`${origin}${next}`)25      } else if (forwardedHost) {26        return NextResponse.redirect(`https://${forwardedHost}${next}`)27      } else {28        return NextResponse.redirect(`${origin}${next}`)29      }30    }31  }3233  // return the user to an error page with instructions34  return NextResponse.redirect(`${origin}/auth/auth-code-error`)35}
```

When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signOut() {7  const { error } = await supabase.auth.signOut()8}
```

## Resources[#](#resources)

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Slack Developer Dashboard](https://api.slack.com/apps)
