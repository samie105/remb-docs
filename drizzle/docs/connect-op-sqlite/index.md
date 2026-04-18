---
title: "Drizzle <> OP SQLite"
source: "https://orm.drizzle.team/docs/connect-op-sqlite"
canonical_url: "https://orm.drizzle.team/docs/connect-op-sqlite"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:41.504Z"
content_hash: "38591fc7efa004decd2f13246993d991e6feaf1202824966700b681ac3ce6540"
menu_path: ["Drizzle <> OP SQLite"]
section_path: []
nav_prev: {"path": "drizzle/docs/connect-expo-sqlite/index.md", "title": "Drizzle <> Expo SQLite"}
nav_next: {"path": "drizzle/docs/connect-react-native-sqlite/index.md", "title": "Drizzle <> React Native SQLite"}
---

According to the **[official github page](https://github.com/OP-Engineering/op-sqlite)**, OP-SQLite embeds the latest version of SQLite and provides a low-level API to execute SQL queries.

npm

yarn

pnpm

bun

```
npm i drizzle-orm @op-engineering/op-sqlite
npm i -D drizzle-kit
```

```
yarn add drizzle-orm @op-engineering/op-sqlite
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm @op-engineering/op-sqlite
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm @op-engineering/op-sqlite
bun add -D drizzle-kit
```

```
import { drizzle } from "drizzle-orm/op-sqlite";
import { open } from '@op-engineering/op-sqlite';

const opsqlite = open({
  name: 'myDB',
});
const db = drizzle(opsqlite);

await db.select().from(users);
```

You can use Drizzle Kit for SQL migration generation.  
Please make sure to check how [Drizzle Kit migrations](drizzle/docs/kit-overview/index.md) work before proceeding.  
OP SQLite requires you to have SQL migrations bundled into the app and we’ve got you covered.

#### Install babel plugin[](#install-babel-plugin)

It’s necessary to bundle SQL migration files as string directly to your bundle.

```
npm install babel-plugin-inline-import
```

#### Update config files.[](#update-config-files)

You will need to update `babel.config.js`, `metro.config.js` and `drizzle.config.ts` files

```
module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
    [
      'inline-import',
      {
        extensions: ['.sql'],
      },
    ],
  ],
};
```

```
const { getDefaultConfig } = require('@react-native/metro-config');

const config = getDefaultConfig(__dirname);

config.resolver.sourceExts.push('sql');

module.exports = config;
```

Make sure to have `dialect: 'sqlite'` and `driver: 'expo'` in Drizzle Kit config

```
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
	schema: './db/schema.ts',
	out: './drizzle',
  dialect: 'sqlite',
	driver: 'expo', // <--- very important
});
```

#### Generate migrations[](#generate-migrations)

After creating SQL schema file and drizzle.config.ts file, you can generate migrations

```
npx drizzle-kit generate
```

#### Add migrations to your app[](#add-migrations-to-your-app)

Now you need to import `migrations.js` file into your Expo/React Native app from `./drizzle` folder. You can run migrations on application startup using our custom `useMigrations` migrations hook on in `useEffect` hook manually as you want.

```
import { drizzle } from "drizzle-orm/op-sqlite";
import { open } from '@op-engineering/op-sqlite';
import { useMigrations } from 'drizzle-orm/op-sqlite/migrator';
import migrations from './drizzle/migrations';

const opsqliteDb = open({
  name: 'myDB',
});

const db = drizzle(opsqliteDb);

export default function App() {
  const { success, error } = useMigrations(db, migrations);

  if (error) {
    return (
      <View>
        <Text>Migration error: {error.message}</Text>
      </View>
    );
  }

  if (!success) {
    return (
      <View>
        <Text>Migration is in progress...</Text>
      </View>
    );
  }

  return ...your application component;
}
```
