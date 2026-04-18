---
title: "Index and query documents"
source: "https://redis.io/docs/latest/develop/clients/nodejs/queryjson/"
canonical_url: "https://redis.io/docs/latest/develop/clients/nodejs/queryjson/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:43.487Z"
content_hash: "7b1baf1814137ae1a7b66d82dbdb7c616e938ef8444f2ac8ad3afc78c44ee9ec"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Index and query documents","→","Index and query documents"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Index and query documents","→","Index and query documents"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/json/indexing_json/index.md", "title": "Index/Search JSON documents"}
nav_next: {"path": "redis/docs/latest/integrate/riot/install/index.md", "title": "Install"}
---

# Index and query documents

Learn how to use Redis Search with JSON and hash documents.

This example shows how to create a [search index](/docs/latest/develop/ai/search-and-query/indexing/) for [JSON](/docs/latest/develop/data-types/json/) documents and run queries against the index. It then goes on to show the slight differences in the equivalent code for [hash](/docs/latest/develop/data-types/hashes/) documents.

Note:

From [v5.0.0](https://github.com/redis/node-redis/releases/tag/redis%405.0.0) onwards, `node-redis` uses query dialect 2 by default. Redis Search methods such as [`ft.search()`](/docs/latest/commands/ft.search/) will explicitly request this dialect, overriding the default set for the server. See [Query dialects](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/) for more information.

## Initialize

Make sure that you have [Redis Open Source](/docs/latest/operate/oss_and_stack/) or another Redis server available. Also install the [`node-redis`](/docs/latest/develop/clients/nodejs/) client library if you haven't already done so.

Add the following dependencies:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## Create data

Create some test data to add to your database. The example data shown below is compatible with both JSON and hash objects.

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## Add the index

Connect to your Redis database. The code below shows the most basic connection but see [Connect to the server](/docs/latest/develop/clients/nodejs/connect/) to learn more about the available connection options.

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](/docs/latest/develop/ai/search-and-query/query/).

First, drop any existing index to avoid a collision. (The callback is required to avoid an error if the index doesn't already exist.)

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

Then create the index:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## Add the data

Add the three sets of user data to the database as [JSON](/docs/latest/develop/data-types/json/) objects. If you use keys with the `user:` prefix then Redis will index the objects automatically as you add them. Note that placing the commands in a `Promise.all()` call is an easy way to create a [pipeline](/docs/latest/develop/clients/nodejs/transpipe/), which is more efficient than sending the commands individually.

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## Query the data

You can now use the index to search the JSON objects. The [query](/docs/latest/develop/ai/search-and-query/query/) below searches for objects that have the text "Paul" in any field and have an `age` value in the range 30 to 40:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

Specify query options to return only the `city` field:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

Use an [aggregation query](/docs/latest/develop/ai/search-and-query/query/aggregation/) to count all users in each city.

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you need to specify some slightly different options.

When you create the schema for a hash index, you don't need to add aliases for the fields, since you use the basic names to access the fields anyway. Also, you must use `HASH` for the `ON` option when you create the index. The code below shows these changes with a new index called `hash-idx:users`, which is otherwise the same as the `idx:users` index used for JSON documents in the previous examples.

First, drop any existing index to avoid a collision.

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

Then create the new index:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

You use [`hSet()`](/docs/latest/commands/hset/) to add the hash documents instead of [`json.set()`](/docs/latest/commands/json.set/), but the same flat `userX` objects work equally well with either hash or JSON:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

The query commands work the same here for hash as they do for JSON (but the name of the hash index is different). The format of the result is also the same:

```node.js
import {
    createClient,
    SCHEMA_FIELD_TYPE,
    FT_AGGREGATE_GROUP_BY_REDUCERS,
    FT_AGGREGATE_STEPS,
} from 'redis';

const user1 = {
    name: 'Paul John',
    email: 'paul.john@example.com',
    age: 42,
    city: 'London'
};

const user2 = {
    name: 'Eden Zamir',
    email: 'eden.zamir@example.com',
    age: 29,
    city: 'Tel Aviv'
};

const user3 = {
    name: 'Paul Zamir',
    email: 'paul.zamir@example.com',
    age: 35,
    city: 'Tel Aviv'
};

const client = await createClient();
await client.connect();

await client.ft.dropIndex('idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('idx:users', {
    '$.name': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'name'
    },
    '$.city': {
        type: SCHEMA_FIELD_TYPE.TEXT,
        AS: 'city'
    },
    '$.age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC,
        AS: 'age'
    }
}, {
    ON: 'JSON',
    PREFIX: 'user:'
});

const [user1Reply, user2Reply, user3Reply] = await Promise.all([
    client.json.set('user:1', '$', user1),
    client.json.set('user:2', '$', user2),
    client.json.set('user:3', '$', user3)
]);

let findPaulResult = await client.ft.search('idx:users', 'Paul @age:[30 40]');

console.log(findPaulResult.total); // >>> 1

findPaulResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: user:3, name: Paul Zamir, age: 35

let citiesResult = await client.ft.search('idx:users', '*',{
    RETURN: 'city'
});

console.log(citiesResult.total); // >>> 3

citiesResult.documents.forEach(cityDoc => {
    console.log(cityDoc.value);
});
// >>> { city: 'London' }
// >>> { city: 'Tel Aviv' }
// >>> { city: 'Tel Aviv' }

let aggResult = await client.ft.aggregate('idx:users', '*', {
    STEPS: [{
        type: FT_AGGREGATE_STEPS.GROUPBY,
        properties: '@city',
        REDUCE: [{
            type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
            AS: 'count'
        }]
    }]
});

console.log(aggResult.total); // >>> 2

aggResult.results.forEach(result => {
    console.log(`${result.city} - ${result.count}`);
});
// >>> London - 1
// >>> Tel Aviv - 2

await client.ft.dropIndex('hash-idx:users', { DD: true }).then(() => {}, () => {});

await client.ft.create('hash-idx:users', {
    'name': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'city': {
        type: SCHEMA_FIELD_TYPE.TEXT
    },
    'age': {
        type: SCHEMA_FIELD_TYPE.NUMERIC
    }
}, {
    ON: 'HASH',
    PREFIX: 'huser:'
});

const [huser1Reply, huser2Reply, huser3Reply] = await Promise.all([
    client.hSet('huser:1', user1),
    client.hSet('huser:2', user2),
    client.hSet('huser:3', user3)
]);

let findPaulHashResult = await client.ft.search(
    'hash-idx:users', 'Paul @age:[30 40]'
);

console.log(findPaulHashResult.total); // >>> 1

findPaulHashResult.documents.forEach(doc => {
    console.log(`ID: ${doc.id}, name: ${doc.value.name}, age: ${doc.value.age}`);
});
// >>> ID: huser:3, name: Paul Zamir, age: 35

await client.quit();
```

## More information

See the [Redis Search](/docs/latest/develop/ai/search-and-query/) docs for a full description of all query features with examples.

## On this page


