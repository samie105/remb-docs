---
title: "PGMQ Extension"
source: "https://supabase.com/docs/guides/queues/pgmq"
canonical_url: "https://supabase.com/docs/guides/queues/pgmq"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:36.469Z"
content_hash: "e44481a88a5f12aef34087ef95e52391f5db8bdc00616c47338c1b972c70cdf1"
menu_path: ["Queues","Queues","References","References","PGMQ Extension","PGMQ Extension"]
section_path: ["Queues","Queues","References","References","PGMQ Extension","PGMQ Extension"]
---
# 

PGMQ Extension

* * *

pgmq is a lightweight message queue built on Postgres.

## Features[#](#features)

*   Lightweight - No background worker or external dependencies, just Postgres functions packaged in an extension
*   "exactly once" delivery of messages to a consumer within a visibility timeout
*   API parity with AWS SQS and RSMQ
*   Messages stay in the queue until explicitly removed
*   Messages can be archived, instead of deleted, for long-term retention and replayability

## Enable the extension[#](#enable-the-extension)

```
1create extension pgmq;
```

## Usage [#](#get-usage)

### Queue management[#](#queue-management)

#### `create`[#](#create)

Create a new queue.

```
1pgmq.create(queue_name text)2returns void
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

```
1select from pgmq.create('my_queue');2 create3--------
```

#### `create_unlogged`[#](#createunlogged)

Creates an unlogged table. This is useful when write throughput is more important than durability. See Postgres documentation for [unlogged tables](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-UNLOGGED) for more information.

```
1pgmq.create_unlogged(queue_name text)2returns void
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

```
1select pgmq.create_unlogged('my_unlogged');2 create_unlogged3-----------------
```

* * *

#### `detach_archive`[#](#detacharchive)

Drop the queue's archive table as a member of the PGMQ extension. Useful for preventing the queue's archive table from being dropped when `drop extension pgmq` is executed. This does not prevent the further archives() from appending to the archive table.

```
1pgmq.detach_archive(queue_name text)
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

```
1select * from pgmq.detach_archive('my_queue');2 detach_archive3----------------
```

* * *

#### `drop_queue`[#](#dropqueue)

Deletes a queue and its archive table.

```
1pgmq.drop_queue(queue_name text)2returns boolean
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

```
1select * from pgmq.drop_queue('my_unlogged');2 drop_queue3------------4 t
```

### Sending messages[#](#sending-messages)

#### `send`[#](#send)

Send a single message to a queue.

```
1pgmq.send(2    queue_name text,3    msg jsonb,4    delay integer default 05)6returns setof bigint
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg`

`jsonb`

The message to send to the queue

`delay`

`integer`

Time in seconds before the message becomes visible. Defaults to 0.

Example:

```
1select * from pgmq.send('my_queue', '{"hello": "world"}');2 send3------4    4
```

* * *

#### `send_batch`[#](#sendbatch)

Send 1 or more messages to a queue.

```
1pgmq.send_batch(2    queue_name text,3    msgs jsonb[],4    delay integer default 05)6returns setof bigint
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msgs`

`jsonb[]`

Array of messages to send to the queue

`delay`

`integer`

Time in seconds before the messages becomes visible. Defaults to 0.

```
1select * from pgmq.send_batch(2    'my_queue',3    array[4      '{"hello": "world_0"}'::jsonb,5      '{"hello": "world_1"}'::jsonb6    ]7);8 send_batch9------------10          111          2
```

* * *

### Reading messages[#](#reading-messages)

#### `read`[#](#read)

Read 1 or more messages from a queue. The VT specifies the duration of time in seconds that the message is invisible to other consumers. At the end of that duration, the message is visible again and could be read by other consumers.

```
1pgmq.read(2    queue_name text,3    vt integer,4    qty integer5)67returns setof pgmq.message_record
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`vt`

`integer`

Time in seconds that the message become invisible after reading

`qty`

`integer`

The number of messages to read from the queue. Defaults to 1

Example:

```
1select * from pgmq.read('my_queue', 10, 2);2 msg_id | read_ct |          enqueued_at          |              vt               |       message3--------+---------+-------------------------------+-------------------------------+----------------------4      1 |       1 | 2023-10-28 19:14:47.356595-05 | 2023-10-28 19:17:08.608922-05 | {"hello": "world_0"}5      2 |       1 | 2023-10-28 19:14:47.356595-05 | 2023-10-28 19:17:08.608974-05 | {"hello": "world_1"}6(2 rows)
```

* * *

#### `read_with_poll`[#](#readwithpoll)

Same as read(). Also provides convenient long-poll functionality. When there are no messages in the queue, the function call will wait for `max_poll_seconds` in duration before returning. If messages reach the queue during that duration, they will be read and returned immediately.

```
1pgmq.read_with_poll(2    queue_name text,3    vt integer,4    qty integer,5    max_poll_seconds integer default 5,6    poll_interval_ms integer default 1007)8returns setof pgmq.message_record
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`vt`

`integer`

Time in seconds that the message become invisible after reading.

`qty`

`integer`

The number of messages to read from the queue. Defaults to 1.

`max_poll_seconds`

`integer`

Time in seconds to wait for new messages to reach the queue. Defaults to 5.

`poll_interval_ms`

`integer`

Milliseconds between the internal poll operations. Defaults to 100.

Example:

```
1select * from pgmq.read_with_poll('my_queue', 1, 1, 5, 100);2 msg_id | read_ct |          enqueued_at          |              vt               |      message3--------+---------+-------------------------------+-------------------------------+--------------------4      1 |       1 | 2023-10-28 19:09:09.177756-05 | 2023-10-28 19:27:00.337929-05 | {"hello": "world"}
```

* * *

#### `pop`[#](#pop)

Reads a single message from a queue and deletes it upon read.

Note: utilization of pop() results in at-most-once delivery semantics if the consuming application does not guarantee processing of the message.

```
1pgmq.pop(queue_name text)2returns setof pgmq.message_record
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

```
1pgmq=# select * from pgmq.pop('my_queue');2 msg_id | read_ct |          enqueued_at          |              vt               |      message3--------+---------+-------------------------------+-------------------------------+--------------------4      1 |       2 | 2023-10-28 19:09:09.177756-05 | 2023-10-28 19:27:00.337929-05 | {"hello": "world"}
```

* * *

### Deleting/Archiving messages[#](#deletingarchiving-messages)

#### `delete` (single)[#](#delete-single)

Deletes a single message from a queue.

```
1pgmq.delete (queue_name text, msg_id: bigint)2returns boolean
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg_id`

`bigint`

Message ID of the message to delete

Example:

```
1select pgmq.delete('my_queue', 5);2 delete3--------4 t
```

* * *

#### `delete` (batch)[#](#delete-batch)

Delete one or many messages from a queue.

```
1pgmq.delete (queue_name text, msg_ids: bigint[])2returns setof bigint
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg_ids`

`bigint[]`

Array of message IDs to delete

Examples:

Delete two messages that exist.

```
1select * from pgmq.delete('my_queue', array[2, 3]);2 delete3--------4      25      3
```

Delete two messages, one that exists and one that does not. Message `999` does not exist.

```
1select * from pgmq.delete('my_queue', array[6, 999]);2 delete3--------4      6
```

* * *

#### `purge_queue`[#](#purgequeue)

Permanently deletes all messages in a queue. Returns the number of messages that were deleted.

```
1purge_queue(queue_name text)2returns bigint
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

Example:

Purge the queue when it contains 8 messages;

```
1select * from pgmq.purge_queue('my_queue');2 purge_queue3-------------4           8
```

* * *

#### `archive` (single)[#](#archive-single)

Removes a single requested message from the specified queue and inserts it into the queue's archive.

```
1pgmq.archive(queue_name text, msg_id bigint)2returns boolean
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg_id`

`bigint`

Message ID of the message to archive

Returns Boolean value indicating success or failure of the operation.

Example; remove message with ID 1 from queue `my_queue` and archive it:

```
1select * from pgmq.archive('my_queue', 1);2 archive3---------4       t
```

* * *

#### `archive` (batch)[#](#archive-batch)

Deletes a batch of requested messages from the specified queue and inserts them into the queue's archive. Returns an array of message ids that were successfully archived.

```
1pgmq.archive(queue_name text, msg_ids bigint[])2RETURNS SETOF bigint
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg_ids`

`bigint[]`

Array of message IDs to archive

Examples:

Delete messages with ID 1 and 2 from queue `my_queue` and move to the archive.

```
1select * from pgmq.archive('my_queue', array[1, 2]);2 archive3---------4       15       2
```

Delete messages 4, which exists and 999, which does not exist.

```
1select * from pgmq.archive('my_queue', array[4, 999]);2 archive3---------4       4
```

* * *

### Utilities[#](#utilities)

#### `set_vt`[#](#setvt)

Sets the visibility timeout of a message to a specified time duration in the future. Returns the record of the message that was updated.

```
1pgmq.set_vt(2    queue_name text,3    msg_id bigint,4    vt_offset integer5)6returns pgmq.message_record
```

**Parameters:**

Parameter

Type

Description

`queue_name`

`text`

The name of the queue

`msg_id`

`bigint`

ID of the message to set visibility time

`vt_offset`

`integer`

Duration from now, in seconds, that the message's VT should be set to

Example:

Set the visibility timeout of message 1 to 30 seconds from now.

```
1select * from pgmq.set_vt('my_queue', 11, 30);2 msg_id | read_ct |          enqueued_at          |              vt               |       message3--------+---------+-------------------------------+-------------------------------+----------------------4     1 |       0 | 2023-10-28 19:42:21.778741-05 | 2023-10-28 19:59:34.286462-05 | {"hello": "world_0"}
```

* * *

#### `list_queues`[#](#listqueues)

List all the queues that currently exist.

```
1list_queues()2RETURNS TABLE(3    queue_name text,4    created_at timestamp with time zone,5    is_partitioned boolean,6    is_unlogged boolean7)
```

Example:

```
1select * from pgmq.list_queues();2      queue_name      |          created_at           | is_partitioned | is_unlogged3----------------------+-------------------------------+----------------+-------------4 my_queue             | 2023-10-28 14:13:17.092576-05 | f              | f5 my_partitioned_queue | 2023-10-28 19:47:37.098692-05 | t              | f6 my_unlogged          | 2023-10-28 20:02:30.976109-05 | f              | t
```

* * *

#### `metrics`[#](#metrics)

Get metrics for a specific queue.

```
1pgmq.metrics(queue_name: text)2returns table(3    queue_name text,4    queue_length bigint,5    newest_msg_age_sec integer,6    oldest_msg_age_sec integer,7    total_messages bigint,8    scrape_time timestamp with time zone9)
```

**Parameters:**

Parameter

Type

Description

queue\_name

text

The name of the queue

**Returns:**

| Attribute | Type | Description | | :------------------- | :------------------------- | :------------------------------------------------------------------------ | -------------------------------------------------- | | `queue_name` | `text` | The name of the queue | | `queue_length` | `bigint` | Number of messages currently in the queue | | `newest_msg_age_sec` | `integer | null` | Age of the newest message in the queue, in seconds | | `oldest_msg_age_sec` | `integer | null` | Age of the oldest message in the queue, in seconds | | `total_messages` | `bigint` | Total number of messages that have passed through the queue over all time | | `scrape_time` | `timestamp with time zone` | The current timestamp |

Example:

```
1select * from pgmq.metrics('my_queue');2 queue_name | queue_length | newest_msg_age_sec | oldest_msg_age_sec | total_messages |          scrape_time3------------+--------------+--------------------+--------------------+----------------+-------------------------------4 my_queue   |           16 |               2445 |               2447 |             35 | 2023-10-28 20:23:08.406259-05
```

* * *

#### `metrics_all`[#](#metricsall)

Get metrics for all existing queues.

```
1pgmq.metrics_all()2RETURNS TABLE(3    queue_name text,4    queue_length bigint,5    newest_msg_age_sec integer,6    oldest_msg_age_sec integer,7    total_messages bigint,8    scrape_time timestamp with time zone9)
```

**Returns:**

| Attribute | Type | Description | | :------------------- | :------------------------- | :------------------------------------------------------------------------ | -------------------------------------------------- | | `queue_name` | `text` | The name of the queue | | `queue_length` | `bigint` | Number of messages currently in the queue | | `newest_msg_age_sec` | `integer | null` | Age of the newest message in the queue, in seconds | | `oldest_msg_age_sec` | `integer | null` | Age of the oldest message in the queue, in seconds | | `total_messages` | `bigint` | Total number of messages that have passed through the queue over all time | | `scrape_time` | `timestamp with time zone` | The current timestamp |

```
1select * from pgmq.metrics_all();2      queue_name      | queue_length | newest_msg_age_sec | oldest_msg_age_sec | total_messages |          scrape_time3----------------------+--------------+--------------------+--------------------+----------------+-------------------------------4 my_queue             |           16 |               2563 |               2565 |             35 | 2023-10-28 20:25:07.016413-055 my_partitioned_queue |            1 |                 11 |                 11 |              1 | 2023-10-28 20:25:07.016413-056 my_unlogged          |            1 |                  3 |                  3 |              1 | 2023-10-28 20:25:07.016413-05
```

### Types[#](#types)

#### `message_record`[#](#messagerecord)

The complete representation of a message in a queue.

Attribute Name

Type

Description

`msg_id`

`bigint`

Unique ID of the message

`read_ct`

`bigint`

Number of times the message has been read. Increments on read().

`enqueued_at`

`timestamp with time zone`

time that the message was inserted into the queue

`vt`

`timestamp with time zone`

Timestamp when the message will become available for consumers to read

`message`

`jsonb`

The message payload

Example:

```
1msg_id | read_ct |          enqueued_at          |              vt               |      message2--------+---------+-------------------------------+-------------------------------+--------------------3      1 |       1 | 2023-10-28 19:06:19.941509-05 | 2023-10-28 19:06:27.419392-05 | {"hello": "world"}
```

## Resources[#](#resources)

*   Official Docs: [pgmq/api](https://pgmq.github.io/pgmq/#creating-a-queue)
