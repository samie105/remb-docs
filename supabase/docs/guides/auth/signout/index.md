---
title: "Signing out"
source: "https://supabase.com/docs/guides/auth/signout"
canonical_url: "https://supabase.com/docs/guides/auth/signout"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:19.519Z"
content_hash: "0c3bbdba3eb53fe53075143be14803db7b53f0ffa53bf75f4c59218184c8154c"
menu_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Signout","Signout"]
section_path: ["Auth","Auth","Flows (How-tos)","Flows (How-tos)","Signout","Signout"]
nav_prev: {"path": "../signing-keys/index.md", "title": "JWT Signing Keys"}
nav_next: {"path": "../social-login/index.md", "title": "Social Login"}
---

# 

Signing out

## 

Signing out a user

* * *

Signing out a user works the same way no matter what method they used to sign in.

Call the sign out method from the client library. It removes the active session and clears Auth data from the storage medium.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6async function signOut() {7  const { error } = await supabase.auth.signOut()8}
```

## Sign out and scopes[#](#sign-out-and-scopes)

Supabase Auth allows you to specify three different scopes for when a user invokes the [sign out API](/docs/reference/javascript/auth-signout) in your application:

*   `global` (default) when all sessions active for the user are terminated.
*   `local` which only terminates the current session for the user but keep sessions on other devices or browsers active.
*   `others` to terminate all but the current session for the user.

You can invoke these by providing the `scope` option:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...')45// ---cut---6// defaults to the global scope7await supabase.auth.signOut()89// sign out from the current session only10await supabase.auth.signOut({ scope: 'local' })
```

Upon sign out, all refresh tokens and potentially other database objects related to the affected sessions are destroyed and the client library removes the session stored in the local storage medium.

Access Tokens of revoked sessions remain valid until their expiry time, encoded in the `exp` claim. The user won't be immediately logged out and will only be logged out when the Access Token expires.
