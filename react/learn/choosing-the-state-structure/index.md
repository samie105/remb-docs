---
title: "Choosing the State Structure"
source: "https://react.dev/learn/choosing-the-state-structure"
canonical_url: "https://react.dev/learn/choosing-the-state-structure"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:48.239Z"
content_hash: "db83fbbc4397154247714c759693153e24a2fa70da231c1c33cbcd27b20002cb"
menu_path: ["Choosing the State Structure"]
section_path: []
nav_prev: {"path": "../reacting-to-input-with-state/index.md", "title": "Reacting to Input with State"}
nav_next: {"path": "../sharing-state-between-components/index.md", "title": "Sharing State Between Components"}
---

Structuring state well can make a difference between a component that is pleasant to modify and debug, and one that is a constant source of bugs. Here are some tips you should consider when structuring state.

### You will learn

*   When to use a single vs multiple state variables
*   What to avoid when organizing state
*   How to fix common issues with the state structure

## Principles for structuring state[](#principles-for-structuring-state "Link for Principles for structuring state ")

When you write a component that holds some state, you’ll have to make choices about how many state variables to use and what the shape of their data should be. While it’s possible to write correct programs even with a suboptimal state structure, there are a few principles that can guide you to make better choices:

1.  **Group related state.** If you always update two or more state variables at the same time, consider merging them into a single state variable.
2.  **Avoid contradictions in state.** When the state is structured in a way that several pieces of state may contradict and “disagree” with each other, you leave room for mistakes. Try to avoid this.
3.  **Avoid redundant state.** If you can calculate some information from the component’s props or its existing state variables during rendering, you should not put that information into that component’s state.
4.  **Avoid duplication in state.** When the same data is duplicated between multiple state variables, or within nested objects, it is difficult to keep them in sync. Reduce duplication when you can.
5.  **Avoid deeply nested state.** Deeply hierarchical state is not very convenient to update. When possible, prefer to structure state in a flat way.

The goal behind these principles is to _make state easy to update without introducing mistakes_. Removing redundant and duplicate data from state helps ensure that all its pieces stay in sync. This is similar to how a database engineer might want to [“normalize” the database structure](https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description) to reduce the chance of bugs. To paraphrase Albert Einstein, **“Make your state as simple as it can be—but no simpler.”**

Now let’s see how these principles apply in action.

You might sometimes be unsure between using a single or multiple state variables.

Should you do this?

```
const [x, setX] = useState(0);const [y, setY] = useState(0);
```

Or this?

```
const [position, setPosition] = useState({ x: 0, y: 0 });
```

Technically, you can use either of these approaches. But **if some two state variables always change together, it might be a good idea to unify them into a single state variable.** Then you won’t forget to always keep them in sync, like in this example where moving the cursor updates both coordinates of the red dot:

Another case where you’ll group data into an object or an array is when you don’t know how many pieces of state you’ll need. For example, it’s helpful when you have a form where the user can add custom fields.

### Pitfall

If your state variable is an object, remember that [you can’t update only one field in it](../updating-objects-in-state/index.md) without explicitly copying the other fields. For example, you can’t do `setPosition({ x: 100 })` in the above example because it would not have the `y` property at all! Instead, if you wanted to set `x` alone, you would either do `setPosition({ ...position, x: 100 })`, or split them into two state variables and do `setX(100)`.

## Avoid contradictions in state[](#avoid-contradictions-in-state "Link for Avoid contradictions in state ")

Here is a hotel feedback form with `isSending` and `isSent` state variables:

While this code works, it leaves the door open for “impossible” states. For example, if you forget to call `setIsSent` and `setIsSending` together, you may end up in a situation where both `isSending` and `isSent` are `true` at the same time. The more complex your component is, the harder it is to understand what happened.

**Since `isSending` and `isSent` should never be `true` at the same time, it is better to replace them with one `status` state variable that may take one of _three_ valid states:** `'typing'` (initial), `'sending'`, and `'sent'`:

You can still declare some constants for readability:

```
const isSending = status === 'sending';const isSent = status === 'sent';
```

But they’re not state variables, so you don’t need to worry about them getting out of sync with each other.

## Avoid redundant state[](#avoid-redundant-state "Link for Avoid redundant state ")

If you can calculate some information from the component’s props or its existing state variables during rendering, you **should not** put that information into that component’s state.

For example, take this form. It works, but can you find any redundant state in it?

This form has three state variables: `firstName`, `lastName`, and `fullName`. However, `fullName` is redundant. **You can always calculate `fullName` from `firstName` and `lastName` during render, so remove it from state.**

This is how you can do it:

Here, `fullName` is _not_ a state variable. Instead, it’s calculated during render:

```
const fullName = firstName + ' ' + lastName;
```

As a result, the change handlers don’t need to do anything special to update it. When you call `setFirstName` or `setLastName`, you trigger a re-render, and then the next `fullName` will be calculated from the fresh data.

##### Deep Dive

#### Don’t mirror props in state[](#don-t-mirror-props-in-state "Link for Don’t mirror props in state ")

A common example of redundant state is code like this:

```
function Message({ messageColor }) {const [color, setColor] = useState(messageColor);
```

Here, a `color` state variable is initialized to the `messageColor` prop. The problem is that **if the parent component passes a different value of `messageColor` later (for example, `'red'` instead of `'blue'`), the `color` _state variable_ would not be updated!** The state is only initialized during the first render.

This is why “mirroring” some prop in a state variable can lead to confusion. Instead, use the `messageColor` prop directly in your code. If you want to give it a shorter name, use a constant:

```
function Message({ messageColor }) {const color = messageColor;
```

This way it won’t get out of sync with the prop passed from the parent component.

”Mirroring” props into state only makes sense when you _want_ to ignore all updates for a specific prop. By convention, start the prop name with `initial` or `default` to clarify that its new values are ignored:

```
function Message({ initialColor }) {// The `color` state variable holds the *first* value of `initialColor`.// Further changes to the `initialColor` prop are ignored.const [color, setColor] = useState(initialColor);
```

## Avoid duplication in state[](#avoid-duplication-in-state "Link for Avoid duplication in state ")

This menu list component lets you choose a single travel snack out of several:

Currently, it stores the selected item as an object in the `selectedItem` state variable. However, this is not great: **the contents of the `selectedItem` is the same object as one of the items inside the `items` list.** This means that the information about the item itself is duplicated in two places.

Why is this a problem? Let’s make each item editable:

Notice how if you first click “Choose” on an item and _then_ edit it, **the input updates but the label at the bottom does not reflect the edits.** This is because you have duplicated state, and you forgot to update `selectedItem`.

Although you could update `selectedItem` too, an easier fix is to remove duplication. In this example, instead of a `selectedItem` object (which creates a duplication with objects inside `items`), you hold the `selectedId` in state, and _then_ get the `selectedItem` by searching the `items` array for an item with that ID:

The state used to be duplicated like this:

*   `items = [{ id: 0, title: 'pretzels'}, ...]`
*   `selectedItem = {id: 0, title: 'pretzels'}`

But after the change it’s like this:

*   `items = [{ id: 0, title: 'pretzels'}, ...]`
*   `selectedId = 0`

The duplication is gone, and you only keep the essential state!

Now if you edit the _selected_ item, the message below will update immediately. This is because `setItems` triggers a re-render, and `items.find(...)` would find the item with the updated title. You didn’t need to hold _the selected item_ in state, because only the _selected ID_ is essential. The rest could be calculated during render.

## Avoid deeply nested state[](#avoid-deeply-nested-state "Link for Avoid deeply nested state ")

Imagine a travel plan consisting of planets, continents, and countries. You might be tempted to structure its state using nested objects and arrays, like in this example:

Now let’s say you want to add a button to delete a place you’ve already visited. How would you go about it? [Updating nested state](../updating-objects-in-state/index.md#updating-a-nested-object) involves making copies of objects all the way up from the part that changed. Deleting a deeply nested place would involve copying its entire parent place chain. Such code can be very verbose.

**If the state is too nested to update easily, consider making it “flat”.** Here is one way you can restructure this data. Instead of a tree-like structure where each `place` has an array of _its child places_, you can have each place hold an array of _its child place IDs_. Then store a mapping from each place ID to the corresponding place.

This data restructuring might remind you of seeing a database table:

**Now that the state is “flat” (also known as “normalized”), updating nested items becomes easier.**

In order to remove a place now, you only need to update two levels of state:

*   The updated version of its _parent_ place should exclude the removed ID from its `childIds` array.
*   The updated version of the root “table” object should include the updated version of the parent place.

Here is an example of how you could go about it:

You can nest state as much as you like, but making it “flat” can solve numerous problems. It makes state easier to update, and it helps ensure you don’t have duplication in different parts of a nested object.

##### Deep Dive

#### Improving memory usage[](#improving-memory-usage "Link for Improving memory usage ")

Ideally, you would also remove the deleted items (and their children!) from the “table” object to improve memory usage. This version does that. It also [uses Immer](../updating-objects-in-state/index.md#write-concise-update-logic-with-immer) to make the update logic more concise.

Sometimes, you can also reduce state nesting by moving some of the nested state into the child components. This works well for ephemeral UI state that doesn’t need to be stored, like whether an item is hovered.

## Recap[](#recap "Link for Recap")

*   If two state variables always update together, consider merging them into one.
*   Choose your state variables carefully to avoid creating “impossible” states.
*   Structure your state in a way that reduces the chances that you’ll make a mistake updating it.
*   Avoid redundant and duplicate state so that you don’t need to keep it in sync.
*   Don’t put props _into_ state unless you specifically want to prevent updates.
*   For UI patterns like selection, keep ID or index in state instead of the object itself.
*   If updating deeply nested state is complicated, try flattening it.

#### 

Challenge

1

of

4:

Fix a component that’s not updating[](#fix-a-component-thats-not-updating "Link for this heading")

This `Clock` component receives two props: `color` and `time`. When you select a different color in the select box, the `Clock` component receives a different `color` prop from its parent component. However, for some reason, the displayed color doesn’t update. Why? Fix the problem.
