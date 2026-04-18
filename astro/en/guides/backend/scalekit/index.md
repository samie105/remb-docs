---
title: "Scalekit & Astro"
source: "https://docs.astro.build/en/guides/backend/scalekit/"
canonical_url: "https://docs.astro.build/en/guides/backend/scalekit/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:42.310Z"
content_hash: "2f780ce350d9127c94625c9a3d1d3317a492e0024ad4a147e1f42f42031c6864"
menu_path: ["Scalekit & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/backend/prisma-postgres/index.md", "title": "Prisma Postgres & Astro"}
nav_next: {"path": "astro/en/guides/backend/sentry/index.md", "title": "Monitor your Astro Site with Sentry"}
---

# Scalekit & Astro

[Scalekit](https://scalekit.com/) is an authentication platform built for B2B and AI applications. It provides social login, enterprise SSO, magic links, and more — managing the full OAuth 2.0 / OIDC flow so you get back tokens and a user profile without building any login UI. A single Scalekit environment supports multiple applications (for example, `app.yourcompany.com` and `docs.yourcompany.com`), so your users authenticate once and share the same session across all your properties.

## Initializing Scalekit in Astro

[Section titled “Initializing Scalekit in Astro”](#initializing-scalekit-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   A Scalekit account and environment. If you don’t have one, you can sign up for free at [scalekit.com](https://scalekit.com/) and create a new environment.
*   An Astro project with [`output: 'server'` for on-demand rendering](/en/guides/on-demand-rendering/) enabled.
*   Scalekit credentials for your environment. You can find these in the **Settings > API Credentials** section of your Scalekit dashboard.
    *   `SCALEKIT_ENVIRONMENT_URL`: The URL of your Scalekit environment.
    *   `SCALEKIT_CLIENT_ID`: Your Scalekit client ID.
    *   `SCALEKIT_CLIENT_SECRET`: Your Scalekit client secret.
    *   `SCALEKIT_REDIRECT_URI`: The callback URL Scalekit will redirect to after login (e.g. `http://localhost:4321/api/auth/callback`). Register this in your Scalekit dashboard under **Settings > Redirects**.

### Adding Scalekit credentials

[Section titled “Adding Scalekit credentials”](#adding-scalekit-credentials)

To add your Scalekit credentials to your Astro project, add the following to your `.env` file:

```
SCALEKIT_ENVIRONMENT_URL=YOUR_SCALEKIT_ENVIRONMENT_URLSCALEKIT_CLIENT_ID=YOUR_SCALEKIT_CLIENT_IDSCALEKIT_CLIENT_SECRET=YOUR_SCALEKIT_CLIENT_SECRETSCALEKIT_REDIRECT_URI=http://localhost:4321/api/auth/callback
```

Now, these environment variables are available in your project.

If you would like to have IntelliSense for your environment variables, edit or create the `env.d.ts` in your `src/` directory and add the following:

```
/// <reference types="astro/client" />
interface ImportMetaEnv {  readonly SCALEKIT_ENVIRONMENT_URL: string;  readonly SCALEKIT_CLIENT_ID: string;  readonly SCALEKIT_CLIENT_SECRET: string;  readonly SCALEKIT_REDIRECT_URI: string;}
interface ImportMeta {  readonly env: ImportMetaEnv;}
declare namespace App {  interface Locals {    user?: {      sub: string;      email?: string;      name?: string;    };  }}
```

Read more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your project should now include these files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect to Scalekit, install `@scalekit-sdk/node` in your project.

*   [npm](#tab-panel-1450)
*   [pnpm](#tab-panel-1451)
*   [Yarn](#tab-panel-1452)

```
npm install @scalekit-sdk/node
```

Next, create a folder named `lib` in your `src/` directory and add a Scalekit client file:

```
import { ScalekitClient } from "@scalekit-sdk/node";
export const scalekit = new ScalekitClient(  import.meta.env.SCALEKIT_ENVIRONMENT_URL,  import.meta.env.SCALEKIT_CLIENT_ID,  import.meta.env.SCALEKIT_CLIENT_SECRET,);
export const REDIRECT_URI =  import.meta.env.SCALEKIT_REDIRECT_URI ?? "http://localhost:4321/api/auth/callback";
```

Now, your project should include these files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   **scalekit.ts**
        
    *   env.d.ts
    
*   .env
*   package.json

## Adding authentication with Scalekit

[Section titled “Adding authentication with Scalekit”](#adding-authentication-with-scalekit)

Scalekit handles authentication through a standard OAuth 2.0 / OIDC redirect flow. Your app sends users to Scalekit, they sign in, and Scalekit redirects them back to your callback URL with an authorization code you exchange for tokens. This guide uses the Authorization Code flow with a client secret, which is appropriate for server-side rendered applications.

### Creating auth server endpoints

[Section titled “Creating auth server endpoints”](#creating-auth-server-endpoints)

To add authentication to your project, you will need to create three server endpoints:

*   `GET /api/auth/login`: redirects users to Scalekit to sign in.
*   `GET /api/auth/callback`: exchanges the authorization code for tokens and sets session cookies.
*   `GET /api/auth/logout`: clears session cookies and ends the Scalekit session.

Create these endpoints in the `src/pages/api/auth/` directory of your project. Your project should now include these new files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   scalekit.ts
        
    *   Directorypages/
        
        *   Directoryapi/
            
            *   Directoryauth/
                
                *   **login.ts**
                *   **callback.ts**
                *   **logout.ts**
                
            
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

`login.ts` generates an authorization URL and redirects the user to Scalekit to sign in.

```
import type { APIRoute } from "astro";import { scalekit, REDIRECT_URI } from "../../../lib/scalekit";
export const GET: APIRoute = async () => {  const url = scalekit.getAuthorizationUrl(REDIRECT_URI, {    scopes: ["openid", "profile", "email", "offline_access"],  });  return Response.redirect(url);};
```

`callback.ts` receives the authorization code from Scalekit, exchanges it for tokens, and stores them in HttpOnly cookies.

```
import type { APIRoute } from "astro";import { scalekit, REDIRECT_URI } from "../../../lib/scalekit";
export const GET: APIRoute = async ({ request, cookies }) => {  const url = new URL(request.url);  const code = url.searchParams.get("code");
  if (!code) {    return Response.redirect(new URL("/", request.url).origin);  }
  const { user, idToken, accessToken, refreshToken } =    await scalekit.authenticateWithCode(code, REDIRECT_URI);
  const secure = url.protocol === "https:";  const cookieOptions = { httpOnly: true, path: "/", sameSite: "lax" as const, secure };
  cookies.set("sk-id-token", idToken, cookieOptions);  cookies.set("sk-access-token", accessToken, cookieOptions);  cookies.set("sk-refresh-token", refreshToken, cookieOptions);
  return Response.redirect(new URL("/", request.url).origin);};
```

`logout.ts` clears the session cookies and redirects to Scalekit’s logout endpoint to end the Scalekit session.

```
import type { APIRoute } from "astro";import { scalekit } from "../../../lib/scalekit";
export const GET: APIRoute = async ({ request, cookies }) => {  const idToken = cookies.get("sk-id-token")?.value;
  cookies.delete("sk-id-token", { path: "/" });  cookies.delete("sk-access-token", { path: "/" });  cookies.delete("sk-refresh-token", { path: "/" });
  const logoutUrl = scalekit.getLogoutUrl({    idTokenHint: idToken,    postLogoutRedirectUri: new URL("/", request.url).origin,  });
  return Response.redirect(logoutUrl);};
```

### Adding session middleware

[Section titled “Adding session middleware”](#adding-session-middleware)

Create a `src/middleware.ts` file to validate the access token on every request and populate `Astro.locals.user` with the authenticated user’s profile. When the access token has expired, the middleware automatically refreshes it using the refresh token.

```
import { defineMiddleware } from "astro:middleware";import type { IdTokenClaim } from "@scalekit-sdk/node";import { scalekit } from "./lib/scalekit";
export const onRequest = defineMiddleware(async (context, next) => {  const accessToken = context.cookies.get("sk-access-token")?.value;
  if (accessToken) {    try {      const claims = await scalekit.validateToken<IdTokenClaim>(accessToken);      context.locals.user = {        sub: claims.sub,        email: claims.email,        name: claims.name,      };    } catch {      // Access token invalid or expired — try to refresh      const refreshToken = context.cookies.get("sk-refresh-token")?.value;      if (refreshToken) {        try {          const { accessToken: newToken } =            await scalekit.refreshAccessToken(refreshToken);
          const secure = new URL(context.request.url).protocol === "https:";          context.cookies.set("sk-access-token", newToken, {            httpOnly: true,            path: "/",            sameSite: "lax",            secure,          });
          const claims = await scalekit.validateToken<IdTokenClaim>(newToken);          context.locals.user = {            sub: claims.sub,            email: claims.email,            name: claims.name,          };        } catch {          // Refresh failed — clear session cookies          context.cookies.delete("sk-id-token", { path: "/" });          context.cookies.delete("sk-access-token", { path: "/" });          context.cookies.delete("sk-refresh-token", { path: "/" });        }      }    }  }
  return next();});
```

### Creating an authenticated page

[Section titled “Creating an authenticated page”](#creating-an-authenticated-page)

Now that your middleware populates `Astro.locals.user`, you can create pages that show different content based on authentication state.

`dashboard.astro` is a page that is only accessible to authenticated users. It reads the user from `Astro.locals`, set by the middleware, and redirects to the home page if the user is not signed in.

```
---import Layout from "../layouts/Layout.astro";
const user = Astro.locals.user;
if (!user) {  return Astro.redirect("/");}---
<Layout title="Dashboard">  <h1>Welcome, {user.name ?? user.email}</h1>  <p>You are signed in.</p>  <a href="/api/auth/logout">Sign out</a></Layout>
```

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Scalekit Node.js SDK documentation](https://github.com/scalekit-inc/scalekit-sdk-node)
*   [Astro blog tutorial with Scalekit authentication (Authorization Code flow)](https://github.com/scalekit-developers/astro-scalekit-auth-example)
*   [Scalekit developer docs site source (PKCE flow, no SDK)](https://github.com/scalekit-inc/developer-docs)

## More backend service guides

*   ![](/logos/appwriteio.svg)
    
    ### [Appwrite](/en/guides/backend/appwrite/)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](/en/guides/backend/firebase/)
    
*   ![](/logos/neon.svg)
    
    ### [Neon](/en/guides/backend/neon/)
    
*   ![](/logos/prisma-postgres.svg)
    
    ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)
    
*   ![](/logos/scalekit.svg)
    
    ### [Scalekit](/en/guides/backend/scalekit/)
    
*   ![](/logos/sentry.svg)
    
    ### [Sentry](/en/guides/backend/sentry/)
    
*   ![](/logos/supabase.svg)
    
    ### [Supabase](/en/guides/backend/supabase/)
    
*   ![](/logos/turso.svg)
    
    ### [Turso](/en/guides/backend/turso/)
    
*   ![](/logos/xata.svg)
    
    ### [Xata](/en/guides/backend/xata/)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


