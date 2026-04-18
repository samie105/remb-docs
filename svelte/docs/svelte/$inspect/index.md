---
title: "$inspect"
source: "https://svelte.dev/docs/svelte/$inspect"
canonical_url: "https://svelte.dev/docs/svelte/$inspect"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:53.793Z"
content_hash: "1e2a154b84583edd68d50ace16b43db956c9462686c558fee38aeef2fc133915"
menu_path: ["$inspect"]
section_path: []
---
> `$inspect` only works during development. In a production build it becomes a noop.

The `$inspect` rune is roughly equivalent to `console.log`, with the exception that it will re-run whenever its argument changes. `$inspect` tracks reactive state deeply, meaning that updating something inside an object or array using fine-grained reactivity will cause it to re-fire:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA22Q0W6CQBBFf2UyMVHiBvqMQNLHfkNpwrqOuHGYJeygbQj_3ohaX_p8TmZO7oRiO8IcV15iT043aZomaPDomSLmnxPubaSH9N73abwQK6FBF0RJNGKORXSD77WqpVYmBRdGUShhFdUqbd6S3ZN0FKNt6cXWJ2IO68WQWv8ylhPm6Sc7yDK4emZwQWJgSjm0cD2RQLOoDYQBmofegDtZaamWInulSbEfVYNAEMfenctpk0BZ3Wu327n6EDdQR6JFdjerWgov_aiw93LIL5ZHKqfHkxmyCg3-N43St2Kuw0gG9ae_8dueOH8ZVOv56uWA-dFypPkX_VwbIYIBAAA)

```
<script>
	let count = $state(0);
	let message = $state('hello');

	$inspect(count, message); // will console.log when `count` or `message` change
</script>

<button onclick={() => count++}>Increment</button>
<input bind:value={message} />
```

```
<script lang="ts">
	let count = $state(0);
	let message = $state('hello');

	$inspect(count, message); // will console.log when `count` or `message` change
</script>

<button onclick={() => count++}>Increment</button>
<input bind:value={message} />
```

On updates, a stack trace will be printed, making it easy to find the origin of a state change (unless you're in the playground, due to technical limitations).

## $inspect(...).with[](#$inspect\(\).with)

`$inspect(...)` returns an object with a `with` method, which you can invoke with a callback that will then be invoked instead of `console.log`. The first argument to the callback is either `"init"` or `"update"`; subsequent arguments are the values passed to `$inspect`:

[Open in playground](/playground/untitled#H4sIAAAAAAAAA21Q0W6DMAz8FcuqVFAj2DMFpD3uG8akhuC20VIHJaasQvz7BHTby55s-e5055uQ9Y2wwJ3l2JORJMuyNButXNcNFZ6to4jF-4StjvSkv_Z9Fu_khFCh8SzEErHAMppge6kbbsSRgPEDC1Swi6KFkpf02PCC_dqthKdhIo-e1KZJoaphWqiN2DOsEFRVBfuh77TQPv1BG-moHS4XCkfIc_ABTsZz9I4yCdrQSS238aqF7hTg4QcYNcsmnpcxL6nK_C86l-0g4hk8G2fNZzUla5412eEw129sAt2Ipcw3Zo0K_6tG6EuwkDCQwuUFLNY-cf5QKNq60XKHxVm7SPM3eESCl4wBAAA)

```
<script>
	let count = $state(0);

	$inspect(count).with((type, count) => {
		if (type === 'update') {
			debugger; // or `console.trace`, or whatever you want
		}
	});
</script>

<button onclick={() => count++}>Increment</button>
```

```
<script lang="ts">
	let count = $state(0);

	$inspect(count).with((type, count) => {
		if (type === 'update') {
			debugger; // or `console.trace`, or whatever you want
		}
	});
</script>

<button onclick={() => count++}>Increment</button>
```

## $inspect.trace(...)[](#$inspect.trace\(\))

This rune, added in 5.14, causes the surrounding function to be _traced_ in development. Any time the function re-runs as part of an [effect]($effect) or a [derived]($derived), information will be printed to the console about which pieces of reactive state caused the effect to fire.

```
<script>
	import { doSomeWork } from './elsewhere';

	$effect(() => {
		// $inspect.trace must be the first statement of a function body
		$inspect.trace();
		doSomeWork();
	});
</script>
```

`$inspect.trace` takes an optional first argument which will be used as the label.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/02-runes/07-$inspect.md) [llms.txt](/docs/svelte/$inspect/llms.txt)

previous next

[$bindable](/docs/svelte/$bindable) [$host](/docs/svelte/$host)
