---
title: "Use Supabase with Expo React Native"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/expo-react-native"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/expo-react-native"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:05.013Z"
content_hash: "90e2fa4c7a22d36d969142a22ca0df33012c2f08a9be3632e899774f09b64abe"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Expo React Native","Expo React Native"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Expo React Native","Expo React Native"]
---
# 

Use Supabase with Expo React Native

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from an Expo app.

* * *

1

### Create a Supabase project

Go to [database.new](https://database.new) and create a new Supabase project.

Alternatively, you can create a project using the Management API:

```
1# First, get your access token from https://supabase.com/dashboard/account/tokens2export SUPABASE_ACCESS_TOKEN="your-access-token"34# List your organizations to get the organization ID5curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \6  https://api.supabase.com/v1/organizations78# Create a new project (replace <org-id> with your organization ID)9curl -X POST https://api.supabase.com/v1/projects \10  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \11  -H "Content-Type: application/json" \12  -d '{13    "organization_id": "<org-id>",14    "name": "My Project",15    "region": "us-east-1",16    "db_pass": "<your-secure-password>"17  }'
```

When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create an `instruments` table with some sample data.

```
1-- Create the table2create table instruments (3  id bigint primary key generated always as identity,4  name text not null5);6-- Insert some sample data into the table7insert into instruments (name)8values9  ('violin'),10  ('viola'),11  ('cello');1213alter table instruments enable row level security;
```

Make the data in your table publicly readable by adding an RLS policy:

```
1create policy "public can read instruments"2on public.instruments3for select to anon4using (true);
```

2

### Create an Expo app

Create a minimal Expo app using the `create-expo-app` command with the blank TypeScript template.

##### Explore drop-in UI components for your Supabase app.

UI components built on shadcn/ui that connect to Supabase via a single command.

[Explore Components](https://supabase.com/ui)

###### Terminal

```
1npx create-expo-app my-app --template blank-typescript
```

3

### Install the Supabase client library

The fastest way to get started is to use the `@supabase/supabase-js` client library which provides a convenient interface for working with Supabase from a React Native app.

Navigate to the Expo app and install `supabase-js` along with the required dependencies for secure storage and URL handling.

###### Terminal

```
1cd my-app && npx expo install @supabase/supabase-js react-native-url-polyfill expo-sqlite
```

4

### Declare Supabase Environment Variables

Create a `.env` file in the root of your project and populate it with your Supabase connection variables.

Expo requires environment variables to be prefixed with `EXPO_PUBLIC_` to be accessible in your app code.

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### .env

```
1EXPO_PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Initialize the Supabase client

Create a helper file at `lib/supabase.ts` to initialize the Supabase client using the environment variables.

The code below uses Expo's localStorage polyfill to persist authentication sessions.

###### lib/supabase.ts

```
1import 'react-native-url-polyfill/auto'2import { createClient } from '@supabase/supabase-js'3import 'expo-sqlite/localStorage/install';45const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL6const supabasePublishableKey = process.env.EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY78export const supabase = createClient(supabaseUrl, supabasePublishableKey, {9  auth: {10    storage: localStorage,11    autoRefreshToken: true,12    persistSession: true,13    detectSessionInUrl: false,14  },15})
```

6

### Query data from the app

Replace the contents of `App.tsx` with the following code to fetch and display the instruments from your database.

Use `useEffect` to fetch the data when the component mounts and display the query result using React Native components.

###### App.tsx

```
1import { useEffect, useState } from 'react'2import { StyleSheet, View, FlatList, Text } from 'react-native'3import { supabase } from './lib/supabase'45export default function App() {6  const [instruments, setInstruments] = useState([])78  useEffect(() => {9    getInstruments()10  }, [])1112  async function getInstruments() {13    const { data } = await supabase.from('instruments').select()14    setInstruments(data)15  }1617  return (18    <View style={styles.container}>19      <FlatList20        data={instruments}21        keyExtractor={(item) => item.id.toString()}22        renderItem={({ item }) => (23          <Text style={styles.item}>{item.name}</Text>24        )}25      />26    </View>27  )28}2930const styles = StyleSheet.create({31  container: {32    flex: 1,33    backgroundColor: '#fff',34    paddingTop: 50,35    paddingHorizontal: 16,36  },37  item: {38    padding: 16,39    borderBottomWidth: 1,40    borderBottomColor: '#ccc',41  },42})
```

7

### Start the app

Run the development server and scan the QR code with the Expo Go app on your phone, or press `i` for iOS simulator or `a` for Android emulator.

###### Terminal

```
1npx expo start
```

## Next steps[#](#next-steps)

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)
