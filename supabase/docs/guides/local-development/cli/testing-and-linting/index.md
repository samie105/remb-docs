---
title: "Testing and linting"
source: "https://supabase.com/docs/guides/local-development/cli/testing-and-linting"
canonical_url: "https://supabase.com/docs/guides/local-development/cli/testing-and-linting"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:31.079Z"
content_hash: "5cbedc2a6bef21526e1fb2beae6d96f8370fb0004e4909a8fbb2db38b0e000ca"
menu_path: ["Testing and linting"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/local-development/cli/getting-started/index.md", "title": "Supabase CLI"}
nav_next: {"path": "supabase/docs/guides/local-development/testing/overview/index.md", "title": "Testing Overview"}
---

# 

Testing and linting

## 

Using the CLI to test your Supabase project.

* * *

The Supabase CLI provides a set of tools to help you test and lint your Postgres database and Edge\` Functions.

## Testing your database[#](#testing-your-database)

The Supabase CLI provides Postgres linting using the `supabase test db` command.

```
1supabase test db --help2Tests local database with pgTAP34Usage:5  supabase test db [flags]
```

This is powered by the [pgTAP](/docs/guides/database/extensions/pgtap) extension. You can find a full guide to writing and running tests in the [Testing your database](/docs/guides/database/testing) section.

### Test helpers[#](#test-helpers)

Our friends at [Basejump](https://usebasejump.com/) have created a useful set of Database [Test Helpers](https://github.com/usebasejump/supabase-test-helpers), with an accompanying [blog post](https://usebasejump.com/blog/testing-on-supabase-with-pgtap).

### Running database tests in CI[#](#running-database-tests-in-ci)

Use our GitHub Action to [automate your database tests](/docs/guides/deployment/ci/testing).

## Testing your Edge Functions[#](#testing-your-edge-functions)

Edge Functions are powered by Deno, which provides a [native set of testing tools](https://deno.land/manual@v1.35.3/basics/testing). We extend this functionality in the Supabase CLI. You can find a detailed guide in the [Edge Functions section](/docs/guides/functions/unit-test).

## Testing Auth emails[#](#testing-auth-emails)

The Supabase CLI uses [Mailpit](https://github.com/axllent/mailpit) to capture emails sent from your local machine. This is useful for testing emails sent from Supabase Auth.

### Accessing Mailpit[#](#accessing-mailpit)

By default, Mailpit is available at [localhost:54324](http://localhost:54324) when you run `supabase start`. Open this URL in your browser to view the emails.

### Going into production[#](#going-into-production)

The "default" email provided by Supabase is only for development purposes. It is [heavily restricted](/docs/guides/platform/going-into-prod#auth-rate-limits) to ensure that it is not used for spam. Before going into production, you must configure your own email provider. This is as simple as enabling a new SMTP credentials in your [project settings](/dashboard/project/_/auth/smtp).

## Linting your database[#](#linting-your-database)

The Supabase CLI provides Postgres linting using the `supabase db lint` command:

```
1supabase db lint --help2Checks local database for typing error34Usage:5  supabase db lint [flags]67Flags:8  --level [ warning | error ] Error level to emit. (default warning)9  --linked Lints the linked project for schema errors.10  -s, --schema strings List of schema to include. (default all)
```

This is powered by [plpgsql\_check](https://github.com/okbob/plpgsql_check), which leverages the internal Postgres parser/evaluator so you see any errors that would occur at runtime. It provides the following features:

*   validates you are using the correct types for function parameters
*   identifies unused variables and function arguments
*   detection of dead code (any code after an `RETURN` command)
*   detection of missing `RETURN` commands with your Postgres function
*   identifies unwanted hidden casts, which can be a performance issue
*   checks `EXECUTE` statements against SQL injection vulnerability

Check the Reference Docs for [more information](/docs/reference/cli/supabase-db-lint).

