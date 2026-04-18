---
title: "PostgreSQL: Documentation: 18: 29.13. Upgrade"
source: "https://www.postgresql.org/docs/current/logical-replication-upgrade.html"
canonical_url: "https://www.postgresql.org/docs/current/logical-replication-upgrade.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:54.061Z"
content_hash: "87774f66f4f2ac390311b667b186d28c44398fa60b93295157fb1d621d1ca89c"
menu_path: ["PostgreSQL: Documentation: 18: 29.13. Upgrade"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-file-settings.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.8.\u00a0pg_file_settings"}
nav_next: {"path": "postgres/docs/current/sql-createtableas.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TABLE AS"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/logical-replication-upgrade.html "PostgreSQL devel - 29.13. Upgrade")

Migration of [](postgres/docs/current/glossary.html/index.md#GLOSSARY-LOGICAL-REPLICATION-CLUSTER)[logical replication clusters](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-LOGICAL-REPLICATION-CLUSTER "Logical replication cluster") is possible only when all the members of the old logical replication clusters are version 17.0 or later.

### 29.13.1. Prepare for Publisher Upgrades [#](#PREPARE-PUBLISHER-UPGRADES)

pg\_upgrade attempts to migrate logical slots. This helps avoid the need for manually defining the same logical slots on the new publisher. Migration of logical slots is only supported when the old cluster is version 17.0 or later. Logical slots on clusters before version 17.0 will silently be ignored.

Before you start upgrading the publisher cluster, ensure that the subscription is temporarily disabled, by executing [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html "ALTER SUBSCRIPTION"). Re-enable the subscription after the upgrade.

There are some prerequisites for pg\_upgrade to be able to upgrade the logical slots. If these are not met an error will be reported.

*   The new cluster must have [`wal_level`](postgres/docs/current/runtime-config-wal.html/index.md#GUC-WAL-LEVEL) as `logical`.
    
*   The new cluster must have [`max_replication_slots`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-MAX-REPLICATION-SLOTS) configured to a value greater than or equal to the number of slots present in the old cluster.
    
*   The output plugins referenced by the slots on the old cluster must be installed in the new PostgreSQL executable directory.
    
*   The old cluster has replicated all the transactions and logical decoding messages to subscribers.
    
*   All slots on the old cluster must be usable, i.e., there are no slots whose [pg\_replication\_slots](https://www.postgresql.org/docs/current/view-pg-replication-slots.html "53.20. pg_replication_slots").`conflicting` is not `true`.
    
*   The new cluster must not have permanent logical slots, i.e., there must be no slots where [pg\_replication\_slots](https://www.postgresql.org/docs/current/view-pg-replication-slots.html "53.20. pg_replication_slots").`temporary` is `false`.
    

### 29.13.2. Prepare for Subscriber Upgrades [#](#PREPARE-SUBSCRIBER-UPGRADES)

Setup the [subscriber configurations](https://www.postgresql.org/docs/current/logical-replication-config.html#LOGICAL-REPLICATION-CONFIG-SUBSCRIBER "29.12.2. Subscribers") in the new subscriber. pg\_upgrade attempts to migrate subscription dependencies which includes the subscription's table information present in [pg\_subscription\_rel](https://www.postgresql.org/docs/current/catalog-pg-subscription-rel.html "52.55. pg_subscription_rel") system catalog and also the subscription's replication origin. This allows logical replication on the new subscriber to continue from where the old subscriber was up to. Migration of subscription dependencies is only supported when the old cluster is version 17.0 or later. Subscription dependencies on clusters before version 17.0 will silently be ignored.

There are some prerequisites for pg\_upgrade to be able to upgrade the subscriptions. If these are not met an error will be reported.

*   All the subscription tables in the old subscriber should be in state `i` (initialize) or `r` (ready). This can be verified by checking [pg\_subscription\_rel](https://www.postgresql.org/docs/current/catalog-pg-subscription-rel.html "52.55. pg_subscription_rel").`srsubstate`.
    
*   The replication origin entry corresponding to each of the subscriptions should exist in the old cluster. This can be found by checking [pg\_subscription](https://www.postgresql.org/docs/current/catalog-pg-subscription.html "52.54. pg_subscription") and [pg\_replication\_origin](https://www.postgresql.org/docs/current/catalog-pg-replication-origin.html "52.44. pg_replication_origin") system tables.
    
*   The new cluster must have [`max_active_replication_origins`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-MAX-ACTIVE-REPLICATION-ORIGINS) configured to a value greater than or equal to the number of subscriptions present in the old cluster.
    

### 29.13.3. Upgrading Logical Replication Clusters [#](#UPGRADING-LOGICAL-REPLICATION-CLUSTERS)

While upgrading a subscriber, write operations can be performed in the publisher. These changes will be replicated to the subscriber once the subscriber upgrade is completed.

### Note

The logical replication restrictions apply to logical replication cluster upgrades also. See [Section 29.8](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "29.8. Restrictions") for details.

The prerequisites of publisher upgrade apply to logical replication cluster upgrades also. See [Section 29.13.1](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#PREPARE-PUBLISHER-UPGRADES "29.13.1. Prepare for Publisher Upgrades") for details.

The prerequisites of subscriber upgrade apply to logical replication cluster upgrades also. See [Section 29.13.2](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#PREPARE-SUBSCRIBER-UPGRADES "29.13.2. Prepare for Subscriber Upgrades") for details.

### Warning

Upgrading logical replication cluster requires multiple steps to be performed on various nodes. Because not all operations are transactional, the user is advised to take backups as described in [Section 25.3.2](https://www.postgresql.org/docs/current/continuous-archiving.html#BACKUP-BASE-BACKUP "25.3.2. Making a Base Backup").

The steps to upgrade the following logical replication clusters are detailed below:

*   Follow the steps specified in [Section 29.13.3.1](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#STEPS-TWO-NODE-LOGICAL-REPLICATION-CLUSTER "29.13.3.1. Steps to Upgrade a Two-node Logical Replication Cluster") to upgrade a two-node logical replication cluster.
    
*   Follow the steps specified in [Section 29.13.3.2](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#STEPS-CASCADED-LOGICAL-REPLICATION-CLUSTER "29.13.3.2. Steps to Upgrade a Cascaded Logical Replication Cluster") to upgrade a cascaded logical replication cluster.
    
*   Follow the steps specified in [Section 29.13.3.3](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#STEPS-TWO-NODE-CIRCULAR-LOGICAL-REPLICATION-CLUSTER "29.13.3.3. Steps to Upgrade a Two-node Circular Logical Replication Cluster") to upgrade a two-node circular logical replication cluster.
    

#### 29.13.3.1. Steps to Upgrade a Two-node Logical Replication Cluster [#](#STEPS-TWO-NODE-LOGICAL-REPLICATION-CLUSTER)

Let's say publisher is in `node1` and subscriber is in `node2`. The subscriber `node2` has a subscription `sub1_node1_node2` which is subscribing the changes from `node1`.

1.  Disable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-DISABLE), e.g.:
    
    /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 DISABLE;
    
2.  Stop the publisher server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1 stop
    
3.  Initialize `data1_upgraded` instance by using the required newer version.
    
4.  Upgrade the publisher `node1`'s server to the required newer version, e.g.:
    
    pg\_upgrade
            --old-datadir "/opt/PostgreSQL/postgres/17/data1"
            --new-datadir "/opt/PostgreSQL/postgres/18/data1\_upgraded"
            --old-bindir "/opt/PostgreSQL/postgres/17/bin"
            --new-bindir "/opt/PostgreSQL/postgres/18/bin"
    
5.  Start the upgraded publisher server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1\_upgraded start -l logfile
    
6.  Stop the subscriber server in `node2`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data2 stop
    
7.  Initialize `data2_upgraded` instance by using the required newer version.
    
8.  Upgrade the subscriber `node2`'s server to the required new version, e.g.:
    
    pg\_upgrade
           --old-datadir "/opt/PostgreSQL/postgres/17/data2"
           --new-datadir "/opt/PostgreSQL/postgres/18/data2\_upgraded"
           --old-bindir "/opt/PostgreSQL/postgres/17/bin"
           --new-bindir "/opt/PostgreSQL/postgres/18/bin"
    
9.  Start the upgraded subscriber server in `node2`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data2\_upgraded start -l logfile
    
10.  On `node2`, create any tables that were created in the upgraded publisher `node1` server between [Step 1](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#TWO-NODE-CLUSTER-DISABLE-SUBSCRIPTIONS-NODE2 "Step 1") and now, e.g.:
     
     /\* node2 # \*/ CREATE TABLE distributors (did integer PRIMARY KEY, name varchar(40));
     
11.  Enable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... ENABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-ENABLE), e.g.:
     
     /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 ENABLE;
     
12.  Refresh the `node2` subscription's publications using [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-REFRESH-PUBLICATION), e.g.:
     
     /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 REFRESH PUBLICATION;
     

### Note

In the steps described above, the publisher is upgraded first, followed by the subscriber. Alternatively, the user can use similar steps to upgrade the subscriber first, followed by the publisher.

#### 29.13.3.2. Steps to Upgrade a Cascaded Logical Replication Cluster [#](#STEPS-CASCADED-LOGICAL-REPLICATION-CLUSTER)

Let's say we have a cascaded logical replication setup `node1`\->`node2`\->`node3`. Here `node2` is subscribing the changes from `node1` and `node3` is subscribing the changes from `node2`. The `node2` has a subscription `sub1_node1_node2` which is subscribing the changes from `node1`. The `node3` has a subscription `sub1_node2_node3` which is subscribing the changes from `node2`.

1.  Disable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-DISABLE), e.g.:
    
    /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 DISABLE;
    
2.  Stop the server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1 stop
    
3.  Initialize `data1_upgraded` instance by using the required newer version.
    
4.  Upgrade the `node1`'s server to the required newer version, e.g.:
    
    pg\_upgrade
            --old-datadir "/opt/PostgreSQL/postgres/17/data1"
            --new-datadir "/opt/PostgreSQL/postgres/18/data1\_upgraded"
            --old-bindir "/opt/PostgreSQL/postgres/17/bin"
            --new-bindir "/opt/PostgreSQL/postgres/18/bin"
    
5.  Start the upgraded server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1\_upgraded start -l logfile
    
6.  Disable all the subscriptions on `node3` that are subscribing the changes from `node2` by using [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-DISABLE), e.g.:
    
    /\* node3 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node3 DISABLE;
    
7.  Stop the server in `node2`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data2 stop
    
8.  Initialize `data2_upgraded` instance by using the required newer version.
    
9.  Upgrade the `node2`'s server to the required new version, e.g.:
    
    pg\_upgrade
            --old-datadir "/opt/PostgreSQL/postgres/17/data2"
            --new-datadir "/opt/PostgreSQL/postgres/18/data2\_upgraded"
            --old-bindir "/opt/PostgreSQL/postgres/17/bin"
            --new-bindir "/opt/PostgreSQL/postgres/18/bin"
    
10.  Start the upgraded server in `node2`, e.g.:
     
     pg\_ctl -D /opt/PostgreSQL/data2\_upgraded start -l logfile
     
11.  On `node2`, create any tables that were created in the upgraded publisher `node1` server between [Step 1](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#CASCADED-CLUSTER-DISABLE-SUB-NODE1-NODE2 "Step 1") and now, e.g.:
     
     /\* node2 # \*/ CREATE TABLE distributors (did integer PRIMARY KEY, name varchar(40));
     
12.  Enable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... ENABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-ENABLE), e.g.:
     
     /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 ENABLE;
     
13.  Refresh the `node2` subscription's publications using [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-REFRESH-PUBLICATION), e.g.:
     
     /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 REFRESH PUBLICATION;
     
14.  Stop the server in `node3`, e.g.:
     
     pg\_ctl -D /opt/PostgreSQL/data3 stop
     
15.  Initialize `data3_upgraded` instance by using the required newer version.
     
16.  Upgrade the `node3`'s server to the required new version, e.g.:
     
     pg\_upgrade
             --old-datadir "/opt/PostgreSQL/postgres/17/data3"
             --new-datadir "/opt/PostgreSQL/postgres/18/data3\_upgraded"
             --old-bindir "/opt/PostgreSQL/postgres/17/bin"
             --new-bindir "/opt/PostgreSQL/postgres/18/bin"
     
17.  Start the upgraded server in `node3`, e.g.:
     
     pg\_ctl -D /opt/PostgreSQL/data3\_upgraded start -l logfile
     
18.  On `node3`, create any tables that were created in the upgraded `node2` between [Step 6](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#CASCADED-CLUSTER-DISABLE-SUB-NODE2-NODE3 "Step 6") and now, e.g.:
     
     /\* node3 # \*/ CREATE TABLE distributors (did integer PRIMARY KEY, name varchar(40));
     
19.  Enable all the subscriptions on `node3` that are subscribing the changes from `node2` by using [`ALTER SUBSCRIPTION ... ENABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-ENABLE), e.g.:
     
     /\* node3 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node3 ENABLE;
     
20.  Refresh the `node3` subscription's publications using [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-REFRESH-PUBLICATION), e.g.:
     
     /\* node3 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node3 REFRESH PUBLICATION;
     

#### 29.13.3.3. Steps to Upgrade a Two-node Circular Logical Replication Cluster [#](#STEPS-TWO-NODE-CIRCULAR-LOGICAL-REPLICATION-CLUSTER)

Let's say we have a circular logical replication setup `node1`\->`node2` and `node2`\->`node1`. Here `node2` is subscribing the changes from `node1` and `node1` is subscribing the changes from `node2`. The `node1` has a subscription `sub1_node2_node1` which is subscribing the changes from `node2`. The `node2` has a subscription `sub1_node1_node2` which is subscribing the changes from `node1`.

1.  Disable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-DISABLE), e.g.:
    
    /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 DISABLE;
    
2.  Stop the server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1 stop
    
3.  Initialize `data1_upgraded` instance by using the required newer version.
    
4.  Upgrade the `node1`'s server to the required newer version, e.g.:
    
    pg\_upgrade
            --old-datadir "/opt/PostgreSQL/postgres/17/data1"
            --new-datadir "/opt/PostgreSQL/postgres/18/data1\_upgraded"
            --old-bindir "/opt/PostgreSQL/postgres/17/bin"
            --new-bindir "/opt/PostgreSQL/postgres/18/bin"
    
5.  Start the upgraded server in `node1`, e.g.:
    
    pg\_ctl -D /opt/PostgreSQL/data1\_upgraded start -l logfile
    
6.  Enable all the subscriptions on `node2` that are subscribing the changes from `node1` by using [`ALTER SUBSCRIPTION ... ENABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-ENABLE), e.g.:
    
    /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 ENABLE;
    
7.  On `node1`, create any tables that were created in `node2` between [Step 1](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#CIRCULAR-CLUSTER-DISABLE-SUB-NODE2 "Step 1") and now, e.g.:
    
    /\* node1 # \*/ CREATE TABLE distributors (did integer PRIMARY KEY, name varchar(40));
    
8.  Refresh the `node1` subscription's publications to copy initial table data from `node2` using [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-REFRESH-PUBLICATION), e.g.:
    
    /\* node1 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node1 REFRESH PUBLICATION;
    
9.  Disable all the subscriptions on `node1` that are subscribing the changes from `node2` by using [`ALTER SUBSCRIPTION ... DISABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-DISABLE), e.g.:
    
    /\* node1 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node1 DISABLE;
    
10.  Stop the server in `node2`, e.g.:
     
     pg\_ctl -D /opt/PostgreSQL/data2 stop
     
11.  Initialize `data2_upgraded` instance by using the required newer version.
     
12.  Upgrade the `node2`'s server to the required new version, e.g.:
     
     pg\_upgrade
             --old-datadir "/opt/PostgreSQL/postgres/17/data2"
             --new-datadir "/opt/PostgreSQL/postgres/18/data2\_upgraded"
             --old-bindir "/opt/PostgreSQL/postgres/17/bin"
             --new-bindir "/opt/PostgreSQL/postgres/18/bin"
     
13.  Start the upgraded server in `node2`, e.g.:
     
     pg\_ctl -D /opt/PostgreSQL/data2\_upgraded start -l logfile
     
14.  Enable all the subscriptions on `node1` that are subscribing the changes from `node2` by using [`ALTER SUBSCRIPTION ... ENABLE`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-ENABLE), e.g.:
     
     /\* node1 # \*/ ALTER SUBSCRIPTION sub1\_node2\_node1 ENABLE;
     
15.  On `node2`, create any tables that were created in the upgraded `node1` between [Step 9](https://www.postgresql.org/docs/current/logical-replication-upgrade.html#CIRCULAR-CLUSTER-DISABLE-SUB-NODE1 "Step 9") and now, e.g.:
     
     /\* node2 # \*/ CREATE TABLE distributors (did integer PRIMARY KEY, name varchar(40));
     
16.  Refresh the `node2` subscription's publications to copy initial table data from `node1` using [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html#SQL-ALTERSUBSCRIPTION-PARAMS-REFRESH-PUBLICATION), e.g.:
     
     /\* node2 # \*/ ALTER SUBSCRIPTION sub1\_node1\_node2 REFRESH PUBLICATION;
