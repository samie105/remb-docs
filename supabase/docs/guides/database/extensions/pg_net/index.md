---
title: "pg_net: Async Networking"
source: "https://supabase.com/docs/guides/database/extensions/pg_net"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_net"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:43.431Z"
content_hash: "7b2387a68ef938de557a83e3e85f58069515508ec4d21e4d0094903b45c31ce6"
menu_path: ["Database","Database","Extensions","Extensions","pg_net: Async Networking","pg_net: Async Networking"]
section_path: ["Database","Database","Extensions","Extensions","pg_net: Async Networking","pg_net: Async Networking"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pg_jsonschema/index.md", "title": "pg_jsonschema: JSON Schema Validation"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pg_plan_filter/index.md", "title": "pg_plan_filter: Restrict Total Cost"}
---

# 

pg\_net: Async Networking

* * *

The pg\_net API is in beta. Functions signatures may change.

[pg\_net](https://github.com/supabase/pg_net/) enables Postgres to make asynchronous HTTP/HTTPS requests in SQL. It differs from the [`http`](/docs/guides/database/extensions/http) extension in that it is asynchronous by default. This makes it useful in blocking functions (like triggers).

It eliminates the need for servers to continuously poll for database changes and instead allows the database to proactively notify external resources about significant events.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "pg\_net" and enable the extension.

## `http_get`[#](#httpget)

Creates an HTTP GET request returning the request's ID. HTTP requests are not started until the transaction is committed.

### Signature [#](#get-signature)

This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.

```
1net.http_get(2    -- url for the request3    url text,4    -- key/value pairs to be url encoded and appended to the `url`5    params jsonb default '{}'::jsonb,6    -- key/values to be included in request headers7    headers jsonb default '{}'::jsonb,8    -- the maximum number of milliseconds the request may take before being canceled9    timeout_milliseconds int default 200010)11    -- request_id reference12    returns bigint1314    strict15    volatile16    parallel safe17    language plpgsql
```

### Usage [#](#get-usage)

```
1select2    net.http_get('https://news.ycombinator.com')3    as request_id;4request_id5----------6         17(1 row)
```

## `http_post`[#](#httppost)

Creates an HTTP POST request with a JSON body, returning the request's ID. HTTP requests are not started until the transaction is committed.

The body's character set encoding matches the database's `server_encoding` setting.

### Signature [#](#post-signature)

This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function

```
1net.http_post(2    -- url for the request3    url text,4    -- body of the POST request5    body jsonb default '{}'::jsonb,6    -- key/value pairs to be url encoded and appended to the `url`7    params jsonb default '{}'::jsonb,8    -- key/values to be included in request headers9    headers jsonb default '{"Content-Type": "application/json"}'::jsonb,10    -- the maximum number of milliseconds the request may take before being canceled11    timeout_milliseconds int default 200012)13    -- request_id reference14    returns bigint1516    volatile17    parallel safe18    language plpgsql
```

### Usage [#](#post-usage)

```
1select2    net.http_post(3        url:='https://httpbin.org/post',4        body:='{"hello": "world"}'::jsonb5    ) as request_id;6request_id7----------8         19(1 row)
```

## `http_delete`[#](#httpdelete)

Creates an HTTP DELETE request, returning the request's ID. HTTP requests are not started until the transaction is committed.

### Signature [#](#post-signature)

This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function

```
1net.http_delete(2    -- url for the request3    url text,4    -- key/value pairs to be url encoded and appended to the `url`5    params jsonb default '{}'::jsonb,6    -- key/values to be included in request headers7    headers jsonb default '{}'::jsonb,8    -- the maximum number of milliseconds the request may take before being canceled9    timeout_milliseconds int default 200010)11    -- request_id reference12    returns bigint1314    strict15    volatile16    parallel safe17    language plpgsql18    security definer
```

### Usage [#](#delete-usage)

```
1select2    net.http_delete(3        'https://dummy.restapiexample.com/api/v1/delete/2'4    ) as request_id;5----------6         17(1 row)
```

## Analyzing responses[#](#analyzing-responses)

Waiting requests are stored in the `net.http_request_queue` table. Upon execution, they are deleted.

```
1CREATE UNLOGGED TABLE2    net.http_request_queue (3        id bigint NOT NULL DEFAULT nextval('net.http_request_queue_id_seq'::regclass),4        method text NOT NULL,5        url text NOT NULL,6        headers jsonb NOT NULL,7        body bytea NULL,8        timeout_milliseconds integer NOT NULL9    )
```

Once a response is returned, by default, it is stored for 6 hours in the `net._http_response` table.

```
1CREATE UNLOGGED TABLE2    net._http_response (3        id bigint NULL,4        status_code integer NULL,5        content_type text NULL,6        headers jsonb NULL,7        content text NULL,8        timed_out boolean NULL,9        error_msg text NULL,10        created timestamp with time zone NOT NULL DEFAULT now()11    )
```

The responses can be observed with the following query:

```
1select * from net._http_response;
```

The data can also be observed in the `net` schema with the [Supabase Dashboard's SQL Editor](/dashboard/project/_/editor)

## Debugging requests[#](#debugging-requests)

### Inspecting request data[#](#inspecting-request-data)

The [Postman Echo API](https://documenter.getpostman.com/view/5025623/SWTG5aqV) returns a response with the same body and content as the request. It can be used to inspect the data being sent.

Sending a post request to the echo API

```
1select2    net.http_post(3        url := 'https://postman-echo.com/post',4        body := '{"key1": "value", "key2": 5}'::jsonb5    ) as request_id;
```

Inspecting the echo API response content to ensure it contains the right body

```
1select2    "content"3from net._http_response4where id = <request_id>5-- returns information about the request6-- including the body sent: {"key": "value", "key": 5}
```

Alternatively, by wrapping a request in a [database function](/docs/guides/database/functions), sent row data can be logged or returned for inspection and debugging.

```
1create or replace function debugging_example (row_id int)2returns jsonb as $$3declare4    -- Store payload data5    row_data_var jsonb;6begin7    -- Retrieve row data and convert to JSON8    select to_jsonb("<example_table>".*) into row_data_var9    from "<example_table>"10    where "<example_table>".id = row_id;1112    -- Initiate HTTP POST request to URL13    perform14        net.http_post(15            url := 'https://postman-echo.com/post',16            -- Use row data as payload17            body := row_data_var18        ) as request_id;1920    -- Optionally Log row data or other data for inspection in Supabase Dashboard's Postgres Logs21    raise log 'Logging an entire row as JSON (%)', row_data_var;2223    -- return row data to inspect24    return row_data_var;2526-- Handle exceptions here if needed27exception28    when others then29        raise exception 'An error occurred: %', SQLERRM;30end;31$$ language plpgsql;3233-- calling function34select debugging_example(<row_id>);
```

### Inspecting failed requests[#](#inspecting-failed-requests)

Finds all failed requests

```
1select2  *3from net._http_response4where "status_code" >= 400 or "error_msg" is not null5order by "created" desc;
```

## Configuration[#](#configuration)

##### Must be on pg\_net v0.12.0 or above to reconfigure

Supabase supports reconfiguring pg\*net starting from v0.12.0+. For the latest release, initiate a Postgres upgrade in the [Infrastructure Settings](/dashboard/project/*/settings/infrastructure).

The extension is configured to reliably execute up to 200 requests per second. The response messages are stored for only 6 hours to prevent needless buildup. The default behavior can be modified by rewriting config variables.

### Get current settings[#](#get-current-settings)

```
1select2  "name",3  "setting"4from pg_settings5where "name" like 'pg_net%';
```

### Alter settings[#](#alter-settings)

Change variables:

```
1alter role "postgres" set pg_net.ttl to '24 hours';2alter role "postgres" set pg_net.batch_size to 500;
```

Then reload the settings and restart the `pg_net` background worker with:

```
1select net.worker_restart();
```

## Examples[#](#examples)

### Invoke a Supabase Edge Function[#](#invoke-a-supabase-edge-function)

Make a POST request to a Supabase Edge Function with auth header and JSON body payload:

```
1select2    net.http_post(3        url:='https://project-ref.supabase.co/functions/v1/function-name',4        headers:='{"Content-Type": "application/json", "Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,5        body:='{"name": "pg_net"}'::jsonb6    ) as request_id;
```

### Call an endpoint every minute with [pg\_cron](/docs/guides/database/extensions/pgcron)[#](#call-an-endpoint-every-minute-with-pgcron)

The pg\_cron extension enables Postgres to become its own cron server. With it you can schedule regular calls with up to a minute precision to endpoints.

```
1select cron.schedule(2	'cron-job-name',3	'* * * * *', -- Executes every minute (cron syntax)4	$$5	    -- SQL query6	    select "net"."http_post"(7            -- URL of Edge function8            url:='https://project-ref.supabase.co/functions/v1/function-name',9            headers:='{"Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,10            body:='{"name": "pg_net"}'::jsonb11	    ) as "request_id";12	$$13);
```

### Execute pg\_net in a trigger[#](#execute-pgnet-in-a-trigger)

Make a call to an external endpoint when a trigger event occurs.

```
1-- function called by trigger2create or replace function <function_name>()3    returns trigger4    language plpgSQL5as $$6begin7    -- calls pg_net function net.http_post8    -- sends request to postman API9    perform "net"."http_post"(10      'https://postman-echo.com/post'::text,11      jsonb_build_object(12        'old_row', to_jsonb(old.*),13        'new_row', to_jsonb(new.*)14      ),15      headers:='{"Content-Type": "application/json"}'::jsonb16    ) as request_id;17    return new;18END $$;1920-- trigger for table update21create trigger <trigger_name>22    after update on <table_name>23    for each row24    execute function <function_name>();
```

### Send multiple table rows in one request[#](#send-multiple-table-rows-in-one-request)

```
1with "selected_table_rows" as (2    select3        -- Converts all the rows into a JSONB array4        jsonb_agg(to_jsonb(<table_name>.*)) as JSON_payload5    from <table_name>6    -- good practice to LIMIT the max amount of rows7)8select9    net.http_post(10        url := 'https://postman-echo.com/post'::text,11        body := JSON_payload12    ) AS request_id13FROM "selected_table_rows";
```

More examples can be seen on the [Extension's GitHub page](https://github.com/supabase/pg_net/)

## Limitations[#](#limitations)

*   To improve speed and performance, the requests and responses are stored in [unlogged tables](https://pgpedia.info/u/unlogged-table.html), which are not preserved during a crash or unclean shutdown.
*   By default, response data is saved for only 6 hours
*   Can only make POST requests with JSON data. No other data formats are supported
*   Intended to handle at most 200 requests per second. Increasing the rate can introduce instability
*   Does not have support for PATCH/PUT requests
*   Can only work with one database at a time. It defaults to the `postgres` database.

## Resources[#](#resources)

*   Source code: [github.com/supabase/pg\_net](https://github.com/supabase/pg_net/)
*   Official Docs: [github.com/supabase/pg\_net](https://github.com/supabase/pg_net/)
