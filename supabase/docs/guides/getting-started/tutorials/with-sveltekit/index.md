---
title: "Build a User Management App with SvelteKit"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:24.218Z"
content_hash: "bce79d07c177a86eba948d12a26b0f33ae2a827a4c1a4e014d74f07f737953cd"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","SvelteKit","SvelteKit"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","SvelteKit","SvelteKit"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-svelte/index.md", "title": "Build a User Management App with Svelte"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-swift/index.md", "title": "Build a User Management App with Swift and SwiftUI"}
---

# 

Build a User Management App with SvelteKit

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/sveltekit-user-management).

## Project setup[#](#project-setup)

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.

### Create a project[#](#create-a-project)

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.

### Set up the database schema[#](#set-up-the-database-schema)

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
3.  Click **Run**.

You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

```
1supabase link --project-ref <project-id>2# You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>3supabase db pull
```

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=sveltekit).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=sveltekit), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the Svelte app from scratch.

### Initialize a Svelte app[#](#initialize-a-svelte-app)

Use the [SvelteKit Skeleton Project](https://svelte.dev/docs/kit) to initialize an app called `supabase-sveltekit` (for this tutorial, select "SvelteKit minimal" and use TypeScript):

```
1npx sv create supabase-sveltekit2cd supabase-sveltekit3npm install
```

Then install the Supabase client library: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

And finally, save the environment variables in a `.env` file. All you need are the `PUBLIC_SUPABASE_URL` and the key that you copied [earlier](#get-api-details).

```
1PUBLIC_SUPABASE_URL="YOUR_SUPABASE_URL"2PUBLIC_SUPABASE_PUBLISHABLE_KEY="YOUR_SUPABASE_PUBLISHABLE_KEY"
```

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `src/styles.css` to make the app look nice. You can find the full contents of this file [in the example repository](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/sveltekit-user-management/src/styles.css).

### Creating a Supabase client for SSR[#](#creating-a-supabase-client-for-ssr)

The `ssr` package configures Supabase to use Cookies, which are required for server-side languages and frameworks.

Install the SSR package:

```
1npm install @supabase/ssr
```

Creating a Supabase client with the `ssr` package automatically configures it to use Cookies. This means the user's session is available throughout the entire SvelteKit stack - page, layout, server, and hooks.

Add the code below to a `src/hooks.server.ts` file to initialize the client on the server:

```
1// src/hooks.server.ts2import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public'3import { createServerClient } from '@supabase/ssr'4import type { Handle } from '@sveltejs/kit'56export const handle: Handle = async ({ event, resolve }) => {7  event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {8    cookies: {9      getAll: () => event.cookies.getAll(),10      /**11       * Note: You have to add the `path` variable to the12       * set and remove method due to sveltekit's cookie API13       * requiring this to be set, setting the path to `/`14       * will replicate previous/standard behaviour (https://kit.svelte.dev/docs/types#public-types-cookies)15       */16      setAll: (cookiesToSet, headers) => {17        cookiesToSet.forEach(({ name, value, options }) => {18          event.cookies.set(name, value, { ...options, path: '/' })19        })20        if (Object.keys(headers).length > 0) {21          event.setHeaders(headers)22        }23      },24    },25  })2627  return resolve(event, {28    filterSerializedResponseHeaders(name: string) {29      return name === 'content-range' || name === 'x-supabase-api-version'30    },31  })32}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/hooks.server.ts)

Note that `auth.getSession` reads the auth token and the unencoded session data from the local storage medium. It _doesn't_ send a request back to the Supabase Auth server unless the local session is expired.

You should **never** trust the unencoded session data if you're writing server code, since it could be tampered with by the sender. If you need verified, trustworthy user data, call `auth.getUser` instead, which always makes a request to the Auth server to fetch trusted data.

As this tutorial uses TypeScript the compiler complains about `event.locals.supabase` and `event.locals.safeGetSession`, you can fix this by updating the `src/app.d.ts` with the content below:

```
1import type { SupabaseClient } from '@supabase/supabase-js'2// See https://kit.svelte.dev/docs/types#app3// for information about these interfaces4declare global {5  namespace App {6    // interface Error {}7    interface Locals {8      supabase: SupabaseClient9    }10    // interface PageState {}11    // interface Platform {}12  }13}1415export {}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/app.d.ts)

Create a new `src/routes/+layout.server.ts` file to handle the session on the server-side.

```
1// src/routes/+layout.server.ts2import type { LayoutServerLoad } from './$types'34export const load: LayoutServerLoad = async ({ cookies }) => {5  return {6    cookies: cookies.getAll(),7  }8}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/+layout.server.ts)

Start the dev server (`npm run dev`) to generate the `./$types` files we are referencing in our project.

Create a new `src/routes/+layout.ts` file to handle the session and the `supabase` object on the client-side.

```
1// src/routes/+layout.ts2import { PUBLIC_SUPABASE_PUBLISHABLE_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'3import type { LayoutLoad } from './$types'4import { createBrowserClient, createServerClient, isBrowser } from '@supabase/ssr'56export const load: LayoutLoad = async ({ fetch, data, depends }) => {7  depends('supabase:auth')89  const supabase = isBrowser()10    ? createBrowserClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {11        global: {12          fetch,13        },14      })15    : createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {16        global: {17          fetch,18        },19        cookies: {20          getAll() {21            return data.cookies22          },23        },24      })2526  /**27   * `getClaims` validates the JWT signature locally (for asymmetric keys) once28   * the relevant signing keys are available or cached, and returns the decoded29   * claims. While an initial or periodic network request may be required to30   * fetch or refresh keys, this is both faster and safer than `getSession`,31   * which does not validate the JWT.32   */33  const { data: claimsData, error } = await supabase.auth.getClaims()34  const claims = error ? null : claimsData?.claims3536  return { supabase, claims }37}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/+layout.ts)

Create `src/routes/+layout.svelte`:

```
1<!-- src/routes/+layout.svelte -->2<script lang="ts">3	import '../styles.css'4	import { invalidate } from '$app/navigation'5	import { onMount } from 'svelte'67	let { data, children } = $props()8	let { supabase, claims } = $derived(data)910	onMount(() => {11		const { data } = supabase.auth.onAuthStateChange((event, _session) => {12			if (_session?.expires_at !== claims?.exp) {13				invalidate('supabase:auth')14			}15		})1617		return () => data.subscription.unsubscribe()18	})19</script>2021<svelte:head>22	<title>User Management</title>23</svelte:head>2425<div class="container" style="padding: 50px 0 100px 0">26	{@render children()}27</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/+layout.svelte)

## Set up a login page[#](#set-up-a-login-page)

Create a magic link login/signup page for your application by updating the `routes/+page.svelte` file:

```
1<!-- src/routes/+page.svelte -->2<script lang="ts">3	import { enhance } from '$app/forms'4	import type { ActionData, SubmitFunction } from './$types.js'56	interface Props {7		form: ActionData8	}9	let { form }: Props = $props()1011	let loading = $state(false)1213	const handleSubmit: SubmitFunction = () => {14		loading = true15		return async ({ update }) => {16			update()17			loading = false18		}19	}20</script>2122<svelte:head>23	<title>User Management</title>24</svelte:head>2526<form class="row flex flex-center" method="POST" use:enhance={handleSubmit}>27	<div class="col-6 form-widget">28		<h1 class="header">Supabase + SvelteKit</h1>29		<p class="description">Sign in via magic link with your email below</p>30		{#if form?.message !== undefined}31		<div class="success {form?.success ? '' : 'fail'}">32			{form?.message}33		</div>34		{/if}35		<div>36			<label for="email">Email address</label>37			<input 38				id="email" 39				name="email" 40				class="inputField" 41				type="email" 42				placeholder="Your email" 43				value={form?.email ?? ''} 44			/>45		</div>46		{#if form?.errors?.email}47		<span class="flex items-center text-sm error">48			{form?.errors?.email}49		</span>50		{/if}51		<div>52			<button class="button primary block">53				{ loading ? 'Loading' : 'Send magic link' }54			</button>55		</div>56	</div>57</form>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/+page.svelte)

Create a `src/routes/+page.server.ts` file that handles the magic link form when submitted.

```
1// src/routes/+page.server.ts2import { fail, redirect } from '@sveltejs/kit'3import type { Actions, PageServerLoad } from './$types'45export const load: PageServerLoad = async ({ url, locals: { supabase } }) => {6  const { data, error } = await supabase.auth.getClaims()78  // if the user is already logged in return them to the account page9  if (!error && data?.claims) {10    redirect(303, '/account')11  }1213  return { url: url.origin }14}1516export const actions: Actions = {17  default: async (event) => {18    const {19      url,20      request,21      locals: { supabase },22    } = event23    const formData = await request.formData()24    const email = formData.get('email') as string25    const validEmail = /^[\w-\.+]+@([\w-]+\.)+[\w-]{2,8}$/.test(email)2627    if (!validEmail) {28      return fail(400, { errors: { email: 'Please enter a valid email address' }, email })29    }3031    const { error } = await supabase.auth.signInWithOtp({ email })3233    if (error) {34      return fail(400, {35        success: false,36        email,37        message: `There was an issue, Please contact support.`,38      })39    }4041    return {42      success: true,43      message: 'Please check your email for a magic link to log into the website.',44    }45  },46}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/+page.server.ts)

### Email template[#](#email-template)

Change the email template to support a server-side authentication flow.

Before proceeding, change the email template to support sending a token hash:

*   Go to the [**Auth** > **Emails**](/dashboard/project/_/auth/templates) page in the project dashboard.
*   Select the **Confirm signup** template.
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
*   Repeat the previous step for **Magic link** template.

##### Did you know?

You can also customize emails sent out to new users, including the email's looks, content, and query parameters. Check out the [settings of your project](/dashboard/project/_/auth/templates).

### Confirmation endpoint[#](#confirmation-endpoint)

As this is a server-side rendering (SSR) environment, you need to create a server endpoint responsible for exchanging the `token_hash` for a session.

The following code snippet performs the following steps:

*   Retrieves the `token_hash` sent back from the Supabase Auth server using the `token_hash` query parameter.
*   Exchanges this `token_hash` for a session, which you store in storage (in this case, cookies).
*   Finally, redirect the user to the `account` page or the `error` page.

```
1// src/routes/auth/confirm/+server.js2import type { EmailOtpType } from '@supabase/supabase-js'3import { redirect } from '@sveltejs/kit'45import type { RequestHandler } from './$types'67export const GET: RequestHandler = async ({ url, locals: { supabase } }) => {8  const token_hash = url.searchParams.get('token_hash')9  const type = url.searchParams.get('type') as EmailOtpType | null10  const next = url.searchParams.get('next') ?? '/account'1112  /**13   * Clean up the redirect URL by deleting the Auth flow parameters.14   *15   * `next` is preserved for now, because it's needed in the error case.16   */17  const redirectTo = new URL(url)18  redirectTo.pathname = next19  redirectTo.searchParams.delete('token_hash')20  redirectTo.searchParams.delete('type')2122  if (token_hash && type) {23    const { error } = await supabase.auth.verifyOtp({ type, token_hash })24    if (!error) {25      redirectTo.searchParams.delete('next')26      redirect(303, redirectTo)27    }28  }2930  redirectTo.pathname = '/auth/error'31  redirect(303, redirectTo)32}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/auth/confirm/+server.ts)

### Authentication error page[#](#authentication-error-page)

If there is an error with confirming the token, redirect the user to an error page.

```
1<p>Login error</p>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/auth/error/+page.svelte)

### Account page[#](#account-page)

After a user signs in, they need to be able to edit their profile details page. Create a new `src/routes/account/+page.svelte` file with the content below.

```
1<script lang="ts">2	import { enhance } from '$app/forms';3	import type { SubmitFunction } from '@sveltejs/kit';45	// ...67	let { data, form } = $props()8	let { claims, supabase, profile } = $derived(data)9	let profileForm: HTMLFormElement10	let loading = $state(false)11	let fullName: string = profile?.full_name ?? ''12	let username: string = profile?.username ?? ''13	let website: string = profile?.website ?? ''1415	// ...1617	const handleSubmit: SubmitFunction = () => {18		loading = true19		return async ({ update }) => {20			loading = false21			update()22		}23	}2425	const handleSignOut: SubmitFunction = () => {26		loading = true27		return async ({ update }) => {28			loading = false29			update()30		}31	}32</script>3334<div class="form-widget">35	<form36		class="form-widget"37		method="post"38		action="?/update"39		use:enhance={handleSubmit}40		bind:this={profileForm}4142        // ...4344        />45		<input type="hidden" name="avatarUrl" value={avatarUrl} />46		<div>47			<label for="email">Email</label>48			<input id="email" type="text" value={claims?.email ?? ''} disabled />49		</div>5051		<div>52			<label for="fullName">Full Name</label>53			<input id="fullName" name="fullName" type="text" value={form?.fullName ?? fullName} />54		</div>5556		<div>57			<label for="username">Username</label>58			<input id="username" name="username" type="text" value={form?.username ?? username} />59		</div>6061		<div>62			<label for="website">Website</label>63			<input id="website" name="website" type="url" value={form?.website ?? website} />64		</div>6566		<div>67			<input68				type="submit"69				class="button block primary"70				value={loading ? 'Loading...' : 'Update'}71				disabled={loading}72			/>73		</div>74	</form>7576	<form method="post" action="?/signout" use:enhance={handleSignOut}>77		<div>78			<button class="button block" disabled={loading}>Sign Out</button>79		</div>80	</form>81</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/account/+page.svelte)

Now, create the associated `src/routes/account/+page.server.ts` file that handles loading data from the server through the `load` function and handle all form actions through the `actions` object.

###### src/routes/account/+page.server.ts

```
1import { fail, redirect } from '@sveltejs/kit'2import type { Actions, PageServerLoad } from './$types'34export const load: PageServerLoad = async ({ locals: { supabase } }) => {5  const { data: claimsData, error } = await supabase.auth.getClaims()67  if (error || !claimsData?.claims) {8    redirect(303, '/')9  }1011  const { claims } = claimsData1213  const { data: profile } = await supabase14    .from('profiles')15    .select(`username, full_name, website, avatar_url`)16    .eq('id', claims.sub)17    .single()1819  return { claims, profile }20}2122export const actions: Actions = {23  update: async ({ request, locals: { supabase } }) => {24    const formData = await request.formData()25    const fullName = formData.get('fullName') as string26    const username = formData.get('username') as string27    const website = formData.get('website') as string28    const avatarUrl = formData.get('avatarUrl') as string2930    const { data: claimsData, error: claimsError } = await supabase.auth.getClaims()3132    if (claimsError || !claimsData?.claims) {33      return fail(401, { fullName, username, website, avatarUrl })34    }3536    const { error } = await supabase.from('profiles').upsert({37      id: claimsData.claims.sub,38      full_name: fullName,39      username,40      website,41      avatar_url: avatarUrl,42      updated_at: new Date(),43    })4445    if (error) {46      return fail(500, {47        fullName,48        username,49        website,50        avatarUrl,51      })52    }5354    return {55      fullName,56      username,57      website,58      avatarUrl,59    }60  },61  signout: async ({ locals: { supabase } }) => {62    await supabase.auth.signOut()63    redirect(303, '/')64  },65}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/account/+page.server.ts)

### Launch![#](#launch)

With all the pages in place, run this command in a terminal:

```
1npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase Svelte](/docs/img/supabase-svelte-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component called `Avatar.svelte` in the `src/routes/account` directory:

```
1<!-- src/routes/account/Avatar.svelte -->2<script lang="ts">3	import type { SupabaseClient } from '@supabase/supabase-js'45	interface Props {6		size?: number7		url?: string8		supabase: SupabaseClient9		onupload?: () => void10	}11	let { size = 10, url = $bindable(), supabase, onupload }: Props = $props()1213	let avatarUrl: string | null = $state(null)14	let uploading = $state(false)15	let files: FileList = $state()1617	const downloadImage = async (path: string) => {18		try {19			const { data, error } = await supabase.storage.from('avatars').download(path)2021			if (error) {22				throw error23			}2425			const url = URL.createObjectURL(data)26			avatarUrl = url27		} catch (error) {28			if (error instanceof Error) {29				console.log('Error downloading image: ', error.message)30			}31		}32	}3334	const uploadAvatar = async () => {35		try {36			uploading = true3738			if (!files || files.length === 0) {39				throw new Error('You must select an image to upload.')40			}4142			const file = files[0]43			const fileExt = file.name.split('.').pop()44			const filePath = `${Math.random()}.${fileExt}`4546			const { error } = await supabase.storage.from('avatars').upload(filePath, file)4748			if (error) {49				throw error50			}5152			url = filePath53			setTimeout(() => {54				onupload?.()55			}, 100)56		} catch (error) {57			if (error instanceof Error) {58				alert(error.message)59			}60		} finally {61			uploading = false62		}63	}6465	$effect(() => {66		if (url) downloadImage(url)67	})68</script>6970<div>71	{#if avatarUrl}72		<img73			src={avatarUrl}74			alt={avatarUrl ? 'Avatar' : 'No image'}75			class="avatar image"76			style="height: {size}em; width: {size}em;"77		/>78	{:else}79		<div class="avatar no-image" style="height: {size}em; width: {size}em;"></div>80	{/if}81	<input type="hidden" name="avatarUrl" value={url} />8283	<div style="width: {size}em;">84		<label class="button primary block" for="single">85			{uploading ? 'Uploading ...' : 'Upload'}86		</label>87		<input88			style="visibility: hidden; position:absolute;"89			type="file"90			id="single"91			accept="image/*"92			bind:files93			onchange={uploadAvatar}94			disabled={uploading}95		/>96	</div>97</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/account/Avatar.svelte)

### Add the new widget[#](#add-the-new-widget)

Add the widget to the Account page:

```
1<script lang="ts">23    // ...45    import Avatar from './Avatar.svelte'67// ...891011	// ...1213	>14        <Avatar15            {supabase}16            bind:url={avatarUrl}17            size={10}18            onupload={() => {19                profileForm.requestSubmit();20            }}2122		// ...2324		</div>2526		// ...
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/sveltekit-user-management/src/routes/account/+page.svelte)

At this stage you have a fully functional application!


