---
title: "Performance - Web documentation"
source: "https://docs.deno.com/api/web/performance"
canonical_url: "https://docs.deno.com/api/web/performance"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:08.825Z"
content_hash: "9c8747d9b110bf988c6407f59eedea49ac2f2fa0590a3f2d3b601b2cd749bffe"
menu_path: ["Performance - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/messaging/index.md", "title": "Messaging - Web documentation"}
nav_next: {"path": "deno/deno/api/web/platform/index.md", "title": "Platform - Web documentation"}
---

### Interfaces [#](#Interfaces)

I

v

[Performance](./././~/Performance "Performance")

Deno supports [User Timing Level 3](https://w3c.github.io/user-timing) which is not widely supported yet in other runtimes.

*   [mark](./././~/Performance#method_mark_0)
*   [measure](./././~/Performance#method_measure_0)
*   [prototype](./././~/Performance#property_prototype)

I

v

[PerformanceEntry](./././~/PerformanceEntry "PerformanceEntry")

Encapsulates a single performance metric that is part of the performance timeline. A performance entry can be directly created by making a performance mark or measure (for example by calling the `.mark()` method) at an explicit point in an application.

*   [duration](./././~/PerformanceEntry#property_duration)
*   [entryType](./././~/PerformanceEntry#property_entrytype)
*   [name](./././~/PerformanceEntry#property_name)
*   [prototype](./././~/PerformanceEntry#property_prototype)
*   [startTime](./././~/PerformanceEntry#property_starttime)
*   [toJSON](./././~/PerformanceEntry#method_tojson_0)

I

v

[PerformanceMark](./././~/PerformanceMark "PerformanceMark")

`PerformanceMark` is an abstract interface for `PerformanceEntry` objects with an entryType of `"mark"`. Entries of this type are created by calling `performance.mark()` to add a named `DOMHighResTimeStamp` (the mark) to the performance timeline.

*   [detail](./././~/PerformanceMark#property_detail)
*   [entryType](./././~/PerformanceMark#property_entrytype)
*   [prototype](./././~/PerformanceMark#property_prototype)

I

[PerformanceMarkOptions](./././~/PerformanceMarkOptions "PerformanceMarkOptions")

Options which are used in conjunction with `performance.mark`. Check out the MDN [`performance.mark()`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark#markoptions) documentation for more details.

*   [detail](./././~/PerformanceMarkOptions#property_detail)
*   [startTime](./././~/PerformanceMarkOptions#property_starttime)

I

v

[PerformanceMeasure](./././~/PerformanceMeasure "PerformanceMeasure")

`PerformanceMeasure` is an abstract interface for `PerformanceEntry` objects with an entryType of `"measure"`. Entries of this type are created by calling `performance.measure()` to add a named `DOMHighResTimeStamp` (the measure) between two marks to the performance timeline.

*   [detail](./././~/PerformanceMeasure#property_detail)
*   [entryType](./././~/PerformanceMeasure#property_entrytype)
*   [prototype](./././~/PerformanceMeasure#property_prototype)

I

[PerformanceMeasureOptions](./././~/PerformanceMeasureOptions "PerformanceMeasureOptions")

Options which are used in conjunction with `performance.measure`. Check out the MDN [`performance.mark()`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/measure#measureoptions) documentation for more details.

*   [detail](./././~/PerformanceMeasureOptions#property_detail)
*   [duration](./././~/PerformanceMeasureOptions#property_duration)
*   [end](./././~/PerformanceMeasureOptions#property_end)
*   [start](./././~/PerformanceMeasureOptions#property_start)

### Type Aliases [#](<#Type Aliases>)

T

[PerformanceEntryList](./././~/PerformanceEntryList "PerformanceEntryList")

No documentation available

### Variables [#](#Variables)

v

[performance](./././~/performance "performance")

No documentation available


