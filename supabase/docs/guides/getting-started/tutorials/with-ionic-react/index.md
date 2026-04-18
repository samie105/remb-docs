---
title: "Build a User Management App with Ionic React"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-react"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-react"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:51.582Z"
content_hash: "33ec6aef2846608aca746c8d641e5f3706ed3387788da4ef1a498c8bc2ad95ec"
menu_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Ionic React","Ionic React"]
section_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Ionic React","Ionic React"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-flutter/index.md", "title": "Build a User Management App with Flutter"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-ionic-angular/index.md", "title": "Build a User Management App with Ionic Angular"}
---

# 

Build a User Management App with Ionic React

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/ionic-demos/ionic-angular-account.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/ionic-react-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=ionicreact).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=ionicreact), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start building the React app from scratch.

### Initialize an Ionic React app[#](#initialize-an-ionic-react-app)

Use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize an app called `supabase-ionic-react`:

```
1npm install -g @ionic/cli2ionic start supabase-ionic-react blank --type react3cd supabase-ionic-react
```

Install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```
1npm install @supabase/supabase-js
```

Save the environment variables in a `.env`. You need the API URL and the key that you copied [earlier](#get-api-details).

```
1VITE_SUPABASE_URL=YOUR_SUPABASE_URL2VITE_SUPABASE_KEY=YOUR_SUPABASE_KEY
```

With the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed in the browser, which is safe because they use a restricted publishable key and the SQL quickstart enables [Row Level Security](/docs/guides/auth#row-level-security) on the `profiles` table.

###### src/supabaseClient.ts

```
1import { createClient } from '@supabase/supabase-js'23const supabaseUrl = import.meta.env.VITE_SUPABASE_URL4const supabaseKey = import.meta.env.VITE_SUPABASE_KEY56if (!supabaseUrl || !supabaseKey) {7  throw new Error(8    'Missing Supabase environment variables: VITE_SUPABASE_URL and VITE_SUPABASE_KEY must be set.'9  )10}1112export const supabase = createClient(supabaseUrl, supabaseKey)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/supabaseClient.ts)

### Set up a login route[#](#set-up-a-login-route)

Set up a React component to manage logins and sign ups which uses Magic Links, so users can sign in with their email without using passwords.

###### src/pages/Login.tsx

```
1import { useState } from 'react'2import type React from 'react'3import {4  IonButton,5  IonContent,6  IonHeader,7  IonInput,8  IonItem,9  IonList,10  IonPage,11  IonTitle,12  IonToolbar,13  useIonToast,14  useIonLoading,15} from '@ionic/react'16import { supabase } from '../supabaseClient'1718export function LoginPage() {19  const [email, setEmail] = useState('')2021  const [showLoading, hideLoading] = useIonLoading()22  const [showToast] = useIonToast()23  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {24    e.preventDefault()25    await showLoading()26    try {27      const { error } = await supabase.auth.signInWithOtp({ email })28      if (error) throw error29      await showToast({ message: 'Check your email for the login link!' })30    } catch (e: any) {31      await showToast({ message: e.error_description || e.message, duration: 5000 })32    } finally {33      await hideLoading()34    }35  }36  return (37    <IonPage>38      <IonHeader>39        <IonToolbar>40          <IonTitle>Login</IonTitle>41        </IonToolbar>42      </IonHeader>4344      <IonContent>45        <div className="ion-padding">46          <h1>Supabase + Ionic React</h1>47          <p>Sign in via magic link with your email below</p>48        </div>49        <IonList inset={true}>50          <form onSubmit={handleLogin}>51            <IonItem>52              <IonInput53                value={email}54                name="email"55                onIonInput={(e) => setEmail(e.detail.value ?? '')}56                type="email"57                label="Email"58                labelPlacement="stacked"59              ></IonInput>60            </IonItem>61            <div className="ion-text-center">62              <IonButton type="submit" fill="clear">63                Login64              </IonButton>65            </div>66          </form>67        </IonList>68      </IonContent>69    </IonPage>70  )71}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/pages/Login.tsx)

### Account page[#](#account-page)

After a user signs in, they should be able to edit their profile details and manage their account.

Create a new component for that called `Account.tsx`.

###### src/pages/Account.tsx

```
1import {2  IonButton,3  IonContent,4  IonHeader,5  IonInput,6  IonItem,7  IonLabel,8  IonPage,9  IonTitle,10  IonToolbar,11  useIonLoading,12  useIonToast,13  useIonRouter,14} from '@ionic/react'15import { useEffect, useState } from 'react'16import { Avatar } from '../components/Avatar'17import { supabase } from '../supabaseClient'1819export function AccountPage() {20  const [showLoading, hideLoading] = useIonLoading()21  const [showToast] = useIonToast()22  const router = useIonRouter()23  const [email, setEmail] = useState('')24  const [profile, setProfile] = useState({25    username: '',26    website: '',27    avatar_url: '',28  })2930  useEffect(() => {31    getProfile()32  }, [])3334  const getProfile = async () => {35    await showLoading()36    try {37      const { data: authData } = await supabase.auth.getClaims()38      if (!authData?.claims) throw new Error('No user logged in')39      const { claims } = authData4041      setEmail(claims.email as string)4243      const { data, error, status } = await supabase44        .from('profiles')45        .select(`username, website, avatar_url`)46        .eq('id', claims.sub)47        .single()4849      if (error && status !== 406) {50        throw error51      }5253      if (data) {54        setProfile({55          username: data.username,56          website: data.website,57          avatar_url: data.avatar_url,58        })59      }60    } catch (error: any) {61      showToast({ message: error.message, duration: 5000 })62    } finally {63      await hideLoading()64    }65  }6667  const signOut = async () => {68    await supabase.auth.signOut()69    router.push('/', 'forward', 'replace')70  }7172  const updateProfile = async (e?: any, avatar_url?: string) => {73    e?.preventDefault()7475    await showLoading()7677    try {78      const { data } = await supabase.auth.getClaims()79      if (!data?.claims) throw new Error('No user logged in')80      const { claims } = data8182      const updates = {83        id: claims.sub,84        ...profile,85        ...(avatar_url !== undefined ? { avatar_url } : {}),86        updated_at: new Date(),87      }8889      const { error } = await supabase.from('profiles').upsert(updates)9091      if (error) {92        throw error93      }9495      // Ensure local profile state reflects the updated avatar URL96      if (avatar_url !== undefined) {97        setProfile((prev) => ({98          ...prev,99          avatar_url,100        }))101      }102103      if (avatar_url !== undefined) {104        setProfile((current) => ({105          ...current,106          avatar_url,107        }))108      }109    } catch (error: any) {110      showToast({ message: error.message, duration: 5000 })111    } finally {112      await hideLoading()113    }114  }115116  return (117    <IonPage>118      <IonHeader>119        <IonToolbar>120          <IonTitle>Account</IonTitle>121        </IonToolbar>122      </IonHeader>123124      <IonContent>125        <Avatar126          url={profile.avatar_url}127          onUpload={(fileName) => updateProfile(undefined, fileName)}128        ></Avatar>129        <form onSubmit={updateProfile}>130          <IonItem>131            <IonLabel>132              <p>Email</p>133              <p>{email}</p>134            </IonLabel>135          </IonItem>136137          <IonItem>138            <IonInput139              type="text"140              name="username"141              value={profile.username}142              onIonInput={(e) => setProfile({ ...profile, username: e.detail.value ?? '' })}143              label="Name"144              labelPlacement="stacked"145            ></IonInput>146          </IonItem>147148          <IonItem>149            <IonInput150              type="url"151              name="website"152              value={profile.website}153              onIonInput={(e) => setProfile({ ...profile, website: e.detail.value ?? '' })}154              label="Website"155              labelPlacement="stacked"156            ></IonInput>157          </IonItem>158          <div className="ion-text-center">159            <IonButton fill="clear" type="submit">160              Update Profile161            </IonButton>162          </div>163        </form>164165        <div className="ion-text-center">166          <IonButton fill="clear" onClick={signOut}>167            Log Out168          </IonButton>169        </div>170      </IonContent>171    </IonPage>172  )173}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/pages/Account.tsx)

### Launch![#](#launch)

Now that you have all the components in place, update `App.tsx`:

###### src/App.tsx

```
1import { Redirect, Route } from 'react-router-dom'2import { IonApp, IonRouterOutlet, setupIonicReact } from '@ionic/react'3import { IonReactRouter } from '@ionic/react-router'4import { supabase } from './supabaseClient'56import '@ionic/react/css/ionic.bundle.css'78/* Theme variables */9import './theme/variables.css'10import { LoginPage } from './pages/Login'11import { AccountPage } from './pages/Account'12import { useEffect, useState } from 'react'13import type { FC } from 'react'1415setupIonicReact()1617const App: FC = () => {18  const [claims, setClaims] = useState<any>(null)1920  useEffect(() => {21    supabase.auth.getClaims().then(({ data }) => {22      if (data) {23        setClaims(data.claims)24      }25    })2627    const {28      data: { subscription },29    } = supabase.auth.onAuthStateChange(() => {30      supabase.auth.getClaims().then(({ data }) => {31        if (data) {32          setClaims(data.claims)33        }34      })35    })3637    return () => subscription.unsubscribe()38  }, [])3940  return (41    <IonApp>42      <IonReactRouter>43        <IonRouterOutlet>44          <Route45            exact46            path="/"47            render={() => {48              return claims ? <Redirect to="/account" /> : <LoginPage />49            }}50          />51          <Route52            exact53            path="/account"54            render={() => (claims ? <AccountPage /> : <Redirect to="/" />)}55          />56        </IonRouterOutlet>57      </IonReactRouter>58    </IonApp>59  )60}6162export default App
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/App.tsx)

Once that's done, run this in a terminal window:

```
1ionic serve
```

Then open your browser to the URL printed by `ionic serve` (by default, [http://localhost:8100](http://localhost:8100)) and you should see the completed app.

![Supabase Ionic React](/docs/img/ionic-demos/ionic-react.png)

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.

### Create an upload widget[#](#create-an-upload-widget)

First install two packages in order to interact with the user's camera.

```
1npm install @ionic/pwa-elements @capacitor/camera
```

[Capacitor](https://capacitorjs.com) is a cross platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.

Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.

With those packages installed update `index.tsx` to include an additional bootstrapping call for the Ionic PWA Elements.

###### src/index.tsx

```
1import React from 'react'2import { createRoot } from 'react-dom/client'3import App from './App'4import { defineCustomElements } from '@ionic/pwa-elements/loader'56defineCustomElements(window)78const container = document.getElementById('root')9const root = createRoot(container!)10root.render(11  <React.StrictMode>12    <App />13  </React.StrictMode>14)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/index.tsx)

Then create an `AvatarComponent`.

###### src/components/Avatar.tsx

```
1import { IonIcon } from '@ionic/react'2import { person } from 'ionicons/icons'3import { Camera, CameraResultType } from '@capacitor/camera'4import { useEffect, useState } from 'react'5import { supabase } from '../supabaseClient'6import './Avatar.css'78export function Avatar({9  url,10  onUpload,11}: {12  url: string13  onUpload: (file: string) => Promise<void>14}) {15  const [avatarUrl, setAvatarUrl] = useState<string | undefined>()1617  useEffect(() => {18    if (url) {19      downloadImage(url)20    }21  }, [url])2223  const uploadAvatar = async () => {24    try {25      const photo = await Camera.getPhoto({26        resultType: CameraResultType.DataUrl,27      })2829      const file = await fetch(photo.dataUrl!)30        .then((res) => res.blob())31        .then((blob) => new File([blob], 'my-file', { type: `image/${photo.format}` }))3233      const fileName = `${Math.random()}-${new Date().getTime()}.${photo.format}`34      const { error: uploadError } = await supabase.storage.from('avatars').upload(fileName, file)35      if (uploadError) {36        throw uploadError37      }38      await onUpload(fileName)39    } catch (error) {40      console.log(error)41    }42  }4344  const downloadImage = async (path: string) => {45    try {46      const { data, error } = await supabase.storage.from('avatars').download(path)47      if (error) {48        throw error49      }50      const url = URL.createObjectURL(data)51      setAvatarUrl(url)52    } catch (error: any) {53      console.log('Error downloading image: ', error.message)54    }55  }5657  useEffect(() => {58    return () => {59      if (avatarUrl) {60        URL.revokeObjectURL(avatarUrl)61      }62    }63  }, [avatarUrl])6465  return (66    <div className="avatar">67      <button type="button" className="avatar_wrapper" onClick={uploadAvatar}>68        {avatarUrl ? (69          <img src={avatarUrl} alt="User avatar" />70        ) : (71          <IonIcon icon={person} className="no-avatar" />72        )}73      </button>74    </div>75  )76}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/components/Avatar.tsx)

### Add the new widget[#](#add-the-new-widget)

And then add the widget to the Account page:

###### src/pages/Account.tsx

```
1// ...23import { Avatar } from '../components/Avatar'45      // ...67      }89      if (avatar_url !== undefined) {10        setProfile((current) => ({11          ...current,12          avatar_url,13        }))14      }15    } catch (error: any) {16      showToast({ message: error.message, duration: 5000 })1718      // ...
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/ionic-react-user-management/src/pages/Account.tsx)

At this stage you have a fully functional application!
