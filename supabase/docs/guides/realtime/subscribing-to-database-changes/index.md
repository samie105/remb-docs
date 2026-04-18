---
title: "Subscribing to Database Changes"
source: "https://supabase.com/docs/guides/realtime/subscribing-to-database-changes"
canonical_url: "https://supabase.com/docs/guides/realtime/subscribing-to-database-changes"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:57.585Z"
content_hash: "9cf38357667b98027c5674a505334edd58ea9c66f5ee7f9b09c637cfa3f19831"
menu_path: ["Realtime","Realtime","Guides","Guides","Subscribing to Database Changes","Subscribing to Database Changes"]
section_path: ["Realtime","Realtime","Guides","Guides","Subscribing to Database Changes","Subscribing to Database Changes"]
nav_prev: {"path": "supabase/docs/guides/security/hipaa-compliance/index.md", "title": "HIPAA Compliance and Supabase"}
nav_next: {"path": "supabase/docs/guides/security/platform-audit-logs/index.md", "title": "Platform Audit Logs"}
---

# 

Subscribing to Database Changes

## 

Listen to database changes in real-time from your website or application.

* * *

You can use Supabase to subscribe to real-time database changes. There are two options available:

1.  [Broadcast](/docs/guides/realtime/broadcast). This is the recommended method for scalability and security.
2.  [Postgres Changes](/docs/guides/realtime/postgres-changes). This is a simpler method. It requires less setup, but does not scale as well as Broadcast.

## Using Broadcast[#](#using-broadcast)

To automatically send messages when a record is created, updated, or deleted, we can attach a [Postgres trigger](/docs/guides/database/postgres/triggers) to any table. Supabase Realtime provides a `realtime.broadcast_changes()` function which we can use in conjunction with a trigger. This function will use a private channel and needs broadcast authorization RLS policies to be met.

### Broadcast authorization[#](#broadcast-authorization)

[Realtime Authorization](/docs/guides/realtime/authorization) is required for receiving Broadcast messages. This is an example of a policy that allows authenticated users to listen to messages from topics:

```
1create policy "Authenticated users can receive broadcasts"2on "realtime"."messages"3for select4to authenticated5using ( true );
```

### Create a trigger function[#](#create-a-trigger-function)

Let's create a function that we can call any time a record is created, updated, or deleted. This function will make use of some of Postgres's native [trigger variables](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-DML-TRIGGER). For this example, we want to have a topic with the name `topic:<record id>` to which we're going to broadcast events.

```
1create or replace function public.your_table_changes()2returns trigger3security definer4language plpgsql5as $$6begin7  perform realtime.broadcast_changes(8    'topic:' || coalesce(NEW.id, OLD.id) ::text,       -- topic - the topic to which you're broadcasting where you can use the topic id to build the topic name9    TG_OP,                                             -- event - the event that triggered the function10    TG_OP,                                             -- operation - the operation that triggered the function11    TG_TABLE_NAME,                                     -- table - the table that caused the trigger12    TG_TABLE_SCHEMA,                                   -- schema - the schema of the table that caused the trigger13    NEW,                                               -- new record - the record after the change14    OLD                                                -- old record - the record before the change15  );16  return null;17end;18$$;
```

### Create a trigger[#](#create-a-trigger)

Let's set up a trigger so the function is executed after any changes to the table.

```
1create trigger handle_your_table_changes2after insert or update or delete3on public.your_table4for each row5execute function your_table_changes ();
```

#### Listening on client side[#](#listening-on-client-side)

Finally, on the client side, listen to the topic `topic:<record_id>` to receive the events. Remember to set the channel as a private channel, since `realtime.broadcast_changes` uses Realtime Authorization.

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5const gameId = 'id'6await supabase.realtime.setAuth() // Needed for Realtime Authorization7const changes = supabase8  .channel(`topic:${gameId}`, {9    config: { private: true },10  })11  .on('broadcast', { event: 'INSERT' }, (payload) => console.log(payload))12  .on('broadcast', { event: 'UPDATE' }, (payload) => console.log(payload))13  .on('broadcast', { event: 'DELETE' }, (payload) => console.log(payload))14  .subscribe()
```

## Using Postgres Changes[#](#using-postgres-changes)

Postgres Changes are simple to use, but have some [limitations](/docs/guides/realtime/postgres-changes#limitations) as your application scales. We recommend using Broadcast for most use cases.

### Enable Postgres Changes[#](#enable-postgres-changes)

You'll first need to create a `supabase_realtime` publication and add your tables (that you want to subscribe to) to the publication:

```
1begin;23-- remove the supabase_realtime publication4drop5  publication if exists supabase_realtime;67-- re-create the supabase_realtime publication with no tables8create publication supabase_realtime;910commit;1112-- add a table called 'messages' to the publication13-- (update this to match your tables)14alter15  publication supabase_realtime add table messages;
```

### Streaming inserts[#](#streaming-inserts)

You can use the `INSERT` event to stream all new rows.

```
1// @noImplicitAny: false2import { createClient } from '@supabase/supabase-js'3const supabase = createClient('your_project_url', 'your_supabase_api_key')45// ---cut---6const channel = supabase7  .channel('schema-db-changes')8  .on(9    'postgres_changes',10    {11      event: 'INSERT',12      schema: 'public',13    },14    (payload) => console.log(payload)15  )16  .subscribe()
```

### Streaming updates[#](#streaming-updates)

You can use the `UPDATE` event to stream all updated rows.

```
1// @noImplicitAny: false2import { createClient } from '@supabase/supabase-js'3const supabase = createClient('your_project_url', 'your_supabase_api_key')45// ---cut---6const channel = supabase7  .channel('schema-db-changes')8  .on(9    'postgres_changes',10    {11      event: 'UPDATE',12      schema: 'public',13    },14    (payload) => console.log(payload)15  )16  .subscribe()
```

