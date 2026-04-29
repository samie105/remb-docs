---
title: "Build a User Management App with Expo React Native"
source: "https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native"
canonical_url: "https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:44.146Z"
content_hash: "2d00f6043308db057a31f83381d1383c4fe7c215fbef31d7e8fc848828d0525e"
menu_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Expo React Native","Expo React Native"]
section_path: ["Start with Supabase","Start with Supabase","Mobile tutorials","Mobile tutorials","Expo React Native","Expo React Native"]
nav_prev: {"path": "supabase/docs/guides/getting-started/tutorials/with-angular/index.md", "title": "Build a User Management App with Angular"}
nav_next: {"path": "supabase/docs/guides/getting-started/tutorials/with-flutter/index.md", "title": "Build a User Management App with Flutter"}
---

# 

Build a User Management App with Expo React Native

* * *

This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](../../../auth/index.md#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](../../../auth/index.md) - allow users to sign up and log in.
*   [Supabase Storage](../../../storage/index.md) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/supabase-flutter-demo.png)

If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/expo-user-management).

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

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=exporeactnative).

[Read the API keys docs](../../../api/api-keys/index.md) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=exporeactnative), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

## Building the app[#](#building-the-app)

Start by building the React Native app from scratch.

### Initialize a React Native app[#](#initialize-a-react-native-app)

Use [`expo`](https://docs.expo.dev/get-started/create-a-new-app/) to initialize an app called `expo-user-management`:

```
1npx create-expo-app -t expo-template-blank-typescript expo-user-management23cd expo-user-management
```

Then install the additional dependencies:

```
1npx expo install @supabase/supabase-js @rneui/themed expo-sqlite
```

Now create a helper file to initialize the Supabase client using the API URL and the key that you copied [earlier](#get-api-details).

These variables are safe to expose in your Expo app since Supabase has [Row Level Security](../../../database/postgres/row-level-security/index.md) enabled on your Database.

###### lib/supabase.ts

```
1import { createClient } from '@supabase/supabase-js'2import AsyncStorage from '@react-native-async-storage/async-storage'34const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL!5const supabaseKey = process.env.EXPO_PUBLIC_SUPABASE_KEY!67export const supabase = createClient(supabaseUrl, supabaseKey, {8  auth: {9    storage: AsyncStorage as any,10    autoRefreshToken: true,11    persistSession: true,12    detectSessionInUrl: false,13  },14})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/expo-user-management/lib/supabase.ts)

### Set up a login component[#](#set-up-a-login-component)

Set up a React Native component to manage logins and sign ups. Users should be able to sign in with their email and password.

###### components/Auth.tsx

```
1import React, { useState } from 'react'2import { Alert, StyleSheet, View } from 'react-native'3import { supabase } from '../lib/supabase'4import { Button, Input } from '@rneui/themed'56export default function Auth() {7  const [email, setEmail] = useState('')8  const [password, setPassword] = useState('')9  const [loading, setLoading] = useState(false)1011  async function signInWithEmail() {12    setLoading(true)13    console.log({ email, password })14    const { error } = await supabase.auth.signInWithPassword({15      email: email,16      password: password,17    })1819    if (error) Alert.alert(error.message)20    setLoading(false)21  }2223  async function signUpWithEmail() {24    setLoading(true)25    const { error } = await supabase.auth.signUp({26      email: email,27      password: password,28    })2930    if (error) Alert.alert(error.message)31    setLoading(false)32  }3334  return (35    <View>36      <View style={[styles.verticallySpaced, styles.mt20]}>37        <Input38          label="Email"39          leftIcon={{ type: 'font-awesome', name: 'envelope' }}40          onChangeText={(text) => setEmail(text)}41          value={email}42          placeholder="email@address.com"43          autoCapitalize={'none'}44        />45      </View>46      <View style={styles.verticallySpaced}>47        <Input48          label="Password"49          leftIcon={{ type: 'font-awesome', name: 'lock' }}50          onChangeText={(text) => setPassword(text)}51          value={password}52          secureTextEntry={true}53          placeholder="Password"54          autoCapitalize={'none'}55        />56      </View>57      <View style={[styles.verticallySpaced, styles.mt20]}>58        <Button title="Sign in" disabled={loading} onPress={() => signInWithEmail()} />59      </View>60      <View style={styles.verticallySpaced}>61        <Button title="Sign up" disabled={loading} onPress={() => signUpWithEmail()} />62      </View>63    </View>64  )65}6667const styles = StyleSheet.create({68  container: {69    marginTop: 40,70    padding: 12,71  },72  verticallySpaced: {73    paddingTop: 4,74    paddingBottom: 4,75    alignSelf: 'stretch',76  },77  mt20: {78    marginTop: 20,79  },80})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/expo-user-management/components/Auth.tsx)

By default Supabase Auth requires email verification before a session is created for the users. To support email verification you need to [implement deep link handling](/docs/guides/auth/native-mobile-deep-linking?platform=react-native)!

While testing, you can disable email confirmation in your [project's email auth provider settings](/dashboard/project/_/auth/providers).

### Account page[#](#account-page)

After a user signs in, you can let them to edit their profile details and manage their account.

Create a new component for that called `Account.tsx`.

###### components/Account.tsx

```
1import { useState, useEffect } from 'react'2import { supabase } from '../lib/supabase'3import { StyleSheet, View, Alert } from 'react-native'4import { Button, Input } from '@rneui/themed'5import Avatar from './Avatar'67export default function Account({ userId, email }: { userId: string; email?: string }) {8  const [loading, setLoading] = useState(true)9  const [username, setUsername] = useState('')10  const [website, setWebsite] = useState('')11  const [avatarUrl, setAvatarUrl] = useState('')1213  useEffect(() => {14    if (userId) getProfile()15  }, [userId])1617  async function getProfile() {18    try {19      setLoading(true)2021      let { data, error, status } = await supabase22        .from('profiles')23        .select(`username, website, avatar_url`)24        .eq('id', userId)25        .single()26      if (error && status !== 406) {27        throw error28      }2930      if (data) {31        setUsername(data.username)32        setWebsite(data.website)33        setAvatarUrl(data.avatar_url)34      }35    } catch (error) {36      if (error instanceof Error) {37        Alert.alert(error.message)38      }39    } finally {40      setLoading(false)41    }42  }4344  async function updateProfile({45    username,46    website,47    avatar_url,48  }: {49    username: string50    website: string51    avatar_url: string52  }) {53    try {54      setLoading(true)5556      const updates = {57        id: userId,58        username,59        website,60        avatar_url,61        updated_at: new Date(),62      }6364      let { error } = await supabase.from('profiles').upsert(updates)6566      if (error) {67        throw error68      }69    } catch (error) {70      if (error instanceof Error) {71        Alert.alert(error.message)72      }73    } finally {74      setLoading(false)75    }76  }7778  return (79    <View>80      <View>81        <Avatar82          size={200}83          url={avatarUrl}84          onUpload={(url: string) => {85            setAvatarUrl(url)86            updateProfile({ username, website, avatar_url: url })87          }}88        />89      </View>90      <View style={[styles.verticallySpaced, styles.mt20]}>91        <Input label="Email" value={email} disabled />92      </View>93      <View style={styles.verticallySpaced}>94        <Input label="Username" value={username || ''} onChangeText={(text) => setUsername(text)} />95      </View>96      <View style={styles.verticallySpaced}>97        <Input label="Website" value={website || ''} onChangeText={(text) => setWebsite(text)} />98      </View>99100      <View style={[styles.verticallySpaced, styles.mt20]}>101        <Button102          title={loading ? 'Loading ...' : 'Update'}103          onPress={() => updateProfile({ username, website, avatar_url: avatarUrl })}104          disabled={loading}105        />106      </View>107108      <View style={styles.verticallySpaced}>109        <Button title="Sign Out" onPress={() => supabase.auth.signOut()} />110      </View>111    </View>112  )113}114115const styles = StyleSheet.create({116  container: {117    marginTop: 40,118    padding: 12,119  },120  verticallySpaced: {121    paddingTop: 4,122    paddingBottom: 4,123    alignSelf: 'stretch',124  },125  mt20: {126    marginTop: 20,127  },128})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/expo-user-management/components/Account.tsx)

### Launch![#](#launch)

Now that you have all the components in place, update `App.tsx`:

###### App.tsx

```
1import 'react-native-url-polyfill/auto'2import { useState, useEffect } from 'react'3import { supabase } from './lib/supabase'4import Auth from './components/Auth'5import Account from './components/Account'6import { View } from 'react-native'78export default function App() {9  const [userId, setUserId] = useState<string | null>(null)10  const [email, setEmail] = useState<string | undefined>(undefined)1112  useEffect(() => {13    supabase.auth.getClaims().then(({ data: { claims } }) => {14      if (claims) {15        setUserId(claims.sub)16        setEmail(claims.email)17      }18    })1920    supabase.auth.onAuthStateChange(async (_event, _session) => {21      const {22        data: { claims },23      } = await supabase.auth.getClaims()24      if (claims) {25        setUserId(claims.sub)26        setEmail(claims.email)27      } else {28        setUserId(null)29        setEmail(undefined)30      }31    })32  }, [])3334  return <View>{userId ? <Account key={userId} userId={userId} email={email} /> : <Auth />}</View>35}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/expo-user-management/App.tsx)

Once that's done, run this in a terminal window:

```
1npm start
```

And then press the appropriate key for the environment you want to test the app in and you should see the completed app.

## Bonus: Profile photos[#](#bonus-profile-photos)

Every Supabase project is configured with [Storage](../../../storage/index.md) for managing large files like photos and videos.

### Additional dependency installation[#](#additional-dependency-installation)

You need an image picker that works on the environment you are building the project for, this example uses `expo-image-picker`.

```
1npx expo install expo-image-picker
```

### Create an upload widget[#](#create-an-upload-widget)

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component:

###### components/Avatar.tsx

```
1import { useState, useEffect } from 'react'2import { supabase } from '../lib/supabase'3import { StyleSheet, View, Alert, Image, Button } from 'react-native'4import * as ImagePicker from 'expo-image-picker'56interface Props {7  size: number8  url: string | null9  onUpload: (filePath: string) => void10}1112export default function Avatar({ url, size = 150, onUpload }: Props) {13  const [uploading, setUploading] = useState(false)14  const [avatarUrl, setAvatarUrl] = useState<string | null>(null)15  const avatarSize = { height: size, width: size }1617  useEffect(() => {18    if (url) downloadImage(url)19  }, [url])2021  async function downloadImage(path: string) {22    try {23      const { data, error } = await supabase.storage.from('avatars').download(path)2425      if (error) {26        throw error27      }2829      const fr = new FileReader()30      fr.readAsDataURL(data)31      fr.onload = () => {32        setAvatarUrl(fr.result as string)33      }34    } catch (error) {35      if (error instanceof Error) {36        console.log('Error downloading image: ', error.message)37      }38    }39  }4041  async function uploadAvatar() {42    try {43      setUploading(true)4445      const result = await ImagePicker.launchImageLibraryAsync({46        mediaTypes: ['images'],47        allowsEditing: true,48        quality: 1,49      })5051      if (result.canceled || !result.assets || result.assets.length === 0) {52        return53      }5455      const image = result.assets[0]56      if (!image.uri) {57        throw new Error('No image uri!')58      }5960      const arraybuffer = await fetch(image.uri).then((res) => res.arrayBuffer())61      const fileExt = image.uri.split('.').pop()?.toLowerCase() ?? 'jpeg'62      const filePath = `${Math.random()}.${fileExt}`6364      const { error } = await supabase.storage.from('avatars').upload(filePath, arraybuffer, {65        contentType: image.mimeType ?? 'image/jpeg',66      })6768      if (error) {69        throw error70      }7172      onUpload(filePath)73    } catch (error) {74      if (error instanceof Error) {75        Alert.alert(error.message)76      }77    } finally {78      setUploading(false)79    }80  }8182  return (83    <View>84      {avatarUrl ? (85        <Image86          source={{ uri: avatarUrl }}87          accessibilityLabel="Avatar"88          style={[avatarSize, styles.avatar, styles.image]}89        />90      ) : (91        <View style={[avatarSize, styles.avatar, styles.noImage]} />92      )}93      <View>94        <Button95          title={uploading ? 'Uploading ...' : 'Upload'}96          onPress={uploadAvatar}97          disabled={uploading}98        />99      </View>100    </View>101  )102}103104const styles = StyleSheet.create({105  avatar: {106    borderRadius: 5,107    overflow: 'hidden',108    maxWidth: '100%',109  },110  image: {111    objectFit: 'cover',112    paddingTop: 0,113  },114  noImage: {115    backgroundColor: '#333',116    borderRadius: 5,117  },118})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/user-management/expo-user-management/components/Avatar.tsx)

### Add the new widget[#](#add-the-new-widget)

And then add the widget to the Account page. The `Account.tsx` component [shown earlier](#account-page) already includes the `Avatar` component when using the full example code.

Now run the prebuild command to get the application working on your chosen platform.

```
1npx expo prebuild
```

At this stage you have a fully functional application!
