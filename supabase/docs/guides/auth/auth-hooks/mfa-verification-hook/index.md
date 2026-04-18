---
title: "MFA Verification Hook"
source: "https://supabase.com/docs/guides/auth/auth-hooks/mfa-verification-hook"
canonical_url: "https://supabase.com/docs/guides/auth/auth-hooks/mfa-verification-hook"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:47.019Z"
content_hash: "ad5ffc90904528bbf4c9e5a1cc8305b9d958b8b73f793dc54b4deafae0d2f6e0"
menu_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","MFA verification hook","MFA verification hook"]
section_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","MFA verification hook","MFA verification hook"]
nav_prev: {"path": "supabase/docs/guides/auth/auth-hooks/custom-access-token-hook/index.md", "title": "Custom Access Token Hook"}
nav_next: {"path": "supabase/docs/guides/auth/auth-hooks/password-verification-hook/index.md", "title": "Password Verification Hook"}
---

# 

MFA Verification Hook

* * *

You can add additional checks to the [Supabase MFA implementation](/docs/guides/auth/auth-mfa) with hooks. For example, you can:

*   Limit the number of verification attempts performed over a period of time.
*   Sign out users who have too many invalid verification attempts.
*   Count, rate limit, or ban sign-ins.

**Inputs**

Supabase Auth will send a payload containing these fields to your hook:

Field

Type

Description

`factor_id`

`string`

Unique identifier for the MFA factor being verified

`factor_type`

`string`

`totp` or `phone`

`user_id`

`string`

Unique identifier for the user

`valid`

`boolean`

Whether the verification attempt was valid. For TOTP, this means that the six digit code was correct (true) or incorrect (false).

```
1{2  "factor_id": "6eab6a69-7766-48bf-95d8-bd8f606894db",3  "user_id": "3919cb6e-4215-4478-a960-6d3454326cec",4  "valid": true5}
```

**Outputs**

Return this if your hook processed the input without errors.

Field

Type

Description

`decision`

`string`

The decision on whether to allow authentication to move forward. Use `reject` to deny the verification attempt and log the user out of all active sessions. Use `continue` to use the default Supabase Auth behavior.

`message`

`string`

The message to show the user if the decision was `reject`.

```
1{2  "decision": "reject",3  "message": "You have exceeded maximum number of MFA attempts."4}
```

Your company requires that a user can input an incorrect MFA Verification code no more than once every 2 seconds.

Create a table to record the last time a user had an incorrect MFA verification attempt for a factor.

```
1create table public.mfa_failed_verification_attempts (2  user_id uuid not null,3  factor_id uuid not null,4  last_failed_at timestamp not null default now(),5  primary key (user_id, factor_id)6);
```

Create a hook to read and write information to this table. For example:

```
1create function public.hook_mfa_verification_attempt(event jsonb)2  returns jsonb3  language plpgsql4as $$5  declare6    last_failed_at timestamp;7  begin8    if event->'valid' is true then9      -- code is valid, accept it10      return jsonb_build_object('decision', 'continue');11    end if;1213    select last_failed_at into last_failed_at14      from public.mfa_failed_verification_attempts15      where16        user_id = event->'user_id'17          and18        factor_id = event->'factor_id';1920    if last_failed_at is not null and now() - last_failed_at < interval '2 seconds' then21      -- last attempt was done too quickly22      return jsonb_build_object(23        'error', jsonb_build_object(24          'http_code', 429,25          'message',   'Please wait a moment before trying again.'26        )27      );28    end if;2930    -- record this failed attempt31    insert into public.mfa_failed_verification_attempts32      (33        user_id,34        factor_id,35        last_refreshed_at36      )37      values38      (39        event->'user_id',40        event->'factor_id',41        now()42      )43      on conflict do update44        set last_refreshed_at = now();4546    -- finally let Supabase Auth do the default behavior for a failed attempt47    return jsonb_build_object('decision', 'continue');48  end;49$$;5051-- Assign appropriate permissions and revoke access52grant all53  on table public.mfa_failed_verification_attempts54  to supabase_auth_admin;5556revoke all57  on table public.mfa_failed_verification_attempts58  from authenticated, anon, public;
```


