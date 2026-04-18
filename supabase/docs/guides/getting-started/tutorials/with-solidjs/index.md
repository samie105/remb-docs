---
title: "Build a User Management App with SolidJS"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-solidjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-solidjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:18.327Z"
content_hash: "38bb67f389b01a1cc52afd7eb06313b0acf7a316fcd043a0673df12d2815a40c"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","SolidJS","SolidJS"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","SolidJS","SolidJS"]
---
# 

Build a User Management App with SolidJS

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/solid-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=solidjs).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=solidjs), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the SolidJS app from scratch.

### Initialize a SolidJS app[#](#initialize-a-solidjs-app)

You can use [degit](https://github.com/Rich-Harris/degit) to initialize an app called `supabase-solid`:

```
1npx degit solidjs/templates/ts supabase-solid2cd supabase-solid
```

Then install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

And finally save the environment variables in a `.env` with the API URL and the key that you copied [earlier](#get-api-details).

```
1VITE_SUPABASE_URL=https://your-project-ref.supabase.co2VITE_SUPABASE_PUBLISHABLE_KEY=your-publishable-key
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/.env.example)

Now that you have the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's completely fine since you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

```
1import { createClient } from '@supabase/supabase-js'2import { Database } from './schema'34const supabaseUrl = import.meta.env.VITE_SUPABASE_URL5const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY67export const supabase = createClient(supabaseUrl, supabasePublishableKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/supabaseClient.tsx)

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `src/index.css` to make the app look better. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/solid-user-management/src/index.css).

### Set up a login component[#](#set-up-a-login-component)

Set up a SolidJS component to manage logins and sign ups using Magic Links, so users can sign in with their email without using passwords.

```
1import { Component, createSignal } from 'solid-js'2import { supabase } from './supabaseClient'34const Auth: Component = () => {5  const [loading, setLoading] = createSignal(false)6  const [email, setEmail] = createSignal('')78  const handleLogin = async (e: SubmitEvent) => {9    e.preventDefault()1011    try {12      setLoading(true)13      const { error } = await supabase.auth.signInWithOtp({ email: email() })14      if (error) throw error15      alert('Check your email for the login link!')16    } catch (error) {17      if (error instanceof Error) {18        alert(error.message)19      }20    } finally {21      setLoading(false)22    }23  }2425  return (26    <div class="row flex-center flex">27      <div class="col-6 form-widget" aria-live="polite">28        <h1 class="header">Supabase + SolidJS</h1>29        <p class="description">Sign in via magic link with your email below</p>30        <form class="form-widget" onSubmit={handleLogin}>31          <div>32            <label for="email">Email</label>33            <input34              id="email"35              class="inputField"36              type="email"37              placeholder="Your email"38              value={email()}39              onChange={(e) => setEmail(e.currentTarget.value)}40            />41          </div>42          <div>43            <button type="submit" class="button block" aria-live="polite">44              {loading() ? <span>Loading</span> : <span>Send magic link</span>}45            </button>46          </div>47        </form>48      </div>49    </div>50  )51}5253export default Auth
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/Auth.tsx)

### Account page[#](#account-page)

After a user is signed in allow them to edit their profile details and manage their account.

Create a new component for that called `Account.tsx`.

```
1import { Component, createEffect, createSignal } from 'solid-js'23// ...45import { supabase } from './supabaseClient'67interface Props {8  userId: string9  userEmail: string | null10}1112const Account: Component<Props> = ({ userId, userEmail }) => {13  const [loading, setLoading] = createSignal(true)14  const [username, setUsername] = createSignal<string | null>(null)15  const [website, setWebsite] = createSignal<string | null>(null)16  const [avatarUrl, setAvatarUrl] = createSignal<string | null>(null)1718  createEffect(() => {19    getProfile()20  })2122  const getProfile = async () => {23    try {24      setLoading(true)2526      let { data, error, status } = await supabase27        .from('profiles')28        .select(`username, website, avatar_url`)29        .eq('id', userId)30        .single()3132      if (error && status !== 406) {33        throw error34      }3536      if (data) {37        setUsername(data.username)38        setWebsite(data.website)39        setAvatarUrl(data.avatar_url)40      }41    } catch (error) {42      if (error instanceof Error) {43        alert(error.message)44      }45    } finally {46      setLoading(false)47    }48  }4950  const updateProfile = async (e: Event) => {51    e.preventDefault()5253    try {54      setLoading(true)5556      const updates = {57        id: userId,58        username: username(),59        website: website(),60        avatar_url: avatarUrl(),61        updated_at: new Date().toISOString(),62      }6364      let { error } = await supabase.from('profiles').upsert(updates)6566      if (error) {67        throw error68      }69    } catch (error) {70      if (error instanceof Error) {71        alert(error.message)72      }73    } finally {74      setLoading(false)75    }76  }7778  return (79    <div aria-live="polite">80      <form onSubmit={updateProfile} class="form-widget">8182        {/* ... */}8384        <div>Email: {userEmail}</div>85        <div>86          <label for="username">Name</label>87          <input88            id="username"89            type="text"90            value={username() || ''}91            onChange={(e) => setUsername(e.currentTarget.value)}92          />93        </div>94        <div>95          <label for="website">Website</label>96          <input97            id="website"98            type="text"99            value={website() || ''}100            onChange={(e) => setWebsite(e.currentTarget.value)}101          />102        </div>103        <div>104          <button type="submit" class="button primary block" disabled={loading()}>105            {loading() ? 'Saving ...' : 'Update profile'}106          </button>107        </div>108        <button type="button" class="button block" onClick={() => supabase.auth.signOut()}>109          Sign Out110        </button>111      </form>112    </div>113  )114}115116export default Account
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/Account.tsx)

### Launch![#](#launch)

Now that you have all the components in place, update `App.tsx`:

```
1import { Component, createEffect, createSignal } from 'solid-js'2import { supabase } from './supabaseClient'3import Account from './Account'4import Auth from './Auth'56const App: Component = () => {7  const [userId, setUserId] = createSignal<string | null>(null)8  const [userEmail, setUserEmail] = createSignal<string | null>(null)910  const syncClaims = async () => {11    const { data } = await supabase.auth.getClaims()12    setUserId((data?.claims.sub as string) ?? null)13    setUserEmail((data?.claims.email as string) ?? null)14  }1516  createEffect(() => {17    syncClaims()1819    supabase.auth.onAuthStateChange(() => {20      syncClaims()21    })22  })2324  return (25    <div class="container" style={{ padding: '50px 0 100px 0' }}>26      {!userId() ? <Auth /> : <Account userId={userId()!} userEmail={userEmail()} />}27    </div>28  )29}3031export default App
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/App.tsx)

Once that's done, run this in a terminal window:

```
1npm start
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase SolidJS](/docs/img/supabase-solidjs-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component:

```
1import { Component, createEffect, createSignal, JSX } from 'solid-js'2import { supabase } from './supabaseClient'34interface Props {5  size: number6  url: string | null7  onUpload: (event: Event, filePath: string) => void8}910const Avatar: Component<Props> = (props) => {11  const [avatarUrl, setAvatarUrl] = createSignal<string | null>(null)12  const [uploading, setUploading] = createSignal(false)1314  createEffect(() => {15    if (props.url) downloadImage(props.url)16  })1718  const downloadImage = async (path: string) => {19    try {20      const { data, error } = await supabase.storage.from('avatars').download(path)21      if (error) {22        throw error23      }24      const url = URL.createObjectURL(data)25      setAvatarUrl(url)26    } catch (error) {27      if (error instanceof Error) {28        console.log('Error downloading image: ', error.message)29      }30    }31  }3233  const uploadAvatar: JSX.EventHandler<HTMLInputElement, Event> = async (event) => {34    try {35      setUploading(true)3637      const target = event.currentTarget38      if (!target?.files || target.files.length === 0) {39        throw new Error('You must select an image to upload.')40      }4142      const file = target.files[0]43      const fileExt = file.name.split('.').pop()44      const fileName = `${Math.random()}.${fileExt}`45      const filePath = `${fileName}`4647      let { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)4849      if (uploadError) {50        throw uploadError51      }5253      props.onUpload(event, filePath)54    } catch (error) {55      if (error instanceof Error) {56        alert(error.message)57      }58    } finally {59      setUploading(false)60    }61  }6263  return (64    <div style={{ width: `${props.size}px` }} aria-live="polite">65      {avatarUrl() ? (66        <img67          src={avatarUrl()!}68          alt={avatarUrl() ? 'Avatar' : 'No image'}69          class="avatar image"70          style={{ height: `${props.size}px`, width: `${props.size}px` }}71        />72      ) : (73        <div74          class="avatar no-image"75          style={{ height: `${props.size}px`, width: `${props.size}px` }}76        />77      )}78      <div style={{ width: `${props.size}px` }}>79        <label class="button primary block" for="single">80          {uploading() ? 'Uploading ...' : 'Upload avatar'}81        </label>82        <span style="display:none">83          <input84            type="file"85            id="single"86            accept="image/*"87            onChange={uploadAvatar}88            disabled={uploading()}89          />90        </span>91      </div>92    </div>93  )94}9596export default Avatar
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/Avatar.tsx)

### Add the new widget[#](#add-the-new-widget)

And then add the widget to the Account page:

```
1import { Component, createEffect, createSignal } from 'solid-js'2import Avatar from './Avatar'3import { supabase } from './supabaseClient'45  // ...67  return (8    <div aria-live="polite">9      <form onSubmit={updateProfile} class="form-widget">10        <Avatar11          url={avatarUrl()}12          size={150}13          onUpload={(e: Event, url: string) => {14            setAvatarUrl(url)15            updateProfile(e)16          }}17        />18        <div>Email: {userEmail}</div>19        <div>2021  // ...
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/solid-user-management/src/Account.tsx)

At this stage you have a fully functional application!
