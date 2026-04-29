---
title: "Build a User Management App with React"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-react"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-react"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:10.214Z"
content_hash: "a07552bb66108245ddcfe3f7144c22baeb2cea3768d45bf34caa77648ae5de7f"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","React","React"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","React","React"]
nav_prev: {"path": "../with-nuxt-3/index.md", "title": "Build a User Management App with Nuxt 3"}
nav_next: {"path": "../with-redwoodjs/index.md", "title": "Build a User Management App with RedwoodJS"}
---

# 

Build a User Management App with React

* * *

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/react-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=react).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=react), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the React app from scratch.

### Initialize a React app[#](#initialize-a-react-app)

Use [Vite](https://vitejs.dev/guide/) to initialize an app called `supabase-react`:

```
1npm create vite@latest supabase-react -- --template react2cd supabase-react
```

Install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js).

```
1npm install @supabase/supabase-js
```

And finally, save the environment variables in a `.env.local` file. Use the Project URL and the key that you copied [earlier](#get-api-details).

###### .env

```
1VITE_SUPABASE_URL=2VITE_SUPABASE_PUBLISHABLE_KEY=
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/.env.example)

With the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's fine as you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

Create and edit `src/supabaseClient.js`:

###### src/supabaseClient.js

```
1/**2 * lib/supabaseClient.js3 * Helper to initialize the Supabase client.4 */56import { createClient } from '@supabase/supabase-js'78const supabaseUrl = import.meta.env.VITE_SUPABASE_URL9const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY1011export const supabase = createClient(supabaseUrl, supabasePublishableKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/src/supabaseClient.js)

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `src/index.css` to make the app look nice. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/react-user-management/src/index.css).

### Set up a login component[#](#set-up-a-login-component)

Create a React component to manage logins and sign-ups. It uses Magic Links, so users can sign in with their email without using passwords.

Create and edit `src/Auth.jsx`:

###### src/Auth.jsx

```
1import { useState } from 'react'2import { supabase } from './supabaseClient'34export default function Auth() {5  const [loading, setLoading] = useState(false)6  const [email, setEmail] = useState('')78  const handleLogin = async (event) => {9    event.preventDefault()1011    setLoading(true)12    const { error } = await supabase.auth.signInWithOtp({ email })1314    if (error) {15      alert(error.error_description || error.message)16    } else {17      alert('Check your email for the login link!')18    }19    setLoading(false)20  }2122  return (23    <div className="row flex flex-center">24      <div className="col-6 form-widget">25        <h1 className="header">Supabase + React</h1>26        <p className="description">Sign in via magic link with your email below</p>27        <form className="form-widget" onSubmit={handleLogin}>28          <div>29            <input30              className="inputField"31              type="email"32              placeholder="Your email"33              value={email}34              required={true}35              onChange={(e) => setEmail(e.target.value)}36            />37          </div>38          <div>39            <button className={'button block'} disabled={loading}>40              {loading ? <span>Loading</span> : <span>Send magic link</span>}41            </button>42          </div>43        </form>44      </div>45    </div>46  )47}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/src/Auth.jsx)

### Account page[#](#account-page)

Users also need a way to edit their profile details and manage their accounts after signing in.

### Create an upload widget[#](#create-an-upload-widget)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component:

Create and edit `src/Avatar.jsx`:

###### src/Avatar.jsx

```
1import { useEffect, useState } from 'react'2import { supabase } from './supabaseClient'34export default function Avatar({ url, size, onUpload }) {5  const [avatarUrl, setAvatarUrl] = useState(null)6  const [uploading, setUploading] = useState(false)78  useEffect(() => {9    if (url) downloadImage(url)10  }, [url])1112  async function downloadImage(path) {13    try {14      const { data, error } = await supabase.storage.from('avatars').download(path)15      if (error) {16        throw error17      }18      const url = URL.createObjectURL(data)19      setAvatarUrl(url)20    } catch (error) {21      console.log('Error downloading image: ', error.message)22    }23  }2425  async function uploadAvatar(event) {26    try {27      setUploading(true)2829      if (!event.target.files || event.target.files.length === 0) {30        throw new Error('You must select an image to upload.')31      }3233      const file = event.target.files[0]34      const fileExt = file.name.split('.').pop()35      const fileName = `${Math.random()}.${fileExt}`36      const filePath = `${fileName}`3738      let { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)3940      if (uploadError) {41        throw uploadError42      }4344      onUpload(event, filePath)45    } catch (error) {46      alert(error.message)47    } finally {48      setUploading(false)49    }50  }5152  return (53    <div>54      {avatarUrl ? (55        <img56          src={avatarUrl}57          alt="Avatar"58          className="avatar image"59          style={{ height: size, width: size }}60        />61      ) : (62        <div className="avatar no-image" style={{ height: size, width: size }} />63      )}64      <div style={{ width: size }}>65        <label className="button primary block" htmlFor="single">66          {uploading ? 'Uploading ...' : 'Upload'}67        </label>68        <input69          style={{70            visibility: 'hidden',71            position: 'absolute',72          }}73          type="file"74          id="single"75          accept="image/*"76          onChange={uploadAvatar}77          disabled={uploading}78        />79      </div>80    </div>81  )82}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/src/Avatar.jsx)

After a user is signed in, allow them to edit their profile details and manage their account.

Create a new component for that called `src/Account.jsx` and also add the `Avatar` component created earlier.

###### src/Account.jsx

```
1import { useState, useEffect } from 'react'2import { supabase } from './supabaseClient'3import Avatar from './Avatar'45export default function Account({ user }) {6  const [loading, setLoading] = useState(true)7  const [username, setUsername] = useState(null)8  const [website, setWebsite] = useState(null)9  const [avatar_url, setAvatarUrl] = useState(null)1011  useEffect(() => {12    let ignore = false13    async function getProfile() {14      setLoading(true)1516      const { data, error } = await supabase17        .from('profiles')18        .select(`username, website, avatar_url`)19        .eq('id', user.id)20        .single()2122      if (!ignore) {23        if (error) {24          console.warn(error)25        } else if (data) {26          setUsername(data.username)27          setWebsite(data.website)28          setAvatarUrl(data.avatar_url)29        }30      }3132      setLoading(false)33    }3435    getProfile()3637    return () => {38      ignore = true39    }40  }, [user])4142  async function updateProfile(event, avatarUrl) {43    event.preventDefault()4445    setLoading(true)4647    const updates = {48      id: user.id,49      username,50      website,51      avatar_url: avatarUrl,52      updated_at: new Date(),53    }5455    const { error } = await supabase.from('profiles').upsert(updates)5657    if (error) {58      alert(error.message)59    } else {60      setAvatarUrl(avatarUrl)61    }62    setLoading(false)63  }6465  return (66    <form onSubmit={updateProfile} className="form-widget">67      <Avatar68        url={avatar_url}69        size={150}70        onUpload={(event, url) => {71          updateProfile(event, url)72        }}73      />74      <div>75        <label htmlFor="email">Email</label>76        <input id="email" type="text" value={user.email} disabled />77      </div>78      <div>79        <label htmlFor="username">Name</label>80        <input81          id="username"82          type="text"83          required84          value={username || ''}85          onChange={(e) => setUsername(e.target.value)}86        />87      </div>88      <div>89        <label htmlFor="website">Website</label>90        <input91          id="website"92          type="url"93          value={website || ''}94          onChange={(e) => setWebsite(e.target.value)}95        />96      </div>9798      <div>99        <button className="button block primary" type="submit" disabled={loading}>100          {loading ? 'Loading ...' : 'Update'}101        </button>102      </div>103104      <div>105        <button className="button block" type="button" onClick={() => supabase.auth.signOut()}>106          Sign Out107        </button>108      </div>109    </form>110  )111}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/src/Account.jsx)

### Launch![#](#launch)

Now that you have all the components in place, update `src/App.jsx`, which fetches the current user via the [`getUser`](/docs/reference/javascript/auth-getuser) method if there is an existing session. This method performs a network request to the Supabase Auth server.

###### src/App.jsx

```
1import { useState, useEffect } from 'react'2import './App.css'3import { supabase } from './supabaseClient'4import Auth from './Auth'5import Account from './Account'67function App() {8  const [user, setUser] = useState(null)910  useEffect(() => {11    supabase.auth.getUser().then(({ data: { user } }) => {12      setUser(user)13    })1415    supabase.auth.onAuthStateChange(async () => {16      const {17        data: { user },18      } = await supabase.auth.getUser()19      setUser(user)20    })21  }, [])2223  return (24    <div className="container" style={{ padding: '50px 0 100px 0' }}>25      {!user ? <Auth /> : <Account key={user.id} user={user} />}26    </div>27  )28}2930export default App
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/react-user-management/src/App.jsx)

Once that's done, run this in a terminal window:

```
1npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase React](/docs/img/supabase-react-demo.png)

At this stage you have a fully functional application!
