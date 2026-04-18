---
title: "Debugging"
source: "https://docs.deno.com/runtime/fundamentals/debugging/"
canonical_url: "https://docs.deno.com/runtime/fundamentals/debugging/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:30.838Z"
content_hash: "0bd2faf721b0452aa941be468a1206a02f1d2ecb5e252e968b5a9cd679f66ec0"
menu_path: ["Debugging"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/fundamentals/testing/index.md", "title": "Testing"}
nav_next: {"path": "deno/deno/runtime/fundamentals/workspaces/index.md", "title": "Workspaces and monorepos"}
---

# or with deno eval
deno eval --cpu-prof "for (let i = 0; i < 1e8; i++) {}"
```

When your program exits, Deno will write a `.cpuprofile` file to the current directory (e.g., `CPU.1769017882255.25986.cpuprofile`). This file can be loaded into Chrome DevTools (Performance tab) or other V8 profile viewers for analysis.

### CPU profiling flags

Flag

Description

`--cpu-prof`

Enable CPU profiling. Profile is written to disk on exit.

`--cpu-prof-dir=<DIR>`

Directory where the CPU profile will be written. Defaults to current directory. Implicitly enables `--cpu-prof`.

`--cpu-prof-name=<NAME>`

Filename for the CPU profile. Defaults to `CPU.<timestamp>.<pid>.cpuprofile`.

`--cpu-prof-interval=<MICROSECONDS>`

Sampling interval in microseconds. Default is `1000` (1ms). Lower values give more detail but larger files.

`--cpu-prof-md`

Generate a human-readable Markdown report alongside the `.cpuprofile` file.

`--cpu-prof-flamegraph`

Generate an interactive SVG flamegraph alongside the `.cpuprofile` file.

Note

CPU profiles report line numbers from the transpiled JavaScript code, not the original TypeScript source. This is a limitation of V8's profiler. For TypeScript files, the reported line numbers may not match your source code directly.

### Analyzing profiles in Chrome DevTools

To analyze the `.cpuprofile` file:

1.  Open Chrome DevTools (F12)
2.  Go to the **Performance** tab
3.  Click the **Load profile** button (up arrow icon)
4.  Select your `.cpuprofile` file

The DevTools will display a flame chart and detailed breakdown of where time was spent in your application.

### Example: Markdown report

The `--cpu-prof-md` flag generates a Markdown summary that's easy to read without loading the profile into DevTools:

\>\_

```sh
deno run -A --cpu-prof --cpu-prof-md server.js
```

This creates both a `.cpuprofile` file and a `.md` file with a report like:

```md
# CPU Profile

| Duration | Samples | Interval | Functions |
| -------- | ------- | -------- | --------- |
| 833.06ms | 641     | 1000us   | 10        |

**Top 10:** `op_crypto_get_random_values` 98.5%, `(garbage collector)` 0.7%,
`getRandomValues` 0.6%, `assertBranded` 0.2%

## Hot Functions (Self Time)

| Self% |     Self | Total% |    Total | Function                      | Location          |
| ----: | -------: | -----: | -------: | ----------------------------- | ----------------- |
| 98.5% | 533.00ms |  98.5% | 533.00ms | `op_crypto_get_random_values` | [native code]     |
|  0.7% |   4.00ms |   0.7% |   4.00ms | `(garbage collector)`         | [native code]     |
|  0.6% |   3.00ms |   0.6% |   3.00ms | `getRandomValues`             | 00_crypto.js:5274 |
|  0.2% |   1.00ms |   0.2% |   1.00ms | `assertBranded`               | 00_webidl.js:1149 |

## Call Tree (Total Time)

| Total% |    Total | Self% |     Self | Function                      | Location          |
| -----: | -------: | ----: | -------: | ----------------------------- | ----------------- |
|  16.8% |  91.00ms | 16.8% |  91.00ms | `(anonymous)`                 | server.js:1       |
|   0.6% |   3.00ms |  0.6% |   3.00ms | `getRandomValues`             | 00_crypto.js:5274 |
|  98.5% | 533.00ms | 98.5% | 533.00ms | `op_crypto_get_random_values` | [native code]     |

## Function Details

### `op_crypto_get_random_values`

[native code] | Self: 98.5% (533.00ms) | Total: 98.5% (533.00ms) | Samples: 533
```

The report includes:

*   **Summary**: Total duration, sample count, sampling interval, and function count
*   **Top 10**: Quick overview of the most expensive functions
*   **Hot Functions**: Functions sorted by self time (time spent in the function itself, excluding callees)
*   **Call Tree**: Hierarchical view showing the call stack and time distribution
*   **Function Details**: Per-function breakdown with sample counts

### Example: Interactive flamegraph

The `--cpu-prof-flamegraph` flag generates a self-contained, interactive SVG flamegraph that you can open directly in a browser — no external tools required:

\>\_

```sh
deno run --cpu-prof --cpu-prof-flamegraph your_script.ts
```

This creates both a `.cpuprofile` file and an `.svg` file. Open the SVG in any browser to explore the profile interactively:

*   **Click** any frame to zoom into that subtree
*   **Reset Zoom** button to restore the full view
*   **Ctrl+F** or the **Search** button for regex-based function search with highlighting and matched percentage
*   **Invert** checkbox to flip into an icicle graph (root at top)
*   **Hover** any frame to see the function name and sample count

The flamegraph also works with `deno eval`:

\>\_

```sh
deno eval --cpu-prof --cpu-prof-flamegraph "for (let i = 0; i < 1e8; i++) {}"
```

## OpenTelemetry integration

For production applications or complex systems, OpenTelemetry provides a more comprehensive approach to observability and debugging. Deno includes built-in support for OpenTelemetry, allowing you to:

*   Trace requests through your application
*   Monitor application performance metrics
*   Collect structured logs
*   Export telemetry data to monitoring systems

\>\_

```sh
OTEL_DENO=true deno run your_script.ts
```

This will automatically collect and export runtime observability data, including:

*   HTTP request traces
*   Runtime metrics
*   Console logs and errors

For full details on Deno's OpenTelemetry integration, including custom metrics, traces, and configuration options, see the [OpenTelemetry documentation](/runtime/fundamentals/open_telemetry).

## TLS session debugging

Set the `SSLKEYLOGFILE` environment variable to log TLS session keys to a file. This enables you to decrypt and inspect encrypted network traffic with tools like [Wireshark](https://www.wireshark.org/):

\>\_

```sh
SSLKEYLOGFILE=./keys.log deno run -N main.ts
```

Then load `keys.log` in Wireshark (Edit > Preferences > Protocols > TLS > (Pre)-Master-Secret log filename) to decrypt captured TLS traffic.

