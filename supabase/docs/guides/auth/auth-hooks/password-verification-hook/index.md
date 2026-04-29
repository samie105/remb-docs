---
title: "Password Verification Hook"
source: "https://supabase.com/docs/guides/auth/auth-hooks/password-verification-hook"
canonical_url: "https://supabase.com/docs/guides/auth/auth-hooks/password-verification-hook"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:55.297Z"
content_hash: "37a3c42375296b03625c18a77848006748c378f789d920777f9783aea7a1bb38"
menu_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","Password verification hook","Password verification hook"]
section_path: ["Auth","Auth","More","More","More","Auth Hooks","Auth Hooks","Password verification hook","Password verification hook"]
nav_prev: {"path": "../mfa-verification-hook/index.md", "title": "MFA Verification Hook"}
nav_next: {"path": "../send-email-hook/index.md", "title": "Send Email Hook"}
---

# 

Password Verification Hook

* * *

Your company wishes to increase security beyond the requirements of the default password implementation in order to fulfill security or compliance requirements. You plan to track the status of a password sign-in attempt and take action via an email or a restriction on logins where necessary.

As this hook runs on unauthenticated requests, malicious users can abuse the hook by calling it multiple times. Pay extra care when using the hook as you can unintentionally block legitimate users from accessing your application.

Check if a password is valid prior to taking any additional action to ensure the user is legitimate. Where possible, send an email or notification instead of blocking the user.

**Inputs**

Field

Type

Description

`user_id`

`string`

Unique identifier for the user attempting to sign in. Correlate this to the `auth.users` table.

`valid`

`boolean`

Whether the password verification attempt was valid.

```
1{2  "user_id": "3919cb6e-4215-4478-a960-6d3454326cec",3  "valid": true4}
```

**Outputs**

Return these only if your hook processed the input without errors.

Field

Type

Description

`decision`

`string`

The decision on whether to allow authentication to move forward. Use `reject` to deny the verification attempt and log the user out of all active sessions. Use `continue` to use the default Supabase Auth behavior.

`message`

`string`

The message to show the user if the decision was `reject`.

`should_logout_user`

`boolean`

Whether to log out the user if a `reject` decision is issued. Has no effect when a `continue` decision is issued.

```
1{2  "decision": "reject",3  "message": "You have exceeded maximum number of password sign-in attempts.",4  "should_logout_user": "false"5}
```

As part of new security measures within the company, users can only input an incorrect password every 10 seconds and not more than that. You want to write a hook to enforce this.

Create a table to record each user's last incorrect password verification attempt.

```
1create table public.password_failed_verification_attempts (2  user_id uuid not null,3  last_failed_at timestamp not null default now(),4  primary key (user_id)5);
```

Create a hook to read and write information to this table. For example:

```
1create function public.hook_password_verification_attempt(event jsonb)2returns jsonb3language plpgsql4as $$5  declare6    last_failed_at timestamp;7  begin8    if event->'valid' is true then9      -- password is valid, accept it10      return jsonb_build_object('decision', 'continue');11    end if;1213    select last_failed_at into last_failed_at14      from public.password_failed_verification_attempts15      where16        user_id = event->'user_id';1718    if last_failed_at is not null and now() - last_failed_at < interval '10 seconds' then19      -- last attempt was done too quickly20      return jsonb_build_object(21        'error', jsonb_build_object(22          'http_code', 429,23          'message',   'Please wait a moment before trying again.'24        )25      );26    end if;2728    -- record this failed attempt29    insert into public.password_failed_verification_attempts30      (31        user_id,32        last_failed_at33      )34      values35      (36        event->'user_id',37        now()38      )39      on conflict do update40        set last_failed_at = now();4142    -- finally let Supabase Auth do the default behavior for a failed attempt43    return jsonb_build_object('decision', 'continue');44  end;45$$;4647-- Assign appropriate permissions48grant all49  on table public.password_failed_verification_attempts50  to supabase_auth_admin;5152revoke all53  on table public.password_failed_verification_attempts54  from authenticated, anon, public;
```
