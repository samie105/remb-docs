---
title: "Describing the UI"
source: "https://react.dev/learn/describing-the-ui"
canonical_url: "https://react.dev/learn/describing-the-ui"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:53.182Z"
content_hash: "6917b63516fcbba17d3251da781741b8a8eff9689666f8a172d5a78539f64faf"
menu_path: ["Describing the UI"]
section_path: []
nav_prev: {"path": "react/learn/react-compiler/debugging/index.md", "title": "Debugging and Troubleshooting"}
nav_next: {"path": "react/learn/your-first-component/index.md", "title": "Your First Component"}
---

React is a JavaScript library for rendering user interfaces (UI). UI is built from small units like buttons, text, and images. React lets you combine them into reusable, nestable _components._ From web sites to phone apps, everything on the screen can be broken down into components. In this chapter, you’ll learn to create, customize, and conditionally display React components.

## Your first component[](#your-first-component "Link for Your first component ")

React applications are built from isolated pieces of UI called _components_. A React component is a JavaScript function that you can sprinkle with markup. Components can be as small as a button, or as large as an entire page. Here is a `Gallery` component rendering three `Profile` components:

* * *

## Importing and exporting components[](#importing-and-exporting-components "Link for Importing and exporting components ")

You can declare many components in one file, but large files can get difficult to navigate. To solve this, you can _export_ a component into its own file, and then _import_ that component from another file:

* * *

## Writing markup with JSX[](#writing-markup-with-jsx "Link for Writing markup with JSX ")

Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information.

If we paste existing HTML markup into a React component, it won’t always work:

If you have existing HTML like this, you can fix it using a [converter](https://transform.tools/html-to-jsx):

* * *

## JavaScript in JSX with curly braces[](#javascript-in-jsx-with-curly-braces "Link for JavaScript in JSX with curly braces ")

JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to “open a window” to JavaScript:

* * *

## Passing props to a component[](#passing-props-to-a-component "Link for Passing props to a component ")

React components use _props_ to communicate with each other. Every parent component can pass some information to its child components by giving them props. Props might remind you of HTML attributes, but you can pass any JavaScript value through them, including objects, arrays, functions, and even JSX!

* * *

## Conditional rendering[](#conditional-rendering "Link for Conditional rendering ")

Your components will often need to display different things depending on different conditions. In React, you can conditionally render JSX using JavaScript syntax like `if` statements, `&&`, and `? :` operators.

In this example, the JavaScript `&&` operator is used to conditionally render a checkmark:

* * *

## Rendering lists[](#rendering-lists "Link for Rendering lists ")

You will often want to display multiple similar components from a collection of data. You can use JavaScript’s `filter()` and `map()` with React to filter and transform your array of data into an array of components.

For each array item, you will need to specify a `key`. Usually, you will want to use an ID from the database as a `key`. Keys let React keep track of each item’s place in the list even if the list changes.

## Ready to learn this topic?

Read **[Rendering Lists](react/learn/rendering-lists/index.md)** to learn how to render a list of components, and how to choose a key.

[Read More](react/learn/rendering-lists/index.md)

* * *

## Keeping components pure[](#keeping-components-pure "Link for Keeping components pure ")

Some JavaScript functions are _pure._ A pure function:

*   **Minds its own business.** It does not change any objects or variables that existed before it was called.
*   **Same inputs, same output.** Given the same inputs, a pure function should always return the same result.

By strictly only writing your components as pure functions, you can avoid an entire class of baffling bugs and unpredictable behavior as your codebase grows. Here is an example of an impure component:

You can make this component pure by passing a prop instead of modifying a preexisting variable:

* * *

## Your UI as a tree[](#your-ui-as-a-tree "Link for Your UI as a tree ")

React uses trees to model the relationships between components and modules.

A React render tree is a representation of the parent and child relationship between components.

![A tree graph with five nodes, with each node representing a component. The root node is located at the top the tree graph and is labelled 'Root Component'. It has two arrows extending down to two nodes labelled 'Component A' and 'Component C'. Each of the arrows is labelled with 'renders'. 'Component A' has a single 'renders' arrow to a node labelled 'Component B'. 'Component C' has a single 'renders' arrow to a node labelled 'Component D'.](/images/docs/diagrams/generic_render_tree.dark.png)

![A tree graph with five nodes, with each node representing a component. The root node is located at the top the tree graph and is labelled 'Root Component'. It has two arrows extending down to two nodes labelled 'Component A' and 'Component C'. Each of the arrows is labelled with 'renders'. 'Component A' has a single 'renders' arrow to a node labelled 'Component B'. 'Component C' has a single 'renders' arrow to a node labelled 'Component D'.](/images/docs/diagrams/generic_render_tree.png)

An example React render tree.

Components near the top of the tree, near the root component, are considered top-level components. Components with no child components are leaf components. This categorization of components is useful for understanding data flow and rendering performance.

Modelling the relationship between JavaScript modules is another useful way to understand your app. We refer to it as a module dependency tree.

![A tree graph with five nodes. Each node represents a JavaScript module. The top-most node is labelled 'RootModule.js'. It has three arrows extending to the nodes: 'ModuleA.js', 'ModuleB.js', and 'ModuleC.js'. Each arrow is labelled as 'imports'. 'ModuleC.js' node has a single 'imports' arrow that points to a node labelled 'ModuleD.js'.](/images/docs/diagrams/generic_dependency_tree.dark.png)

![A tree graph with five nodes. Each node represents a JavaScript module. The top-most node is labelled 'RootModule.js'. It has three arrows extending to the nodes: 'ModuleA.js', 'ModuleB.js', and 'ModuleC.js'. Each arrow is labelled as 'imports'. 'ModuleC.js' node has a single 'imports' arrow that points to a node labelled 'ModuleD.js'.](/images/docs/diagrams/generic_dependency_tree.png)

An example module dependency tree.

A dependency tree is often used by build tools to bundle all the relevant JavaScript code for the client to download and render. A large bundle size regresses user experience for React apps. Understanding the module dependency tree is helpful to debug such issues.

## Ready to learn this topic?

Read **[Your UI as a Tree](react/learn/understanding-your-ui-as-a-tree/index.md)** to learn how to create a render and module dependency trees for a React app and how they’re useful mental models for improving user experience and performance.

[Read More](react/learn/understanding-your-ui-as-a-tree/index.md)

* * *

## What’s next?[](#whats-next "Link for What’s next? ")

Head over to [Your First Component](react/learn/your-first-component/index.md) to start reading this chapter page by page!

Or, if you’re already familiar with these topics, why not read about [Adding Interactivity](react/learn/adding-interactivity/index.md)?

