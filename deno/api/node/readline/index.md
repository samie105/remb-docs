---
title: "readline - Node documentation"
source: "https://docs.deno.com/api/node/readline/"
canonical_url: "https://docs.deno.com/api/node/readline/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:41.671Z"
content_hash: "ee5244703ea322a95f7091df845d1c2502daeb0b0b66e300978c9308048c7631"
menu_path: ["readline - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:readline";
```

The `node:readline` module provides an interface for reading data from a [Readable](https://nodejs.org/docs/latest-v22.x/api/stream.html#readable-streams) stream (such as [`process.stdin`](https://nodejs.org/docs/latest-v22.x/api/process.html#processstdin)) one line at a time.

To use the promise-based APIs:

```js
import * as readline from 'node:readline/promises';
```

To use the callback and sync APIs:

```js
import * as readline from 'node:readline';
```

The following simple example illustrates the basic use of the `node:readline` module.

```js
import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

const rl = readline.createInterface({ input, output });

const answer = await rl.question('What do you think of Node.js? ');

console.log(`Thank you for your valuable feedback: ${answer}`);

rl.close();
```

Once this code is invoked, the Node.js application will not terminate until the `readline.Interface` is closed because the interface waits for data to be received on the `input` stream.

### Classes [#](#Classes)

c

[Interface](.././readline/~/Interface "Interface")

Instances of the `readline.Interface` class are constructed using the `readline.createInterface()` method. Every instance is associated with a single `input` [Readable](https://nodejs.org/docs/latest-v22.x/api/stream.html#readable-streams) stream and a single `output` [Writable](https://nodejs.org/docs/latest-v22.x/api/stream.html#writable-streams) stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

*   [addListener](.././readline/~/Interface#method_addlistener_0)
*   [close](.././readline/~/Interface#method_close_0)
*   [cursor](.././readline/~/Interface#property_cursor)
*   [emit](.././readline/~/Interface#method_emit_0)
*   [getCursorPos](.././readline/~/Interface#method_getcursorpos_0)
*   [getPrompt](.././readline/~/Interface#method_getprompt_0)
*   [line](.././readline/~/Interface#property_line)
*   [on](.././readline/~/Interface#method_on_0)
*   [once](.././readline/~/Interface#method_once_0)
*   [pause](.././readline/~/Interface#method_pause_0)
*   [prependListener](.././readline/~/Interface#method_prependlistener_0)
*   [prependOnceListener](.././readline/~/Interface#method_prependoncelistener_0)
*   [prompt](.././readline/~/Interface#method_prompt_0)
*   [question](.././readline/~/Interface#method_question_0)
*   [resume](.././readline/~/Interface#method_resume_0)
*   [setPrompt](.././readline/~/Interface#method_setprompt_0)
*   [terminal](.././readline/~/Interface#property_terminal)
*   [write](.././readline/~/Interface#method_write_0)

c

[promises.Interface](.././readline/promises/~/promises.Interface "promises.Interface")

Instances of the `readlinePromises.Interface` class are constructed using the `readlinePromises.createInterface()` method. Every instance is associated with a single `input` `Readable` stream and a single `output` `Writable` stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

*   [question](.././readline/promises/~/promises.Interface#method_question_0)

c

[promises.Readline](.././readline/promises/~/promises.Readline "promises.Readline")

No documentation available

*   [clearLine](.././readline/promises/~/promises.Readline#method_clearline_0)
*   [clearScreenDown](.././readline/promises/~/promises.Readline#method_clearscreendown_0)
*   [commit](.././readline/promises/~/promises.Readline#method_commit_0)
*   [cursorTo](.././readline/promises/~/promises.Readline#method_cursorto_0)
*   [moveCursor](.././readline/promises/~/promises.Readline#method_movecursor_0)
*   [rollback](.././readline/promises/~/promises.Readline#method_rollback_0)

### Functions [#](#Functions)

f

[clearLine](.././readline/~/clearLine "clearLine")

The `readline.clearLine()` method clears current line of given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) stream in a specified direction identified by `dir`.

f

[clearScreenDown](.././readline/~/clearScreenDown "clearScreenDown")

The `readline.clearScreenDown()` method clears the given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) stream from the current position of the cursor down.

f

[createInterface](.././readline/~/createInterface "createInterface")

The `readline.createInterface()` method creates a new `readline.Interface` instance.

f

[cursorTo](.././readline/~/cursorTo "cursorTo")

The `readline.cursorTo()` method moves cursor to the specified position in a given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) `stream`.

f

[emitKeypressEvents](.././readline/~/emitKeypressEvents "emitKeypressEvents")

The `readline.emitKeypressEvents()` method causes the given `Readable` stream to begin emitting `'keypress'` events corresponding to received input.

f

[moveCursor](.././readline/~/moveCursor "moveCursor")

The `readline.moveCursor()` method moves the cursor _relative_ to its current position in a given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) `stream`.

f

[promises.createInterface](.././readline/promises/~/promises.createInterface "promises.createInterface")

The `readlinePromises.createInterface()` method creates a new `readlinePromises.Interface` instance.

### Interfaces [#](#Interfaces)

I

[CursorPos](.././readline/~/CursorPos "CursorPos")

No documentation available

*   [cols](.././readline/~/CursorPos#property_cols)
*   [rows](.././readline/~/CursorPos#property_rows)

I

[Key](.././readline/~/Key "Key")

No documentation available

*   [ctrl](.././readline/~/Key#property_ctrl)
*   [meta](.././readline/~/Key#property_meta)
*   [name](.././readline/~/Key#property_name)
*   [sequence](.././readline/~/Key#property_sequence)
*   [shift](.././readline/~/Key#property_shift)

I

[promises.ReadLineOptions](.././readline/promises/~/promises.ReadLineOptions "promises.ReadLineOptions")

No documentation available

*   [completer](.././readline/promises/~/promises.ReadLineOptions#property_completer)

I

[ReadLineOptions](.././readline/~/ReadLineOptions "ReadLineOptions")

No documentation available

*   [completer](.././readline/~/ReadLineOptions#property_completer)
*   [crlfDelay](.././readline/~/ReadLineOptions#property_crlfdelay)
*   [escapeCodeTimeout](.././readline/~/ReadLineOptions#property_escapecodetimeout)
*   [history](.././readline/~/ReadLineOptions#property_history)
*   [historySize](.././readline/~/ReadLineOptions#property_historysize)
*   [input](.././readline/~/ReadLineOptions#property_input)
*   [output](.././readline/~/ReadLineOptions#property_output)
*   [prompt](.././readline/~/ReadLineOptions#property_prompt)
*   [removeHistoryDuplicates](.././readline/~/ReadLineOptions#property_removehistoryduplicates)
*   [signal](.././readline/~/ReadLineOptions#property_signal)
*   [tabSize](.././readline/~/ReadLineOptions#property_tabsize)
*   [terminal](.././readline/~/ReadLineOptions#property_terminal)

### Namespaces [#](#Namespaces)

N

[promises](.././readline/~/promises "promises")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[AsyncCompleter](.././readline/~/AsyncCompleter "AsyncCompleter")

No documentation available

T

[Completer](.././readline/~/Completer "Completer")

No documentation available

T

[CompleterResult](.././readline/~/CompleterResult "CompleterResult")

No documentation available

T

[Direction](.././readline/~/Direction "Direction")

No documentation available

T

[promises.Completer](.././readline/promises/~/promises.Completer "promises.Completer")

No documentation available

T

[ReadLine](.././readline/~/ReadLine "ReadLine")

No documentation available
