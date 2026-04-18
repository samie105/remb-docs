---
title: "svelte/reactivity/window"
source: "https://svelte.dev/docs/svelte/svelte-reactivity-window"
canonical_url: "https://svelte.dev/docs/svelte/svelte-reactivity-window"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:51.969Z"
content_hash: "65c12fd560fb0bc771c62494cb57fac26770e4233a67f5ace1700f174d9e3562"
menu_path: ["svelte/reactivity/window"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/svelte-motion/index.md", "title": "svelte/motion"}
nav_next: {"path": "svelte/docs/svelte/svelte-reactivity/index.md", "title": "svelte/reactivity"}
---

This module exports reactive versions of various `window` values, each of which has a reactive `current` property that you can reference in reactive contexts (templates, [deriveds]($derived) and [effects]($effect)) without using [`<svelte:window>`](svelte-window) bindings or manually creating your own event listeners.

```
<script>
	import { innerWidth, innerHeight } from 'svelte/reactivity/window';
</script>

<p>{innerWidth.current}x{innerHeight.current}</p>
```

```
import {
	const devicePixelRatio: {
    readonly current: number | undefined;
}devicePixelRatio.current is a reactive view of window.devicePixelRatio. On the server it is undefined.
Note that behaviour differs between browsers — on Chrome it will respond to the current zoom level,
on Firefox and Safari it won't.
@since5.11.0referencedevicePixelRatio,
	const innerHeight: ReactiveValue<number | undefined>innerHeight.current is a reactive view of window.innerHeight. On the server it is undefined.
@since5.11.0referenceinnerHeight,
	const innerWidth: ReactiveValue<number | undefined>innerWidth.current is a reactive view of window.innerWidth. On the server it is undefined.
@since5.11.0referenceinnerWidth,
	const online: ReactiveValue<boolean | undefined>online.current is a reactive view of navigator.onLine. On the server it is undefined.
@since5.11.0referenceonline,
	const outerHeight: ReactiveValue<number | undefined>outerHeight.current is a reactive view of window.outerHeight. On the server it is undefined.
@since5.11.0referenceouterHeight,
	const outerWidth: ReactiveValue<number | undefined>outerWidth.current is a reactive view of window.outerWidth. On the server it is undefined.
@since5.11.0referenceouterWidth,
	const screenLeft: ReactiveValue<number | undefined>screenLeft.current is a reactive view of window.screenLeft. It is updated inside a requestAnimationFrame callback. On the server it is undefined.
@since5.11.0referencescreenLeft,
	const screenTop: ReactiveValue<number | undefined>screenTop.current is a reactive view of window.screenTop. It is updated inside a requestAnimationFrame callback. On the server it is undefined.
@since5.11.0referencescreenTop,
	const scrollX: ReactiveValue<number | undefined>scrollX.current is a reactive view of window.scrollX. On the server it is undefined.
@since5.11.0referencescrollX,
	const scrollY: ReactiveValue<number | undefined>scrollY.current is a reactive view of window.scrollY. On the server it is undefined.
@since5.11.0referencescrollY
} from 'svelte/reactivity/window';
```

## devicePixelRatio[](#devicePixelRatio)

> Available since 5.11.0

`devicePixelRatio.current` is a reactive view of `window.devicePixelRatio`. On the server it is `undefined`. Note that behaviour differs between browsers — on Chrome it will respond to the current zoom level, on Firefox and Safari it won't.

```
const devicePixelRatio: {
	get current(): number | undefined;
};
```

## innerHeight[](#innerHeight)

> Available since 5.11.0

`innerHeight.current` is a reactive view of `window.innerHeight`. On the server it is `undefined`.

```
const innerHeight: ReactiveValue<number | undefined>;
```

## innerWidth[](#innerWidth)

> Available since 5.11.0

`innerWidth.current` is a reactive view of `window.innerWidth`. On the server it is `undefined`.

```
const innerWidth: ReactiveValue<number | undefined>;
```

## online[](#online)

> Available since 5.11.0

`online.current` is a reactive view of `navigator.onLine`. On the server it is `undefined`.

```
const online: ReactiveValue<boolean | undefined>;
```

## outerHeight[](#outerHeight)

> Available since 5.11.0

`outerHeight.current` is a reactive view of `window.outerHeight`. On the server it is `undefined`.

```
const outerHeight: ReactiveValue<number | undefined>;
```

## outerWidth[](#outerWidth)

> Available since 5.11.0

`outerWidth.current` is a reactive view of `window.outerWidth`. On the server it is `undefined`.

```
const outerWidth: ReactiveValue<number | undefined>;
```

## screenLeft[](#screenLeft)

> Available since 5.11.0

`screenLeft.current` is a reactive view of `window.screenLeft`. It is updated inside a `requestAnimationFrame` callback. On the server it is `undefined`.

```
const screenLeft: ReactiveValue<number | undefined>;
```

## screenTop[](#screenTop)

> Available since 5.11.0

`screenTop.current` is a reactive view of `window.screenTop`. It is updated inside a `requestAnimationFrame` callback. On the server it is `undefined`.

```
const screenTop: ReactiveValue<number | undefined>;
```

## scrollX[](#scrollX)

> Available since 5.11.0

`scrollX.current` is a reactive view of `window.scrollX`. On the server it is `undefined`.

```
const scrollX: ReactiveValue<number | undefined>;
```

## scrollY[](#scrollY)

> Available since 5.11.0

`scrollY.current` is a reactive view of `window.scrollY`. On the server it is `undefined`.

```
const scrollY: ReactiveValue<number | undefined>;
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/98-reference/21-svelte-reactivity-window.md) [llms.txt](/docs/svelte/svelte-reactivity-window/llms.txt)

previous next

[svelte/motion](/docs/svelte/svelte-motion) [svelte/reactivity](/docs/svelte/svelte-reactivity)
