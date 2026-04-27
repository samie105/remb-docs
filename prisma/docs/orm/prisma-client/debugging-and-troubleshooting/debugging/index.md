---
title: "Debugging"
source: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:38:22.722Z"
content_hash: "f9cdac538230f678d9cab4821b6f4d270945246675e09d58572f2aed142eacd2"
menu_path: ["Debugging"]
section_path: []
content_language: "en"
---
Debugging and Troubleshooting

This page explains how to enable debugging output for Prisma Client by setting the \`DEBUG\` environment variable

You can enable debugging output in Prisma Client and Prisma CLI via the [`DEBUG`](https://www.prisma.io/docs/orm/reference/environment-variables-reference#debug) environment variable. It accepts two namespaces to print debugging output:

-   `prisma:engine`: Prints relevant debug messages happening in a Prisma ORM [engine](https://github.com/prisma/prisma-engines/)
-   `prisma:client`: Prints relevant debug messages happening in the Prisma Client runtime
-   `prisma*`: Prints all debug messages from Prisma Client or CLI
-   `*`: Prints all debug messages

Here are examples for setting these debugging options in bash:

```
# enable only `prisma:engine`-level debugging output
export DEBUG="prisma:engine"

# enable only `prisma:client`-level debugging output
export DEBUG="prisma:client"

# enable both `prisma-client`- and `engine`-level debugging output
export DEBUG="prisma:client,prisma:engine"
```

To enable all `prisma` debugging options, set `DEBUG` to `prisma*`:

```
export DEBUG="prisma*"
```

On Windows, use `set` instead of `export`:

```
set DEBUG="prisma*"
```

To enable _all_ debugging options, set `DEBUG` to `*`:

```
export DEBUG="*"
```
