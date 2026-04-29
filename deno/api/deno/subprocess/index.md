---
title: "Subprocess - Deno documentation"
source: "https://docs.deno.com/api/deno/subprocess"
canonical_url: "https://docs.deno.com/api/deno/subprocess"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:55:12.237Z"
content_hash: "2ddbfb0b2c072b0f6780da8c1c610b11b361e83def1de13eabcbdc1eb8c2cdd0"
menu_path: ["Subprocess - Deno documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../runtime/index.md", "title": "Runtime - Deno documentation"}
nav_next: {"path": "../telemetry/index.md", "title": "Telemetry - Deno documentation"}
---

c

[Deno.ChildProcess](./././~/Deno.ChildProcess "Deno.ChildProcess")

The interface for handling a child process returned from `Deno.Command.spawn`.

-   [kill](./././~/Deno.ChildProcess#method_kill_0)
-   [output](./././~/Deno.ChildProcess#method_output_0)
-   [pid](./././~/Deno.ChildProcess#property_pid)
-   [ref](./././~/Deno.ChildProcess#method_ref_0)
-   [status](./././~/Deno.ChildProcess#property_status)
-   [stderr](./././~/Deno.ChildProcess#accessor_stderr)
-   [stdin](./././~/Deno.ChildProcess#accessor_stdin)
-   [stdout](./././~/Deno.ChildProcess#accessor_stdout)
-   [unref](./././~/Deno.ChildProcess#method_unref_0)

c

[Deno.Command](./././~/Deno.Command "Deno.Command")

Create a child process.

-   [output](./././~/Deno.Command#method_output_0)
-   [outputSync](./././~/Deno.Command#method_outputsync_0)
-   [spawn](./././~/Deno.Command#method_spawn_0)

f

[Deno.kill](./././~/Deno.kill "Deno.kill")

Send a signal to process under given `pid`. The value and meaning of the `signal` to the process is operating system and process dependant. `Signal` provides the most common signals. Default signal is `"SIGTERM"`.

f

[Deno.spawn](./././~/Deno.spawn "Deno.spawn")

Spawns a new subprocess, returning a [`Deno.ChildProcess`](./././~/Deno.ChildProcess) handle.

f

[Deno.spawnAndWait](./././~/Deno.spawnAndWait "Deno.spawnAndWait")

Spawns a subprocess, waits for it to finish, and returns the output.

f

[Deno.spawnAndWaitSync](./././~/Deno.spawnAndWaitSync "Deno.spawnAndWaitSync")

Synchronously spawns a subprocess, waits for it to finish, and returns the output.

I

[Deno.CommandOptions](./././~/Deno.CommandOptions "Deno.CommandOptions")

Options which can be set when calling [`Deno.Command`](./././~/Deno.Command).

-   [args](./././~/Deno.CommandOptions#property_args)
-   [clearEnv](./././~/Deno.CommandOptions#property_clearenv)
-   [cwd](./././~/Deno.CommandOptions#property_cwd)
-   [detached](./././~/Deno.CommandOptions#property_detached)
-   [env](./././~/Deno.CommandOptions#property_env)
-   [gid](./././~/Deno.CommandOptions#property_gid)
-   [signal](./././~/Deno.CommandOptions#property_signal)
-   [stderr](./././~/Deno.CommandOptions#property_stderr)
-   [stdin](./././~/Deno.CommandOptions#property_stdin)
-   [stdout](./././~/Deno.CommandOptions#property_stdout)
-   [uid](./././~/Deno.CommandOptions#property_uid)
-   [windowsRawArguments](./././~/Deno.CommandOptions#property_windowsrawarguments)

I

[Deno.CommandOutput](./././~/Deno.CommandOutput "Deno.CommandOutput")

The interface returned from calling `Deno.Command.output` or `Deno.Command.outputSync` which represents the result of spawning the child process.

-   [stderr](./././~/Deno.CommandOutput#property_stderr)
-   [stdout](./././~/Deno.CommandOutput#property_stdout)

I

[Deno.CommandStatus](./././~/Deno.CommandStatus "Deno.CommandStatus")

No documentation available

-   [code](./././~/Deno.CommandStatus#property_code)
-   [signal](./././~/Deno.CommandStatus#property_signal)
-   [success](./././~/Deno.CommandStatus#property_success)

I

[Deno.SubprocessReadableStream](./././~/Deno.SubprocessReadableStream "Deno.SubprocessReadableStream")

The interface for stdout and stderr streams for child process returned from `Deno.Command.spawn`.

-   [arrayBuffer](./././~/Deno.SubprocessReadableStream#method_arraybuffer_0)
-   [bytes](./././~/Deno.SubprocessReadableStream#method_bytes_0)
-   [json](./././~/Deno.SubprocessReadableStream#method_json_0)
-   [text](./././~/Deno.SubprocessReadableStream#method_text_0)
