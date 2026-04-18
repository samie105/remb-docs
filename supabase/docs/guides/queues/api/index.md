---
title: "API"
source: "https://supabase.com/docs/guides/queues/api"
canonical_url: "https://supabase.com/docs/guides/queues/api"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:23.559Z"
content_hash: "aab1c1c9be2c25b10b46aa1fe7d356014dd6f33e51c9d4309ebc96c6dd536426"
menu_path: ["Queues","Queues","References","References","API","API"]
section_path: ["Queues","Queues","References","References","API","API"]
---
# 

API

* * *

When you create a Queue in Supabase, you can choose to create helper database functions in the `pgmq_public` schema. This schema exposes operations to manage Queue Messages to consumers client-side, but does not expose functions for creating or dropping Queues.

Database functions in `pgmq_public` can be exposed via Supabase Data API so consumers client-side can call them. Visit the [Quickstart](/docs/guides/queues/quickstart) for an example.

### `pgmq_public.pop(queue_name)`[#](#pgmqpublicpopqueuename)

Retrieves the next available message and deletes it from the specified Queue.

*   `queue_name` (`text`): Queue name

* * *

### `pgmq_public.send(queue_name, message, sleep_seconds)`[#](#pgmqpublicsendqueuename-message-sleepseconds)

Adds a Message to the specified Queue, optionally delaying its visibility to all consumers by a number of seconds.

*   `queue_name` (`text`): Queue name
*   `message` (`jsonb`): Message payload to send
*   `sleep_seconds` (`integer`, optional): Delay message visibility by specified seconds. Defaults to 0

* * *

### `pgmq_public.send_batch(queue_name, messages, sleep_seconds)`[#](#pgmqpublicsendbatchqueuename-messages-sleepseconds)

Adds a batch of Messages to the specified Queue, optionally delaying their availability to all consumers by a number of seconds.

*   `queue_name` (`text`): Queue name
*   `messages` (`jsonb[]`): Array of message payloads to send
*   `sleep_seconds` (`integer`, optional): Delay messages visibility by specified seconds. Defaults to 0

* * *

### `pgmq_public.archive(queue_name, message_id)`[#](#pgmqpublicarchivequeuename-messageid)

Archives a Message by moving it from the Queue table to the Queue's archive table.

*   `queue_name` (`text`): Queue name
*   `message_id` (`bigint`): ID of the Message to archive

* * *

### `pgmq_public.delete(queue_name, message_id)`[#](#pgmqpublicdeletequeuename-messageid)

Permanently deletes a Message from the specified Queue.

*   `queue_name` (`text`): Queue name
*   `message_id` (`bigint`): ID of the Message to delete

* * *

### `pgmq_public.read(queue_name, sleep_seconds, n)`[#](#pgmqpublicreadqueuename-sleepseconds-n)

Reads up to "n" Messages from the specified Queue with an optional "sleep\_seconds" (visibility timeout).

*   `queue_name` (`text`): Queue name
*   `sleep_seconds` (`integer`): Visibility timeout in seconds
*   `n` (`integer`): Maximum number of Messages to read
