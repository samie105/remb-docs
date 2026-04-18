---
title: "Vector set embeddings"
source: "https://redis.io/docs/latest/develop/clients/nodejs/vecsets/"
canonical_url: "https://redis.io/docs/latest/develop/clients/nodejs/vecsets/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:04.927Z"
content_hash: "e356548cb3ea42bd72023fd5abd08f0b8726374df61aa7f74dd0726adeab1dee"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Vector set embeddings","→","Vector set embeddings"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)","→\n      \n        Vector set embeddings","→","Vector set embeddings"]
nav_prev: {"path": "redis/docs/latest/develop/ai/redisvl/user_guide/vectorizers/index.md", "title": "Vectorizers"}
nav_next: {"path": "redis/docs/latest/develop/whats-new/8-2/index.md", "title": "Redis 8.2"}
---

# Vector set embeddings

Index and query embeddings with Redis vector sets

A Redis [vector set](/docs/latest/develop/data-types/vector-sets/) lets you store a set of unique keys, each with its own associated vector. You can then retrieve keys from the set according to the similarity between their stored vectors and a query vector that you specify.

You can use vector sets to store any type of numeric vector but they are particularly optimized to work with text embedding vectors (see [Redis for AI](/docs/latest/develop/ai/) to learn more about text embeddings). The example below shows how to use the [`@xenova/transformers`](https://www.npmjs.com/package/@xenova/transformers) library to generate vector embeddings and then store and retrieve them using a vector set with `node-redis`.

## Initialize

Start by [installing](/docs/latest/develop/clients/nodejs/#install) `node-redis` if you haven't already done so. Also, install `@xenova/transformers`:

```bash
npm install @xenova/transformers
```

In your JavaScript source file, import the required classes:

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

The first of these imports is the `@xenova/transformers` class, which generates an embedding from a section of text. This example uses `transformers.pipeline` with the [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model for the embeddings. This model generates vectors with 384 dimensions, regardless of the length of the input text, but note that the input is truncated to 256 tokens (see [Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6) at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens are related to the original text).

The output from `transformers.pipeline` is a function (called `pipe` in the examples) that you can call to generate embeddings. The `pipeOptions` object is a parameter for `pipe` that specifies how to generate sentence embeddings from token embeddings (see the [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) documentation for details).

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

## Create the data

The example data is contained in an object with some brief descriptions of famous people:

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

## Add the data to a vector set

The next step is to connect to Redis and add the data to a new vector set.

The code below iterates through all the key-value pairs in the `peopleData` object and adds corresponding elements to a vector set called `famousPeople`.

Use the `pipe()` function created above to generate the embedding and then use `Array.from()` to convert the embedding to an array of `float32` values that you can pass to the [`vAdd()`](/docs/latest/commands/vadd/) command to set the embedding.

The call to `vAdd()` also adds the `born` and `died` values from the `peopleData` object as attribute data. You can access this during a query or by using the [`vGetAttr()`](/docs/latest/commands/vgetattr/) method.

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

## Query the vector set

You can now query the data in the set. The basic approach is to use the `pipe()` function to generate another embedding vector for the query text. (This is the same method used to add the elements to the set.) Then, pass the query vector to [`vSim()`](/docs/latest/commands/vsim/) to return elements of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

This returns the following list of elements (formatted slightly for clarity):

```
'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
    "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
    "Marie Curie","Paul Erdos"]
```

The first two people in the list are the two actors, as expected, but none of the people from Linus Pauling onward was especially well-known for acting (and there certainly isn't any information about that in the short description text). As it stands, the search attempts to rank all the elements in the set, based on the information contained in the embedding model. You can use the `COUNT` parameter of `vSim()` to limit the list of elements to just the most relevant few items:

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

The reason for using text embeddings rather than simple text search is that the embeddings represent semantic information. This allows a query to find elements with a similar meaning even if the text is different. For example, the word "entertainer" doesn't appear in any of the descriptions but if you use it as a query, the actors and musicians are ranked highest in the results list:

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

Similarly, if you use "science" as a query, you get the following results:

```
'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani","Paul Erdos",
"Marie Fredriksson","Masako Natsume","Freddie Mercury","Chaim Topol"]
```

The scientists are ranked highest but they are then followed by the mathematicians. This seems reasonable given the connection between mathematics and science.

You can also use [filter expressions](/docs/latest/develop/data-types/vector-sets/filtered-search/) with `vSim()` to restrict the search further. For example, repeat the "science" query, but this time limit the results to people who died before the year 2000:

```node.js
import * as transformers from '@xenova/transformers';
import { createClient } from 'redis';

const pipe = await transformers.pipeline(
    'feature-extraction', 'Xenova/all-MiniLM-L6-v2'
);

const pipeOptions = {
    pooling: 'mean',
    normalize: true,
};

const peopleData = {
    "Marie Curie": {
        "born": 1867, "died": 1934,
        "description": `
        Polish-French chemist and physicist. The only person ever to win
        two Nobel prizes for two different sciences.
        `
    },
    "Linus Pauling": {
        "born": 1901, "died": 1994,
        "description": `
        American chemist and peace activist. One of only two people to win two
        Nobel prizes in different fields (chemistry and peace).
        `
    },
    "Freddie Mercury": {
        "born": 1946, "died": 1991,
        "description": `
        British musician, best known as the lead singer of the rock band
        Queen.
        `
    },
    "Marie Fredriksson": {
        "born": 1958, "died": 2019,
        "description": `
        Swedish multi-instrumentalist, mainly known as the lead singer and
        keyboardist of the band Roxette.
        `
    },
    "Paul Erdos": {
        "born": 1913, "died": 1996,
        "description": `
        Hungarian mathematician, known for his eccentric personality almost
        as much as his contributions to many different fields of mathematics.
        `
    },
    "Maryam Mirzakhani": {
        "born": 1977, "died": 2017,
        "description": `
        Iranian mathematician. The first woman ever to win the Fields medal
        for her contributions to mathematics.
        `
    },
    "Masako Natsume": {
        "born": 1957, "died": 1985,
        "description": `
        Japanese actress. She was very famous in Japan but was primarily
        known elsewhere in the world for her portrayal of Tripitaka in the
        TV series Monkey.
        `
    },
    "Chaim Topol": {
        "born": 1935, "died": 2023,
        "description": `
        Israeli actor and singer, usually credited simply as 'Topol'. He was
        best known for his many appearances as Tevye in the musical Fiddler
        on the Roof.
        `
    }
};

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();

for (const [name, details] of Object.entries(peopleData)) {
    const embedding = await pipe(details.description, pipeOptions);
    const embeddingArray = Array.from(embedding.data);

    await client.vAdd('famousPeople', embeddingArray, name);
    await client.vSetAttr('famousPeople', name, JSON.stringify({
        born: details.born,
        died: details.died
    }));
}

const queryValue = "actors";

const queryEmbedding = await pipe(queryValue, pipeOptions);
const queryArray = Array.from(queryEmbedding.data);

const actorsResults = await client.vSim('famousPeople', queryArray);

console.log(`'actors': ${JSON.stringify(actorsResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue2 = "actors";

const queryEmbedding2 = await pipe(queryValue2, pipeOptions);
const queryArray2 = Array.from(queryEmbedding2.data);

const twoActorsResults = await client.vSim('famousPeople', queryArray2, {
    COUNT: 2
});

console.log(`'actors (2)': ${JSON.stringify(twoActorsResults)}`);
// >>> 'actors (2)': ["Masako Natsume","Chaim Topol"]

const queryValue3 = "entertainer";

const queryEmbedding3 = await pipe(queryValue3, pipeOptions);
const queryArray3 = Array.from(queryEmbedding3.data);

const entertainerResults = await client.vSim('famousPeople', queryArray3);

console.log(`'entertainer': ${JSON.stringify(entertainerResults)}`);
// >>> 'actors': ["Masako Natsume","Chaim Topol","Linus Pauling",
// "Marie Fredriksson","Maryam Mirzakhani","Freddie Mercury",
// "Marie Curie","Paul Erdos"]

const queryValue4 = "science";

const queryEmbedding4 = await pipe(queryValue4, pipeOptions);
const queryArray4 = Array.from(queryEmbedding4.data);

const scienceResults = await client.vSim('famousPeople', queryArray4);

console.log(`'science': ${JSON.stringify(scienceResults)}`);
// >>> 'science': ["Linus Pauling","Marie Curie","Maryam Mirzakhani",
// "Paul Erdos","Marie Fredriksson","Masako Natsume","Freddie Mercury",
// "Chaim Topol"]

const queryValue5 = "science";

const queryEmbedding5 = await pipe(queryValue5, pipeOptions);
const queryArray5 = Array.from(queryEmbedding5.data);

const science2000Results = await client.vSim('famousPeople', queryArray5, {
    FILTER: '.died < 2000'
});

console.log(`'science2000': ${JSON.stringify(science2000Results)}`);
// >>> 'science2000': ["Linus Pauling","Marie Curie","Paul Erdos",
// "Masako Natsume","Freddie Mercury"]

await client.quit();
```

Note that the boolean filter expression is applied to items in the list before the vector distance calculation is performed. Items that don't pass the filter test are removed from the results completely, rather than just reduced in rank. This can help to improve the performance of the search because there is no need to calculate the vector distance for elements that have already been filtered out of the search.

## More information

See the [vector sets](/docs/latest/develop/data-types/vector-sets/) docs for more information and code examples. See the [Redis for AI](/docs/latest/develop/ai/) section for more details about text embeddings and other AI techniques you can use with Redis.

You may also be interested in [vector search](/docs/latest/develop/clients/nodejs/vecsearch/). This is a feature of [Redis Search](/docs/latest/develop/ai/search-and-query/) that lets you retrieve [JSON](/docs/latest/develop/data-types/json/) and [hash](/docs/latest/develop/data-types/hashes/) documents based on vector data stored in their fields.

## On this page
