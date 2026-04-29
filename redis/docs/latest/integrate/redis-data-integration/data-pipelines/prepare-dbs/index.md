---
title: "Prepare source databases"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:11.482Z"
content_hash: "78c679e80707636740d882905a7f7d3d9ee73e6fee9d0eb25a95f5d4b1307b45"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases"]
nav_prev: {"path": "../pipeline-config/index.md", "title": "Pipeline configuration file"}
nav_next: {"path": "aws-aurora-rds/index.md", "title": "Prepare AWS RDS and Aurora databases for RDI"}
---

# Prepare source databases

Enable CDC features in your source databases

Each database uses a different mechanism to track changes to its data and generally, these mechanisms are not switched on by default. RDI's Debezium collector uses these mechanisms for change data capture (CDC), so you must prepare your source database before you can use it with RDI.

RDI supports the following source databases:

Database

Versions

AWS RDS Versions

GCP SQL Versions

Oracle

19c, 21c, 23ai (LogMiner only)

19c, 21c

\-

MariaDB

10.5, 11.4.x, 11.7.x

10.4 to 10.11, 11.4.3

\-

MongoDB

6.0, 7.0, 8.0

\-

\-

MySQL

5.7, 8.0.x, 8.4.x, 9.0, 9.1

8.0.x

8.0

PostgreSQL

10, 11, 12, 13, 14, 15, 16, 17

11, 12, 13, 14, 15, 16

15

Supabase (uses PostgreSQL)

10, 11, 12, 13, 14, 15, 16, 17

\-

\-

SQL Server

2017, 2019, 2022

2016, 2017, 2019, 2022

2019

Spanner

\-

\-

All versions

AlloyDB for PostgreSQL

14.2, 15.7

\-

14.2, 15.7

AWS Aurora/PostgreSQL

15

15

\-

Neon

14, 15, 16, 17

\-

\-

The pages in this section give detailed instructions to get your source database ready for Debezium to use:
