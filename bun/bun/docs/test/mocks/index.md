---
title: "Mocks"
source: "https://bun.com/docs/test/mocks"
canonical_url: "https://bun.com/docs/test/mocks"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:37.983Z"
content_hash: "2bd2a623b44b2c268730acc5cb56775d58bc732b8da2b4cdd9b1dadfbc1eda3f"
menu_path: ["Mocks"]
section_path: []
nav_prev: {"path": "bun/bun/docs/test/lifecycle/index.md", "title": "Lifecycle hooks"}
nav_next: {"path": "bun/bun/docs/test/reporters/index.md", "title": "Test Reporters"}
---

# Load these modules before running tests.
preload = ["./my-preload"]
```

### Module Mock Best Practices

#### When to Use Preload

**What happens if I mock a module that’s already been imported?** If you mock a module that’s already been imported, the module will be updated in the module cache. This means that any modules that import the module will get the mocked version, BUT the original module will still have been evaluated. That means that any side effects from the original module will still have happened. If you want to prevent the original module from being evaluated, you should use `--preload` to load your mocks before your tests run.

#### Practical Module Mock Examples

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)api-client.test.ts

```
import { test, expect, mock, beforeEach } from "bun:test";

// Mock the API client module
mock.module("./api-client", () => ({
  fetchUser: mock(async (id: string) => ({ id, name: `User ${id}` })),
  createUser: mock(async (user: any) => ({ ...user, id: "new-id" })),
  updateUser: mock(async (id: string, user: any) => ({ ...user, id })),
}));

test("user service with mocked API", async () => {
  const { fetchUser } = await import("./api-client");
  const { UserService } = await import("./user-service");

  const userService = new UserService();
  const user = await userService.getUser("123");

  expect(fetchUser).toHaveBeenCalledWith("123");
  expect(user.name).toBe("User 123");
});
```

#### Mocking External Dependencies

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)database.test.ts

```
import { test, expect, mock } from "bun:test";

// Mock external database library
mock.module("pg", () => ({
  Client: mock(function () {
    return {
      connect: mock(async () => {}),
      query: mock(async (sql: string) => ({
        rows: [{ id: 1, name: "Test User" }],
      })),
      end: mock(async () => {}),
    };
  }),
}));

test("database operations", async () => {
  const { Database } = await import("./database");
  const db = new Database();

  const users = await db.getUsers();
  expect(users).toHaveLength(1);
  expect(users[0].name).toBe("Test User");
});
```

## Global Mock Functions

### Clear All Mocks

Reset all mock function state (calls, results, etc.) without restoring their original implementation:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { expect, mock, test } from "bun:test";

const random1 = mock(() => Math.random());
const random2 = mock(() => Math.random());

test("clearing all mocks", () => {
  random1();
  random2();

  expect(random1).toHaveBeenCalledTimes(1);
  expect(random2).toHaveBeenCalledTimes(1);

  mock.clearAllMocks();

  expect(random1).toHaveBeenCalledTimes(0);
  expect(random2).toHaveBeenCalledTimes(0);

  // Note: implementations are preserved
  expect(typeof random1()).toBe("number");
  expect(typeof random2()).toBe("number");
});
```

This resets the `.mock.calls`, `.mock.instances`, `.mock.contexts`, and `.mock.results` properties of all mocks, but unlike `mock.restore()`, it does not restore the original implementation.

### Restore All Mocks

Instead of manually restoring each mock individually with `mockFn.mockRestore()`, restore all mocks with one command by calling `mock.restore()`. Doing so does not reset the value of modules overridden with `mock.module()`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { expect, mock, spyOn, test } from "bun:test";

import * as fooModule from "./foo.ts";
import * as barModule from "./bar.ts";
import * as bazModule from "./baz.ts";

test("foo, bar, baz", () => {
  const fooSpy = spyOn(fooModule, "foo");
  const barSpy = spyOn(barModule, "bar");
  const bazSpy = spyOn(bazModule, "baz");

  // Original implementations still work
  expect(fooModule.foo()).toBe("foo");
  expect(barModule.bar()).toBe("bar");
  expect(bazModule.baz()).toBe("baz");

  // Mock implementations
  fooSpy.mockImplementation(() => 42);
  barSpy.mockImplementation(() => 43);
  bazSpy.mockImplementation(() => 44);

  expect(fooModule.foo()).toBe(42);
  expect(barModule.bar()).toBe(43);
  expect(bazModule.baz()).toBe(44);

  // Restore all
  mock.restore();

  expect(fooModule.foo()).toBe("foo");
  expect(barModule.bar()).toBe("bar");
  expect(bazModule.baz()).toBe("baz");
});
```

Using `mock.restore()` can reduce the amount of code in your tests by adding it to `afterEach` blocks in each test file or even in your test preload code.

## Vitest Compatibility

For added compatibility with tests written for Vitest, Bun provides the `vi` object as an alias for parts of the Jest mocking API:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect, vi } from "bun:test";

// Using the 'vi' alias similar to Vitest
test("vitest compatibility", () => {
  const mockFn = vi.fn(() => 42);

  mockFn();
  expect(mockFn).toHaveBeenCalled();

  // The following functions are available on the vi object:
  // vi.fn
  // vi.spyOn
  // vi.mock
  // vi.restoreAllMocks
  // vi.clearAllMocks
});
```

This makes it easier to port tests from Vitest to Bun without having to rewrite all your mocks.

## Implementation Details

Understanding how `mock.module()` works helps you use it more effectively:

### Cache Interaction

Module mocks interact with both ESM and CommonJS module caches.

### Lazy Evaluation

The mock factory callback is only evaluated when the module is actually imported or required.

### Path Resolution

Bun automatically resolves the module specifier as though you were doing an import, supporting:

*   Relative paths (`'./module'`)
*   Absolute paths (`'/path/to/module'`)
*   Package names (`'lodash'`)

### Import Timing Effects

*   **When mocking before first import**: No side effects from the original module occur
*   **When mocking after import**: The original module’s side effects have already happened

For this reason, using `--preload` is recommended for mocks that need to prevent side effects.

### Live Bindings

Mocked ESM modules maintain live bindings, so changing the mock will update all existing imports.

## Advanced Patterns

### Factory Functions

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { mock } from "bun:test";

function createMockUser(overrides = {}) {
  return {
    id: "mock-id",
    name: "Mock User",
    email: "mock@example.com",
    ...overrides,
  };
}

const mockUserService = {
  getUser: mock(async (id: string) => createMockUser({ id })),
  createUser: mock(async (data: any) => createMockUser(data)),
  updateUser: mock(async (id: string, data: any) => createMockUser({ id, ...data })),
};
```

### Conditional Mocking

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { test, expect, mock } from "bun:test";

const shouldUseMockApi = process.env.NODE_ENV === "test";

if (shouldUseMockApi) {
  mock.module("./api", () => ({
    fetchData: mock(async () => ({ data: "mocked" })),
  }));
}

test("conditional API usage", async () => {
  const { fetchData } = await import("./api");
  const result = await fetchData();

  if (shouldUseMockApi) {
    expect(result.data).toBe("mocked");
  }
});
```

### Mock Cleanup Patterns

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
import { afterEach, beforeEach } from "bun:test";

beforeEach(() => {
  // Set up common mocks
  mock.module("./logger", () => ({
    log: mock(() => {}),
    error: mock(() => {}),
    warn: mock(() => {}),
  }));
});

afterEach(() => {
  // Clean up all mocks
  mock.restore();
  mock.clearAllMocks();
});
```

## Best Practices

### Keep Mocks Simple

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
// Good: Simple, focused mock
const mockUserApi = {
  getUser: mock(async id => ({ id, name: "Test User" })),
};

// Avoid: Overly complex mock behavior
const complexMock = mock(input => {
  if (input.type === "A") {
    return processTypeA(input);
  } else if (input.type === "B") {
    return processTypeB(input);
  }
  // ... lots of complex logic
});
```

### Use Type-Safe Mocks

```
interface UserService {
  getUser(id: string): Promise<User>;
  createUser(data: CreateUserData): Promise<User>;
}

const mockUserService: UserService = {
  getUser: mock(async (id: string) => ({ id, name: "Test User" })),
  createUser: mock(async data => ({ id: "new-id", ...data })),
};
```

### Test Mock Behavior

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)test.ts

```
test("service calls API correctly", async () => {
  const mockApi = { fetchUser: mock(async () => ({ id: "1" })) };

  const service = new UserService(mockApi);
  await service.getUser("123");

  // Verify the mock was called correctly
  expect(mockApi.fetchUser).toHaveBeenCalledWith("123");
  expect(mockApi.fetchUser).toHaveBeenCalledTimes(1);
});
```

## Notes

### Auto-mocking

`__mocks__` directory and auto-mocking are not supported yet. If this is blocking you from switching to Bun, please [file an issue](https://github.com/oven-sh/bun/issues).

### ESM vs CommonJS

Module mocks have different implementations for ESM and CommonJS modules. For ES Modules, Bun has added patches to JavaScriptCore that allow Bun to override export values at runtime and update live bindings recursively.
