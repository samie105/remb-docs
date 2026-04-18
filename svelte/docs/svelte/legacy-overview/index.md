---
title: "Overview"
source: "https://svelte.dev/docs/svelte/legacy-overview"
canonical_url: "https://svelte.dev/docs/svelte/legacy-overview"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:41.918Z"
content_hash: "9d23c22cb01d56e15f3081d66280dfb5ebd86f6c223085fde39341501d15c7b4"
menu_path: ["Overview"]
section_path: []
---
Svelte 5 introduced some significant changes to Svelte's API, including [runes](what-are-runes), [snippets](snippet) and event attributes. As a result, some Svelte 3/4 features are deprecated (though supported for now, unless otherwise specified) and will eventually be removed. We recommend that you incrementally [migrate your existing code](v5-migration-guide).

The following pages document these features for

*   people still using Svelte 3/4
*   people using Svelte 5, but with components that haven't yet been migrated

Since Svelte 3/4 syntax still works in Svelte 5, we will distinguish between _legacy mode_ and _runes mode_. Once a component is in runes mode (which you can opt into by using runes, or by explicitly setting the `runes: true` compiler option), legacy mode features are no longer available.

If you're exclusively interested in the Svelte 3/4 syntax, you can browse its documentation at [v4.svelte.dev](https://v4.svelte.dev).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/00-legacy-overview.md) [llms.txt](/docs/svelte/legacy-overview/llms.txt)

previous next

[Runtime warnings](/docs/svelte/runtime-warnings) [Reactive let/var declarations](/docs/svelte/legacy-let)
