---
title: "Testing Your Database"
source: "https://supabase.com/docs/guides/database/testing"
canonical_url: "https://supabase.com/docs/guides/database/testing"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:38.548Z"
content_hash: "d06b5321b385766287831ac0321401b7311fca0c518e0b4cf611c4bf0a081555"
menu_path: ["Database","Database","Configuration, optimization, and testing","Configuration, optimization, and testing","Testing your database","Testing your database"]
section_path: ["Database","Database","Configuration, optimization, and testing","Configuration, optimization, and testing","Testing your database","Testing your database"]
nav_prev: {"path": "../tables/index.md", "title": "Tables and Data"}
nav_next: {"path": "../vault/index.md", "title": "Vault"}
---

# Testing using the Supabase CLI

You can use the Supabase CLI to test your database. The minimum required version of the CLI is [v1.11.4](https://github.com/supabase/cli/releases). To get started:

*   [Install the Supabase CLI](/docs/guides/cli) on your local machine

## Creating a test[#](#creating-a-test)

Create a tests folder inside the `supabase` folder:

```
1mkdir -p ./supabase/tests/database
```

Create a new file with the `.sql` extension which will contain the test.

```
1touch ./supabase/tests/database/hello_world.test.sql
```

## Writing tests[#](#writing-tests)

All `sql` files use [pgTAP](/docs/guides/database/extensions/pgtap) as the test runner.

Let's write a simple test to check that our `auth.users` table has an ID column. Open `hello_world.test.sql` and add the following code:

```
1begin;2select plan(1); -- only one statement to run34SELECT has_column(5    'auth',6    'users',7    'id',8    'id should exist'9);1011select * from finish();12rollback;
```

## Running tests[#](#running-tests)

To run the test, you can use:

```
1supabase test db
```

This will produce the following output:

```
1$ supabase test db2supabase/tests/database/hello_world.test.sql .. ok3All tests successful.4Files=1, Tests=1,  1 wallclock secs ( 0.01 usr  0.00 sys +  0.04 cusr  0.02 csys =  0.07 CPU)5Result: PASS
```

## More resources[#](#more-resources)

*   [Testing RLS policies](/docs/guides/database/extensions/pgtap#testing-rls-policies)
*   [pgTAP extension](/docs/guides/database/extensions/pgtap)
*   Official [pgTAP documentation](https://pgtap.org/)
