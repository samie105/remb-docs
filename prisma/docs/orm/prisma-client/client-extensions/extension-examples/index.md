---
title: "Shared packages & examples"
source: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/extension-examples"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/client-extensions/extension-examples"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:38:03.371Z"
content_hash: "1271c9385e9a589fa5c3c456017a5d328afeffad3a9496baa41bcd81f4962b27"
menu_path: ["Shared packages & examples"]
section_path: []
content_language: "en"
nav_prev: {"path": "prisma/docs/orm/prisma-client/client-extensions/client/index.md", "title": "Add methods to Prisma Client"}
nav_next: {"path": "prisma/docs/orm/prisma-client/client-extensions/model/index.md", "title": "Add custom methods to your models"}
---

Client Extensions

Explore the Prisma Client extensions that have been built by Prisma and its community

The following is a list of extensions we've built at Prisma:

The following is a list of extensions created by the community. If you want to create your own package, refer to the [Shared Prisma Client extensions](../shared-extensions/index.md) documentation.

If you have built an extension and would like to see it featured, feel free to add it to the list by opening a pull request.

| Example | Description |
| --- | --- |
| [`audit-log-context`](https://github.com/prisma/prisma-client-extensions/tree/main/audit-log-context) | Provides the current user's ID as context to Postgres audit log triggers |
| [`callback-free-itx`](https://github.com/prisma/prisma-client-extensions/tree/main/callback-free-itx) | Adds a method to start interactive transactions without callbacks |
| [`computed-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/computed-fields) | Adds virtual / computed fields to result objects |
| [`input-transformation`](https://github.com/prisma/prisma-client-extensions/tree/main/input-transformation) | Transforms the input arguments passed to Prisma Client queries to filter the result set |
| [`input-validation`](https://github.com/prisma/prisma-client-extensions/tree/main/input-validation) | Runs custom validation logic on input arguments passed to mutation methods |
| [`instance-methods`](https://github.com/prisma/prisma-client-extensions/tree/main/instance-methods) | Adds Active Record-like methods like `save()` and `delete()` to result objects |
| [`json-field-types`](https://github.com/prisma/prisma-client-extensions/tree/main/json-field-types) | Uses strongly-typed runtime parsing for data stored in JSON columns |
| [`model-filters`](https://github.com/prisma/prisma-client-extensions/tree/main/model-filters) | Adds reusable filters that can composed into complex `where` conditions for a model |
| [`obfuscated-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/obfuscated-fields) | Prevents sensitive data (e.g. `password` fields) from being included in results |
| [`query-logging`](https://github.com/prisma/prisma-client-extensions/tree/main/query-logging) | Wraps Prisma Client queries with simple query timing and logging |
| [`readonly-client`](https://github.com/prisma/prisma-client-extensions/tree/main/readonly-client) | Creates a client that only allows read operations |
| [`retry-transactions`](https://github.com/prisma/prisma-client-extensions/tree/main/retry-transactions) | Adds a retry mechanism to transactions with exponential backoff and jitter |
| [`row-level-security`](https://github.com/prisma/prisma-client-extensions/tree/main/row-level-security) | Uses Postgres row-level security policies to isolate data a multi-tenant application |
| [`static-methods`](https://github.com/prisma/prisma-client-extensions/tree/main/static-methods) | Adds custom query methods to Prisma Client models |
| [`transformed-fields`](https://github.com/prisma/prisma-client-extensions/tree/main/transformed-fields) | Demonstrates how to use result extensions to transform query results and add i18n to an app |
| [`exists-method`](https://github.com/prisma/prisma-client-extensions/tree/main/exists-fn) | Demonstrates how to add an `exists` method to all your models |
| [`update-delete-ignore-not-found`](https://github.com/prisma/prisma-client-extensions/tree/main/update-delete-ignore-not-found) | Demonstrates how to add the `updateIgnoreOnNotFound` and `deleteIgnoreOnNotFound` methods to all your models. |

-   Learn more about [Prisma Client extensions](../index.md).
