---
title: "{@debug ...}"
source: "https://svelte.dev/docs/svelte/@debug"
canonical_url: "https://svelte.dev/docs/svelte/@debug"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:26.634Z"
content_hash: "f35384a260b70828b32f201ec00a2554565b4f1b09ddb752b3882fb019528811"
menu_path: ["{@debug ...}"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/@const/index.md", "title": "{@const ...}"}
nav_next: {"path": "svelte/docs/svelte/bind/index.md", "title": "bind:"}
---

The `{@debug ...}` tag offers an alternative to `console.log(...)`. It logs the values of specific variables whenever they change, and pauses code execution if you have devtools open.

```
<script>
	let user = {
		firstname: 'Ada',
		lastname: 'Lovelace'
	};
</script>

{@debug user}

<h1>Hello {user.firstname}!</h1>
```

`{@debug ...}` accepts a comma-separated list of variable names (not arbitrary expressions).

```
<!-- Compiles -->
{@debug user}
{@debug user1, user2, user3}

<!-- WON'T compile -->
{@debug user.firstname}
{@debug myArray[0]}
{@debug !isReady}
{@debug typeof user === 'object'}
```

The `{@debug}` tag without any arguments will insert a `debugger` statement that gets triggered when _any_ state changes, as opposed to the specified variables.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/11-@debug.md) [llms.txt](/docs/svelte/@debug/llms.txt)

previous next

[{@const ...}](/docs/svelte/@const) [bind:](/docs/svelte/bind)
