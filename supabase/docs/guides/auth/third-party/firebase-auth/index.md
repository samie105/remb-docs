---
title: "Firebase Auth"
source: "https://supabase.com/docs/guides/auth/third-party/firebase-auth"
canonical_url: "https://supabase.com/docs/guides/auth/third-party/firebase-auth"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:16.496Z"
content_hash: "907c277729a6be95c5631c4257639765e13ae23216da369a1c735d157d68a634"
menu_path: ["Auth","Auth","Third-party auth","Third-party auth","Firebase Auth","Firebase Auth"]
section_path: ["Auth","Auth","Third-party auth","Third-party auth","Firebase Auth","Firebase Auth"]
nav_prev: {"path": "../clerk/index.md", "title": "Clerk"}
nav_next: {"path": "../overview/index.md", "title": "Third-party auth"}
---

# 

Firebase Auth

## 

Use Firebase Auth with your Supabase project

* * *

Firebase Auth can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.

## Getting started[#](#getting-started)

1.  First you need to add an integration to connect your Supabase project with your Firebase project. You will need to get the Project ID in the [Firebase Console](https://console.firebase.google.com/u/0/project/_/settings/general).
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party).
3.  If you are using Third Party Auth when self hosting, create and attach restrictive RLS policies to all tables in your public schema, Storage and Realtime to **prevent unauthorized access from unrelated Firebase projects**.
4.  Assign the `role: 'authenticated'` [custom user claim](https://firebase.google.com/docs/auth/admin/custom-claims) to all your users.
5.  Finally set up the Supabase client in your application.

## Setup the Supabase client library[#](#setup-the-supabase-client-library)

Creating a client for the Web is as easy as passing the `accessToken` async function. This function should [return the Firebase Auth JWT of the current user](https://firebase.google.com/docs/auth/admin/verify-id-tokens#web) (or null if no such user) is found.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient(4  'https://<supabase-project>.supabase.co',5  'SUPABASE_PUBLISHABLE_KEY',6  {7    accessToken: async () => {8      return (await firebase.auth().currentUser?.getIdToken(/* forceRefresh */ false)) ?? null9    },10  }11)
```

Make sure all users in your application have the `role: 'authenticated'` [custom claim](https://firebase.google.com/docs/auth/admin/custom-claims) set. If you're using the `onCreate` Cloud Function to add this custom claim to newly signed up users, you will need to call `getIdToken(/* forceRefresh */ true)` immediately after sign up as the `onCreate` function does not run synchronously.

## Add a new Third-Party Auth integration to your project[#](#add-a-new-third-party-auth-integration-to-your-project)

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

In the CLI add the following config to your `supabase/config.toml` file:

```
1[auth.third_party.firebase]2enabled = true3project_id = "<id>"
```

## Adding an extra layer of security to your project's RLS policies (self-hosting only)[#](#adding-an-extra-layer-of-security-to-your-projects-rls-policies-self-hosting-only)

**Follow this section carefully to prevent unauthorized access to your project's data when self-hosting.**

When using the Supabase hosted platform, following this step is optional.

Firebase Auth uses a single set of JWT signing keys for all projects. This means that JWTs issued from an unrelated Firebase project to yours could access data in your Supabase project.

When using the Supabase hosted platform, JWTs coming from Firebase project IDs you have not registered will be rejected before they reach your database. When self-hosting implementing this mechanism is your responsibility. An easy way to guard against this is to create and maintain the following RLS policies for **all of your tables in the `public` schema**. You should also attach this policy to [Storage](/docs/guides/storage/security/access-control) buckets or [Realtime](/docs/guides/realtime/authorization) channels.

It's recommended you use a [restrictive Postgres Row-Level Security policy](https://www.postgresql.org/docs/current/sql-createpolicy.html).

Restrictive RLS policies differ from regular (or permissive) policies in that they use the `as restrictive` clause when being defined. They do not grant permissions, but rather restrict any existing or future permissions. They're great for cases like this where the technical limitations of Firebase Auth remain separate from your app's logic.

Postgres has two types of policies: permissive and restrictive. This example uses restrictive policies so make sure you don't omit the `as restrictive` clause.

This is an example of such an RLS policy that will restrict access to only your project's (denoted with `<firebase-project-id>`) users, and not any other Firebase project.

```
1create policy "Restrict access to Supabase Auth and Firebase Auth for project ID <firebase-project-id>"2  on table_name3  as restrictive4  to authenticated5  using (6    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')7    or8    (9        auth.jwt()->>'iss' = 'https://securetoken.google.com/<firebase-project-id>'10        and11        auth.jwt()->>'aud' = '<firebase-project-id>'12     )13  );
```

If you have a lot of tables in your app, or need to manage complex RLS policies for [Storage](/docs/guides/storage) or [Realtime](/docs/guides/realtime) it can be useful to define a [stable Postgres function](https://www.postgresql.org/docs/current/xfunc-volatility.html) that performs the check to cut down on duplicate code. For example:

```
1create function public.is_supabase_or_firebase_project_jwt()2  returns bool3  language sql4  stable5  returns null on null input6  return (7    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')8    or9    (10        auth.jwt()->>'iss' = concat('https://securetoken.google.com/<firebase-project-id>')11        and12        auth.jwt()->>'aud' = '<firebase-project-id>'13     )14  );
```

Make sure you substitute `<project-ref>` with your Supabase project's ID and the `<firebase-project-id>` to your Firebase Project ID. Then the restrictive policies on all your tables, buckets and channels can be simplified to be:

```
1create policy "Restrict access to correct Supabase and Firebase projects"2  on table_name3  as restrictive4  to authenticated5  using ((select public.is_supabase_or_firebase_project_jwt()) is true);
```

## Assign the "role" custom claim[#](#assign-the-role-custom-claim)

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

By default, Firebase JWTs do not contain a `role` claim in them. If you were to send such a JWT to your Supabase project, the `anon` role would be assigned when executing the Postgres query. Most of your app's logic will be accessible by the `authenticated` role.

### Use Firebase Authentication functions to assign the authenticated role[#](#use-firebase-authentication-functions-to-assign-the-authenticated-role)

You have two choices to set up a Firebase Authentication function depending on your Firebase project's configuration:

1.  Easiest: Use a [blocking Firebase Authentication function](https://firebase.google.com/docs/auth/extend-with-blocking-functions) but this is only available if your project uses [Firebase Authentication with Identity Platform](https://cloud.google.com/security/products/identity-platform).
2.  Manually assign the custom claims to all users with the [admin SDK](https://firebase.google.com/docs/auth/admin/custom-claims#set_and_validate_custom_user_claims_via_the_admin_sdk) and define an [`onCreate` Firebase Authentication Cloud Function](https://firebase.google.com/docs/auth/extend-with-functions) to persist the role to all newly created users.

```
1import { beforeUserCreated, beforeUserSignedIn } from 'firebase-functions/v2/identity'23export const beforecreated = beforeUserCreated((event) => {4  return {5    customClaims: {6      // The Supabase project will use this role to assign the `authenticated`7      // Postgres role.8      role: 'authenticated',9    },10  }11})1213export const beforesignedin = beforeUserSignedIn((event) => {14  return {15    customClaims: {16      // The Supabase project will use this role to assign the `authenticated`17      // Postgres role.18      role: 'authenticated',19    },20  }21})
```

Note that instead of using `customClaims` you can instead use `sessionClaims`. The difference is that `session_claims` are not saved in the Firebase user profile, but remain valid for as long as the user is signed in.

Finally deploy your functions for the changes to take effect:

```
1firebase deploy --only functions
```

Note that these functions are only called on new sign-ups and sign-ins. Existing users will not have these claims in their ID tokens. You will need to use the admin SDK to assign the role custom claim to all users. Make sure you do this after the blocking Firebase Authentication functions as described above are deployed.

### Use the admin SDK to assign the role custom claim to all users[#](#use-the-admin-sdk-to-assign-the-role-custom-claim-to-all-users)

You need to run a script that will assign the `role: 'authenticated'` custom claim to all of your existing Firebase Authentication users. You can do this by combining the [list users](https://firebase.google.com/docs/auth/admin/manage-users#list_all_users) and [set custom user claims](https://firebase.google.com/docs/auth/admin/create-custom-tokens) admin APIs. An example script is provided below:

```
1'use strict';2const { initializeApp } = require('firebase-admin/app');3const { getAuth } = require('firebase-admin/auth');4initializeApp();56async function setRoleCustomClaim() => {7  let nextPageToken = undefined89  do {10    const listUsersResult = await getAuth().listUsers(1000, nextPageToken)1112    nextPageToken = listUsersResult.pageToken1314    await Promise.all(listUsersResult.users.map(async (userRecord) => {15      try {16        await getAuth().setCustomUserClaims(userRecord.id, {17          role: 'authenticated'18        })19      } catch (error) {20        console.error('Failed to set custom role for user', userRecord.id)21      }22    })23  } while (nextPageToken);24};2526setRoleCustomClaim().then(() => process.exit(0))
```

After all users have received the `role: 'authenticated'` claim, it will appear in all newly issued ID tokens for the user.
