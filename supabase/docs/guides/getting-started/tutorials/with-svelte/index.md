---
title: "Build a User Management App with Svelte"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-svelte"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-svelte"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:20.051Z"
content_hash: "b2582527de0cfa300ca353de395a1ec6ae9cdcdb8038a856a2de8d69338d955d"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Svelte","Svelte"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Svelte","Svelte"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-solidjs/index.md", "title": "Build a User Management App with SolidJS"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-sveltekit/index.md", "title": "Build a User Management App with SvelteKit"}
---

# 

Build a User Management App with Svelte

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/svelte-user-management).

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

You can use the Vite Svelte TypeScript Template to initialize an app called `supabase-svelte`:

```
1npm create vite@latest supabase-svelte -- --template svelte-ts2cd supabase-svelte3npm install
```

Install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

Finally, save the environment variables in a `.env`. All you need are the API URL and the key that you copied [earlier](#get-api-details).

```
1VITE_SUPABASE_URL=YOUR_SUPABASE_URL2VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```

Now you have the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's fine since you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

###### src/supabaseClient.ts

```
1import { createClient } from '@supabase/supabase-js'23const supabaseUrl = import.meta.env.VITE_SUPABASE_URL4const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY56export const supabase = createClient(supabaseUrl, supabasePublishableKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/supabaseClient.ts)

### App styling (optional)[#](#app-styling-optional)

Optionally, update the CSS file `src/app.css` to make the app look nice. You can find the full contents of this file [on GitHub](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/svelte-user-management/src/app.css).

### Set up a login component[#](#set-up-a-login-component)

Set up a Svelte component to manage logins and sign ups. It uses Magic Links, so users can sign in with their email without using passwords.

###### src/lib/Auth.svelte

```
1<script lang="ts">2  import { supabase } from "../supabaseClient";34  let loading = $state(false);5  let email = $state("");67  const handleLogin = async () => {8    try {9      loading = true;10      const { error } = await supabase.auth.signInWithOtp({ email });11      if (error) throw error;12      alert("Check your email for login link!");13    } catch (error) {14      if (error instanceof Error) {15        alert(error.message);16      }17    } finally {18      loading = false;19    }20  };21</script>2223<div class="row flex-center flex">24  <div class="col-6 form-widget" aria-live="polite">25    <h1 class="header">Supabase + Svelte</h1>26    <p class="description">Sign in via magic link with your email below</p>27    <form class="form-widget" onsubmit={(e) => { e.preventDefault(); handleLogin(); }}>28      <div>29        <label for="email">Email</label>30        <input31          id="email"32          class="inputField"33          type="email"34          placeholder="Your email"35          bind:value={email}36        />37      </div>38      <div>39        <button40          type="submit"41          class="button block"42          aria-live="polite"43          disabled={loading}44        >45          <span>{loading ? "Loading" : "Send magic link"}</span>46        </button>47      </div>48    </form>49  </div>50</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/lib/Auth.svelte)

### Account page[#](#account-page)

After a user is signed in, allow them to edit their profile details and manage their account. Create a new component for that called `Account.svelte`.

```
1<script lang="ts">2  import { onMount } from "svelte";3  import type { AuthSession } from "@supabase/supabase-js";4  import { supabase } from "../supabaseClient";56  // ...78  interface Props {9    session: AuthSession;10  }1112  let { session }: Props = $props();1314  // ...1516  let username = $state<string | null>(null);17  let website = $state<string | null>(null);18  let avatarUrl = $state<string | null>(null);1920  onMount(() => {21    getProfile();22  });2324  const getProfile = async () => {25    try {26      loading = true;27      const { user } = session;2829      const { data, error, status } = await supabase30        .from("profiles")31        .select("username, website, avatar_url")32        .eq("id", user.id)33        .single();3435      if (error && status !== 406) throw error;3637// ...383940      if (data) {41        username = data.username;42        website = data.website;43        avatarUrl = data.avatar_url;44      }45    } catch (error) {46      if (error instanceof Error) {47        alert(error.message);48      }49    } finally {50      loading = false;51    }52  };5354  const updateProfile = async () => {55    try {56      loading = true;57      const { user } = session;585960        // ...6162        id: user.id,63        username,64        website,65        avatar_url: avatarUrl,66        updated_at: new Date().toISOString(),67      };6869      const { error } = await supabase.from("profiles").upsert(updates);7071      if (error) {72        throw error;73      }74    } catch (error) {75      if (error instanceof Error) {76        alert(error.message);77      }78    } finally {79      loading = false;80    }8182// ...8384</script>8586<form onsubmit={(e) => { e.preventDefault(); updateProfile(); }} class="form-widget">87  <div>Email: {session.user.email}</div>88  <div>89    <Avatar bind:url={avatarUrl} size={150} onupload={updateProfile} />90    <label for="username">Name</label>91    <input id="username" type="text" bind:value={username} />92  </div>93  <div>94    <label for="website">Website</label>95    <input id="website" type="text" bind:value={website} />96  </div>97  <div>98    <button type="submit" class="button primary block" disabled={loading}>99      {loading ? "Saving ..." : "Update profile"}100    </button>101  </div>102  <button103    type="button"104    class="button block"105    onclick={() => supabase.auth.signOut()}106  >107    Sign Out108  </button>109</form>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/lib/Account.svelte)

### Launch![#](#launch)

Now that you have all the components in place, update `App.svelte`:

###### src/App.svelte

```
1<script lang="ts">2  import { onMount } from 'svelte'3  import { supabase } from './supabaseClient'4  import type { AuthSession } from '@supabase/supabase-js'5  import Account from './lib/Account.svelte'6  import Auth from './lib/Auth.svelte'78  let session = $state<AuthSession | null>(null)910  onMount(() => {11    supabase.auth.getSession().then(({ data }) => {12      session = data.session13    })1415    supabase.auth.onAuthStateChange((_event, _session) => {16      session = _session17    })18  })19</script>2021<div class="container" style="padding: 50px 0 100px 0">22  {#if !session}23  <Auth />24  {:else}25  <Account {session} />26  {/if}27</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/App.svelte)

Once that's done, run this in a terminal window:

```
1npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

Svelte uses Vite and the default port is `5173`, Supabase uses `port 3000`. To change the redirection port for Supabase go to: **Authentication > URL Configuration** and change the **Site URL** to `http://localhost:5173/`

![Supabase Svelte](/docs/img/supabase-svelte-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component:

###### src/lib/Avatar.svelte

```
1<script lang="ts">2  import { supabase } from "../supabaseClient";34  interface Props {5    size: number;6    url?: string | null;7    onupload?: () => void;8  }910  let { size, url = $bindable(null), onupload }: Props = $props();1112  let avatarUrl = $state<string | null>(null);13  let uploading = $state(false);14  let files = $state<FileList>();1516  const downloadImage = async (path: string) => {17    try {18      const { data, error } = await supabase.storage19        .from("avatars")20        .download(path);2122      if (error) {23        throw error;24      }2526      const url = URL.createObjectURL(data);27      avatarUrl = url;28    } catch (error) {29      if (error instanceof Error) {30        console.log("Error downloading image: ", error.message);31      }32    }33  };3435  const uploadAvatar = async () => {36    try {37      uploading = true;3839      if (!files || files.length === 0) {40        throw new Error("You must select an image to upload.");41      }4243      const file = files[0];44      const fileExt = file.name.split(".").pop();45      const filePath = `${Math.random()}.${fileExt}`;4647      const { error } = await supabase.storage48        .from("avatars")49        .upload(filePath, file);5051      if (error) {52        throw error;53      }5455      url = filePath;56      onupload?.();57    } catch (error) {58      if (error instanceof Error) {59        alert(error.message);60      }61    } finally {62      uploading = false;63    }64  };6566  $effect(() => {67    if (url) downloadImage(url);68  });69</script>7071<div style="width: {size}px" aria-live="polite">72  {#if avatarUrl}73    <img74      src={avatarUrl}75      alt={avatarUrl ? "Avatar" : "No image"}76      class="avatar image"77      style="height: {size}px, width: {size}px"78    />79  {:else}80    <div class="avatar no-image" style="height: {size}px, width: {size}px"></div>81  {/if}82  <div style="width: {size}px">83    <label class="button primary block" for="single">84      {uploading ? "Uploading ..." : "Upload avatar"}85    </label>86    <span style="display:none">87      <input88        type="file"89        id="single"90        accept="image/*"91        bind:files92        onchange={uploadAvatar}93        disabled={uploading}94      />95    </span>96  </div>97</div>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/lib/Avatar.svelte)

### Add the new widget[#](#add-the-new-widget)

And then you can add the widget to the Account page:

```
1<script lang="ts">23  // ...45  import Avatar from "./Avatar.svelte";67    // ...89    } finally {10      loading = false;11    }1213  // ...1415  };1617  // ...1819  </div>20  <button21    type="button"22    class="button block"23    onclick={() => supabase.auth.signOut()}24  >25    Sign Out26  </button>27</form>
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/svelte-user-management/src/lib/Account.svelte)

At this stage you have a fully functional application!

