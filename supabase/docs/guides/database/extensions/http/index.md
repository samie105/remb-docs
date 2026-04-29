---
title: "http: RESTful Client"
source: "https://supabase.com/docs/guides/database/extensions/http"
canonical_url: "https://supabase.com/docs/guides/database/extensions/http"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:34.094Z"
content_hash: "f61247d7ff6f7e0b4b564c9faf99f8ef6d4067946622643af3b5e22d33e0cb55"
menu_path: ["Database","Database","Extensions","Extensions","http: RESTful Client","http: RESTful Client"]
section_path: ["Database","Database","Extensions","Extensions","http: RESTful Client","http: RESTful Client"]
nav_prev: {"path": "../index.md", "title": "Postgres Extensions Overview"}
nav_next: {"path": "../hypopg/index.md", "title": "HypoPG: Hypothetical indexes"}
---

# 

http: RESTful Client

* * *

The `http` extension allows you to call RESTful endpoints within Postgres.

## Quick demo[#](#quick-demo)

## Overview[#](#overview)

Let's cover some basic concepts:

*   REST: stands for REpresentational State Transfer. It's a way to request data from external services.
*   RESTful APIs are servers which accept HTTP "calls". The calls are typically:
    *   `GET` − Read only access to a resource.
    *   `POST` − Creates a new resource.
    *   `DELETE` − Removes a resource.
    *   `PUT` − Updates an existing resource or creates a new resource.

You can use the `http` extension to make these network requests from Postgres.

## Usage[#](#usage)

### Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `http` and enable the extension.

### Available functions[#](#available-functions)

While the main usage is `http('http_request')`, there are 5 wrapper functions for specific functionality:

*   `http_get()`
*   `http_post()`
*   `http_put()`
*   `http_delete()`
*   `http_head()`

### Returned values[#](#returned-values)

A successful call to a web URL from the `http` extension returns a record with the following fields:

*   `status`: integer
*   `content_type`: character varying
*   `headers`: http\_header\[\]
*   `content`: character varying. Typically you would want to cast this to `jsonb` using the format `content::jsonb`

## Examples[#](#examples)

### Simple `GET` example[#](#simple-get-example)

```
1select2  "status", "content"::jsonb3from4  extensions.http_get('https://jsonplaceholder.typicode.com/todos/1');
```

### Simple `POST` example[#](#simple-post-example)

```
1select2  "status", "content"::jsonb3from4  extensions.http_post(5    'https://jsonplaceholder.typicode.com/posts',6    '{ "title": "foo", "body": "bar", "userId": 1 }',7    'application/json'8  );
```

## Resources[#](#resources)

*   Official [`http` GitHub Repository](https://github.com/pramsey/pgsql-http)
