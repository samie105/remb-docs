---
title: "WorkOS"
source: "https://supabase.com/docs/guides/auth/third-party/workos"
canonical_url: "https://supabase.com/docs/guides/auth/third-party/workos"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:15.823Z"
content_hash: "f2c89900cc4ded373ab87daa8c099f59d424c6ed9c8d6675d3f9f62d59a85095"
menu_path: ["Auth","Auth","Third-party auth","Third-party auth","WorkOS","WorkOS"]
section_path: ["Auth","Auth","Third-party auth","Third-party auth","WorkOS","WorkOS"]
nav_prev: {"path": "supabase/docs/guides/auth/third-party/overview/index.md", "title": "Third-party auth"}
nav_next: {"path": "supabase/docs/guides/auth/users/index.md", "title": "Users"}
---

# 

WorkOS

## 

Use WorkOS with your Supabase project

* * *

WorkOS can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.

## Getting started[#](#getting-started)

1.  First you need to add an integration to connect your Supabase project with your WorkOS tenant. You will need your WorkOS issuer. The issuer is `https://api.workos.com/user_management/<your-client-id>`. Substitute your [custom auth domain](https://workos.com/docs/custom-domains/auth-api) for "api.workos.com" if configured.
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party).
3.  Set up a JWT template to assign the `role: 'authenticated'` claim to your access token.

## Setup the Supabase client library[#](#setup-the-supabase-client-library)

```
1import { createClient } from '@supabase/supabase-js'2import { createClient as createAuthKitClient } from '@workos-inc/authkit-js'34const authkit = await createAuthKitClient('WORKOS_CLIENT_ID', {5  apiHostname: '<WORKOS_AUTH_DOMAIN>',6})78const supabase = createClient(9  'https://<supabase-project>.supabase.co',10  'SUPABASE_PUBLISHABLE_KEY',11  {12    accessToken: async () => {13      return authkit.getAccessToken()14    },15  }16)
```

## Add a new Third-Party Auth integration to your project[#](#add-a-new-third-party-auth-integration-to-your-project)

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

## Set up a JWT template to add the authenticated role.[#](#set-up-a-jwt-template-to-add-the-authenticated-role)

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

WorkOS JWTs already contain a `role` claim that corresponds to the user's role in their organization. It is necessary to adjust the `role` claim to be `"authenticated"` like Supabase expects. This can be done using JWT templates (navigate to Authentication -> Sessions -> JWT Template in the WorkOS Dashboard).

This template overrides the `role` claim to meet Supabase's expectations, and adds the WorkOS role in a new `user_role` claim:

```
1{2  "role": "authenticated",3  "user_role": {{organization_membership.role}}4}
```
