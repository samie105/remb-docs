---
title: "Password security"
source: "https://supabase.com/docs/guides/auth/password-security"
canonical_url: "https://supabase.com/docs/guides/auth/password-security"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:20.278Z"
content_hash: "097514acc66a85065446f22ac62ee6256ab5980772de2dd9d81b05a6389d0f5e"
menu_path: ["Auth","Auth","Security","Security","Password Security","Password Security"]
section_path: ["Auth","Auth","Security","Security","Password Security","Password Security"]
nav_prev: {"path": "supabase/docs/guides/auth/oauth-server/token-security/index.md", "title": "Token Security and Row Level Security"}
nav_next: {"path": "supabase/docs/guides/auth/passwords/index.md", "title": "Password-based Auth"}
---

# 

Password security

## 

Help your users to protect their password security

* * *

A password is more secure if it is harder to guess or brute-force. In theory, a password is harder to guess if it is longer. It is also harder to guess if it uses a larger set of characters (for example, digits, lowercase and uppercase letters, and symbols).

This table shows the _minimum_ number of guesses that need to be tried to access a user's account:

Required characters

Length

Guesses

Digits only

8

~ 227

Digits and letters

8

~ 241

Digits, lower and uppercase letters

8

~ 248

Digits, lower and uppercase letters, symbols

8

~ 252

In reality though, passwords are not always generated at random. They often contain variations of names, words, dates, and common phrases. Malicious actors can use these properties to guess a password in fewer attempts.

There are hundreds of millions (and growing!) known passwords out there. Malicious actors can use these lists of leaked passwords to automate login attempts (known as credential stuffing) and steal or access sensitive user data.

## Password strength and leaked password protection[#](#password-strength-and-leaked-password-protection)

To help protect your users, Supabase Auth allows you fine-grained control over the strength of the passwords used on your project. You can configure these in your project's [Auth settings](/dashboard/project/_/auth/providers?provider=Email):

*   Set a large minimum password length. Anything less than 8 characters is not recommended.
*   Set the required characters that must appear at least once in a user's password. Use the strongest option of requiring digits, lowercase and uppercase letters, and symbols. The allowed symbols are: ``!@#$%^&*()_+-=[]{};'\:"|<>?,./`~``
*   Prevent the use of leaked passwords. Supabase Auth uses the open-source [HaveIBeenPwned.org Pwned Passwords API](https://haveibeenpwned.com/Passwords) to reject passwords that have been leaked and are known by malicious actors.

Leaked password protection is available on the Pro Plan and above.

## Require reauthentication when changing password[#](#require-reauthentication-when-changing-password)

Users will need to be recently logged in to change their password without requiring reauthentication. (A user is considered recently logged in if the session was created within the last 24 hours.) If disabled, a user can change their password at any time.

When enabled, a `nonce` will be sent to the user and this nonce must be validated before the a password change can occur. This can be triggered with the [reauthenticate()](/docs/reference/javascript/auth-reauthentication) API call.

```
1const { error } = await supabase.auth.reauthenticate()2...3// send the nonce provided by the user with the password change4const { data, error } = await supabase.auth.updateUser({5  email: 'user@email.com',6  nonce: `${nonce}`,7  password: "new_super_strong_password"8})
```

## Require current password when changing password[#](#require-current-password-when-changing-password)

Enforce that users supply their current password when trying to change the password. When enabled, the password change request will validate that the current password is correct before updating the user's password.

```
1const { data, error } = await supabase.auth.updateUser({2  email: 'user@email.com',3  current_password: "correct_current_password",4  password: "new_super_strong_password"5})
```

## Additional recommendations[#](#additional-recommendations)

In addition to choosing suitable password strength settings and preventing the use of leaked passwords, consider asking your users to:

*   Use a password manager to store and generate passwords.
*   Avoid password reuse across websites and apps.
*   Avoid using personal information in passwords.
*   Use [Multi-Factor Authentication](../auth-mfa/index.md).

## Frequently asked questions[#](#frequently-asked-questions)

### How are passwords stored?[#](#how-are-passwords-stored)

Supabase Auth uses [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), a strong password hashing function, to store hashes of users' passwords. Only hashed passwords are stored. You cannot impersonate a user with the password hash. Each hash is accompanied by a randomly generated salt parameter for extra security.

The hash is stored in the `encrypted_password` column of the `auth.users` table. The column's name is a misnomer (cryptographic hashing is not encryption), but is kept for backward compatibility.

### How will strengthened password requirements affect current users?[#](#how-will-strengthened-password-requirements-affect-current-users)

Existing users can still sign in with their current password even if it doesn't meet the new, strengthened password requirements. However, if their password falls short of these updated standards, they will encounter a `WeakPasswordError` during the `signInWithPassword` process, explaining why it's considered weak. This change is also applicable to new users and existing users changing their passwords, ensuring everyone adheres to the enhanced security standards.
