---
title: "pgjwt: JSON Web Tokens"
source: "https://supabase.com/docs/guides/database/extensions/pgjwt"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgjwt"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:55.012Z"
content_hash: "52d4ff62e63668403284ff5905d3c4402b3c4557512301400904fa4e422cefba"
menu_path: ["Database","Database","Extensions","Extensions","pgjwt (deprecated)","pgjwt (deprecated)"]
section_path: ["Database","Database","Extensions","Extensions","pgjwt (deprecated)","pgjwt (deprecated)"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pgaudit/index.md", "title": "PGAudit: Postgres Auditing"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pgmq/index.md", "title": "pgmq: Queues"}
---

# 

pgjwt: JSON Web Tokens

* * *

Supabase creates and handles JWT for you. It is built into the platform. **If you use Postgres version 15 or earlier**, you don't need the pgjwt extension, and it is safe to disable. For more information on how Supabase handles JWTs, read the [Supabase and JWTs documentation](/docs/guides/auth/jwts#supabase-and-jwts)

The `pgjwt` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.

The [`pgjwt`](https://github.com/michelp/pgjwt) (Postgres JSON Web Token) extension allows you to create and parse [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token) within a Postgres database. JWTs are commonly used for authentication and authorization in web applications and services.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `pgjwt` and enable the extension.

## API[#](#api)

*   [`sign(payload json, secret text, algorithm text default 'HSA256')`](https://github.com/michelp/pgjwt#usage): Signs a JWT containing _payload_ with _secret_ using _algorithm_.
*   [`verify(token text, secret text, algorithm text default 'HSA256')`](https://github.com/michelp/pgjwt#usage): Decodes a JWT _token_ that was signed with _secret_ using _algorithm_.

Where:

*   `payload` is an encrypted JWT represented as a string.
*   `secret` is the private/secret passcode which is used to sign the JWT and verify its integrity.
*   `algorithm` is the method used to sign the JWT using the secret.
*   `token` is an encrypted JWT represented as a string.

## Usage[#](#usage)

Once the extension is installed, you can use its functions to create and parse JWTs. Here's an example of how you can use the `sign` function to create a JWT:

```
1select2  extensions.sign(3    payload   := '{"sub":"1234567890","name":"John Doe","iat":1516239022}',4    secret    := 'secret',5    algorithm := 'HS256'6  );
```

The `pgjwt_encode` function returns a string that represents the JWT, which can then be safely transmitted between parties.

```
1sign2---------------------------------3 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX4 VCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw5 ibmFtZSI6IkpvaG4gRG9lIiwiaWF0Ijo6 xNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y97 22BhjWgQzWXcXNrz0ogtVhfEd2o8(1 row)
```

To parse a JWT and extract its claims, you can use the `verify` function. Here's an example:

```
1select2  extensions.verify(3    token := 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiRm9vIn0.Q8hKjuadCEhnCPuqIj9bfLhTh_9QSxshTRsA5Aq4IuM',4    secret    := 'secret',5    algorithm := 'HS256'6  );
```

Which returns the decoded contents and some associated metadata.

```
1header            |    payload     | valid2-----------------------------+----------------+-------3 {"alg":"HS256","typ":"JWT"} | {"name":"Foo"} | t4(1 row)
```

## Resources[#](#resources)

*   Official [`pgjwt` documentation](https://github.com/michelp/pgjwt)
