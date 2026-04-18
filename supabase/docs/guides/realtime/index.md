---
title: "Realtime"
source: "https://supabase.com/docs/guides/realtime"
canonical_url: "https://supabase.com/docs/guides/realtime"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:33.930Z"
content_hash: "18c828d605656ea98cf3406660cac08a66faf5b4bb3093df8e14f378b1a5d528"
menu_path: ["Realtime","Realtime","Overview","Overview"]
section_path: ["Realtime","Realtime","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/local-development/index.md", "title": "Local Development & CLI"}
nav_next: {"path": "supabase/docs/guides/queues/index.md", "title": "Supabase Queues"}
---

# 

Realtime

## 

Send and receive messages to connected clients.

* * *

Supabase provides a globally distributed [Realtime](https://github.com/supabase/realtime) service with the following features:

*   [Broadcast](/docs/guides/realtime/broadcast): Send low-latency messages between clients. Perfect for real-time messaging, database changes, cursor tracking, game events, and custom notifications.
*   [Presence](/docs/guides/realtime/presence): Track and synchronize user state across clients. Ideal for showing who's online, or active participants.
*   [Postgres Changes](/docs/guides/realtime/postgres-changes): Listen to database changes in real-time.

## What can you build?[#](#what-can-you-build)

*   **Chat applications** - Real-time messaging with typing indicators and online presence
*   **Collaborative tools** - Document editing, whiteboards, and shared workspaces
*   **Live dashboards** - Real-time data visualization and monitoring
*   **Multiplayer games** - Synchronized game state and player interactions
*   **Social features** - Live notifications, reactions, and user activity feeds

Check the [Getting Started](/docs/guides/realtime/getting_started) guide to get started.

## Examples[#](#examples)

[

Multiplayer.dev

Showcase application displaying cursor movements and chat messages using Broadcast.

](https://multiplayer.dev)

[

Chat

Supabase UI chat component using Broadcast to send message between users.

](https://supabase.com/ui/docs/nextjs/realtime-chat)

[

Avatar Stack

Supabase UI avatar stack component using Presence to track connected users.

](https://supabase.com/ui/docs/nextjs/realtime-avatar-stack)

[

Realtime Cursor

Supabase UI realtime cursor component using Broadcast to share users' cursors to build collaborative applications.

](https://supabase.com/ui/docs/nextjs/realtime-cursor)

## Resources[#](#resources)

Find the source code and documentation in the Supabase GitHub repository.

[

Supabase Realtime

View the source code.

](https://github.com/supabase/realtime)

[

Realtime: Multiplayer Edition

Read more about Supabase Realtime.

](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability)

