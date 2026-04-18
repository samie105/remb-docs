---
title: "SSO and Social Login with WorkOS"
source: "https://supabase.com/docs/guides/auth/social-login/auth-workos"
canonical_url: "https://supabase.com/docs/guides/auth/social-login/auth-workos"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:57.000Z"
content_hash: "73d1f71341485030132020f3c48826d27757fb83abc1681382929ba4da7b4552"
menu_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","WorkOS","WorkOS"]
section_path: ["Auth","Auth","More","More","More","Social Login (OAuth)","Social Login (OAuth)","WorkOS","WorkOS"]
---
# 

SSO and Social Login with WorkOS

* * *

## Use Social Login with WorkOS[#](#use-social-login-with-workos)

### Step 1. Create a WorkOS organization[#](#step-1-create-a-workos-organization)

Log in to the WorkOS dashboard and visit the Organizations tab to create an organization. ![Create an Organization](/docs/img/guides/auth-workos/workos-create-organization.png)

Alternatively, you can [create an organization via the WorkOS API](https://workos.com/docs/reference/organization/create).

## Step 2. Obtain your `Client ID` and `WORKOS_API_KEY` values[#](#step-2-obtain-your-client-id-and-workosapikey-values)

![Get your Environment's Client ID and Secret](/docs/img/guides/auth-workos/workos-dashboard-get-client-id-and-key.png)

Visit the getting started page of the [WorkOS Dashboard](https://dashboard.workos.com/get-started). Copy the following values from the Quickstart panel:

*   `WORKOS_CLIENT_ID`
*   `WORKOS_API_KEY`

You must be signed in to see these values.

## Step 3. Add your WorkOS credentials to your Supabase project[#](#step-3-add-your-workos-credentials-to-your-supabase-project)

![Enter your WorkOS application details in your Supabase app's auth provider settings panel](/docs/img/guides/auth-workos/supabase-workos-configuration.png)

1.  Go to your Supabase Project Dashboard.
2.  In the left sidebar, click the Authentication icon (near the top).
3.  Click on Providers under the Configuration section.
4.  Click on WorkOS from the accordion list to expand.
5.  Toggle the `WorkOS Enabled` switch to ON.
6.  Enter `https://api.workos.com` in the WorkOS URL field.
7.  Enter your WorkOS Client ID and WorkOS Client Secret saved in the previous step.
8.  Copy the `Callback URL (for OAuth)` value from the form and save it somewhere handy.
9.  Click Save.

You can also configure the WorkOS auth provider using the Management API:

```
1# Get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"3export PROJECT_REF="your-project-ref"45# Configure WorkOS auth provider6curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \7  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \8  -H "Content-Type: application/json" \9  -d '{10    "external_workos_enabled": true,11    "external_workos_url": "https://api.workos.com",12    "external_workos_client_id": "your-workos-client-id",13    "external_workos_secret": "your-workos-client-secret"14  }'
```

## Step 4. Set your Supabase redirect URI in the WorkOS Dashboard[#](#step-4-set-your-supabase-redirect-uri-in-the-workos-dashboard)

Visit the WorkOS dashboard and click the redirects button in the left navigation panel.

On the redirects page, enter your Supabase project's `Callback URL (for OAuth)` which you saved in the previous step, as shown below:

![Set your Supbase project redirect URL in the WorkOS dashboard](/docs/img/guides/auth-workos/workos-set-supabase-redirect.png)

## Step 5. Add login code to your client app[#](#step-5-add-login-code-to-your-client-app)

When a user signs in, call `signInWithOAuth` with `workos` as the provider.

```
1import { createClient } from '@supabase/supabase-js';2const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...');3const redirect = (url: string) => {}45// ---cut---6async function signInWithWorkOS() {7  const { data, error } = await supabase.auth.signInWithOAuth({8    provider: 'workos',9    options: {10      redirectTo: 'http://example.com/auth/v1/callback', // Make sure your redirect URL is configured in the Supabase Dashboard Auth settings11      queryParams: {12        connection: '<connection_id>',13      },14    },15  })1617  if (data.url) {18    redirect(data.url) // use the redirect API for your server or framework19  }20}
```

You can find your `connection_id` in the WorkOS dashboard under the Organizations tab. Select your organization and then click View connection.

Within your specified callback URL, you'll exchange the code for a logged-in user profile:

```
1import { NextResponse } from 'next/server'2import { createClient } from '@/utils/supabase/server'34export async function GET(request: Request) {5  const { searchParams, origin } = new URL(request.url)6  const code = searchParams.get('code')7  // if "next" is in param, use it as the redirect URL8  let next = searchParams.get('next') ?? '/'9  if (!next.startsWith('/')) {10    // if "next" is not a relative URL, use the default11    next = '/'12  }1314  if (code) {15    const supabase = await createClient()16    const { error } = await supabase.auth.exchangeCodeForSession(code)17    if (!error) {18      const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer19      const isLocalEnv = process.env.NODE_ENV === 'development'20      if (isLocalEnv) {21        // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host22        return NextResponse.redirect(`${origin}${next}`)23      } else if (forwardedHost) {24        return NextResponse.redirect(`https://${forwardedHost}${next}`)25      } else {26        return NextResponse.redirect(`${origin}${next}`)27      }28    }29  }3031  // return the user to an error page with instructions32  return NextResponse.redirect(`${origin}/auth/auth-code-error`)33}
```

## Resources[#](#resources)

*   [WorkOS Documentation](https://workos.com/docs/sso/guide)
