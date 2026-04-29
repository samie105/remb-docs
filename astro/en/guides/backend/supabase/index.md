---
title: "Supabase & Astro"
source: "https://docs.astro.build/en/guides/backend/supabase/"
canonical_url: "https://docs.astro.build/en/guides/backend/supabase/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:48.706Z"
content_hash: "bbb148d67766c1876f604d63c76aefe7cf7b7b2f59f76148ec66d47269ef0eff"
menu_path: ["Supabase & Astro"]
section_path: []
nav_prev: {"path": "astro/en/guides/backend/sentry/index.md", "title": "Monitor your Astro Site with Sentry"}
nav_next: {"path": "astro/en/guides/backend/turso/index.md", "title": "Turso & Astro"}
---

# Supabase & Astro

[Supabase](https://supabase.com/) is an open source Firebase alternative. It provides a Postgres database, authentication, edge functions, realtime subscriptions, and storage.

## Initializing Supabase in Astro

[Section titled “Initializing Supabase in Astro”](#initializing-supabase-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

*   A Supabase project. If you don’t have one, you can sign up for free at [supabase.com](https://supabase.com/) and create a new project.
*   An Astro project with [`output: 'server'` for on-demand rendering](../../on-demand-rendering/index.md) enabled.
*   Supabase credentials for your project. You can find these in the **Settings > API** tab of your Supabase project.
    *   `SUPABASE_URL`: The URL of your Supabase project.
    *   `SUPABASE_ANON_KEY`: The anonymous key for your Supabase project.

### Adding Supabase credentials

[Section titled “Adding Supabase credentials”](#adding-supabase-credentials)

To add your Supabase credentials to your Astro project, add the following to your `.env` file:

```
SUPABASE_URL=YOUR_SUPABASE_URLSUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
```

Now, these environment variables are available in your project.

If you would like to have IntelliSense for your environment variables, edit or create the `env.d.ts` in your `src/` directory and add the following:

```
interface ImportMetaEnv {  readonly SUPABASE_URL: string  readonly SUPABASE_ANON_KEY: string}
interface ImportMeta {  readonly env: ImportMetaEnv}
```

Your project should now include these files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect to Supabase, you will need to install `@supabase/supabase-js` in your project.

*   [npm](#tab-panel-1456)
*   [pnpm](#tab-panel-1457)
*   [Yarn](#tab-panel-1458)

```
npm install @supabase/supabase-js
```

Next, create a folder named `lib` in your `src/` directory. This is where you will add your Supabase client.

In `supabase.ts`, add the following to initialize your Supabase client:

```
import { createClient } from "@supabase/supabase-js";
export const supabase = createClient(  import.meta.env.SUPABASE_URL,  import.meta.env.SUPABASE_ANON_KEY,);
```

Now, your project should include these files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   **supabase.ts**
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

## Adding authentication with Supabase

[Section titled “Adding authentication with Supabase”](#adding-authentication-with-supabase)

Supabase provides authentication out of the box. It supports email/password authentication and OAuth authentication with many providers including GitHub, Google, and several others.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

*   An Astro project [initialized with Supabase](#initializing-supabase-in-astro).
*   A Supabase project with email/password authentication enabled. You can enable this in the **Authentication > Providers** tab of your Supabase project.

### Creating auth server endpoints

[Section titled “Creating auth server endpoints”](#creating-auth-server-endpoints)

To add authentication to your project, you will need to create a few server endpoints. These endpoints will be used to register, sign in, and sign out users.

*   `POST /api/auth/register`: to register a new user.
*   `POST /api/auth/signin`: to sign in a user.
*   `GET /api/auth/signout`: to sign out a user.

Create these endpoints in the `src/pages/api/auth` directory of your project. If you are using `static` rendering mode, you must specify `export const prerender = false` at the top of each file to render these endpoints on demand. Your project should now include these new files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   supabase.ts
        
    *   Directorypages/
        
        *   Directoryapi/
            
            *   Directoryauth/
                
                *   **signin.ts**
                *   **signout.ts**
                *   **register.ts**
                
            
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

`register.ts` creates a new user in Supabase. It accepts a `POST` request with the an email and password. It then uses the Supabase SDK to create a new user.

```
// With `output: 'static'` configured:// export const prerender = false;import type { APIRoute } from "astro";import { supabase } from "../../../lib/supabase";
export const POST: APIRoute = async ({ request, redirect }) => {  const formData = await request.formData();  const email = formData.get("email")?.toString();  const password = formData.get("password")?.toString();
  if (!email || !password) {    return new Response("Email and password are required", { status: 400 });  }
  const { error } = await supabase.auth.signUp({    email,    password,  });
  if (error) {    return new Response(error.message, { status: 500 });  }
  return redirect("/signin");};
```

`signin.ts` signs in a user. It accepts a `POST` request with the an email and password. It then uses the Supabase SDK to sign in the user.

```
// With `output: 'static'` configured:// export const prerender = false;import type { APIRoute } from "astro";import { supabase } from "../../../lib/supabase";
export const POST: APIRoute = async ({ request, cookies, redirect }) => {  const formData = await request.formData();  const email = formData.get("email")?.toString();  const password = formData.get("password")?.toString();
  if (!email || !password) {    return new Response("Email and password are required", { status: 400 });  }
  const { data, error } = await supabase.auth.signInWithPassword({    email,    password,  });
  if (error) {    return new Response(error.message, { status: 500 });  }
  const { access_token, refresh_token } = data.session;  cookies.set("sb-access-token", access_token, {    path: "/",  });  cookies.set("sb-refresh-token", refresh_token, {    path: "/",  });  return redirect("/dashboard");};
```

`signout.ts` signs out a user. It accepts a `GET` request and removes the user’s access and refresh tokens.

```
// With `output: 'static'` configured:// export const prerender = false;import type { APIRoute } from "astro";
export const GET: APIRoute = async ({ cookies, redirect }) => {  cookies.delete("sb-access-token", { path: "/" });  cookies.delete("sb-refresh-token", { path: "/" });  return redirect("/signin");};
```

### Creating auth pages

[Section titled “Creating auth pages”](#creating-auth-pages)

Now that you have created your server endpoints, create the pages that will use them.

*   `src/pages/register`: contains a form to register a new user.
*   `src/pages/signin`: contains a form to sign in a user.
*   `src/pages/dashboard`: contains a page that is only accessible to authenticated users.

Create these pages in the `src/pages` directory. Your project should now include these new files:

*   Directorysrc/
    
    *   Directorylib/
        
        *   supabase.ts
        
    *   Directorypages/
        
        *   Directoryapi/
            
            *   Directoryauth/
                
                *   signin.ts
                *   signout.ts
                *   register.ts
                
            
        *   **register.astro**
        *   **signin.astro**
        *   **dashboard.astro**
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

`register.astro` contains a form to register a new user. It accepts an email and password and sends a `POST` request to `/api/auth/register`.

```
---import Layout from "../layouts/Layout.astro";---
<Layout title="Register">  <h1>Register</h1>  <p>Already have an account? <a href="/signin">Sign in</a></p>  <form action="/api/auth/register" method="post">    <label for="email">Email</label>    <input type="email" name="email" id="email" />    <label for="password">Password</label>    <input type="password" name="password" id="password" />    <button type="submit">Register</button>  </form></Layout>
```

`signin.astro` contains a form to sign in a user. It accepts an email and password and sends a `POST` request to `/api/auth/signin`. It also checks for the presence of the access and refresh tokens. If they are present, it redirects to the dashboard.

```
---import Layout from "../layouts/Layout.astro";
const { cookies, redirect } = Astro;
const accessToken = cookies.get("sb-access-token");const refreshToken = cookies.get("sb-refresh-token");
if (accessToken && refreshToken) {  return redirect("/dashboard");}---
<Layout title="Sign in">  <h1>Sign in</h1>  <p>New here? <a href="/register">Create an account</a></p>  <form action="/api/auth/signin" method="post">    <label for="email">Email</label>    <input type="email" name="email" id="email" />    <label for="password">Password</label>    <input type="password" name="password" id="password" />    <button type="submit">Login</button>  </form></Layout>
```

`dashboard.astro` contains a page that is only accessible to authenticated users. It checks for the presence of the access and refresh tokens. If they are not present or are invalid, it redirects to the sign in page.

```
---import Layout from "../layouts/Layout.astro";import { supabase } from "../lib/supabase";
const accessToken = Astro.cookies.get("sb-access-token");const refreshToken = Astro.cookies.get("sb-refresh-token");
if (!accessToken || !refreshToken) {  return Astro.redirect("/signin");}
let session;try {  session = await supabase.auth.setSession({    refresh_token: refreshToken.value,    access_token: accessToken.value,  });  if (session.error) {    Astro.cookies.delete("sb-access-token", {      path: "/",    });    Astro.cookies.delete("sb-refresh-token", {      path: "/",    });    return Astro.redirect("/signin");  }} catch (error) {  Astro.cookies.delete("sb-access-token", {    path: "/",  });  Astro.cookies.delete("sb-refresh-token", {    path: "/",  });  return Astro.redirect("/signin");}
const email = session.data.user?.email;---<Layout title="dashboard">  <h1>Welcome {email}</h1>  <p>We are happy to see you here</p>  <form action="/api/auth/signout">    <button type="submit">Sign out</button>  </form></Layout>
```

### Adding OAuth authentication

[Section titled “Adding OAuth authentication”](#adding-oauth-authentication)

To add OAuth authentication to your project, you will need to edit your Supabase client to enable authentication flow with `"pkce"`. You can read more about authentication flows in the [Supabase documentation](https://supabase.com/docs/guides/auth/server-side-rendering#understanding-the-authentication-flow).

```
import { createClient } from "@supabase/supabase-js";
export const supabase = createClient(  import.meta.env.SUPABASE_URL,  import.meta.env.SUPABASE_ANON_KEY,  {    auth: {      flowType: "pkce",    },  },);
```

Next, in the Supabase dashboard, enable the OAuth provider you would like to use. You can find the list of supported providers in the **Authentication > Providers** tab of your Supabase project.

The following example uses GitHub as the OAuth provider. To connect your project to GitHub, follow the steps in the [Supabase documentation](https://supabase.com/docs/guides/auth/social-login/auth-github).

Then, create a new server endpoint to handle the OAuth callback at `src/pages/api/auth/callback.ts`. This endpoint will be used to exchange the OAuth code for an access and refresh token.

```
import type { APIRoute } from "astro";import { supabase } from "../../../lib/supabase";
export const GET: APIRoute = async ({ url, cookies, redirect }) => {  const authCode = url.searchParams.get("code");
  if (!authCode) {    return new Response("No code provided", { status: 400 });  }
  const { data, error } = await supabase.auth.exchangeCodeForSession(authCode);
  if (error) {    return new Response(error.message, { status: 500 });  }
  const { access_token, refresh_token } = data.session;
  cookies.set("sb-access-token", access_token, {    path: "/",  });  cookies.set("sb-refresh-token", refresh_token, {    path: "/",  });
  return redirect("/dashboard");};
```

Next, edit the sign in page to include a new button to sign in with the OAuth provider. This button should send a `POST` request to `/api/auth/signin` with the `provider` set to the name of the OAuth provider.

```
---import Layout from "../layouts/Layout.astro";
const { cookies, redirect } = Astro;
const accessToken = cookies.get("sb-access-token");const refreshToken = cookies.get("sb-refresh-token");
if (accessToken && refreshToken) {  return redirect("/dashboard");}---
<Layout title="Sign in">  <h1>Sign in</h1>  <p>New here? <a href="/register">Create an account</a></p>  <form action="/api/auth/signin" method="post">    <label for="email">Email</label>    <input type="email" name="email" id="email" />    <label for="password">Password</label>    <input type="password" name="password" id="password" />    <button type="submit">Login</button>    <button value="github" name="provider" type="submit">Sign in with GitHub</button>  </form></Layout>
```

Finally, edit the sign in server endpoint to handle the OAuth provider. If the `provider` is present, it will redirect to the OAuth provider. Otherwise, it will sign in the user with the email and password.

```
import type { APIRoute } from "astro";import { supabase } from "../../../lib/supabase";import type { Provider } from "@supabase/supabase-js";
export const POST: APIRoute = async ({ request, cookies, redirect }) => {  const formData = await request.formData();  const email = formData.get("email")?.toString();  const password = formData.get("password")?.toString();  const provider = formData.get("provider")?.toString();
  const validProviders = ["google", "github", "discord"];
  if (provider && validProviders.includes(provider)) {    const { data, error } = await supabase.auth.signInWithOAuth({      provider: provider as Provider,      options: {        redirectTo: "http://localhost:4321/api/auth/callback"      },    });
    if (error) {      return new Response(error.message, { status: 500 });    }
    return redirect(data.url);  }
  if (!email || !password) {    return new Response("Email and password are required", { status: 400 });  }
  const { data, error } = await supabase.auth.signInWithPassword({    email,    password,  });
  if (error) {    return new Response(error.message, { status: 500 });  }
  const { access_token, refresh_token } = data.session;  cookies.set("sb-access-token", access_token, {    path: "/",  });  cookies.set("sb-refresh-token", refresh_token, {    path: "/",  });  return redirect("/dashboard");};
```

After creating the OAuth callback endpoint and editing the sign in page and server endpoint, your project should have the following file structure:

*   Directorysrc/
    
    *   Directorylib/
        
        *   supabase.ts
        
    *   Directorypages/
        
        *   Directoryapi/
            
            *   Directoryauth/
                
                *   signin.ts
                *   signout.ts
                *   register.ts
                *   callback.ts
                
            
        *   register.astro
        *   signin.astro
        *   dashboard.astro
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

## Community Resources

[Section titled “Community Resources”](#community-resources)

*   [Getting into the holiday spirit with Astro, React, and Supabase](https://www.aleksandra.codes/astro-supabase)
*   [Astro and Supabase auth demo](https://github.com/kevinzunigacuellar/astro-supabase)

## More backend service guides

*   ![](/logos/appwriteio.svg)
    
    ### [Appwrite](../appwrite/index.md)
    
*   ![](/logos/firebase.svg)
    
    ### [Firebase](../firebase/index.md)
    
*   ![](/logos/neon.svg)
    
    ### [Neon](../neon/index.md)
    
*   ![](/logos/prisma-postgres.svg)
    
    ### [Prisma Postgres](../prisma-postgres/index.md)
    
*   ![](/logos/scalekit.svg)
    
    ### [Scalekit](../scalekit/index.md)
    
*   ![](/logos/sentry.svg)
    
    ### [Sentry](../sentry/index.md)
    
*   ![](/logos/supabase.svg)
    
    ### [Supabase](index.md)
    
*   ![](/logos/turso.svg)
    
    ### [Turso](../turso/index.md)
    
*   ![](/logos/xata.svg)
    
    ### [Xata](../xata/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
