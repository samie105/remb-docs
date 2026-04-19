---
title: "DOM testing"
source: "https://bun.com/docs/test/dom"
canonical_url: "https://bun.com/docs/test/dom"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:26.089Z"
content_hash: "4e1e8ac9cf7aec653f9e120f8acc8f4c3c4955a908767de564409ac166cade2a"
menu_path: ["DOM testing"]
section_path: []
---
Bun’s test runner plays well with existing component and DOM testing libraries, including React Testing Library and happy-dom.

## happy-dom

For writing headless tests for your frontend code and components, we recommend happy-dom. Happy DOM implements a complete set of HTML and DOM APIs in plain JavaScript, making it possible to simulate a browser environment with high fidelity. To get started install the `@happy-dom/global-registrator` package as a dev dependency.

terminal

```
bun add -d @happy-dom/global-registrator
```

We’ll be using Bun’s preload functionality to register the happy-dom globals before running our tests. This step will make browser APIs like `document` available in the global scope. Create a file called `happydom.ts` in the root of your project and add the following code:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)happydom.ts

```
import { GlobalRegistrator } from "@happy-dom/global-registrator";

GlobalRegistrator.register();
```

To preload this file before `bun test`, open or create a `bunfig.toml` file and add the following lines.

bunfig.toml

```
[test]
preload = ["./happydom.ts"]
```

This will execute `happydom.ts` when you run `bun test`. Now you can write tests that use browser APIs like `document` and `window`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)dom.test.ts

```
import { test, expect } from "bun:test";

test("dom test", () => {
  document.body.innerHTML = `<button>My button</button>`;
  const button = document.querySelector("button");
  expect(button?.innerText).toEqual("My button");
});
```

### TypeScript Support

Depending on your `tsconfig.json` setup, you may see a “Cannot find name ‘document’” type error in the code above. To “inject” the types for `document` and other browser APIs, add the following triple-slash directive to the top of any test file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)dom.test.ts

```
/// <reference lib="dom" />

import { test, expect } from "bun:test";

test("dom test", () => {
  document.body.innerHTML = `<button>My button</button>`;
  const button = document.querySelector("button");
  expect(button?.innerText).toEqual("My button");
});
```

Let’s run this test with `bun test`:

terminal

```
bun test
```

```
bun test v1.3.3

dom.test.ts:
✓ dom test [0.82ms]

 1 pass
 0 fail
 1 expect() calls
Ran 1 tests across 1 files. 1 total [125.00ms]
```

## React Testing Library

Bun works seamlessly with React Testing Library for testing React components. After setting up happy-dom as shown above, you can install and use React Testing Library normally.

terminal

```
bun add -d @testing-library/react @testing-library/jest-dom
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)component.test.tsx

```
/// <reference lib="dom" />

import { test, expect } from 'bun:test';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';

function Button({ children }: { children: React.ReactNode }) {
  return <button>{children}</button>;
}

test('renders button', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByRole('button')).toHaveTextContent('Click me');
});
```

## Advanced DOM Testing

### Custom Elements

You can test custom elements and web components using the same setup:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)custom-element.test.ts

```
/// <reference lib="dom" />

import { test, expect } from "bun:test";

test("custom element", () => {
  // Define a custom element
  class MyElement extends HTMLElement {
    constructor() {
      super();
      this.innerHTML = "<p>Custom element content</p>";
    }
  }

  customElements.define("my-element", MyElement);

  // Use it in tests
  document.body.innerHTML = "<my-element></my-element>";
  const element = document.querySelector("my-element");
  expect(element?.innerHTML).toBe("<p>Custom element content</p>");
});
```

### Event Testing

Test DOM events and user interactions:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)events.test.ts

```
/// <reference lib="dom" />

import { test, expect } from "bun:test";

test("button click event", () => {
  let clicked = false;

  document.body.innerHTML = '<button id="test-btn">Click me</button>';
  const button = document.getElementById("test-btn");

  button?.addEventListener("click", () => {
    clicked = true;
  });

  button?.click();
  expect(clicked).toBe(true);
});
```

## Configuration Tips

### Global Setup

For more complex DOM testing setups, you can create a more comprehensive preload file:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test-setup.ts

```
import { GlobalRegistrator } from "@happy-dom/global-registrator";
import "@testing-library/jest-dom";

// Register happy-dom globals
GlobalRegistrator.register();

// Add any global test configuration here
global.ResizeObserver = class ResizeObserver {
  observe() {}
  unobserve() {}
  disconnect() {}
};

// Mock other APIs as needed
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});
```

Then update your `bunfig.toml`:

bunfig.toml

```
[test]
preload = ["./test-setup.ts"]
```

## Troubleshooting

### Common Issues

**TypeScript errors for DOM APIs**: Make sure to include the `/// <reference lib="dom" />` directive at the top of your test files. **Missing globals**: Ensure that `@happy-dom/global-registrator` is properly imported and registered in your preload file. **React component rendering issues**: Make sure you’ve installed both `@testing-library/react` and have happy-dom set up correctly.

### Performance Considerations

Happy-dom is fast, but for very large test suites, you might want to:

*   Use `beforeEach` to reset the DOM state between tests
*   Avoid creating too many DOM elements in a single test
*   Consider using `cleanup` functions from testing libraries

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test-setup.ts

```
import { afterEach } from "bun:test";
import { cleanup } from "@testing-library/react";

afterEach(() => {
  cleanup();
  document.body.innerHTML = "";
});
```
