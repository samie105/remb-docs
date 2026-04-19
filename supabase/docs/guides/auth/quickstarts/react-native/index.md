---
title: "Use Supabase Auth with React Native"
source: "https://supabase.com/docs/guides/auth/quickstarts/react-native"
canonical_url: "https://supabase.com/docs/guides/auth/quickstarts/react-native"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:41.083Z"
content_hash: "be89dfcac7092f36f6bebd1f4bb4d7e7eaaf70cd7250f9130f33790b17164453"
menu_path: ["Auth","Auth","Getting Started","Getting Started","React Native","React Native"]
section_path: ["Auth","Auth","Getting Started","Getting Started","React Native","React Native"]
nav_prev: {"path": "supabase/docs/guides/auth/quickstarts/react/index.md", "title": "Use Supabase Auth with React"}
nav_next: {"path": "supabase/docs/guides/auth/quickstarts/with-expo-react-native-social-auth/index.md", "title": "Build a Social Auth App with Expo React Native"}
---

# 

Use Supabase Auth with React Native

## 

Learn how to use Supabase Auth with React Native

* * *

1

### Create a new Supabase project

[Launch a new project](/dashboard) in the Supabase Dashboard.

Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql).

###### SQL\_EDITOR

```
1select * from auth.users;
```

2

### Create a React app

Create a React app using the `create-expo-app` command.

###### Terminal

```
1npx create-expo-app -t expo-template-blank-typescript my-app
```

3

### Install the Supabase client library

Install `supabase-js` and the required dependencies.

###### Terminal

```
1cd my-app && npx expo install @supabase/supabase-js @react-native-async-storage/async-storage @rneui/themed react-native-url-polyfill
```

4

### Set up your login component

Create a helper file `lib/supabase.ts` that exports a Supabase client using your Project URL and key.

Rename `.env.example` to `.env` and populate with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### lib/supabase.ts

```
1import { AppState, Platform } from 'react-native'2import 'react-native-url-polyfill/auto'3import AsyncStorage from '@react-native-async-storage/async-storage'4import { createClient, processLock } from '@supabase/supabase-js'56const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL!7const supabaseAnonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY!89export const supabase = createClient(supabaseUrl, supabaseAnonKey, {10  auth: {11    ...(Platform.OS !== 'web' ? { storage: AsyncStorage } : {}),12    autoRefreshToken: true,13    persistSession: true,14    detectSessionInUrl: false,15    lock: processLock,16  },17})1819// Tells Supabase Auth to continuously refresh the session automatically20// if the app is in the foreground. When this is added, you will continue21// to receive `onAuthStateChange` events with the `TOKEN_REFRESHED` or22// `SIGNED_OUT` event if the user's session is terminated. This should23// only be registered once.24if (Platform.OS !== 'web') {25  AppState.addEventListener('change', (state) => {26    if (state === 'active') {27      supabase.auth.startAutoRefresh()28    } else {29      supabase.auth.stopAutoRefresh()30    }31  })32}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/quickstarts/react-native/lib/supabase.ts)

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=exporeactnative).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=exporeactnative).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=exporeactnative), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Create a login component

Create a React Native component to manage logins and sign ups. The app later uses the [`getClaims`](/docs/reference/javascript/auth-getclaims) method in `App.tsx` to validate the local JWT before showing the signed-in user.

###### components/Auth.tsx

```
1import React, { useState } from 'react'2import { Alert, StyleSheet, View, Text, TextInput, TouchableOpacity } from 'react-native'3import { supabase } from '../lib/supabase'45export default function Auth() {6  const [email, setEmail] = useState('')7  const [password, setPassword] = useState('')8  const [loading, setLoading] = useState(false)910  async function signInWithEmail() {11    setLoading(true)12    const { error } = await supabase.auth.signInWithPassword({13      email: email,14      password: password,15    })1617    if (error) Alert.alert(error.message)18    setLoading(false)19  }2021  async function signUpWithEmail() {22    setLoading(true)23    const {24      data: { session },25      error,26    } = await supabase.auth.signUp({27      email: email,28      password: password,29    })3031    if (error) Alert.alert(error.message)32    if (!session) Alert.alert('Please check your inbox for email verification!')33    setLoading(false)34  }3536  return (37    <View style={styles.container}>38      <View style={[styles.verticallySpaced, styles.mt20]}>39        <Text style={styles.label}>Email</Text>40        <TextInput41          onChangeText={(text) => setEmail(text)}42          value={email}43          placeholder="email@address.com"44          autoCapitalize="none"45          style={styles.input}46        />47      </View>48      <View style={styles.verticallySpaced}>49        <Text style={styles.label}>Password</Text>50        <TextInput51          onChangeText={(text) => setPassword(text)}52          value={password}53          secureTextEntry={true}54          placeholder="Password"55          autoCapitalize="none"56          style={styles.input}57        />58      </View>59      <View style={[styles.verticallySpaced, styles.mt20]}>60        <TouchableOpacity61          style={[styles.button, loading && styles.buttonDisabled]}62          onPress={() => signInWithEmail()}63          disabled={loading}64        >65          <Text style={styles.buttonText}>Sign in</Text>66        </TouchableOpacity>67      </View>68      <View style={styles.verticallySpaced}>69        <TouchableOpacity70          style={[styles.button, loading && styles.buttonDisabled]}71          onPress={() => signUpWithEmail()}72          disabled={loading}73        >74          <Text style={styles.buttonText}>Sign up</Text>75        </TouchableOpacity>76      </View>77    </View>78  )79}8081const styles = StyleSheet.create({82  container: {83    marginTop: 40,84    padding: 12,85  },86  verticallySpaced: {87    paddingTop: 4,88    paddingBottom: 4,89    alignSelf: 'stretch',90  },91  mt20: {92    marginTop: 20,93  },94  label: {95    fontSize: 16,96    fontWeight: '600',97    color: '#86939e',98    marginBottom: 6,99  },100  input: {101    borderWidth: 1,102    borderColor: '#86939e',103    borderRadius: 4,104    padding: 12,105    fontSize: 16,106  },107  button: {108    backgroundColor: '#2089dc',109    borderRadius: 4,110    padding: 12,111    alignItems: 'center',112  },113  buttonDisabled: {114    opacity: 0.5,115  },116  buttonText: {117    color: '#fff',118    fontSize: 16,119    fontWeight: '600',120  },121})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/quickstarts/react-native/components/Auth.tsx)

6

### Add the Auth component to your app

Add the `Auth` component to your `App.tsx` file. If the user is logged in, print the user id to the screen.

###### App.tsx

```
1import 'react-native-url-polyfill/auto'2import { useState, useEffect } from 'react'3import { supabase } from './lib/supabase'4import Auth from './components/Auth'5import { View, Text } from 'react-native'6import { JwtPayload } from '@supabase/supabase-js'78export default function App() {9  const [claims, setClaims] = useState<JwtPayload | null>(null)1011  useEffect(() => {12    supabase.auth.getClaims().then(({ data: { claims } }) => {13      setClaims(claims)14    })1516    supabase.auth.onAuthStateChange(() => {17      supabase.auth.getClaims().then(({ data: { claims } }) => {18        setClaims(claims)19      })20    })21  }, [])2223  return (24    <View>25      <Auth />26      {claims && <Text>{claims.sub}</Text>}27    </View>28  )29}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/auth/quickstarts/react-native/App.tsx)

7

### Start the app

Start the app, and follow the instructions in the terminal.

###### Terminal

```
1npm start
```
