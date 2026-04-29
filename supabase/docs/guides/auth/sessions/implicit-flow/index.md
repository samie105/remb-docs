---
title: "Implicit flow"
source: "https://supabase.com/docs/guides/auth/sessions/implicit-flow"
canonical_url: "https://supabase.com/docs/guides/auth/sessions/implicit-flow"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:59.777Z"
content_hash: "eb387c184f1ed2f3321215b585b8ca89031b1dc62cb1c440f4948956a25c59b2"
menu_path: ["Auth","Auth","More","More","More","Sessions","Sessions","Implicit flow","Implicit flow"]
section_path: ["Auth","Auth","More","More","More","Sessions","Sessions","Implicit flow","Implicit flow"]
nav_prev: {"path": "supabase/docs/guides/auth/sessions/index.md", "title": "User sessions"}
nav_next: {"path": "supabase/docs/guides/auth/sessions/pkce-flow/index.md", "title": "PKCE flow"}
---

# 

Implicit flow

## 

About authenticating with implicit flow.

* * *

The implicit flow is one of two ways that a user can authenticate and your app can receive the necessary access and refresh tokens.

The flow is an implementation detail handled for you by Supabase Auth, but understanding the difference between implicit and [PKCE flow](../pkce-flow/index.md) is important for understanding the difference between client-only and server-side auth.

## How it works[#](#how-it-works)

After a successful signin, the user is redirected to your app with a URL that looks like this:

```
1https://yourapp.com/...#access_token=<...>&refresh_token=<...>&...
```

The access and refresh tokens are contained in the URL fragment.

The client libraries:

*   Detect this type of URL
*   Extract the access token, refresh token, and some extra information
*   Persist this information to local storage for further use by the library and your app

## Limitations[#](#limitations)

The implicit flow only works on the client. Web browsers do not send the URL fragment to the server by design. This is a security feature:

*   You may be hosting your single-page app on a third-party server. The third-party service shouldn't get access to your user's credentials.
*   Even if the server is under your direct control, `GET` requests and their full URLs are often logged. This approach avoids leaking credentials in request or access logs.

If you wish to obtain the access token and refresh token on a server, use the [PKCE flow](../pkce-flow/index.md).
