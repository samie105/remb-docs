---
title: "Vector set embeddings"
source: "https://redis.io/docs/latest/develop/clients/jedis/vecsets/"
canonical_url: "https://redis.io/docs/latest/develop/clients/jedis/vecsets/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:57.524Z"
content_hash: "95a91164c99f6e9a8ceb123b23c6f48e85de272cfb9e7ec9a8df6730e9807c08"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Vector set embeddings","→","Vector set embeddings"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Vector set embeddings","→","Vector set embeddings"]
nav_prev: {"path": "../vecsearch/index.md", "title": "Index and query vectors"}
nav_next: {"path": "../../lettuce/index.md", "title": "Lettuce guide (Java)"}
---

# Vector set embeddings

Index and query embeddings with Redis vector sets

A Redis [vector set](/docs/latest/develop/data-types/vector-sets/) lets you store a set of unique keys, each with its own associated vector. You can then retrieve keys from the set according to the similarity between their stored vectors and a query vector that you specify.

You can use vector sets to store any type of numeric vector but they are particularly optimized to work with text embedding vectors (see [Redis for AI](/docs/latest/develop/ai/) to learn more about text embeddings). The example below shows how to generate vector embeddings and then store and retrieve them using a vector set with `Jedis`.

## Initialize

If you are using [Maven](https://maven.apache.org/), add the following dependencies to your `pom.xml` file (note that you need `Jedis` v6.2.0 or later to use vector sets):

```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>7.2.0</version>
</dependency>

<dependency>
    <groupId>ai.djl.huggingface</groupId>
    <artifactId>tokenizers</artifactId>
    <version>0.33.0</version>
</dependency>

<dependency>
    <groupId>ai.djl.pytorch</groupId>
    <artifactId>pytorch-model-zoo</artifactId>
    <version>0.33.0</version>
</dependency>

<dependency>
    <groupId>ai.djl</groupId>
    <artifactId>api</artifactId>
    <version>0.33.0</version>
</dependency>
```

If you are using [Gradle](https://gradle.org/), add the following dependencies to your `build.gradle` file:

```bash
compileOnly 'redis.clients:jedis:7.2.0'
compileOnly 'ai.djl.huggingface:tokenizers:0.33.0'
compileOnly 'ai.djl.pytorch:pytorch-model-zoo:0.33.0'
compileOnly 'ai.djl:api:0.33.0'
```

In a new Java file, import the required classes:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

The imports include the classes required to generate embeddings from text. This example uses an instance of the `Predictor` class with the [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model for the embeddings. This model generates vectors with 384 dimensions, regardless of the length of the input text, but note that the input is truncated to 256 tokens (see [Word piece tokenization](https://huggingface.co/learn/nlp-course/en/chapter6/6) at the [Hugging Face](https://huggingface.co/) docs to learn more about the way tokens are related to the original text).

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

## Create the data

The example data is contained in a `List<Person>` object with some brief descriptions of famous people.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

## Add the data to a vector set

The code below connects to Redis, then iterates through all the items in the `people` list, generates embeddings for each person's description, and then adds the appropriate elements to a vector set called `famousPeople`. Note that the `predict()` call is in a `try`/`catch` block because it can throw exceptions if it can't download the embedding model (you should add code to handle the exceptions for production).

The call to `vadd()` also adds the `born` and `died` values from the original `people` list as attribute data. You can access this during a query or by using the [`vgetattr()`](/docs/latest/commands/vgetattr/) method.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

## Query the vector set

You can now query the data in the set. The basic approach is to use the `predict()` method to generate another embedding vector for the query text. (This is the same method used to add the elements to the set.) Then, pass the query vector to [`vsim()`](/docs/latest/commands/vsim/) to return elements of the set, ranked in order of similarity to the query.

Start with a simple query for "actors":

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

This returns the following list of elements (formatted slightly for clarity):

```
['Masako Natsume', 'Chaim Topol', 'Linus Pauling',
'Marie Fredriksson', 'Maryam Mirzakhani', 'Marie Curie',
'Freddie Mercury', 'Paul Erdos']
```

The first two people in the list are the two actors, as expected, but none of the people from Linus Pauling onward was especially well-known for acting (and there certainly isn't any information about that in the short description text). As it stands, the search attempts to rank all the elements in the set, based on the information contained in the embedding model. You can use the `count` parameter of `vsim()` to limit the list of elements to just the most relevant few items:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

The reason for using text embeddings rather than simple text search is that the embeddings represent semantic information. This allows a query to find elements with a similar meaning even if the text is different. For example, the word "entertainer" doesn't appear in any of the descriptions, but if you use it as a query, the actors and musicians are ranked highest in the results list:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

Similarly, if you use "science" as a query, you get the following results:

```
['Marie Curie', 'Linus Pauling', 'Maryam Mirzakhani',
'Paul Erdos', 'Marie Fredriksson', 'Freddie Mercury', 'Masako Natsume',
'Chaim Topol']
```

The scientists are ranked highest, followed by the mathematicians. This ranking seems reasonable given the connection between mathematics and science.

You can also use [filter expressions](/docs/latest/develop/data-types/vector-sets/filtered-search/) with `vsim()` to restrict the search further. For example, repeat the "science" query, but this time limit the results to people who died before the year 2000:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.params.VAddParams;
import redis.clients.jedis.params.VSimParams;

import java.util.*;

// DJL classes for model loading and inference.
import ai.djl.huggingface.translator.TextEmbeddingTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.repository.zoo.Criteria;
import ai.djl.training.util.ProgressBar;

public class HomeVecSets {

        Predictor<String, float[]> predictor = null;

        try {
            Criteria<String, float[]> criteria = Criteria.builder().setTypes(String.class, float[].class)
                    .optModelUrls("djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2")
                    .optEngine("PyTorch").optTranslatorFactory(new TextEmbeddingTranslatorFactory())
                    .optProgress(new ProgressBar()).build();

            predictor = criteria.loadModel().newPredictor();
        } catch (Exception e) {
            // ...
        }

        final class Person {
            final String name;
            final int born;
            final int died;
            final String description;
            Person(String name, int born, int died, String description) {
                this.name = name; this.born = born; this.died = died; this.description = description;
            }
        }

        List<Person> people = Arrays.asList(
            new Person(
                "Marie Curie",
                1867, 1934,
                "Polish-French chemist and physicist. The only person ever to win" +
                " two Nobel prizes for two different sciences."
            ),
            new Person(
                "Linus Pauling",
                1901, 1994,
                "American chemist and peace activist. One of only two people to" +
                " win two Nobel prizes in different fields (chemistry and peace)."
            ),
            new Person(
                "Freddie Mercury",
                1946, 1991,
                "British musician, best known as the lead singer of the rock band Queen."
            ),
            new Person(
                "Marie Fredriksson",
                1958, 2019,
                "Swedish multi-instrumentalist, mainly known as the lead singer and" +
                " keyboardist of the band Roxette."
            ),
            new Person(
                "Paul Erdos",
                1913, 1996,
                "Hungarian mathematician, known for his eccentric personality almost" +
                " as much as his contributions to many different fields of mathematics."
            ),
            new Person(
                "Maryam Mirzakhani",
                1977, 2017,
                "Iranian mathematician. The first woman ever to win the Fields medal" +
                " for her contributions to mathematics."
            ),
            new Person(
                "Masako Natsume",
                1957, 1985,
                "Japanese actress. She was very famous in Japan but was primarily" +
                " known elsewhere in the world for her portrayal of Tripitaka in the" +
                " TV series Monkey."
            ),
            new Person(
                "Chaim Topol",
                1935, 2023,
                "Israeli actor and singer, usually credited simply as 'Topol'. He was" +
                " best known for his many appearances as Tevye in the musical Fiddler" +
                " on the Roof."
            )
        );

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        for (Person person : people) {
            float[] embedding;
            try {
                embedding = predictor.predict(person.description);
            } catch (Exception e) {
                // This just allows the code to compile without errors.
                // In a real-world scenario, you would handle the exception properly.
                embedding = new float[384];
            }

            // Add element with attributes using VAddParams
            String attrs = String.format("{\"born\": %d, \"died\": %d}", person.born, person.died);
            boolean added = jedis.vadd("famousPeople", embedding, person.name, new VAddParams().setAttr(attrs));
            System.out.println(added); // >>> true
        }

        float[] actorsEmbedding;
        try {
            actorsEmbedding = predictor.predict("actors");
        } catch (Exception e) {
            actorsEmbedding = new float[384];
        }

        List<String> basicResults = jedis.vsim("famousPeople", actorsEmbedding);
        System.out.println(basicResults);
        // >>> [Masako Natsume, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Maryam Mirzakhani, Marie Curie, Freddie Mercury, Paul Erdos]

        VSimParams limitParams = new VSimParams().count(2);
        List<String> limitedResults = jedis.vsim("famousPeople", actorsEmbedding, limitParams);
        System.out.println(limitedResults);
        // >>> [Masako Natsume, Chaim Topol]

        float[] entertainerEmbedding;
        try {
            entertainerEmbedding = predictor.predict("entertainers");
        } catch (Exception e) {
            entertainerEmbedding = new float[384];
        }

        List<String> entertainerResults = jedis.vsim("famousPeople", entertainerEmbedding);
        System.out.println(entertainerResults);
        // >>> [Freddie Mercury, Chaim Topol, Linus Pauling, Marie Fredriksson,
        // >>> Masako Natsume, Paul Erdos, Maryam Mirzakhani, Marie Curie]

        float[] scienceEmbedding;
        try {
            scienceEmbedding = predictor.predict("science");
        } catch (Exception e) {
            scienceEmbedding = new float[384];
        }

        List<String> scienceResults = jedis.vsim("famousPeople", scienceEmbedding);
        System.out.println(scienceResults);
        // >>> [Marie Curie, Linus Pauling, Maryam Mirzakhani, Paul Erdos, Marie Fredriksson, Freddie Mercury, Masako Natsume, Chaim Topol]

        float[] science2000Embedding;
        try {
            science2000Embedding = predictor.predict("science");
        } catch (Exception e) {
            science2000Embedding = new float[384];
        }

        VSimParams filterParams = new VSimParams().filter(".died < 2000");
        List<String> filteredResults = jedis.vsim("famousPeople", science2000Embedding, filterParams);
        System.out.println(filteredResults);
        // >>> [Marie Curie, Linus Pauling, Paul Erdos, Freddie Mercury, Masako Natsume]
    }
}

```

Note that the boolean filter expression is applied to items in the list before the vector distance calculation is performed. Items that don't pass the filter test are removed from the results completely, rather than just reduced in rank. This can help to improve the performance of the search because there is no need to calculate the vector distance for elements that have already been filtered out of the search.

## More information

See the [vector sets](/docs/latest/develop/data-types/vector-sets/) docs for more information and code examples. See the [Redis for AI](/docs/latest/develop/ai/) section for more details about text embeddings and other AI techniques you can use with Redis.

You may also be interested in [vector search](/docs/latest/develop/clients/jedis/vecsearch/). This is a feature of [Redis Search](/docs/latest/develop/ai/search-and-query/) that lets you retrieve [JSON](/docs/latest/develop/data-types/json/) and [hash](/docs/latest/develop/data-types/hashes/) documents based on vector data stored in their fields.

## On this page
