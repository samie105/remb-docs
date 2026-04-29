---
title: "cluster - Node documentation"
source: "https://docs.deno.com/api/node/cluster/"
canonical_url: "https://docs.deno.com/api/node/cluster/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:04:00.225Z"
content_hash: "3337c5cb14df9e215d9f0b7d84e14e91ad79584d46be6bc5b9782830b8ebd6d8"
menu_path: ["cluster - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../child_process/index.md", "title": "child_process - Node documentation"}
nav_next: {"path": "../console/index.md", "title": "console - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:cluster";
```

Deno compatibility

All exports are non-functional stubs.

Clusters of Node.js processes can be used to run multiple instances of Node.js that can distribute workloads among their application threads. When process isolation is not needed, use the [`worker_threads`](https://nodejs.org/docs/latest-v22.x/api/worker_threads.html) module instead, which allows running multiple application threads within a single Node.js instance.

The cluster module allows easy creation of child processes that all share server ports.

```js
import cluster from 'node:cluster';
import http from 'node:http';
import { availableParallelism } from 'node:os';
import process from 'node:process';

const numCPUs = availableParallelism();

if (cluster.isPrimary) {
  console.log(`Primary ${process.pid} is running`);

  // Fork workers.
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`worker ${worker.process.pid} died`);
  });
} else {
  // Workers can share any TCP connection
  // In this case it is an HTTP server
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('hello world\n');
  }).listen(8000);

  console.log(`Worker ${process.pid} started`);
}
```

Running Node.js will now share port 8000 between the workers:

```console
$ node server.js
Primary 3596 is running
Worker 4324 started
Worker 4520 started
Worker 6056 started
Worker 5644 started
```

On Windows, it is not yet possible to set up a named pipe server in a worker.

c

[Worker](.././cluster/~/Worker "Worker")

No documentation available

-   [addListener](.././cluster/~/Worker#method_addlistener_0)
-   [destroy](.././cluster/~/Worker#method_destroy_0)
-   [disconnect](.././cluster/~/Worker#method_disconnect_0)
-   [emit](.././cluster/~/Worker#method_emit_0)
-   [exitedAfterDisconnect](.././cluster/~/Worker#property_exitedafterdisconnect)
-   [id](.././cluster/~/Worker#property_id)
-   [isConnected](.././cluster/~/Worker#method_isconnected_0)
-   [isDead](.././cluster/~/Worker#method_isdead_0)
-   [kill](.././cluster/~/Worker#method_kill_0)
-   [on](.././cluster/~/Worker#method_on_0)
-   [once](.././cluster/~/Worker#method_once_0)
-   [prependListener](.././cluster/~/Worker#method_prependlistener_0)
-   [prependOnceListener](.././cluster/~/Worker#method_prependoncelistener_0)
-   [process](.././cluster/~/Worker#property_process)
-   [send](.././cluster/~/Worker#method_send_0)

I

[Address](.././cluster/~/Address "Address")

No documentation available

-   [address](.././cluster/~/Address#property_address)
-   [addressType](.././cluster/~/Address#property_addresstype)
-   [port](.././cluster/~/Address#property_port)

I

[Cluster](.././cluster/~/Cluster "Cluster")

No documentation available

-   [SCHED\_NONE](.././cluster/~/Cluster#property_sched_none)
-   [SCHED\_RR](.././cluster/~/Cluster#property_sched_rr)
-   [addListener](.././cluster/~/Cluster#method_addlistener_0)
-   [disconnect](.././cluster/~/Cluster#method_disconnect_0)
-   [emit](.././cluster/~/Cluster#method_emit_0)
-   [fork](.././cluster/~/Cluster#method_fork_0)
-   [isMaster](.././cluster/~/Cluster#property_ismaster)
-   [isPrimary](.././cluster/~/Cluster#property_isprimary)
-   [isWorker](.././cluster/~/Cluster#property_isworker)
-   [on](.././cluster/~/Cluster#method_on_0)
-   [once](.././cluster/~/Cluster#method_once_0)
-   [prependListener](.././cluster/~/Cluster#method_prependlistener_0)
-   [prependOnceListener](.././cluster/~/Cluster#method_prependoncelistener_0)
-   [schedulingPolicy](.././cluster/~/Cluster#property_schedulingpolicy)
-   [settings](.././cluster/~/Cluster#property_settings)
-   [setupMaster](.././cluster/~/Cluster#method_setupmaster_0)
-   [setupPrimary](.././cluster/~/Cluster#method_setupprimary_0)
-   [worker](.././cluster/~/Cluster#property_worker)
-   [workers](.././cluster/~/Cluster#property_workers)

I

[ClusterSettings](.././cluster/~/ClusterSettings "ClusterSettings")

No documentation available

-   [args](.././cluster/~/ClusterSettings#property_args)
-   [cwd](.././cluster/~/ClusterSettings#property_cwd)
-   [exec](.././cluster/~/ClusterSettings#property_exec)
-   [execArgv](.././cluster/~/ClusterSettings#property_execargv)
-   [gid](.././cluster/~/ClusterSettings#property_gid)
-   [inspectPort](.././cluster/~/ClusterSettings#property_inspectport)
-   [serialization](.././cluster/~/ClusterSettings#property_serialization)
-   [silent](.././cluster/~/ClusterSettings#property_silent)
-   [stdio](.././cluster/~/ClusterSettings#property_stdio)
-   [uid](.././cluster/~/ClusterSettings#property_uid)
-   [windowsHide](.././cluster/~/ClusterSettings#property_windowshide)

T

[SerializationType](.././cluster/~/SerializationType "SerializationType")

No documentation available

v

[cluster](.././cluster/~/cluster "cluster")

No documentation available

v

[default](.././cluster/~/default "default")

No documentation available
