---
title: "Database Webhooks"
source: "https://supabase.com/docs/guides/database/webhooks"
canonical_url: "https://supabase.com/docs/guides/database/webhooks"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:54.278Z"
content_hash: "78df0d8f90c28d2221d48a6485090e36efcf5bef55bfae8ec52a08e0967b6313"
menu_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing database webhooks","Managing database webhooks"]
section_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing database webhooks","Managing database webhooks"]
nav_prev: {"path": "supabase/docs/guides/database/vault/index.md", "title": "Vault"}
nav_next: {"path": "supabase/docs/guides/deployment/going-into-prod/index.md", "title": "Production Checklist"}
---

# 

Database Webhooks

## 

Trigger external payloads on database events.

* * *

Database Webhooks allow you to send real-time data from your database to another system whenever a table event occurs.

You can hook into three table events: `INSERT`, `UPDATE`, and `DELETE`. All events are fired _after_ a database row is changed.

## Webhooks vs triggers[#](#webhooks-vs-triggers)

Database Webhooks are very similar to triggers, and that's because Database Webhooks are just a convenience wrapper around triggers using the [pg\_net](/docs/guides/database/extensions/pgnet) extension. This extension is asynchronous, and therefore will not block your database changes for long-running network requests.

This video demonstrates how you can create a new customer in Stripe each time a row is inserted into a `profiles` table:

## Creating a webhook[#](#creating-a-webhook)

1.  Create a new [Database Webhook](/dashboard/project/_/integrations/webhooks/overview) in the Dashboard.
2.  Give your Webhook a name.
3.  Select the table you want to hook into.
4.  Select one or more events (table inserts, updates, or deletes) you want to hook into.

Since webhooks are just database triggers, you can also create one from SQL statement directly.

```
1create trigger "my_webhook" after insert2on "public"."my_table" for each row3execute function "supabase_functions"."http_request"(4  'http://host.docker.internal:3000',5  'POST',6  '{"Content-Type":"application/json"}',7  '{}',8  '1000'9);
```

We currently support HTTP webhooks. These can be sent as `POST` or `GET` requests with a JSON payload.

## Payload[#](#payload)

The payload is automatically generated from the underlying table record:

```
1type InsertPayload = {2  type: 'INSERT'3  table: string4  schema: string5  record: TableRecord<T>6  old_record: null7}8type UpdatePayload = {9  type: 'UPDATE'10  table: string11  schema: string12  record: TableRecord<T>13  old_record: TableRecord<T>14}15type DeletePayload = {16  type: 'DELETE'17  table: string18  schema: string19  record: null20  old_record: TableRecord<T>21}
```

## Monitoring[#](#monitoring)

Logging history of webhook calls is available under the `net` schema of your database. For more info, see the [GitHub Repo](https://github.com/supabase/pg_net).

## Local development[#](#local-development)

When using Database Webhooks on your local Supabase instance, you need to be aware that the Postgres database runs inside a Docker container. This means that `localhost` or `127.0.0.1` in your webhook URL will refer to the container itself, not your host machine where your application is running.

To target services running on your host machine, use `host.docker.internal`. If that doesn't work, you may need to use your machine's local IP address instead.

For example, if you want to trigger an edge function when a webhook fires, your webhook URL would be:

```
1http://host.docker.internal:54321/functions/v1/my-function-name
```

If you're experiencing connection issues with webhooks locally, verify you're using the correct hostname instead of `localhost`.

## Resources[#](#resources)

*   [pg\_net](/docs/guides/database/extensions/pgnet): an async networking extension for Postgres

