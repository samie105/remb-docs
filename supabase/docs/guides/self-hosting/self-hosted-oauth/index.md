---
title: "Configure Social Login (OAuth) Providers"
source: "https://supabase.com/docs/guides/self-hosting/self-hosted-oauth"
canonical_url: "https://supabase.com/docs/guides/self-hosting/self-hosted-oauth"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:41.310Z"
content_hash: "f437af716f4998d840b305945d521e8b0081b8e5ba147dd923f4f0b272f5b6f4"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure Social Login (OAuth)","Configure Social Login (OAuth)"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Configure Social Login (OAuth)","Configure Social Login (OAuth)"]
nav_prev: {"path": "../self-hosted-functions/index.md", "title": "Self-Hosted Functions"}
nav_next: {"path": "../self-hosted-phone-mfa/index.md", "title": "Configure Phone Login & MFA"}
---

# 

Configure Social Login (OAuth) Providers

## 

Set up social login (OAuth/OIDC) providers for self-hosted Supabase with Docker.

* * *

This guide covers the **server-side configuration** required to enable social login providers on a self-hosted Supabase instance running with Docker Compose. This applies to all OAuth and OIDC-based providers, including third-party identity providers like Keycloak.

## Before you begin[#](#before-you-begin)

You need:

*   A working self-hosted Supabase installation. See [Self-Hosting with Docker](/docs/guides/self-hosting/docker).
*   `API_EXTERNAL_URL` set to the publicly reachable URL of your Supabase instance (e.g., `https://<your-domain>`).

HTTPS is strongly recommended in production. Most OAuth providers reject `http://` callback URLs (except `localhost`).

Your **OAuth callback URL** is built from `API_EXTERNAL_URL`. For example, if `API_EXTERNAL_URL` is `https://<your-domain>`, the callback URL will become:

```
1https://<your-domain>/auth/v1/callback
```

You will have to register this URL with each OAuth provider.

## OAuth request flow[#](#oauth-request-flow)

When a user signs in with an OAuth provider, the following flow occurs:

1.  Your app calls `supabase.auth.signInWithOAuth()` and the browser redirects to the Auth service
2.  API gateway (Kong) routes the request to the Auth container (`/auth/v1/authorize`)
3.  Auth redirects the user to the OAuth provider (e.g., Google) for consent
4.  The provider redirects back to `https://<your-domain>/auth/v1/callback`
5.  Auth exchanges the authorization code for tokens and redirects the user to your `SITE_URL` or an allowed redirect URL

## Auth environment variables[#](#auth-environment-variables)

The Auth service (GoTrue) uses the prefix `GOTRUE_EXTERNAL_` followed by a provider name for all OAuth configuration. For example, when using Google:

*   `GOTRUE_EXTERNAL_GOOGLE_ENABLED`
*   `GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID`
*   `GOTRUE_EXTERNAL_GOOGLE_SECRET`
*   `GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI`

## Step-by-step configuration[#](#step-by-step-configuration)

The default `.env.example` and `docker-compose.yml` include commented-out placeholders for Google, GitHub, and Azure.

### Step 1: Register your app with the provider[#](#step-1-register-your-app-with-the-provider)

1.  Go to the OAuth provider's developer console and create an application.
2.  Set the **authorized redirect URL**, e.g., `https://<your-domain>/auth/v1/callback`
3.  Copy the **client ID** and **client secret** into your `.env` file.

### Step 2: Configure environment variables[#](#step-2-configure-environment-variables)

Uncomment the lines for your provider in `.env` and add your client ID and secret, e.g., for Google:

```
1GOOGLE_ENABLED=true2GOOGLE_CLIENT_ID=your-client-id3GOOGLE_SECRET=your-client-secret
```

### Step 3: Enable the matching lines in Docker Compose configuration[#](#step-3-enable-the-matching-lines-in-docker-compose-configuration)

Uncomment the corresponding `GOTRUE_EXTERNAL_` lines in the `auth` service's `environment`:

```
1auth:2  environment:3    # ... existing variables ...4    GOTRUE_EXTERNAL_GOOGLE_ENABLED: ${GOOGLE_ENABLED}5    GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID: ${GOOGLE_CLIENT_ID}6    GOTRUE_EXTERNAL_GOOGLE_SECRET: ${GOOGLE_SECRET}7    GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI: ${API_EXTERNAL_URL}/auth/v1/callback
```

For providers **not** pre-configured in the files (see the [full provider list](#other-supported-providers) below), add the lines manually following the same pattern: variables in `.env`, passthrough with `GOTRUE_EXTERNAL_PROVIDER_` in `docker-compose.yml`.

### Step 4: Restart the auth service[#](#step-4-restart-the-auth-service)

```
1docker compose up -d --force-recreate --no-deps auth
```

### Step 5: Verify the configuration[#](#step-5-verify-the-configuration)

Check that the provider is enabled:

```
1curl -H 'apikey: your-anon-key' https://<your-domain>/auth/v1/settings
```

The response should include your provider under `external`:

```
1{2  "external": {3    "google": true4  }5}
```

## Provider-specific setup[#](#provider-specific-setup)

**Google Cloud Console setup:**

1.  Go to [Google Cloud Console](https://console.cloud.google.com/)
2.  Create or select a project
3.  Select **Solutions** > **All products** in the navigation menu on the left
4.  Go to **APIs & services** > **OAuth consent screen** and click **Get started**
5.  Follow the configuration steps and add an **External** app
6.  Go to **APIs & Services** > **Credentials**
7.  Click **Create Credentials** > **OAuth client ID**
8.  Set application type to **Web application**
9.  Under **Authorized redirect URIs**, add: `https://<your-domain>/auth/v1/callback`
10.  Click **Create** and copy the client ID and client secret

**`.env`:**

```
1GOOGLE_ENABLED=true2GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com3GOOGLE_SECRET=your-google-client-secret
```

**`docker-compose.yml`:**

```
1auth:2  environment:3    # ... existing variables ...4    GOTRUE_EXTERNAL_GOOGLE_ENABLED: ${GOOGLE_ENABLED}5    GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID: ${GOOGLE_CLIENT_ID}6    GOTRUE_EXTERNAL_GOOGLE_SECRET: ${GOOGLE_SECRET}7    GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI: ${API_EXTERNAL_URL}/auth/v1/callback
```

## Other supported providers[#](#other-supported-providers)

Supabase Auth supports the following OAuth providers:

Provider

Env prefix

Additional variables

Docs

Apple

`APPLE_`

\-

[Login with Apple](/docs/guides/auth/social-login/auth-apple)

Azure (Microsoft)

`AZURE_`

`URL` (tenant URL)

[Login with Azure](/docs/guides/auth/social-login/auth-azure)

Bitbucket

`BITBUCKET_`

\-

[Login with Bitbucket](/docs/guides/auth/social-login/auth-bitbucket)

Discord

`DISCORD_`

\-

[Login with Discord](/docs/guides/auth/social-login/auth-discord)

Facebook

`FACEBOOK_`

\-

[Login with Facebook](/docs/guides/auth/social-login/auth-facebook)

Figma

`FIGMA_`

\-

[Login with Figma](/docs/guides/auth/social-login/auth-figma)

GitHub

`GITHUB_`

`URL` (for GitHub Enterprise)

[Login with GitHub](/docs/guides/auth/social-login/auth-github)

GitLab

`GITLAB_`

`URL` (for self-hosted GitLab)

[Login with GitLab](/docs/guides/auth/social-login/auth-gitlab)

Google

`GOOGLE_`

\-

[Login with Google](/docs/guides/auth/social-login/auth-google)

Kakao

`KAKAO_`

\-

[Login with Kakao](/docs/guides/auth/social-login/auth-kakao)

Keycloak (OIDC)

`KEYCLOAK_`

`URL` (realm URL, **required**)

[Login with Keycloak](/docs/guides/auth/social-login/auth-keycloak)

LinkedIn (OIDC)

`LINKEDIN_OIDC_`

\-

[Login with LinkedIn](/docs/guides/auth/social-login/auth-linkedin)

Notion

`NOTION_`

\-

[Login with Notion](/docs/guides/auth/social-login/auth-notion)

Slack (OIDC)

`SLACK_OIDC_`

\-

[Login with Slack](/docs/guides/auth/social-login/auth-slack)

Snapchat

`SNAPCHAT_`

\-

\-

Spotify

`SPOTIFY_`

\-

[Login with Spotify](/docs/guides/auth/social-login/auth-spotify)

Twitch

`TWITCH_`

\-

[Login with Twitch](/docs/guides/auth/social-login/auth-twitch)

Twitter

`TWITTER_`

\-

[Login with Twitter](/docs/guides/auth/social-login/auth-twitter)

WorkOS

`WORKOS_`

\-

[Login with WorkOS](/docs/guides/auth/social-login/auth-workos)

Zoom

`ZOOM_`

\-

[Login with Zoom](/docs/guides/auth/social-login/auth-zoom)

For each provider, you need at minimum `ENABLED`, `CLIENT_ID`, `SECRET`, and `REDIRECT_URI` in `.env` and `docker-compose.yml`.

**LinkedIn (OIDC)** and **Slack (OIDC)** use multi-word env prefixes. The full Docker Compose variables are `GOTRUE_EXTERNAL_LINKEDIN_OIDC_CLIENT_ID` and `GOTRUE_EXTERNAL_SLACK_OIDC_CLIENT_ID` respectively - not `LINKEDIN_CLIENT_ID` or `SLACK_CLIENT_ID`.

## Test the login flow[#](#test-the-login-flow)

You can test OAuth with the following minimal HTML page:

*   Save the code below to `index.html`
*   Start `python -m http.server 3000` in the same directory
*   Make sure `SITE_URL` is set to `http://localhost:3000` in your self-hosted Supabase `.env` configuration
*   Open your browser and go to `http://localhost:3000`

```
1<!doctype html>2<html>3  <body>4    <h1>Supabase OAuth Test</h1>5    <button id="loginBtn">Sign in with Google</button>6    <pre id="result"></pre>78    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>9    <script>10      document.addEventListener('DOMContentLoaded', function () {11        const SUPABASE_URL = 'https://<your-domain>'12        const SUPABASE_ANON_KEY = 'your-anon-key'1314        const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY)1516        const button = document.getElementById('loginBtn')1718        button.addEventListener('click', async () => {19          const { error } = await supabase.auth.signInWithOAuth({20            provider: 'google',21          })2223          if (error) {24            document.getElementById('result').textContent = JSON.stringify(error, null, 2)25          }26        })2728        supabase.auth.getSession().then(({ data }) => {29          if (data.session) {30            document.getElementById('result').textContent =31              'Logged in as: ' + data.session.user.email32          }33        })34      })35    </script>36  </body>37</html>
```

For detailed client-side integration, see [Social Login](/docs/guides/auth/social-login).

## Troubleshooting[#](#troubleshooting)

### "Provider not enabled" or provider seen as false in settings[#](#provider-not-enabled-or-provider-seen-as-false-in-settings)

*   Check that `GOTRUE_EXTERNAL_*_ENABLED` is set to `true` in `docker-compose.yml`
*   Verify the `.env` variable is not empty, e.g., check with `docker compose exec auth env | grep GOOGLE`

### Variables added to the environment but provider still not working[#](#variables-added-to-the-environment-but-provider-still-not-working)

Configuration variables from `.env` are **not** automatically available inside the container unless there's a matching passthrough definition in `docker-compose.yml`. Check, e.g., for:

```
1GOTRUE_EXTERNAL_GOOGLE_ENABLED: ${GOOGLE_ENABLED}
```

Run `docker compose exec auth env | grep GOTRUE_EXTERNAL` to verify the variables are reaching the container.

### Site URL or redirect URL errors after login[#](#site-url-or-redirect-url-errors-after-login)

After a successful OAuth login, the Auth service redirects to `SITE_URL` or a URL from `ADDITIONAL_REDIRECT_URLS`. Ensure:

*   `SITE_URL` in `.env` is set to your application's URL
*   If your app uses a different redirect URL, add it to `ADDITIONAL_REDIRECT_URLS` (comma-separated)

### Nonce check failure on mobile (Google Sign In)[#](#nonce-check-failure-on-mobile-google-sign-in)

When using Google Sign In on mobile with ID tokens, nonce verification may fail because mobile SDKs don't always support the nonce flow that the Auth service expects.

`GOTRUE_EXTERNAL_SKIP_NONCE_CHECK` disables nonce validation on ID tokens, which weakens replay-attack protection. Treat it as a **short-lived troubleshooting workaround**, not a permanent fix:

*   Enable it only in the environment where you're debugging the issue.
*   Revert it as soon as the issue is resolved.
*   Prefer fixing the client-side nonce handling or switching to an OAuth flow (authorization code with PKCE) that avoids ID-token nonce issues entirely.

To enable it, uncomment the following line in `docker-compose.yml`:

```
1GOTRUE_EXTERNAL_SKIP_NONCE_CHECK: true
```

### Auth service fails to start[#](#auth-service-fails-to-start)

Check the auth container logs:

```
1docker compose logs auth
```

Common causes:

*   Missing required environment variable (e.g., `CLIENT_ID` or `SECRET` is empty)
*   Invalid `API_EXTERNAL_URL` (must be a valid URL with protocol)

## Environment variable reference[#](#environment-variable-reference)

All OAuth-related environment variables for the `auth` service in `docker-compose.yml`:

Variable

Description

Required

`GOTRUE_EXTERNAL_*_ENABLED`

Enable the provider (`true`/`false`)

Yes

`GOTRUE_EXTERNAL_*_CLIENT_ID`

OAuth client ID from the provider

Yes

`GOTRUE_EXTERNAL_*_SECRET`

OAuth client secret from the provider

Yes

`GOTRUE_EXTERNAL_*_REDIRECT_URI`

Callback URL: `${API_EXTERNAL_URL}/auth/v1/callback`

Yes

`GOTRUE_SITE_URL`

Default redirect URL after authentication (set via `SITE_URL` in `.env`)

Yes

## Additional resources[#](#additional-resources)

*   [Redirect URLs](/docs/guides/auth/redirect-urls)
*   [Auth server on GitHub](https://github.com/supabase/auth) (check README and `example.env`)
