---
title: "Amazon Cognito (Amplify)"
source: "https://supabase.com/docs/guides/auth/third-party/aws-cognito"
canonical_url: "https://supabase.com/docs/guides/auth/third-party/aws-cognito"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:05.749Z"
content_hash: "b3aadcf89c42c059d3e0a7f411810911158d0ea97d3112927e4980bb9bb4f85b"
menu_path: ["Auth","Auth","Third-party auth","Third-party auth","AWS Cognito (Amplify)","AWS Cognito (Amplify)"]
section_path: ["Auth","Auth","Third-party auth","Third-party auth","AWS Cognito (Amplify)","AWS Cognito (Amplify)"]
nav_prev: {"path": "supabase/docs/guides/auth/social-login/auth-zoom/index.md", "title": "Login with Zoom"}
nav_next: {"path": "supabase/docs/guides/auth/third-party/auth0/index.md", "title": "Auth0"}
---

# 

Amazon Cognito (Amplify)

## 

Use Amazon Cognito via Amplify or standalone with your Supabase project

* * *

Amazon Cognito User Pools (via AWS Amplify or on its own) can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.

## Getting started[#](#getting-started)

1.  First you need to add an integration to connect your Supabase project with your Amazon Cognito User Pool. You will need the pool's ID and region.
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party) or configure it in the CLI.
3.  Assign the `role: 'authenticated'` custom claim to all JWTs by using a Pre-Token Generation Trigger.
4.  Finally setup the Supabase client in your application.

## Setup the Supabase client library[#](#setup-the-supabase-client-library)

```
1import { fetchAuthSession, Hub } from 'aws-amplify/auth'23const supabase = createClient(4  'https://<supabase-project>.supabase.co',5  'SUPABASE_PUBLISHABLE_KEY',6  {7    accessToken: async () => {8      const tokens = await fetchAuthSession()910      // Alternatively you can use tokens?.idToken instead.11      return tokens?.accessToken12    },13  }14)1516// if you're using Realtime you also need to set up a listener for Cognito auth changes17Hub.listen('auth', () => {18  fetchAuthSession().then((tokens) => supabase.realtime.setAuth(tokens?.accessToken))19})
```

## Add a new Third-Party Auth integration to your project[#](#add-a-new-third-party-auth-integration-to-your-project)

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

In the CLI add the following config to your `supabase/config.toml` file:

```
1[auth.third_party.aws_cognito]2enabled = true3user_pool_id = "<id>"4user_pool_region = "<region>"
```

## Use a pre-token generation trigger to assign the authenticated role[#](#use-a-pre-token-generation-trigger-to-assign-the-authenticated-role)

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

By default, Amazon Cognito JWTs (both ID token and access tokens) do not contain a `role` claim in them. If you were to send such a JWT to your Supabase project, the `anon` role would be assigned when executing the Postgres query. Most of your app's logic will be accessible by the `authenticated` role.

A recommended approach to do this is to configure a [Pre-Token Generation Trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) either `V1_0` (ID token only) or `V2_0` (both access and ID token). To do this you will need to create a new Lambda function (in any language and runtime) and assign it to the [Amazon Cognito User Pool's Lambda Triggers configuration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html). For example, the Lambda function should look similar to this:

```
1export const handler = async (event) => {2  event.response = {3    claimsOverrideDetails: {4      claimsToAddOrOverride: {5        role: 'authenticated',6      },7    },8  }910  return event11}
```
