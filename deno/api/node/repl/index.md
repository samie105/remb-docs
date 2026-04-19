---
title: "repl - Node documentation"
source: "https://docs.deno.com/api/node/repl/"
canonical_url: "https://docs.deno.com/api/node/repl/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:46.462Z"
content_hash: "16d127650d4ab5f40d166f332c2a99f956df233c7a1104a3c31cbba94463de62"
menu_path: ["repl - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:repl";
```

Deno compatibility

All symbols are not supported.

The `node:repl` module provides a Read-Eval-Print-Loop (REPL) implementation that is available both as a standalone program or includible in other applications. It can be accessed using:

```js
import repl from 'node:repl';
```

### Classes [#](#Classes)

c

[Recoverable](.././repl/~/Recoverable "Recoverable")

No documentation available

*   [err](.././repl/~/Recoverable#property_err)

c

[REPLServer](.././repl/~/REPLServer "REPLServer")

No documentation available

*   [addListener](.././repl/~/REPLServer#method_addlistener_0)
*   [clearBufferedCommand](.././repl/~/REPLServer#method_clearbufferedcommand_0)
*   [commands](.././repl/~/REPLServer#property_commands)
*   [completer](.././repl/~/REPLServer#property_completer)
*   [context](.././repl/~/REPLServer#property_context)
*   [defineCommand](.././repl/~/REPLServer#method_definecommand_0)
*   [displayPrompt](.././repl/~/REPLServer#method_displayprompt_0)
*   [editorMode](.././repl/~/REPLServer#property_editormode)
*   [emit](.././repl/~/REPLServer#method_emit_0)
*   [eval](.././repl/~/REPLServer#property_eval)
*   [ignoreUndefined](.././repl/~/REPLServer#property_ignoreundefined)
*   [input](.././repl/~/REPLServer#property_input)
*   [inputStream](.././repl/~/REPLServer#property_inputstream)
*   [last](.././repl/~/REPLServer#property_last)
*   [lastError](.././repl/~/REPLServer#property_lasterror)
*   [on](.././repl/~/REPLServer#method_on_0)
*   [once](.././repl/~/REPLServer#method_once_0)
*   [output](.././repl/~/REPLServer#property_output)
*   [outputStream](.././repl/~/REPLServer#property_outputstream)
*   [prependListener](.././repl/~/REPLServer#method_prependlistener_0)
*   [prependOnceListener](.././repl/~/REPLServer#method_prependoncelistener_0)
*   [replMode](.././repl/~/REPLServer#property_replmode)
*   [setupHistory](.././repl/~/REPLServer#method_setuphistory_0)
*   [underscoreAssigned](.././repl/~/REPLServer#property_underscoreassigned)
*   [underscoreErrAssigned](.././repl/~/REPLServer#property_underscoreerrassigned)
*   [useColors](.././repl/~/REPLServer#property_usecolors)
*   [useGlobal](.././repl/~/REPLServer#property_useglobal)
*   [writer](.././repl/~/REPLServer#property_writer)

### Functions [#](#Functions)

f

[start](.././repl/~/start "start")

No documentation available

### Interfaces [#](#Interfaces)

I

[REPLCommand](.././repl/~/REPLCommand "REPLCommand")

No documentation available

*   [action](.././repl/~/REPLCommand#property_action)
*   [help](.././repl/~/REPLCommand#property_help)

I

[ReplOptions](.././repl/~/ReplOptions "ReplOptions")

No documentation available

*   [breakEvalOnSigint](.././repl/~/ReplOptions#property_breakevalonsigint)
*   [completer](.././repl/~/ReplOptions#property_completer)
*   [eval](.././repl/~/ReplOptions#property_eval)
*   [ignoreUndefined](.././repl/~/ReplOptions#property_ignoreundefined)
*   [input](.././repl/~/ReplOptions#property_input)
*   [output](.././repl/~/ReplOptions#property_output)
*   [preview](.././repl/~/ReplOptions#property_preview)
*   [prompt](.././repl/~/ReplOptions#property_prompt)
*   [replMode](.././repl/~/ReplOptions#property_replmode)
*   [terminal](.././repl/~/ReplOptions#property_terminal)
*   [useColors](.././repl/~/ReplOptions#property_usecolors)
*   [useGlobal](.././repl/~/ReplOptions#property_useglobal)
*   [writer](.././repl/~/ReplOptions#property_writer)

### Type Aliases [#](<#Type Aliases>)

T

[REPLCommandAction](.././repl/~/REPLCommandAction "REPLCommandAction")

No documentation available

T

[REPLEval](.././repl/~/REPLEval "REPLEval")

No documentation available

T

[REPLWriter](.././repl/~/REPLWriter "REPLWriter")

No documentation available

### Variables [#](#Variables)

v

[REPL\_MODE\_SLOPPY](.././repl/~/REPL_MODE_SLOPPY "REPL_MODE_SLOPPY")

A flag passed in the REPL options. Evaluates expressions in sloppy mode.

v

[REPL\_MODE\_STRICT](.././repl/~/REPL_MODE_STRICT "REPL_MODE_STRICT")

A flag passed in the REPL options. Evaluates expressions in strict mode. This is equivalent to prefacing every repl statement with `'use strict'`.

v

[writer](.././repl/~/writer "writer")

This is the default "writer" value, if none is passed in the REPL options, and it can be overridden by custom print functions.
