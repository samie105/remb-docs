---
title: "pgrouting: Geospatial Routing"
source: "https://supabase.com/docs/guides/database/extensions/pgrouting"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgrouting"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:59.109Z"
content_hash: "8fea32990e60d9c5a67d3729f9bdec25ad1c0eedf8832b678ce4d2c6159a961b"
menu_path: ["Database","Database","Extensions","Extensions","pgRouting: Geospatial Routing","pgRouting: Geospatial Routing"]
section_path: ["Database","Database","Extensions","Extensions","pgRouting: Geospatial Routing","pgRouting: Geospatial Routing"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pgmq/index.md", "title": "pgmq: Queues"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pgroonga/index.md", "title": "PGroonga: Multilingual Full Text Search"}
---

# 

pgrouting: Geospatial Routing

* * *

[`pgRouting`](http://pgrouting.org) is Postgres and [PostGIS](http://postgis.net) extension adding geospatial routing functionality.

The core functionality of `pgRouting` is a set of path finding algorithms including:

*   All Pairs Shortest Path, Johnson’s Algorithm
*   All Pairs Shortest Path, Floyd-Warshall Algorithm
*   Shortest Path A\*
*   Bi-directional Dijkstra Shortest Path
*   Bi-directional A\* Shortest Path
*   Shortest Path Dijkstra
*   Driving Distance
*   K-Shortest Path, Multiple Alternative Paths
*   K-Dijkstra, One to Many Shortest Path
*   Traveling Sales Person
*   Turn Restriction Shortest Path (TRSP)

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `pgrouting` and enable the extension.

## Example[#](#example)

As an example, we'll solve the [traveling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using the `pgRouting`'s `pgr_TSPeuclidean` function from some PostGIS coordinates.

A summary of the traveling salesperson problem is, given a set of city coordinates, solve for a path that goes through each city and minimizes the total distance traveled.

First we populate a table with some X, Y coordinates

```
1create table wi29 (2  id bigint,3  x float,4  y float,5  geom gis.geometry6);78insert into wi29 (id, x, y)9values10  (1,20833.3333,17100.0000),11  (2,20900.0000,17066.6667),12  (3,21300.0000,13016.6667),13  (4,21600.0000,14150.0000),14  (5,21600.0000,14966.6667),15  (6,21600.0000,16500.0000),16  (7,22183.3333,13133.3333),17  (8,22583.3333,14300.0000),18  (9,22683.3333,12716.6667),19  (10,23616.6667,15866.6667),20  (11,23700.0000,15933.3333),21  (12,23883.3333,14533.3333),22  (13,24166.6667,13250.0000),23  (14,25149.1667,12365.8333),24  (15,26133.3333,14500.0000),25  (16,26150.0000,10550.0000),26  (17,26283.3333,12766.6667),27  (18,26433.3333,13433.3333),28  (19,26550.0000,13850.0000),29  (20,26733.3333,11683.3333),30  (21,27026.1111,13051.9444),31  (22,27096.1111,13415.8333),32  (23,27153.6111,13203.3333),33  (24,27166.6667,9833.3333),34  (25,27233.3333,10450.0000),35  (26,27233.3333,11783.3333),36  (27,27266.6667,10383.3333),37  (28,27433.3333,12400.0000),38  (29,27462.5000,12992.2222);
```

Next we use the `pgr_TSPeuclidean` function to find the best path.

```
1select2    *3from4     pgr_TSPeuclidean($$select * from wi29$$)
```

```
1seq | node |       cost       |     agg_cost     2-----+------+------------------+------------------3   1 |    1 |                0 |                04   2 |    2 |  74.535614157127 |  74.5356141571275   3 |    6 | 900.617093380362 | 975.1527075374896   4 |   10 | 2113.77757765045 | 3088.930285187937   5 |   11 | 106.718669615254 | 3195.648954803198   6 |   12 | 1411.95293791574 | 4607.601892718939   7 |   13 | 1314.23824873744 | 5921.8401414563710   8 |   14 | 1321.76283931305 | 7243.6029807694211   9 |   17 | 1202.91366735569 |  8446.516648125112  10 |   18 | 683.333268292684 | 9129.8499164177913  11 |   15 | 1108.05137466134 | 10237.901291079114  12 |   19 | 772.082339448903 |  11009.98363052815  13 |   22 | 697.666150054665 | 11707.649780582716  14 |   23 | 220.141999627513 | 11927.791780210217  15 |   21 | 197.926372783442 | 12125.718152993718  16 |   29 | 440.456596290771 | 12566.174749284419  17 |   28 | 592.939989005405 | 13159.114738289820  18 |   26 | 648.288376333318 | 13807.403114623121  19 |   20 | 509.901951359278 | 14317.305065982422  20 |   25 | 1330.83095428717 | 15648.136020269623  21 |   27 |  74.535658878487 | 15722.671679148124  22 |   24 | 559.016994374947 |  16281.68867352325  23 |   16 | 1243.87392358622 | 17525.562597109226  24 |    9 |  4088.0585364911 | 21613.621133600427  25 |    7 |  650.85409697993 | 22264.475230580328  26 |    3 | 891.004385199336 | 23155.479615779629  27 |    4 | 1172.36699411442 |  24327.84660989430  28 |    8 | 994.708187806297 | 25322.554797700331  29 |    5 | 1188.01888359478 | 26510.573681295132  30 |    1 | 2266.91173136004 | 28777.4854126552
```

## Resources[#](#resources)

*   Official [`pgRouting` documentation](https://docs.pgrouting.org/latest/en/index.html)

