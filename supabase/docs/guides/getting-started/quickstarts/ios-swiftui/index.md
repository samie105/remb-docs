---
title: "Use Supabase with iOS and SwiftUI"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/ios-swiftui"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/ios-swiftui"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:12.347Z"
content_hash: "010622ad3abf9a8dedef9ad077fc75c8ed0cc08a71ab8ad2bfe4e445816b5e4d"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","iOS SwiftUI","iOS SwiftUI"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","iOS SwiftUI","iOS SwiftUI"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/hono/index.md", "title": "Use Supabase with Hono"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/laravel/index.md", "title": "Use Supabase with Laravel"}
---

# 

Use Supabase with iOS and SwiftUI

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from an iOS app.

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

### Create an iOS SwiftUI app with Xcode

Open Xcode > New Project > iOS > App. You can skip this step if you already have a working app.

3

### Install the Supabase client library

Add the [supabase-swift](https://github.com/supabase/supabase-swift) package to your app using the Swift Package Manager.

In Xcode, navigate to **File > Add Package Dependencies...** and enter the repository URL `https://github.com/supabase/supabase-swift` in the search bar. For detailed instructions, see Apple's [tutorial on adding package dependencies](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

Make sure to add `Supabase` product package as a dependency to your application target.

4

### Initialize the Supabase client

Create a new `Supabase.swift` file add a new Supabase instance using your project URL and publishable key:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

###### Supabase.swift

```
1import Supabase23let supabase = SupabaseClient(4  supabaseURL: URL(string: "YOUR_SUPABASE_URL")!,5  supabaseKey: "YOUR_SUPABASE_PUBLISHABLE_KEY"6)
```

You can also get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=swift).

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=swift).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=mobiles&framework=swift), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

5

### Create a data model for instruments

Create a decodable struct to deserialize the data from the database.

Add the following code to a new file named `Instrument.swift`.

###### Instrument.swift

```
1struct Instrument: Decodable, Identifiable {2  let id: Int3  let name: String4}
```

6

### Query data from the app

Use a `task` to fetch the data from the database and display it using a `List`.

Replace the default `ContentView` with the following code.

###### ContentView.swift

```
1import SwiftUI23struct ContentView: View {45  @State var instruments: [Instrument] = []67  var body: some View {8    List(instruments) { instrument in9      Text(instrument.name)10    }11    .overlay {12      if instruments.isEmpty {13        ProgressView()14      }15    }16    .task {17      do {18        instruments = try await supabase.from("instruments").select().execute().value19      } catch {20        dump(error)21      }22    }23  }24}
```

7

### Start the app

Run the app on a simulator or a physical device by hitting `Cmd + R` on Xcode.

## Setting up deep links[#](#setting-up-deep-links)

If you want to implement authentication features like magic links or OAuth, you need to set up deep links to redirect users back to your app. For instructions on configuring custom URL schemes for your iOS app, see the [deep linking guide](/docs/guides/auth/native-mobile-deep-linking?platform=swift).

## Next steps[#](#next-steps)

*   Learn how to build a complete user management app with authentication in the [Swift tutorial](/docs/guides/getting-started/tutorials/with-swift)
*   Explore the [supabase-swift](https://github.com/supabase/supabase-swift) library on GitHub

