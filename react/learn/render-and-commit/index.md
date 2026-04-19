---
title: "Render and Commit"
source: "https://react.dev/learn/render-and-commit"
canonical_url: "https://react.dev/learn/render-and-commit"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:44.533Z"
content_hash: "85b7f286c0114d6c173a94d8bb8718947ae0b64086417229b74c59b185e91de6"
menu_path: ["Render and Commit"]
section_path: []
nav_prev: {"path": "react/learn/state-a-components-memory/index.md", "title": "State: A Component's Memory"}
nav_next: {"path": "react/learn/state-as-a-snapshot/index.md", "title": "State as a Snapshot"}
---

Before your components are displayed on screen, they must be rendered by React. Understanding the steps in this process will help you think about how your code executes and explain its behavior.

### You will learn

*   What rendering means in React
*   When and why React renders a component
*   The steps involved in displaying a component on screen
*   Why rendering does not always produce a DOM update

Imagine that your components are cooks in the kitchen, assembling tasty dishes from ingredients. In this scenario, React is the waiter who puts in requests from customers and brings them their orders. This process of requesting and serving UI has three steps:

1.  **Triggering** a render (delivering the guest’s order to the kitchen)
2.  **Rendering** the component (preparing the order in the kitchen)
3.  **Committing** to the DOM (placing the order on the table)

1.  ![React as a server in a restaurant, fetching orders from the users and delivering them to the Component Kitchen.](https://react.dev/images/docs/illustrations/i_render-and-commit1.png)
    
    Trigger
    
2.  ![The Card Chef gives React a fresh Card component.](https://react.dev/images/docs/illustrations/i_render-and-commit2.png)
    
    Render
    
3.  ![React delivers the Card to the user at their table.](https://react.dev/images/docs/illustrations/i_render-and-commit3.png)
    
    Commit
    

## Step 1: Trigger a render[](#step-1-trigger-a-render "Link for Step 1: Trigger a render ")

There are two reasons for a component to render:

1.  It’s the component’s **initial render.**
2.  The component’s (or one of its ancestors’) **state has been updated.**

### Initial render[](#initial-render "Link for Initial render ")

When your app starts, you need to trigger the initial render. Frameworks and sandboxes sometimes hide this code, but it’s done by calling [`createRoot`](https://react.dev/reference/react-dom/client/createRoot) with the target DOM node, and then calling its `render` method with your component:

Try commenting out the `root.render()` call and see the component disappear!

### Re-renders when state updates[](#re-renders-when-state-updates "Link for Re-renders when state updates ")

Once the component has been initially rendered, you can trigger further renders by updating its state with the [`set` function.](https://react.dev/reference/react/useState#setstate) Updating your component’s state automatically queues a render. (You can imagine these as a restaurant guest ordering tea, dessert, and all sorts of things after putting in their first order, depending on the state of their thirst or hunger.)

1.  ![React as a server in a restaurant, serving a Card UI to the user, represented as a patron with a cursor for their head. The patron expresses they want a pink card, not a black one!](https://react.dev/images/docs/illustrations/i_rerender1.png)
    
    State update...
    
2.  ![React returns to the Component Kitchen and tells the Card Chef they need a pink Card.](https://react.dev/images/docs/illustrations/i_rerender2.png)
    
    ...triggers...
    
3.  ![The Card Chef gives React the pink Card.](https://react.dev/images/docs/illustrations/i_rerender3.png)
    
    ...render!
    

## Step 2: React renders your components[](#step-2-react-renders-your-components "Link for Step 2: React renders your components ")

After you trigger a render, React calls your components to figure out what to display on screen. **“Rendering” is React calling your components.**

*   **On initial render,** React will call the root component.
*   **For subsequent renders,** React will call the function component whose state update triggered the render.

This process is recursive: if the updated component returns some other component, React will render _that_ component next, and if that component also returns something, it will render _that_ component next, and so on. The process will continue until there are no more nested components and React knows exactly what should be displayed on screen.

In the following example, React will call `Gallery()` and `Image()` several times:

*   **During the initial render,** React will [create the DOM nodes](https://developer.mozilla.org/docs/Web/API/Document/createElement) for `<section>`, `<h1>`, and three `<img>` tags.
*   **During a re-render,** React will calculate which of their properties, if any, have changed since the previous render. It won’t do anything with that information until the next step, the commit phase.

### Pitfall

Rendering must always be a [pure calculation](react/learn/keeping-components-pure/index.md):

*   **Same inputs, same output.** Given the same inputs, a component should always return the same JSX. (When someone orders a salad with tomatoes, they should not receive a salad with onions!)
*   **It minds its own business.** It should not change any objects or variables that existed before rendering. (One order should not change anyone else’s order.)

Otherwise, you can encounter confusing bugs and unpredictable behavior as your codebase grows in complexity. When developing in “Strict Mode”, React calls each component’s function twice, which can help surface mistakes caused by impure functions.

##### Deep Dive

#### Optimizing performance[](#optimizing-performance "Link for Optimizing performance ")

The default behavior of rendering all components nested within the updated component is not optimal for performance if the updated component is very high in the tree. If you run into a performance issue, there are several opt-in ways to solve it described in the [Performance](https://reactjs.org/docs/optimizing-performance.html) section. **Don’t optimize prematurely!**

## Step 3: React commits changes to the DOM[](#step-3-react-commits-changes-to-the-dom "Link for Step 3: React commits changes to the DOM ")

After rendering (calling) your components, React will modify the DOM.

*   **For the initial render,** React will use the [`appendChild()`](https://developer.mozilla.org/docs/Web/API/Node/appendChild) DOM API to put all the DOM nodes it has created on screen.
*   **For re-renders,** React will apply the minimal necessary operations (calculated while rendering!) to make the DOM match the latest rendering output.

**React only changes the DOM nodes if there’s a difference between renders.** For example, here is a component that re-renders with different props passed from its parent every second. Notice how you can add some text into the `<input>`, updating its `value`, but the text doesn’t disappear when the component re-renders:

This works because during this last step, React only updates the content of `<h1>` with the new `time`. It sees that the `<input>` appears in the JSX in the same place as last time, so React doesn’t touch the `<input>`—or its `value`!

## Epilogue: Browser paint[](#epilogue-browser-paint "Link for Epilogue: Browser paint ")

After rendering is done and React updated the DOM, the browser will repaint the screen. Although this process is known as “browser rendering”, we’ll refer to it as “painting” to avoid confusion throughout the docs.

![A browser painting 'still life with card element'.](https://react.dev/images/docs/illustrations/i_browser-paint.png)

## Recap[](#recap "Link for Recap")

*   Any screen update in a React app happens in three steps:
    1.  Trigger
    2.  Render
    3.  Commit
*   You can use Strict Mode to find mistakes in your components
*   React does not touch the DOM if the rendering result is the same as last time
