---
title: "Architecture Overview"
source: "https://docs.deno.com/runtime/contributing/architecture/"
canonical_url: "https://docs.deno.com/runtime/contributing/architecture/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:18:09.033Z"
content_hash: "e5a43e9aad6509d60c4626913a6ac3d0e15b6dbe9fd72dbad65bb5464d1c2f29"
menu_path: ["Architecture Overview"]
section_path: []
content_language: "en"
---
**On this page**

-   [Deno and Linux analogy](#deno-and-linux-analogy)
    -   [Resources](#resources)
    -   [Metrics](#metrics)
-   [Conference](#conference)

## Deno and Linux analogy

| **Linux** | **Deno** |
| --- | --- |
| Processes | Web Workers |
| Syscalls | Ops |
| File descriptors (fd) | [Resource ids (rid)](#resources) |
| Scheduler | Tokio |
| Userland: libc++ / glib / boost | [https://jsr.io/@std](https://jsr.io/@std) |
| /proc/$$/stat | [Deno.metrics()](#metrics) |
| man pages | deno types / [https://docs.deno.com](https://docs.deno.com) |

### Resources

Resources (AKA `rid`) are Deno's version of file descriptors. They are integer values used to refer to open files, sockets, and other concepts. For testing it would be good to be able to query the system for how many open resources there are.

```ts
console.log(Deno.resources());
// { 0: "stdin", 1: "stdout", 2: "stderr" }
Deno.close(0);
console.log(Deno.resources());
// { 1: "stdout", 2: "stderr" }
```

### Metrics

Metrics is Deno's internal counter for various statistics.

```shell
> console.table(Deno.metrics())
┌─────────────────────────┬───────────┐
│          (idx)          │  Values   │
├─────────────────────────┼───────────┤
│      opsDispatched      │    9      │
│    opsDispatchedSync    │    0      │
│   opsDispatchedAsync    │    0      │
│ opsDispatchedAsyncUnref │    0      │
│      opsCompleted       │    9      │
│    opsCompletedSync     │    0      │
│    opsCompletedAsync    │    0      │
│ opsCompletedAsyncUnref  │    0      │
│    bytesSentControl     │   504     │
│      bytesSentData      │    0      │
│      bytesReceived      │   856     │
└─────────────────────────┴───────────┘
```

## Conference

-   Ryan Dahl. (May 27, 2020). [An interesting case with Deno](https://www.youtube.com/watch?v=1b7FoBwxc7E). Deno Israel.
-   Bartek Iwańczuk. (Oct 6, 2020). [Deno internals - how modern JS/TS runtime is built](https://www.youtube.com/watch?v=AOvg_GbnsbA&t=35m13s). Paris Deno.
