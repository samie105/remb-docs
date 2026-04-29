---
title: "Redis command tips"
source: "https://redis.io/docs/latest/develop/reference/command-tips/"
canonical_url: "https://redis.io/docs/latest/develop/reference/command-tips/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:12.183Z"
content_hash: "4b6264818ed38f0781d0500b67e6ede5a0b70ef31146aefd15e98487523cf00f"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis reference","→","Redis reference","→\n      \n        Redis command tips","→","Redis command tips"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis reference","→","Redis reference","→\n      \n        Redis command tips","→","Redis command tips"]
nav_prev: {"path": "../command-arguments/index.md", "title": "Redis command arguments"}
nav_next: {"path": "../eviction/index.md", "title": "Key eviction"}
---

# Redis command tips

Get additional information about a command

Command tips are an array of strings. These provide Redis clients with additional information about the command. The information can instruct Redis Cluster clients as to how the command should be executed and its output processed in a clustered deployment.

Unlike the command's flags (see the 3rd element of [`COMMAND`](/docs/latest/commands/command/)'s reply), which are strictly internal to the server's operation, tips don't serve any purpose other than being reported to clients.

Command tips are arbitrary strings. However, the following sections describe proposed tips and demonstrate the conventions they are likely to adhere to.

## nondeterministic\_output

This tip indicates that the command's output isn't deterministic. That means that calls to the command may yield different results with the same arguments and data. That difference could be the result of the command's random nature (e.g., [`RANDOMKEY`](/docs/latest/commands/randomkey/) and [`SPOP`](/docs/latest/commands/spop/)); the call's timing (e.g., [`TTL`](/docs/latest/commands/ttl/)); or generic differences that relate to the server's state (e.g., [`INFO`](/docs/latest/commands/info/) and [`CLIENT LIST`](/docs/latest/commands/client-list/)).

**Note:** Prior to Redis 7.0, this tip was the _random_ command flag.

## nondeterministic\_output\_order

The existence of this tip indicates that the command's output is deterministic, but its ordering is random (e.g., [`HGETALL`](/docs/latest/commands/hgetall/) and [`SMEMBERS`](/docs/latest/commands/smembers/)).

**Note:** Prior to Redis 7.0, this tip was the _sort_\__for_\__script_ flag.

## request\_policy

This tip can help clients determine the shards to send the command in clustering mode. The default behavior a client should implement for commands without the _request\_policy_ tip is as follows:

1.  The command doesn't accept key name arguments: the client can execute the command on an arbitrary shard.
2.  For commands that accept one or more key name arguments: the client should route the command to a single shard, as determined by the hash slot of the input keys.

In cases where the client should adopt a behavior different than the default, the _request\_policy_ tip can be one of:

*   **all\_nodes:** the client should execute the command on all nodes - masters and replicas alike. An example is the [`CONFIG SET`](/docs/latest/commands/config-set/) command. This tip is in-use by commands that don't accept key name arguments. The command operates atomically per shard.

*   **all\_shards:** the client should execute the command on all master shards (e.g., the [`DBSIZE`](/docs/latest/commands/dbsize/) command). This tip is in-use by commands that don't accept key name arguments. The command operates atomically per shard.

*   **multi\_shard:** the client should execute the command on several shards. The client should split the inputs according to the hash slots of its input key name arguments. For example, the command `DEL {foo} {foo}1 bar` should be split to `DEL {foo} {foo}1` and `DEL bar`. If the keys are hashed to more than a single slot, the command must be split even if all the slots are managed by the same shard. Examples for such commands include [`MSET`](/docs/latest/commands/mset/), [`MGET`](/docs/latest/commands/mget/) and [`DEL`](/docs/latest/commands/del/). However, note that [`SUNIONSTORE`](/docs/latest/commands/sunionstore/) isn't considered as _multi\_shard_ because all of its keys must belong to the same hash slot.
*   **special:** indicates a non-trivial form of the client's request policy, such as the [`SCAN`](/docs/latest/commands/scan/) command.

## response\_policy

This tip can help clients determine the aggregate they need to compute from the replies of multiple shards in a cluster. The default behavior for commands without a _request\_policy_ tip only applies to replies with of nested types (i.e., an array, a set, or a map). The client's implementation for the default behavior should be as follows:

1.  The command doesn't accept key name arguments: the client can aggregate all replies within a single nested data structure. For example, the array replies we get from calling [`KEYS`](/docs/latest/commands/keys/) against all shards. These should be packed in a single in no particular order.
2.  For commands that accept one or more key name arguments: the client needs to retain the same order of replies as the input key names. For example, [`MGET`](/docs/latest/commands/mget/)'s aggregated reply.

The _response\_policy_ tip is set for commands that reply with scalar data types, or when it's expected that clients implement a non-default aggregate. This tip can be one of:

*   **one\_succeeded:** the clients should return success if at least one shard didn't reply with an error. The client should reply with the first non-error reply it obtains. If all shards return an error, the client can reply with any one of these. For example, consider a [`SCRIPT KILL`](/docs/latest/commands/script-kill/) command that's sent to all shards. Although the script should be loaded in all of the cluster's shards, the [`SCRIPT KILL`](/docs/latest/commands/script-kill/) will typically run only on one at a given time.
*   **all\_succeeded:** the client should return successfully only if there are no error replies. Even a single error reply should disqualify the aggregate and be returned. Otherwise, the client should return one of the non-error replies. As an example, consider the [`CONFIG SET`](/docs/latest/commands/config-set/), [`SCRIPT FLUSH`](/docs/latest/commands/script-flush/) and [`SCRIPT LOAD`](/docs/latest/commands/script-load/) commands.
*   **agg\_logical\_and:** the client should return the result of a logical _AND_ operation on all replies (only applies to integer replies, usually from commands that return either _0_ or _1_). Consider the [`SCRIPT EXISTS`](/docs/latest/commands/script-exists/) command as an example. It returns an array of _0_'s and _1_'s that denote the existence of its given SHA1 sums in the script cache. The aggregated response should be _1_ only when all shards had reported that a given script SHA1 sum is in their respective cache.
*   **agg\_logical\_or:** the client should return the result of a logical _OR_ operation on all replies (only applies to integer replies, usually from commands that return either _0_ or _1_).
*   **agg\_min:** the client should return the minimal value from the replies (only applies to numerical replies). The aggregate reply from a cluster-wide [`WAIT`](/docs/latest/commands/wait/) command, for example, should be the minimal value (number of synchronized replicas) from all shards.
*   **agg\_max:** the client should return the maximal value from the replies (only applies to numerical replies).
*   **agg\_sum:** the client should return the sum of replies (only applies to numerical replies). Example: [`DBSIZE`](/docs/latest/commands/dbsize/).
*   **special:** this type of tip indicates a non-trivial form of reply policy. [`INFO`](/docs/latest/commands/info/) is an excellent example of that.

## Example

```
redis> command info ping
1)  1) "ping"
    2) (integer) -1
    3) 1) fast
    4) (integer) 0
    5) (integer) 0
    6) (integer) 0
    7) 1) @fast
       2) @connection
    8) 1) "request_policy:all_shards"
       2) "response_policy:all_succeeded"
    9) (empty array)
   10) (empty array)
```

## On this page
