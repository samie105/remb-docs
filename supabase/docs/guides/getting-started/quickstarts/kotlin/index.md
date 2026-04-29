---
title: "Use Supabase with Android Kotlin"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/kotlin"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/kotlin"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:15.501Z"
content_hash: "c26dbbeb4206938409f9ae6a866f625aa4689cde6c8048c3e8374d90fb764218"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Android Kotlin","Android Kotlin"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Android Kotlin","Android Kotlin"]
nav_prev: {"path": "../ios-swiftui/index.md", "title": "Use Supabase with iOS and SwiftUI"}
nav_next: {"path": "../laravel/index.md", "title": "Use Supabase with Laravel"}
---

# 

Use Supabase with Android Kotlin

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from an Android Kotlin app.

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

### Create an Android app with Android Studio

Open Android Studio > New > New Android Project.

3

### Install the Dependencies

Open `build.gradle.kts` (app) file and add the serialization plug, Ktor client, and Supabase client.

Replace the version placeholders `$kotlin_version` with the Kotlin version of the project, and `$supabase_version` and `$ktor_version` with the respective latest versions.

The latest supabase-kt version can be found [here](https://github.com/supabase-community/supabase-kt/releases) and Ktor version can be found [here](https://ktor.io/docs/welcome.html).

```
1plugins {2  ...3  kotlin("plugin.serialization") version "$kotlin_version"4}5...6dependencies {7  ...8  implementation(platform("io.github.jan-tennert.supabase:bom:$supabase_version"))9  implementation("io.github.jan-tennert.supabase:postgrest-kt")10  implementation("io.ktor:ktor-client-android:$ktor_version")11}
```

4

### Add internet access permission

Add the following line to the `AndroidManifest.xml` file under the `manifest` tag and outside the `application` tag.

```
1...2<uses-permission android:name="android.permission.INTERNET" />3...
```

5

### Initialize the Supabase client

You can create a Supabase client whenever you need to perform an API call.

For the sake of simplicity, we will create a client in the `MainActivity.kt` file at the top just below the imports.

Replace the `supabaseUrl` and `supabaseKey` with your own:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1import ...23val supabase = createSupabaseClient(4    supabaseUrl = "https://xyzcompany.supabase.co",5    supabaseKey = "your_publishable_key"6  ) {7    install(Postgrest)8}9...
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=androidkotlin).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=androidkotlin).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=androidkotlin), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

6

### Create a data model for instruments

Create a serializable data class to represent the data from the database.

Add the following below the `createSupabaseClient` function in the `MainActivity.kt` file.

```
1@Serializable2data class Instrument(3    val id: Int,4    val name: String,5)
```

7

### Query data from the app

Use `LaunchedEffect` to fetch data from the database and display it in a `LazyColumn`.

Replace the default `MainActivity` class with the following code.

Note that we are making a network request from our UI code. In production, you should probably use a `ViewModel` to separate the UI and data fetching logic.

```
1class MainActivity : ComponentActivity() {2    override fun onCreate(savedInstanceState: Bundle?) {3        super.onCreate(savedInstanceState)4        setContent {5            SupabaseTutorialTheme {6                // A surface container using the 'background' color from the theme7                Surface(8                    modifier = Modifier.fillMaxSize(),9                    color = MaterialTheme.colorScheme.background10                ) {11                    InstrumentsList()12                }13            }14        }15    }16}1718@Composable19fun InstrumentsList() {20    var instruments by remember { mutableStateOf<List<Instrument>>(listOf()) }21    LaunchedEffect(Unit) {22        withContext(Dispatchers.IO) {23            instruments = supabase.from("instruments")24                              .select().decodeList<Instrument>()25        }26    }27    LazyColumn {28        items(29            instruments,30            key = { instrument -> instrument.id },31        ) { instrument ->32            Text(33                instrument.name,34                modifier = Modifier.padding(8.dp),35            )36        }37    }38}
```

8

### Start the app

Run the app on an emulator or a physical device by clicking the `Run app` button in Android Studio.
