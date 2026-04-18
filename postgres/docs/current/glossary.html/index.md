---
title: "PostgreSQL: Documentation: 18: Appendix M. Glossary"
source: "https://www.postgresql.org/docs/current/glossary.html"
canonical_url: "https://www.postgresql.org/docs/current/glossary.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:03.003Z"
content_hash: "e4264961ddf8a418e32ad0a565d3c2db9c4c213d0387ccd41e7acd8f79713f86"
menu_path: ["PostgreSQL: Documentation: 18: Appendix M. Glossary"]
section_path: []
---
This is a list of terms and their meaning in the context of PostgreSQL and relational database systems in general.

ACID

[](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMICITY)[Atomicity](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMICITY "Atomicity"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSISTENCY)[Consistency](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSISTENCY "Consistency"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ISOLATION)[Isolation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ISOLATION "Isolation"), and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DURABILITY)[Durability](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DURABILITY "Durability"). This set of properties of database transactions is intended to guarantee validity in concurrent operation and even in event of errors, power failures, etc.

Aggregate function (routine)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[function](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") that combines (_aggregates_) multiple input values, for example by counting, averaging or adding, yielding a single output value.

For more information, see [Section 9.21](https://www.postgresql.org/docs/current/functions-aggregate.html "9.21. Aggregate Functions").

See Also [Window function (routine)](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WINDOW-FUNCTION).

Access Method

Interfaces which PostgreSQL use in order to access data in tables and indexes. This abstraction allows for adding support for new types of data storage.

For more information, see [Chapter 62](https://www.postgresql.org/docs/current/tableam.html "Chapter 62. Table Access Method Interface Definition") and [Chapter 63](https://www.postgresql.org/docs/current/indexam.html "Chapter 63. Index Access Method Interface Definition").

Analytic function

See [Window function (routine)](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WINDOW-FUNCTION).

Analyze (operation)

The act of collecting statistics from data in [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") and other [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relations](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") to help the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PLANNER)[query planner](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PLANNER "Query planner") to make decisions about how to execute [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[queries](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query").

(Don't confuse this term with the `ANALYZE` option to the [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html "EXPLAIN") command.)

For more information, see [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE").

Asynchronous I/O (AIO)

Asynchronous I/O (AIO) describes performing I/O in a non-blocking way (asynchronously), in contrast to synchronous I/O, which blocks for the entire duration of the I/O.

With AIO, starting an I/O operation is separated from waiting for the result of the operation, allowing multiple I/O operations to be initiated concurrently, as well as performing CPU heavy operations concurrently with I/O. The price for that increased concurrency is increased complexity.

See Also [Input/Output](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-IO).

Atomic

In reference to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATUM)[datum](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATUM "Datum"): the fact that its value cannot be broken down into smaller components.

In reference to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[database transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction"): see [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMICITY)[atomicity](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMICITY "Atomicity").

Atomicity

The property of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction") that either all its operations complete as a single unit or none do. In addition, if a system failure occurs during the execution of a transaction, no partial results are visible after recovery. This is one of the ACID properties.

Attribute

An element with a certain name and data type found within a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[tuple](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple").

Autovacuum (process)

A set of background processes that routinely perform [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VACUUM)[vacuum](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VACUUM "Vacuum") and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ANALYZE)[analyze](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ANALYZE "Analyze (operation)") operations. The [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that coordinates the work and is always present (unless autovacuum is disabled) is known as the _autovacuum launcher_, and the processes that carry out the tasks are known as the _autovacuum workers_.

For more information, see [Section 24.1.6](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM "24.1.6. The Autovacuum Daemon").

Auxiliary process

A process within an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") that is in charge of some specific background task for the instance. The auxiliary processes consist of the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUTOVACUUM)[autovacuum launcher](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUTOVACUUM "Autovacuum (process)") (but not the autovacuum workers), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WRITER)[background writer](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WRITER "Background writer (process)"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINTER)[checkpointer](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINTER "Checkpointer (process)"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGER)[logger](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGER "Logger (process)"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-STARTUP-PROCESS)[startup process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-STARTUP-PROCESS "Startup process"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-ARCHIVER)[WAL archiver](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-ARCHIVER "WAL archiver (process)"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECEIVER)[WAL receiver](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECEIVER "WAL receiver (process)") (but not the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-SENDER)[WAL senders](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-SENDER "WAL sender (process)")), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-SUMMARIZER)[WAL summarizer](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-SUMMARIZER "WAL summarizer (process)"), and the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-WRITER)[WAL writer](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-WRITER "WAL writer (process)").

Backend (process)

Process of an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") which acts on behalf of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION)[client session](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION "Session") and handles its requests.

(Don't confuse this term with the similar terms [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WORKER)[Background Worker](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WORKER "Background worker (process)") or [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WRITER)[Background Writer](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKGROUND-WRITER "Background writer (process)")).

Background worker (process)

Process within an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance"), which runs system- or user-supplied code. Serves as infrastructure for several features in PostgreSQL, such as [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION)[logical replication](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION "Replication") and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARALLEL-QUERY)[parallel queries](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARALLEL-QUERY "Parallel query"). In addition, [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-EXTENSION)[Extensions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-EXTENSION "Extension") can add custom background worker processes.

For more information, see [Chapter 46](https://www.postgresql.org/docs/current/bgworker.html "Chapter 46. Background Worker Processes").

Background writer (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that writes dirty [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-PAGE)[data pages](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-PAGE "Data page") from [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared memory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") to the file system. It wakes up periodically, but works only for a short period in order to distribute its expensive I/O activity over time to avoid generating larger I/O peaks which could block other processes.

For more information, see [Section 19.4.4](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-BACKGROUND-WRITER "19.4.4. Background Writer").

Base Backup

A binary copy of all [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster") files. It is generated by the tool [pg\_basebackup](https://www.postgresql.org/docs/current/app-pgbasebackup.html "pg_basebackup"). In combination with WAL files it can be used as the starting point for recovery, log shipping, or streaming replication.

Bloat

Space in data pages which does not contain current row versions, such as unused (free) space or outdated row versions.

Bootstrap superuser

The first [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER)[user](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER "User") initialized in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster").

This user owns all system catalog tables in each database. It is also the role from which all granted permissions originate. Because of these things, this role may not be dropped.

This role also behaves as a normal [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE-SUPERUSER)[database superuser](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE-SUPERUSER "Database superuser"), and its superuser status cannot be removed.

Buffer Access Strategy

Some operations will access a large number of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-PAGE)[pages](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-PAGE "Data page"). A _Buffer Access Strategy_ helps to prevent these operations from evicting too many pages from [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared buffers](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory").

A Buffer Access Strategy sets up references to a limited number of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared buffers](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") and reuses them circularly. When the operation requires a new page, a victim buffer is chosen from the buffers in the strategy ring, which may require flushing the page's dirty data and possibly also unflushed [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log") to permanent storage.

Buffer Access Strategies are used for various operations such as sequential scans of large tables, `VACUUM`, `COPY`, `CREATE TABLE AS SELECT`, `ALTER TABLE`, `CREATE DATABASE`, `CREATE INDEX`, and `CLUSTER`.

Cast

A conversion of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATUM)[datum](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATUM "Datum") from its current data type to another data type.

For more information, see [CREATE CAST](https://www.postgresql.org/docs/current/sql-createcast.html "CREATE CAST").

Catalog

The SQL standard uses this term to indicate what is called a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") in PostgreSQL's terminology.

(Don't confuse this term with [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SYSTEM-CATALOG)[system catalog](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SYSTEM-CATALOG "System catalog")).

For more information, see [Section 22.1](https://www.postgresql.org/docs/current/manage-ag-overview.html "22.1. Overview").

Check constraint

A type of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT)[constraint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT "Constraint") defined on a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") which restricts the values allowed in one or more [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute"). The check constraint can make reference to any attribute of the same row in the relation, but cannot reference other rows of the same relation or other relations.

For more information, see [Section 5.5](https://www.postgresql.org/docs/current/ddl-constraints.html "5.5. Constraints").

Checkpoint

A point in the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log") sequence at which it is guaranteed that the heap and index data files have been updated with all information from [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared memory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") modified before that checkpoint; a _checkpoint record_ is written and flushed to WAL to mark that point.

A checkpoint is also the act of carrying out all the actions that are necessary to reach a checkpoint as defined above. This process is initiated when predefined conditions are met, such as a specified amount of time has passed, or a certain volume of records has been written; or it can be invoked by the user with the command `CHECKPOINT`.

For more information, see [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration").

Checkpointer (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that is responsible for executing [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT)[checkpoints](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT "Checkpoint").

Class (archaic)

See [Relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION).

Client (process)

Any process, possibly remote, that establishes a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION)[session](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION "Session") by [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION)[connecting](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION "Connection") to an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") to interact with a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database").

Cluster owner

The operating system user that owns the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-DIRECTORY)[data directory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-DIRECTORY "Data directory") and under which the `postgres` process is run. It is required that this user exist prior to creating a new [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster").

On operating systems with a `root` user, said user is not allowed to be the cluster owner.

Column

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attribute](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute") found in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") or [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW)[view](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW "View").

Commit

The act of finalizing a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction") within the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database"), which makes it visible to other transactions and assures its [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DURABILITY)[durability](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DURABILITY "Durability").

For more information, see [COMMIT](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT").

Concurrency

The concept that multiple independent operations happen within the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") at the same time. In PostgreSQL, concurrency is controlled by the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MVCC)[multiversion concurrency control](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MVCC "Multi-version concurrency control (MVCC)") mechanism.

Connection

An established line of communication between a client process and a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)") process, usually over a network, supporting a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION)[session](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION "Session"). This term is sometimes used as a synonym for session.

For more information, see [Section 19.3](https://www.postgresql.org/docs/current/runtime-config-connection.html "19.3. Connections and Authentication").

Consistency

The property that the data in the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") is always in compliance with [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT)[integrity constraints](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT "Constraint"). Transactions may be allowed to violate some of the constraints transiently before it commits, but if such violations are not resolved by the time it commits, such a transaction is automatically [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLLBACK)[rolled back](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLLBACK "Rollback"). This is one of the ACID properties.

Constraint

A restriction on the values of data allowed within a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"), or in attributes of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DOMAIN)[domain](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DOMAIN "Domain").

For more information, see [Section 5.5](https://www.postgresql.org/docs/current/ddl-constraints.html "5.5. Constraints").

Cumulative Statistics System

A system which, if enabled, accumulates statistical information about the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance")'s activities.

For more information, see [Section 27.2](https://www.postgresql.org/docs/current/monitoring-stats.html "27.2. The Cumulative Statistics System").

Data area

See [Data directory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATA-DIRECTORY).

Database

A named collection of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT)[local SQL objects](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT "SQL object").

For more information, see [Section 22.1](https://www.postgresql.org/docs/current/manage-ag-overview.html "22.1. Overview").

Database cluster

A collection of databases and global SQL objects, and their common static and dynamic metadata. Sometimes referred to as a _cluster_. A database cluster is created using the [initdb](https://www.postgresql.org/docs/current/app-initdb.html "initdb") program.

In PostgreSQL, the term _cluster_ is also sometimes used to refer to an instance. (Don't confuse this term with the SQL command `CLUSTER`.)

See also [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLUSTER-OWNER)[cluster owner](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLUSTER-OWNER "Cluster owner"), the operating-system owner of a cluster, and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BOOTSTRAP-SUPERUSER)[bootstrap superuser](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BOOTSTRAP-SUPERUSER "Bootstrap superuser"), the PostgreSQL owner of a cluster.

Database server

See [Instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE).

Database superuser

A role having _superuser status_ (see [Section 21.2](https://www.postgresql.org/docs/current/role-attributes.html "21.2. Role Attributes")).

Frequently referred to as _superuser_.

Data directory

The base directory on the file system of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER)[server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER "Server") that contains all data files and subdirectories associated with a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster") (with the exception of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLESPACE)[tablespaces](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLESPACE "Tablespace"), and optionally [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log")). The environment variable `PGDATA` is commonly used to refer to the data directory.

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster")'s storage space comprises the data directory plus any additional tablespaces.

For more information, see [Section 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html "66.1. Database File Layout").

Data page

The basic structure used to store relation data. All pages are of the same size. Data pages are typically stored on disk, each in a specific file, and can be read to [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared buffers](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") where they can be modified, becoming _dirty_. They become clean when written to disk. New pages, which initially exist in memory only, are also dirty until written.

Datum

The internal representation of one value of an SQL data type.

Delete

An SQL command which removes [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") from a given [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") or [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation").

For more information, see [DELETE](https://www.postgresql.org/docs/current/sql-delete.html "DELETE").

Domain

A user-defined data type that is based on another underlying data type. It acts the same as the underlying type except for possibly restricting the set of allowed values.

For more information, see [Section 8.18](https://www.postgresql.org/docs/current/domains.html "8.18. Domain Types").

Durability

The assurance that once a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction") has been [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COMMIT)[committed](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COMMIT "Commit"), the changes remain even after a system failure or crash. This is one of the ACID properties.

Epoch

See [Transaction ID](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-XID).

Extension

A software add-on package that can be installed on an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") to get extra features.

For more information, see [Section 36.17](https://www.postgresql.org/docs/current/extend-extensions.html "36.17. Packaging Related Objects into an Extension").

File segment

A physical file which stores data for a given [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation"). File segments are limited in size by a configuration value (typically 1 gigabyte), so if a relation exceeds that size, it is split into multiple segments.

For more information, see [Section 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html "66.1. Database File Layout").

(Don't confuse this term with the similar term [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE)[WAL segment](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE "WAL file")).

Foreign data wrapper

A means of representing data that is not contained in the local [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") so that it appears as if were in local [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table(s)](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"). With a foreign data wrapper it is possible to define a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-SERVER)[foreign server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-SERVER "Foreign server") and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE)[foreign tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE "Foreign table (relation)").

For more information, see [CREATE FOREIGN DATA WRAPPER](https://www.postgresql.org/docs/current/sql-createforeigndatawrapper.html "CREATE FOREIGN DATA WRAPPER").

Foreign key

A type of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT)[constraint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT "Constraint") defined on one or more [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN)[columns](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN "Column") in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") which requires the value(s) in those [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN)[columns](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN "Column") to identify zero or one [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[row](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") in another (or, infrequently, the same) [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table").

Foreign server

A named collection of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE)[foreign tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE "Foreign table (relation)") which all use the same [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER)[foreign data wrapper](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER "Foreign data wrapper") and have other configuration values in common.

For more information, see [CREATE SERVER](https://www.postgresql.org/docs/current/sql-createserver.html "CREATE SERVER").

Foreign table (relation)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") which appears to have [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN)[columns](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-COLUMN "Column") similar to a regular [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"), but will forward requests for data through its [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER)[foreign data wrapper](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER "Foreign data wrapper"), which will return [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET)[result sets](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET "Result set") structured according to the definition of the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE)[foreign table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE "Foreign table (relation)").

For more information, see [CREATE FOREIGN TABLE](https://www.postgresql.org/docs/current/sql-createforeigntable.html "CREATE FOREIGN TABLE").

Fork

Each of the separate segmented file sets in which a relation is stored. The _main fork_ is where the actual data resides. There also exist two secondary forks for metadata: the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FSM)[free space map](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FSM "Free space map (fork)") and the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VM)[visibility map](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VM "Visibility map (fork)"). [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNLOGGED)[Unlogged relations](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNLOGGED "Unlogged") also have an _init fork_.

Free space map (fork)

A storage structure that keeps metadata about each data page of a table's main fork. The free space map entry for each page stores the amount of free space that's available for future tuples, and is structured to be efficiently searched for available space for a new tuple of a given size.

For more information, see [Section 66.3](https://www.postgresql.org/docs/current/storage-fsm.html "66.3. Free Space Map").

Function (routine)

A type of routine that receives zero or more arguments, returns zero or more output values, and is constrained to run within one transaction. Functions are invoked as part of a query, for example via `SELECT`. Certain functions can return [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET)[sets](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET "Result set"); those are called _set-returning functions_.

Functions can also be used for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRIGGER)[triggers](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRIGGER "Trigger") to invoke.

For more information, see [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION").

GMT

See [UTC](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UTC).

Grant

An SQL command that is used to allow a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER)[user](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER "User") or [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE)[role](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE "Role") to access specific objects within the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database").

For more information, see [GRANT](https://www.postgresql.org/docs/current/sql-grant.html "GRANT").

Heap

Contains the values of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[row](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") attributes (i.e., the data) for a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation"). The heap is realized within one or more [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FILE-SEGMENT)[file segments](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FILE-SEGMENT "File segment") in the relation's [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FORK)[main fork](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FORK "Fork").

Host

A computer that communicates with other computers over a network. This is sometimes used as a synonym for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER)[server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER "Server"). It is also used to refer to a computer where [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT)[client processes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT "Client (process)") run.

Index (relation)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that contains data derived from a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") or [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW)[materialized view](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW "Materialized view (relation)"). Its internal structure supports fast retrieval of and access to the original data.

For more information, see [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html "CREATE INDEX").

Incremental backup

A special [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BASEBACKUP)[base backup](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BASEBACKUP "Base Backup") that for some files may contain only those pages that were modified since a previous backup, as opposed to the full contents of every file. Like base backups, it is generated by the tool [pg\_basebackup](https://www.postgresql.org/docs/current/app-pgbasebackup.html "pg_basebackup").

To restore incremental backups the tool [pg\_combinebackup](https://www.postgresql.org/docs/current/app-pgcombinebackup.html "pg_combinebackup") is used, which combines incremental backups with a base backup. Afterwards, recovery can use [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log") to bring the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster") to a consistent state.

For more information, see [Section 25.3.3](https://www.postgresql.org/docs/current/continuous-archiving.html#BACKUP-INCREMENTAL-BACKUP "25.3.3. Making an Incremental Backup").

Input/Output (I/O)

Input/Output (I/O) describes the communication between a program and peripheral devices. In the context of database systems, I/O commonly, but not exclusively, refers to interaction with storage devices or the network.

See Also [Asynchronous I/O](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AIO).

Insert

An SQL command used to add new data into a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table").

For more information, see [INSERT](https://www.postgresql.org/docs/current/sql-insert.html "INSERT").

Instance

A group of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)") and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary processes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that communicate using a common shared memory area. One [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-POSTMASTER)[postmaster process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-POSTMASTER "Postmaster (process)") manages the instance; one instance manages exactly one [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster") with all its databases. Many instances can run on the same [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER)[server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER "Server") as long as their TCP ports do not conflict.

The instance handles all key features of a DBMS: read and write access to files and shared memory, assurance of the ACID properties, [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION)[connections](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION "Connection") to [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT)[client processes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT "Client (process)"), privilege verification, crash recovery, replication, etc.

Isolation

The property that the effects of a transaction are not visible to [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONCURRENCY)[concurrent transactions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONCURRENCY "Concurrency") before it commits. This is one of the ACID properties.

For more information, see [Section 13.2](https://www.postgresql.org/docs/current/transaction-iso.html "13.2. Transaction Isolation").

Join

An operation and SQL keyword used in [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[queries](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query") for combining data from multiple [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relations](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation").

Key

A means of identifying a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[row](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") within a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") or other [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") by values contained within one or more [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute") in that relation.

Lock

A mechanism that allows a process to limit or prevent simultaneous access to a resource.

Log file

Log files contain human-readable text lines about events. Examples include login failures, long-running queries, etc.

For more information, see [Section 24.3](https://www.postgresql.org/docs/current/logfile-maintenance.html "24.3. Log File Maintenance").

Logged

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") is considered [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGED)[logged](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGED "Logged") if changes to it are sent to the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log"). By default, all regular tables are logged. A table can be specified as [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNLOGGED)[unlogged](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNLOGGED "Unlogged") either at creation time or via the `ALTER TABLE` command.

Logger (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") which, if enabled, writes information about database events into the current [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOG-FILE)[log file](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOG-FILE "Log file"). When reaching certain time- or volume-dependent criteria, a new log file is created. Also called _syslogger_.

For more information, see [Section 19.8](https://www.postgresql.org/docs/current/runtime-config-logging.html "19.8. Error Reporting and Logging").

Logical replication cluster

A set of publisher and subscriber instances with the publisher instance replicating changes to the subscriber instance.

Log record

Archaic term for a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD)[WAL record](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD "WAL record").

Log sequence number (LSN)

Byte offset into the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log"), increasing monotonically with each new [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD)[WAL record](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD "WAL record").

For more information, see [`pg_lsn`](https://www.postgresql.org/docs/current/datatype-pg-lsn.html "8.20. pg_lsn Type") and [Section 28.6](https://www.postgresql.org/docs/current/wal-internals.html "28.6. WAL Internals").

LSN

See [Log sequence number](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOG-SEQUENCE-NUMBER).

Master (server)

See [Primary (server)](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER).

Materialized

The property that some information has been pre-computed and stored for later use, rather than computing it on-the-fly.

This term is used in [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW)[materialized view](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW "Materialized view (relation)"), to mean that the data derived from the view's query is stored on disk separately from the sources of that data.

This term is also used to refer to some multi-step queries to mean that the data resulting from executing a given step is stored in memory (with the possibility of spilling to disk), so that it can be read multiple times by another step.

Materialized view (relation)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that is defined by a `SELECT` statement (just like a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW)[view](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW "View")), but stores data in the same way that a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") does. It cannot be modified via `INSERT`, `UPDATE`, `DELETE`, or `MERGE` operations.

For more information, see [CREATE MATERIALIZED VIEW](https://www.postgresql.org/docs/current/sql-creatematerializedview.html "CREATE MATERIALIZED VIEW").

Merge

An SQL command used to conditionally add, modify, or remove [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") in a given [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"), using data from a source [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation").

For more information, see [MERGE](https://www.postgresql.org/docs/current/sql-merge.html "MERGE").

Multi-version concurrency control (MVCC)

A mechanism designed to allow several [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transactions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction") to be reading and writing the same rows without one process causing other processes to stall. In PostgreSQL, MVCC is implemented by creating copies (_versions_) of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[tuples](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") as they are modified; after transactions that can see the old versions terminate, those old versions need to be removed.

Null

A concept of non-existence that is a central tenet of relational database theory. It represents the absence of a definite value.

Optimizer

See [Query planner](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PLANNER).

Parallel query

The ability to handle parts of executing a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[query](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query") to take advantage of parallel processes on servers with multiple CPUs.

Partition

One of several disjoint (not overlapping) subsets of a larger set.

In reference to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITIONED-TABLE)[partitioned table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITIONED-TABLE "Partitioned table (relation)"): One of the tables that each contain part of the data of the partitioned table, which is said to be the _parent_. The partition is itself a table, so it can also be queried directly; at the same time, a partition can sometimes be a partitioned table, allowing hierarchies to be created.

In reference to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WINDOW-FUNCTION)[window function](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WINDOW-FUNCTION "Window function (routine)") in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[query](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query"), a partition is a user-defined criterion that identifies which neighboring [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") of the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET)[query's result set](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET "Result set") can be considered by the function.

Partitioned table (relation)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that is in semantic terms the same as a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"), but whose storage is distributed across several [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITION)[partitions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITION "Partition").

Postmaster (process)

The very first process of an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance"). It starts and manages the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary processes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") and creates [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend processes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)") on demand.

For more information, see [Section 18.3](https://www.postgresql.org/docs/current/server-start.html "18.3. Starting the Database Server").

Primary key

A special case of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNIQUE-CONSTRAINT)[unique constraint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-UNIQUE-CONSTRAINT "Unique constraint") defined on a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") or other [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that also guarantees that all of the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute") within the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-KEY)[primary key](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-KEY "Primary key") do not have [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-NULL)[null](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-NULL "Null") values. As the name implies, there can be only one primary key per table, though it is possible to have multiple unique constraints that also have no null-capable attributes.

Primary (server)

When two or more [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[databases](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") are linked via [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION)[replication](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION "Replication"), the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER)[server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER "Server") that is considered the authoritative source of information is called the _primary_, also known as a _master_.

Procedure (routine)

A type of routine. Their distinctive qualities are that they do not return values, and that they are allowed to make transactional statements such as `COMMIT` and `ROLLBACK`. They are invoked via the `CALL` command.

For more information, see [CREATE PROCEDURE](https://www.postgresql.org/docs/current/sql-createprocedure.html "CREATE PROCEDURE").

Query

A request sent by a client to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)"), usually to return results or to modify data on the database.

Query planner

The part of PostgreSQL that is devoted to determining (_planning_) the most efficient way to execute [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[queries](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query"). Also known as _query optimizer_, _optimizer_, or simply _planner_.

Record

See [Tuple](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE).

Recycling

See [WAL file](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE).

Referential integrity

A means of restricting data in one [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") by a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-KEY)[foreign key](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-KEY "Foreign key") so that it must have matching data in another [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation").

Relation

The generic term for all objects in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") that have a name and a list of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute") defined in a specific order. [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[Tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SEQUENCE)[sequences](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SEQUENCE "Sequence (relation)"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW)[views](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW "View"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE)[foreign tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-TABLE "Foreign table (relation)"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW)[materialized views](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MATERIALIZED-VIEW "Materialized view (relation)"), composite types, and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INDEX)[indexes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INDEX "Index (relation)") are all relations.

More generically, a relation is a set of tuples; for example, the result of a query is also a relation.

In PostgreSQL, _Class_ is an archaic synonym for _relation_.

Replica (server)

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") that is paired with a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER)[primary](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER "Primary (server)") database and is maintaining a copy of some or all of the primary database's data. The foremost reasons for doing this are to allow for greater access to that data, and to maintain availability of the data in the event that the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER)[primary](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER "Primary (server)") becomes unavailable.

Replication

The act of reproducing data on one [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER)[server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SERVER "Server") onto another server called a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA)[replica](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA "Replica (server)"). This can take the form of _physical replication_, where all file changes from one server are copied verbatim, or _logical replication_ where a defined subset of data changes are conveyed using a higher-level representation.

Restartpoint

A variant of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT)[checkpoint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT "Checkpoint") performed on a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA)[replica](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA "Replica (server)").

For more information, see [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration").

Result set

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") transmitted from a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)") to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT)[client](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT "Client (process)") upon the completion of an SQL command, usually a `SELECT` but it can be an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` command if the `RETURNING` clause is specified.

The fact that a result set is a relation means that a query can be used in the definition of another query, becoming a _subquery_.

Revoke

A command to prevent access to a named set of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") objects for a named list of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE)[roles](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE "Role").

For more information, see [REVOKE](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE").

Role

A collection of access privileges to the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database"). Roles are themselves a privilege that can be granted to other roles. This is often done for convenience or to ensure completeness when multiple [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER)[users](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-USER "User") need the same privileges.

For more information, see [CREATE ROLE](https://www.postgresql.org/docs/current/sql-createrole.html "CREATE ROLE").

Rollback

A command to undo all of the operations performed since the beginning of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction").

For more information, see [ROLLBACK](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK").

Routine

A defined set of instructions stored in the database system that can be invoked for execution. A routine can be written in a variety of programming languages. Routines can be [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[functions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") (including set-returning functions and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRIGGER)[trigger functions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRIGGER "Trigger")), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AGGREGATE)[aggregate functions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AGGREGATE "Aggregate function (routine)"), and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PROCEDURE)[procedures](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PROCEDURE "Procedure (routine)").

Many routines are already defined within PostgreSQL itself, but user-defined ones can also be added.

Row

See [Tuple](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE).

Savepoint

A special mark in the sequence of steps in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction"). Data modifications after this point in time may be reverted to the time of the savepoint.

For more information, see [SAVEPOINT](https://www.postgresql.org/docs/current/sql-savepoint.html "SAVEPOINT").

Schema

A schema is a namespace for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT)[SQL objects](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT "SQL object"), which all reside in the same [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database"). Each SQL object must reside in exactly one schema.

All system-defined SQL objects reside in schema `pg_catalog`.

More generically, the term _schema_ is used to mean all data descriptions ([](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") definitions, [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT)[constraints](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT "Constraint"), comments, etc.) for a given [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") or subset thereof.

For more information, see [Section 5.10](https://www.postgresql.org/docs/current/ddl-schemas.html "5.10. Schemas").

Segment

See [File segment](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FILE-SEGMENT).

Select

The SQL command used to request data from a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database"). Normally, `SELECT` commands are not expected to modify the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") in any way, but it is possible that [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[functions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") invoked within the query could have side effects that do modify data.

For more information, see [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT").

Sequence (relation)

A type of relation that is used to generate values. Typically the generated values are sequential non-repeating numbers. They are commonly used to generate surrogate [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-KEY)[primary key](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-KEY "Primary key") values.

Server

A computer on which PostgreSQL [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instances](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") run. The term _server_ denotes real hardware, a container, or a _virtual machine_.

This term is sometimes used to refer to an instance or to a host.

Session

A state that allows a client and a backend to interact, communicating over a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION)[connection](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONNECTION "Connection").

Shared memory

RAM which is used by the processes common to an [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance"). It mirrors parts of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") files, provides a transient area for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD)[WAL records](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD "WAL record"), and stores additional common information. Note that shared memory belongs to the complete instance, not to a single database.

The largest part of shared memory is known as _shared buffers_ and is used to mirror part of data files, organized into pages. When a page is modified, it is called a dirty page until it is written back to the file system.

For more information, see [Section 19.4.1](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY "19.4.1. Memory").

SQL object

Any object that can be created with a `CREATE` command. Most objects are specific to one database, and are commonly known as _local objects_.

Most local objects reside in a specific [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SCHEMA)[schema](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SCHEMA "Schema") in their containing database, such as [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relations](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") (all types), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[routines](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") (all types), data types, etc. The names of such objects of the same type in the same schema are enforced to be unique.

There also exist local objects that do not reside in schemas; some examples are [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-EXTENSION)[extensions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-EXTENSION "Extension"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CAST)[data type casts](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CAST "Cast"), and [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER)[foreign data wrappers](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER "Foreign data wrapper"). The names of such objects of the same type are enforced to be unique within the database.

Other object types, such as [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE)[roles](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE "Role"), [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLESPACE)[tablespaces](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLESPACE "Tablespace"), replication origins, subscriptions for logical replication, and databases themselves are not local SQL objects since they exist entirely outside of any specific database; they are called _global objects_. The names of such objects are enforced to be unique within the whole database cluster.

For more information, see [Section 22.1](https://www.postgresql.org/docs/current/manage-ag-overview.html "22.1. Overview").

SQL standard

A series of documents that define the SQL language.

Standby (server)

See [Replica (server)](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA).

Startup process

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that replays WAL during crash recovery and in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION)[physical replica](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICATION "Replication").

(The name is historical: the startup process was named before replication was implemented; the name refers to its task as it relates to the server startup following a crash.)

Superuser

As used in this documentation, it is a synonym for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE-SUPERUSER)[database superuser](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE-SUPERUSER "Database superuser").

System catalog

A collection of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") which describe the structure of all [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT)[SQL objects](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT "SQL object") of the instance. The system catalog resides in the schema `pg_catalog`. These tables contain data in internal representation and are not typically considered useful for user examination; a number of user-friendlier [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW)[views](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-VIEW "View"), also in schema `pg_catalog`, offer more convenient access to some of that information, while additional tables and views exist in schema `information_schema` (see [Chapter 35](https://www.postgresql.org/docs/current/information-schema.html "Chapter 35. The Information Schema")) that expose some of the same and additional information as mandated by the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-STANDARD)[SQL standard](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-STANDARD "SQL standard").

For more information, see [Section 5.10](https://www.postgresql.org/docs/current/ddl-schemas.html "5.10. Schemas").

Table

A collection of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[tuples](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") having a common data structure (the same number of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute"), in the same order, having the same name and type per position). A table is the most common form of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") in PostgreSQL.

For more information, see [CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html "CREATE TABLE").

Tablespace

A named location on the server file system. All [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT)[SQL objects](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SQL-OBJECT "SQL object") which require storage beyond their definition in the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SYSTEM-CATALOG)[system catalog](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SYSTEM-CATALOG "System catalog") must belong to a single tablespace. Initially, a database cluster contains a single usable tablespace which is used as the default for all SQL objects, called `pg_default`.

For more information, see [Section 22.6](https://www.postgresql.org/docs/current/manage-ag-tablespaces.html "22.6. Tablespaces").

Temporary table

[](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[Tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") that exist either for the lifetime of a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION)[session](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION "Session") or a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction"), as specified at the time of creation. The data in them is not visible to other sessions, and is not [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGED)[logged](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGGED "Logged"). Temporary tables are often used to store intermediate data for a multi-step operation.

For more information, see [CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html "CREATE TABLE").

TOAST

A mechanism by which large attributes of table rows are split and stored in a secondary table, called the _TOAST table_. Each relation with large attributes has its own TOAST table.

For more information, see [Section 66.2](https://www.postgresql.org/docs/current/storage-toast.html "66.2. TOAST").

Transaction

A combination of commands that must act as a single [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMIC)[atomic](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATOMIC "Atomic") command: they all succeed or all fail as a single unit, and their effects are not visible to other [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION)[sessions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SESSION "Session") until the transaction is complete, and possibly even later, depending on the isolation level.

For more information, see [Section 13.2](https://www.postgresql.org/docs/current/transaction-iso.html "13.2. Transaction Isolation").

Transaction ID

The numerical, unique, sequentially-assigned identifier that each transaction receives when it first causes a database modification. Frequently abbreviated as _xid_. When stored on disk, xids are only 32-bits wide, so only approximately four billion write transaction IDs can be generated; to permit the system to run for longer than that, _epochs_ are used, also 32 bits wide. When the counter reaches the maximum xid value, it starts over at `3` (values under that are reserved) and the epoch value is incremented by one. In some contexts, the epoch and xid values are considered together as a single 64-bit value; see [Section 67.1](https://www.postgresql.org/docs/current/transaction-id.html "67.1. Transactions and Identifiers") for more details.

For more information, see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types").

Transactions per second (TPS)

Average number of transactions that are executed per second, totaled across all sessions active for a measured run. This is used as a measure of the performance characteristics of an instance.

Trigger

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[function](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") which can be defined to execute whenever a certain operation (`INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`) is applied to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation"). A trigger executes within the same [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION)[transaction](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TRANSACTION "Transaction") as the statement which invoked it, and if the function fails, then the invoking statement also fails.

For more information, see [CREATE TRIGGER](https://www.postgresql.org/docs/current/sql-createtrigger.html "CREATE TRIGGER").

Tuple

A collection of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE)[attributes](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ATTRIBUTE "Attribute") in a fixed order. That order may be defined by the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table") (or other [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation")) where the tuple is contained, in which case the tuple is often called a _row_. It may also be defined by the structure of a result set, in which case it is sometimes called a _record_.

Unique constraint

A type of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT)[constraint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CONSTRAINT "Constraint") defined on a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") which restricts the values allowed in one or a combination of columns so that each value or combination of values can only appear once in the relation — that is, no other row in the relation contains values that are equal to those.

Because [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-NULL)[null values](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-NULL "Null") are not considered equal to each other, multiple rows with null values are allowed to exist without violating the unique constraint.

Unlogged

The property of certain [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relations](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that the changes to them are not reflected in the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log"). This disables replication and crash recovery for these relations.

The primary use of unlogged tables is for storing transient work data that must be shared across processes.

[](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TEMPORARY-TABLE)[Temporary tables](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TEMPORARY-TABLE "Temporary table") are always unlogged.

Update

An SQL command used to modify [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") that may already exist in a specified [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE)[table](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TABLE "Table"). It cannot create or remove rows.

For more information, see [UPDATE](https://www.postgresql.org/docs/current/sql-update.html "UPDATE").

User

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE)[role](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-ROLE "Role") that has the _login privilege_ (see [Section 21.2](https://www.postgresql.org/docs/current/role-attributes.html "21.2. Role Attributes")).

User mapping

The translation of login credentials in the local [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE)[database](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DATABASE "Database") to credentials in a remote data system defined by a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER)[foreign data wrapper](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FOREIGN-DATA-WRAPPER "Foreign data wrapper").

For more information, see [CREATE USER MAPPING](https://www.postgresql.org/docs/current/sql-createusermapping.html "CREATE USER MAPPING").

UTC

Universal Coordinated Time, the primary global time reference, approximately the time prevailing at the zero meridian of longitude. Often but inaccurately referred to as GMT (Greenwich Mean Time).

Vacuum

The process of removing outdated [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[tuple versions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") from tables or materialized views, and other closely related processing required by PostgreSQL's implementation of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MVCC)[MVCC](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-MVCC "Multi-version concurrency control (MVCC)"). This can be initiated through the use of the `VACUUM` command, but can also be handled automatically via [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUTOVACUUM)[autovacuum](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUTOVACUUM "Autovacuum (process)") processes.

For more information, see [Section 24.1](https://www.postgresql.org/docs/current/routine-vacuuming.html "24.1. Routine Vacuuming") .

View

A [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION)[relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION "Relation") that is defined by a `SELECT` statement, but has no storage of its own. Any time a query references a view, the definition of the view is substituted into the query as if the user had typed it as a subquery instead of the name of the view.

For more information, see [CREATE VIEW](https://www.postgresql.org/docs/current/sql-createview.html "CREATE VIEW").

Visibility map (fork)

A storage structure that keeps metadata about each data page of a table's main fork. The visibility map entry for each page stores two bits: the first one (`all-visible`) indicates that all tuples in the page are visible to all transactions. The second one (`all-frozen`) indicates that all tuples in the page are marked frozen.

WAL

See [Write-ahead log](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL).

WAL archiver (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") which, if enabled, saves copies of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE)[WAL files](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE "WAL file") for the purpose of creating backups or keeping [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA)[replicas](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA "Replica (server)") current.

For more information, see [Section 25.3](https://www.postgresql.org/docs/current/continuous-archiving.html "25.3. Continuous Archiving and Point-in-Time Recovery (PITR)").

WAL file

Also known as _WAL segment_ or _WAL segment file_. Each of the sequentially-numbered files that provide storage space for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL)[WAL](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL "Write-ahead log"). The files are all of the same predefined size and are written in sequential order, interspersing changes as they occur in multiple simultaneous sessions. If the system crashes, the files are read in order, and each of the changes is replayed to restore the system to the state it was in before the crash.

Each WAL file can be released after a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT)[checkpoint](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CHECKPOINT "Checkpoint") writes all the changes in it to the corresponding data files. Releasing the file can be done either by deleting it, or by changing its name so that it will be used in the future, which is called _recycling_.

For more information, see [Section 28.6](https://www.postgresql.org/docs/current/wal-internals.html "28.6. WAL Internals").

WAL record

A low-level description of an individual data change. It contains sufficient information for the data change to be re-executed (_replayed_) in case a system failure causes the change to be lost. WAL records use a non-printable binary format.

For more information, see [Section 28.6](https://www.postgresql.org/docs/current/wal-internals.html "28.6. WAL Internals").

WAL receiver (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that runs on a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA)[replica](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA "Replica (server)") to receive WAL from the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER)[primary server](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PRIMARY-SERVER "Primary (server)") for replay by the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-STARTUP-PROCESS)[startup process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-STARTUP-PROCESS "Startup process").

For more information, see [Section 26.2](https://www.postgresql.org/docs/current/warm-standby.html "26.2. Log-Shipping Standby Servers").

WAL segment

See [WAL file](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE).

WAL sender (process)

A special [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND)[backend process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)") that streams WAL over a network. The receiving end can be a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECEIVER)[WAL receiver](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECEIVER "WAL receiver (process)") in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA)[replica](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-REPLICA "Replica (server)"), [pg\_receivewal](https://www.postgresql.org/docs/current/app-pgreceivewal.html "pg_receivewal"), or any other client program that speaks the replication protocol.

WAL summarizer (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that summarizes WAL data for [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INCREMENTAL-BACKUP)[incremental backups](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INCREMENTAL-BACKUP "Incremental backup").

For more information, see [Section 19.5.7](https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-SUMMARIZATION "19.5.7. WAL Summarization").

WAL writer (process)

An [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC)[auxiliary process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AUXILIARY-PROC "Auxiliary process") that writes [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD)[WAL records](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD "WAL record") from [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY)[shared memory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") to [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE)[WAL files](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE "WAL file").

For more information, see [Section 19.5](https://www.postgresql.org/docs/current/runtime-config-wal.html "19.5. Write Ahead Log").

Window function (routine)

A type of [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION)[function](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-FUNCTION "Function (routine)") used in a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY)[query](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-QUERY "Query") that applies to a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITION)[partition](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-PARTITION "Partition") of the query's [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET)[result set](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RESULT-SET "Result set"); the function's result is based on values found in [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE)[rows](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-TUPLE "Tuple") of the same partition or frame.

All [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AGGREGATE)[aggregate functions](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AGGREGATE "Aggregate function (routine)") can be used as window functions, but window functions can also be used to, for example, give ranks to each of the rows in the partition. Also known as _analytic functions_.

For more information, see [Section 3.5](https://www.postgresql.org/docs/current/tutorial-window.html "3.5. Window Functions").

Write-ahead log

The journal that keeps track of the changes in the [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER)[database cluster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DB-CLUSTER "Database cluster") as user- and system-invoked operations take place. It comprises many individual [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD)[WAL records](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-RECORD "WAL record") written sequentially to [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE)[WAL files](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-WAL-FILE "WAL file").
