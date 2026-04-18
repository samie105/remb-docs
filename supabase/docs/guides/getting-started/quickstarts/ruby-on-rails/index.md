---
title: "Use Supabase with Ruby on Rails"
source: "https://supabase.com/docs/guides/getting-started/quickstarts/ruby-on-rails"
canonical_url: "https://supabase.com/docs/guides/getting-started/quickstarts/ruby-on-rails"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:25.741Z"
content_hash: "69eab1f3dfdf90d661b64b7d417eeed50d0ad631bc624fdf01746b30901a3667"
menu_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Ruby on Rails","Ruby on Rails"]
section_path: ["Start with Supabase","Start with Supabase","Framework Quickstarts","Framework Quickstarts","Ruby on Rails","Ruby on Rails"]
nav_prev: {"path": "supabase/docs/guides/getting-started/quickstarts/redwoodjs/index.md", "title": "Use Supabase with RedwoodJS"}
nav_next: {"path": "supabase/docs/guides/getting-started/quickstarts/refine/index.md", "title": "Use Supabase with Refine"}
---

# 

Use Supabase with Ruby on Rails

## 

Learn how to create a Rails project and connect it to your Supabase Postgres database.

* * *

1

### Create a Rails Project

Make sure your Ruby and Rails versions are up to date, then use `rails new` to scaffold a new Rails project. Use the `-d=postgresql` flag to set it up for Postgres.

Go to the [Rails docs](https://guides.rubyonrails.org/getting_started.html) for more details.

###### Terminal

```
1rails new blog -d=postgresql
```

2

### Set up the Postgres connection details

Go to [database.new](https://database.new) and create a new Supabase project. Save your database password securely.

When your project is up and running, navigate to your project dashboard and click on [Connect](/dashboard/project/_?showConnect=true&method=session).

Look for the Session Pooler connection string and copy the string. You will need to replace the Password with your saved database password. You can reset your database password in your [Database Settings](/dashboard/project/_/database/settings) if you do not have it.

If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

###### Terminal

```
1export DATABASE_URL=postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
```

3

### Create and run a database migration

Rails includes Active Record as the ORM as well as database migration tooling which generates the SQL migration files for you.

Create an example `Article` model and generate the migration files.

###### Terminal

```
1bin/rails generate model Article title:string body:text2bin/rails db:migrate
```

4

### Use the Model to interact with the database

You can use the included Rails console to interact with the database. For example, you can create new entries or list all entries in a Model's table.

###### Terminal

```
1bin/rails console
```

###### irb

```
1article = Article.new(title: "Hello Rails", body: "I am on Rails!")2article.save # Saves the entry to the database34Article.all
```

5

### Start the app

Run the development server. Go to [http://127.0.0.1:3000](http://127.0.0.1:3000) in a browser to see your application running.

###### Terminal

```
1bin/rails server
```
