---
title: "Clerk"
source: "https://supabase.com/docs/guides/auth/third-party/clerk"
canonical_url: "https://supabase.com/docs/guides/auth/third-party/clerk"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:08.745Z"
content_hash: "7917fc92ebeaf1a95faf7717b8ded0a37202f06e79242ab9792cd018f562e9fa"
menu_path: ["Auth","Auth","Third-party auth","Third-party auth","Clerk","Clerk"]
section_path: ["Auth","Auth","Third-party auth","Third-party auth","Clerk","Clerk"]
nav_prev: {"path": "supabase/docs/guides/auth/third-party/auth0/index.md", "title": "Auth0"}
nav_next: {"path": "supabase/docs/guides/auth/third-party/overview/index.md", "title": "Third-party auth"}
---

# 

Clerk

## 

Use Clerk with your Supabase project

* * *

Clerk can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.

## Getting started[#](#getting-started)

Getting started is incredibly easy. Start off by visiting [Clerk's Connect with Supabase page](https://dashboard.clerk.com/setup/supabase) to configure your Clerk instance for Supabase compatibility.

Finally add a [new Third-Party Auth integration with Clerk](/dashboard/project/_/auth/third-party) in the Supabase dashboard.

### Configure for local development or self-hosting[#](#configure-for-local-development-or-self-hosting)

When developing locally or self-hosting with the Supabase CLI, add the following config to your `supabase/config.toml` file:

```
1[auth.third_party.clerk]2enabled = true3domain = "example.clerk.accounts.dev"
```

You will still need to configure your Clerk instance for Supabase compatibility.

### Manually configuring your Clerk instance[#](#manually-configuring-your-clerk-instance)

If you are not able to use [Clerk's Connect with Supabase page](https://dashboard.clerk.com/setup/supabase) to configure your Clerk instance for working with Supabase, follow these steps.

1.  Add the `role` claim to [Clerk session tokens](https://clerk.com/docs/backend-requests/resources/session-tokens) by [customizing them](https://clerk.com/docs/backend-requests/custom-session-token). End-users who are authenticated should have the `authenticated` value for the claim. If you have an advanced Postgres setup where authenticated end-users use different Postgres roles to access the database, adjust the value to use the correct role name.
2.  Once all Clerk session tokens for your instance contain the `role` claim, add a [new Third-Party Auth integration with Clerk](/dashboard/project/_/auth/third-party) in the Supabase dashboard or register it in the CLI as instructed above.

## Setup the Supabase client library[#](#setup-the-supabase-client-library)

```
1const supabaseClient = createClient(2    process.env.NEXT_PUBLIC_SUPABASE_URL!,3    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,4    {5      // Session accessed from Clerk SDK, either as Clerk.session (vanilla6      // JavaScript) or useSession (React)7      accessToken: async () => session?.getToken() ?? null,8    }9  )
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/clerk/hooks/useSupabaseClient.ts)

## Using RLS policies[#](#using-rls-policies)

Once you've configured the Supabase client library to use Clerk session tokens, you can use RLS policies to secure access to your project's database, Storage objects and Realtime channels.

The recommended way to design RLS policies with Clerk is to use claims present in your Clerk session token to allow or reject access to your project's data. Check [Clerk's docs](https://clerk.com/docs/backend-requests/resources/session-tokens) on the available JWT claims and their values.

### Example: Check user organization role[#](#example-check-user-organization-role)

```
1create policy "Only organization admins can insert in table"2on secured_table3for insert4to authenticated5with check (6  (((select auth.jwt()->>'org_role') = 'org:admin') or ((select auth.jwt()->'o'->>'rol') = 'admin'))7    and8  (organization_id = (select coalesce(auth.jwt()->>'org_id', auth.jwt()->'o'->>'id')))9);
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/clerk/supabase/migrations/20250501155648_setup_database.sql)

This RLS policy checks that the newly inserted row in the table has the user's declared organization ID in the `organization_id` column. Additionally it ensures that they're an `org:admin`.

This way only organization admins can add rows to the table, for organizations they're a member of.

### Example: Check user has passed second factor verification[#](#example-check-user-has-passed-second-factor-verification)

```
1create policy "Only users that have passed second factor verification can read from table"2on secured_table3as restrictive4for select5to authenticated6using (7  ((select auth.jwt()->'fva'->>1) != '-1')8);
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/clerk/supabase/migrations/20250501155648_setup_database.sql)

This example uses a restrictive RLS policy checks that the [second factor verification](https://clerk.com/docs/guides/reverification) age element in the `fva` claim is not `'-1'` indicating the user has passed through second factor verification.

## Deprecated integration with JWT templates[#](#deprecated-integration-with-jwt-templates)

As of 1st April 2025 the previously available [Clerk Integration with Supabase](/partners/integrations/clerk) is considered deprecated and is no longer recommended for use. All projects using the deprecated integration will be excluded from Third-Party Monthly Active User (TP-MAU) charges until at least 1st January 2026.

This integration used low-level primitives that are still available in Supabase and Clerk, such as a [configurable JWT secret](/dashboard/project/_/settings/api) and [JWT templates from Clerk](https://clerk.com/docs/backend-requests/jwt-templates). This enables you to keep using it in an unofficial manner, though only limited support will be provided from Supabase.

Deprecation is done for the following reasons:

*   Sharing your project's JWT secret with a third-party is a problematic security practice
*   Rotating the project's JWT secret in this case almost always results in significant downtime for your application
*   Additional latency to [generate a new JWT](https://clerk.com/docs/backend-requests/jwt-templates#generate-a-jwt) for use with Supabase, instead of using the Clerk [session tokens](https://clerk.com/docs/backend-requests/resources/session-tokens)
