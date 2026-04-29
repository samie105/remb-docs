---
title: "perf_hooks - Node documentation"
source: "https://docs.deno.com/api/node/perf_hooks/"
canonical_url: "https://docs.deno.com/api/node/perf_hooks/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:09:42.081Z"
content_hash: "cf9dcbac2734147caa94add8c60f2b6d6f22602555e98264f3f2044a55f5193e"
menu_path: ["perf_hooks - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../path/index.md", "title": "path - Node documentation"}
nav_next: {"path": "../process/index.md", "title": "process - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:perf_hooks";
```

This module provides an implementation of a subset of the W3C [Web Performance APIs](https://w3c.github.io/perf-timing-primer/) as well as additional APIs for Node.js-specific performance measurements.

Node.js supports the following [Web Performance APIs](https://w3c.github.io/perf-timing-primer/):

-   [High Resolution Time](https://www.w3.org/TR/hr-time-2)
-   [Performance Timeline](https://w3c.github.io/performance-timeline/)
-   [User Timing](https://www.w3.org/TR/user-timing/)
-   [Resource Timing](https://www.w3.org/TR/resource-timing-2/)

```js
import { PerformanceObserver, performance } from 'node:perf_hooks';

const obs = new PerformanceObserver((items) => {
  console.log(items.getEntries()[0].duration);
  performance.clearMarks();
});
obs.observe({ type: 'measure' });
performance.measure('Start to Now');

performance.mark('A');
doSomeLongRunningProcess(() => {
  performance.measure('A to Now', 'A');

  performance.mark('B');
  performance.measure('A to B', 'A', 'B');
});
```

c

v

[PerformanceEntry](.././perf_hooks/~/PerformanceEntry "PerformanceEntry")

The constructor of this class is not exposed to users directly.

-   [detail](.././perf_hooks/~/PerformanceEntry#property_detail)
-   [duration](.././perf_hooks/~/PerformanceEntry#property_duration)
-   [entryType](.././perf_hooks/~/PerformanceEntry#property_entrytype)
-   [name](.././perf_hooks/~/PerformanceEntry#property_name)
-   [startTime](.././perf_hooks/~/PerformanceEntry#property_starttime)
-   [toJSON](.././perf_hooks/~/PerformanceEntry#method_tojson_0)

c

v

[PerformanceMark](.././perf_hooks/~/PerformanceMark "PerformanceMark")

Exposes marks created via the `Performance.mark()` method.

-   [duration](.././perf_hooks/~/PerformanceMark#property_duration)
-   [entryType](.././perf_hooks/~/PerformanceMark#property_entrytype)

c

v

[PerformanceMeasure](.././perf_hooks/~/PerformanceMeasure "PerformanceMeasure")

Exposes measures created via the `Performance.measure()` method.

-   [entryType](.././perf_hooks/~/PerformanceMeasure#property_entrytype)

c

[PerformanceNodeTiming](.././perf_hooks/~/PerformanceNodeTiming "PerformanceNodeTiming")

_This property is an extension by Node.js. It is not available in Web browsers._

-   [bootstrapComplete](.././perf_hooks/~/PerformanceNodeTiming#property_bootstrapcomplete)
-   [entryType](.././perf_hooks/~/PerformanceNodeTiming#property_entrytype)
-   [environment](.././perf_hooks/~/PerformanceNodeTiming#property_environment)
-   [idleTime](.././perf_hooks/~/PerformanceNodeTiming#property_idletime)
-   [loopExit](.././perf_hooks/~/PerformanceNodeTiming#property_loopexit)
-   [loopStart](.././perf_hooks/~/PerformanceNodeTiming#property_loopstart)
-   [nodeStart](.././perf_hooks/~/PerformanceNodeTiming#property_nodestart)
-   [uvMetricsInfo](.././perf_hooks/~/PerformanceNodeTiming#property_uvmetricsinfo)
-   [v8Start](.././perf_hooks/~/PerformanceNodeTiming#property_v8start)

c

v

[PerformanceObserver](.././perf_hooks/~/PerformanceObserver "PerformanceObserver")

No documentation available

-   [disconnect](.././perf_hooks/~/PerformanceObserver#method_disconnect_0)
-   [observe](.././perf_hooks/~/PerformanceObserver#method_observe_0)
-   [takeRecords](.././perf_hooks/~/PerformanceObserver#method_takerecords_0)

c

v

[PerformanceObserverEntryList](.././perf_hooks/~/PerformanceObserverEntryList "PerformanceObserverEntryList")

No documentation available

-   [getEntries](.././perf_hooks/~/PerformanceObserverEntryList#method_getentries_0)
-   [getEntriesByName](.././perf_hooks/~/PerformanceObserverEntryList#method_getentriesbyname_0)
-   [getEntriesByType](.././perf_hooks/~/PerformanceObserverEntryList#method_getentriesbytype_0)

c

v

[PerformanceResourceTiming](.././perf_hooks/~/PerformanceResourceTiming "PerformanceResourceTiming")

Provides detailed network timing data regarding the loading of an application's resources.

-   [connectEnd](.././perf_hooks/~/PerformanceResourceTiming#property_connectend)
-   [connectStart](.././perf_hooks/~/PerformanceResourceTiming#property_connectstart)
-   [decodedBodySize](.././perf_hooks/~/PerformanceResourceTiming#property_decodedbodysize)
-   [domainLookupEnd](.././perf_hooks/~/PerformanceResourceTiming#property_domainlookupend)
-   [domainLookupStart](.././perf_hooks/~/PerformanceResourceTiming#property_domainlookupstart)
-   [encodedBodySize](.././perf_hooks/~/PerformanceResourceTiming#property_encodedbodysize)
-   [entryType](.././perf_hooks/~/PerformanceResourceTiming#property_entrytype)
-   [fetchStart](.././perf_hooks/~/PerformanceResourceTiming#property_fetchstart)
-   [redirectEnd](.././perf_hooks/~/PerformanceResourceTiming#property_redirectend)
-   [redirectStart](.././perf_hooks/~/PerformanceResourceTiming#property_redirectstart)
-   [requestStart](.././perf_hooks/~/PerformanceResourceTiming#property_requeststart)
-   [responseEnd](.././perf_hooks/~/PerformanceResourceTiming#property_responseend)
-   [secureConnectionStart](.././perf_hooks/~/PerformanceResourceTiming#property_secureconnectionstart)
-   [toJSON](.././perf_hooks/~/PerformanceResourceTiming#method_tojson_0)
-   [transferSize](.././perf_hooks/~/PerformanceResourceTiming#property_transfersize)
-   [workerStart](.././perf_hooks/~/PerformanceResourceTiming#property_workerstart)

f

[createHistogram](.././perf_hooks/~/createHistogram "createHistogram")

Returns a `RecordableHistogram`.

f

[monitorEventLoopDelay](.././perf_hooks/~/monitorEventLoopDelay "monitorEventLoopDelay")

No documentation available

I

[CreateHistogramOptions](.././perf_hooks/~/CreateHistogramOptions "CreateHistogramOptions")

No documentation available

-   [figures](.././perf_hooks/~/CreateHistogramOptions#property_figures)
-   [max](.././perf_hooks/~/CreateHistogramOptions#property_max)
-   [min](.././perf_hooks/~/CreateHistogramOptions#property_min)

I

[EventLoopMonitorOptions](.././perf_hooks/~/EventLoopMonitorOptions "EventLoopMonitorOptions")

No documentation available

-   [resolution](.././perf_hooks/~/EventLoopMonitorOptions#property_resolution)

I

[EventLoopUtilization](.././perf_hooks/~/EventLoopUtilization "EventLoopUtilization")

No documentation available

-   [active](.././perf_hooks/~/EventLoopUtilization#property_active)
-   [idle](.././perf_hooks/~/EventLoopUtilization#property_idle)
-   [utilization](.././perf_hooks/~/EventLoopUtilization#property_utilization)

I

[Histogram](.././perf_hooks/~/Histogram "Histogram")

No documentation available

-   [count](.././perf_hooks/~/Histogram#property_count)
-   [countBigInt](.././perf_hooks/~/Histogram#property_countbigint)
-   [exceeds](.././perf_hooks/~/Histogram#property_exceeds)
-   [exceedsBigInt](.././perf_hooks/~/Histogram#property_exceedsbigint)
-   [max](.././perf_hooks/~/Histogram#property_max)
-   [maxBigInt](.././perf_hooks/~/Histogram#property_maxbigint)
-   [mean](.././perf_hooks/~/Histogram#property_mean)
-   [min](.././perf_hooks/~/Histogram#property_min)
-   [minBigInt](.././perf_hooks/~/Histogram#property_minbigint)
-   [percentile](.././perf_hooks/~/Histogram#method_percentile_0)
-   [percentileBigInt](.././perf_hooks/~/Histogram#method_percentilebigint_0)
-   [percentiles](.././perf_hooks/~/Histogram#property_percentiles)
-   [percentilesBigInt](.././perf_hooks/~/Histogram#property_percentilesbigint)
-   [reset](.././perf_hooks/~/Histogram#method_reset_0)
-   [stddev](.././perf_hooks/~/Histogram#property_stddev)

I

[IntervalHistogram](.././perf_hooks/~/IntervalHistogram "IntervalHistogram")

No documentation available

-   [disable](.././perf_hooks/~/IntervalHistogram#method_disable_0)
-   [enable](.././perf_hooks/~/IntervalHistogram#method_enable_0)

I

[MarkOptions](.././perf_hooks/~/MarkOptions "MarkOptions")

No documentation available

-   [detail](.././perf_hooks/~/MarkOptions#property_detail)
-   [startTime](.././perf_hooks/~/MarkOptions#property_starttime)

I

[MeasureOptions](.././perf_hooks/~/MeasureOptions "MeasureOptions")

No documentation available

-   [detail](.././perf_hooks/~/MeasureOptions#property_detail)
-   [duration](.././perf_hooks/~/MeasureOptions#property_duration)
-   [end](.././perf_hooks/~/MeasureOptions#property_end)
-   [start](.././perf_hooks/~/MeasureOptions#property_start)

I

[NodeGCPerformanceDetail](.././perf_hooks/~/NodeGCPerformanceDetail "NodeGCPerformanceDetail")

No documentation available

-   [flags](.././perf_hooks/~/NodeGCPerformanceDetail#property_flags)
-   [kind](.././perf_hooks/~/NodeGCPerformanceDetail#property_kind)

I

[Performance](.././perf_hooks/~/Performance "Performance")

No documentation available

-   [clearMarks](.././perf_hooks/~/Performance#method_clearmarks_0)
-   [clearMeasures](.././perf_hooks/~/Performance#method_clearmeasures_0)
-   [clearResourceTimings](.././perf_hooks/~/Performance#method_clearresourcetimings_0)
-   [eventLoopUtilization](.././perf_hooks/~/Performance#property_eventlooputilization)
-   [getEntries](.././perf_hooks/~/Performance#method_getentries_0)
-   [getEntriesByName](.././perf_hooks/~/Performance#method_getentriesbyname_0)
-   [getEntriesByType](.././perf_hooks/~/Performance#method_getentriesbytype_0)
-   [mark](.././perf_hooks/~/Performance#method_mark_0)
-   [markResourceTiming](.././perf_hooks/~/Performance#method_markresourcetiming_0)
-   [measure](.././perf_hooks/~/Performance#method_measure_0)
-   [nodeTiming](.././perf_hooks/~/Performance#property_nodetiming)
-   [now](.././perf_hooks/~/Performance#method_now_0)
-   [setResourceTimingBufferSize](.././perf_hooks/~/Performance#method_setresourcetimingbuffersize_0)
-   [timeOrigin](.././perf_hooks/~/Performance#property_timeorigin)
-   [timerify](.././perf_hooks/~/Performance#method_timerify_0)
-   [toJSON](.././perf_hooks/~/Performance#method_tojson_0)

I

[RecordableHistogram](.././perf_hooks/~/RecordableHistogram "RecordableHistogram")

No documentation available

-   [add](.././perf_hooks/~/RecordableHistogram#method_add_0)
-   [record](.././perf_hooks/~/RecordableHistogram#method_record_0)
-   [recordDelta](.././perf_hooks/~/RecordableHistogram#method_recorddelta_0)

I

[TimerifyOptions](.././perf_hooks/~/TimerifyOptions "TimerifyOptions")

No documentation available

-   [histogram](.././perf_hooks/~/TimerifyOptions#property_histogram)

I

[UVMetrics](.././perf_hooks/~/UVMetrics "UVMetrics")

No documentation available

-   [events](.././perf_hooks/~/UVMetrics#property_events)
-   [eventsWaiting](.././perf_hooks/~/UVMetrics#property_eventswaiting)
-   [loopCount](.././perf_hooks/~/UVMetrics#property_loopcount)

N

[constants](.././perf_hooks/~/constants "constants")

No documentation available

T

[EntryType](.././perf_hooks/~/EntryType "EntryType")

No documentation available

T

[EventLoopUtilityFunction](.././perf_hooks/~/EventLoopUtilityFunction "EventLoopUtilityFunction")

No documentation available

T

[PerformanceObserverCallback](.././perf_hooks/~/PerformanceObserverCallback "PerformanceObserverCallback")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_ALL\_AVAILABLE\_GARBAGE](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE "constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_ALL\_EXTERNAL\_MEMORY](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY "constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_CONSTRUCT\_RETAINED](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED "constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_FORCED](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_FORCED "constants.NODE_PERFORMANCE_GC_FLAGS_FORCED")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_NO](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_NO "constants.NODE_PERFORMANCE_GC_FLAGS_NO")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_SCHEDULE\_IDLE](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE "constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_SYNCHRONOUS\_PHANTOM\_PROCESSING](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING "constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_INCREMENTAL](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_INCREMENTAL "constants.NODE_PERFORMANCE_GC_INCREMENTAL")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_MAJOR](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_MAJOR "constants.NODE_PERFORMANCE_GC_MAJOR")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_MINOR](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_MINOR "constants.NODE_PERFORMANCE_GC_MINOR")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_WEAKCB](.././perf_hooks/~/constants.NODE_PERFORMANCE_GC_WEAKCB "constants.NODE_PERFORMANCE_GC_WEAKCB")

No documentation available

v

[performance](.././perf_hooks/~/performance "performance")

No documentation available
