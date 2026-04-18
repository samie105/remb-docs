---
title: "Using Custom Schemas"
source: "https://supabase.com/docs/guides/api/using-custom-schemas"
canonical_url: "https://supabase.com/docs/guides/api/using-custom-schemas"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:54.351Z"
content_hash: "aaebe41311928303171c9ade380e3b7955e9d9a5bec03afcf6f150d49b52aa01"
menu_path: ["Data REST API","Data REST API","Using the Data APIs","Using the Data APIs","Using custom schemas","Using custom schemas"]
section_path: ["Data REST API","Data REST API","Using the Data APIs","Using the Data APIs","Using custom schemas","Using custom schemas"]
nav_prev: {"path": "supabase/docs/guides/api/sql-to-api/index.md", "title": "Converting SQL to JavaScript API"}
nav_next: {"path": "supabase/docs/guides/api/sql-to-rest/index.md", "title": "SQL to REST API Translator"}
---

# 

Using Custom Schemas

* * *

By default, your database has a `public` schema which is automatically exposed on data APIs.

## Creating custom schemas[#](#creating-custom-schemas)

You can create your own custom schema/s by running the following SQL, substituting `myschema` with the name you want to use for your schema:

```
1CREATE SCHEMA myschema;
```

## Exposing custom schemas[#](#exposing-custom-schemas)

You can expose custom database schemas - to do so you need to follow these steps:

1.  Go to [API settings](/dashboard/project/_/settings/api) and add your custom schema to "Exposed schemas".
2.  Run the following SQL, substituting `myschema` with your schema name:

```
1GRANT USAGE ON SCHEMA myschema TO anon, authenticated, service_role;2GRANT ALL ON ALL TABLES IN SCHEMA myschema TO anon, authenticated, service_role;3GRANT ALL ON ALL ROUTINES IN SCHEMA myschema TO anon, authenticated, service_role;4GRANT ALL ON ALL SEQUENCES IN SCHEMA myschema TO anon, authenticated, service_role;5ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON TABLES TO anon, authenticated, service_role;6ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON ROUTINES TO anon, authenticated, service_role;7ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA myschema GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;
```

Now you can access these schemas from data APIs:

```
1// Initialize the JS client2import { createClient } from '@supabase/supabase-js'3const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {4  db: { schema: 'myschema' },5})67// Make a request8const { data: todos, error } = await supabase.from('todos').select('*')910// You can also change the target schema on a per-query basis11const { data: todos, error } = await supabase.schema('myschema').from('todos').select('*')
```

