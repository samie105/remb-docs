---
title: "svelte/animate"
source: "https://svelte.dev/docs/svelte/svelte-animate"
canonical_url: "https://svelte.dev/docs/svelte/svelte-animate"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:25.792Z"
content_hash: "fd7cbd20757491f0e769ee8ab3d085cfe5d597d55a22d3078cfb5ada045cdaae"
menu_path: ["svelte/animate"]
section_path: []
---
```
import { function flip(node: Element, { from, to }: {
    from: DOMRect;
    to: DOMRect;
}, params?: FlipParams): AnimationConfigThe flip function calculates the start and end position of an element and animates between them, translating the x and y values.
flip stands for First, Last, Invert, Play.
referenceflip } from 'svelte/animate';
```

## flip[](#flip)

The flip function calculates the start and end position of an element and animates between them, translating the x and y values. `flip` stands for [First, Last, Invert, Play](https://aerotwist.com/blog/flip-your-animations/).

```
function flip(
	node: Element,
	{
		from,
		to
	}: {
		from: DOMRect;
		to: DOMRect;
	},
	params?: FlipParams
): AnimationConfig;
```

## AnimationConfig[](#AnimationConfig)

```
interface AnimationConfig {…}
```

```
delay?: number;
```

```
duration?: number;
```

```
easing?: (t: number) => number;
```

```
css?: (t: number, u: number) => string;
```

```
tick?: (t: number, u: number) => void;
```

## FlipParams[](#FlipParams)

```
interface FlipParams {…}
```

```
delay?: number;
```

```
duration?: number | ((len: number) => number);
```

```
easing?: (t: number) => number;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-animate.md) [llms.txt](/docs/svelte/svelte-animate/llms.txt)

previous next

[svelte/action](/docs/svelte/svelte-action) [svelte/attachments](/docs/svelte/svelte-attachments)
