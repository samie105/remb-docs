---
title: "Login with Notion"
source: "https://supabase.com/docs/guides/auth/social-login/auth-notion"
canonical_url: "https://supabase.com/docs/guides/auth/social-login/auth-notion"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:43.060Z"
content_hash: "53562c5ae34b86a2b1af0d446cafe6497f873aa00d2714b22c159417025a4dae"
menu_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Notion","Notion"]
section_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","Notion","Notion"]
nav_prev: {"path": "supabase/docs/guides/auth/social-login/auth-linkedin/index.md", "title": "Login with LinkedIn"}
nav_next: {"path": "supabase/docs/guides/auth/social-login/auth-slack/index.md", "title": "Login with Slack"}
---

# 

Login with Notion

* * *

To enable Notion Auth for your project, you need to set up a Notion Application and add the Application OAuth credentials to your Supabase Dashboard.

## Overview[#](#overview)

Setting up Notion logins for your application consists of 3 parts:

*   Create and configure a Notion Application [Notion Developer Portal](https://www.notion.so/my-integrations)
*   Retrieve your OAuth client ID and OAuth client secret and add them to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)

## Create your notion integration[#](#create-your-notion-integration)

*   Go to [developers.notion.com](https://developers.notion.com/).
    
*   Click "View my integrations" and login. ![notion.so](/docs/img/guides/auth-notion/notion.png)
    
*   Once logged in, go to [notion.so/my-integrations](https://notion.so/my-integrations) and create a new integration.
    
*   When creating your integration, ensure that you select "Public integration" under "Integration type" and "Read user information including email addresses" under "Capabilities".
    
*   You will need to add a redirect URI, see [Add the redirect URI](#add-the-redirect-uri)
    
*   Once you've filled in the necessary fields, click "Submit" to finish creating the integration.
    

![notion.so](/docs/img/guides/auth-notion/notion-developer.png)

## Add the redirect URI[#](#add-the-redirect-uri)

*   After selecting "Public integration", you should see an option to add "Redirect URIs".

![notion.so](/docs/img/guides/auth-notion/notion-redirect-uri.png)

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Sign In / Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Notion** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

#### Local development[#](#local-development)

When testing OAuth locally with the Supabase CLI, ensure your OAuth provider is configured with the local Supabase Auth callback URL:

[http://localhost:54321/auth/v1/callback](http://localhost:54321/auth/v1/callback)

If this callback URL is missing or misconfigured, OAuth sign-in may fail or not redirect correctly during local development.

See the [local development docs](../../../local-development/index.md) for more details.

For testing OAuth locally with the Supabase CLI see the [local development docs](../../../local-development/index.md).

## Add your Notion credentials into your Supabase project[#](#add-your-notion-credentials-into-your-supabase-project)

*   Once you've created your notion integration, you should be able to retrieve the "OAuth client ID" and "OAuth client secret" from the "OAuth Domain and URIs" tab.

![notion.so](/docs/img/guides/auth-notion/notion-creds.png)

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Notion** from the accordion list to expand and turn **Notion Enabled** to ON
*   Enter your **Notion Client ID** and **Notion Client Secret** saved in the previous step
*   Click `Save`

## Add login code to your client app[#](#add-login-code-to-your-client-app)

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](../../server-side/creating-a-client/index.md) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `notion` as the `provider`:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signInWithNotion() {7  const { data, error } = await supabase.auth.signInWithOAuth({8    provider: 'notion',9  })10}
```

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](../../redirect-urls/index.md).

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
*   [Notion Account](https://notion.so)
*   [Notion Developer Portal](https://www.notion.so/my-integrations)
