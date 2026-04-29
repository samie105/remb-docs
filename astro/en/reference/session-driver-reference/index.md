---
title: "Astro Session Driver API"
source: "https://docs.astro.build/en/reference/session-driver-reference/"
canonical_url: "https://docs.astro.build/en/reference/session-driver-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:00.769Z"
content_hash: "e4778f5c5d3d48630282f66da5467c2f7ff248f36a984c6466f41a4615fa9ccf"
menu_path: ["Astro Session Driver API"]
section_path: []
nav_prev: {"path": "astro/en/reference/dev-toolbar-app-reference/index.md", "title": "Dev Toolbar App API"}
nav_next: {"path": "astro/en/reference/font-provider-reference/index.md", "title": "Astro Font Provider API"}
---

# Astro Session Driver API

Astro [sessions](../../guides/sessions/index.md) allow to share data between requests for on-demand rendered pages. They require an Astro Session Driver to store session data.

## Built-in drivers

[Section titled “Built-in drivers”](#built-in-drivers)

Astro exports built-in session drivers from `astro/config`:

```
import { sessionDrivers } from 'astro/config'
```

Any [unstorage driver](https://unstorage.unjs.io/drivers) can be used, for example:

```
import { defineConfig, sessionDrivers } from 'astro/config'
export default defineConfig({    session: {        driver: sessionDrivers.redis({            url: process.env.REDIS_URL        }),    }})
```

## Building a session driver

[Section titled “Building a session driver”](#building-a-session-driver)

A session driver is made of two parts:

*   The [driver config](#the-session-driver-config), which lets Astro know what implementation to use at runtime and what config to forward
*   The [driver implementation](#the-session-driver-implementation), which handles the storage logic at runtime

### The session driver config

[Section titled “The session driver config”](#the-session-driver-config)

A `SessionDriverConfig` is an object containing a required runtime [`entrypoint`](#entrypoint) and an optional [`config`](#config). The preferred method for implementing it is to export a function that returns this object and takes the configuration as an optional parameter.

The following example defines a memory driver config:

```
import type { SessionDriverConfig } from 'astro'
export interface Config {    max?: number;}
export function memoryDriver(config: Config = {}): SessionDriverConfig {    return {        entrypoint: new URL('./runtime.js', import.meta.url),        config,    }}
```

It is then registered in the Astro config:

```
import { defineConfig } from 'astro/config'import { memoryDriver } from './driver/config'
export default defineConfig({    session: {        driver: memoryDriver({            max: 500        })    }})
```

#### `entrypoint`

[Section titled “entrypoint”](#entrypoint)

**Type:** `string | URL`

**Added in:** `astro@6.0.0`

Defines the entrypoint for the [driver implementation](#the-session-driver-implementation).

#### `config`

[Section titled “config”](#config)

**Type:** `Record<string, any> | undefined`

**Added in:** `astro@6.0.0`

Defines the serializable config passed to [driver implementation](#the-session-driver-implementation) at runtime.

### The session driver implementation

[Section titled “The session driver implementation”](#the-session-driver-implementation)

A `SessionDriver` is an object responsible for [storing](#setitem), [retrieving](#getitem) and [deleting](#removeitem) data when [using sessions at runtime](../api-reference/index.md#session) (e.g. `context.session.set()`). You can implement it in your session driver module by exporting a default function that takes the [driver config](#config) as parameter.

The following example implements a memory driver:

```
import type { SessionDriver } from 'astro'import type { Config } from './config'import { LRUCache } from 'lru-cache'
export default function(config: Config): SessionDriver {    const cache = new LRUCache({ max: config.max })    return {        setItem: async (key, value) => {            cache.set(key, value)        },        getItem: async (key) => {            return cache.get(key)        },        removeItem: async (key) => {            cache.delete(key)        },    }}
```

#### `setItem()`

[Section titled “setItem()”](#setitem)

**Type:** `(key: string, value: any) => Promise<void>`

**Added in:** `astro@6.0.0`

Defines a function that sets session data by key.

#### `getItem()`

[Section titled “getItem()”](#getitem)

**Type:** `(key: string) => Promise<any>`

**Added in:** `astro@6.0.0`

Defines a function that retrieves session data by key.

#### `removeItem()`

[Section titled “removeItem()”](#removeitem)

**Type:** `(key: string) => Promise<void>`

**Added in:** `astro@6.0.0`

Defines a function that removes session data by key.

## Unstorage compatibility

[Section titled “Unstorage compatibility”](#unstorage-compatibility)

Unstorage driver types are compatible with Astro’s `SessionDriver` type.

That means you can use an unstorage package export as an [entrypoint](#entrypoint). For example:

```
import type { SessionDriverConfig } from 'astro'
export function configuredRedisDriver(): SessionDriverConfig {    return {        entrypoint: 'unstorage/drivers/redis',        config: {            tls: true        }    }}
```

Alternatively, you can import and use an unstorage driver directly in the implementation. For example:

```
import type { SessionDriver } from 'astro'import redisDriver from "unstorage/drivers/redis";
export default function(config): SessionDriver {    return redisDriver({        ...config,        tls: true    })}
```

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
