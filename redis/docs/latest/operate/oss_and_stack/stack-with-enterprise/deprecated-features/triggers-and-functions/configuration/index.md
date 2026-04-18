---
title: "Configuration"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/configuration/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/configuration/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:07.273Z"
content_hash: "795e6a863dde794ed3ee5ed98e9a3c8765355a00669f6de86503ede1393022f6"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Configuration","→","Configuration"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Configuration","→","Configuration"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/timeseries/configuration/index.md", "title": "Configuration Parameters"}
nav_next: {"path": "redis/docs/latest/develop/reference/key-specs/index.md", "title": "Command key specifications"}
---

# Configuration

Configure the operation parameters

Redis Open Source

Redis Software

Redis Cloud

Redis Open Source

Redis Enterprise for Kubernetes

clients

Redis Stack's triggers and functions feature provides configuration options to control its operation. These options can be set when the module is bootstrapped and, in some cases, at runtime.

The following sections describe the configuration options and how to set them.

## Bootstrap configuration

You can set your configuration options when the module is loaded. When the module is loaded at start time, the module configuration can be defined in the Redis configuration file. When loading the module at runtime the configuration can be given to the [`MODULE LOADEX`](/docs/latest/commands/module-loadex/) command. Each configuration must be prefixed with the module name, `redisgears_2.<configuration name>`.

## Runtime configuration

You may set certain configuration options at runtime. Setting a configuration at runtime is done using [`CONFIG SET`](/docs/latest/commands/config-set/) command. Here each configuration must be prefixed with the module name, `redisgears_2.<configuration name>`.

Example:

```bash
> config set redisgears_2.lock-redis-timeout 1000
OK
```

## Configurations

### execution-threads

The `execution-threads` configuration option controls the number of background threads that run JS code. **Note that libraries are considered single threaded**. This configuration allows Redis to parallelize the invocation of multiple libraries.

_Expected Value_

Integer

_Default_

1

_Minimum Value_

1

_Maximum Value_

32

_Runtime Configurability_

No

### library-fatal-failure-policy

The `library-fatal-failure-policy` configuration option controls how to handle a fatal error. A fatal error is consider one of the following:

*   Block timeout - The function blocks the Redis processes for too long (configurable using the [lock-redis-timeout](#lock-redis-timeout) configuration value)
*   OOM - The function consumes too much memory (configurable using the [v8-maxmemory](#v8-maxmemory) configuration value).

This configuration basically allows choosing between two options:

*   Do not break atomicity property, even at the cost of killing the Redis processes.
*   Keep my Redis processes alive, even at the cost of losing atomicity.

_Expected Value_

*   kill - Save the atomicity property. Risk of killing the Redis processes.
*   abort - Abort the invocation of the function and keep the Redis processes alive. Risk of losing the atomicity property.

_Default_

abort

_Runtime Configurability_

Yes

### v8-maxmemory

The `v8-maxmemory` configuration option controls the maximum amount of memory used by all V8 libraries. Exceeding this limit is considered a fatal error and will be handled base on the [library-fatal-failure-policy](#library-fatal-failure-policy) configuration value.

_Expected Value_

Integer

_Default_

200M

_Minimum Value_

50M

_Maximum Value_

1G

_Runtime Configurability_

No

### v8-library-initial-memory-usage

The `v8-library-initial-memory-usage` configuration option controls the initial memory given to a single V8 library. This value can not be greater then [`v8-library-initial-memory-limit`](#v8-library-initial-memory-limit) or [v8-maxmemory](#v8-maxmemory).

_Expected Value_

Integer

_Default_

2M

_Minimum Value_

1M

_Maximum Value_

10M

_Runtime Configurability_

No

### v8-library-initial-memory-limit

The `v8-library-initial-memory-limit` configuration option controls the initial memory limit on a single V8 library. This value can not be greater then [v8-maxmemory](#v8-maxmemory).

_Expected Value_

Integer

_Default_

3M

_Minimum Value_

2M

_Maximum Value_

20M

_Runtime Configurability_

No

### v8-library-memory-usage-delta

The `v8-library-memory-usage-delta` configuration option controls the delta by which we will increase the V8 library memory limit once the limit reached. This value can not be greater then [v8-maxmemory](#v8-maxmemory).

_Expected Value_

Integer

_Default_

1M

_Minimum Value_

1M

_Maximum Value_

10M

_Runtime Configurability_

No

### lock-redis-timeout

The `lock-redis-timeout` configuration option controls the maximum amount of time (in MS) a library can lock Redis. Exceeding this limit is considered a fatal error and will be handled based on the [library-fatal-failure-policy](#library-fatal-failure-policy) configuration value. This configuration only affects library loading at runtime with `TFUNCTION LOAD`. The timeout for loading a library from RDB is set separately via [db-loading-lock-redis-timeout](#db-loading-lock-redis-timeout).

_Expected Value_

Integer

_Default_

500 MS

_Minimum Value_

100 MS

_Maximum Value_

Unlimited

_Runtime Configurability_

Yes

#### Side effects

When setting `lock-redis-timeout`, if the new value is higher than the `db-loading-lock-redis-timeout`, the `db-loading-lock-redis-timeout` is also updated to this value.

### db-loading-lock-redis-timeout

This timeout configuration is used for setting the upper time limit (in milliseconds) for the library loading from RDB.

_Expected Value_

Integer

_Default_

30000 MS

_Minimum Value_

100 MS

_Maximum Value_

Unlimited

_Runtime Configurability_

Yes

#### Notes

The value cannot be lower than the value of `lock-redis-timeout`.

### remote-task-default-timeout

The `remote-task-default-timeout` configuration option controls the timeout when waiting for a remote task to finish. If the timeout is reached an error will result.

_Expected Value_

Integer

_Default_

500 MS

_Minimum Value_

1 MS

_Maximum Value_

Unlimited

_Runtime Configurability_

Yes

### error-verbosity

The `error-verbosity` configuration option controls the verbosity of error messages that will be provided by triggers and functions. The higher the value the more verbose the error messages will be (for example, including stack traces and extra information for better analysis and debugging).

_Expected Value_

Integer

_Default_

1

_Minimum Value_

1

_Maximum Value_

2

_Runtime Configurability_

Yes

## On this page
