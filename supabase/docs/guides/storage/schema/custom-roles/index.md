---
title: "Custom Roles"
source: "https://supabase.com/docs/guides/storage/schema/custom-roles"
canonical_url: "https://supabase.com/docs/guides/storage/schema/custom-roles"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:27.977Z"
content_hash: "b4248c83374013ce32d5e7123ae0140039510d8cd1cc53cb7197a541fd93613b"
menu_path: ["Storage","Storage","More","More","More","Schema","Schema","Custom Roles","Custom Roles"]
section_path: ["Storage","Storage","More","More","More","Schema","Schema","Custom Roles","Custom Roles"]
nav_prev: {"path": "supabase/docs/guides/storage/s3/compatibility/index.md", "title": "S3 Compatibility"}
nav_next: {"path": "supabase/docs/guides/storage/schema/design/index.md", "title": "The Storage Schema"}
---

# 

Custom Roles

## 

Learn about using custom roles with storage schema

* * *

In this guide, you will learn how to create and use custom roles with Storage to manage role-based access to objects and buckets. The same approach can be used to use custom roles with any other Supabase service.

Supabase Storage uses the same role-based access control system as any other Supabase service using RLS (Row Level Security).

## Create a custom role[#](#create-a-custom-role)

Let's create a custom role `manager` to provide full read access to a specific bucket. For a more advanced setup, see the [RBAC Guide](/docs/guides/api/custom-claims-and-role-based-access-control-rbac#create-auth-hook-to-apply-user-role).

```
1create role 'manager';23-- Important to grant the role to the authenticator and anon role4grant manager to authenticator;5grant anon to manager;
```

## Create a policy[#](#create-a-policy)

Let's create a policy that gives full read permissions to all objects in the bucket `teams` for the `manager` role.

```
1create policy "Manager can view all files in the bucket 'teams'"2on storage.objects3for select4to manager5using (6 bucket_id = 'teams'7);
```

## Test the policy[#](#test-the-policy)

To impersonate the `manager` role, you will need a valid JWT token with the `manager` role. You can quickly create one using the `jsonwebtoken` library in Node.js.

Signing a new JWT requires your `JWT_SECRET`. You must store this secret securely. Never expose it in frontend code, and do not check it into version control.

```
1const jwt = require('jsonwebtoken')23const JWT_SECRET = 'your-jwt-secret' // You can find this in your Supabase project settings under API. Store this securely.4const USER_ID = '' // the user id that we want to give the manager role56const token = jwt.sign({ role: 'manager', sub: USER_ID }, JWT_SECRET, {7  expiresIn: '1h',8})
```

Now you can use this token to access the Storage API.

```
1const { StorageClient } = require('@supabase/storage-js')23const PROJECT_URL = 'https://your-project-id.supabase.co/storage/v1'45const storage = new StorageClient(PROJECT_URL, {6  authorization: `Bearer ${token}`,7})89await storage.from('teams').list()
```

