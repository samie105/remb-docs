---
title: "What are runes?"
source: "https://svelte.dev/docs/svelte/what-are-runes"
canonical_url: "https://svelte.dev/docs/svelte/what-are-runes"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:25.107Z"
content_hash: "9f95ac6a5aa0e838b1cdff7a2f503efb35edd536f84651b52a236128c28cf22c"
menu_path: ["What are runes?"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-js-files/index.md", "title": ".svelte.js and .svelte.ts files"}
nav_next: {"path": "svelte/docs/svelte/$state/index.md", "title": "$state"}
---

> **rune** /ruːn/ _noun_
> 
> A letter or mark used as a mystical or magic symbol.

Runes are symbols that you use in `.svelte` and `.svelte.js` / `.svelte.ts` files to control the Svelte compiler. If you think of Svelte as a language, runes are part of the syntax — they are _keywords_.

Runes have a `$` prefix and look like functions:

```
let let message: stringmessage = function $state<"hello">(initial: "hello"): "hello" (+1 overload)
namespace $stateDeclares reactive state.
Example:
let count = $state(0);@see{@link https://svelte.dev/docs/svelte/$state Documentation}@paraminitial The initial value$state('hello');
```

They differ from normal JavaScript functions in important ways, however:

*   You don't need to import them — they are part of the language
*   They're not values — you can't assign them to a variable or pass them as arguments to a function
*   Just like JavaScript keywords, they are only valid in certain positions (the compiler will help you if you put them in the wrong place)

> Legacy mode
> 
> Runes didn't exist prior to Svelte 5.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/02-runes/01-what-are-runes.md) [llms.txt](/docs/svelte/what-are-runes/llms.txt)

previous next

[.svelte.js and .svelte.ts files](/docs/svelte/svelte-js-files) [$state](/docs/svelte/$state)

