---
title: "Pipelines and transactions"
source: "https://redis.io/docs/latest/develop/clients/jedis/transpipe/"
canonical_url: "https://redis.io/docs/latest/develop/clients/jedis/transpipe/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:04:38.298Z"
content_hash: "6f1acfe73d53640458ae34e5a52eee7385356d41b17448d480e7fb613647dc1b"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Pipelines and transactions","→","Pipelines and transactions"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Pipelines and transactions","→","Pipelines and transactions"]
---
# Pipelines and transactions

Learn how to use Redis pipelines and transactions

Redis lets you send a sequence of commands to the server together in a batch. There are two types of batch that you can use:

*   **Pipelines** avoid network and processing overhead by sending several commands to the server together in a single communication. The server then sends back a single communication with all the responses. See the [Pipelining](/docs/latest/develop/using-commands/pipelining/) page for more information.
*   **Transactions** guarantee that all the included commands will execute to completion without being interrupted by commands from other clients. See the [Transactions](/docs/latest/develop/using-commands/transactions/) page for more information.

## Execute a pipeline

To execute commands in a pipeline, you first create a pipeline object and then add commands to it using methods that resemble the standard command methods (for example, `set()` and `get()`). The commands are buffered in the pipeline and only execute when you call the `sync()` method on the pipeline object.

The main difference with the pipeline commands is that they return `Response<Type>` objects, where `Type` is the return type of the standard command method. A `Response` object contains a valid result only after the pipeline has finished executing. You can access the result using the `Response` object's `get()` method.

```java
import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.AbstractPipeline;
import redis.clients.jedis.AbstractTransaction;
import redis.clients.jedis.Response;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PipeTransExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        // Make sure you close the pipeline after use to release resources
        // and return the connection to the pool.
        try (AbstractPipeline pipe = jedis.pipelined()) {

            for (int i = 0; i < 5; i++) {
                pipe.set(String.format("seat:%d", i), String.format("#%d", i));
            }

            pipe.sync();
        }

        try (AbstractPipeline pipe = jedis.pipelined()) {

            Response<String> resp0 = pipe.get("seat:0");
            Response<String> resp3 = pipe.get("seat:3");
            Response<String> resp4 = pipe.get("seat:4");

            pipe.sync();

            // Responses are available after the pipeline has executed.
            System.out.println(resp0.get()); // >>> #0
            System.out.println(resp3.get()); // >>> #3
            System.out.println(resp4.get()); // >>> #4

        }

        try ( AbstractTransaction trans = jedis.multi()) {

           trans.incrBy("counter:1", 1);
           trans.incrBy("counter:2", 2);
           trans.incrBy("counter:3", 3);

           trans.exec();
        }
        System.out.println(jedis.get("counter:1")); // >>> 1
        System.out.println(jedis.get("counter:2")); // >>> 2
        System.out.println(jedis.get("counter:3")); // >>> 3

        // Set initial value of `shellpath`.
        jedis.set("shellpath", "/usr/syscmds/");

        // Start the transaction and watch the key we are about to update.
        try (AbstractTransaction trans = jedis.transaction(false)) { // create a Transaction object without sending MULTI command
            trans.watch("shellpath"); // send WATCH command(s)
            trans.multi(); // send MULTI command

            String currentPath = jedis.get("shellpath");
            String newPath = currentPath + ":/usr/mycmds/";

            // Commands added to the `trans` object
            // will be buffered until `trans.exec()` is called.
            Response<String> setResult = trans.set("shellpath", newPath);
            List<Object> transResults = trans.exec();

            // The `exec()` call returns null if the transaction failed.
            if (transResults != null) {
                // Responses are available if the transaction succeeded.
                System.out.println(setResult.get()); // >>> OK

                // You can also get the results from the list returned by
                // `trans.exec()`.
                for (Object item: transResults) {
                    System.out.println(item);
                }
                // >>> OK

                System.out.println(jedis.get("shellpath"));
                // >>> /usr/syscmds/:/usr/mycmds/
            }
        }

        jedis.close();
    }   
}
```

## Execute a transaction

A transaction works in a similar way to a pipeline. Create a transaction object with the `multi()` command, call command methods on that object, and then call the transaction object's `exec()` method to execute it. You can access the results from commands in the transaction using `Response` objects, as you would with a pipeline. However, the `exec()` method also returns a `List<Object>` value that contains all the result values in the order the commands were executed (see [Watch keys for changes](#watch-keys-for-changes) below for an example that uses the results list).

```java
import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.AbstractPipeline;
import redis.clients.jedis.AbstractTransaction;
import redis.clients.jedis.Response;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PipeTransExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        // Make sure you close the pipeline after use to release resources
        // and return the connection to the pool.
        try (AbstractPipeline pipe = jedis.pipelined()) {

            for (int i = 0; i < 5; i++) {
                pipe.set(String.format("seat:%d", i), String.format("#%d", i));
            }

            pipe.sync();
        }

        try (AbstractPipeline pipe = jedis.pipelined()) {

            Response<String> resp0 = pipe.get("seat:0");
            Response<String> resp3 = pipe.get("seat:3");
            Response<String> resp4 = pipe.get("seat:4");

            pipe.sync();

            // Responses are available after the pipeline has executed.
            System.out.println(resp0.get()); // >>> #0
            System.out.println(resp3.get()); // >>> #3
            System.out.println(resp4.get()); // >>> #4

        }

        try ( AbstractTransaction trans = jedis.multi()) {

           trans.incrBy("counter:1", 1);
           trans.incrBy("counter:2", 2);
           trans.incrBy("counter:3", 3);

           trans.exec();
        }
        System.out.println(jedis.get("counter:1")); // >>> 1
        System.out.println(jedis.get("counter:2")); // >>> 2
        System.out.println(jedis.get("counter:3")); // >>> 3

        // Set initial value of `shellpath`.
        jedis.set("shellpath", "/usr/syscmds/");

        // Start the transaction and watch the key we are about to update.
        try (AbstractTransaction trans = jedis.transaction(false)) { // create a Transaction object without sending MULTI command
            trans.watch("shellpath"); // send WATCH command(s)
            trans.multi(); // send MULTI command

            String currentPath = jedis.get("shellpath");
            String newPath = currentPath + ":/usr/mycmds/";

            // Commands added to the `trans` object
            // will be buffered until `trans.exec()` is called.
            Response<String> setResult = trans.set("shellpath", newPath);
            List<Object> transResults = trans.exec();

            // The `exec()` call returns null if the transaction failed.
            if (transResults != null) {
                // Responses are available if the transaction succeeded.
                System.out.println(setResult.get()); // >>> OK

                // You can also get the results from the list returned by
                // `trans.exec()`.
                for (Object item: transResults) {
                    System.out.println(item);
                }
                // >>> OK

                System.out.println(jedis.get("shellpath"));
                // >>> /usr/syscmds/:/usr/mycmds/
            }
        }

        jedis.close();
    }   
}
```

## Watch keys for changes

Redis supports _optimistic locking_ to avoid inconsistent updates to different keys. The basic idea is to watch for changes to any keys that you use in a transaction while you are are processing the updates. If the watched keys do change, you must restart the updates with the latest data from the keys. See [Transactions](/docs/latest/develop/using-commands/transactions/) for more information about optimistic locking.

The code below reads a string that represents a `PATH` variable for a command shell, then appends a new command path to the string before attempting to write it back. If the watched key is modified by another client before writing, the transaction aborts. Note that you should call read-only commands for the watched keys synchronously on the usual client object (called `jedis` in our examples) but you still call commands for the transaction on the transaction object.

For production usage, you would generally call code like the following in a loop to retry it until it succeeds or else report or log the failure.

```java
import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.AbstractPipeline;
import redis.clients.jedis.AbstractTransaction;
import redis.clients.jedis.Response;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PipeTransExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        // Make sure you close the pipeline after use to release resources
        // and return the connection to the pool.
        try (AbstractPipeline pipe = jedis.pipelined()) {

            for (int i = 0; i < 5; i++) {
                pipe.set(String.format("seat:%d", i), String.format("#%d", i));
            }

            pipe.sync();
        }

        try (AbstractPipeline pipe = jedis.pipelined()) {

            Response<String> resp0 = pipe.get("seat:0");
            Response<String> resp3 = pipe.get("seat:3");
            Response<String> resp4 = pipe.get("seat:4");

            pipe.sync();

            // Responses are available after the pipeline has executed.
            System.out.println(resp0.get()); // >>> #0
            System.out.println(resp3.get()); // >>> #3
            System.out.println(resp4.get()); // >>> #4

        }

        try ( AbstractTransaction trans = jedis.multi()) {

           trans.incrBy("counter:1", 1);
           trans.incrBy("counter:2", 2);
           trans.incrBy("counter:3", 3);

           trans.exec();
        }
        System.out.println(jedis.get("counter:1")); // >>> 1
        System.out.println(jedis.get("counter:2")); // >>> 2
        System.out.println(jedis.get("counter:3")); // >>> 3

        // Set initial value of `shellpath`.
        jedis.set("shellpath", "/usr/syscmds/");

        // Start the transaction and watch the key we are about to update.
        try (AbstractTransaction trans = jedis.transaction(false)) { // create a Transaction object without sending MULTI command
            trans.watch("shellpath"); // send WATCH command(s)
            trans.multi(); // send MULTI command

            String currentPath = jedis.get("shellpath");
            String newPath = currentPath + ":/usr/mycmds/";

            // Commands added to the `trans` object
            // will be buffered until `trans.exec()` is called.
            Response<String> setResult = trans.set("shellpath", newPath);
            List<Object> transResults = trans.exec();

            // The `exec()` call returns null if the transaction failed.
            if (transResults != null) {
                // Responses are available if the transaction succeeded.
                System.out.println(setResult.get()); // >>> OK

                // You can also get the results from the list returned by
                // `trans.exec()`.
                for (Object item: transResults) {
                    System.out.println(item);
                }
                // >>> OK

                System.out.println(jedis.get("shellpath"));
                // >>> /usr/syscmds/:/usr/mycmds/
            }
        }

        jedis.close();
    }   
}
```

## On this page
