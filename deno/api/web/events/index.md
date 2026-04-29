---
title: "Events - Web documentation"
source: "https://docs.deno.com/api/web/events"
canonical_url: "https://docs.deno.com/api/web/events"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:58:02.340Z"
content_hash: "e5c0ea997fe4d6b30f0f3023314eb3165cefce22d067ff0960395d99766302c9"
menu_path: ["Events - Web documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../encoding/index.md", "title": "Encoding - Web documentation"}
nav_next: {"path": "../fetch/index.md", "title": "Fetch - Web documentation"}
---

f

[addEventListener](./././~/addEventListener "addEventListener")

Registers an event listener in the global scope, which will be called synchronously whenever the event `type` is dispatched.

f

[dispatchEvent](./././~/dispatchEvent "dispatchEvent")

Dispatches an event in the global scope, synchronously invoking any registered event listeners for this event in the appropriate order. Returns false if event is cancelable and at least one of the event handlers which handled this event called Event.preventDefault(). Otherwise it returns true.

f

[removeEventListener](./././~/removeEventListener "removeEventListener")

Remove a previously registered event listener from the global scope

I

[AddEventListenerOptions](./././~/AddEventListenerOptions "AddEventListenerOptions")

Options for configuring an event listener via `addEventListener`.

-   [once](./././~/AddEventListenerOptions#property_once)
-   [passive](./././~/AddEventListenerOptions#property_passive)
-   [signal](./././~/AddEventListenerOptions#property_signal)

I

v

[CustomEvent](./././~/CustomEvent "CustomEvent")

No documentation available

-   [detail](./././~/CustomEvent#property_detail)
-   [prototype](./././~/CustomEvent#property_prototype)

I

[CustomEventInit](./././~/CustomEventInit "CustomEventInit")

No documentation available

-   [detail](./././~/CustomEventInit#property_detail)

I

v

[ErrorEvent](./././~/ErrorEvent "ErrorEvent")

No documentation available

-   [colno](./././~/ErrorEvent#property_colno)
-   [error](./././~/ErrorEvent#property_error)
-   [filename](./././~/ErrorEvent#property_filename)
-   [lineno](./././~/ErrorEvent#property_lineno)
-   [message](./././~/ErrorEvent#property_message)
-   [prototype](./././~/ErrorEvent#property_prototype)

I

[ErrorEventInit](./././~/ErrorEventInit "ErrorEventInit")

No documentation available

-   [colno](./././~/ErrorEventInit#property_colno)
-   [error](./././~/ErrorEventInit#property_error)
-   [filename](./././~/ErrorEventInit#property_filename)
-   [lineno](./././~/ErrorEventInit#property_lineno)
-   [message](./././~/ErrorEventInit#property_message)

I

v

[Event](./././~/Event "Event")

An event which takes place in the DOM.

-   [AT\_TARGET](./././~/Event#property_at_target)
-   [BUBBLING\_PHASE](./././~/Event#property_bubbling_phase)
-   [CAPTURING\_PHASE](./././~/Event#property_capturing_phase)
-   [NONE](./././~/Event#property_none)
-   [bubbles](./././~/Event#property_bubbles)
-   [cancelBubble](./././~/Event#property_cancelbubble)
-   [cancelable](./././~/Event#property_cancelable)
-   [composed](./././~/Event#property_composed)
-   [composedPath](./././~/Event#method_composedpath_0)
-   [currentTarget](./././~/Event#property_currenttarget)
-   [defaultPrevented](./././~/Event#property_defaultprevented)
-   [eventPhase](./././~/Event#property_eventphase)
-   [initEvent](./././~/Event#method_initevent_0)
-   [isTrusted](./././~/Event#property_istrusted)
-   [preventDefault](./././~/Event#method_preventdefault_0)
-   [prototype](./././~/Event#property_prototype)
-   [returnValue](./././~/Event#property_returnvalue)
-   [srcElement](./././~/Event#property_srcelement)
-   [stopImmediatePropagation](./././~/Event#method_stopimmediatepropagation_0)
-   [stopPropagation](./././~/Event#method_stoppropagation_0)
-   [target](./././~/Event#property_target)
-   [timeStamp](./././~/Event#property_timestamp)
-   [type](./././~/Event#property_type)

I

[EventInit](./././~/EventInit "EventInit")

No documentation available

-   [bubbles](./././~/EventInit#property_bubbles)
-   [cancelable](./././~/EventInit#property_cancelable)
-   [composed](./././~/EventInit#property_composed)

I

[EventListener](./././~/EventListener "EventListener")

No documentation available

I

[EventListenerObject](./././~/EventListenerObject "EventListenerObject")

The `EventListenerObject` interface represents an object that can handle events dispatched by an `EventTarget` object.

-   [handleEvent](./././~/EventListenerObject#method_handleevent_0)

I

[EventListenerOptions](./././~/EventListenerOptions "EventListenerOptions")

No documentation available

-   [capture](./././~/EventListenerOptions#property_capture)

I

v

[EventTarget](./././~/EventTarget "EventTarget")

EventTarget is a DOM interface implemented by objects that can receive events and may have listeners for them.

-   [addEventListener](./././~/EventTarget#method_addeventlistener_0)
-   [dispatchEvent](./././~/EventTarget#method_dispatchevent_0)
-   [prototype](./././~/EventTarget#property_prototype)
-   [removeEventListener](./././~/EventTarget#method_removeeventlistener_0)

I

v

[MessageEvent](./././~/MessageEvent "MessageEvent")

No documentation available

-   [data](./././~/MessageEvent#property_data)
-   [initMessageEvent](./././~/MessageEvent#method_initmessageevent_0)
-   [lastEventId](./././~/MessageEvent#property_lasteventid)
-   [origin](./././~/MessageEvent#property_origin)
-   [ports](./././~/MessageEvent#property_ports)
-   [prototype](./././~/MessageEvent#property_prototype)
-   [source](./././~/MessageEvent#property_source)

I

[MessageEventInit](./././~/MessageEventInit "MessageEventInit")

No documentation available

-   [data](./././~/MessageEventInit#property_data)
-   [lastEventId](./././~/MessageEventInit#property_lasteventid)
-   [origin](./././~/MessageEventInit#property_origin)
-   [ports](./././~/MessageEventInit#property_ports)
-   [source](./././~/MessageEventInit#property_source)

I

v

[ProgressEvent](./././~/ProgressEvent "ProgressEvent")

Events measuring progress of an underlying process, like an HTTP request (for an XMLHttpRequest, or the loading of the underlying resource of an ,

, ,
