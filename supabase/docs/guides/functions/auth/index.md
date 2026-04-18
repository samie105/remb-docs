---
title: "Securing Edge Functions"
source: "https://supabase.com/docs/guides/functions/auth"
canonical_url: "https://supabase.com/docs/guides/functions/auth"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:43.454Z"
content_hash: "ef5c002275ddf9889b09275c338cd5a0e56a6c4d0ac5781c9eae73e989190c78"
menu_path: ["Edge Functions","Edge Functions","More","More","More","Supabase Auth","Supabase Auth","Securing your functions","Securing your functions"]
section_path: ["Edge Functions","Edge Functions","More","More","More","Supabase Auth","Supabase Auth","Securing your functions","Securing your functions"]
nav_prev: {"path": "supabase/docs/guides/functions/ai-models/index.md", "title": "Running AI Models"}
nav_next: {"path": "supabase/docs/guides/functions/background-tasks/index.md", "title": "Background Tasks"}
---

# 

Securing Edge Functions

## 

Best practices on securing Edge Functions

* * *

In the past Supabase Auth used a **symmetric** secret to sign legacy JWTs. But it was replaced by new [JWT Signing Keys](/blog/jwt-signing-keys#start-using-asymmetric-jwts-today). This guide covers the new patterns for securing your Edge Functions.

If you need to validate using the old method, read the [Legacy JWT Secret guide](/docs/guides/functions/auth-legacy-jwt).

Before continuing, read the [JWT Signing Keys guide](/docs/guides/auth/signing-keys) for details about the main differences compared to Legacy JWTs.

## Overview[#](#overview)

When an HTTP request is sent to Edge Functions, you can use Supabase Auth to secure endpoints. In the past, this verification was controlled by the [`verify_jwt` flag](/docs/guides/functions/function-configuration#skipping-authorization-checks).

But, this method is incompatible with the new [JWT Signing Keys](/docs/guides/auth/signing-keys) and also caused trouble when attempting [third-party integration](https://github.com/orgs/supabase/discussions/34988#discussion-8199151).

For this reason we decided to no longer implicitly force JWT verification, but instead suggest patterns and templates to handle this task. This allows users to own and control the auth code, instead of hiding it internally under Edge Runtime infrastructure.

Following the [upcoming API key changes](https://github.com/orgs/supabase/discussions/29260) timetable, the `verify_jwt` flag will still be supported and enabled by default. To move to the new [JWT Signing Keys](/docs/guides/auth/signing-keys), you need to manually [skip the authorization checks](/docs/guides/functions/function-configuration#skipping-authorization-checks) and follow the steps below.

## Integrating with Supabase Auth[#](#integrating-with-supabase-auth)

Important notes to consider:

*   This is done _inside_ the `Deno.serve()` callback argument, so that the Authorization header is set for each request.
*   Use `Deno.env.get('SUPABASE_URL')` to get the URL associated with your project. Using a value such as `http://localhost:54321` for local development will fail due to Docker containerization.

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

Currently, the new API keys are not available by default on the Edge Functions environment. But you can manually expose them as [secret](/docs/guides/functions/secrets#local-secrets) using the `SB_` prefix.

We're working on exposing these secrets and making them default in the future.

```
1import 'jsr:@supabase/functions-js/edge-runtime.d.ts'2import { createClient } from 'npm:@supabase/supabase-js@2'34const supabase = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SB_PUBLISHABLE_KEY')!)56Deno.serve(async (req) => {7  const authHeader = req.headers.get('Authorization')!8  const token = authHeader.replace('Bearer ', '')910  const { data, error } = await supabase.auth.getClaims(token)11  const userEmail = data?.claims?.email12  if (!userEmail || error) {13    return Response.json(14      { msg: 'Invalid JWT' },15      {16        status: 401,17      }18    )19  }2021  return Response.json({ message: `hello ${userEmail}` })22})
```

## Verifying JWT[#](#verifying-jwt)

### Using Supabase template[#](#using-supabase-template)

You can see [a custom JWT verification example on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/custom-jwt-validation) and a variety of [auth function templates](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/_shared/jwt) also on GitHub.

To verify incoming requests, you can copy/download the specified template and start using it:

The following example uses [`jose`](https://jsr.io/@panva/jose) library to verify received JWTs.

###### \_shared/jwt/default.ts

```
1// ...23import * as jose from 'jsr:@panva/jose@6'45const SUPABASE_JWT_ISSUER =6  Deno.env.get('SB_JWT_ISSUER') ?? Deno.env.get('SUPABASE_URL') + '/auth/v1'78const SUPABASE_JWT_KEYS = jose.createRemoteJWKSet(9  new URL(Deno.env.get('SUPABASE_URL')! + '/auth/v1/.well-known/jwks.json')10)1112function getAuthToken(req: Request) {13  const authHeader = req.headers.get('authorization')14  if (!authHeader) {15    throw new Error('Missing authorization header')16  }17  const [bearer, token] = authHeader.split(' ')18  if (bearer !== 'Bearer') {19    throw new Error(`Auth header is not 'Bearer {token}'`)20  }2122  return token23}2425function verifySupabaseJWT(jwt: string) {26  return jose.jwtVerify(jwt, SUPABASE_JWT_KEYS, {27    issuer: SUPABASE_JWT_ISSUER,28  })29}3031// Validates authorization header32export async function AuthMiddleware(req: Request, next: (req: Request) => Promise<Response>) {33  if (req.method === 'OPTIONS') return await next(req)3435  try {36    const token = getAuthToken(req)37    const isValidJWT = await verifySupabaseJWT(token)3839    if (isValidJWT) return await next(req)4041    return Response.json(42      { msg: 'Invalid JWT' },43      {44        status: 401,45      }46    )47  } catch (e) {48    return Response.json(49      { msg: e?.toString() },50      {51        status: 401,52      }53    )54  }55}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/_shared/jwt/default.ts)

###### hello/index.ts

```
1// ...23import { AuthMiddleware } from '../_shared/jwt/default.ts'45interface reqPayload {6  name: string7}89Deno.serve((r) =>10  AuthMiddleware(r, async (req) => {11    const { name }: reqPayload = await req.json()12    const data = {13      message: `Hello ${name} from foo!`,14    }1516    return Response.json(data)17  })18)
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/custom-jwt-validation/index.ts)


