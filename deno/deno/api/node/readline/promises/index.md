---
title: "readline/promises - Node documentation"
source: "https://docs.deno.com/api/node/readline/promises/"
canonical_url: "https://docs.deno.com/api/node/readline/promises/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:43.718Z"
content_hash: "182e1362f035d35ef5cd19a04468d1ea6cc4a649c333df52e4ac2cb0777e0e75"
menu_path: ["readline/promises - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/readline/index.md", "title": "readline - Node documentation"}
nav_next: {"path": "deno/deno/api/node/repl/index.md", "title": "repl - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:readline/promises";
```

### Classes [#](#Classes)

c

[Interface](../.././readline/promises/~/Interface "Interface")

Instances of the `readlinePromises.Interface` class are constructed using the `readlinePromises.createInterface()` method. Every instance is associated with a single `input` `Readable` stream and a single `output` `Writable` stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

*   [question](../.././readline/promises/~/Interface#method_question_0)

c

[Readline](../.././readline/promises/~/Readline "Readline")

No documentation available

*   [clearLine](../.././readline/promises/~/Readline#method_clearline_0)
*   [clearScreenDown](../.././readline/promises/~/Readline#method_clearscreendown_0)
*   [commit](../.././readline/promises/~/Readline#method_commit_0)
*   [cursorTo](../.././readline/promises/~/Readline#method_cursorto_0)
*   [moveCursor](../.././readline/promises/~/Readline#method_movecursor_0)
*   [rollback](../.././readline/promises/~/Readline#method_rollback_0)

### Functions [#](#Functions)

f

[createInterface](../.././readline/promises/~/createInterface "createInterface")

The `readlinePromises.createInterface()` method creates a new `readlinePromises.Interface` instance.

### Interfaces [#](#Interfaces)

I

[ReadLineOptions](../.././readline/promises/~/ReadLineOptions "ReadLineOptions")

No documentation available

*   [completer](../.././readline/promises/~/ReadLineOptions#property_completer)

### Type Aliases [#](<#Type Aliases>)

T

[Completer](../.././readline/promises/~/Completer "Completer")

No documentation available
