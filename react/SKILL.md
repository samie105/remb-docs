# React Developer Agent Skill

React is a popular JavaScript library for building user interfaces with reusable, composable components. It solves problems of complex UI state, efficient DOM updates, and helps structure frontend code into manageable, isolated building blocks. These docs provide step-by-step guidance, conceptual overviews, and practical recipes for scaling from a quick demo to large production apps.

---

## Key Concepts

- **Components**: Modular, reusable pieces of UI built as JavaScript functions or classes.
- **JSX**: A syntax extension that lets you write HTML-like markup in JavaScript.
- **Props**: Data passed from parent to child components to configure or display information.
- **State**: Internal data managed by a component that triggers UI updates when changed.
- **Hooks**: Functions (like `useState`, `useEffect`) to add React features to function components.
- **Event Handling**: Wiring up user interactions (keyboard, mouse, etc.) to your app logic.
- **Conditional Rendering**: Showing different UI based on application state.
- **Lists and Keys**: Dynamically rendering arrays of components efficiently.
- **Effects**: Side effects (e.g. data fetching, subscriptions) tied to the component lifecycle.
- **Refs**: Direct access to DOM nodes or React elements for imperative actions.
- **Context**: Mechanism to share data (like themes, current user) deeply throughout the component tree.
- **Reducers**: Advanced state logic management pattern, especially for complex or scoped state.
- **React Compiler**: Upcoming tool for optimizing and transforming React code.

---

## Navigation Guide

**For Beginners or New Projects:**
- See **Quick Start** or the **Tutorial: Tic-Tac-Toe**.
- Use **Creating a React App** or **Build a React App from Scratch** for setup advice.

**For Integrating or Migrating:**
- Find steps in **Add React to an Existing Project**.
- Tooling info in **Setup**, **Editor Setup**, and **Using TypeScript**.

**Core Learning / Concepts:**
- Start at **Thinking in React** for mental models and component design.
- Dive into chapters like **Describing the UI**, **Writing Markup with JSX**, **Passing Props**, **State**, and **Managing State**.
- Use **Escape Hatches** and **Refs** for advanced/interoperability use cases.

**API Details & Troubleshooting:**
- Look to specific concept pages (e.g., **Conditional Rendering**, **Rendering Lists**, **Synchronizing with Effects**).
- Check **React Developer Tools** for debugging help.
- Explore **React Compiler** if optimizing or investigating React's build process.

---

## Top 15 Essential Documentation Pages

1. **[Quick Start](react/learn/index.md)**  
   Learn core React concepts and quickly build your first component.

2. **[Tutorial: Tic-Tac-Toe](react/learn/tutorial-tic-tac-toe/index.md)**  
   Step-by-step tutorial for fundamentals through a hands-on example.

3. **[Thinking in React](react/learn/thinking-in-react/index.md)**  
   How to break UIs into components and accurately map designs to React.

4. **[Installation](react/learn/installation/index.md)**  
   Options for installing React in different environments and projects.

5. **[Creating a React App](react/learn/creating-a-react-app/index.md)**  
   Recommended ways to scaffold new React apps using popular frameworks.

6. **[Build a React App from Scratch](react/learn/build-a-react-app-from-scratch/index.md)**  
   Guide for manual app setup without using frameworks.

7. **[Add React to an Existing Project](react/learn/add-react-to-an-existing-project/index.md)**  
   Instructions for adding React incrementally to non-React codebases.

8. **[Describing the UI](react/learn/describing-the-ui/index.md)**  
   Underlying principles for modeling UIs as components.

9. **[Writing Markup with JSX](react/learn/writing-markup-with-jsx/index.md)**  
   JSX syntax and best practices for writing component markup.

10. **[Passing Props to a Component](react/learn/passing-props-to-a-component/index.md)**  
    How to pass and use inputs/parameters in components.

11. **[State: A Component's Memory](react/learn/state-a-components-memory/index.md)**  
    How React components store and update internal data.

12. **[Managing State](react/learn/managing-state/index.md)**  
    Techniques for state management as applications grow larger.

13. **[Sharing State Between Components](react/learn/sharing-state-between-components/index.md)**  
    Patterns for passing and synchronizing data across components.

14. **[Synchronizing with Effects](react/learn/synchronizing-with-effects/index.md)**  
    Using `useEffect` for tasks linked to component lifecycle or external systems.

15. **[React Developer Tools](react/learn/react-developer-tools/index.md)**  
    Tools and extensions for inspecting and debugging React apps.

---

## Notable Gotchas & Structure Quirks

- **Incremental Learning**: Docs are intentionally progressive, from "hello world" up to advanced architecture.
- **Multiple Entry Paths**: Several install and setup guides—choose based on goals (from scratch, existing project, framework, etc.).
- **Escape Hatches**: Low-level sections exist for direct DOM access or integration with third-party libraries.
- **Compiler Section**: The "React Compiler" section covers experimental/newer features and optimization tooling—distinct from core React runtime.
- **TypeScript**: Only one dedicated high-level doc, but most code in general docs is JS-first; refer to [Using TypeScript](react/learn/typescript/index.md) for integration notes.

---

Use the above sections, and refer to the linked paths when answering developer questions to ensure high-accuracy, context-aware React support.