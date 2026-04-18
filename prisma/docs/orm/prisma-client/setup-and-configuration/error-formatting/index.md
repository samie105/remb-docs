---
title: "Configuring error formatting"
source: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/error-formatting"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/error-formatting"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:31.251Z"
content_hash: "0c25d5fe88e267aac35d65b19ffbfab7c4afd5ef7477bd134597b76629c8e5c1"
menu_path: ["Configuring error formatting"]
section_path: []
---
Setup and Configuration

This page explains how to configure the formatting of errors when using Prisma Client

By default, Prisma Client uses [ANSI escape characters](https://en.wikipedia.org/wiki/ANSI_escape_code) to pretty print the error stack and give recommendations on how to fix a problem. While this is very useful when using Prisma Client from the terminal, in contexts like a GraphQL API, you only want the minimal error without any additional formatting.

This page explains how error formatting can be configured with Prisma Client.

There are 3 error formatting levels:

1.  **Pretty Error** (default): Includes a full stack trace with colors, syntax highlighting of the code and extended error message with a possible solution for the problem.
2.  **Colorless Error**: Same as pretty errors, just without colors.
3.  **Minimal Error**: The raw error message.

In order to configure these different error formatting levels, there are two options:

*   Setting the config options via environment variables
*   Providing the config options to the `PrismaClient` constructor

*   [`NO_COLOR`](https://www.prisma.io/docs/orm/reference/environment-variables-reference#no_color): If this env var is provided, colors are stripped from the error messages. Therefore you end up with a **colorless error**. The `NO_COLOR` environment variable is a standard described [here](https://no-color.org/).
*   `NODE_ENV=production`: If the env var `NODE_ENV` is set to `production`, only the **minimal error** will be printed. This allows for easier digestion of logs in production environments.

### [Formatting via the `PrismaClient` constructor](#formatting-via-the-prismaclient-constructor)

Alternatively, use the `PrismaClient` [`errorFormat`](https://www.prisma.io/docs/orm/reference/prisma-client-reference#errorformat) parameter to set the error format:

```
const prisma = new PrismaClient({
  errorFormat: "pretty",
});
```

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/setup-and-configuration/error-formatting.mdx)
