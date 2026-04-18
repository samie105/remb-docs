---
title: "Getting Started with OAuth 2.1 Server"
source: "https://supabase.com/docs/guides/auth/oauth-server/getting-started"
canonical_url: "https://supabase.com/docs/guides/auth/oauth-server/getting-started"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:20.597Z"
content_hash: "25957651ee425b536982b479495de557762117d6dbd8cb80107503afaf19ca6c"
menu_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Getting Started","Getting Started"]
section_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Getting Started","Getting Started"]
nav_prev: {"path": "supabase/docs/guides/auth/enterprise-sso/auth-sso-saml/index.md", "title": "Single Sign-On with SAML 2.0 for Projects"}
nav_next: {"path": "supabase/docs/guides/auth/oauth-server/mcp-authentication/index.md", "title": "Model Context Protocol (MCP) Authentication"}
---

# 

Getting Started with OAuth 2.1 Server

* * *

This guide will walk you through setting up your Supabase project as an OAuth 2.1 identity provider, from enabling the feature to registering your first client application.

## Prerequisites[#](#prerequisites)

Before you begin, make sure you have:

*   A Supabase project (create one at [supabase.com](https://supabase.com))
*   Admin access to your project
*   (Optional) [Supabase CLI](/docs/guides/cli) v2.54.11 or higher for local development

## Overview[#](#overview)

Setting up OAuth 2.1 in your Supabase project involves these steps:

1.  Enable OAuth 2.1 server capabilities in your project
2.  Configure your authorization path
3.  Build your authorization UI (frontend)
4.  Register OAuth client applications

Testing OAuth flows is often easier on a Supabase project since it's already accessible on the web, no tunnel or additional configuration needed.

## Enable OAuth 2.1 server[#](#enable-oauth-21-server)

OAuth 2.1 server is currently in beta and free to use during the beta period on all Supabase plans.

1.  Go to your project dashboard
2.  Navigate to **Authentication** > **OAuth Server** in the sidebar
3.  Enable OAuth 2.1 server capabilities

Once enabled, your project will expose the necessary OAuth endpoints:

Endpoint

URL

**Authorization endpoint**

`https://<project-ref>.supabase.co/auth/v1/oauth/authorize`

**Token endpoint**

`https://<project-ref>.supabase.co/auth/v1/oauth/token`

**JWKS endpoint**

`https://<project-ref>.supabase.co/auth/v1/.well-known/jwks.json`

**Discovery endpoint**

`https://<project-ref>.supabase.co/.well-known/oauth-authorization-server/auth/v1`

**OIDC discovery**

`https://<project-ref>.supabase.co/auth/v1/.well-known/openid-configuration`

**Use asymmetric JWT signing keys for better security**

By default, Supabase uses HS256 (symmetric) for signing JWTs. For OAuth use cases, we recommend migrating to asymmetric algorithms like RS256 or ES256. Asymmetric keys are more scalable and secure because:

*   OAuth clients can validate JWTs using the public key from your JWKS endpoint
*   No need to share your JWT secret with third-party applications
*   More resilient architecture for distributed systems

Learn more about [configuring JWT signing keys](/docs/guides/auth/signing-keys).

**Note:** If you plan to use OpenID Connect ID tokens (by requesting the `openid` scope), asymmetric signing algorithms are **required**. ID token generation will fail with HS256.

## Configure your authorization path[#](#configure-your-authorization-path)

Before registering clients, you need to configure where your authorization UI will live.

1.  In your project dashboard, navigate to **Authentication** > **OAuth Server**
2.  Set the **Authorization Path** (e.g., `/oauth/consent`)

The authorization path is combined with your Site URL (configured in **Authentication** > **URL Configuration**) to create the full authorization endpoint URL.

Your authorization UI will be at the combined Site URL + Authorization Path. For example:

*   Site URL: `https://example.com` (from **Authentication** > **URL Configuration**)
*   Authorization Path: `/oauth/consent` (from **OAuth Server** settings)
*   Your authorization UI: `https://example.com/oauth/consent`

When OAuth clients initiate the authorization flow, Supabase Auth will redirect users to this URL with an `authorization_id` query parameter. You'll use [Supabase JavaScript library OAuth methods](https://github.com/supabase/supabase-js/blob/master/packages/core/auth-js/src/GoTrueClient.ts#L2159-L2163) to handle the authorization:

*   `supabase.auth.oauth.getAuthorizationDetails(authorization_id)` - Retrieve client and authorization details
*   `supabase.auth.oauth.approveAuthorization(authorization_id)` - Approve the authorization request
*   `supabase.auth.oauth.denyAuthorization(authorization_id)` - Deny the authorization request

## Build your authorization UI[#](#build-your-authorization-ui)

This is where you build the **frontend** for your authorization flow. When third-party apps initiate OAuth, users will be redirected to your authorization path (configured in the previous step) with an `authorization_id` query parameter.

Your authorization UI should:

1.  **Extract authorization\_id** - Get the `authorization_id` from the URL query parameters
2.  **Authenticate the user** - If not already logged in, redirect to your login page (preserving the authorization\_id)
3.  **Retrieve authorization details** - Use `supabase.auth.oauth.getAuthorizationDetails(authorization_id)` to get client information including requested scopes
4.  **Display consent screen** - Show the user what app is requesting access and what scopes/permissions are being requested
5.  **Handle user decision** - Call either `approveAuthorization(authorization_id)` or `denyAuthorization(authorization_id)` based on user choice

The authorization details include a `scope` field (singular) containing a space-separated string of scopes requested by the client (e.g., `"openid email profile"`). You should display these scopes to the user so they understand what information will be shared.

This is a **frontend implementation**. You're building the UI that displays the consent screen and handles user interactions. The actual OAuth token generation is handled by Supabase Auth after you call the approve/deny methods.

### Example authorization UI[#](#example-authorization-ui)

Here's how to build a minimal authorization page at your configured path (e.g., `/oauth/consent`):

```
1// app/oauth/consent/page.tsx2import { createServerClient } from '@supabase/ssr'3import { cookies } from 'next/headers'4import { redirect } from 'next/navigation'56export default async function ConsentPage({7  searchParams,8}: {9  searchParams: { authorization_id?: string }10}) {11  const authorizationId = (await searchParams).authorization_id1213  if (!authorizationId) {14    return <div>Error: Missing authorization_id</div>15  }1617  const supabase = createServerClient(18    process.env.NEXT_PUBLIC_SUPABASE_URL!,19    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,20    {21      cookies: {22        getAll: async () => (await cookies()).getAll(),23        setAll: async (cookiesToSet, _headers) => {24          const cookieStore = await cookies()25          cookiesToSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options))26        },27      },28    }29  )3031  // Check if user is authenticated32  const {33    data: { user },34  } = await supabase.auth.getUser()3536  if (!user) {37    // Redirect to login, preserving authorization_id38    redirect(`/login?redirect=/oauth/consent?authorization_id=${authorizationId}`)39  }4041  // Get authorization details using the authorization_id42  const { data: authDetails, error } =43    await supabase.auth.oauth.getAuthorizationDetails(authorizationId)4445  if (error || !authDetails) {46    return <div>Error: {error?.message || 'Invalid authorization request'}</div>47  }4849  return (50    <div>51      <h1>Authorize {authDetails.client.name}</h1>52      <p>This application wants to access your account.</p>5354      <div>55        <p>56          <strong>Client:</strong> {authDetails.client.name}57        </p>58        <p>59          <strong>Redirect URI:</strong> {authDetails.redirect_uri}60        </p>61        {authDetails.scope && authDetails.scope.trim() && (62          <div>63            <strong>Requested permissions:</strong>64            <ul>65              {authDetails.scope.split(' ').map((scopeItem) => (66                <li key={scopeItem}>{scopeItem}</li>67              ))}68            </ul>69          </div>70        )}71      </div>7273      <form action="/api/oauth/decision" method="POST">74        <input type="hidden" name="authorization_id" value={authorizationId} />75        <button type="submit" name="decision" value="approve">76          Approve77        </button>78        <button type="submit" name="decision" value="deny">79          Deny80        </button>81      </form>82    </div>83  )84}
```

```
1// app/api/oauth/decision/route.ts2import { createServerClient } from '@supabase/ssr'3import { cookies } from 'next/headers'4import { NextResponse } from 'next/server'56export async function POST(request: Request) {7  const formData = await request.formData()8  const decision = formData.get('decision')9  const authorizationId = formData.get('authorization_id') as string1011  if (!authorizationId) {12    return NextResponse.json({ error: 'Missing authorization_id' }, { status: 400 })13  }1415  const supabase = createServerClient(16    process.env.NEXT_PUBLIC_SUPABASE_URL!,17    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,18    {19      cookies: {20        getAll: async () => (await cookies()).getAll(),21        setAll: async (cookiesToSet, _headers) => {22          const cookieStore = await cookies()23          cookiesToSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options))24        },25      },26    }27  )2829  if (decision === 'approve') {30    const { data, error } = await supabase.auth.oauth.approveAuthorization(authorizationId)3132    if (error) {33      return NextResponse.json({ error: error.message }, { status: 400 })34    }3536    // Redirect back to the client with authorization code37    return NextResponse.redirect(data.redirect_to)38  } else {39    const { data, error } = await supabase.auth.oauth.denyAuthorization(authorizationId)4041    if (error) {42      return NextResponse.json({ error: error.message }, { status: 400 })43    }4445    // Redirect back to the client with error46    return NextResponse.redirect(data.redirect_to)47  }48}
```

### How it works[#](#how-it-works)

1.  **User navigates to your authorization path** - When a third-party app initiates OAuth, Supabase Auth redirects the user to your configured authorization path (e.g., `https://example.com/oauth/consent?authorization_id=<id>`)
2.  **Extract authorization\_id** - Your page extracts the `authorization_id` from the URL query parameters
3.  **Check authentication** - Your page checks if the user is logged in, redirecting to login if not (preserving the authorization\_id)
4.  **Retrieve details** - Call `supabase.auth.oauth.getAuthorizationDetails(authorization_id)` to get information about the requesting client
5.  **Show consent screen** - Display a UI asking the user to approve or deny access
6.  **Handle decision** - When the user clicks approve/deny:
    *   Call `supabase.auth.oauth.approveAuthorization(authorization_id)` or `denyAuthorization(authorization_id)`
    *   These methods handle all OAuth logic internally (generating authorization codes, etc.)
    *   They return a `redirect_to` URL
7.  **Redirect back** - Redirect the user to the `redirect_to` URL, which sends them back to the third-party app with either an authorization code (approved) or error (denied)

## Register an OAuth client[#](#register-an-oauth-client)

Before third-party applications can use your project as an identity provider, you need to register them as OAuth clients.

1.  Go to **Authentication** > **OAuth Apps** (under the **Manage** section)
2.  Click **Add a new client**
3.  Enter the client details:
    *   **Client name**: A friendly name for your application
    *   **Redirect URIs**: One or more URLs where users will be redirected after authorization
    *   **Client type**: Choose between:
        *   **Public** - For mobile and single-page apps (no client secret)
        *   **Confidential** - For server-side apps (includes client secret)
4.  Click **Create**

You'll receive:

*   **Client ID**: A unique identifier for the client
*   **Client Secret** (for confidential clients): A secret key for authenticating the client

Store the client secret securely. It will only be shown once. If you lose it, you can regenerate a new one from the **OAuth Apps** page.

#### Token endpoint authentication method[#](#token-endpoint-authentication-method)

When a client exchanges an authorization code or refreshes a token, it must authenticate with the token endpoint. The `token_endpoint_auth_method` controls how this authentication happens:

Method

Description

Used by

`none`

No client authentication. Only `client_id` is sent in the request body.

Public clients (required)

`client_secret_basic`

Client credentials sent via HTTP Basic auth (`Authorization: Basic <base64(client_id:client_secret)>`). **This is the default for confidential clients.**

Confidential clients

`client_secret_post`

Client credentials sent in the request body (`client_id` and `client_secret` as form parameters).

Confidential clients

**Defaults:** Public clients default to `none`. Confidential clients default to `client_secret_basic` (per [RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591#section-2)).

**Constraints:** Public clients must use `none`. Confidential clients cannot use `none`.

You can set this when registering a client via the dashboard or programmatically. See [OAuth Flows](/docs/guides/auth/oauth-server/oauth-flows#step-5-token-exchange) for examples of each method in action.

## Customizing tokens (optional)[#](#customizing-tokens-optional)

By default, OAuth access tokens include standard claims like `user_id`, `role`, and `client_id`. If you need to customize tokens—for example, to set a specific `audience` claim for third-party validation or add client-specific metadata—use [Custom Access Token Hooks](/docs/guides/auth/auth-hooks/access-token-hook).

Custom Access Token Hooks are triggered for all token issuance, including OAuth flows. You can use the `client_id` parameter to customize tokens based on which OAuth client is requesting them.

### Common use cases[#](#common-use-cases)

*   **Customize `audience` claim**: Set the `aud` claim to the third-party API endpoint for proper JWT validation
*   **Add client-specific permissions**: Include custom claims based on which OAuth client is requesting access
*   **Implement dynamic scopes**: Add metadata that RLS policies can use for fine-grained access control

For more examples, see [Token Security & RLS](/docs/guides/auth/oauth-server/token-security#custom-access-token-hooks).

## Redirect URI configuration[#](#redirect-uri-configuration)

Redirect URIs are critical for OAuth security. Supabase Auth will only redirect to URIs that are explicitly registered with the client.

**Not to be confused with general redirect URLs**

This section is about **OAuth client redirect URIs** - where to send users after they authorize third-party apps to access your Supabase project. This is different from the general [Redirect URLs](/docs/guides/auth/redirect-urls) setting, which controls where to send users after they sign in TO your app using social providers.

**Exact matches only - No wildcards or patterns**

OAuth client redirect URIs require exact, complete URL matches. Unlike general redirect URLs (which support wildcards), OAuth client redirect URIs do NOT support wildcards, patterns, or partial URLs. You must register the full, exact callback URL.

### Best practices[#](#best-practices)

*   **Use HTTPS in production** - Always use HTTPS for redirect URIs in production
*   **Register exact, complete URLs** - Each redirect URI must be the full URL including protocol, domain, path, and port if needed
*   **Use separate OAuth clients per environment** - Create separate OAuth clients for development, staging, and production. This provides better security isolation, allows independent secret rotation, and improves auditability. If you need to use the same client across environments, you can register multiple redirect URIs, but separate clients are recommended.

## Next steps[#](#next-steps)

Now that you've registered your first OAuth client, you're ready to:

*   [Understand OAuth flows](/docs/guides/auth/oauth-server/oauth-flows) - Learn how the authorization code and refresh token flows work
*   [Implement MCP authentication](/docs/guides/auth/oauth-server/mcp-authentication) - Enable AI agent authentication
*   [Secure with RLS](/docs/guides/auth/oauth-server/token-security) - Control data access for OAuth clients


