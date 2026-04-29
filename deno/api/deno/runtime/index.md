---
title: "Runtime - Deno documentation"
source: "https://docs.deno.com/api/deno/runtime"
canonical_url: "https://docs.deno.com/api/deno/runtime"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:54:55.031Z"
content_hash: "12db94997ea58e1f2292e9d29c8e6365e02d13c46bc455812650538827632b3d"
menu_path: ["Runtime - Deno documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../permissions/index.md", "title": "Permissions - Deno documentation"}
nav_next: {"path": "../subprocess/index.md", "title": "Subprocess - Deno documentation"}
---

f

[Deno.addSignalListener](./././~/Deno.addSignalListener "Deno.addSignalListener")

Registers the given function as a listener of the given signal event.

f

[Deno.chdir](./././~/Deno.chdir "Deno.chdir")

Change the current working directory to the specified path.

f

[Deno.cwd](./././~/Deno.cwd "Deno.cwd")

Return a string representing the current working directory.

f

[Deno.execPath](./././~/Deno.execPath "Deno.execPath")

Returns the path to the current deno executable.

f

[Deno.exit](./././~/Deno.exit "Deno.exit")

Exit the Deno process with optional exit code.

f

[Deno.gid](./././~/Deno.gid "Deno.gid")

Returns the group id of the process on POSIX platforms. Returns null on windows.

f

[Deno.hostname](./././~/Deno.hostname "Deno.hostname")

Get the `hostname` of the machine the Deno process is running on.

f

[Deno.loadavg](./././~/Deno.loadavg "Deno.loadavg")

Returns an array containing the 1, 5, and 15 minute load averages. The load average is a measure of CPU and IO utilization of the last one, five, and 15 minute periods expressed as a fractional number. Zero means there is no load. On Windows, the three values are always the same and represent the current load, not the 1, 5 and 15 minute load averages.

f

[Deno.memoryUsage](./././~/Deno.memoryUsage "Deno.memoryUsage")

Returns an object describing the memory usage of the Deno process and the V8 subsystem measured in bytes.

f

[Deno.osRelease](./././~/Deno.osRelease "Deno.osRelease")

Returns the release version of the Operating System.

f

[Deno.osUptime](./././~/Deno.osUptime "Deno.osUptime")

Returns the Operating System uptime in number of seconds.

f

[Deno.refTimer](./././~/Deno.refTimer "Deno.refTimer")

Make the timer of the given `id` block the event loop from finishing.

f

[Deno.removeSignalListener](./././~/Deno.removeSignalListener "Deno.removeSignalListener")

Removes the given signal listener that has been registered with [`Deno.addSignalListener`](./././~/Deno.addSignalListener).

f

[Deno.systemMemoryInfo](./././~/Deno.systemMemoryInfo "Deno.systemMemoryInfo")

Displays the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel.

f

[Deno.uid](./././~/Deno.uid "Deno.uid")

Returns the user id of the process on POSIX platforms. Returns null on Windows.

f

[Deno.unrefTimer](./././~/Deno.unrefTimer "Deno.unrefTimer")

Make the timer of the given `id` not block the event loop from finishing.

I

[Deno.Env](./././~/Deno.Env "Deno.Env")

An interface containing methods to interact with the process environment variables.

-   [delete](./././~/Deno.Env#method_delete_0)
-   [get](./././~/Deno.Env#method_get_0)
-   [has](./././~/Deno.Env#method_has_0)
-   [set](./././~/Deno.Env#method_set_0)
-   [toObject](./././~/Deno.Env#method_toobject_0)

I

[Deno.MemoryUsage](./././~/Deno.MemoryUsage "Deno.MemoryUsage")

No documentation available

-   [external](./././~/Deno.MemoryUsage#property_external)
-   [heapTotal](./././~/Deno.MemoryUsage#property_heaptotal)
-   [heapUsed](./././~/Deno.MemoryUsage#property_heapused)
-   [rss](./././~/Deno.MemoryUsage#property_rss)

I

[Deno.SystemMemoryInfo](./././~/Deno.SystemMemoryInfo "Deno.SystemMemoryInfo")

Information returned from a call to [`Deno.systemMemoryInfo`](./././~/Deno.systemMemoryInfo).

-   [available](./././~/Deno.SystemMemoryInfo#property_available)
-   [buffers](./././~/Deno.SystemMemoryInfo#property_buffers)
-   [cached](./././~/Deno.SystemMemoryInfo#property_cached)
-   [free](./././~/Deno.SystemMemoryInfo#property_free)
-   [swapFree](./././~/Deno.SystemMemoryInfo#property_swapfree)
-   [swapTotal](./././~/Deno.SystemMemoryInfo#property_swaptotal)
-   [total](./././~/Deno.SystemMemoryInfo#property_total)

T

[Deno.Signal](./././~/Deno.Signal "Deno.Signal")

Operating signals which can be listened for or sent to sub-processes. What signals and what their standard behaviors are OS dependent.

v

[Deno.args](./././~/Deno.args "Deno.args")

Returns the script arguments to the program.

v

[Deno.build](./././~/Deno.build "Deno.build")

Information related to the build of the current Deno runtime.

-   [arch](./././~/Deno.build#property_arch)
-   [env](./././~/Deno.build#property_env)
-   [os](./././~/Deno.build#property_os)
-   [standalone](./././~/Deno.build#property_standalone)
-   [target](./././~/Deno.build#property_target)
-   [vendor](./././~/Deno.build#property_vendor)

v

[Deno.env](./././~/Deno.env "Deno.env")

An interface containing methods to interact with the process environment variables.

v

[Deno.exitCode](./././~/Deno.exitCode "Deno.exitCode")

The exit code for the Deno process.

v

[Deno.mainModule](./././~/Deno.mainModule "Deno.mainModule")

The URL of the entrypoint module entered from the command-line. It requires read permission to the CWD.

v

[Deno.noColor](./././~/Deno.noColor "Deno.noColor")

Reflects the `NO_COLOR` environment variable at program start.

v

[Deno.pid](./././~/Deno.pid "Deno.pid")

The current process ID of this instance of the Deno CLI.

v

[Deno.ppid](./././~/Deno.ppid "Deno.ppid")

The process ID of parent process of this instance of the Deno CLI.

v

[Deno.version](./././~/Deno.version "Deno.version")

Version information related to the current Deno CLI runtime environment.

-   [deno](./././~/Deno.version#property_deno)
-   [typescript](./././~/Deno.version#property_typescript)
-   [v8](./././~/Deno.version#property_v8)
