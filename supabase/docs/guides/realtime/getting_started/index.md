---
title: "Getting Started with Realtime"
source: "https://supabase.com/docs/guides/realtime/getting_started"
canonical_url: "https://supabase.com/docs/guides/realtime/getting_started"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:08.524Z"
content_hash: "a48f7682199905415ad7d9db0acf5faba85340ceb3eed049ec472400e5bdc0f0"
menu_path: ["Realtime","Realtime","Getting Started","Getting Started"]
section_path: ["Realtime","Realtime","Getting Started","Getting Started"]
nav_prev: {"path": "supabase/docs/guides/realtime/error_codes/index.md", "title": "Operational Error Codes"}
nav_next: {"path": "supabase/docs/guides/realtime/limits/index.md", "title": "Realtime Limits"}
---

# 

Getting Started with Realtime

## 

Learn how to build real-time applications with Supabase Realtime

* * *

## Quick start[#](#quick-start)

### 1\. Install the client library[#](#1-install-the-client-library)

```
1npm install @supabase/supabase-js
```

### 2\. Initialize the client[#](#2-initialize-the-client)

Get your project URL and key.

### Get API details[#](#get-api-details)

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key from [the project **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=).

[Read the API keys docs](/docs/guides/api/api-keys) for a full explanation of all key types and their uses.

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

**The legacy keys will be deprecated shortly, so we strongly encourage switching to and using the new publishable and secret API keys**.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true&connectTab=&framework=), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

**For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://<project>.supabase.co', '<anon_key or sb_publishable_key>')
```

### 3\. Create your first Channel[#](#3-create-your-first-channel)

Channels are the foundation of Realtime. Think of them as rooms where clients can communicate. Each channel is identified by a topic name and if they are public or private.

```
1// Create a channel with a descriptive topic name2const channel = supabase.channel('room:lobby:messages', {3  config: { private: true }, // Recommended for production4})
```

### 4\. Set up authorization[#](#4-set-up-authorization)

Since we're using a private channel, you need to create a basic RLS policy on the `realtime.messages` table to allow authenticated users to connect. Row Level Security (RLS) policies control who can access your Realtime channels based on user authentication and custom rules:

```
1-- Allow authenticated users to receive broadcasts2CREATE POLICY "authenticated_users_can_receive" ON realtime.messages3  FOR SELECT TO authenticated USING (true);45-- Allow authenticated users to send broadcasts6CREATE POLICY "authenticated_users_can_send" ON realtime.messages7  FOR INSERT TO authenticated WITH CHECK (true);
```

### 5\. Send and receive messages[#](#5-send-and-receive-messages)

There are three main ways to send messages with Realtime:

#### 5.1 using client libraries[#](#51-using-client-libraries)

Send and receive messages using the Supabase client:

```
1// Listen for messages2channel3  .on('broadcast', { event: 'message_sent' }, (payload: { payload: any }) => {4    console.log('New message:', payload.payload)5  })6  .subscribe()78// Send a message9channel.send({10  type: 'broadcast',11  event: 'message_sent',12  payload: {13    text: 'Hello, world!',14    user: 'john_doe',15    timestamp: new Date().toISOString(),16  },17})
```

#### 5.2 using HTTP/REST API[#](#52-using-httprest-api)

Send messages via HTTP requests, perfect for server-side applications:

```
1// Send message via REST API2const response = await fetch(`https://<project>.supabase.co/rest/v1/rpc/broadcast`, {3  method: 'POST',4  headers: {5    'Content-Type': 'application/json',6    Authorization: `Bearer <your-service-role-key>`,7    apikey: '<your-service-role-key>',8  },9  body: JSON.stringify({10    topic: 'room:lobby:messages',11    event: 'message_sent',12    payload: {13      text: 'Hello from server!',14      user: 'system',15      timestamp: new Date().toISOString(),16    },17    private: true,18  }),19})
```

#### 5.3 using database triggers[#](#53-using-database-triggers)

Automatically broadcast database changes using triggers. Choose the approach that best fits your needs:

**Using `realtime.broadcast_changes` (Best for mirroring database changes)**

```
1-- Create a trigger function for broadcasting database changes2CREATE OR REPLACE FUNCTION broadcast_message_changes()3RETURNS TRIGGER AS $$4BEGIN5  -- Broadcast to room-specific channel6  PERFORM realtime.broadcast_changes(7    'room:' || NEW.room_id::text || ':messages',8    TG_OP,9    TG_OP,10    TG_TABLE_NAME,11    TG_TABLE_SCHEMA,12    NEW,13    OLD14  );15  RETURN NULL;16END;17$$ LANGUAGE plpgsql SECURITY DEFINER;1819-- Apply trigger to your messages table20CREATE TRIGGER messages_broadcast_trigger21  AFTER INSERT OR UPDATE OR DELETE ON messages22  FOR EACH ROW EXECUTE FUNCTION broadcast_message_changes();
```

**Using `realtime.send` (Best for custom notifications and filtered data)**

```
1-- Create a trigger function for custom notifications2CREATE OR REPLACE FUNCTION notify_message_activity()3RETURNS TRIGGER AS $$4BEGIN5  -- Send custom notification when new message is created6  IF TG_OP = 'INSERT' THEN7    PERFORM realtime.send(8      jsonb_build_object(9        'message_id', NEW.id,10        'user_id', NEW.user_id,11        'room_id', NEW.room_id,12        'created_at', NEW.created_at13      ),14      'message_created',15      'room:' || NEW.room_id::text || ':notifications',16      true  -- private channel17    );18  END IF;1920  RETURN NULL;21END;22$$ LANGUAGE plpgsql SECURITY DEFINER;2324-- Apply trigger to your messages table25CREATE TRIGGER messages_notification_trigger26  AFTER INSERT ON messages27  FOR EACH ROW EXECUTE FUNCTION notify_message_activity();
```

*   **`realtime.broadcast_changes`** sends the full database change with metadata
*   **`realtime.send`** allows you to send custom payloads and control exactly what data is broadcast

## Essential best practices[#](#essential-best-practices)

### Use private channels[#](#use-private-channels)

Always use private channels for production applications to ensure proper security and authorization:

```
1const channel = supabase.channel('room:123:messages', {2  config: { private: true },3})
```

### Follow naming conventions[#](#follow-naming-conventions)

**Channel Topics:** Use the pattern `scope:id:entity`

*   `room:123:messages` - Messages in room 123
*   `game:456:moves` - Game moves for game 456
*   `user:789:notifications` - Notifications for user 789

### Clean up subscriptions[#](#clean-up-subscriptions)

Always unsubscribe when you are done with a channel to ensure you free up resources:

```
1// React example2import { useEffect } from 'react'34useEffect(() => {5  const channel = supabase.channel('room:123:messages')67  return () => {8    supabase.removeChannel(channel)9  }10}, [])
```

## Choose the right feature[#](#choose-the-right-feature)

### When to use Broadcast[#](#when-to-use-broadcast)

*   Real-time messaging and notifications
*   Custom events and game state
*   Database change notifications (with triggers)
*   High-frequency updates (e.g. Cursor tracking)
*   Most use cases

### When to use Presence[#](#when-to-use-presence)

*   User online/offline status
*   Active user counters
*   Use minimally due to computational overhead

### When to use Postgres Changes[#](#when-to-use-postgres-changes)

*   Quick testing and development
*   Low amount of connected users

## Next steps[#](#next-steps)

Now that you understand the basics, dive deeper into each feature:

### Core features[#](#core-features)

*   **[Broadcast](/docs/guides/realtime/broadcast)** - Learn about sending messages, database triggers, and REST API usage
*   **[Presence](/docs/guides/realtime/presence)** - Implement user state tracking and online indicators
*   **[Postgres Changes](/docs/guides/realtime/postgres-changes)** - Understanding database change listeners (consider migrating to Broadcast)

### Security & configuration[#](#security--configuration)

*   **[Authorization](/docs/guides/realtime/authorization)** - Set up RLS policies for private channels
*   **[Settings](/docs/guides/realtime/settings)** - Configure your Realtime instance for optimal performance

### Advanced topics[#](#advanced-topics)

*   **[Architecture](/docs/guides/realtime/architecture)** - Understand how Realtime works under the hood
*   **[Benchmarks](/docs/guides/realtime/benchmarks)** - Performance characteristics and scaling considerations
*   **[Limits](/docs/guides/realtime/limits)** - Usage limits and best practices

### Integration guides[#](#integration-guides)

*   **[Realtime with Next.js](/docs/guides/realtime/realtime-with-nextjs)** - Build real-time Next.js applications
*   **[User Presence](/docs/guides/realtime/realtime-user-presence)** - Implement user presence features
*   **[Database Changes](/docs/guides/realtime/subscribing-to-database-changes)** - Listen to database changes

### Framework examples[#](#framework-examples)

*   **[Flutter Integration](/docs/guides/realtime/realtime-listening-flutter)** - Build real-time Flutter applications

Ready to build something amazing? Start with the [Broadcast guide](/docs/guides/realtime/broadcast) to create your first real-time feature!
