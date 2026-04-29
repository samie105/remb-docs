---
title: "Use Supabase with Flutter"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/flutter"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/flutter"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:09.966Z"
content_hash: "538ac55406ab441d686dab0a7659100c1c5632e8d6940ee8edba74a97a4345ab"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Flutter","Flutter"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Flutter","Flutter"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/flask/index.md", "title": "Use Supabase with Python"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/hono/index.md", "title": "Use Supabase with Hono"}
---

# 

Use Supabase with Flutter

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Flutter app.

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

### Create a Flutter app

Create a Flutter app using the `flutter create` command. You can skip this step if you already have a working app.

###### Terminal

```
1flutter create my_app
```

3

### Install the Supabase client library

The fastest way to get started is to use the [`supabase_flutter`](https://pub.dev/packages/supabase_flutter) client library which provides a convenient interface for working with Supabase from a Flutter app.

Open the `pubspec.yaml` file inside your Flutter app and add `supabase_flutter` as a dependency.

###### pubspec.yaml

```
1supabase_flutter: ^2.0.0
```

4

### Initialize the Supabase client

Open `lib/main.dart` and edit the main function to initialize Supabase using your project URL and publishable key:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### lib/main.dart

```
1import 'package:supabase_flutter/supabase_flutter.dart';23Future<void> main() async {4  WidgetsFlutterBinding.ensureInitialized();56  await Supabase.initialize(7    url: 'YOUR_SUPABASE_URL',8    anonKey: 'YOUR_SUPABASE_PUBLISHABLE_KEY',9  );10  runApp(MyApp());11}
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=flutter).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=flutter).

[Read the API keys docs](../../../api/api-keys/index.md) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=flutter), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Query data from the app

Use a `FutureBuilder` to fetch the data when the home page loads and display the query result in a `ListView`.

Replace the default `MyApp` and `MyHomePage` classes with the following code.

###### lib/main.dart

```
1class MyApp extends StatelessWidget {2  const MyApp({super.key});34  @override5  Widget build(BuildContext context) {6    return const MaterialApp(7      title: 'Instruments',8      home: HomePage(),9    );10  }11}1213class HomePage extends StatefulWidget {14  const HomePage({super.key});1516  @override17  State<HomePage> createState() => _HomePageState();18}1920class _HomePageState extends State<HomePage> {21  final _future = Supabase.instance.client22      .from('instruments')23      .select();2425  @override26  Widget build(BuildContext context) {27    return Scaffold(28      body: FutureBuilder(29        future: _future,30        builder: (context, snapshot) {31          if (!snapshot.hasData) {32            return const Center(child: CircularProgressIndicator());33          }34          final instruments = snapshot.data!;35          return ListView.builder(36            itemCount: instruments.length,37            itemBuilder: ((context, index) {38              final instrument = instruments[index];39              return ListTile(40                title: Text(instrument['name']),41              );42            }),43          );44        },45      ),46    );47  }48}
```

6

### Start the app

Run your app on a platform of your choosing! By default an app should launch in your web browser.

Note that `supabase_flutter` is compatible with web, iOS, Android, macOS, and Windows apps. Running the app on macOS requires additional configuration to [set the entitlements](https://docs.flutter.dev/development/platform-integration/macos/building#setting-up-entitlements).

###### Terminal

```
1flutter run
```

## Setup deep links[#](#setup-deep-links)

Many sign in methods require deep links to redirect the user back to your app after authentication. Read more about setting deep links up for all platforms (including web) in the [Flutter Mobile Guide](../../tutorials/with-flutter/index.md#setup-deep-links).

## Going to production[#](#going-to-production)

### Android[#](#android)

In production, your Android app needs explicit permission to use the internet connection on the user's device which is required to communicate with Supabase APIs. To do this, add the following line to the `android/app/src/main/AndroidManifest.xml` file.

```
1<manifest xmlns:android="http://schemas.android.com/apk/res/android">2  <!-- Required to fetch data from the internet. -->3  <uses-permission android:name="android.permission.INTERNET" />4  <!-- ... -->5</manifest>
```
