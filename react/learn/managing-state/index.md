---
title: "Managing State"
source: "https://react.dev/learn/managing-state"
canonical_url: "https://react.dev/learn/managing-state"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:13.829Z"
content_hash: "0348862d5086a8500c1f4ca9516615f7666e9cb01cdad8cfbed43728fd96583f"
menu_path: ["Managing State"]
section_path: []
nav_prev: {"path": "react/learn/updating-arrays-in-state/index.md", "title": "Updating Arrays in State"}
nav_next: {"path": "react/learn/reacting-to-input-with-state/index.md", "title": "Reacting to Input with State"}
---

As your application grows, it helps to be more intentional about how your state is organized and how the data flows between your components. Redundant or duplicate state is a common source of bugs. In this chapter, you’ll learn how to structure your state well, how to keep your state update logic maintainable, and how to share state between distant components.

## Reacting to input with state[](#reacting-to-input-with-state "Link for Reacting to input with state ")

With React, you won’t modify the UI from code directly. For example, you won’t write commands like “disable the button”, “enable the button”, “show the success message”, etc. Instead, you will describe the UI you want to see for the different visual states of your component (“initial state”, “typing state”, “success state”), and then trigger the state changes in response to user input. This is similar to how designers think about UI.

Here is a quiz form built using React. Note how it uses the `status` state variable to determine whether to enable or disable the submit button, and whether to show the success message instead.

* * *

## Choosing the state structure[](#choosing-the-state-structure "Link for Choosing the state structure ")

Structuring state well can make a difference between a component that is pleasant to modify and debug, and one that is a constant source of bugs. The most important principle is that state shouldn’t contain redundant or duplicated information. If there’s unnecessary state, it’s easy to forget to update it, and introduce bugs!

For example, this form has a **redundant** `fullName` state variable:

You can remove it and simplify the code by calculating `fullName` while the component is rendering:

This might seem like a small change, but many bugs in React apps are fixed this way.

* * *

## Sharing state between components[](#sharing-state-between-components "Link for Sharing state between components ")

Sometimes, you want the state of two components to always change together. To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. This is known as “lifting state up”, and it’s one of the most common things you will do writing React code.

In this example, only one panel should be active at a time. To achieve this, instead of keeping the active state inside each individual panel, the parent component holds the state and specifies the props for its children.

* * *

## Preserving and resetting state[](#preserving-and-resetting-state "Link for Preserving and resetting state ")

When you re-render a component, React needs to decide which parts of the tree to keep (and update), and which parts to discard or re-create from scratch. In most cases, React’s automatic behavior works well enough. By default, React preserves the parts of the tree that “match up” with the previously rendered component tree.

However, sometimes this is not what you want. In this chat app, typing a message and then switching the recipient does not reset the input. This can make the user accidentally send a message to the wrong person:

React lets you override the default behavior, and _force_ a component to reset its state by passing it a different `key`, like `<Chat key={email} />`. This tells React that if the recipient is different, it should be considered a _different_ `Chat` component that needs to be re-created from scratch with the new data (and UI like inputs). Now switching between the recipients resets the input field—even though you render the same component.

* * *

Components with many state updates spread across many event handlers can get overwhelming. For these cases, you can consolidate all the state update logic outside your component in a single function, called “reducer”. Your event handlers become concise because they only specify the user “actions”. At the bottom of the file, the reducer function specifies how the state should update in response to each action!

* * *

## Passing data deeply with context[](#passing-data-deeply-with-context "Link for Passing data deeply with context ")

Usually, you will pass information from a parent component to a child component via props. But passing props can become inconvenient if you need to pass some prop through many components, or if many components need the same information. Context lets the parent component make some information available to any component in the tree below it—no matter how deep it is—without passing it explicitly through props.

Here, the `Heading` component determines its heading level by “asking” the closest `Section` for its level. Each `Section` tracks its own level by asking the parent `Section` and adding one to it. Every `Section` provides information to all components below it without passing props—it does that through context.

* * *

## Scaling up with reducer and context[](#scaling-up-with-reducer-and-context "Link for Scaling up with reducer and context ")

Reducers let you consolidate a component’s state update logic. Context lets you pass information deep down to other components. You can combine reducers and context together to manage state of a complex screen.

With this approach, a parent component with complex state manages it with a reducer. Other components anywhere deep in the tree can read its state via context. They can also dispatch actions to update that state.

