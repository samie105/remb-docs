---
title: "Use Supabase with Python"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/flask"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/flask"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:08.551Z"
content_hash: "191a01d5631ecbf58ae6226093fb8ef6d5eaba61f8b352f294bc9b2f49a28d1a"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Flask (Python)","Flask (Python)"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Flask (Python)","Flask (Python)"]
nav_prev: {"path": "../expo-react-native/index.md", "title": "Use Supabase with Expo React Native"}
nav_next: {"path": "../flutter/index.md", "title": "Use Supabase with Flutter"}
---

# 

Use Supabase with Python

## 

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Python app.

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

### Create a Python app with Flask

Create a new directory for your Python app and set up a virtual environment.

###### Terminal

```
1mkdir my-app && cd my-app2python3 -m venv venv3source venv/bin/activate
```

3

### Install Flask and the Supabase client library

The fastest way to get started is to use Flask for the web framework and the `supabase-py` client library which provides a convenient interface for working with Supabase from a Python app.

Install both packages using pip.

###### Terminal

```
1pip install flask supabase
```

4

### Create Environment Variables file

Create a `.env` file in your project root and populate it with your Supabase connection variables:

###### Project URL

To get your Project URL, [log in](https://supabase.com/dashboard).

###### Publishable key

To get your Publishable key, [log in](https://supabase.com/dashboard).

```
1SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>2SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
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

### Query data from the app

Install the `python-dotenv` package to load environment variables:

```
1pip install python-dotenv
```

Create an `app.py` file and add a route that fetches data from your `instruments` table using the Supabase client.

###### app.py

```
1import os2from flask import Flask3from supabase import create_client, Client4from dotenv import load_dotenv56load_dotenv()78app = Flask(__name__)910supabase: Client = create_client(11    os.environ.get("SUPABASE_URL"),12    os.environ.get("SUPABASE_PUBLISHABLE_KEY")13)1415@app.route('/')16def index():17    response = supabase.table('instruments').select("*").execute()18    instruments = response.data1920    html = '<h1>Instruments</h1><ul>'21    for instrument in instruments:22        html += f'<li>{instrument["name"]}</li>'23    html += '</ul>'2425    return html2627if __name__ == '__main__':28    app.run(debug=True)
```

6

### Start the app

Run the Flask development server, go to [http://localhost:5000](http://localhost:5000) in a browser and you should see the list of instruments.

###### Terminal

```
1python app.py
```

## Next steps[#](#next-steps)

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)
