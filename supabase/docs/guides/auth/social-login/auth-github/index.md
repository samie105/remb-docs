---
title: "Login with GitHub"
source: "https://supabase.com/docs/guides/auth/social-login/auth-github"
canonical_url: "https://supabase.com/docs/guides/auth/social-login/auth-github"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:26.402Z"
content_hash: "aecadcde6d9ce9c2413196f9eb156a6ef15bc456ff9aa3a9a0ca71ee840f6d25"
menu_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","GitHub","GitHub"]
section_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","GitHub","GitHub"]
---
# 

Login with GitHub

* * *

To enable GitHub Auth for your project, you need to set up a GitHub OAuth application and add the application credentials to your Supabase Dashboard.

## Overview[#](#overview)

Setting up GitHub logins for your application consists of 3 parts:

*   Create and configure a GitHub OAuth App on [GitHub](https://github.com/settings/applications/new)
*   Add your GitHub OAuth keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)

## Find your callback URL[#](#find-your-callback-url)

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Sign In / Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitHub** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

#### Local development[#](#local-development)

When testing OAuth locally with the Supabase CLI, ensure your OAuth provider is configured with the local Supabase Auth callback URL:

[http://localhost:54321/auth/v1/callback](http://localhost:54321/auth/v1/callback)

If this callback URL is missing or misconfigured, OAuth sign-in may fail or not redirect correctly during local development.

See the [local development docs](/docs/guides/local-development) for more details.

For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/local-development).

## Register a new OAuth application on GitHub[#](#register-a-new-oauth-application-on-github)

*   Navigate to the [OAuth apps page](https://github.com/settings/developers)
*   Click `Register a new application`. If you've created an app before, click `New OAuth App` here.
*   In `Application name`, type the name of your app.
*   In `Homepage URL`, type the full URL to your app's website.
*   In `Authorization callback URL`, type the callback URL of your app.
*   Leave `Enable Device Flow` unchecked.
*   Click `Register Application`.

Copy your new OAuth credentials

*   Copy and save your `Client ID`.
*   Click `Generate a new client secret`.
*   Copy and save your `Client secret`.

## Enter your GitHub credentials into your Supabase project[#](#enter-your-github-credentials-into-your-supabase-project)

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitHub** from the accordion list to expand and turn **GitHub Enabled** to ON
*   Enter your **GitHub Client ID** and **GitHub Client Secret** saved in the previous step
*   Click `Save`

You can also configure the GitHub auth provider using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Configure GitHub auth provider6curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8  -H "Content-Type: application/json" \9  -d '{10    "external_github_enabled": true,11    "external_github_client_id": "your-github-client-id",12    "external_github_secret": "your-github-client-secret"13  }'
```

## Add login code to your client app[#](#add-login-code-to-your-client-app)

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `github` as the `provider`:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signInWithGithub() {7  const { data, error } = await supabase.auth.signInWithOAuth({8    provider: 'github',9  })10}
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
*   [GitHub Developer Settings](https://github.com/settings/developers)
