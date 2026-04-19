---
title: "Testing - Deno documentation"
source: "https://docs.deno.com/api/deno/testing"
canonical_url: "https://docs.deno.com/api/deno/testing"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:24.532Z"
content_hash: "b98e1b337a290282a2b8263503dc30cd788e1e7e1c947c738b799c91201f12ab"
menu_path: ["Testing - Deno documentation"]
section_path: []
---
### Functions [#](#Functions)

f

[Deno.bench](./././~/Deno.bench "Deno.bench")

Register a benchmark test which will be run when `deno bench` is used on the command line and the containing module looks like a bench module.

### Interfaces [#](#Interfaces)

I

[Deno.BenchContext](./././~/Deno.BenchContext "Deno.BenchContext")

Context that is passed to a benchmarked function. The instance is shared between iterations of the benchmark. Its methods can be used for example to override of the measured portion of the function.

*   [end](./././~/Deno.BenchContext#method_end_0)
*   [name](./././~/Deno.BenchContext#property_name)
*   [origin](./././~/Deno.BenchContext#property_origin)
*   [start](./././~/Deno.BenchContext#method_start_0)

I

[Deno.BenchDefinition](./././~/Deno.BenchDefinition "Deno.BenchDefinition")

The interface for defining a benchmark test using [`Deno.bench`](./././~/Deno.bench).

*   [baseline](./././~/Deno.BenchDefinition#property_baseline)
*   [fn](./././~/Deno.BenchDefinition#property_fn)
*   [group](./././~/Deno.BenchDefinition#property_group)
*   [ignore](./././~/Deno.BenchDefinition#property_ignore)
*   [n](./././~/Deno.BenchDefinition#property_n)
*   [name](./././~/Deno.BenchDefinition#property_name)
*   [only](./././~/Deno.BenchDefinition#property_only)
*   [permissions](./././~/Deno.BenchDefinition#property_permissions)
*   [sanitizeExit](./././~/Deno.BenchDefinition#property_sanitizeexit)
*   [warmup](./././~/Deno.BenchDefinition#property_warmup)

I

[Deno.DenoTest](./././~/Deno.DenoTest "Deno.DenoTest")

No documentation available

*   [afterAll](./././~/Deno.DenoTest#method_afterall_0)
*   [afterEach](./././~/Deno.DenoTest#method_aftereach_0)
*   [beforeAll](./././~/Deno.DenoTest#method_beforeall_0)
*   [beforeEach](./././~/Deno.DenoTest#method_beforeeach_0)
*   [ignore](./././~/Deno.DenoTest#method_ignore_0)
*   [only](./././~/Deno.DenoTest#method_only_0)

I

[Deno.TestContext](./././~/Deno.TestContext "Deno.TestContext")

Context that is passed to a testing function, which can be used to either gain information about the current test, or register additional test steps within the current test.

*   [name](./././~/Deno.TestContext#property_name)
*   [origin](./././~/Deno.TestContext#property_origin)
*   [parent](./././~/Deno.TestContext#property_parent)
*   [step](./././~/Deno.TestContext#method_step_0)

I

[Deno.TestDefinition](./././~/Deno.TestDefinition "Deno.TestDefinition")

No documentation available

*   [fn](./././~/Deno.TestDefinition#property_fn)
*   [ignore](./././~/Deno.TestDefinition#property_ignore)
*   [name](./././~/Deno.TestDefinition#property_name)
*   [only](./././~/Deno.TestDefinition#property_only)
*   [permissions](./././~/Deno.TestDefinition#property_permissions)
*   [sanitizeExit](./././~/Deno.TestDefinition#property_sanitizeexit)
*   [sanitizeOps](./././~/Deno.TestDefinition#property_sanitizeops)
*   [sanitizeResources](./././~/Deno.TestDefinition#property_sanitizeresources)

I

[Deno.TestStepDefinition](./././~/Deno.TestStepDefinition "Deno.TestStepDefinition")

No documentation available

*   [fn](./././~/Deno.TestStepDefinition#property_fn)
*   [ignore](./././~/Deno.TestStepDefinition#property_ignore)
*   [name](./././~/Deno.TestStepDefinition#property_name)
*   [sanitizeExit](./././~/Deno.TestStepDefinition#property_sanitizeexit)
*   [sanitizeOps](./././~/Deno.TestStepDefinition#property_sanitizeops)
*   [sanitizeResources](./././~/Deno.TestStepDefinition#property_sanitizeresources)

### Variables [#](#Variables)

v

[Deno.test](./././~/Deno.test "Deno.test")

Register a test which will be run when `deno test` is used on the command line and the containing module looks like a test module.
