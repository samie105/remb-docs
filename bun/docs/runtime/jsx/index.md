---
title: "JSX"
source: "https://bun.com/docs/runtime/jsx"
canonical_url: "https://bun.com/docs/runtime/jsx"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:34.188Z"
content_hash: "7495c49af145a8160e410041ba3066905d19435a73e45c2cf39ebae9b99c686d"
menu_path: ["JSX"]
section_path: []
nav_prev: {"path": "bun/docs/runtime/jsonl/index.md", "title": "JSONL"}
nav_next: {"path": "bun/docs/runtime/markdown/index.md", "title": "Markdown"}
---

Bun supports `.jsx` and `.tsx` files out of the box. Bun’s internal transpiler converts JSX syntax into vanilla JavaScript before execution.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)react.tsx

```
function Component(props: {message: string}) {
  return (
    <body>
      <h1 style={{color: 'red'}}>{props.message}</h1>
    </body>
  );
}

console.log(<Component message="Hello world!" />);
```

## Configuration

Bun reads your `tsconfig.json` or `jsconfig.json` configuration files to determines how to perform the JSX transform internally. To avoid using either of these, the following options can also be defined in [`bunfig.toml`](bun/docs/runtime/bunfig/index.md). The following compiler options are respected.

### [`jsx`](https://www.typescriptlang.org/tsconfig#jsx)

How JSX constructs are transformed into vanilla JavaScript internally. The table below lists the possible values of `jsx`, along with their transpilation of the following simple JSX component:

```
<Box width={5}>Hello</Box>
```

Compiler options

Transpiled output

`json<br/>{<br/> "jsx": "react"<br/>}<br/>`

`tsx<br/>import { createElement } from "react";<br/>createElement("Box", { width: 5 }, "Hello");<br/>`

`json<br/>{<br/> "jsx": "react-jsx"<br/>}<br/>`

`tsx<br/>import { jsx } from "react/jsx-runtime";<br/>jsx("Box", { width: 5 }, "Hello");<br/>`

`json<br/>{<br/> "jsx": "react-jsxdev"<br/>}<br/>`

`tsx<br/>import { jsxDEV } from "react/jsx-dev-runtime";<br/>jsxDEV(<br/> "Box",<br/> { width: 5, children: "Hello" },<br/> undefined,<br/> false,<br/> undefined,<br/> this,<br/>);<br/>`

The `jsxDEV` variable name is a convention used by React. The `DEV` suffix is a visible way to indicate that the code is intended for use in development. The development version of React is slower and includes additional validity checks & debugging tools.

`json<br/>{<br/> "jsx": "preserve"<br/>}<br/>`

`tsx<br/>// JSX is not transpiled<br/>// "preserve" is not supported by Bun currently<br/><Box width={5}>Hello</Box><br/>`

### [`jsxFactory`](https://www.typescriptlang.org/tsconfig#jsxFactory)

The function name used to represent JSX constructs. Default value is `"createElement"`. This is useful for libraries like [Preact](https://preactjs.com/) that use a different function name (`"h"`).

Compiler options

Transpiled output

`json<br/>{<br/> "jsx": "react",<br/> "jsxFactory": "h"<br/>}<br/>`

`tsx<br/>import { h } from "react";<br/>h("Box", { width: 5 }, "Hello");<br/>`

### [`jsxFragmentFactory`](https://www.typescriptlang.org/tsconfig#jsxFragmentFactory)

The function name used to represent [JSX fragments](https://react.dev/reference/react/Fragment) such as `<>Hello</>`; only applicable when `jsx` is `react`. Default value is `"Fragment"`.

Compiler options

Transpiled output

`json<br/>{<br/> "jsx": "react",<br/> "jsxFactory": "myjsx",<br/> "jsxFragmentFactory": "MyFragment"<br/>}<br/>`

`tsx<br/>// input<br/><>Hello</>;<br/><br/>// output<br/>import { myjsx, MyFragment } from "react";<br/>myjsx(MyFragment, null, "Hello");<br/>`

### [`jsxImportSource`](https://www.typescriptlang.org/tsconfig#jsxImportSource)

The module from which the component factory function (`createElement`, `jsx`, `jsxDEV`, etc) will be imported. Default value is `"react"`. This will typically be necessary when using a component library like Preact.

Compiler options

Transpiled output

`jsonc<br/>{<br/> "jsx": "react",<br/> // jsxImportSource is not defined<br/> // default to "react"<br/>}<br/>`

`tsx<br/>import { jsx } from "react/jsx-runtime";<br/>jsx("Box", { width: 5, children: "Hello" });<br/>`

`jsonc<br/>{<br/> "jsx": "react-jsx",<br/> "jsxImportSource": "preact",<br/>}<br/>`

`tsx<br/>import { jsx } from "preact/jsx-runtime";<br/>jsx("Box", { width: 5, children: "Hello" });<br/>`

`jsonc<br/>{<br/> "jsx": "react-jsxdev",<br/> "jsxImportSource": "preact",<br/>}<br/>`

`tsx<br/>// /jsx-runtime is automatically appended<br/>import { jsxDEV } from "preact/jsx-dev-runtime";<br/>jsxDEV(<br/> "Box",<br/> { width: 5, children: "Hello" },<br/> undefined,<br/> false,<br/> undefined,<br/> this,<br/>);<br/>`

### JSX pragma

All of these values can be set on a per-file basis using _pragmas_. A pragma is a special comment that sets a compiler option in a particular file.

Pragma

Equivalent config

`ts<br/>// @jsx h<br/>`

`jsonc<br/>{<br/> "jsxFactory": "h",<br/>}<br/>`

`ts<br/>// @jsxFrag MyFragment<br/>`

`jsonc<br/>{<br/> "jsxFragmentFactory": "MyFragment",<br/>}<br/>`

`ts<br/>// @jsxImportSource preact<br/>`

`jsonc<br/>{<br/> "jsxImportSource": "preact",<br/>}<br/>`

## Logging

Bun implements special logging for JSX to make debugging easier. Given the following file:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.tsx

```
import { Stack, UserCard } from "./components";

console.log(
  <Stack>
    <UserCard name="Dom" bio="Street racer and Corona lover" />
    <UserCard name="Jakob" bio="Super spy and Dom's secret brother" />
  </Stack>,
);
```

Bun will pretty-print the component tree when logged:

## Prop punning

The Bun runtime also supports “prop punning” for JSX. This is a shorthand syntax useful for assigning a variable to a prop with the same name.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)react.tsx

```
function Div(props: {className: string;}) {
  const {className} = props;

  // without punning
  return <div className={className} />;
  // with punning
  return <div {className} />;
}
```
