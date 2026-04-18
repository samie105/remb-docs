---
title: "diagnostics_channel - Node documentation"
source: "https://docs.deno.com/api/node/diagnostics_channel/"
canonical_url: "https://docs.deno.com/api/node/diagnostics_channel/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:57.991Z"
content_hash: "0712263961e902488513bb4cb333c22197ecf7b9e258748f7777cf6d8e838077"
menu_path: ["diagnostics_channel - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/dgram/index.md", "title": "dgram - Node documentation"}
nav_next: {"path": "deno/deno/api/node/dns/index.md", "title": "dns - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:diagnostics_channel";
```

The `node:diagnostics_channel` module provides an API to create named channels to report arbitrary message data for diagnostics purposes.

It can be accessed using:

```js
import diagnostics_channel from 'node:diagnostics_channel';
```

It is intended that a module writer wanting to report diagnostics messages will create one or many top-level channels to report messages through. Channels may also be acquired at runtime but it is not encouraged due to the additional overhead of doing so. Channels may be exported for convenience, but as long as the name is known it can be acquired anywhere.

If you intend for your module to produce diagnostics data for others to consume it is recommended that you include documentation of what named channels are used along with the shape of the message data. Channel names should generally include the module name to avoid collisions with data from other modules.

### Classes [#](#Classes)

c

[Channel](.././diagnostics_channel/~/Channel "Channel")

The class `Channel` represents an individual named channel within the data pipeline. It is used to track subscribers and to publish messages when there are subscribers present. It exists as a separate object to avoid channel lookups at publish time, enabling very fast publish speeds and allowing for heavy use while incurring very minimal cost. Channels are created with [channel](.././diagnostics_channel/~/channel), constructing a channel directly with `new Channel(name)` is not supported.

*   [bindStore](.././diagnostics_channel/~/Channel#method_bindstore_0)
*   [hasSubscribers](.././diagnostics_channel/~/Channel#property_hassubscribers)
*   [name](.././diagnostics_channel/~/Channel#property_name)
*   [publish](.././diagnostics_channel/~/Channel#method_publish_0)
*   [runStores](.././diagnostics_channel/~/Channel#method_runstores_0)
*   [subscribe](.././diagnostics_channel/~/Channel#method_subscribe_0)
*   [unbindStore](.././diagnostics_channel/~/Channel#method_unbindstore_0)
*   [unsubscribe](.././diagnostics_channel/~/Channel#method_unsubscribe_0)

c

[TracingChannel](.././diagnostics_channel/~/TracingChannel "TracingChannel")

The class `TracingChannel` is a collection of `TracingChannel Channels` which together express a single traceable action. It is used to formalize and simplify the process of producing events for tracing application flow. [tracingChannel](.././diagnostics_channel/~/tracingChannel) is used to construct a `TracingChannel`. As with `Channel` it is recommended to create and reuse a single `TracingChannel` at the top-level of the file rather than creating them dynamically.

*   [asyncEnd](.././diagnostics_channel/~/TracingChannel#property_asyncend)
*   [asyncStart](.././diagnostics_channel/~/TracingChannel#property_asyncstart)
*   [end](.././diagnostics_channel/~/TracingChannel#property_end)
*   [error](.././diagnostics_channel/~/TracingChannel#property_error)
*   [start](.././diagnostics_channel/~/TracingChannel#property_start)
*   [subscribe](.././diagnostics_channel/~/TracingChannel#method_subscribe_0)
*   [traceCallback](.././diagnostics_channel/~/TracingChannel#method_tracecallback_0)
*   [tracePromise](.././diagnostics_channel/~/TracingChannel#method_tracepromise_0)
*   [traceSync](.././diagnostics_channel/~/TracingChannel#method_tracesync_0)
*   [unsubscribe](.././diagnostics_channel/~/TracingChannel#method_unsubscribe_0)

### Functions [#](#Functions)

f

[channel](.././diagnostics_channel/~/channel "channel")

This is the primary entry-point for anyone wanting to publish to a named channel. It produces a channel object which is optimized to reduce overhead at publish time as much as possible.

f

[hasSubscribers](.././diagnostics_channel/~/hasSubscribers "hasSubscribers")

Check if there are active subscribers to the named channel. This is helpful if the message you want to send might be expensive to prepare.

f

[subscribe](.././diagnostics_channel/~/subscribe "subscribe")

Register a message handler to subscribe to this channel. This message handler will be run synchronously whenever a message is published to the channel. Any errors thrown in the message handler will trigger an `'uncaughtException'`.

f

[tracingChannel](.././diagnostics_channel/~/tracingChannel "tracingChannel")

Creates a `TracingChannel` wrapper for the given `TracingChannel Channels`. If a name is given, the corresponding tracing channels will be created in the form of `tracing:${name}:${eventType}` where `eventType` corresponds to the types of `TracingChannel Channels`.

f

[unsubscribe](.././diagnostics_channel/~/unsubscribe "unsubscribe")

Remove a message handler previously registered to this channel with [subscribe](.././diagnostics_channel/~/subscribe).

### Interfaces [#](#Interfaces)

I

[TracingChannelCollection](.././diagnostics_channel/~/TracingChannelCollection "TracingChannelCollection")

No documentation available

*   [asyncEnd](.././diagnostics_channel/~/TracingChannelCollection#property_asyncend)
*   [asyncStart](.././diagnostics_channel/~/TracingChannelCollection#property_asyncstart)
*   [end](.././diagnostics_channel/~/TracingChannelCollection#property_end)
*   [error](.././diagnostics_channel/~/TracingChannelCollection#property_error)
*   [start](.././diagnostics_channel/~/TracingChannelCollection#property_start)

I

[TracingChannelSubscribers](.././diagnostics_channel/~/TracingChannelSubscribers "TracingChannelSubscribers")

No documentation available

*   [asyncEnd](.././diagnostics_channel/~/TracingChannelSubscribers#property_asyncend)
*   [asyncStart](.././diagnostics_channel/~/TracingChannelSubscribers#property_asyncstart)
*   [end](.././diagnostics_channel/~/TracingChannelSubscribers#property_end)
*   [error](.././diagnostics_channel/~/TracingChannelSubscribers#property_error)
*   [start](.././diagnostics_channel/~/TracingChannelSubscribers#property_start)

### Type Aliases [#](<#Type Aliases>)

T

[ChannelListener](.././diagnostics_channel/~/ChannelListener "ChannelListener")

No documentation available

