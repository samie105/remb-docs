---
title: "events - Node documentation"
source: "https://docs.deno.com/api/node/events/"
canonical_url: "https://docs.deno.com/api/node/events/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:44.049Z"
content_hash: "71b44a3785af612e4eb8fd3a0708ef51755c3ffd29b7ca3e316459ac7be8397b"
menu_path: ["events - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/domain/index.md", "title": "domain - Node documentation"}
nav_next: {"path": "deno/deno/api/node/fs/index.md", "title": "fs - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:events";
```

Much of the Node.js core API is built around an idiomatic asynchronous event-driven architecture in which certain kinds of objects (called "emitters") emit named events that cause `Function` objects ("listeners") to be called.

For instance: a `net.Server` object emits an event each time a peer connects to it; a `fs.ReadStream` emits an event when the file is opened; a `stream` emits an event whenever data is available to be read.

All objects that emit events are instances of the `EventEmitter` class. These objects expose an `eventEmitter.on()` function that allows one or more functions to be attached to named events emitted by the object. Typically, event names are camel-cased strings but any valid JavaScript property key can be used.

When the `EventEmitter` object emits an event, all of the functions attached to that specific event are called _synchronously_. Any values returned by the called listeners are _ignored_ and discarded.

The following example shows a simple `EventEmitter` instance with a single listener. The `eventEmitter.on()` method is used to register listeners, while the `eventEmitter.emit()` method is used to trigger the event.

```js
import { EventEmitter } from 'node:events';

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('an event occurred!');
});
myEmitter.emit('event');
```

### Classes [#](#Classes)

c

[EventEmitter.EventEmitterAsyncResource](.././events/~/EventEmitter.EventEmitterAsyncResource "EventEmitter.EventEmitterAsyncResource")

Integrates `EventEmitter` with `AsyncResource` for `EventEmitter`s that require manual async tracking. Specifically, all events emitted by instances of `events.EventEmitterAsyncResource` will run within its `async context`.

*   [asyncId](.././events/~/EventEmitter.EventEmitterAsyncResource#property_asyncid)
*   [asyncResource](.././events/~/EventEmitter.EventEmitterAsyncResource#property_asyncresource)
*   [emitDestroy](.././events/~/EventEmitter.EventEmitterAsyncResource#method_emitdestroy_0)
*   [triggerAsyncId](.././events/~/EventEmitter.EventEmitterAsyncResource#property_triggerasyncid)

### Interfaces [#](#Interfaces)

c

I

N

[EventEmitter](.././events/~/EventEmitter "EventEmitter")

The `EventEmitter` class is defined and exposed by the `node:events` module:

*   [addAbortListener](.././events/~/EventEmitter#method_addabortlistener_0)
*   [addListener](.././events/~/EventEmitter#method_addlistener_0)
*   [captureRejectionSymbol](.././events/~/EventEmitter#property_capturerejectionsymbol)
*   [captureRejections](.././events/~/EventEmitter#property_capturerejections)
*   [defaultMaxListeners](.././events/~/EventEmitter#property_defaultmaxlisteners)
*   [emit](.././events/~/EventEmitter#method_emit_0)
*   [errorMonitor](.././events/~/EventEmitter#property_errormonitor)
*   [eventNames](.././events/~/EventEmitter#method_eventnames_0)
*   [getEventListeners](.././events/~/EventEmitter#method_geteventlisteners_0)
*   [getMaxListeners](.././events/~/EventEmitter#method_getmaxlisteners_0)
*   [listenerCount](.././events/~/EventEmitter#method_listenercount_0)
*   [listeners](.././events/~/EventEmitter#method_listeners_0)
*   [off](.././events/~/EventEmitter#method_off_0)
*   [on](.././events/~/EventEmitter#method_on_0)
*   [once](.././events/~/EventEmitter#method_once_0)
*   [prependListener](.././events/~/EventEmitter#method_prependlistener_0)
*   [prependOnceListener](.././events/~/EventEmitter#method_prependoncelistener_0)
*   [rawListeners](.././events/~/EventEmitter#method_rawlisteners_0)
*   [removeAllListeners](.././events/~/EventEmitter#method_removealllisteners_0)
*   [removeListener](.././events/~/EventEmitter#method_removelistener_0)
*   [setMaxListeners](.././events/~/EventEmitter#method_setmaxlisteners_0)

I

[EventEmitter.Abortable](.././events/~/EventEmitter.Abortable "EventEmitter.Abortable")

No documentation available

*   [signal](.././events/~/EventEmitter.Abortable#property_signal)

I

[EventEmitter.EventEmitterAsyncResourceOptions](.././events/~/EventEmitter.EventEmitterAsyncResourceOptions "EventEmitter.EventEmitterAsyncResourceOptions")

No documentation available

*   [name](.././events/~/EventEmitter.EventEmitterAsyncResourceOptions#property_name)

I

[EventEmitter.EventEmitterReferencingAsyncResource](.././events/~/EventEmitter.EventEmitterReferencingAsyncResource "EventEmitter.EventEmitterReferencingAsyncResource")

No documentation available

*   [eventEmitter](.././events/~/EventEmitter.EventEmitterReferencingAsyncResource#property_eventemitter)

I

[EventEmitterOptions](.././events/~/EventEmitterOptions "EventEmitterOptions")

No documentation available

*   [captureRejections](.././events/~/EventEmitterOptions#property_capturerejections)

I

[StaticEventEmitterIteratorOptions](.././events/~/StaticEventEmitterIteratorOptions "StaticEventEmitterIteratorOptions")

No documentation available

*   [close](.././events/~/StaticEventEmitterIteratorOptions#property_close)
*   [highWaterMark](.././events/~/StaticEventEmitterIteratorOptions#property_highwatermark)
*   [lowWaterMark](.././events/~/StaticEventEmitterIteratorOptions#property_lowwatermark)

I

[StaticEventEmitterOptions](.././events/~/StaticEventEmitterOptions "StaticEventEmitterOptions")

No documentation available

*   [signal](.././events/~/StaticEventEmitterOptions#property_signal)

### Type Aliases [#](<#Type Aliases>)

T

[AnyRest](.././events/~/AnyRest "AnyRest")

No documentation available

T

[Args](.././events/~/Args "Args")

No documentation available

T

[DefaultEventMap](.././events/~/DefaultEventMap "DefaultEventMap")

No documentation available

T

[EventMap](.././events/~/EventMap "EventMap")

No documentation available

T

[Key](.././events/~/Key "Key")

No documentation available

T

[Key2](.././events/~/Key2 "Key2")

No documentation available

T

[Listener](.././events/~/Listener "Listener")

No documentation available

T

[Listener1](.././events/~/Listener1 "Listener1")

No documentation available

T

[Listener2](.././events/~/Listener2 "Listener2")

No documentation available

