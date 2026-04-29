---
title: "Requirements summary"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/installation/reqsummary/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/installation/reqsummary/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:13.281Z"
content_hash: "a6e050cadf17b2b9af37b7c21ee692b644f61560f6149cc63ac34a72f9823292"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Install and upgrade","→","Install and upgrade","→\n      \n        Requirements summary","→","Requirements summary"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Install and upgrade","→","Install and upgrade","→\n      \n        Requirements summary","→","Requirements summary"]
nav_prev: {"path": "../../data-pipelines/transform-examples/index.md", "title": "Job files"}
nav_next: {"path": "../../reference/data-transformation/add_field/index.md", "title": "add_field"}
---

# Requirements summary

Requirements and recommendations for RDI installations.

The sections below summarize the software and hardware requirements for an RDI installation.

## Hardware requirements for VM installation

*   **CPU**: A minimum of 4 CPU cores. You should consider adding 2-6 extra cores on top of this if your dataset is big and you want to ingest the baseline snapshot as fast as possible.
*   **RAM**: 8GB
*   **Disk**: On top of the OS footprint, RDI requires 20GB in the `/var` folder and 1GB in the `/opt` folder (to store the log files). This allows space for upgrades.
*   **Network interface**: 10GB or more.

## OS requirements for VM installation

*   RHEL 8 or 9
*   Ubuntu 20.04, 22.04, or 24.04

## Kubernetes/OpenShift supported versions

RDI only supports versions of Kubernetes and OpenShift that have not yet reached end-of-life (EOL). See the [Kubernetes](https://kubernetes.io/releases/) and [OpenShift](https://access.redhat.com/support/policy/updates/openshift) lifecycle pages for the latest updates.

## RDI database requirements

*   Redis Enterprise v6.4 or greater for the cluster.
    
*   For production, 250MB RAM with one primary and one replica is recommended, but for the quickstart or for development, 125MB and a single shard is sufficient.
    
*   If you are deploying RDI for a production environment then secure this database with a password and TLS.
    
*   Set the database's [eviction policy](/docs/latest/operate/rs/databases/memory-performance/eviction-policy/) to `noeviction`. Note that you can't set this using [`rladmin`](/docs/latest/operate/rs/references/cli-utilities/rladmin/), so you must either do it using the admin UI or with the following [REST API](/docs/latest/operate/rs/references/rest-api/) command:
    
    ```bash
    curl -v -k -d '{"eviction_policy": "noeviction"}' \
      -u '<USERNAME>:<PASSWORD>' \
      -H "Content-Type: application/json" \
      -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
    ```
    
*   Set the database's [data persistence](/docs/latest/operate/rs/databases/configure/database-persistence/) to AOF - fsync every 1 sec. Note that you can't set this using [`rladmin`](/docs/latest/operate/rs/references/cli-utilities/rladmin/), so you must either do it using the admin UI or with the following [REST API](/docs/latest/operate/rs/references/rest-api/) commands:
    
    ```bash
    curl -v -k -d '{"data_persistence":"aof"}' \
      -u '<USERNAME>:<PASSWORD>' \
      -H "Content-Type: application/json" 
      -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
    curl -v -k -d '{"aof_policy":"appendfsync-every-sec"}' \
      -u '<USERNAME>:<PASSWORD>' \
      -H "Content-Type: application/json" \
      -X PUT https://<CLUSTER_FQDN>:9443/v1/bdbs/<BDB_UID>
    ```
    

If you don't have permissions to use AOF persistence, please check the [Using RDI without persistence](/docs/latest/integrate/redis-data-integration/faq/#can-i-use-rdi-without-persistence-enabled) section in the FAQ.

*   **Ensure that the RDI database is not clustered.** RDI will not work correctly if the RDI database is clustered (but note that the target database _can_ be clustered without any problems).
    
    If the **Database clustering** option is checked when you create the RDI database (as shown below), you must _uncheck_ it before proceeding.
    
    [![Uncluster the RDI database.](/docs/latest/images/rdi/ingest/RDIClusterSetting.webp)](/docs/latest/images/rdi/ingest/RDIClusterSetting.webp)
    
    You can check if your RDI database is clustered from its **Configuration** tab in the Redis Enterprise console. The **Database clustering** option should be set to **None**, as shown in the following screenshot:
    
    [![Check that the RDI database is not clustered.](/docs/latest/images/rdi/ingest/RDICheckUnclustered.webp)](/docs/latest/images/rdi/ingest/RDICheckUnclustered.webp)
    
    If you find the database has been clustered by mistake, you must create a new database with clustering disabled before continuing with the RDI installation.
    

## Supported source databases

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

## On this page
