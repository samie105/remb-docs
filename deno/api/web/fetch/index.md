---
title: "Fetch - Web documentation"
source: "https://docs.deno.com/api/web/fetch"
canonical_url: "https://docs.deno.com/api/web/fetch"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:58:08.740Z"
content_hash: "453e778b220eeee26c0d4ecb9fa7e232ee0203ef0e92e7010aea8f4e4538a8d9"
menu_path: ["Fetch - Web documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../events/index.md", "title": "Events - Web documentation"}
nav_next: {"path": "../file/index.md", "title": "File - Web documentation"}
---

f

[fetch](./././~/fetch "fetch")

Fetch a resource from the network. It returns a `Promise` that resolves to the `Response` to that `Request`, whether it is successful or not.

I

[Body](./././~/Body "Body")

No documentation available

-   [arrayBuffer](./././~/Body#method_arraybuffer_0)
-   [blob](./././~/Body#method_blob_0)
-   [body](./././~/Body#property_body)
-   [bodyUsed](./././~/Body#property_bodyused)
-   [bytes](./././~/Body#method_bytes_0)
-   [formData](./././~/Body#method_formdata_0)
-   [json](./././~/Body#method_json_0)
-   [text](./././~/Body#method_text_0)

I

v

[EventSource](./././~/EventSource "EventSource")

No documentation available

-   [CLOSED](./././~/EventSource#property_closed)
-   [CONNECTING](./././~/EventSource#property_connecting)
-   [OPEN](./././~/EventSource#property_open)
-   [addEventListener](./././~/EventSource#method_addeventlistener_0)
-   [close](./././~/EventSource#method_close_0)
-   [onerror](./././~/EventSource#property_onerror)
-   [onmessage](./././~/EventSource#property_onmessage)
-   [onopen](./././~/EventSource#property_onopen)
-   [prototype](./././~/EventSource#property_prototype)
-   [readyState](./././~/EventSource#property_readystate)
-   [removeEventListener](./././~/EventSource#method_removeeventlistener_0)
-   [url](./././~/EventSource#property_url)
-   [withCredentials](./././~/EventSource#property_withcredentials)

I

[EventSourceEventMap](./././~/EventSourceEventMap "EventSourceEventMap")

No documentation available

-   [error](./././~/EventSourceEventMap#property_error)
-   [message](./././~/EventSourceEventMap#property_message)
-   [open](./././~/EventSourceEventMap#property_open)

I

[EventSourceInit](./././~/EventSourceInit "EventSourceInit")

No documentation available

-   [headers](./././~/EventSourceInit#property_headers)
-   [withCredentials](./././~/EventSourceInit#property_withcredentials)

I

v

[FormData](./././~/FormData "FormData")

Provides a way to easily construct a set of key/value pairs representing form fields and their values, which can then be easily sent using the XMLHttpRequest.send() method. It uses the same format a form would use if the encoding type were set to "multipart/form-data".

-   [append](./././~/FormData#method_append_0)
-   [delete](./././~/FormData#method_delete_0)
-   [get](./././~/FormData#method_get_0)
-   [getAll](./././~/FormData#method_getall_0)
-   [has](./././~/FormData#method_has_0)
-   [prototype](./././~/FormData#property_prototype)
-   [set](./././~/FormData#method_set_0)

I

v

[Headers](./././~/Headers "Headers")

This Fetch API interface allows you to perform various actions on HTTP request and response headers. These actions include retrieving, setting, adding to, and removing. A Headers object has an associated header list, which is initially empty and consists of zero or more name and value pairs. You can add to this using methods like append() (see Examples). In all methods of this interface, header names are matched by case-insensitive byte sequence.

-   [append](./././~/Headers#method_append_0)
-   [delete](./././~/Headers#method_delete_0)
-   [get](./././~/Headers#method_get_0)
-   [getSetCookie](./././~/Headers#method_getsetcookie_0)
-   [has](./././~/Headers#method_has_0)
-   [prototype](./././~/Headers#property_prototype)
-   [set](./././~/Headers#method_set_0)

I

v

[Request](./././~/Request "Request")

This Fetch API interface represents a resource request.

-   [cache](./././~/Request#property_cache)
-   [clone](./././~/Request#method_clone_0)
-   [credentials](./././~/Request#property_credentials)
-   [destination](./././~/Request#property_destination)
-   [headers](./././~/Request#property_headers)
-   [integrity](./././~/Request#property_integrity)
-   [isHistoryNavigation](./././~/Request#property_ishistorynavigation)
-   [isReloadNavigation](./././~/Request#property_isreloadnavigation)
-   [keepalive](./././~/Request#property_keepalive)
-   [method](./././~/Request#property_method)
-   [mode](./././~/Request#property_mode)
-   [prototype](./././~/Request#property_prototype)
-   [redirect](./././~/Request#property_redirect)
-   [referrer](./././~/Request#property_referrer)
-   [referrerPolicy](./././~/Request#property_referrerpolicy)
-   [signal](./././~/Request#property_signal)
-   [url](./././~/Request#property_url)

I

[RequestInit](./././~/RequestInit "RequestInit")

No documentation available

-   [body](./././~/RequestInit#property_body)
-   [cache](./././~/RequestInit#property_cache)
-   [credentials](./././~/RequestInit#property_credentials)
-   [headers](./././~/RequestInit#property_headers)
-   [integrity](./././~/RequestInit#property_integrity)
-   [keepalive](./././~/RequestInit#property_keepalive)
-   [method](./././~/RequestInit#property_method)
-   [mode](./././~/RequestInit#property_mode)
-   [redirect](./././~/RequestInit#property_redirect)
-   [referrer](./././~/RequestInit#property_referrer)
-   [referrerPolicy](./././~/RequestInit#property_referrerpolicy)
-   [signal](./././~/RequestInit#property_signal)
-   [window](./././~/RequestInit#property_window)

I

v

[Response](./././~/Response "Response")

This Fetch API interface represents the response to a request.

-   [clone](./././~/Response#method_clone_0)
-   [error](./././~/Response#method_error_0)
-   [headers](./././~/Response#property_headers)
-   [json](./././~/Response#method_json_0)
-   [ok](./././~/Response#property_ok)
-   [prototype](./././~/Response#property_prototype)
-   [redirect](./././~/Response#method_redirect_0)
-   [redirected](./././~/Response#property_redirected)
-   [status](./././~/Response#property_status)
-   [statusText](./././~/Response#property_statustext)
-   [type](./././~/Response#property_type)
-   [url](./././~/Response#property_url)

I

[ResponseInit](./././~/ResponseInit "ResponseInit")

No documentation available

-   [headers](./././~/ResponseInit#property_headers)
-   [status](./././~/ResponseInit#property_status)
-   [statusText](./././~/ResponseInit#property_statustext)

T

[BodyInit](./././~/BodyInit "BodyInit")

No documentation available

T

[FormDataEntryValue](./././~/FormDataEntryValue "FormDataEntryValue")

No documentation available

T

[HeadersInit](./././~/HeadersInit "HeadersInit")

No documentation available

T

[ReferrerPolicy](./././~/ReferrerPolicy "ReferrerPolicy")

No documentation available

T

[RequestCache](./././~/RequestCache "RequestCache")

No documentation available

T

[RequestCredentials](./././~/RequestCredentials "RequestCredentials")

No documentation available

T

[RequestDestination](./././~/RequestDestination "RequestDestination")

No documentation available

T

[RequestInfo](./././~/RequestInfo "RequestInfo")

No documentation available

T

[RequestMode](./././~/RequestMode "RequestMode")

No documentation available

T

[RequestRedirect](./././~/RequestRedirect "RequestRedirect")

No documentation available

T

[ResponseType](./././~/ResponseType "ResponseType")

No documentation available
