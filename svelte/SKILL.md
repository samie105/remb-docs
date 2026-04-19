# Svelte Developer Agent Skill Guide

## Overview

Svelte is a compiler-based framework for building high-performance, reactive user interfaces using a declarative, component-driven model. Unlike traditional frameworks, Svelte shifts much of the work to compile-time, resulting in minimal runtime and highly-optimized JavaScript for the browser. It leverages a unique syntax with runes and features designed for simplicity and great DX.

---

## Key Concepts

- **Svelte Components**: Encapsulated UI logic, markup, and styles in `.svelte` files. The primary unit of reuse.
- **Runes**: Special compiler directives (e.g., `$state`, `$derived`, `$effect`) enabling reactivity and interactivity within Svelte files and modules.
- **Reactivity**: Automatic UI updates in response to state changes, facilitated by runes and Svelte's compiler.
- **Bindings**: Mechanism for two-way data flow between components and DOM elements (`bind:` and `$bindable`).
- **Context**: Enables passing data deeply through the component tree without prop-drilling.
- **Lifecycle Hooks**: Functions that run at specific points in a component's lifespan, for side-effects and resource management.
- **Svelte Directives**: Custom templating constructs for logic, DOM interaction, transitions, and more (`{#if ...}`, `bind:`, `use:`, etc.).
- **Scoped and Global Styles**: CSS can be scoped to components or made global as needed.
- **Hydration**: Support for server-rendered content and seamless client bootstrapping.
- **Migration**: Guides available for upgrading between major Svelte versions (v4 → v5, etc.).

---

## Documentation Navigation Guide

- **Core Concepts & Getting Started**  
  Start with [Overview](svelte/docs/svelte/overview/index.md) and [Getting started](svelte/docs/svelte/getting-started/index.md).
- **Component Authoring**  
  See [`.svelte files`](svelte/docs/svelte/svelte-files/index.md), [Runes](svelte/docs/svelte/what-are-runes/index.md), and all `$rune` pages for reactivity and patterns.
- **Templating & Directives**  
  Blocks like `{#if ...}`, `{#each ...}`, `{#await ...}` and directives like `bind:`, `use:`, `class`, `style:`.
- **Styling**  
  [Scoped styles](svelte/docs/svelte/scoped-styles/index.md), [Global styles](svelte/docs/svelte/global-styles/index.md), [Nested `<style>` elements](svelte/docs/svelte/nested-style-elements/index.md).
- **Component Communication**  
  [Props](svelte/docs/svelte/$props/index.md), [$bindable](svelte/docs/svelte/$bindable/index.md), and [Context](svelte/docs/svelte/context/index.md).
- **State Management**  
  Check [Stores](svelte/docs/svelte/stores/index.md) for shared/global state.
- **API Reference**  
  For programmatic use, consult the `svelte/` namespace pages (e.g., [svelte/store](svelte/docs/svelte/svelte-store/index.md), [svelte/compiler](svelte/docs/svelte/svelte-compiler/index.md)).
- **Migration**  
  Major upgrade details in [Svelte 4 migration guide](svelte/docs/svelte/v4-migration-guide/index.md) and [Svelte 5 migration guide](svelte/docs/svelte/v5-migration-guide/index.md).
- **Troubleshooting**  
  Errors and warnings in [Compiler errors](svelte/docs/svelte/compiler-errors/index.md), [Runtime errors](svelte/docs/svelte/runtime-errors/index.md), and [FAQ](svelte/docs/svelte/faq/index.md).

---

## Top 15 Essential Pages

1. **[Overview](svelte/docs/svelte/overview/index.md)**  
   Core framework introduction and philosophy.

2. **[Getting started](svelte/docs/svelte/getting-started/index.md)**  
   Quickstart instructions, project creation, and tooling setup.

3. **[.svelte files](svelte/docs/svelte/svelte-files/index.md)**  
   Structure and conventions for Svelte component files.

4. **[What are runes?](svelte/docs/svelte/what-are-runes/index.md)**  
   In-depth explanation of Svelte's reactive syntax (runes).

5. **[$state](svelte/docs/svelte/$state/index.md)**  
   How to declare and use reactive local state in components.

6. **[$derived](svelte/docs/svelte/$derived/index.md)**  
   Creating derived values that automatically update.

7. **[$effect](svelte/docs/svelte/$effect/index.md)**  
   Running side-effects in response to reactive state changes.

8. **[bind:](svelte/docs/svelte/bind/index.md)**  
   Syntax for binding component state to DOM/input values.

9. **[Stores](svelte/docs/svelte/stores/index.md)**  
   Managing shared/global reactive state with stores.

10. **[Context](svelte/docs/svelte/context/index.md)**  
    Mechanism for sharing data hierarchically among components.

11. **[Scoped styles](svelte/docs/svelte/scoped-styles/index.md)**  
    Component-local CSS and style encapsulation.

12. **[{#if ...}](svelte/docs/svelte/if/index.md)**  
    Conditional rendering blocks.

13. **[{#each ...}](svelte/docs/svelte/each/index.md)**  
    List rendering and iteration.

14. **[Svelte 5 migration guide](svelte/docs/svelte/v5-migration-guide/index.md)**  
    Key differences from prior releases; must-read for upgraders.

15. **[Compiler errors](svelte/docs/svelte/compiler-errors/index.md)**  
    Reference for Svelte compilation errors and common resolutions.

**Other valuable pages depending on context:**
- [TypeScript](svelte/docs/svelte/typescript/index.md) — Svelte + TS usage.
- [Best practices](svelte/docs/svelte/best-practices/index.md) — Idiomatic Svelte advice.
- [Testing](svelte/docs/svelte/testing/index.md)
- [FAQ](svelte/docs/svelte/faq/index.md)

---

## Notable Gotchas & Structure Notes

- **Runes** are the new official way to express reactivity in Svelte 5+, replacing older `$:` and `export let` mechanisms. See [What are runes?](svelte/docs/svelte/what-are-runes/index.md) and each `$rune` page (e.g. `$state`, `$effect`).
- **Error and Warning pages** are comprehensive but split by phase: compiler/runtime and errors/warnings. Check the right one based on the message.
- **Migration Guides** are split by version. Use them when updating or maintaining older code, as many API/behavior changes are version-specific.
- **Legacy/Old API Pages**: Anything in files starting with `legacy-` covers behavior prior to Svelte 5. For new projects, prioritize rune-based patterns unless maintaining old code.
- **Hydratable data**: Hydration is handled differently; see [Hydratable data](svelte/docs/svelte/hydratable/index.md) for SSR pitfalls.
- **Debugging**: Use [$inspect](svelte/docs/svelte/$inspect/index.md) and [{@debug ...}](svelte/docs/svelte/@debug/index.md) for reactive debugging in dev.
- **Directive Reference**: Template blocks (e.g., `{#if ...}`, `{#each ...}`) and DOM directives (`bind:`, `use:`, `class`) each have their own page for details and caveats.
- **Single `<style>` Tag Rule**: Only one top-level `<style>` tag per component ([Nested <style> elements](svelte/docs/svelte/nested-style-elements/index.md)).

---

For any task, begin with the conceptual intro, consult the relevant `$rune` or directive page, and, for advanced or unexpected issues, review migration guides and error/warning documentation. This structure ensures efficient doc lookup and rapid Svelte problem-solving.