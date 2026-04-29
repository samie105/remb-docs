---
title: "Identities"
source: "https://supabase.com/docs/guides/auth/identities"
canonical_url: "https://supabase.com/docs/guides/auth/identities"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:51.541Z"
content_hash: "4503ccb18c4359ee11df4d14df5b6bc93ec1781778a160c4c03713caeb4d9044"
menu_path: ["Auth","Auth","Concepts","Concepts","Identities","Identities"]
section_path: ["Auth","Auth","Concepts","Concepts","Identities","Identities"]
nav_prev: {"path": "../general-configuration/index.md", "title": "General configuration"}
nav_next: {"path": "../jwt-fields/index.md", "title": "JWT Claims Reference"}
---

# 

Identities

* * *

An identity is an authentication method associated with a user. Supabase Auth supports the following types of identity:

*   Email
*   Phone
*   OAuth
*   SAML

A user can have more than one identity. Anonymous users have no identity until they link an identity to their user.

## The user identity object[#](#the-user-identity-object)

The user identity object contains the following attributes:

Attributes

Type

Description

provider\_id

`string`

The provider id returned by the provider. If the provider is an OAuth provider, the id refers to the user's account with the OAuth provider. If the provider is `email` or `phone`, the id is the user's id from the `auth.users` table.

user\_id

`string`

The user's id that the identity is linked to.

identity\_data

`object`

The identity metadata. For OAuth and SAML identities, this contains information about the user from the provider.

id

`string`

The unique id of the identity.

provider

`string`

The provider name.

email

`string`

The email is a generated column that references the optional email property in the identity\_data

created\_at

`string`

The timestamp that the identity was created.

last\_sign\_in\_at

`string`

The timestamp that the identity was last used to sign in.

updated\_at

`string`

The timestamp that the identity was last updated.
