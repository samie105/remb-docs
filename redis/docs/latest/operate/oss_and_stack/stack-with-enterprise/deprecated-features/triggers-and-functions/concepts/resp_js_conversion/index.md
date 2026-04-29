---
title: "RESP & JavaScript"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/resp_js_conversion/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/resp_js_conversion/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:06.150Z"
content_hash: "f5f7845edb63a3f9266f3ff200ece27d8c88bdb13c86228ac668fe6a0e60fa48"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Concepts","→","Concepts","→\n      \n        RESP & JavaScript","→","RESP & JavaScript"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Concepts","→","Concepts","→\n      \n        RESP & JavaScript","→","RESP & JavaScript"]
nav_prev: {"path": "../library_configuration/index.md", "title": "Library configuration"}
nav_next: {"path": "../sync_async/index.md", "title": "Sync and async"}
---

# RESP & JavaScript

Converting RESP to and from JavaScript

Redis Open Source

Redis Software

Redis Cloud

Redis Open Source

Redis Enterprise for Kubernetes

clients

When running Redis commands from within a function using the `client.call` API, the reply is parsed as a resp3 reply and converted to a JS object using the following rules:

resp 3

JS object type

`status`

`StringObject` with a field called `__reply_type` and value `status` (or error if failed to convert to utf8)

`bulk string`

JS `String` (or error if failed to convert to utf8)

`Error`

Raise JS exception

`long`

JS big integer

`double`

JS number

`array`

JS array

`map`

JS object

`set`

JS set

`bool`

JS boolean

`big number`

`StringObject` with a field called `__reply_type` and value `big_number`

`verbatim string`

`StringObject` with 2 additional fields: 1. `__reply_type` and value `verbatim` 2. `__format` with the value of the ext in the verbatim string (or error if failed to convert to utf8)

`null`

JS null

When running Redis commands from within a function using the `client.callRaw` API, the reply is parsed as a resp3 reply and converted to a JS object using the following rules:

resp 3

JS object type

`status`

JS `ArrayBuffer` with a field called `__reply_type` and value `status`

`bulk string`

JS `ArrayBuffer`

`Error`

Raise JS exception

`long`

JS big integer

`double`

JS number

`array`

JS array

`map`

JS object

`set`

JS set

`bool`

JS boolean

`big number`

`StringObject` with a field called `__reply_type` and value `big_number`

`verbatim string`

JS `ArrayBuffer` with 2 additional fields: 1. `__reply_type` and value `verbatim` 2. `__format` with the value of the ext in the verbatim string

`null`

JS null

## JavaScript to RESP conversion

JS type

RESP2

RESP3

`string`

`bulk string`

`bulk string`

`string` object with field `__reply_type=status`

`status`

`status`

Exception

`error`

`error`

`big integer`

`long`

`long`

`number`

`bulk string`

`double`

`array`

`array`

`array`

`map`

`array`

`map`

`set`

`array`

`set`

`bool`

`long`

`bool`

`string` object with field`__reply_type=varbatim` and `__format=txt`

`bulk string`

`verbatim string` with format as `txt`

`null`

resp2 `null`

resp3 `null`

## On this page
