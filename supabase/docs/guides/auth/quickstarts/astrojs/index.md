---
title: "Use Supabase Auth with Astro"
source: "https://supabase.com/docs/guides/auth/quickstarts/astrojs"
canonical_url: "https://supabase.com/docs/guides/auth/quickstarts/astrojs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:31.393Z"
content_hash: "5b1259c1e517e7b6e1a771baa630b5a60b860744a22753b5b4612d00c1f3e8aa"
menu_path: ["Auth","Auth","Getting Started","Getting Started","Astro","Astro"]
section_path: ["Auth","Auth","Getting Started","Getting Started","Astro","Astro"]
nav_prev: {"path": "supabase/docs/guides/auth/oauth-server/token-security/index.md", "title": "Token Security and Row Level Security"}
nav_next: {"path": "supabase/docs/guides/auth/oauth-server/oauth-flows/index.md", "title": "OAuth 2.1 Flows"}
---

# 

Use Supabase Auth with Astro

## 

Learn how to configure Supabase Auth for Astro with server-side rendering.

* * *

1

### Create a new Supabase project

Head over to [database.new](https://database.new) and create a new Supabase project.

Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql/new).

###### SQL\_EDITOR

```
1select * from auth.users;
```

2

### Create an Astro app

Create a new Astro app using the `npm create` command.

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

###### Terminal

```
1npm create astro@latest my-app2cd my-app
```

3

### Install Supabase libraries and Node adapter

Install the `@supabase/supabase-js` client library, `@supabase/ssr` for server-side auth, and the `@astrojs/node` adapter to enable server-side rendering.

###### Terminal

```
1npm install @supabase/supabase-js @supabase/ssr @astrojs/node
```

4

### Configure Astro for SSR

Update your `astro.config.mjs` to enable server-side rendering with the Node adapter.

###### astro.config.mjs

```
1import { defineConfig } from "astro/config";2import node from "@astrojs/node";34export default defineConfig({5  output: "server",6  adapter: node({7    mode: "standalone",8  }),9});
```

5

### Declare Supabase Environment Variables

Create a `.env.local` file and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### .env.local

```
1PUBLIC_SUPABASE_URL=your-project-url2PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_key
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=astro), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

6

### Create a Supabase client helper

Create a utility file to initialize the Supabase client with SSR support:

###### src/lib/supabase.ts

```
1import { createServerClient, parseCookieHeader } from "@supabase/ssr";2import type { AstroCookies } from "astro";34const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL5const supabasePublishableKey = import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY67export function createClient({8  request,9  cookies,10}: {11  request: Request;12  cookies: AstroCookies;13}) {14  return createServerClient(15    supabaseUrl,16    supabasePublishableKey,17    {18      cookies: {19        getAll() {20          return parseCookieHeader(21            request.headers.get("Cookie") ?? ""22          );23        },24        setAll(cookiesToSet) {25          cookiesToSet.forEach(({ name, value, options }) =>26            cookies.set(name, value, options)27          );28        },29      },30    }31  );32}
```

7

### Create authentication actions

Create a new file at `src/actions/index.ts` to define server-side authentication actions for signing up, signing in, and signing out:

###### src/actions/index.ts

```
1import { defineAction } from "astro:actions";2import { z } from "astro/zod";3import { createClient } from "../lib/supabase";45export const server = {6  signUp: defineAction({7    accept: "form",8    input: z.object({9      email: z.string().email(),10      password: z.string().min(6),11    }),12    handler: async (input, context) => {13      try {14        const supabase = createClient({15          request: context.request,16          cookies: context.cookies,17        });1819        const { error } = await supabase.auth.signUp({20          email: input.email,21          password: input.password,22          options: {23            emailRedirectTo: "http://localhost:4321/auth/callback",24          },25        });2627        if (error) {28          return {29            success: false,30            message: error.message,31          };32        }3334        return {35          success: true,36          message: "Check your email to confirm your account",37        };38      } catch (err) {39        return {40          success: false,41          message: "Unexpected error",42        };43      }44    },45  }),46  signIn: defineAction({47    accept: "form",48    input: z.object({49      email: z.string().email(),50      password: z.string(),51    }),52    handler: async (input, context) => {53      try {54        const supabase = createClient({55          request: context.request,56          cookies: context.cookies,57        });5859        const { error } = await supabase.auth.signInWithPassword({60          email: input.email,61          password: input.password,62        });6364        if (error) {65          return {66            success: false,67            message: error.message,68          };69        }7071        return {72          success: true,73          message: "Signed in successfully",74        };75      } catch (err) {76        return {77          success: false,78          message: "Unexpected error",79        };80      }81    },82  }),83  signOut: defineAction({84    handler: async (_, context) => {85      try {86        const supabase = createClient({87          request: context.request,88          cookies: context.cookies,89        });9091        await supabase.auth.signOut();9293        return {94          success: true,95        };96      } catch (err) {97        return {98          success: false,99          message: "Failed to sign out",100        };101      }102    },103  }),104};
```

8

### Customize email template

Before users can confirm their email, update the Supabase email template to send the token hash to your callback URL.

In your [Supabase project dashboard](/dashboard/project/_/auth/templates):

*   Go to **Auth** > **Email Templates**
*   Select the **Confirm signup** template
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/callback?token_hash={{ .TokenHash }}&type=email`.
*   Change your [Site URL](/dashboard/project/_/auth/url-configuration) to `http://localhost:4321`

###### Email\\

```
1{{ .SiteURL }}/auth/callback?token_hash={{ .TokenHash }}&type=email
```

9

### Create an auth callback page

Create a new file at `src/pages/auth/callback.astro` to handle the email confirmation callback. Extract the token from the URL and verify it with Supabase:

###### src/pages/auth/callback.astro

```
1---2import { createClient } from "../../lib/supabase";3import type { EmailOtpType } from "@supabase/supabase-js";45const supabase = createClient({6  request: Astro.request,7  cookies: Astro.cookies,8});910const requestUrl = new URL(Astro.request.url);11const token_hash = requestUrl.searchParams.get('token_hash');12const type = requestUrl.searchParams.get('type') as EmailOtpType | null;1314if (token_hash && type) {15  const { error } = await supabase.auth.verifyOtp({16    token_hash,17    type,18  });1920  if (!error) {21    return Astro.redirect("/dashboard");22  }23}2425return Astro.redirect("/auth/signin");26---2728<html>29  <head>30    <title>Email Confirmation</title>31  </head>32  <body>33    <p>Confirming your email...</p>34  </body>35</html>
```

10

### Create a sign-up page

Create a new file at `src/pages/auth/signup.astro` with a sign-up form. Use a client-side event listener to handle form submission:

###### src/pages/auth/signup.astro

```
1---2import { createClient } from "../../lib/supabase";34const supabase = createClient({5  request: Astro.request,6  cookies: Astro.cookies,7});89const { data } = await supabase.auth.getUser();1011if (data?.user) {12  return Astro.redirect("/dashboard");13}14---1516<html>17  <head>18    <title>Sign Up</title>19  </head>20  <body>21    <h1>Sign Up</h1>2223    <div id="message"></div>2425    <form id="signup-form">26      <div>27        <label for="email">Email</label>28        <input29          id="email"30          type="email"31          name="email"32          placeholder="your@email.com"33          required34        />35      </div>36      <div>37        <label for="password">Password</label>38        <input39          id="password"40          type="password"41          name="password"42          placeholder="At least 6 characters"43          required44        />45      </div>46      <button type="submit" id="signup-btn">Sign Up</button>47    </form>48    <p>49      Already have an account? <a href="/auth/signin">Sign in</a>50    </p>51  </body>52</html>5354<script>55  import { actions } from "astro:actions";5657  const form = document.querySelector("#signup-form") as HTMLFormElement;58  const btn = document.getElementById("signup-btn") as HTMLButtonElement;59  const messageEl = document.getElementById("message") as HTMLDivElement;6061  form?.addEventListener("submit", async (e) => {62    e.preventDefault();63    btn.disabled = true;64    btn.textContent = "Signing up...";65    messageEl.textContent = "";6667    try {68      const formData = new FormData(form);69      const result = await actions.signUp(formData);7071      if (!result.data?.success) {72        btn.disabled = false;73        btn.textContent = "Sign Up";74        messageEl.textContent = result.data?.message || "Sign up failed";75        messageEl.style.color = "red";76        return;77      }7879      messageEl.textContent = result.data.message;80      messageEl.style.color = "green";81      btn.textContent = "Sign Up";82    } catch (error) {83      btn.disabled = false;84      btn.textContent = "Sign Up";85      messageEl.textContent = "An error occurred. Please try again.";86      messageEl.style.color = "red";87      console.error(error);88    }89  });90</script>
```

11

### Create a sign-in page

Create a new file at `src/pages/auth/signin.astro` with a sign-in form. Use a client-side event listener to handle form submission:

###### src/pages/auth/signin.astro

```
1---2import { createClient } from "../../lib/supabase";34const supabase = createClient({5  request: Astro.request,6  cookies: Astro.cookies,7});89const { data } = await supabase.auth.getUser();1011if (data?.user) {12  return Astro.redirect("/dashboard");13}14---1516<html>17  <head>18    <title>Sign In</title>19  </head>20  <body>21    <h1>Sign In</h1>2223    <div id="message"></div>2425    <form id="signin-form">26      <div>27        <label for="email">Email</label>28        <input29          id="email"30          type="email"31          name="email"32          placeholder="your@email.com"33          required34        />35      </div>36      <div>37        <label for="password">Password</label>38        <input39          id="password"40          type="password"41          name="password"42          placeholder="Your password"43          required44        />45      </div>46      <button type="submit" id="signin-btn">Sign In</button>47    </form>48    <p>49      Don't have an account? <a href="/auth/signup">Sign up</a>50    </p>51  </body>52</html>5354<script>55  import { actions } from "astro:actions";5657  const form = document.querySelector("#signin-form") as HTMLFormElement;58  const btn = document.getElementById("signin-btn") as HTMLButtonElement;59  const messageEl = document.getElementById("message") as HTMLDivElement;6061  form?.addEventListener("submit", async (e) => {62    e.preventDefault();63    btn.disabled = true;64    btn.textContent = "Signing in...";65    messageEl.textContent = "";6667    try {68      const formData = new FormData(form);69      const result = await actions.signIn(formData);7071      if (!result.data?.success) {72        btn.disabled = false;73        btn.textContent = "Sign In";74        messageEl.textContent = result.data?.message || "Sign in failed";75        messageEl.style.color = "red";76        return;77      }7879      // Redirect to dashboard on successful sign in80      window.location.href = "/dashboard";81    } catch (error) {82      btn.disabled = false;83      btn.textContent = "Sign In";84      messageEl.textContent = "An error occurred. Please try again.";85      messageEl.style.color = "red";86      console.error(error);87    }88  });89</script>
```

12

### Create a dashboard page

Create a new file at `src/pages/dashboard.astro` to display the authenticated user's information. Use a client-side event listener for the sign-out button:

###### src/pages/dashboard.astro

```
1---2import { createClient } from "../lib/supabase";34const supabase = createClient({5  request: Astro.request,6  cookies: Astro.cookies,7});89const { data } = await supabase.auth.getUser();10const user = data?.user;1112if (!user) {13  return Astro.redirect("/auth/signin");14}15---1617<html>18  <head>19    <title>Dashboard</title>20  </head>21  <body>22    <h1>Welcome!</h1>23    <p>Email: {user.email}</p>24    <p>User ID: {user.id}</p>2526    <button id="signout-btn">Sign Out</button>27  </body>28</html>2930<script>31  import { actions } from "astro:actions";3233  const btn = document.getElementById("signout-btn") as HTMLButtonElement;3435  btn?.addEventListener("click", async (e) => {36    e.preventDefault();37    btn.disabled = true;38    btn.textContent = "Signing out...";3940    try {41      const result = await actions.signOut();4243      if (!result.data?.success) {44        btn.disabled = false;45        btn.textContent = "Sign Out";46        alert("Failed to sign out");47        return;48      }4950      // Redirect to signin page51      window.location.href = "/auth/signin";52    } catch (error) {53      btn.disabled = false;54      btn.textContent = "Sign Out";55      console.error(error);56    }57  });58</script>
```

13

### Start the app

Start the development server, then navigate to [http://localhost:4321/auth/signup](http://localhost:4321/auth/signup) to test the authentication.

###### Terminal

```
1npm run dev
```

## Learn more[#](#learn-more)

*   [Supabase Auth docs](/docs/guides/auth#authentication) for more Supabase authentication methods

