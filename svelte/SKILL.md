## Overview

Svelte is a compile-time framework that transforms declarative components into fine-grained, imperative DOM updates—eliminating the virtual DOM entirely. Agents must know it because its reactivity model is explicit and compiler-aware, using runes (`$state`, `$derived`, `$effect`) rather than runtime hooks or proxies, which produces minimal vanilla JavaScript and requires precise mental models to debug and extend.

## Mental Model

Reactivity in Svelte is block-scoped and explicit: `$state` declares reactive values, `$derived` computes reactive signals, and `$effect` handles side effects. The compiler statically analyzes these runes to inject granular update logic directly into the generated code, making the runtime nearly invisible. Canonical pages: `svelte/docs/svelte/$state/index.md`, `svelte/docs/svelte/$derived/index.md`, and `svelte/docs/svelte/$effect/index.md`.

## Learning Paths

**Getting Started**
1. `svelte/docs/svelte/$props/index.md` — Receive data from parent components.
2. `svelte/docs/svelte/$state/index.md` — Declare local reactive state.
3. `svelte/docs/svelte/$derived/index.md` — Compute values from state automatically.
4. `svelte/docs/svelte/$effect/index.md` — Manage side effects and lifecycle.

**Component Architecture**
1. `svelte/docs/svelte/$bindable/index.md` — Enable two-way binding for props.
2. `svelte/docs/svelte/$host/index.md` — Access custom-element host nodes.
3. `svelte/docs/svelte/custom-elements/index.md` — Compile to standard web components.
4. `svelte/docs/svelte/svelte-boundary/index.md` — Isolate and handle runtime errors.

**Template & Debugging Deep-Dive**
1. `svelte/docs/svelte/@html/index.md` — Safely inject raw HTML.
2. `svelte/docs/svelte/@const/index.md` — Define compile-time template constants.
3. `svelte/docs/svelte/$inspect/index.md` — Trace reactive state changes in development.
4. `svelte/docs/svelte/runtime-warnings/index.md` — Diagnose reactivity and binding warnings.

## Concept Map

- **Reactivity**
  - State → `svelte/docs/svelte/$state/index.md`
  - Derived signals → `svelte/docs/svelte/$derived/index.md`
  - Side effects → `svelte/docs/svelte/$effect/index.md`
  - Debugging → `svelte/docs/svelte/$inspect/index.md`
- **Data Flow**
  - Props → `svelte/docs/svelte/$props/index.md`
  - Two-way binding → `svelte/docs/svelte/$bindable/index.md`
  - Host element → `svelte/docs/svelte/$host/index.md`
- **Templating**
  - Raw HTML → `svelte/docs/svelte/@html/index.md`
  - Constants → `svelte/docs/svelte/@const/index.md`
  - Attachments → `svelte/docs/svelte/@attach/index.md`
  - Error boundaries → `svelte/docs/svelte/svelte-boundary/index.md`
- **Runtime**
  - Custom elements → `svelte/docs/svelte/custom-elements/index.md`
  - Error codes → `svelte/docs/svelte/runtime-errors/index.md`
  - Warning codes → `svelte/docs/svelte/runtime-warnings/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Declare reactive state | `svelte/docs/svelte/$state/index.md` |
| Compute a derived value | `svelte/docs/svelte/$derived/index.md` |
| Run side effects on state changes | `svelte/docs/svelte/$effect/index.md` |
| Pass data into a component | `svelte/docs/svelte/$props/index.md` |
| Allow two-way prop binding | `svelte/docs/svelte/$bindable/index.md` |
| Debug reactive values | `svelte/docs/svelte/$inspect/index.md` |
| Access a custom element host | `svelte/docs/svelte/$host/index.md` |
| Render raw HTML | `svelte/docs/svelte/@html/index.md` |
| Use compile-time template constants | `svelte/docs/svelte/@const/index.md` |
| Attach behavior to elements | `svelte/docs/svelte/@attach/index.md` |
| Build web components | `svelte/docs/svelte/custom-elements/index.md` |
| Catch component errors | `svelte/docs/svelte/svelte-boundary/index.md` |
| Understand runtime errors | `svelte/docs/svelte/runtime-errors/index.md` |
| Fix runtime warnings | `svelte/docs/svelte/runtime-warnings/index.md` |

## Top Must-Know Pages

1. `svelte/docs/svelte/$state/index.md` — Declares reactive values that drive all UI updates.
2. `svelte/docs/svelte/$props/index.md` — Defines the external inputs that configure a component.
3. `svelte/docs/svelte/$derived/index.md` — Computes read-only reactive values from other state.
4. `svelte/docs/svelte/$effect/index.md` — Executes imperative side effects after reactive state commits.
5. `svelte/docs/svelte/$bindable/index.md` — Marks props as two-way bindable for parent-child sync.
6. `svelte/docs/svelte/$inspect/index.md` — Development-only debugging tool for observing state changes.
7. `svelte/docs/svelte/@html/index.md` — Template syntax for rendering unescaped HTML content.
8. `svelte/docs/svelte/@const/index.md` — Declares block-scoped constants evaluated at compile time.
9. `svelte/docs/svelte/custom-elements/index.md` — Reference for compiling Svelte to standard web components.
10. `svelte/docs/svelte/svelte-boundary/index.md` — Error-boundary component for isolating runtime failures.