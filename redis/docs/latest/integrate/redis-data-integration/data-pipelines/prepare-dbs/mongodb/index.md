---
title: "Prepare MongoDB for RDI"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/mongodb/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/mongodb/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:41.681Z"
content_hash: "31b53ea489c2853d69c5485724b6f41207af8ea49fa1986f7ef9f008f9a26bfe"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare MongoDB for RDI","→","Prepare MongoDB for RDI"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare MongoDB for RDI","→","Prepare MongoDB for RDI"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-mysql/index.md", "title": "Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI"}
nav_next: {"path": "redis/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/my-sql-mariadb/index.md", "title": "Prepare MySQL/MariaDB for RDI"}
---

# Prepare MongoDB for RDI

Prepare MongoDB databases to work with RDI

This guide describes the steps required to prepare a MongoDB database as a source for Redis Data Integration (RDI) pipelines.

## Prerequisites

*   **MongoDB version:** 6.0 or later (replica set, sharded cluster, or MongoDB Atlas).
*   **User privileges:** You must have a MongoDB user with sufficient privileges to read the oplog and collections, and to use change streams.
*   **Network access:** The RDI Collector must be able to connect to all MongoDB nodes in your deployment.

Note:

The MongoDB connector is not capable of monitoring the changes of a standalone MongoDB server, since standalone servers do not have an oplog. The connector will work if the standalone server is converted to a replica set with one member.

## Summary

The following table summarizes the considerations to prepare a MongoDB database for RDI.

Requirement

Description

MongoDB Topology

Replica Set, Sharded Cluster, or MongoDB Atlas

User Roles

readAnyDatabase, clusterMonitor

Oplog

Sufficient size for snapshot and streaming

Pre/Post Images

Enable on collections **only if using a custom key**

Connection String

Must include all hosts, replicaSet (if applicable), authSource, credentials

MongoDB Atlas

**[SSL required](https://debezium.io/documentation/reference/stable/connectors/mongodb.html#mongodb-property-mongodb-ssl-enabled)**, provide root CA as `SOURCE_DB_CACERT` secret in RDI

Network

RDI Collector must reach all MongoDB nodes on required ports

The following checklist shows the steps to prepare a MongoDB database for RDI, with links to the sections that explain the steps in full detail. You may find it helpful to track your progress with the checklist as you complete each step.

## 1\. Configure oplog size

The Debezium MongoDB connector relies on the [oplog](https://www.mongodb.com/docs/manual/core/replica-set-oplog/) to capture changes from a replica set. The oplog is a fixed-size, capped collection. When it reaches its maximum size, it overwrites the oldest entries. If the connector is stopped and restarted, it attempts to resume from its last recorded position in the oplog. If that position has been overwritten, the connector may fail to start and report an invalid resume token error.

To prevent this, ensure the oplog retains enough history for Debezium to resume streaming after interruptions. You can do this by:

*   **Increasing the oplog size:** Set the oplog size based on your workload, ensuring it can store more than the peak number of oplog entries generated per hour.
*   **Setting a minimum oplog retention period (MongoDB 4.4+):** Configure MongoDB to retain oplog entries for a minimum number of hours, guaranteeing availability even if the oplog reaches its maximum size. This is generally preferred, but for high-throughput clusters nearing capacity, you may need to increase the oplog size instead.

For detailed guidance, see the Debezium [oplog configuration documentation](https://debezium.io/documentation/reference/stable/connectors/mongodb.html#mongodb-optimal-oplog-config).

## 2\. Create a MongoDB user for RDI

Create a user with the following roles on the source database:

*   `readAnyDatabase` (optional) OR grant `read` for the specific database(s) you will use with RDI
*   `clusterMonitor`

Example:

```javascript
use admin;
db.createUser({
  user: "rdi_user",
  pwd: "rdi_password",
  roles: [
     // You can have multiple read roles, one per database.
    { role: "read", db: "your_database" },
    // Use the role below if you don't want to grant the `read` role for each database.
    // { role: "readAnyDatabase", db: "admin" },
    { role: "clusterMonitor", db: "admin" }
  ]
});
```

## 3\. Connection string format

The RDI Collector requires a MongoDB connection string that includes all relevant hosts and authentication details.

Example (Replica Set):

```
mongodb://${SOURCE_DB_USERNAME}:${SOURCE_DB_PASSWORD}@host1:27017,host2:27017,host3:27017/?replicaSet=rs0&authSource=admin
```

Example (Sharded Cluster):

```
mongodb://${SOURCE_DB_USERNAME}:${SOURCE_DB_PASSWORD}@host:30000
```

*   For Atlas, adjust the connection string accordingly (see example below).
*   Set `replicaSet` and `authSource` as appropriate for your deployment.

## 4\. Enable change streams and pre/post images (only if using a custom key)

Change Streams are required only if you are using a custom key in your RDI pipeline. Change streams are available by default on replica sets, sharded clusters, and MongoDB Atlas.

If your RDI pipeline uses a custom key, you must enable pre- and post-images on the relevant collections to capture the document state before and after updates or deletes. This allows RDI to access both the previous and updated versions of documents during change events, ensuring accurate synchronization.

Use the command below to enable change streams and pre/post images:

```javascript
db.runCommand({
  collMod: "your_collection",
  changeStreamPreAndPostImages: { enabled: true }
});
```

## 5\. MongoDB Atlas specific requirements

MongoDB Atlas only supports secure connections via SSL. The root CA certificate for MongoDB Atlas must be added as a SOURCE\_DB\_CACERT secret in RDI.

*   Download the MongoDB Atlas root CA certificate.
*   In RDI, add this certificate as a secret named SOURCE\_DB\_CACERT.
*   Ensure that the `mongodb.ssl.enabled: true` setting is present in your RDI configuration.

Example connection string for Atlas:

```
mongodb+srv://${SOURCE_DB_USERNAME}:${SOURCE_DB_PASSWORD}@cluster0.mongodb.net/?authSource=admin
```

## 6\. Network and security

*   Ensure the RDI Collector can connect to all MongoDB nodes on the required ports (default: 27017, or as provided by Atlas).
*   If using TLS/SSL, provide the necessary certificates and connection options in the connection string.

## 7\. Configuration is complete

Once you have followed the steps above, your MongoDB database is ready for Debezium to use.

## See also

*   [MongoDB Replica Set Documentation](https://www.mongodb.com/docs/manual/replication/)
*   [MongoDB Sharded Cluster Documentation](https://www.mongodb.com/docs/manual/sharding/)
*   [MongoDB Change Streams](https://www.mongodb.com/docs/manual/changeStreams/)
*   [MongoDB User Management](https://www.mongodb.com/docs/manual/core/security-users/)
*   [Debezium MongoDB Connector Documentation](https://debezium.io/documentation/reference/stable/connectors/mongodb.html)
*   [MongoDB Atlas SSL Setup](https://debezium.io/documentation/reference/stable/connectors/mongodb.html#mongodb-in-the-cloud)

## On this page

