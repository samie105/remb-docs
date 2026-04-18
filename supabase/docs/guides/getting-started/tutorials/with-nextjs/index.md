---
title: "Build a User Management App with Next.js"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:01.712Z"
content_hash: "b97395d3aaa64906e60ccf9b81a44e13faa86959f1c057c05cdb631c74b4e767"
menu_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Next.js","Next.js"]
section_path: ["Start with Supabase","Start with Supabase","Web app demos","Web app demos","Next.js","Next.js"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-kotlin/index.md", "title": "Build a Product Management Android App with Jetpack Compose"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-nuxt-3/index.md", "title": "Build a User Management App with Nuxt 3"}
---

# 

Build a User Management App with Next.js

* * *

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nextjs).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=frameworks&framework=nextjs), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the Next.js app from scratch.

### Initialize a Next.js app[#](#initialize-a-nextjs-app)

Use [`create-next-app`](https://nextjs.org/docs/getting-started) to initialize an app called `supabase-nextjs`:

```
1npx create-next-app@latest --ts --use-npm supabase-nextjs2cd supabase-nextjs
```

Then install the Supabase client library: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

Save the environment variables in a `.env.local` file at the root of the project, and paste the API URL and the key that you copied [earlier](#get-api-details).

```
1NEXT_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL2NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```

### App styling (optional)[#](#app-styling-optional)

An optional step is to update the CSS file `app/globals.css` to make the app look better. You can find the full contents of this file [in the example repository](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/nextjs-user-management/app/globals.css).

### Supabase Server-Side Auth[#](#supabase-server-side-auth)

Next.js is a highly versatile framework offering pre-rendering at build time (SSG), server-side rendering at request time (SSR), API routes, and proxy edge-functions.

To better integrate with the framework, we've created the `@supabase/ssr` package for Server-Side Auth. It has all the functionalities to quickly configure your Supabase project to use cookies for storing user sessions. Read the [Next.js Server-Side Auth guide](/docs/guides/auth/server-side/nextjs) for more information.

Install the package for Next.js.

```
1npm install @supabase/ssr
```

### Supabase utilities[#](#supabase-utilities)

There are two different types of clients in Supabase:

1.  **Client Component client** - To access Supabase from Client Components, which run in the browser.
2.  **Server Component client** - To access Supabase from Server Components, Server Actions, and Route Handlers, which run only on the server.

We recommend creating the following essential utilities files for creating clients, and organize them within `lib/supabase` at the root of the project.

Create a `client.ts` and a `server.ts` with the following functionalities for client-side Supabase and server-side Supabase, respectively.

```
1import { createBrowserClient } from '@supabase/ssr'23export function createClient() {4  // Create a supabase client on the browser with project's credentials5  return createBrowserClient(6    process.env.NEXT_PUBLIC_SUPABASE_URL!,7    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!8  )9}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/lib/supabase/client.ts)

### Next.js proxy[#](#nextjs-proxy)

Since Server Components can't write cookies, you need [Proxy](https://nextjs.org/docs/app/getting-started/proxy) to refresh expired Auth tokens and store them.

You can accomplish this by:

*   Refreshing the Auth token with the call to `supabase.auth.getClaims`.
*   Passing the refreshed Auth token to Server Components through `request.cookies.set`, so they don't attempt to refresh the same token themselves.
*   Passing the refreshed Auth token to the browser, so it replaces the old token. This is done with `response.cookies.set`.

You could also add a matcher, so that the Proxy only runs on routes that access Supabase. For more information, read [the Next.js matcher documentation](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher).

Be careful when protecting pages. The server gets the user session from the cookies, which anyone can spoof.

Most of the time, use `supabase.auth.getClaims()` to protect pages and user data.

_Never_ trust `supabase.auth.getSession()` inside server code such as proxy. It isn't guaranteed to revalidate the Auth token.

It's safe to trust `getClaims()` because it validates the token in storage, either directly or by calling `getUser()` solely to check the result. It doesn't use the response from `getUser()` itself, only whether the validation succeeded.

Create a `proxy.ts` file at the project root and another one within the `lib/supabase` folder. The `lib/supabase` file contains the logic for updating the session. The `proxy.ts` file uses this, which is a Next.js convention.

```
1import { type NextRequest } from 'next/server'2import { updateSession } from '@/lib/supabase/proxy'34export async function proxy(request: NextRequest) {5  // update user's auth session6  return await updateSession(request)7}89export const config = {10  matcher: [11    /*12     * Match all request paths except for the ones starting with:13     * - _next/static (static files)14     * - _next/image (image optimization files)15     * - favicon.ico (favicon file)16     * Feel free to modify this pattern to include more paths.17     */18    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',19  ],20}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/proxy.ts)

## Set up a login page[#](#set-up-a-login-page)

### Login and signup form[#](#login-and-signup-form)

In order to add login/signup page for your application:

Create a new folder named `login`, containing a `page.tsx` file with a login/signup form.

```
1import { login, signup } from './actions'23export default function LoginPage() {4  return (5    <form>6      <label htmlFor="email">Email:</label>7      <input id="email" name="email" type="email" required />8      <label htmlFor="password">Password:</label>9      <input id="password" name="password" type="password" required />10      <button formAction={login}>Log in</button>11      <button formAction={signup}>Sign up</button>12    </form>13  )14}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/login/page.tsx)

Next, you need to create the login/signup actions to hook up the form to the function. Which does the following:

*   Retrieve the user's information.
*   Send that information to Supabase as a signup request, which in turns sends a confirmation email.
*   Handle any error that arises.

The `cookies` method is called before any calls to Supabase, which takes fetch calls out of Next.js's caching. This is important for authenticated data fetches, to ensure that users get access only to their own data.

Read the Next.js docs to learn more about [opting out of data caching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#opting-out-of-data-caching).

Create the `action.ts` file in the `app/login` folder, which contains the login and signup functions and the `error/page.tsx` file, which displays an error message if the login or signup fails.

```
1'use server'23import { revalidatePath } from 'next/cache'4import { redirect } from 'next/navigation'56import { createClient } from '@/lib/supabase/server'78export async function login(formData: FormData) {9  const supabase = await createClient()1011  // type-casting here for convenience12  // in practice, you should validate your inputs13  const data = {14    email: formData.get('email') as string,15    password: formData.get('password') as string,16  }1718  const { error } = await supabase.auth.signInWithPassword(data)1920  if (error) {21    redirect('/error')22  }2324  revalidatePath('/', 'layout')25  redirect('/account')26}2728export async function signup(formData: FormData) {29  const supabase = await createClient()3031  // type-casting here for convenience32  // in practice, you should validate your inputs33  const data = {34    email: formData.get('email') as string,35    password: formData.get('password') as string,36  }3738  const { error } = await supabase.auth.signUp(data)3940  if (error) {41    redirect('/error')42  }4344  revalidatePath('/', 'layout')45  redirect('/account')46}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/login/actions.ts)

### Email template[#](#email-template)

Before proceeding, change the email template to support support a server-side authentication flow that sends a token hash:

*   Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard.
*   Select the **Confirm signup** template.
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.

##### Did you know?

You can also customize other emails sent out to new users, including the email's looks, content, and query parameters. Check out the [settings of your project](/dashboard/project/_/auth/templates).

### Confirmation endpoint[#](#confirmation-endpoint)

As you are working in a server-side rendering (SSR) environment, you need to create a server endpoint responsible for exchanging the `token_hash` for a session.

The code performs the following steps:

*   Retrieves the code sent back from the Supabase Auth server using the `token_hash` query parameter.
*   Exchanges this code for a session, which you store in your chosen storage mechanism (in this case, cookies).
*   Finally, redirects the user to the `account` page.

###### app/auth/confirm/route.ts

```
1import { type EmailOtpType } from '@supabase/supabase-js'2import { type NextRequest, NextResponse } from 'next/server'3import { createClient } from '@/lib/supabase/server'45// Creating a handler to a GET request to route /auth/confirm6export async function GET(request: NextRequest) {7  const { searchParams } = new URL(request.url)8  const token_hash = searchParams.get('token_hash')9  const type = searchParams.get('type') as EmailOtpType | null10  const next = '/account'1112  // Create redirect link without the secret token13  const redirectTo = request.nextUrl.clone()14  redirectTo.pathname = next15  redirectTo.searchParams.delete('token_hash')16  redirectTo.searchParams.delete('type')1718  if (token_hash && type) {19    const supabase = await createClient()2021    const { error } = await supabase.auth.verifyOtp({22      type,23      token_hash,24    })25    if (!error) {26      redirectTo.searchParams.delete('next')27      return NextResponse.redirect(redirectTo)28    }29  }3031  // return the user to an error page with some instructions32  redirectTo.pathname = '/error'33  return NextResponse.redirect(redirectTo)34}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/auth/confirm/route.ts)

### Account page[#](#account-page)

After a user signs in, allow them to edit their profile details and manage their account.

Create a new component for that called `AccountForm` within the `app/account` folder.

###### app/account/account-form.tsx

```
1'use client'2import { useCallback, useEffect, useState } from 'react'3import { createClient } from '@/lib/supabase/client'4import Avatar from './avatar'56// ...789export default function AccountForm({ claims }: { claims: Claims | null }) {10  const supabase = createClient()11  const [loading, setLoading] = useState(true)12  const [fullname, setFullname] = useState<string | null>(null)13  const [username, setUsername] = useState<string | null>(null)14  const [website, setWebsite] = useState<string | null>(null)15  const [avatar_url, setAvatarUrl] = useState<string | null>(null)1617  const getProfile = useCallback(async () => {18    try {19      if (!claims?.sub) {20        setLoading(false)21        return22      }2324      setLoading(true)2526      const { data, error, status } = await supabase27        .from('profiles')28        .select(`full_name, username, website, avatar_url`)29        .eq('id', claims.sub)30        .single()3132      if (error && status !== 406) {33        console.log(error)34        throw error35      }3637      if (data) {38        setFullname(data.full_name)39        setUsername(data.username)40        setWebsite(data.website)41        setAvatarUrl(data.avatar_url)42      }43    } catch (error) {44      alert('Error loading user data!')45    } finally {46      setLoading(false)47    }48  }, [claims, supabase])4950  useEffect(() => {51    getProfile()52  }, [claims, getProfile])5354  async function updateProfile({55    username,56    website,57    avatar_url,58  }: {59    username: string | null60    fullname: string | null61    website: string | null62    avatar_url: string | null63  }) {64    try {65      if (!claims?.sub) {66        alert('You must be logged in to update your profile')67        return68      }6970      setLoading(true)7172      const { error } = await supabase.from('profiles').upsert({73        id: claims.sub,74        full_name: fullname,75        username,76        website,77        avatar_url,78        updated_at: new Date().toISOString(),79      })8081  // ...8283  return (84    <div className="form-widget">85      <Avatar86        uid={claims?.sub ?? null}87        url={avatar_url}88        size={150}89        onUpload={(url) => {90          setAvatarUrl(url)91          updateProfile({ fullname, username, website, avatar_url: url })92        }}93      />94      <div>95        <label htmlFor="email">Email</label>96        <input id="email" type="text" value={claims?.email ?? ''} disabled />97      </div>98      <div>99        <label htmlFor="fullName">Full Name</label>100        <input101          id="fullName"102          type="text"103          value={fullname || ''}104          onChange={(e) => setFullname(e.target.value)}105        />106      </div>107      <div>108        <label htmlFor="username">Username</label>109        <input110          id="username"111          type="text"112          value={username || ''}113          onChange={(e) => setUsername(e.target.value)}114        />115      </div>116      <div>117        <label htmlFor="website">Website</label>118        <input119          id="website"120          type="url"121          value={website || ''}122          onChange={(e) => setWebsite(e.target.value)}123        />124      </div>125126      <div>127        <button128          className="button primary block"129          onClick={() => updateProfile({ fullname, username, website, avatar_url })}130          disabled={loading || !claims?.sub}131        >132          {loading ? 'Loading ...' : 'Update'}133        </button>134      </div>135136      <div>137        <form action="/auth/signout" method="post">138          <button className="button block" type="submit">139            Sign out140          </button>141        </form>142      </div>143    </div>144  )145}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/account/account-form.tsx)

Create an account page for the `AccountForm` component you just created

###### app/account/page.tsx

```
1import AccountForm from './account-form'2import { createClient } from '@/lib/supabase/server'34export default async function Account() {5  const supabase = await createClient()67  const { data: claimsData } = await supabase.auth.getClaims()89  return <AccountForm claims={claimsData?.claims ?? null} />10}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/account/page.tsx)

### Sign out[#](#sign-out)

Create a route handler to handle the sign out from the server side, making sure to check if the user is logged in first.

###### app/auth/signout/route.ts

```
1import { createClient } from '@/lib/supabase/server'2import { revalidatePath } from 'next/cache'3import { type NextRequest, NextResponse } from 'next/server'45export async function POST(req: NextRequest) {6  const supabase = await createClient()78  // Check if a user's logged in9  const { data: claimsData } = await supabase.auth.getClaims()1011  if (claimsData?.claims) {12    await supabase.auth.signOut()13  }1415  revalidatePath('/', 'layout')16  return NextResponse.redirect(new URL('/login', req.url), {17    status: 302,18  })19}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/auth/signout/route.ts)

### Launch[#](#launch)

Now you have all the pages, route handlers, and components in place, run the following in a terminal window:

```
1npm run dev
```

And then open the browser to [localhost:3000/login](http://localhost:3000/login) and you should see the completed app.

When you enter your email and password, you will receive an email with the title **Confirm Your Signup**. Congrats 🎉!!!

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar widget for the user so that they can upload a profile photo. Start by creating a new component:

###### app/account/avatar.tsx

```
1'use client'2import React, { useEffect, useState } from 'react'3import { createClient } from '@/lib/supabase/client'4import Image from 'next/image'56export default function Avatar({7  uid,8  url,9  size,10  onUpload,11}: {12  uid: string | null13  url: string | null14  size: number15  onUpload: (url: string) => void16}) {17  const supabase = createClient()18  const [avatarUrl, setAvatarUrl] = useState<string | null>(url)19  const [uploading, setUploading] = useState(false)2021  useEffect(() => {22    async function downloadImage(path: string) {23      try {24        const { data, error } = await supabase.storage.from('avatars').download(path)25        if (error) {26          throw error27        }2829        const url = URL.createObjectURL(data)30        setAvatarUrl(url)31      } catch (error) {32        console.log('Error downloading image: ', error)33      }34    }3536    if (url) downloadImage(url)37  }, [url, supabase])3839  const uploadAvatar: React.ChangeEventHandler<HTMLInputElement> = async (event) => {40    try {41      setUploading(true)4243      if (!event.target.files || event.target.files.length === 0) {44        throw new Error('You must select an image to upload.')45      }4647      const file = event.target.files[0]48      const fileExt = file.name.split('.').pop()49      const filePath = `${uid}-${Math.random()}.${fileExt}`5051      const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)5253      if (uploadError) {54        throw uploadError55      }5657      onUpload(filePath)58    } catch (error) {59      alert('Error uploading avatar!')60    } finally {61      setUploading(false)62    }63  }6465  return (66    <div>67      {avatarUrl ? (68        <Image69          width={size}70          height={size}71          src={avatarUrl}72          alt="Avatar"73          className="avatar image"74          style={{ height: size, width: size }}75        />76      ) : (77        <div className="avatar no-image" style={{ height: size, width: size }} />78      )}79      <div style={{ width: size }}>80        <label className="button primary block" htmlFor="single">81          {uploading ? 'Uploading ...' : 'Upload'}82        </label>83        <input84          style={{85            visibility: 'hidden',86            position: 'absolute',87          }}88          type="file"89          id="single"90          accept="image/*"91          onChange={uploadAvatar}92          disabled={uploading}93        />94      </div>95    </div>96  )97}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/account/avatar.tsx)

### Add the new widget[#](#add-the-new-widget)

Then add the widget to the `AccountForm` component:

###### app/account/account-form.tsx

```
1// ...2345        // ...67        updated_at: new Date().toISOString(),8      })9      if (error) throw error10      alert('Profile updated!')11    } catch (error) {12      alert('Error updating the data!')13    } finally {14      setLoading(false)15    }16  }171819          {/* ... */}2021          {loading ? 'Loading ...' : 'Update'}22        </button>23      </div>2425      <div>26        <form action="/auth/signout" method="post">27          <button className="button block" type="submit">28            Sign out29          </button>30        </form>31      </div>32    </div>33  )34}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/nextjs-user-management/app/account/account-form.tsx)

At this stage you have a fully functional application!

## See also[#](#see-also)

*   See the complete [example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management) and deploy it to Vercel
*   [Build a Twitter Clone with the Next.js App Router and Supabase - free egghead course](https://egghead.io/courses/build-a-twitter-clone-with-the-next-js-app-router-and-supabase-19bebadb)
*   Explore the [pre-built Auth components](/ui/docs/nextjs/password-based-auth)
*   Explore the [Supabase Cache Helpers](https://github.com/psteinroe/supabase-cache-helpers)
*   See the [Next.js Subscription Payments Starter](https://github.com/vercel/nextjs-subscription-payments) template on GitHub
