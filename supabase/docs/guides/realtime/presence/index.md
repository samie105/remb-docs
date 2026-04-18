---
title: "Presence"
source: "https://supabase.com/docs/guides/realtime/presence"
canonical_url: "https://supabase.com/docs/guides/realtime/presence"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:19.651Z"
content_hash: "1051c368dca22d589c38a38b459a0d220dae17762b69c9684be0e4dccd54e59b"
menu_path: ["Realtime","Realtime","Usage","Usage","Presence","Presence"]
section_path: ["Realtime","Realtime","Usage","Usage","Presence","Presence"]
nav_prev: {"path": "supabase/docs/guides/realtime/postgres-changes/index.md", "title": "Postgres Changes"}
nav_next: {"path": "supabase/docs/guides/realtime/pricing/index.md", "title": "Realtime Pricing"}
---

# 

Presence

## 

Share state between users with Realtime Presence.

* * *

Let's explore how to implement Realtime Presence to track state between multiple users.

## Usage[#](#usage)

You can use the Supabase client libraries to track Presence state between users.

### How Presence works[#](#how-presence-works)

Presence lets each connected client publish a small piece of state—called a “presence payload”—to a shared channel. Supabase stores each client’s payload under a unique presence key and keeps a merged view of all connected clients.

When any client subscribes, disconnects, or updates their presence payload, Supabase triggers one of three events:

*   **`sync`** — the full presence state has been updated
*   **`join`** — a new client has started tracking presence
*   **`leave`** — a client has stopped tracking presence

##### Sync event behavior

During a `sync` event, you may receive `join` and `leave` events simultaneously, even though no users are actually joining or leaving. This is expected behavior—Presence reconciles its local state with the server state, which can trigger these events as part of the synchronization process. This reflects state reconciliation, not real user movement.

The complete presence state returned by `presenceState()` looks like this:

```
1{2  "client_key_1": [{ "userId": 1, "typing": false }],3  "client_key_2": [{ "userId": 2, "typing": true }]4}
```

### Initialize the client[#](#initialize-the-client)

Get the Project URL and key from [the project's **Connect** dialog](/dashboard/project/_?showConnect=true).

##### Changes to API keys

Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

In most cases, you can get the correct key from [the Project's **Connect** dialog](/dashboard/project/_?showConnect=true), but if you want a specific key, you can find all keys in [the API Keys section of a Project's Settings page](/dashboard/project/_/settings/api-keys/):

*   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
*   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.

```
1import { createClient } from '@supabase/supabase-js'23const SUPABASE_URL = 'https://<project>.supabase.co'4const SUPABASE_KEY = '<sb_publishable_... key>'56const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
```

### Sync and track state[#](#sync-and-track-state)

Listen to the `sync`, `join`, and `leave` events triggered whenever any client joins or leaves the channel or changes their slice of state:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('your_project_url', 'your_supabase_api_key')45// ---cut---6const roomOne = supabase.channel('room_01')78roomOne9  .on('presence', { event: 'sync' }, () => {10    const newState = roomOne.presenceState()11    console.log('sync', newState)12  })13  .on('presence', { event: 'join' }, ({ key, newPresences }) => {14    console.log('join', key, newPresences)15  })16  .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {17    console.log('leave', key, leftPresences)18  })19  .subscribe()
```

### Sending state[#](#sending-state)

You can send state to all subscribers using `track()`:

```
1import { createClient } from '@supabase/supabase-js'2const supabase = createClient('your_project_url', 'your_supabase_api_key')34// ---cut---5const roomOne = supabase.channel('room_01')67const userStatus = {8  user: 'user-1',9  online_at: new Date().toISOString(),10}1112roomOne.subscribe(async (status) => {13  if (status !== 'SUBSCRIBED') { return }1415  const presenceTrackStatus = await roomOne.track(userStatus)16  console.log(presenceTrackStatus)17})
```

A client will receive state from any other client that is subscribed to the same topic (in this case `room_01`). It will also automatically trigger its own `sync` and `join` event handlers.

### Stop tracking[#](#stop-tracking)

You can stop tracking presence using the `untrack()` method. This will trigger the `sync` and `leave` event handlers.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('your_project_url', 'your_supabase_api_key')4const roomOne = supabase.channel('room_01')56// ---cut---7const untrackPresence = async () => {8  const presenceUntrackStatus = await roomOne.untrack()9  console.log(presenceUntrackStatus)10}1112untrackPresence()
```

## Presence options[#](#presence-options)

You can pass configuration options while initializing the Supabase Client.

### Presence key[#](#presence-key)

By default, Presence will generate a unique `UUIDv1` key on the server to track a client channel's state. If you prefer, you can provide a custom key when creating the channel. This key should be unique among clients.

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('SUPABASE_URL', 'SUPABASE_PUBLISHABLE_KEY')45const channelC = supabase.channel('test', {6  config: {7    presence: {8      key: 'userId-123',9    },10  },11})
```
