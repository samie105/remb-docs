---
title: "Consuming Supabase Queue Messages with Edge Functions"
source: "https://supabase.com/docs/guides/queues/consuming-messages-with-edge-functions"
canonical_url: "https://supabase.com/docs/guides/queues/consuming-messages-with-edge-functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:28.651Z"
content_hash: "33b3b2b8731f1e6f8c6986c9a99c78374764c009b8ab3c9c39fbfa9806dd7c1d"
menu_path: ["Queues","Queues","Getting Started","Getting Started","Consuming Messages with Edge Functions","Consuming Messages with Edge Functions"]
section_path: ["Queues","Queues","Getting Started","Getting Started","Consuming Messages with Edge Functions","Consuming Messages with Edge Functions"]
nav_prev: {"path": "supabase/docs/guides/queues/api/index.md", "title": "API"}
nav_next: {"path": "supabase/docs/guides/queues/expose-self-hosted-queues/index.md", "title": "Expose Queues for local and self-hosted Supabase"}
---

# 

Consuming Supabase Queue Messages with Edge Functions

## 

Learn how to consume Supabase Queue messages server-side with a Supabase Edge Function

* * *

This guide helps you read & process queue messages server-side with a Supabase Edge Function. Read [Queues API Reference](/docs/guides/queues/api) for more details on our API.

## Concepts[#](#concepts)

Supabase Queues is a pull-based Message Queue consisting of three main components: Queues, Messages, and Queue Types. You should already be familiar with the [Queues Quickstart](/docs/guides/queues/quickstart).

### Consuming messages in an Edge Function[#](#consuming-messages-in-an-edge-function)

This is a Supabase Edge Function that reads 5 messages off the queue, processes each of them, and deletes each message when it is done.

```
1import 'jsr:@supabase/functions-js/edge-runtime.d.ts'2import { createClient } from 'npm:@supabase/supabase-js@2'34const supabaseUrl = 'supabaseURL'5const supabaseKey = 'supabaseKey'67const supabase = createClient(supabaseUrl, supabaseKey)8const queueName = 'your_queue_name'910// Type definition for queue messages11interface QueueMessage {12  msg_id: bigint13  read_ct: number14  vt: string15  enqueued_at: string16  message: any17}1819async function processMessage(message: QueueMessage) {20  //21  // Do whatever logic you need to with the message content22  //23  // Delete the message from the queue24  const { error: deleteError } = await supabase.schema('pgmq_public').rpc('delete', {25    queue_name: queueName,26    msg_id: message.msg_id,27  })2829  if (deleteError) {30    console.error(`Failed to delete message ${message.msg_id}:`, deleteError)31  } else {32    console.log(`Message ${message.msg_id} deleted from queue`)33  }34}3536Deno.serve(async (req) => {37  const { data: messages, error } = await supabase.schema('pgmq_public').rpc('read', {38    queue_name: queueName,39    sleep_seconds: 0, // Don't wait if queue is empty40    n: 5, // Read 5 messages off the queue41  })4243  if (error) {44    console.error(`Error reading from ${queueName} queue:`, error)45    return new Response(JSON.stringify({ error: error.message }), {46      status: 500,47      headers: { 'Content-Type': 'application/json' },48    })49  }5051  if (!messages || messages.length === 0) {52    console.log('No messages in workflow_messages queue')53    return new Response(JSON.stringify({ message: 'No messages in queue' }), {54      status: 200,55      headers: { 'Content-Type': 'application/json' },56    })57  }5859  console.log(`Found ${messages.length} messages to process`)6061  // Process each message that was read off the queue62  for (const message of messages) {63    try {64      await processMessage(message as QueueMessage)65    } catch (error) {66      console.error(`Error processing message ${message.msg_id}:`, error)67    }68  }6970  // Return immediately while background processing continues71  return new Response(72    JSON.stringify({73      message: `Processing ${messages.length} messages in background`,74      count: messages.length,75    }),76    {77      status: 200,78      headers: { 'Content-Type': 'application/json' },79    }80  )81})
```

Every time this Edge Function is run it:

1.  Read 5 messages off the queue
2.  Call the `processMessage` function
3.  At the end of `processMessage`, the message is deleted from the queue
4.  If `processMessage` throws an error, the error is logged. In this case, the message is still in the queue, so the next time this Edge Function runs it reads the message again.

You might find this kind of setup handy to run with [Supabase Cron](/docs/guides/cron). You can set up Cron so that every N number of minutes or seconds, the Edge Function will run and process a number of messages off the queue.

Similarly, you can invoke the Edge Function on command at any given time with [`supabase.functions.invoke`](/docs/guides/functions/quickstart-dashboard#usage).

