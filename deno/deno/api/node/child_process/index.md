---
title: "child_process - Node documentation"
source: "https://docs.deno.com/api/node/child_process/"
canonical_url: "https://docs.deno.com/api/node/child_process/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:34.275Z"
content_hash: "a652ee4150bc5fd88be45ab2d688a46fe769da82c47da420fb3ac71cd809a656"
menu_path: ["child_process - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/buffer/index.md", "title": "buffer - Node documentation"}
nav_next: {"path": "deno/deno/api/node/cluster/index.md", "title": "cluster - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:child_process";
```

The `node:child_process` module provides the ability to spawn subprocesses in a manner that is similar, but not identical, to [`popen(3)`](http://man7.org/linux/man-pages/man3/popen.3.html). This capability is primarily provided by the [spawn](.././child_process/~/spawn) function:

```js
import { spawn } from 'node:child_process';
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

By default, pipes for `stdin`, `stdout`, and `stderr` are established between the parent Node.js process and the spawned subprocess. These pipes have limited (and platform-specific) capacity. If the subprocess writes to stdout in excess of that limit without the output being captured, the subprocess blocks waiting for the pipe buffer to accept more data. This is identical to the behavior of pipes in the shell. Use the `{ stdio: 'ignore' }` option if the output will not be consumed.

The command lookup is performed using the `options.env.PATH` environment variable if `env` is in the `options` object. Otherwise, `process.env.PATH` is used. If `options.env` is set without `PATH`, lookup on Unix is performed on a default search path search of `/usr/bin:/bin` (see your operating system's manual for execvpe/execvp), on Windows the current processes environment variable `PATH` is used.

On Windows, environment variables are case-insensitive. Node.js lexicographically sorts the `env` keys and uses the first one that case-insensitively matches. Only first (in lexicographic order) entry will be passed to the subprocess. This might lead to issues on Windows when passing objects to the `env` option that have multiple variants of the same key, such as `PATH` and `Path`.

The [spawn](.././child_process/~/spawn) method spawns the child process asynchronously, without blocking the Node.js event loop. The [spawnSync](.././child_process/~/spawnSync) function provides equivalent functionality in a synchronous manner that blocks the event loop until the spawned process either exits or is terminated.

For convenience, the `node:child_process` module provides a handful of synchronous and asynchronous alternatives to [spawn](.././child_process/~/spawn) and [spawnSync](.././child_process/~/spawnSync). Each of these alternatives are implemented on top of [spawn](.././child_process/~/spawn) or [spawnSync](.././child_process/~/spawnSync).

*   [exec](.././child_process/~/exec): spawns a shell and runs a command within that shell, passing the `stdout` and `stderr` to a callback function when complete.
*   [execFile](.././child_process/~/execFile): similar to [exec](.././child_process/~/exec) except that it spawns the command directly without first spawning a shell by default.
*   [fork](.././child_process/~/fork): spawns a new Node.js process and invokes a specified module with an IPC communication channel established that allows sending messages between parent and child.
*   [execSync](.././child_process/~/execSync): a synchronous version of [exec](.././child_process/~/exec) that will block the Node.js event loop.
*   [execFileSync](.././child_process/~/execFileSync): a synchronous version of [execFile](.././child_process/~/execFile) that will block the Node.js event loop.

For certain use cases, such as automating shell scripts, the `synchronous counterparts` may be more convenient. In many cases, however, the synchronous methods can have significant impact on performance due to stalling the event loop while spawned processes complete.

### Classes [#](#Classes)

c

[ChildProcess](.././child_process/~/ChildProcess "ChildProcess")

Instances of the `ChildProcess` represent spawned child processes.

*   [addListener](.././child_process/~/ChildProcess#method_addlistener_0)
*   [channel](.././child_process/~/ChildProcess#property_channel)
*   [connected](.././child_process/~/ChildProcess#property_connected)
*   [disconnect](.././child_process/~/ChildProcess#method_disconnect_0)
*   [emit](.././child_process/~/ChildProcess#method_emit_0)
*   [exitCode](.././child_process/~/ChildProcess#property_exitcode)
*   [kill](.././child_process/~/ChildProcess#method_kill_0)
*   [killed](.././child_process/~/ChildProcess#property_killed)
*   [on](.././child_process/~/ChildProcess#method_on_0)
*   [once](.././child_process/~/ChildProcess#method_once_0)
*   [pid](.././child_process/~/ChildProcess#property_pid)
*   [prependListener](.././child_process/~/ChildProcess#method_prependlistener_0)
*   [prependOnceListener](.././child_process/~/ChildProcess#method_prependoncelistener_0)
*   [ref](.././child_process/~/ChildProcess#method_ref_0)
*   [send](.././child_process/~/ChildProcess#method_send_0)
*   [signalCode](.././child_process/~/ChildProcess#property_signalcode)
*   [spawnargs](.././child_process/~/ChildProcess#property_spawnargs)
*   [spawnfile](.././child_process/~/ChildProcess#property_spawnfile)
*   [stderr](.././child_process/~/ChildProcess#property_stderr)
*   [stdin](.././child_process/~/ChildProcess#property_stdin)
*   [stdio](.././child_process/~/ChildProcess#property_stdio)
*   [stdout](.././child_process/~/ChildProcess#property_stdout)
*   [unref](.././child_process/~/ChildProcess#method_unref_0)

### Functions [#](#Functions)

f

[exec](.././child_process/~/exec "exec")

Spawns a shell then executes the `command` within that shell, buffering any generated output. The `command` string passed to the exec function is processed directly by the shell and special characters (vary based on [shell](https://en.wikipedia.org/wiki/List_of_command-line_interpreters)) need to be dealt with accordingly:

f

[execFile](.././child_process/~/execFile "execFile")

The `child_process.execFile()` function is similar to [exec](.././child_process/~/exec) except that it does not spawn a shell by default. Rather, the specified executable `file` is spawned directly as a new process making it slightly more efficient than [exec](.././child_process/~/exec).

f

[execFileSync](.././child_process/~/execFileSync "execFileSync")

The `child_process.execFileSync()` method is generally identical to [execFile](.././child_process/~/execFile) with the exception that the method will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited.

f

[execSync](.././child_process/~/execSync "execSync")

The `child_process.execSync()` method is generally identical to [exec](.././child_process/~/exec) with the exception that the method will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited. If the child process intercepts and handles the `SIGTERM` signal and doesn't exit, the parent process will wait until the child process has exited.

f

[fork](.././child_process/~/fork "fork")

The `child_process.fork()` method is a special case of [spawn](.././child_process/~/spawn) used specifically to spawn new Node.js processes. Like [spawn](.././child_process/~/spawn), a `ChildProcess` object is returned. The returned `ChildProcess` will have an additional communication channel built-in that allows messages to be passed back and forth between the parent and child. See `subprocess.send()` for details.

f

[spawn](.././child_process/~/spawn "spawn")

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`. If omitted, `args` defaults to an empty array.

f

[spawnSync](.././child_process/~/spawnSync "spawnSync")

The `child_process.spawnSync()` method is generally identical to [spawn](.././child_process/~/spawn) with the exception that the function will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited. If the process intercepts and handles the `SIGTERM` signal and doesn't exit, the parent process will wait until the child process has exited.

### Interfaces [#](#Interfaces)

I

[ChildProcessByStdio](.././child_process/~/ChildProcessByStdio "ChildProcessByStdio")

No documentation available

*   [stderr](.././child_process/~/ChildProcessByStdio#property_stderr)
*   [stdin](.././child_process/~/ChildProcessByStdio#property_stdin)
*   [stdio](.././child_process/~/ChildProcessByStdio#property_stdio)
*   [stdout](.././child_process/~/ChildProcessByStdio#property_stdout)

I

[ChildProcessWithoutNullStreams](.././child_process/~/ChildProcessWithoutNullStreams "ChildProcessWithoutNullStreams")

No documentation available

*   [stderr](.././child_process/~/ChildProcessWithoutNullStreams#property_stderr)
*   [stdin](.././child_process/~/ChildProcessWithoutNullStreams#property_stdin)
*   [stdio](.././child_process/~/ChildProcessWithoutNullStreams#property_stdio)
*   [stdout](.././child_process/~/ChildProcessWithoutNullStreams#property_stdout)

I

[CommonExecOptions](.././child_process/~/CommonExecOptions "CommonExecOptions")

No documentation available

*   [encoding](.././child_process/~/CommonExecOptions#property_encoding)
*   [input](.././child_process/~/CommonExecOptions#property_input)
*   [killSignal](.././child_process/~/CommonExecOptions#property_killsignal)
*   [maxBuffer](.././child_process/~/CommonExecOptions#property_maxbuffer)
*   [stdio](.././child_process/~/CommonExecOptions#property_stdio)

I

[CommonOptions](.././child_process/~/CommonOptions "CommonOptions")

No documentation available

*   [timeout](.././child_process/~/CommonOptions#property_timeout)
*   [windowsHide](.././child_process/~/CommonOptions#property_windowshide)

I

[CommonSpawnOptions](.././child_process/~/CommonSpawnOptions "CommonSpawnOptions")

No documentation available

*   [argv0](.././child_process/~/CommonSpawnOptions#property_argv0)
*   [shell](.././child_process/~/CommonSpawnOptions#property_shell)
*   [stdio](.././child_process/~/CommonSpawnOptions#property_stdio)
*   [windowsVerbatimArguments](.././child_process/~/CommonSpawnOptions#property_windowsverbatimarguments)

I

[ExecException](.././child_process/~/ExecException "ExecException")

No documentation available

*   [cmd](.././child_process/~/ExecException#property_cmd)
*   [code](.././child_process/~/ExecException#property_code)
*   [killed](.././child_process/~/ExecException#property_killed)
*   [signal](.././child_process/~/ExecException#property_signal)
*   [stderr](.././child_process/~/ExecException#property_stderr)
*   [stdout](.././child_process/~/ExecException#property_stdout)

I

[ExecFileOptions](.././child_process/~/ExecFileOptions "ExecFileOptions")

No documentation available

*   [killSignal](.././child_process/~/ExecFileOptions#property_killsignal)
*   [maxBuffer](.././child_process/~/ExecFileOptions#property_maxbuffer)
*   [shell](.././child_process/~/ExecFileOptions#property_shell)
*   [signal](.././child_process/~/ExecFileOptions#property_signal)
*   [windowsVerbatimArguments](.././child_process/~/ExecFileOptions#property_windowsverbatimarguments)

I

[ExecFileOptionsWithBufferEncoding](.././child_process/~/ExecFileOptionsWithBufferEncoding "ExecFileOptionsWithBufferEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecFileOptionsWithBufferEncoding#property_encoding)

I

[ExecFileOptionsWithOtherEncoding](.././child_process/~/ExecFileOptionsWithOtherEncoding "ExecFileOptionsWithOtherEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecFileOptionsWithOtherEncoding#property_encoding)

I

[ExecFileOptionsWithStringEncoding](.././child_process/~/ExecFileOptionsWithStringEncoding "ExecFileOptionsWithStringEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecFileOptionsWithStringEncoding#property_encoding)

I

[ExecFileSyncOptions](.././child_process/~/ExecFileSyncOptions "ExecFileSyncOptions")

No documentation available

*   [shell](.././child_process/~/ExecFileSyncOptions#property_shell)

I

[ExecFileSyncOptionsWithBufferEncoding](.././child_process/~/ExecFileSyncOptionsWithBufferEncoding "ExecFileSyncOptionsWithBufferEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecFileSyncOptionsWithBufferEncoding#property_encoding)

I

[ExecFileSyncOptionsWithStringEncoding](.././child_process/~/ExecFileSyncOptionsWithStringEncoding "ExecFileSyncOptionsWithStringEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecFileSyncOptionsWithStringEncoding#property_encoding)

I

[ExecOptions](.././child_process/~/ExecOptions "ExecOptions")

No documentation available

*   [killSignal](.././child_process/~/ExecOptions#property_killsignal)
*   [maxBuffer](.././child_process/~/ExecOptions#property_maxbuffer)
*   [shell](.././child_process/~/ExecOptions#property_shell)
*   [signal](.././child_process/~/ExecOptions#property_signal)

I

[ExecOptionsWithBufferEncoding](.././child_process/~/ExecOptionsWithBufferEncoding "ExecOptionsWithBufferEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecOptionsWithBufferEncoding#property_encoding)

I

[ExecOptionsWithStringEncoding](.././child_process/~/ExecOptionsWithStringEncoding "ExecOptionsWithStringEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecOptionsWithStringEncoding#property_encoding)

I

[ExecSyncOptions](.././child_process/~/ExecSyncOptions "ExecSyncOptions")

No documentation available

*   [shell](.././child_process/~/ExecSyncOptions#property_shell)

I

[ExecSyncOptionsWithBufferEncoding](.././child_process/~/ExecSyncOptionsWithBufferEncoding "ExecSyncOptionsWithBufferEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecSyncOptionsWithBufferEncoding#property_encoding)

I

[ExecSyncOptionsWithStringEncoding](.././child_process/~/ExecSyncOptionsWithStringEncoding "ExecSyncOptionsWithStringEncoding")

No documentation available

*   [encoding](.././child_process/~/ExecSyncOptionsWithStringEncoding#property_encoding)

I

[ForkOptions](.././child_process/~/ForkOptions "ForkOptions")

No documentation available

*   [detached](.././child_process/~/ForkOptions#property_detached)
*   [execArgv](.././child_process/~/ForkOptions#property_execargv)
*   [execPath](.././child_process/~/ForkOptions#property_execpath)
*   [silent](.././child_process/~/ForkOptions#property_silent)
*   [stdio](.././child_process/~/ForkOptions#property_stdio)
*   [windowsVerbatimArguments](.././child_process/~/ForkOptions#property_windowsverbatimarguments)

I

[MessageOptions](.././child_process/~/MessageOptions "MessageOptions")

No documentation available

*   [keepOpen](.././child_process/~/MessageOptions#property_keepopen)

I

[MessagingOptions](.././child_process/~/MessagingOptions "MessagingOptions")

No documentation available

*   [killSignal](.././child_process/~/MessagingOptions#property_killsignal)
*   [serialization](.././child_process/~/MessagingOptions#property_serialization)
*   [timeout](.././child_process/~/MessagingOptions#property_timeout)

I

[ProcessEnvOptions](.././child_process/~/ProcessEnvOptions "ProcessEnvOptions")

No documentation available

*   [cwd](.././child_process/~/ProcessEnvOptions#property_cwd)
*   [env](.././child_process/~/ProcessEnvOptions#property_env)
*   [gid](.././child_process/~/ProcessEnvOptions#property_gid)
*   [uid](.././child_process/~/ProcessEnvOptions#property_uid)

I

[PromiseWithChild](.././child_process/~/PromiseWithChild "PromiseWithChild")

No documentation available

*   [child](.././child_process/~/PromiseWithChild#property_child)

I

[SpawnOptions](.././child_process/~/SpawnOptions "SpawnOptions")

No documentation available

*   [detached](.././child_process/~/SpawnOptions#property_detached)

I

[SpawnOptionsWithoutStdio](.././child_process/~/SpawnOptionsWithoutStdio "SpawnOptionsWithoutStdio")

No documentation available

*   [stdio](.././child_process/~/SpawnOptionsWithoutStdio#property_stdio)

I

[SpawnOptionsWithStdioTuple](.././child_process/~/SpawnOptionsWithStdioTuple "SpawnOptionsWithStdioTuple")

No documentation available

*   [stdio](.././child_process/~/SpawnOptionsWithStdioTuple#property_stdio)

I

[SpawnSyncOptions](.././child_process/~/SpawnSyncOptions "SpawnSyncOptions")

No documentation available

*   [encoding](.././child_process/~/SpawnSyncOptions#property_encoding)
*   [input](.././child_process/~/SpawnSyncOptions#property_input)
*   [maxBuffer](.././child_process/~/SpawnSyncOptions#property_maxbuffer)

I

[SpawnSyncOptionsWithBufferEncoding](.././child_process/~/SpawnSyncOptionsWithBufferEncoding "SpawnSyncOptionsWithBufferEncoding")

No documentation available

*   [encoding](.././child_process/~/SpawnSyncOptionsWithBufferEncoding#property_encoding)

I

[SpawnSyncOptionsWithStringEncoding](.././child_process/~/SpawnSyncOptionsWithStringEncoding "SpawnSyncOptionsWithStringEncoding")

No documentation available

*   [encoding](.././child_process/~/SpawnSyncOptionsWithStringEncoding#property_encoding)

I

[SpawnSyncReturns](.././child_process/~/SpawnSyncReturns "SpawnSyncReturns")

No documentation available

*   [error](.././child_process/~/SpawnSyncReturns#property_error)
*   [output](.././child_process/~/SpawnSyncReturns#property_output)
*   [pid](.././child_process/~/SpawnSyncReturns#property_pid)
*   [signal](.././child_process/~/SpawnSyncReturns#property_signal)
*   [status](.././child_process/~/SpawnSyncReturns#property_status)
*   [stderr](.././child_process/~/SpawnSyncReturns#property_stderr)
*   [stdout](.././child_process/~/SpawnSyncReturns#property_stdout)

### Type Aliases [#](<#Type Aliases>)

T

[ExecFileException](.././child_process/~/ExecFileException "ExecFileException")

No documentation available

T

[IOType](.././child_process/~/IOType "IOType")

No documentation available

T

[SendHandle](.././child_process/~/SendHandle "SendHandle")

No documentation available

T

[Serializable](.././child_process/~/Serializable "Serializable")

No documentation available

T

[SerializationType](.././child_process/~/SerializationType "SerializationType")

No documentation available

T

[StdioNull](.././child_process/~/StdioNull "StdioNull")

No documentation available

T

[StdioOptions](.././child_process/~/StdioOptions "StdioOptions")

No documentation available

T

[StdioPipe](.././child_process/~/StdioPipe "StdioPipe")

No documentation available

T

[StdioPipeNamed](.././child_process/~/StdioPipeNamed "StdioPipeNamed")

No documentation available


