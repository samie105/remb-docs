---
title: "Build a User Management App with Refine"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-refine"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-refine"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:15.708Z"
content_hash: "bb0e7de1686175c5cdfb4fdb3033745d42c7920684c1938dbb11abd47443e6ba"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Refine","Refine"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Refine","Refine"]
nav_prev: {"path": "../with-redwoodjs/index.md", "title": "Build a User Management App with RedwoodJS"}
nav_next: {"path": "../with-solidjs/index.md", "title": "Build a User Management App with SolidJS"}
---

# 

Build a User Management App with Refine

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/refine-user-management).

## About Refine[#](#about-refine)

[Refine](https://github.com/refinedev/refine) is a React-based framework used to rapidly build data-heavy applications like admin panels, dashboards, storefronts and any type of CRUD apps. It separates app concerns into individual layers, each backed by a React context and respective provider object. For example, the auth layer represents a context served by a specific set of [`authProvider`](https://refine.dev/docs/tutorial/understanding-authprovider/index/) methods that carry out authentication and authorization actions such as logging in, logging out, getting roles data, etc. Similarly, the data layer offers another level of abstraction equipped with [`dataProvider`](https://refine.dev/docs/tutorial/understanding-dataprovider/index/) methods to handle CRUD operations at appropriate backend API endpoints.

Refine provides hassle-free integration with a Supabase backend with its supplementary [`@refinedev/supabase`](https://github.com/refinedev/refine/tree/main/packages/supabase) package. It generates `authProvider` and `dataProvider` methods at project initialization, so you don't need to spend much effort defining them yourself, choose Supabase as the backend service while creating the app with `create refine-app`.

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=refine).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=refine), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the Refine app from scratch.

### Initialize a Refine app[#](#initialize-a-refine-app)

Use [create refine-app](https://refine.dev/docs/tutorial/getting-started/headless/create-project/#launch-the-refine-cli-setup) command to initialize an app. Run the following in the terminal:

```
1npm create refine-app@latest -- --preset refine-supabase
```

The command above uses the `refine-supabase` preset which chooses the Supabase supplementary package for the app. There's no UI framework, so the app has a headless UI with plain React and CSS styling.

The `refine-supabase` preset installs the `@refinedev/supabase` package which out-of-the-box includes the Supabase dependency: [supabase-js](https://github.com/supabase/supabase-js).

Install the `@refinedev/react-hook-form` and `react-hook-form` packages that to use [React Hook Form](https://react-hook-form.com) inside Refine apps. Run:

```
1npm install @refinedev/react-hook-form react-hook-form
```

### Refine `supabaseClient`[#](#refine-supabaseclient)

The `create refine-app` generated a Supabase client in the `src/utility/supabaseClient.ts` file. It has two constants: `SUPABASE_URL` and `SUPABASE_KEY`. Replace them as `supabaseUrl` and `supabasePublishableKey` respectively and assign them your Supabase server's values.

Update it with environment variables managed by Vite:

###### src/utility/supabaseClient.ts

```
1import { createClient } from '@refinedev/supabase'23const supabaseUrl = import.meta.env.VITE_SUPABASE_URL4const supabaseKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY56export const supabaseClient = createClient(supabaseUrl, supabaseKey, {7  db: {8    schema: 'public',9  },10  auth: {11    persistSession: true,12  },13})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/utility/supabaseClient.ts)

Save the environment variables in a `.env.local` file. All you need are the API URL and the key that you copied [earlier](#get-api-details).

```
1VITE_SUPABASE_URL=YOUR_SUPABASE_URL2VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```

The `supabaseClient` fetches calls to Supabase endpoints from the app. The client is instrumental in implementing authentication using Refine's auth provider methods and CRUD actions with appropriate data provider methods.

One optional step is to update the CSS file `src/App.css` to make the app look nice. You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/refine-user-management/src/App.css).

In order to add login and user profile pages in this App, tweak the `<Refine />` component inside `App.tsx`.

### The `<Refine />` component[#](#the-refine--component)

The `App.tsx` file initially looks like this:

```
1import { Refine, WelcomePage } from '@refinedev/core'2import { RefineKbar, RefineKbarProvider } from '@refinedev/kbar'3import routerProvider, {4  DocumentTitleHandler,5  UnsavedChangesNotifier,6} from '@refinedev/react-router'7import { dataProvider, liveProvider } from '@refinedev/supabase'8import { BrowserRouter, Route, Routes } from 'react-router'9import './App.css'10import authProvider from './authProvider'11import { supabaseClient } from './utility'1213function App() {14  return (15    <BrowserRouter>16      <RefineKbarProvider>17        <Refine18          dataProvider={dataProvider(supabaseClient)}19          liveProvider={liveProvider(supabaseClient)}20          authProvider={authProvider}21          routerProvider={routerProvider}22          options={{23            syncWithLocation: true,24            warnWhenUnsavedChanges: true,25          }}26        >27          <Routes>28            <Route index element={<WelcomePage />} />29          </Routes>30          <RefineKbar />31          <UnsavedChangesNotifier />32          <DocumentTitleHandler />33        </Refine>34      </RefineKbarProvider>35    </BrowserRouter>36  )37}3839export default App
```

Focus on the [`<Refine />`](https://refine.dev/docs/api-reference/core/components/refine-config/) component, which comes with props passed to it. Notice the `dataProvider` prop. It uses a `dataProvider()` function with `supabaseClient` passed as argument to generate the data provider object. The `authProvider` object also uses `supabaseClient` in implementing its methods. You can look it up in `src/authProvider.ts` file.

## Customize `authProvider`[#](#customize-authprovider)

If you examine the `authProvider` object you can notice that it has a `login` method that implements an OAuth and Email / Password strategy for authentication. This tutorial instead removes them and use Magic Links to allow users sign in with their email without using passwords.

Use `supabaseClient` auth's `signInWithOtp` method inside `authProvider.login` method:

###### src/authProvider.ts

```
1login: async ({ email }) => {2  try {3    const { error } = await supabaseClient.auth.signInWithOtp({ email });45    if (!error) {6      alert("Check your email for the login link!");7      return {8        success: true,9      };10    };1112    throw error;13  } catch (e: any) {14    alert(e.message);15    return {16      success: false,17      e,18    };19  }20},
```

Remove `register`, `updatePassword`, `forgotPassword` and `getPermissions` properties, which are optional type members and also not necessary for the app. The final `authProvider` object looks like this:

###### src/authProvider.ts

```
1import { AuthProvider } from '@refinedev/core'23import { supabaseClient } from './utility'45const authProvider: AuthProvider = {6  login: async ({ email }) => {7    try {8      const { error } = await supabaseClient.auth.signInWithOtp({ email })910      if (!error) {11        alert('Check your email for the login link!')12        return {13          success: true,14        }15      }1617      throw error18    } catch (e: any) {19      alert(e.message)20      return {21        success: false,22        e,23      }24    }25  },26  logout: async () => {27    const { error } = await supabaseClient.auth.signOut()2829    if (error) {30      return {31        success: false,32        error,33      }34    }3536    return {37      success: true,38      redirectTo: '/',39    }40  },41  onError: async (error) => {42    console.error(error)43    return { error }44  },45  check: async () => {46    try {47      const { data, error } = await supabaseClient.auth.getClaims()4849      if (error || !data) {50        return {51          authenticated: false,52          error: {53            message: 'Check failed',54            name: 'Session not found',55          },56          logout: true,57          redirectTo: '/login',58        }59      }60    } catch (error: any) {61      return {62        authenticated: false,63        error: error || {64          message: 'Check failed',65          name: 'Not authenticated',66        },67        logout: true,68        redirectTo: '/login',69      }70    }7172    return {73      authenticated: true,74    }75  },76  getIdentity: async () => {77    const { data } = await supabaseClient.auth.getUser()7879    if (data?.user) {80      return {81        ...data.user,82        name: data.user.email,83      }84    }8586    return null87  },88}8990export default authProvider
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/authProvider.ts)

### Set up a login component[#](#set-up-a-login-component)

As the app uses the headless Refine core package that comes with no supported UI framework set up a plain React component to manage logins and sign ups.

Create and edit `src/components/auth.tsx`:

###### src/components/auth.tsx

```
1import { useState } from 'react'23import { useLogin } from '@refinedev/core'45export default function Auth() {6  const [email, setEmail] = useState('')7  const { isPending, mutate: login } = useLogin()89  const handleLogin = async (event: { preventDefault: () => void }) => {10    event.preventDefault()11    login({ email })12  }1314  return (15    <div className="row flex flex-center container">16      <div className="col-6 form-widget">17        <h1 className="header">Supabase + Refine</h1>18        <p className="description">Sign in via magic link with your email below</p>19        <form className="form-widget" onSubmit={handleLogin}>20          <div>21            <input22              className="inputField"23              type="email"24              placeholder="Your email"25              value={email}26              required={true}27              onChange={(e) => setEmail(e.target.value)}28            />29          </div>30          <div>31            <button className={'button block'} disabled={isPending}>32              {isPending ? <span>Loading</span> : <span>Send magic link</span>}33            </button>34          </div>35        </form>36      </div>37    </div>38  )39}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/components/auth.tsx)

The [`useLogin()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogin/) Refine auth hook to grab the `mutate: login` method to use inside `handleLogin()` function and `isLoading` state for the form submission. The `useLogin()` hook conveniently offers access to `authProvider.login` method for authenticating the user with OTP.

### Account page[#](#account-page)

After a user is signed in, allow them to edit their profile details and manage their account.

Create a new component for that in `src/components/account.tsx`.

###### src/components/account.tsx

```
1import { BaseKey, useGetIdentity, useLogout } from '@refinedev/core'23import { useForm } from '@refinedev/react-hook-form'45// ...67interface IUserIdentity {8  id?: BaseKey9  username: string10  name: string11}1213export interface IProfile {14  id?: string15  username?: string16  website?: string17  avatar_url?: string18}1920export default function Account() {21  const { data: userIdentity } = useGetIdentity<IUserIdentity>()2223  const { mutate: logOut } = useLogout()2425  const {26    refineCore: { formLoading, query, onFinish },27    register,28    control,29    handleSubmit,30  } = useForm<IProfile>({31    refineCoreProps: {32      resource: 'profiles',33      action: 'edit',34      id: userIdentity?.id,35      redirect: false,36      onMutationError: (data) => alert(data?.message),37    },38  })3940  return (41    <div className="container" style={{ padding: '50px 0 100px 0' }}>42      <form onSubmit={handleSubmit(onFinish)} className="form-widget">4344          {/* ... */}4546          <label htmlFor="email">Email</label>47          <input id="email" name="email" type="text" value={userIdentity?.name} disabled />48        </div>49        <div>50          <label htmlFor="username">Name</label>51          <input id="username" type="text" {...register('username')} />52        </div>53        <div>54          <label htmlFor="website">Website</label>55          <input id="website" type="url" {...register('website')} />56        </div>5758        <div>59          <button className="button block primary" type="submit" disabled={formLoading}>60            {formLoading ? 'Loading ...' : 'Update'}61          </button>62        </div>6364        <div>65          <button className="button block" type="button" onClick={() => logOut()}>66            Sign Out67          </button>68        </div>69      </form>70    </div>71  )72}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/components/account.tsx)

This uses three Refine hooks, namely the [`useGetIdentity()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useGetIdentity/), [`useLogOut()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogout/) and [`useForm()`](https://refine.dev/docs/packages/documentation/react-hook-form/useForm/) hooks.

`useGetIdentity()` is a auth hook that gets the identity of the authenticated user. It grabs the current user by invoking the `authProvider.getIdentity` method under the hood.

`useLogOut()` is also an auth hook. It calls the `authProvider.logout` method to end the session.

`useForm()`, in contrast, is a data hook that exposes a series of useful objects that serve the edit form. For example, grabbing the `onFinish` function to submit the form with the `handleSubmit` event handler. It also uses `formLoading` property to present state changes of the submitted form.

The `useForm()` hook is a higher-level hook built on top of Refine's `useForm()` core hook. It fully supports form state management, field validation and submission using React Hook Form. Behind the scenes, it invokes the `dataProvider.getOne` method to get the user profile data from the Supabase `/profiles` endpoint and also invokes `dataProvider.update` method when `onFinish()` is called.

### Launch![#](#launch)

Now that you have all the components in place, define the routes for the pages in which they should be rendered.

Add the routes for `/login` with the `<Auth />` component and the routes for `index` path with the `<Account />` component. So, the final `App.tsx`:

###### src/App.tsx

```
1import { Authenticated, Refine } from '@refinedev/core'2import { RefineKbar, RefineKbarProvider } from '@refinedev/kbar'3import routerProvider, {4  CatchAllNavigate,5  DocumentTitleHandler,6  UnsavedChangesNotifier,7} from '@refinedev/react-router'8import { BrowserRouter, Outlet, Route, Routes } from 'react-router'910import { dataProvider, liveProvider } from '@refinedev/supabase'11import authProvider from './authProvider'12import { supabaseClient } from './utility'1314import Account from './components/account'15import Auth from './components/auth'1617import './App.css'1819function App() {20  return (21    <BrowserRouter>22      <RefineKbarProvider>23        <Refine24          dataProvider={dataProvider(supabaseClient)}25          liveProvider={liveProvider(supabaseClient)}26          authProvider={authProvider}27          routerProvider={routerProvider}28          options={{29            syncWithLocation: true,30            warnWhenUnsavedChanges: true,31          }}32        >33          <Routes>34            <Route35              element={36                <Authenticated37                  key="authenticated-routes"38                  fallback={<CatchAllNavigate to="/login" />}39                >40                  <Outlet />41                </Authenticated>42              }43            >44              <Route index element={<Account />} />45            </Route>46            <Route element={<Authenticated key="auth-pages" fallback={<Outlet />} />}>47              <Route path="/login" element={<Auth />} />48            </Route>49          </Routes>50          <RefineKbar />51          <UnsavedChangesNotifier />52          <DocumentTitleHandler />53        </Refine>54      </RefineKbarProvider>55    </BrowserRouter>56  )57}5859export default App
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/App.tsx)

Test the App by running the server again:

```
1npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase Refine](/docs/img/supabase-refine-demo.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Add a new component:

Create and edit `src/components/avatar.tsx`:

###### src/components/avatar.tsx

```
1import { useEffect, useState } from 'react'23import { supabaseClient } from '../utility/supabaseClient'45type TAvatarProps = {6  url?: string7  size: number8  onUpload: (filePath: string) => void9}1011export default function Avatar({ url, size, onUpload }: TAvatarProps) {12  const [avatarUrl, setAvatarUrl] = useState('')13  const [uploading, setUploading] = useState(false)1415  useEffect(() => {16    if (url) downloadImage(url)17  }, [url])1819  async function downloadImage(path: string) {20    try {21      const { data, error } = await supabaseClient.storage.from('avatars').download(path)22      if (error) {23        throw error24      }25      const url = URL.createObjectURL(data)26      setAvatarUrl(url)27    } catch (error: any) {28      console.log('Error downloading image: ', error?.message)29    }30  }3132  async function uploadAvatar(event: React.ChangeEvent<HTMLInputElement>) {33    try {34      setUploading(true)3536      if (!event.target.files || event.target.files.length === 0) {37        throw new Error('You must select an image to upload.')38      }3940      const file = event.target.files[0]41      const fileExt = file.name.split('.').pop()42      const fileName = `${Math.random()}.${fileExt}`43      const filePath = `${fileName}`4445      const { error: uploadError } = await supabaseClient.storage46        .from('avatars')47        .upload(filePath, file)4849      if (uploadError) {50        throw uploadError51      }52      onUpload(filePath)53    } catch (error: any) {54      alert(error.message)55    } finally {56      setUploading(false)57    }58  }5960  return (61    <div>62      {avatarUrl ? (63        <img64          src={avatarUrl}65          alt="Avatar"66          className="avatar image"67          style={{ height: size, width: size }}68        />69      ) : (70        <div className="avatar no-image" style={{ height: size, width: size }} />71      )}72      <div style={{ width: size }}>73        <label className="button primary block" htmlFor="single">74          {uploading ? 'Uploading ...' : 'Upload'}75        </label>76        <input77          style={{78            visibility: 'hidden',79            position: 'absolute',80          }}81          type="file"82          id="single"83          name="avatar_url"84          accept="image/*"85          onChange={uploadAvatar}86          disabled={uploading}87        />88      </div>89    </div>90  )91}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/components/avatar.tsx)

### Add the new widget[#](#add-the-new-widget)

And then add the widget to the Account page at `src/components/account.tsx`:

###### src/components/account.tsx

```
1import { BaseKey, useGetIdentity, useLogout } from '@refinedev/core'23import { useForm } from '@refinedev/react-hook-form'4import { Controller } from 'react-hook-form'56import Avatar from './avatar'78interface IUserIdentity {9  id?: BaseKey10  username: string11  name: string12}1314export interface IProfile {15  id?: string16  username?: string17  website?: string18  avatar_url?: string19}2021export default function Account() {22  const { data: userIdentity } = useGetIdentity<IUserIdentity>()2324  const { mutate: logOut } = useLogout()2526  const {27    refineCore: { formLoading, query, onFinish },28    register,29    control,30    handleSubmit,31  } = useForm<IProfile>({32    refineCoreProps: {33      resource: 'profiles',34      action: 'edit',35      id: userIdentity?.id,36      redirect: false,37      onMutationError: (data) => alert(data?.message),38    },39  })4041  return (42    <div className="container" style={{ padding: '50px 0 100px 0' }}>43      <form onSubmit={handleSubmit(onFinish)} className="form-widget">44        <Controller45          control={control}46          name="avatar_url"47          render={({ field }) => {48            return (49              <Avatar50                url={field.value}51                size={150}52                onUpload={(filePath) => {53                  onFinish({54                    ...query?.data?.data,55                    avatar_url: filePath,56                    onMutationError: (data: { message: string }) => alert(data?.message),57                  })58                  field.onChange({59                    target: {60                      value: filePath,61                    },62                  })63                }}64              />65            )66          }}67        />68        <div>69          <label htmlFor="email">Email</label>70          <input id="email" name="email" type="text" value={userIdentity?.name} disabled />71        </div>72        <div>73          <label htmlFor="username">Name</label>74          <input id="username" type="text" {...register('username')} />75        </div>76        <div>77          <label htmlFor="website">Website</label>78          <input id="website" type="url" {...register('website')} />79        </div>8081        <div>82          <button className="button block primary" type="submit" disabled={formLoading}>83            {formLoading ? 'Loading ...' : 'Update'}84          </button>85        </div>8687        <div>88          <button className="button block" type="button" onClick={() => logOut()}>89            Sign Out90          </button>91        </div>92      </form>93    </div>94  )95}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/refine-user-management/src/components/account.tsx)

At this stage, you have a fully functional application!
