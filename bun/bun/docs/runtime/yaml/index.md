---
title: "YAML"
source: "https://bun.com/docs/runtime/yaml"
canonical_url: "https://bun.com/docs/runtime/yaml"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:14.139Z"
content_hash: "549a3d7f4060ee8922b0249a12da4e7f74029942c8aa1d3b1e544bc644f7e114"
menu_path: ["YAML"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/workers/index.md", "title": "Workers"}
nav_next: {"path": "bun/bun/docs/test/code-coverage/index.md", "title": "Code coverage"}
---

# Employee record
employee: &emp
  name: Jane Smith
  department: Engineering
  skills:
    - JavaScript
    - TypeScript
    - React

manager: *emp  # Reference to employee

config: !!str 123  # Explicit string type

description: |
  This is a multi-line
  literal string that preserves
  line breaks and spacing.

summary: >
  This is a folded string
  that joins lines with spaces
  unless there are blank lines.
`;

const data = Bun.YAML.parse(yaml);
```

#### Error Handling

`Bun.YAML.parse()` throws a `SyntaxError` if the YAML is invalid:

```
try {
  Bun.YAML.parse("invalid: yaml: content:");
} catch (error) {
  console.error("Failed to parse YAML:", error.message);
}
```

* * *

## Module Import

### ES Modules

You can import YAML files directly as ES modules. The YAML content is parsed and made available as both default and named exports:

config.yaml

```
database:
  host: localhost
  port: 5432
  name: myapp

redis:
  host: localhost
  port: 6379

features:
  auth: true
  rateLimit: true
  analytics: false
```

#### Default Import

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import config from "./config.yaml";

console.log(config.database.host); // "localhost"
console.log(config.redis.port); // 6379
```

#### Named Imports

You can destructure top-level YAML properties as named imports:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import { database, redis, features } from "./config.yaml";

console.log(database.host); // "localhost"
console.log(redis.port); // 6379
console.log(features.auth); // true
```

Or combine both:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import config, { database, features } from "./config.yaml";

// Use the full config object
console.log(config);

// Or use specific parts
if (features.rateLimit) {
  setupRateLimiting(database);
}
```

### CommonJS

YAML files can also be required in CommonJS:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
const config = require("./config.yaml");
console.log(config.database.name); // "myapp"

// Destructuring also works
const { database, redis } = require("./config.yaml");
console.log(database.port); // 5432
```

* * *

## Hot Reloading with YAML

One of the most powerful features of Bun’s YAML support is hot reloading. When you run your application with `bun --hot`, changes to YAML files are automatically detected and reloaded without closing connections

### Configuration Hot Reloading

config.yaml

```
server:
  port: 3000
  host: localhost

features:
  debug: true
  verbose: false
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { server, features } from "./config.yaml";

console.log(`Starting server on ${server.host}:${server.port}`);

if (features.debug) {
  console.log("Debug mode enabled");
}

// Your server code here
Bun.serve({
  port: server.port,
  hostname: server.host,
  fetch(req) {
    if (features.verbose) {
      console.log(`${req.method} ${req.url}`);
    }
    return new Response("Hello World");
  },
});
```

Run with hot reloading:

terminal

```
bun --hot server.ts
```

Now when you modify `config.yaml`, the changes are immediately reflected in your running application. This is perfect for:

*   Adjusting configuration during development
*   Testing different settings without restarts
*   Live debugging with configuration changes
*   Feature flag toggling

* * *

## Configuration Management

### Environment-Based Configuration

YAML excels at managing configuration across different environments:

config.yaml

```
defaults: &defaults
  timeout: 5000
  retries: 3
  cache:
    enabled: true
    ttl: 3600

development:
  <<: *defaults
  api:
    url: http://localhost:4000
    key: dev_key_12345
  logging:
    level: debug
    pretty: true

staging:
  <<: *defaults
  api:
    url: https://staging-api.example.com
    key: ${STAGING_API_KEY}
  logging:
    level: info
    pretty: false

production:
  <<: *defaults
  api:
    url: https://api.example.com
    key: ${PROD_API_KEY}
  cache:
    enabled: true
    ttl: 86400
  logging:
    level: error
    pretty: false
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import configs from "./config.yaml";

const env = process.env.NODE_ENV || "development";
const config = configs[env];

// Environment variables in YAML values can be interpolated
function interpolateEnvVars(obj: any): any {
  if (typeof obj === "string") {
    return obj.replace(/\${(\w+)}/g, (_, key) => process.env[key] || "");
  }
  if (typeof obj === "object") {
    for (const key in obj) {
      obj[key] = interpolateEnvVars(obj[key]);
    }
  }
  return obj;
}

export default interpolateEnvVars(config);
```

### Feature Flags Configuration

features.yaml

```
features:
  newDashboard:
    enabled: true
    rolloutPercentage: 50
    allowedUsers:
      - admin@example.com
      - beta@example.com

  experimentalAPI:
    enabled: false
    endpoints:
      - /api/v2/experimental
      - /api/v2/beta

  darkMode:
    enabled: true
    default: auto # auto, light, dark
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)feature-flags.ts

```
import { features } from "./features.yaml";

export function isFeatureEnabled(featureName: string, userEmail?: string): boolean {
  const feature = features[featureName];

  if (!feature?.enabled) {
    return false;
  }

  // Check rollout percentage
  if (feature.rolloutPercentage < 100) {
    const hash = hashCode(userEmail || "anonymous");
    if (hash % 100 >= feature.rolloutPercentage) {
      return false;
    }
  }

  // Check allowed users
  if (feature.allowedUsers && userEmail) {
    return feature.allowedUsers.includes(userEmail);
  }

  return true;
}

// Use with hot reloading to toggle features in real-time
if (isFeatureEnabled("newDashboard", user.email)) {
  renderNewDashboard();
} else {
  renderLegacyDashboard();
}
```

### Database Configuration

database.yaml

```
connections:
  primary:
    type: postgres
    host: ${DB_HOST:-localhost}
    port: ${DB_PORT:-5432}
    database: ${DB_NAME:-myapp}
    username: ${DB_USER:-postgres}
    password: ${DB_PASS}
    pool:
      min: 2
      max: 10
      idleTimeout: 30000

  cache:
    type: redis
    host: ${REDIS_HOST:-localhost}
    port: ${REDIS_PORT:-6379}
    password: ${REDIS_PASS}
    db: 0

  analytics:
    type: clickhouse
    host: ${ANALYTICS_HOST:-localhost}
    port: 8123
    database: analytics

migrations:
  autoRun: ${AUTO_MIGRATE:-false}
  directory: ./migrations

seeds:
  enabled: ${SEED_DB:-false}
  directory: ./seeds
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)db.ts

```
import { connections, migrations } from "./database.yaml";
import { createConnection } from "./database-driver";

// Parse environment variables with defaults
function parseConfig(config: any) {
  return JSON.parse(
    JSON.stringify(config).replace(
      /\${([^:-]+)(?::([^}]+))?}/g,
      (_, key, defaultValue) => process.env[key] || defaultValue || "",
    ),
  );
}

const dbConfig = parseConfig(connections);

export const db = await createConnection(dbConfig.primary);
export const cache = await createConnection(dbConfig.cache);
export const analytics = await createConnection(dbConfig.analytics);

// Auto-run migrations if configured
if (parseConfig(migrations).autoRun === "true") {
  await runMigrations(db, migrations.directory);
}
```

### Bundler Integration

When you import YAML files in your application and bundle it with Bun, the YAML is parsed at build time and included as a JavaScript module:

terminal

```
bun build app.ts --outdir=dist
```

This means:

*   Zero runtime YAML parsing overhead in production
*   Smaller bundle sizes
*   Tree-shaking support for unused configuration (named imports)

### Dynamic Imports

YAML files can be dynamically imported, useful for loading configuration on demand:

Load configuration based on environment

```
const env = process.env.NODE_ENV || "development";
const { default: config } = await import(`./configs/${env}.yaml`);

// Load user-specific settings
async function loadUserSettings(userId: string) {
  try {
    const settings = await import(`./users/${userId}/settings.yaml`);
    return settings.default;
  } catch {
    const { default: defaults } = await import("./users/default-settings.yaml");
    return defaults;
  }
}
```

