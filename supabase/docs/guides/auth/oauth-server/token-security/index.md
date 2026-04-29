---
title: "Token Security and Row Level Security"
source: "https://supabase.com/docs/guides/auth/oauth-server/token-security"
canonical_url: "https://supabase.com/docs/guides/auth/oauth-server/token-security"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:29.960Z"
content_hash: "49a772e74ed4b195b58e4724822ad68d8d160bb9e12c2e2027b13757f164bccc"
menu_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Token Security & RLS","Token Security & RLS"]
section_path: ["Auth","Auth","OAuth 2.1 Server","OAuth 2.1 Server","Token Security & RLS","Token Security & RLS"]
nav_prev: {"path": "supabase/docs/guides/auth/oauth-server/oauth-flows/index.md", "title": "OAuth 2.1 Flows"}
nav_next: {"path": "supabase/docs/guides/auth/password-security/index.md", "title": "Password security"}
---

# 

Token Security and Row Level Security

* * *

When you enable OAuth 2.1 in your Supabase project, third-party applications can access user data on their behalf. Row Level Security (RLS) policies are crucial for controlling exactly what data each OAuth client can access.

**Scopes control OIDC data, not database access**

The OAuth scopes (`openid`, `email`, `profile`, `phone`) control what user information is included in ID tokens and returned by the UserInfo endpoint. They do **not** control access to your database tables or API endpoints.

Use RLS to define which OAuth clients can access which data, regardless of the scopes they requested.

## How OAuth tokens work with RLS[#](#how-oauth-tokens-work-with-rls)

OAuth access tokens issued by Supabase Auth are JWTs that include all standard Supabase claims plus OAuth-specific claims. This means your existing RLS policies continue to work, and you can add OAuth-specific logic to create granular access controls.

### Token structure[#](#token-structure)

Every OAuth access token includes:

```
1{2  "sub": "user-uuid",3  "role": "authenticated",4  "aud": "authenticated",5  "user_id": "user-uuid",6  "email": "user@example.com",7  "client_id": "9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d",8  "aal": "aal1",9  "amr": [{ "method": "password", "timestamp": 1735815600 }],10  "session_id": "session-uuid",11  "iss": "https://<project-ref>.supabase.co/auth/v1",12  "iat": 1735815600,13  "exp": 173581920014}
```

The key OAuth-specific claim is:

Claim

Description

`client_id`

Unique identifier of the OAuth client that obtained this token

You can use this claim in RLS policies to grant different permissions to different clients.

## Extracting OAuth claims in RLS[#](#extracting-oauth-claims-in-rls)

Use the `auth.jwt()` function to access token claims in your policies:

```
1-- Get the client ID from the token2(auth.jwt() ->> 'client_id')34-- Check if the token is from an OAuth client5(auth.jwt() ->> 'client_id') IS NOT NULL67-- Check if the token is from a specific client8(auth.jwt() ->> 'client_id') = 'mobile-app-client-id'
```

## Common RLS patterns for OAuth[#](#common-rls-patterns-for-oauth)

### Pattern 1: Grant specific client full access[#](#pattern-1-grant-specific-client-full-access)

Allow a specific OAuth client to access all user data:

```
1CREATE POLICY "Mobile app can access user data"2ON user_data FOR ALL3USING (4  auth.uid() = user_id AND5  (auth.jwt() ->> 'client_id') = 'mobile-app-client-id'6);
```

### Pattern 2: Grant multiple clients read-only access[#](#pattern-2-grant-multiple-clients-read-only-access)

Allow several OAuth clients to read data, but not modify it:

```
1CREATE POLICY "Third-party apps can read profiles"2ON profiles FOR SELECT3USING (4  auth.uid() = user_id AND5  (auth.jwt() ->> 'client_id') IN (6    'analytics-client-id',7    'reporting-client-id',8    'dashboard-client-id'9  )10);
```

### Pattern 3: Restrict sensitive data from OAuth clients[#](#pattern-3-restrict-sensitive-data-from-oauth-clients)

Prevent OAuth clients from accessing sensitive data:

```
1CREATE POLICY "OAuth clients cannot access payment info"2ON payment_methods FOR ALL3USING (4  auth.uid() = user_id AND5  (auth.jwt() ->> 'client_id') IS NULL  -- Only direct user sessions6);
```

### Pattern 4: Client-specific data access[#](#pattern-4-client-specific-data-access)

Different clients access different subsets of data:

```
1-- Analytics client can only read aggregated data2CREATE POLICY "Analytics client reads summaries"3ON user_metrics FOR SELECT4USING (5  auth.uid() = user_id AND6  (auth.jwt() ->> 'client_id') = 'analytics-client-id'7);89-- Admin client can read and modify all data10CREATE POLICY "Admin client full access"11ON user_data FOR ALL12USING (13  auth.uid() = user_id AND14  (auth.jwt() ->> 'client_id') = 'admin-client-id'15);
```

## Real-world examples[#](#real-world-examples)

### Example 1: Multi-platform application[#](#example-1-multi-platform-application)

You have a web app, mobile app, and third-party integrations:

```
1-- Web app: Full access2CREATE POLICY "Web app full access"3ON profiles FOR ALL4USING (5  auth.uid() = user_id AND6  (7    (auth.jwt() ->> 'client_id') = 'web-app-client-id'8    OR (auth.jwt() ->> 'client_id') IS NULL  -- Direct user sessions9  )10);1112-- Mobile app: Read-only access to profiles13CREATE POLICY "Mobile app reads profiles"14ON profiles FOR SELECT15USING (16  auth.uid() = user_id AND17  (auth.jwt() ->> 'client_id') = 'mobile-app-client-id'18);1920-- Third-party integration: Limited data access21CREATE POLICY "Integration reads public data"22ON profiles FOR SELECT23USING (24  auth.uid() = user_id AND25  (auth.jwt() ->> 'client_id') = 'integration-client-id' AND26  is_public = true27);
```

## Custom access token hooks[#](#custom-access-token-hooks)

[Custom Access Token Hooks](../../auth-hooks/custom-access-token-hook/index.md) work with OAuth tokens, allowing you to inject custom claims based on the OAuth client. This is particularly useful for customizing standard JWT claims like `audience` (`aud`) or adding client-specific metadata.

Custom Access Token Hooks are triggered for **all** token issuance. Use `client_id` or `authentication_method` (`oauth_provider/authorization_code` for OAuth flows) to differentiate OAuth from regular authentication.

### Customizing the audience claim[#](#customizing-the-audience-claim)

A common use case is customizing the `audience` claim for different OAuth clients. This allows third-party services to validate that tokens were issued specifically for them:

```
1import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'23serve(async (req) => {4  const { user, claims, client_id } = await req.json()56  // Customize audience based on OAuth client7  if (client_id === 'mobile-app-client-id') {8    return new Response(9      JSON.stringify({10        claims: {11          aud: 'https://api.myapp.com',12          app_version: '2.0.0',13        },14      }),15      { headers: { 'Content-Type': 'application/json' } }16    )17  }1819  if (client_id === 'analytics-partner-id') {20    return new Response(21      JSON.stringify({22        claims: {23          aud: 'https://analytics.partner.com',24          access_level: 'read-only',25        },26      }),27      { headers: { 'Content-Type': 'application/json' } }28    )29  }3031  // Default audience for non-OAuth flows32  return new Response(JSON.stringify({ claims: {} }), {33    headers: { 'Content-Type': 'application/json' },34  })35})
```

The `audience` claim is especially important for:

*   **JWT validation by third parties**: Services can verify tokens were issued for their specific API
*   **Multi-tenant applications**: Different audiences for different client applications
*   **Compliance**: Meeting security requirements that mandate audience validation

### Adding client-specific claims[#](#adding-client-specific-claims)

You can also add custom claims and metadata based on the OAuth client:

```
1import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'2import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'34serve(async (req) => {5  const { user, claims, client_id } = await req.json()67  const supabase = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SECRET_KEY')!)89  // Add custom claims based on OAuth client10  let customClaims = {}1112  if (client_id === 'mobile-app-client-id') {13    customClaims.aud = 'https://mobile.myapp.com'14    customClaims.app_version = '2.0.0'15    customClaims.platform = 'mobile'16  } else if (client_id === 'analytics-client-id') {17    customClaims.aud = 'https://analytics.myapp.com'18    customClaims.read_only = true19    customClaims.data_retention_days = 9020  } else if (client_id?.startsWith('mcp-')) {21    // MCP AI agents22    const { data: agent } = await supabase23      .from('approved_ai_agents')24      .select('name, max_data_retention_days')25      .eq('client_id', client_id)26      .single()2728    customClaims.aud = `https://mcp.myapp.com/${client_id}`29    customClaims.ai_agent = true30    customClaims.agent_name = agent?.name31    customClaims.max_retention = agent?.max_data_retention_days32  }3334  return new Response(JSON.stringify({ claims: customClaims }), {35    headers: { 'Content-Type': 'application/json' },36  })37})
```

Use these custom claims in RLS:

```
1-- Policy based on custom claims2CREATE POLICY "Read-only clients cannot modify"3ON user_data FOR UPDATE4USING (5  auth.uid() = user_id AND6  (auth.jwt() -> 'user_metadata' ->> 'read_only')::boolean IS NOT TRUE7);89-- Policy based on audience claim10CREATE POLICY "Only specific audience can access"11ON api_data FOR SELECT12USING (13  auth.uid() = user_id AND14  (auth.jwt() ->> 'aud') IN (15    'https://api.myapp.com',16    'https://mobile.myapp.com'17  )18);
```

## Security best practices[#](#security-best-practices)

### 1\. Principle of least privilege[#](#1-principle-of-least-privilege)

Grant OAuth clients only the minimum permissions they need:

```
1-- Bad: Grant all access by default2CREATE POLICY "OAuth clients full access"3ON user_data FOR ALL4USING (auth.uid() = user_id);56-- Good: Grant specific access per client7CREATE POLICY "Specific client specific access"8ON user_data FOR SELECT9USING (10  auth.uid() = user_id AND11  (auth.jwt() ->> 'client_id') = 'trusted-client-id'12);
```

### 2\. Separate policies for OAuth clients[#](#2-separate-policies-for-oauth-clients)

Create dedicated policies for OAuth clients rather than mixing them with user policies:

```
1-- User access2CREATE POLICY "Users access their own data"3ON user_data FOR ALL4USING (5  auth.uid() = user_id AND6  (auth.jwt() ->> 'client_id') IS NULL7);89-- OAuth client access (separate policy)10CREATE POLICY "OAuth clients limited access"11ON user_data FOR SELECT12USING (13  auth.uid() = user_id AND14  (auth.jwt() ->> 'client_id') IN ('client-1', 'client-2')15);
```

### 3\. Regularly audit OAuth clients[#](#3-regularly-audit-oauth-clients)

Track and review which clients have access:

```
1-- View all active OAuth clients2SELECT3  oc.client_id,4  oc.name,5  oc.created_at,6  COUNT(DISTINCT s.user_id) as active_users7FROM auth.oauth_clients oc8LEFT JOIN auth.sessions s ON s.client_id = oc.client_id9WHERE s.created_at > NOW() - INTERVAL '30 days'10GROUP BY oc.client_id, oc.name, oc.created_at;
```

## Testing your policies[#](#testing-your-policies)

Always test your RLS policies before deploying to production:

```
1-- Test as a specific OAuth client2SET request.jwt.claims = '{3  "sub": "test-user-uuid",4  "role": "authenticated",5  "client_id": "test-client-id"6}';78-- Test queries9SELECT * FROM user_data WHERE user_id = 'test-user-uuid';1011-- Reset12RESET request.jwt.claims;
```

Or use the Supabase Dashboard's [RLS policy tester](/dashboard/project/_/auth/policies).

## Troubleshooting[#](#troubleshooting)

### Policy not working for OAuth client[#](#policy-not-working-for-oauth-client)

**Problem**: OAuth client can't access data despite having a valid token.

**Check**:

1.  Verify the policy includes the client's `client_id`
2.  Ensure RLS is enabled on the table
3.  Check for conflicting restrictive policies
4.  Test with secret key to isolate RLS issues

```
1-- Debug: See what client_id is in the token2SELECT auth.jwt() ->> 'client_id';34-- Debug: Test without RLS5SET LOCAL role = service_role;6SELECT * FROM your_table;
```

### Policy too permissive[#](#policy-too-permissive)

**Problem**: OAuth client has access to data it shouldn't.

**Solution**: Use `AS RESTRICTIVE` policies to add additional constraints:

```
1-- This policy runs in addition to permissive policies2CREATE POLICY "Restrict OAuth clients"3ON sensitive_data4AS RESTRICTIVE5FOR ALL6TO authenticated7USING (8  -- OAuth clients cannot access this table at all9  (auth.jwt() ->> 'client_id') IS NULL10);
```

### Can't differentiate between users and OAuth clients[#](#cant-differentiate-between-users-and-oauth-clients)

**Problem**: Need to apply different logic for direct user sessions vs OAuth.

**Solution**: Check if `client_id` is present:

```
1-- Direct user sessions (no OAuth)2CREATE POLICY "Direct users full access"3ON user_data FOR ALL4USING (5  auth.uid() = user_id AND6  (auth.jwt() ->> 'client_id') IS NULL7);89-- OAuth clients (limited access)10CREATE POLICY "OAuth clients read only"11ON user_data FOR SELECT12USING (13  auth.uid() = user_id AND14  (auth.jwt() ->> 'client_id') IS NOT NULL15);
```

## Next steps[#](#next-steps)

*   [Learn about JWTs](../../jwts/index.md) - Deep dive into Supabase token structure
*   [Row Level Security](/docs/guides/auth/row-level-security) - Complete RLS guide
*   [Custom Access Token Hooks](../../auth-hooks/custom-access-token-hook/index.md) - Inject custom claims
*   [OAuth flows](../oauth-flows/index.md) - Understand token issuance
