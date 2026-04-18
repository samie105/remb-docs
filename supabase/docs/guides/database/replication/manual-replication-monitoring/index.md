---
title: "Manual Replication Monitoring"
source: "https://supabase.com/docs/guides/database/replication/manual-replication-monitoring"
canonical_url: "https://supabase.com/docs/guides/database/replication/manual-replication-monitoring"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:55.041Z"
content_hash: "116f776ff54f4cb93812257217f21810ebfe7af0ec17f6e995ddffa5b7c19897"
menu_path: ["Database","Database","More","More","More","Manual replication","Manual replication","Monitoring","Monitoring"]
section_path: ["Database","Database","More","More","More","Manual replication","Manual replication","Monitoring","Monitoring"]
---
# 

Manual Replication Monitoring

## 

Track replication health and performance.

* * *

Monitoring replication lag is important and there are 3 ways to do this:

1.  Dashboard - Under the [Reports](/docs/guides/telemetry/reports) of the dashboard, you can view the replication lag of your project
2.  Database -
    *   pg\_stat\_subscription (subscriber) - if PID is null, then the subscription is not active
    *   pg\_stat\_subscription\_stats - look here for error\_count to see if there were issues applying or syncing (if yes, check the logs for why)
    *   pg\_replication\_slots - use this to check if the slot is active and you can also calculate the lag from here
3.  [Metrics](/docs/guides/telemetry/metrics) - Using the prometheus endpoint for your project
    *   replication\_slots\_max\_lag\_bytes - this is the more important one
    *   pg\_stat\_replication\_replay\_lag - lag to replay WAL files from the source DB on the target DB (throttled by disk or high activity)
    *   pg\_stat\_replication\_send\_lag - lag in sending WAL files from the source DB (a high lag means that the publisher is not being asked to send new WAL files OR network issues)

### Primary[#](#primary)

#### Replication status and lag[#](#replication-status-and-lag)

The `pg_stat_replication` table shows the status of any replicas connected to the primary database.

```
1select pid, application_name, state, sent_lsn, write_lsn, flush_lsn, replay_lsn, sync_state2from pg_stat_replication;
```

#### Replication slot status[#](#replication-slot-status)

A replication slot can be in one of three states:

*   `active` - The slot is active and is receiving data
*   `inactive` - The slot is not active and is not receiving data
*   `lost` - The slot is lost and is not receiving data

The state can be checked using the `pg_replication_slots` table:

```
1select slot_name, active, state from pg_replication_slots;
```

#### WAL size[#](#wal-size)

The WAL size can be checked using the `pg_ls_waldir()` function:

```
1select * from pg_ls_waldir();
```

#### Check the LSN[#](#check-the-lsn)

```
1select pg_current_wal_lsn();
```

### Subscriber[#](#subscriber)

#### Subscription status[#](#subscription-status)

The `pg_subscription` table shows the status of any subscriptions on a replica and the `pg_subscription_rel` table shows the status of each table within a subscription.

The `srsubstate` column in `pg_subscription_rel` can be one of the following:

*   `i` - Initializing - The subscription is being initialized
*   `d` - Data Synchronizing - The subscription is synchronizing data for the first time (i.e. doing the initial copy)
*   `s` - Synchronized - The subscription is synchronized
*   `r` - Replicating - The subscription is replicating data

```
1SELECT2    sub.subname AS subscription_name,3    relid::regclass AS table_name,4    srel.srsubstate AS replication_state,5    CASE srel.srsubstate6        WHEN 'i' THEN 'Initializing'7        WHEN 'd' THEN 'Data Synchronizing'8        WHEN 's' THEN 'Synchronized'9        WHEN 'r' THEN 'Replicating'10        ELSE 'Unknown'11    END AS state_description,12    srel.srsyncedlsn AS last_synced_lsn13FROM14    pg_subscription sub15JOIN16    pg_subscription_rel srel ON sub.oid = srel.srsubid17ORDER BY18    table_name;
```

#### Check the LSN[#](#check-the-lsn)

```
1select pg_last_wal_replay_lsn();
```
