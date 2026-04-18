---
title: "Reactive $: statements"
source: "https://svelte.dev/docs/svelte/legacy-reactive-assignments"
canonical_url: "https://svelte.dev/docs/svelte/legacy-reactive-assignments"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:09.534Z"
content_hash: "327230528a5b6d6d6415870ca0c20f5958888eb291caea1369340a4168b54f76"
menu_path: ["Reactive $: statements"]
section_path: []
---
In runes mode, reactions to state updates are handled with the [`$derived`]($derived) and [`$effect`]($effect) runes.

In legacy mode, any top-level statement (i.e. not inside a block or a function) can be made reactive by prefixing it with a `$:` [label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label). These statements run after other code in the `<script>` and before the component markup is rendered, then whenever the values that they depend on change.

```
<script>
	let a = 1;
	let b = 2;

	// this is a 'reactive statement', and it will re-run
	// when `a`, `b` or `sum` change
	$: console.log(`${a} + ${b} = ${sum}`);

	// this is a 'reactive assignment' — `sum` will be
	// recalculated when `a` or `b` change. It is
	// not necessary to declare `sum` separately
	$: sum = a + b;
</script>
```

Statements are ordered _topologically_ by their dependencies and their assignments: since the `console.log` statement depends on `sum`, `sum` is calculated first even though it appears later in the source.

Multiple statements can be combined by putting them in a block:

```
$: {
	// recalculate `total` when `items` changes
	total = 0;

	for (const const item: anyitem of items) {
		total += const item: anyitem.value;
	}
}
```

The left-hand side of a reactive assignments can be an identifier, or it can be a destructuring assignment:

```
$: ({ larry: anylarry, moe: anymoe, curly: anycurly } = stooges);
```

## Understanding dependencies[](#Understanding-dependencies)

The dependencies of a `$:` statement are determined at compile time — they are whichever variables are referenced (but not assigned to) inside the statement.

In other words, a statement like this will _not_ re-run when `count` changes, because the compiler cannot 'see' the dependency:

```
let let count: numbercount = 0;
let let double: () => numberdouble = () => let count: numbercount * 2;

$: doubled = let double: () => numberdouble();
```

Similarly, topological ordering will fail if dependencies are referenced indirectly: `z` will never update, because `y` is not considered 'dirty' when the update occurs. Moving `$: z = y` below `$: setY(x)` will fix it:

```
<script>
	let x = 0;
	let y = 0;

	$: z = y;
	$: setY(x);

	function setY(value) {
		y = value;
	}
</script>
```

## Browser-only code[](#Browser-only-code)

Reactive statements run during server-side rendering as well as in the browser. This means that any code that should only run in the browser must be wrapped in an `if` block:

```
$: if (browser) {
	var document: Documentwindow.document returns a reference to the document contained in the window.
MDN Reference
document.Document.title: stringThe document.title property gets or sets the current title of the document.
MDN Reference
title = title;
}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/02-legacy-reactive-assignments.md) [llms.txt](/docs/svelte/legacy-reactive-assignments/llms.txt)

previous next

[Reactive let/var declarations](/docs/svelte/legacy-let) [export let](/docs/svelte/legacy-export-let)
