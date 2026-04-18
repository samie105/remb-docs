---
title: "timescaledb: Time-Series data"
source: "https://supabase.com/docs/guides/database/extensions/timescaledb"
canonical_url: "https://supabase.com/docs/guides/database/extensions/timescaledb"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:19.306Z"
content_hash: "565beaeac9828d8bf4ea6e355a573fada25e49a618b2266cc4389373030b833b"
menu_path: ["Database","Database","Extensions","Extensions","timescaledb (deprecated)","timescaledb (deprecated)"]
section_path: ["Database","Database","Extensions","Extensions","timescaledb (deprecated)","timescaledb (deprecated)"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/rum/index.md", "title": "RUM: improved inverted index for full-text search based on GIN index"}
nav_next: {"path": "supabase/docs/guides/database/extensions/uuid-ossp/index.md", "title": "uuid-ossp: Unique Identifiers"}
---

# 

timescaledb: Time-Series data

* * *

The `timescaledb` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.

If you are using hypertables, follow the [migration guide](/docs/guides/database/migrating-to-pg-partman) to convert to native partitioning managed by `pg_partman`.

For additional support, contact our Success team by creating a support ticket in the Supabase Dashboard.

[`timescaledb`](https://docs.timescale.com/timescaledb/latest/) is a Postgres extension designed for improved handling of time-series data. It provides a scalable, high-performance solution for storing and querying time-series data on top of a standard Postgres database.

`timescaledb` uses a time-series-aware storage model and indexing techniques to improve performance of Postgres in working with time-series data. The extension divides data into chunks based on time intervals, allowing it to scale efficiently, especially for large data sets. The data is then compressed, optimized for write-heavy workloads, and partitioned for parallel processing. `timescaledb` also includes a set of functions, operators, and indexes that work with time-series data to reduce query times, and make data easier to work with.

Supabase projects come with [TimescaleDB Apache 2 Edition](https://docs.timescale.com/about/latest/timescaledb-editions/#timescaledb-apache-2-edition). Functionality only available under the Community Edition is not available.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `timescaledb` and enable the extension.

Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension". To disable an extension you can call `drop extension`.

It's good practice to create the extension within a separate schema (like `extensions`) to keep your `public` schema clean.

## Usage[#](#usage)

To demonstrate how `timescaledb` works, let's consider a simple example where we have a table that stores temperature data from different sensors. We will create a table named "temperatures" and store data for two sensors.

First we create a hypertable, which is a virtual table that is partitioned into chunks based on time intervals. The hypertable acts as a proxy for the actual table and makes it easy to query and manage time-series data.

```
1create table temperatures (2  time timestamptz not null,3  sensor_id int not null,4  temperature double precision not null5);67select create_hypertable('temperatures', 'time');
```

Next, we can populate some values

```
1insert into temperatures (time, sensor_id, temperature)2values3    ('2023-02-14 09:00:00', 1, 23.5),4    ('2023-02-14 09:00:00', 2, 21.2),5    ('2023-02-14 09:05:00', 1, 24.5),6    ('2023-02-14 09:05:00', 2, 22.3),7    ('2023-02-14 09:10:00', 1, 25.1),8    ('2023-02-14 09:10:00', 2, 23.9),9    ('2023-02-14 09:15:00', 1, 24.9),10    ('2023-02-14 09:15:00', 2, 22.7),11    ('2023-02-14 09:20:00', 1, 24.7),12    ('2023-02-14 09:20:00', 2, 23.5);
```

And finally we can query the table using `timescaledb`'s `time_bucket` function to divide the time-series into intervals of the specified size (in this case, 1 hour) averaging the `temperature` reading within each group.

```
1select2    time_bucket('1 hour', time) AS hour,3    avg(temperature) AS average_temperature4from5    temperatures6where7    sensor_id = 18    and time > NOW() - interval '1 hour'9group by10    hour;
```

## Resources[#](#resources)

*   Official [`timescaledb` documentation](https://docs.timescale.com/timescaledb/latest/)


