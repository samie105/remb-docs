---
title: "Scaling Up with Reducer and Context"
source: "https://react.dev/learn/scaling-up-with-reducer-and-context"
canonical_url: "https://react.dev/learn/scaling-up-with-reducer-and-context"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:43.678Z"
content_hash: "f1414b457841a360e90ceafca7b36065928ab2742bb5cb04afa5aaef8b1bb33b"
menu_path: ["Scaling Up with Reducer and Context"]
section_path: []
nav_prev: {"path": "../passing-data-deeply-with-context/index.md", "title": "Passing Data Deeply with Context"}
nav_next: {"path": "../escape-hatches/index.md", "title": "Escape Hatches"}
---

Reducers let you consolidate a component’s state update logic. Context lets you pass information deep down to other components. You can combine reducers and context together to manage state of a complex screen.

### You will learn

*   How to combine a reducer with context
*   How to avoid passing state and dispatch through props
*   How to keep context and state logic in a separate file

## Combining a reducer with context[](#combining-a-reducer-with-context "Link for Combining a reducer with context ")

In this example from [the introduction to reducers](../extracting-state-logic-into-a-reducer/index.md), the state is managed by a reducer. The reducer function contains all of the state update logic and is declared at the bottom of this file:

A reducer helps keep the event handlers short and concise. However, as your app grows, you might run into another difficulty. **Currently, the `tasks` state and the `dispatch` function are only available in the top-level `TaskApp` component.** To let other components read the list of tasks or change it, you have to explicitly [pass down](../passing-props-to-a-component/index.md) the current state and the event handlers that change it as props.

For example, `TaskApp` passes a list of tasks and the event handlers to `TaskList`:

```
<TaskListtasks={tasks}onChangeTask={handleChangeTask}onDeleteTask={handleDeleteTask}/>
```

And `TaskList` passes the event handlers to `Task`:

```
<Tasktask={task}onChange={onChangeTask}onDelete={onDeleteTask}/>
```

In a small example like this, this works well, but if you have tens or hundreds of components in the middle, passing down all state and functions can be quite frustrating!

This is why, as an alternative to passing them through props, you might want to put both the `tasks` state and the `dispatch` function [into context.](../passing-data-deeply-with-context/index.md) **This way, any component below `TaskApp` in the tree can read the tasks and dispatch actions without the repetitive “prop drilling”.**

Here is how you can combine a reducer with context:

1.  **Create** the context.
2.  **Put** state and dispatch into context.
3.  **Use** context anywhere in the tree.

### Step 1: Create the context[](#step-1-create-the-context "Link for Step 1: Create the context ")

The `useReducer` Hook returns the current `tasks` and the `dispatch` function that lets you update them:

```
const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
```

To pass them down the tree, you will [create](../passing-data-deeply-with-context/index.md#step-2-use-the-context) two separate contexts:

*   `TasksContext` provides the current list of tasks.
*   `TasksDispatchContext` provides the function that lets components dispatch actions.

Export them from a separate file so that you can later import them from other files:

Here, you’re passing `null` as the default value to both contexts. The actual values will be provided by the `TaskApp` component.

### Step 2: Put state and dispatch into context[](#step-2-put-state-and-dispatch-into-context "Link for Step 2: Put state and dispatch into context ")

Now you can import both contexts in your `TaskApp` component. Take the `tasks` and `dispatch` returned by `useReducer()` and [provide them](../passing-data-deeply-with-context/index.md#step-3-provide-the-context) to the entire tree below:

```
import { TasksContext, TasksDispatchContext } from './TasksContext.js';export default function TaskApp() {const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);// ...return (<TasksContext value={tasks}><TasksDispatchContext value={dispatch}>        ...</TasksDispatchContext></TasksContext>);}
```

For now, you pass the information both via props and in context:

In the next step, you will remove prop passing.

### Step 3: Use context anywhere in the tree[](#step-3-use-context-anywhere-in-the-tree "Link for Step 3: Use context anywhere in the tree ")

Now you don’t need to pass the list of tasks or the event handlers down the tree:

```
<TasksContext value={tasks}><TasksDispatchContext value={dispatch}><h1>Day off in Kyoto</h1><AddTask /><TaskList /></TasksDispatchContext></TasksContext>
```

Instead, any component that needs the task list can read it from the `TasksContext`:

```
export default function TaskList() {const tasks = useContext(TasksContext);// ...
```

To update the task list, any component can read the `dispatch` function from context and call it:

```
export default function AddTask() {const [text, setText] = useState('');const dispatch = useContext(TasksDispatchContext);// ...return (// ...<button onClick={() => {setText('');dispatch({type: 'added',id: nextId++,text: text,});}}>Add</button>// ...
```

**The `TaskApp` component does not pass any event handlers down, and the `TaskList` does not pass any event handlers to the `Task` component either.** Each component reads the context that it needs:

**The state still “lives” in the top-level `TaskApp` component, managed with `useReducer`.** But its `tasks` and `dispatch` are now available to every component below in the tree by importing and using these contexts.

## Moving all wiring into a single file[](#moving-all-wiring-into-a-single-file "Link for Moving all wiring into a single file ")

You don’t have to do this, but you could further declutter the components by moving both reducer and context into a single file. Currently, `TasksContext.js` contains only two context declarations:

```
import { createContext } from 'react';export const TasksContext = createContext(null);export const TasksDispatchContext = createContext(null);
```

This file is about to get crowded! You’ll move the reducer into that same file. Then you’ll declare a new `TasksProvider` component in the same file. This component will tie all the pieces together:

1.  It will manage the state with a reducer.
2.  It will provide both contexts to components below.
3.  It will [take `children` as a prop](../passing-props-to-a-component/index.md#passing-jsx-as-children) so you can pass JSX to it.

```
export function TasksProvider({ children }) {const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);return (<TasksContext value={tasks}><TasksDispatchContext value={dispatch}>{children}</TasksDispatchContext></TasksContext>);}
```

**This removes all the complexity and wiring from your `TaskApp` component:**

You can also export functions that _use_ the context from `TasksContext.js`:

```
export function useTasks() {return useContext(TasksContext);}export function useTasksDispatch() {return useContext(TasksDispatchContext);}
```

When a component needs to read context, it can do it through these functions:

```
const tasks = useTasks();const dispatch = useTasksDispatch();
```

This doesn’t change the behavior in any way, but it lets you later split these contexts further or add some logic to these functions. **Now all of the context and reducer wiring is in `TasksContext.js`. This keeps the components clean and uncluttered, focused on what they display rather than where they get the data:**

import { useState } from 'react';
import { useTasks, useTasksDispatch } from './TasksContext.js';

export default function TaskList() {
  const tasks = useTasks();
  return (
    <ul\>
      {tasks.map(task \=> (
        <li key\={task.id}\>
          <Task task\={task} />
        </li\>
      ))}
    </ul\>
  );
}

function Task({ task }) {
  const \[isEditing, setIsEditing\] = useState(false);
  const dispatch = useTasksDispatch();
  let taskContent;
  if (isEditing) {
    taskContent = (
      <\>
        <input
          value\={task.text}
          onChange\={e \=> {
            dispatch({
              type: 'changed',
              task: {
                ...task,
                text: e.target.value
              }
            });
          }} />
        <button onClick\={() \=> setIsEditing(false)}\>
          Save
        </button\>
      </\>
    );
  } else {
    taskContent = (
      <\>
        {task.text}
        <button onClick\={() \=> setIsEditing(true)}\>
          Edit
        </button\>
      </\>
    );
  }
  return (
    <label\>
      <input
        type\="checkbox"
        checked\={task.done}
        onChange\={e \=> {
          dispatch({
            type: 'changed',
            task: {
              ...task,
              done: e.target.checked
            }
          });
        }}
      />
      {taskContent}
      <button onClick\={() \=> {
        dispatch({
          type: 'deleted',
          id: task.id
        });
      }}\>
        Delete
      </button\>
    </label\>
  );
}

You can think of `TasksProvider` as a part of the screen that knows how to deal with tasks, `useTasks` as a way to read them, and `useTasksDispatch` as a way to update them from any component below in the tree.

### Note

Functions like `useTasks` and `useTasksDispatch` are called _[Custom Hooks.](../reusing-logic-with-custom-hooks/index.md)_ Your function is considered a custom Hook if its name starts with `use`. This lets you use other Hooks, like `useContext`, inside it.

As your app grows, you may have many context-reducer pairs like this. This is a powerful way to scale your app and [lift state up](../sharing-state-between-components/index.md) without too much work whenever you want to access the data deep in the tree.

## Recap[](#recap "Link for Recap")

*   You can combine reducer with context to let any component read and update state above it.
*   To provide state and the dispatch function to components below:
    1.  Create two contexts (for state and for dispatch functions).
    2.  Provide both contexts from the component that uses the reducer.
    3.  Use either context from components that need to read them.
*   You can further declutter the components by moving all wiring into one file.
    *   You can export a component like `TasksProvider` that provides context.
    *   You can also export custom Hooks like `useTasks` and `useTasksDispatch` to read it.
*   You can have many context-reducer pairs like this in your app.
