---
title: "unstable_catchError"
source: "https://nextjs.org/docs/app/api-reference/functions/catchError"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/catchError"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:00.020Z"
content_hash: "65966545a0ebe517f26b3c33c62f049c0c5f02212d8c8c45adb60d5aa7dc9f19"
menu_path: ["unstable_catchError"]
section_path: []
version: "latest"
content_language: "en"
---
[API Reference](/docs/app/api-reference)[Functions](/docs/app/api-reference/functions)unstable\_catchError

# unstable\_catchError

Last updated April 23, 2026

The `unstable_catchError` function creates a component that wraps its children in an error boundary. It provides a programmatic alternative to the [`error.js`](/docs/app/api-reference/file-conventions/error) file convention, enabling component-level error recovery anywhere in your component tree.

Compared to a custom React error boundary, `unstable_catchError` is designed to work with Next.js out of the box:

-   **Built-in error recovery** — [`unstable_retry()`](/docs/app/api-reference/file-conventions/error#unstable_retry) re-fetches and re-renders the error boundary's children, including Server Components.
-   **Framework-aware integration** — APIs like `redirect()` and `notFound()` work by throwing special errors under the hood. `unstable_catchError` handles these seamlessly, so they're not accidentally caught by your error boundary.
-   **Client navigation handling** — The error state automatically clears when you do a client navigation to a different route.

`unstable_catchError` can be called from [Client Components](/docs/app/getting-started/server-and-client-components).

app/custom-error-boundary.tsx

JavaScriptTypeScript

```
'use client'
 
import { unstable_catchError, type ErrorInfo } from 'next/error'
 
function ErrorFallback(
  props: { title: string },
  { error, unstable_retry }: ErrorInfo
) {
  return (
    <div>
      <h2>{props.title}</h2>
      <p>{error.message}</p>
      <button onClick={() => unstable_retry()}>Try again</button>
    </div>
  )
}
 
export default unstable_catchError(ErrorFallback)
```

## Reference[](#reference)

### Parameters[](#parameters)

`unstable_catchError` accepts a single argument:

```
const ErrorWrapper = unstable_catchError(fallback)
```

#### `fallback`[](#fallback)

A function that renders the error UI when an error is caught. It receives two arguments:

-   `props` — The props passed to the wrapper component (excluding `children`).
-   `errorInfo` — An object containing information about the error:

| Property | Type | Description |
| --- | --- | --- |
| `error` | [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) | The error instance that was caught. |
| `unstable_retry` | `() => void` | Re-fetches and re-renders the error boundary's children. If successful, the fallback is replaced with the re-rendered result. |
| `reset` | `() => void` | Resets the error state and re-renders without re-fetching. Use [`unstable_retry()`](/docs/app/api-reference/file-conventions/error#unstable_retry) in most cases. |

The `fallback` function must be a Client Component (or defined in a `'use client'` module).

### Returns[](#returns)

`unstable_catchError` returns a React component that:

-   Accepts the same props as your fallback's first argument, plus `children`.
-   Wraps `children` in an error boundary.
-   Renders the `fallback` when an error is caught in `children`.

## Examples[](#examples)

### Client Component[](#client-component)

Define a fallback and use the returned component to wrap parts of your UI:

app/some-component.tsx

JavaScriptTypeScript

```
import ErrorWrapper from '../custom-error-boundary'
 
export default function Component({ children }: { children: React.ReactNode }) {
  return <ErrorWrapper title="Dashboard Error">{children}</ErrorWrapper>
}
```

### Recovering from errors[](#recovering-from-errors)

Use `unstable_retry()` to prompt the user to recover from the error. When called, the function re-fetches and re-renders the error boundary's children. If successful, the fallback is replaced with the re-rendered result.

In most cases, use `unstable_retry()` instead of `reset()`. The `reset()` function only clears the error state and re-renders without re-fetching, which means it won't recover from Server Component errors.

app/custom-error-boundary.tsx

JavaScriptTypeScript

```
'use client'
 
import { unstable_catchError, type ErrorInfo } from 'next/error'
 
function ErrorFallback(props: {}, { error, unstable_retry, reset }: ErrorInfo) {
  return (
    <div>
      <p>{error.message}</p>
      <button onClick={() => unstable_retry()}>Try again</button>
      <button onClick={() => reset()}>Reset</button>
    </div>
  )
}
 
export default unstable_catchError(ErrorFallback)
```

### Server-rendered error fallback[](#server-rendered-error-fallback)

You can pass server-rendered content as a prop to display data-driven fallback UI. This works by rendering a Server Component as a `React.ReactNode` prop that the fallback displays when an error is caught.

> **Good to know**: This pattern eagerly renders the fallback on every page render, even when no error occurs. For most use cases, a simpler client-side fallback is sufficient.

app/error-boundary.tsx

JavaScriptTypeScript

```
'use client'
 
import { unstable_catchError, type ErrorInfo } from 'next/error'
 
function ErrorFallback(
  props: { fallback: React.ReactNode },
  errorInfo: ErrorInfo
) {
  return props.fallback
}
 
export default unstable_catchError(ErrorFallback)
```

app/some-component.tsx

JavaScriptTypeScript

```
import ErrorBoundary from '../error-boundary'
 
async function ErrorFallback() {
  const data = await getData()
  return <div>{data.message}</div>
}
 
export default function Component({ children }: { children: React.ReactNode }) {
  return <ErrorBoundary fallback={<ErrorFallback />}>{children}</ErrorBoundary>
}
```

> **Good to know**:
> 
> -   Unlike the `error.js` file convention which is scoped to route segments, `unstable_catchError` can be used to wrap any part of your component tree for component-level error recovery.
> -   Props passed to the wrapper component are forwarded to the fallback function, making it easy to create reusable error UIs with different configurations.
> -   You don't need to wrap `error.js` default exports with `unstable_catchError`. The [`error.js`](/docs/app/api-reference/file-conventions/error) file convention already renders inside a built-in error boundary provided by Next.js.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v16.2.0` | `unstable_catchError` introduced. |

## Learn more about error handling

[

### Error Handling

Learn how to display expected errors and handle uncaught exceptions.

](/docs/app/getting-started/error-handling)[

### error.js

API reference for the error.js special file.

](/docs/app/api-reference/file-conventions/error)

Was this helpful?
