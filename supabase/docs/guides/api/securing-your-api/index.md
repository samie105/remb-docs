---
title: "Securing your API"
source: "https://supabase.com/docs/guides/api/securing-your-api"
canonical_url: "https://supabase.com/docs/guides/api/securing-your-api"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:43.545Z"
content_hash: "198bae0d20be8ce01ff5931fa6c3af8d3d55117c9376455ad95cb81d15a56abb"
menu_path: ["Data REST API","Data REST API","Security","Security","Securing your API","Securing your API"]
section_path: ["Data REST API","Data REST API","Security","Security","Securing your API","Securing your API"]
nav_prev: {"path": "supabase/docs/guides/api/quickstart/index.md", "title": "Build an API route in less than 2 minutes."}
nav_next: {"path": "supabase/docs/guides/api/sql-to-api/index.md", "title": "Converting SQL to JavaScript API"}
---

# 

Securing your API

* * *

The data APIs are designed to work with Postgres Row Level Security (RLS). If you use [Supabase Auth](/docs/guides/auth), you can restrict data based on the logged-in user.

To control access to your data, you can use [Policies](/docs/guides/auth#policies).

## Enabling row level security[#](#enabling-row-level-security)

Any table you create in the `public` schema will be accessible via the Supabase Data API.

To restrict access, enable Row Level Security (RLS) on all tables, views, and functions in the `public` schema. You can then write RLS policies to grant users access to specific database rows or functions based on their authentication token.

Always enable Row Level Security on tables, views, and functions in the `public` schema to protect your data.

Any table created through the Supabase Dashboard will have RLS enabled by default. If you created the tables via the SQL editor or via another way, enable RLS like so:

1.  Go to the [Authentication > Policies](/dashboard/project/_/auth/policies) page in the Dashboard.
2.  Select **Enable RLS** to enable Row Level Security.

With RLS enabled, you can create Policies that allow or disallow users to access and update data. We provide a detailed guide for creating Row Level Security Policies in our [Authorization documentation](/docs/guides/database/postgres/row-level-security).

Any table **without RLS enabled** in the `public` schema will be accessible to the public, using the `anon` role. Always make sure that RLS is enabled or that you've got other security measures in place to avoid unauthorized access to your project's data!

## Disable the API or restrict to custom schema[#](#disable-the-api-or-restrict-to-custom-schema)

If you don't use the Data API, or if you don't want to expose the `public` schema, you can either disable it entirely or change the automatically exposed schema to one of your choice. See **[Hardening the Data API](/docs/guides/api/hardening-data-api)** for instructions.

## Enforce additional rules on each request[#](#enforce-additional-rules-on-each-request)

Using Row Level Security policies may not always be adequate or sufficient to protect APIs.

Here are some common situations where additional protections are necessary:

*   Enforcing per-IP or per-user rate limits.
*   Checking custom or additional API keys before allowing further access.
*   Rejecting requests after exceeding a quota or requiring payment.
*   Disallowing direct access to certain tables, views or functions in the `public` schema.

You can build these cases in your application by creating a Postgres function that will read information from the request and perform additional checks, such as counting the number of requests received or checking that an API key is already registered in your database before serving the response.

Define a function like so:

```
1create function public.check_request()2  returns void3  language plpgsql4  security definer5  as $$6begin7  -- your logic here8end;9$$;
```

And register it to run on every Data API request using:

```
1alter role authenticator2  set pgrst.db_pre_request = 'public.check_request';
```

This configures the `public.check_request` function to run on every Data API request. To have the changes take effect, you should run:

```
1notify pgrst, 'reload config';
```

The `pgrst.db_pre_request` configuration only works with the **Data API** (PostgREST). It does not work with Realtime, Storage, or other Supabase products.

If you're using `db_pre_request` to call a function (like `set_information()`) that sets up context or performs checks on every request, and you need similar behavior for other Supabase products, you must call the function directly in your Row Level Security (RLS) policies instead.

**Example:**

If you have a `db_pre_request` function that calls `set_information()` that returns `true` to set up context or perform checks, and you have an RLS policy like:

```
1create policy "Individuals can view their own todos."2on todos for select3using ( (select auth.uid()) = user_id );
```

To achieve the same behavior with other Supabase products, you need to call the function directly in your RLS policy:

```
1create policy "Individuals can view their own todos."2on todos for select3using ( set_information() AND (select auth.uid()) = user_id );
```

This ensures the function is called when evaluating RLS policies for all products, not just Data API requests.

**Performance consideration:**

Be aware that calling functions directly in RLS policies can impact database performance, as the function is evaluated for each row when the policy is checked. Consider optimizing your function or using caching strategies if performance becomes an issue.

Inside the function you can perform any additional checks on the request headers or JWT and raise an exception to prevent the request from completing. For example, this exception raises an HTTP 402 Payment Required response with a `hint` and additional `X-Powered-By` header:

```
1raise sqlstate 'PGRST' using2  message = json_build_object(3    'code',    '123',4    'message', 'Payment Required',5    'details', 'Quota exceeded',6    'hint',    'Upgrade your plan')::text,7  detail = json_build_object(8    'status',  402,9    'headers', json_build_object(10      'X-Powered-By', 'Nerd Rage'))::text;
```

When raised within the `public.check_request` function, the resulting HTTP response will look like:

```
1HTTP/1.1 402 Payment Required2Content-Type: application/json; charset=utf-83X-Powered-By: Nerd Rage45{6  "message": "Payment Required",7  "details": "Quota exceeded",8  "hint": "Upgrade your plan",9  "code": "123"10}
```

Use the [JSON operator functions](https://www.postgresql.org/docs/current/functions-json.html) to build rich and dynamic responses from exceptions.

If you use a custom HTTP status code like 419, you can supply the `status_text` key in the `detail` clause of the exception to describe the HTTP status.

If you're using PostgREST version 11 or lower ([find out your PostgREST version](/dashboard/project/_/settings/infrastructure)) a different and less powerful [syntax](https://postgrest.org/en/stable/references/errors.html#raise-errors-with-http-status-codes) needs to be used.

### Accessing request information[#](#accessing-request-information)

Like with RLS policies, you can access information about the request by using the `current_setting()` Postgres function. Here are some examples on how this works:

```
1-- To get all the headers sent in the request2SELECT current_setting('request.headers', true)::json;34-- To get a single header, you can use JSON arrow operators5SELECT current_setting('request.headers', true)::json->>'user-agent';67-- Access Cookies8SELECT current_setting('request.cookies', true)::json;
```

`current_setting()`

Example

Description

`request.method`

`GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`

Request's method

`request.path`

`table`

Table's path

`request.path`

`view`

View's path

`request.path`

`rpc/function`

Functions's path

`request.headers`

`{ "User-Agent": "...", ... }`

JSON object of the request's headers

`request.cookies`

`{ "cookieA": "...", "cookieB": "..." }`

JSON object of the request's cookies

`request.jwt`

`{ "sub": "a7194ea3-...", ... }`

JSON object of the JWT payload

To access the IP address of the client look up the [X-Forwarded-For header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) in the `request.headers` setting. For example:

```
1SELECT split_part(2  current_setting('request.headers', true)::json->>'x-forwarded-for',3  ',', 1); -- takes the client IP before the first comma (,)
```

Read more about [PostgREST's pre-request function](https://postgrest.org/en/stable/references/transactions.html#pre-request).

### Examples[#](#examples)

You can only rate-limit `POST`, `PUT`, `PATCH` and `DELETE` requests. This is because `GET` and `HEAD` requests run in read-only mode, and will be served by [Read Replicas](/docs/guides/platform/read-replicas) which do not support writing to the database.

Outline:

*   A new row is added to a `private.rate_limits` table each time a modifying action is done to the database containing the IP address and the timestamp of the action.
*   If there are over 100 requests from the same IP address in the last 5 minutes, the request is rejected with an HTTP 420 code.

Create the table:

```
1create table private.rate_limits (2  ip inet,3  request_at timestamp4);56-- add an index so that lookups are fast7create index rate_limits_ip_request_at_idx on private.rate_limits (ip, request_at desc);
```

The `private` schema is used as it cannot be accessed over the API!

Create the `public.check_request` function:

```
1create function public.check_request()2  returns void3  language plpgsql4  security definer5  as $$6declare7  req_method text := current_setting('request.method', true);8  req_ip inet := split_part(9    current_setting('request.headers', true)::json->>'x-forwarded-for',10    ',', 1)::inet;11  count_in_five_mins integer;12begin13  if req_method = 'GET' or req_method = 'HEAD' or req_method is null then14    -- rate limiting can't be done on GET and HEAD requests15    return;16  end if;1718  select19    count(*) into count_in_five_mins20  from private.rate_limits21  where22    ip = req_ip and request_at between now() - interval '5 minutes' and now();2324  if count_in_five_mins > 100 then25    raise sqlstate 'PGRST' using26      message = json_build_object(27        'message', 'Rate limit exceeded, try again after a while')::text,28      detail = json_build_object(29        'status',  420,30        'status_text', 'Enhance Your Calm')::text;31  end if;3233  insert into private.rate_limits (ip, request_at) values (req_ip, now());34end;35  $$;
```

Finally, configure the `public.check_request()` function to run on every Data API request:

```
1alter role authenticator2  set pgrst.db_pre_request = 'public.check_request';34notify pgrst, 'reload config';
```

The `pgrst.db_pre_request` configuration only works with the **Data API** (PostgREST). It does not work with Realtime, Storage, or other Supabase products.

If you're using `db_pre_request` to call a function (like `set_information()`) that sets up context or performs checks on every request, and you need similar behavior for other Supabase products, you must call the function directly in your Row Level Security (RLS) policies instead.

**Example:**

If you have a `db_pre_request` function that calls `set_information()` that returns `true` to set up context or perform checks, and you have an RLS policy like:

```
1create policy "Individuals can view their own todos."2on todos for select3using ( (select auth.uid()) = user_id );
```

To achieve the same behavior with other Supabase products, you need to call the function directly in your RLS policy:

```
1create policy "Individuals can view their own todos."2on todos for select3using ( set_information() AND (select auth.uid()) = user_id );
```

This ensures the function is called when evaluating RLS policies for all products, not just Data API requests.

**Performance consideration:**

Be aware that calling functions directly in RLS policies can impact database performance, as the function is evaluated for each row when the policy is checked. Consider optimizing your function or using caching strategies if performance becomes an issue.

To clear old entries in the `private.rate_limits` table, set up a [pg\_cron](/docs/guides/database/extensions/pg_cron) job to clean them up.
