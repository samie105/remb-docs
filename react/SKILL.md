**Overview**

React is a declarative library for building user interfaces from encapsulated, reusable components. An agent needs to know it because modern frontend architecture is component-driven, and React’s unidirectional data flow, snapshot-based state, and explicit effects model dominate how interactive UIs are engineered.

**Mental Model**

React treats UI as a pure function of state: components return a description of what should appear, and React reconciles changes through a render-and-commit cycle. State is local and flows down via props, while side effects are isolated into event handlers or Effects. Canonical pages: `react/learn/describing-the-ui/index.md`, `react/learn/state-a-components-memory/index.md`, `react/learn/render-and-commit/index.md`, `react/learn/keeping-components-pure/index.md`.

**Learning Paths**

*Getting Started*
1. `react/learn/installation/index.md`
2. `react/learn/your-first-component/index.md`
3. `react/learn/describing-the-ui/index.md`
4. `react/learn/adding-interactivity/index.md`
5. `react/learn/state-a-components-memory/index.md`

*Production Ready*
1. `react/learn/choosing-the-state-structure/index.md`
2. `react/learn/synchronizing-with-effects/index.md`
3. `react/learn/you-might-not-need-an-effect/index.md`
4. `react/learn/referencing-values-with-refs/index.md`
5. `react/learn/manipulating-the-dom-with-refs/index.md`

*Reference Deep-Dive*
1. `react/learn/render-and-commit/index.md`
2. `react/learn/keeping-components-pure/index.md`
3. `react/learn/react-compiler/index.md`
4. `react/learn/react-compiler/incremental-adoption/index.md`
5. `react/learn/react-compiler/debugging/index.md`

**Concept Map**

- UI Description
  - JSX: `react/learn/writing-markup-with-jsx/index.md`
  - Components: `react/learn/your-first-component/index.md`
  - Props: `react/learn/passing-props-to-a-component/index.md`
  - Conditional Rendering: `react/learn/conditional-rendering/index.md`
  - Lists: `react/learn/rendering-lists/index.md`
- State & Data Flow
  - Component Memory: `react/learn/state-a-components-memory/index.md`
  - Snapshot Semantics: `react/learn/state-as-a-snapshot/index.md`
  - State Structure: `react/learn/choosing-the-state-structure/index.md`
  - Preserving State: `react/learn/preserving-and-resetting-state/index.md`
  - Context: `react/learn/passing-data-deeply-with-context/index.md`
- Interactivity & Effects
  - Events: `react/learn/responding-to-events/index.md`
  - Effects: `react/learn/synchronizing-with-effects/index.md`
  - Unnecessary Effects: `react/learn/you-might-not-need-an-effect/index.md`
  - Refs: `react/learn/referencing-values-with-refs/index.md`
  - DOM Manipulation: `react/learn/manipulating-the-dom-with-refs/index.md`
- Architecture
  - Purity: `react/learn/keeping-components-pure/index.md`
  - Render & Commit: `react/learn/render-and-commit/index.md`
  - React Compiler: `react/learn/react-compiler/index.md`

**If You Need To...**

| If you need to... | read |
|---|---|
| Bootstrap a new project | `react/learn/creating-a-react-app/index.md` |
| Add React to an existing site | `react/learn/add-react-to-an-existing-project/index.md` |
| Understand how state updates work | `react/learn/render-and-commit/index.md` |
| Handle user input | `react/learn/responding-to-events/index.md` |
| Run side effects safely | `react/learn/synchronizing-with-effects/index.md` |
| Avoid redundant state | `react/learn/choosing-the-state-structure/index.md` |
| Access DOM nodes directly | `react/learn/manipulating-the-dom-with-refs/index.md` |
| Optimize re-renders | `react/learn/react-compiler/index.md` |
| Pass data deeply without prop drilling | `react/learn/passing-data-deeply-with-context/index.md` |
| Reset component state on navigation | `react/learn/preserving-and-resetting-state/index.md` |

**Top Must-Know Pages**

1. `react/learn/describing-the-ui/index.md` — Core concepts for expressing UI through components, JSX, and props.
2. `react/learn/state-a-components-memory/index.md` — How components remember values across renders using `useState`.
3. `react/learn/render-and-commit/index.md` — The three-phase cycle that translates state changes into DOM updates.
4. `react/learn/keeping-components-pure/index.md` — Why components must act as pure functions and how to avoid side effects during render.
5. `react/learn/synchronizing-with-effects/index.md` — How to safely run side effects outside the render flow.
6. `react/learn/you-might-not-need-an-effect/index.md` — Patterns for deriving state and avoiding unnecessary effect logic.
7. `react/learn/choosing-the-state-structure/index.md` — Principles for organizing state to minimize bugs and complexity.
8. `react/learn/responding-to-events/index.md` — Handling user interactions via event handlers in React.
9. `react/learn/react-compiler/index.md` — Automated memoization and optimization through the React Compiler.
10. `react/learn/adding-interactivity/index.md` — Fundamentals of making components respond to user input and update state.