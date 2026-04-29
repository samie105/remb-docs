---
title: "Build a User Management App with RedwoodJS"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-redwoodjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-redwoodjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:12.666Z"
content_hash: "c1ac48bf9f298f1239928a5012593e36c6f5a40d57131c2945a8a62fb2c8a958"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","RedwoodJS","RedwoodJS"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","RedwoodJS","RedwoodJS"]
nav_prev: {"path": "../with-react/index.md", "title": "Build a User Management App with React"}
nav_next: {"path": "../with-refine/index.md", "title": "Build a User Management App with Refine"}
---

# 

Build a User Management App with RedwoodJS

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/redwoodjs/redwoodjs-supabase-quickstart).

## About RedwoodJS[#](#about-redwoodjs)

A Redwood application is split into two parts: a frontend and a backend. This is represented as two node projects within a single monorepo.

The frontend project is called **`web`** and the backend project is called **`api`**. For clarity, we will refer to these in prose as **"sides,"** that is, the `web side` and the `api side`. They are separate projects because code on the `web side` will end up running in the user's browser while code on the `api side` will run on a server somewhere.

Important: When this guide refers to "API," that means the Supabase API and when it refers to `api side`, that means the RedwoodJS `api side`.

The **`api side`** is an implementation of a GraphQL API. The business logic is organized into "services" that represent their own internal API and can be called both from external GraphQL requests and other internal services.

The **`web side`** is built with React. Redwood's router makes it simple to map URL paths to React "Page" components (and automatically code-split your app on each route). Pages may contain a "Layout" component to wrap content. They also contain "Cells" and regular React components. Cells allow you to declaratively manage the lifecycle of a component that fetches and displays data.

For the sake of consistency with the other framework tutorials, we'll build this app a little differently than normal. We _**won't use**_ Prisma to connect to the Supabase Postgres database or [Prisma migrations](https://redwoodjs.com/docs/cli-commands#prisma-migrate) as one typically might in a Redwood app. Instead, we'll rely on the Supabase client to do some of the work on the **`web`** side and use the client again on the **`api`** side to do data fetching as well.

That means you will want to refrain from running any `yarn rw prisma migrate` commands and also double check your build commands on deployment to ensure Prisma won't reset your database. Prisma currently doesn't support cross-schema foreign keys, so introspecting the schema fails due to how your Supabase `public` schema references the `auth.users`.

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Let's start building the RedwoodJS app from scratch.

RedwoodJS requires Node.js `>= 14.x <= 16.x` and Yarn `>= 1.15`.

Make sure you have installed yarn since RedwoodJS relies on it to [manage its packages in workspaces](https://classic.yarnpkg.com/lang/en/docs/workspaces/) for its `web` and `api` "sides."

### Initialize a RedwoodJS app[#](#initialize-a-redwoodjs-app)

We can use [Create Redwood App](https://redwoodjs.com/docs/quick-start) command to initialize an app called `supabase-redwoodjs`:

```
1yarn create redwood-app supabase-redwoodjs2cd supabase-redwoodjs
```

While the app is installing, you should see:

```
1✔ Creating Redwood app2  ✔ Checking node and yarn compatibility3  ✔ Creating directory 'supabase-redwoodjs'4✔ Installing packages5  ✔ Running 'yarn install'... (This could take a while)6✔ Convert TypeScript files to JavaScript7✔ Generating types89Thanks for trying out Redwood!
```

Then let's install the only additional dependency [supabase-js](https://github.com/supabase/supabase-js) by running the `setup auth` command:

```
1yarn redwood setup auth supabase
```

When prompted:

> Overwrite existing /api/src/lib/auth.\[jt\]s?

Say, **yes** and it will setup the Supabase client in your app and also provide hooks used with Supabase authentication.

```
1✔ Generating auth lib...2  ✔ Successfully wrote file `./api/src/lib/auth.js`3  ✔ Adding auth config to web...4  ✔ Adding auth config to GraphQL API...5  ✔ Adding required web packages...6  ✔ Installing packages...7  ✔ One more thing...89  You will need to add your Supabase URL (SUPABASE_URL), public API KEY,10  and JWT SECRET (SUPABASE_KEY, and SUPABASE_JWT_SECRET) to your .env file.
```

Next, we want to save the environment variables in a `.env`. We need the `API URL` as well as the key and `jwt_secret` that you copied [earlier](#get-api-details).

```
1SUPABASE_URL=YOUR_SUPABASE_URL2SUPABASE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY3SUPABASE_JWT_SECRET=YOUR_SUPABASE_JWT_SECRET
```

And finally, you will also need to save **just** the `web side` environment variables to the `redwood.toml`.

```
1[web]2  title = "Supabase Redwood Tutorial"3  port = 89104  apiProxyPath = "/.redwood/functions"5  includeEnvironmentVariables = ["SUPABASE_URL", "SUPABASE_KEY"]6[api]7  port = 89118[browser]9  open = true
```

These variables will be exposed on the browser, and that's completely fine. They allow your web app to initialize the Supabase client with your publishable key since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

You'll see these being used to configure your Supabase client in `web/src/App.js`:

```
1// ... Redwood imports2import { AuthProvider } from '@redwoodjs/auth'3import { createClient } from '@supabase/supabase-js'45// ...67const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)89const App = () => (10  <FatalErrorBoundary page={FatalErrorPage}>11    <RedwoodProvider titleTemplate="%PageTitle | %AppTitle">12      <AuthProvider client={supabase} type="supabase">13        <RedwoodApolloProvider>14          <Routes />15        </RedwoodApolloProvider>16      </AuthProvider>17    </RedwoodProvider>18  </FatalErrorBoundary>19)2021export default App
```

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `web/src/index.css` to make the app look nice. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/react-user-management/src/index.css).

### Start RedwoodJS and your first page[#](#start-redwoodjs-and-your-first-page)

Let's test our setup at the moment by starting up the app:

```
1yarn rw dev
```

`rw` is an alias for `redwood`, as in `yarn rw` to run Redwood CLI commands.

You should see a "Welcome to RedwoodJS" page and a message about not having any pages yet.

So, let's create a "home" page:

```
1yarn rw generate page home /23✔ Generating page files...4  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.stories.js`5  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.test.js`6  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.js`7✔ Updating routes file...8✔ Generating types ...
```

The `/` is important here as it creates a root level route.

You can stop the `dev` server if you want; to see your changes, just be sure to run `yarn rw dev` again.

You should see the `Home` page route in `web/src/Routes.js`:

```
1import { Router, Route } from '@redwoodjs/router'23const Routes = () => {4  return (5    <Router>6      <Route path="/" page={HomePage} name="home" />7      <Route notfound page={NotFoundPage} />8    </Router>9  )10}1112export default Routes
```

### Set up a login component[#](#set-up-a-login-component)

Let's set up a Redwood component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

```
1yarn rw g component auth23  ✔ Generating component files...4    ✔ Successfully wrote file `./web/src/components/Auth/Auth.test.js`5    ✔ Successfully wrote file `./web/src/components/Auth/Auth.stories.js`6    ✔ Successfully wrote file `./web/src/components/Auth/Auth.js`
```

Now, update the `Auth.js` component to contain:

```
1import { useState } from 'react'2import { useAuth } from '@redwoodjs/auth'34const Auth = () => {5  const { logIn } = useAuth()6  const [loading, setLoading] = useState(false)7  const [email, setEmail] = useState('')89  const handleLogin = async (email) => {10    try {11      setLoading(true)12      const { error } = await logIn({ email })13      if (error) throw error14      alert('Check your email for the login link!')15    } catch (error) {16      alert(error.error_description || error.message)17    } finally {18      setLoading(false)19    }20  }2122  return (23    <div className="row flex-center flex">24      <div className="col-6 form-widget">25        <h1 className="header">Supabase + RedwoodJS</h1>26        <p className="description">Sign in via magic link with your email below</p>27        <div>28          <input29            className="inputField"30            type="email"31            placeholder="Your email"32            value={email}33            onChange={(e) => setEmail(e.target.value)}34          />35        </div>36        <div>37          <button38            onClick={(e) => {39              e.preventDefault()40              handleLogin(email)41            }}42            className={'button block'}43            disabled={loading}44          >45            {loading ? <span>Loading</span> : <span>Send magic link</span>}46          </button>47        </div>48      </div>49    </div>50  )51}5253export default Auth
```

### Set up an account component[#](#set-up-an-account-component)

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `Account.js`.

```
1yarn rw g component account23  ✔ Generating component files...4    ✔ Successfully wrote file `./web/src/components/Account/Account.test.js`5    ✔ Successfully wrote file `./web/src/components/Account/Account.stories.js`6    ✔ Successfully wrote file `./web/src/components/Account/Account.js`
```

And then update the file to contain:

```
1import { useState, useEffect } from 'react'2import { useAuth } from '@redwoodjs/auth'34const Account = () => {5  const { client: supabase, currentUser, logOut } = useAuth()6  const [loading, setLoading] = useState(true)7  const [username, setUsername] = useState(null)8  const [website, setWebsite] = useState(null)9  const [avatar_url, setAvatarUrl] = useState(null)1011  useEffect(() => {12    getProfile()13  }, [supabase.auth.session])1415  async function getProfile() {16    try {17      setLoading(true)18      const user = supabase.auth.user()1920      const { data, error, status } = await supabase21        .from('profiles')22        .select(`username, website, avatar_url`)23        .eq('id', user.id)24        .single()2526      if (error && status !== 406) {27        throw error28      }2930      if (data) {31        setUsername(data.username)32        setWebsite(data.website)33        setAvatarUrl(data.avatar_url)34      }35    } catch (error) {36      alert(error.message)37    } finally {38      setLoading(false)39    }40  }4142  async function updateProfile({ username, website, avatar_url }) {43    try {44      setLoading(true)45      const user = supabase.auth.user()4647      const updates = {48        id: user.id,49        username,50        website,51        avatar_url,52        updated_at: new Date(),53      }5455      const { error } = await supabase.from('profiles').upsert(updates, {56        returning: 'minimal', // Don't return the value after inserting57      })5859      if (error) {60        throw error61      }6263      alert('Updated profile!')64    } catch (error) {65      alert(error.message)66    } finally {67      setLoading(false)68    }69  }7071  return (72    <div className="row flex-center flex">73      <div className="col-6 form-widget">74        <h1 className="header">Supabase + RedwoodJS</h1>75        <p className="description">Your profile</p>76        <div className="form-widget">77          <div>78            <label htmlFor="email">Email</label>79            <input id="email" type="text" value={currentUser.email} disabled />80          </div>81          <div>82            <label htmlFor="username">Name</label>83            <input84              id="username"85              type="text"86              value={username || ''}87              onChange={(e) => setUsername(e.target.value)}88            />89          </div>90          <div>91            <label htmlFor="website">Website</label>92            <input93              id="website"94              type="url"95              value={website || ''}96              onChange={(e) => setWebsite(e.target.value)}97            />98          </div>99100          <div>101            <button102              className="button primary block"103              onClick={() => updateProfile({ username, website, avatar_url })}104              disabled={loading}105            >106              {loading ? 'Loading ...' : 'Update'}107            </button>108          </div>109110          <div>111            <button className="button block" onClick={() => logOut()}>112              Sign Out113            </button>114          </div>115        </div>116      </div>117    </div>118  )119}120121export default Account
```

You'll see the use of `useAuth()` several times. Redwood's `useAuth` hook provides convenient ways to access `logIn`, `logOut`, `currentUser`, and access the `supabase` authenticate client. We'll use it to get an instance of the Supabase client to interact with your API.

### Update home page[#](#update-home-page)

Now that we have all the components in place, let's update your `HomePage` page to use them:

```
1import { useAuth } from '@redwoodjs/auth'2import { MetaTags } from '@redwoodjs/web'34import Account from 'src/components/Account'5import Auth from 'src/components/Auth'67const HomePage = () => {8  const { isAuthenticated } = useAuth()910  return (11    <>12      <MetaTags title="Welcome" />13      {!isAuthenticated ? <Auth /> : <Account />}14    </>15  )16}1718export default HomePage
```

What we're doing here is showing the sign in form if you aren't logged in and your account profile if you are.

### Launch![#](#launch)

Once that's done, run this in a terminal window to launch the `dev` server:

```
1yarn rw dev
```

And then open the browser to [localhost:8910](http://localhost:8910) and you should see the completed app.

![Supabase RedwoodJS](/docs/img/supabase-redwoodjs-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

```
1yarn rw g component avatar2  ✔ Generating component files...3    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.test.js`4    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.stories.js`5    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.js`
```

Now, update your Avatar component to contain the following widget:

```
1import { useEffect, useState } from 'react'2import { useAuth } from '@redwoodjs/auth'34const Avatar = ({ url, size, onUpload }) => {5  const { client: supabase } = useAuth()67  const [avatarUrl, setAvatarUrl] = useState(null)8  const [uploading, setUploading] = useState(false)910  useEffect(() => {11    if (url) downloadImage(url)12  }, [url])1314  async function downloadImage(path) {15    try {16      const { data, error } = await supabase.storage.from('avatars').download(path)17      if (error) {18        throw error19      }20      const url = URL.createObjectURL(data)21      setAvatarUrl(url)22    } catch (error) {23      console.log('Error downloading image: ', error.message)24    }25  }2627  async function uploadAvatar(event) {28    try {29      setUploading(true)3031      if (!event.target.files || event.target.files.length === 0) {32        throw new Error('You must select an image to upload.')33      }3435      const file = event.target.files[0]36      const fileExt = file.name.split('.').pop()37      const fileName = `${Math.random()}.${fileExt}`38      const filePath = `${fileName}`3940      const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)4142      if (uploadError) {43        throw uploadError44      }4546      onUpload(filePath)47    } catch (error) {48      alert(error.message)49    } finally {50      setUploading(false)51    }52  }5354  return (55    <div>56      {avatarUrl ? (57        <img58          src={avatarUrl}59          alt="Avatar"60          className="avatar image"61          style={{ height: size, width: size }}62        />63      ) : (64        <div className="avatar no-image" style={{ height: size, width: size }} />65      )}66      <div style={{ width: size }}>67        <label className="button primary block" htmlFor="single">68          {uploading ? 'Uploading ...' : 'Upload'}69        </label>70        <input71          style={{72            visibility: 'hidden',73            position: 'absolute',74          }}75          type="file"76          id="single"77          accept="image/*"78          onChange={uploadAvatar}79          disabled={uploading}80        />81      </div>82    </div>83  )84}8586export default Avatar
```

### Add the new widget[#](#add-the-new-widget)

And then we can add the widget to the Account component:

```
1// Import the new component2import Avatar from 'src/components/Avatar'34// ...56return (7  <div className="form-widget">8    {/* Add to the body */}9    <Avatar10      url={avatar_url}11      size={150}12      onUpload={(url) => {13        setAvatarUrl(url)14        updateProfile({ username, website, avatar_url: url })15      }}16    />17    {/* ... */}18  </div>19)
```

At this stage you have a fully functional application!

## See also[#](#see-also)

*   Learn more about [RedwoodJS](https://redwoodjs.com)
*   Visit the [RedwoodJS Discourse Community](https://community.redwoodjs.com)
