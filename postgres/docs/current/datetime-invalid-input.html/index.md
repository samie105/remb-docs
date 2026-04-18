---
title: "PostgreSQL: Documentation: 18: B.2. Handling of Invalid or Ambiguous Timestamps"
source: "https://www.postgresql.org/docs/current/datetime-invalid-input.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-invalid-input.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:15.020Z"
content_hash: "46f501e7d5da4d1e4c45bd31220a1c513c278aaa3d84c95919532fa4ce97ab2c"
menu_path: ["PostgreSQL: Documentation: 18: B.2. Handling of Invalid or Ambiguous Timestamps"]
section_path: []
nav_prev: {"path": "postgres/docs/current/color-when.html/index.md", "title": "PostgreSQL: Documentation: 18: N.1.\u00a0When Color is Used"}
nav_next: {"path": "postgres/docs/current/protocol-replication.html/index.md", "title": "PostgreSQL: Documentation: 18: 54.4.\u00a0Streaming Replication Protocol"}
---

Ordinarily, if a date/time string is syntactically valid but contains out-of-range field values, an error will be thrown. For example, input specifying the 31st of February will be rejected.

During a daylight-savings-time transition, it is possible for a seemingly valid timestamp string to represent a nonexistent or ambiguous timestamp. Such cases are not rejected; the ambiguity is resolved by determining which UTC offset to apply. For example, supposing that the [TimeZone](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE) parameter is set to `America/New_York`, consider

\=> SELECT '2018-03-11 02:30'::timestamptz;
      timestamptz
------------------------
 2018-03-11 03:30:00-04
(1 row)

Because that day was a spring-forward transition date in that time zone, there was no civil time instant 2:30AM; clocks jumped forward from 2AM EST to 3AM EDT. PostgreSQL interprets the given time as if it were standard time (UTC-5), which then renders as 3:30AM EDT (UTC-4).

Conversely, consider the behavior during a fall-back transition:

\=> SELECT '2018-11-04 01:30'::timestamptz;
      timestamptz
------------------------
 2018-11-04 01:30:00-05
(1 row)

On that date, there were two possible interpretations of 1:30AM; there was 1:30AM EDT, and then an hour later after clocks jumped back from 2AM EDT to 1AM EST, there was 1:30AM EST. Again, PostgreSQL interprets the given time as if it were standard time (UTC-5). We can force the other interpretation by specifying daylight-savings time:

\=> SELECT '2018-11-04 01:30 EDT'::timestamptz;
      timestamptz
------------------------
 2018-11-04 01:30:00-04
(1 row)

The precise rule that is applied in such cases is that an invalid timestamp that appears to fall within a jump-forward daylight savings transition is assigned the UTC offset that prevailed in the time zone just before the transition, while an ambiguous timestamp that could fall on either side of a jump-back transition is assigned the UTC offset that prevailed just after the transition. In most time zones this is equivalent to saying that “the standard-time interpretation is preferred when in doubt”.

In all cases, the UTC offset associated with a timestamp can be specified explicitly, using either a numeric UTC offset or a time zone abbreviation that corresponds to a fixed UTC offset. The rule just given applies only when it is necessary to infer a UTC offset for a time zone in which the offset varies.
