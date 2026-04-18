---
title: "HyperLogLog"
source: "https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/"
canonical_url: "https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:58.938Z"
content_hash: "a9d54632bf1539dfac961b841bb4850b4cd1b9505504f1738392eac49ae97cf8"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        Probabilistic","→","Probabilistic","→\n      \n        HyperLogLog","→","HyperLogLog"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        Probabilistic","→","Probabilistic","→\n      \n        HyperLogLog","→","HyperLogLog"]
nav_prev: {"path": "redis/docs/latest/develop/ai/redisvl/user_guide/getting_started/index.md", "title": "Getting Started with RedisVL"}
nav_next: {"path": "redis/docs/latest/operate/redisinsight/install/install-on-desktop/index.md", "title": "Install on desktop"}
---

# HyperLogLog

HyperLogLog is a probabilistic data structure that estimates the cardinality of a set.

*   [
    
    PFADD v2.8.9 @write @hyperloglog @fast
    
    Adds elements to a HyperLogLog key. Creates the key if it doesn't exist. O(1) to add every element.
    
    ](https://redis.io/docs/latest/commands/pfadd/)
*   [
    
    PFCOUNT v2.8.9 @read @hyperloglog @slow
    
    Returns the approximated cardinality of the set(s) observed by the HyperLogLog key(s). O(1) with a very small average constant time when called with a single key. O(N) with N being the number of keys, and much bigger constant times, when called with multiple keys.
    
    ](https://redis.io/docs/latest/commands/pfcount/)
*   [
    
    PFDEBUG v2.8.9 @write @hyperloglog @admin @slow @dangerous
    
    Internal commands for debugging HyperLogLog values. N/A
    
    ](https://redis.io/docs/latest/commands/pfdebug/)
*   [
    
    PFMERGE v2.8.9 @write @hyperloglog @slow
    
    Merges one or more HyperLogLog values into a single key. O(N) to merge N HyperLogLogs, but with high constant times.
    
    ](https://redis.io/docs/latest/commands/pfmerge/)
*   [
    
    PFSELFTEST v2.8.9 @hyperloglog @admin @slow @dangerous
    
    An internal command for testing HyperLogLog values. N/A
    
    ](https://redis.io/docs/latest/commands/pfselftest/)

HyperLogLog is a probabilistic data structure that estimates the cardinality of a set, trading perfect accuracy for efficient space utilization. The Redis implementation uses up to 12 KB of memory and provides a standard error rate of 0.81%.

Counting unique items usually requires an amount of memory proportional to the number of items you want to count, because you need to remember the elements you have already seen in the past in order to avoid counting them multiple times. However, a set of algorithms exist that trade memory for precision: they return an estimated measure with a standard error, which, in the case of the Redis implementation for HyperLogLog, is less than 1%. The magic of this algorithm is that you no longer need to use an amount of memory proportional to the number of items counted, and instead can use a constant amount of memory; 12k bytes in the worst case, or a lot less if your HyperLogLog (We'll just call them HLL from now) has seen very few elements.

HLLs in Redis, while technically a different data structure, are encoded as a Redis string, so you can call [`GET`](/docs/latest/commands/get/) to serialize a HLL, and [`SET`](/docs/latest/commands/set/) to deserialize it back to the server.

Conceptually the HLL API is like using Sets to do the same task. You would [`SADD`](/docs/latest/commands/sadd/) every observed element into a set, and would use [`SCARD`](/docs/latest/commands/scard/) to check the number of elements inside the set, which are unique since [`SADD`](/docs/latest/commands/sadd/) will not re-add an existing element.

While you don't really _add items_ into an HLL, because the data structure only contains a state that does not include actual elements, the API is the same:

*   Every time you see a new element, you add it to the count with [`PFADD`](/docs/latest/commands/pfadd/).
*   When you want to retrieve the current approximation of unique elements added using the [`PFADD`](/docs/latest/commands/pfadd/) command, you can use the [`PFCOUNT`](/docs/latest/commands/pfcount/) command. If you need to merge two different HLLs, the [`PFMERGE`](/docs/latest/commands/pfmerge/) command is available. Since HLLs provide approximate counts of unique elements, the result of the merge will give you an approximation of the number of unique elements across both source HLLs.

```plaintext
> PFADD bikes Hyperion Deimos Phoebe Quaoar
(integer) 1
> PFCOUNT bikes
(integer) 4
> PFADD commuter_bikes Salacia Mimas Quaoar
(integer) 1
> PFMERGE all_bikes bikes commuter_bikes
OK
> PFCOUNT all_bikes
(integer) 6
```

```python
"""
Code samples for HyperLogLog doc pages:
    https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/
"""

import redis

r = redis.Redis(decode_responses=True)

res1 = r.pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar")
print(res1)  # >>> 1

res2 = r.pfcount("bikes")
print(res2)  # >>> 4

res3 = r.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar")
print(res3)  # >>> 1

res4 = r.pfmerge("all_bikes", "bikes", "commuter_bikes")
print(res4)  # >>> True

res5 = r.pfcount("all_bikes")
print(res5)  # >>> 6

```

```node.js
import assert from 'assert';
import { createClient } from 'redis';

const client = createClient();
await client.connect();

const res1 = await client.pfAdd('bikes', ['Hyperion', 'Deimos', 'Phoebe', 'Quaoar']);
console.log(res1);  // >>> 1

const res2 = await client.pfCount('bikes');
console.log(res2);  // >>> 4

const res3 = await client.pfAdd('commuter_bikes', ['Salacia', 'Mimas', 'Quaoar']);
console.log(res3);  // >>> 1

const res4 = await client.pfMerge('all_bikes', ['bikes', 'commuter_bikes']);
console.log(res4);  // >>> OK

const res5 = await client.pfCount('all_bikes');
console.log(res5);  // >>> 6

```

```java
package io.redis.examples;

import org.junit.jupiter.api.Test;
import redis.clients.jedis.RedisClient;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HyperLogLogExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        long res1 = jedis.pfadd("bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar");
        System.out.println(res1); // >>> 1

        long res2 = jedis.pfcount("bikes");
        System.out.println(res2); // >>> 4

        long res3 = jedis.pfadd("commuter_bikes", "Salacia", "Mimas", "Quaoar");
        System.out.println(res3); // >>> 1

        String res4 = jedis.pfmerge("all_bikes", "bikes", "commuter_bikes");
        System.out.println(res4); // >>> OK

        long res5 = jedis.pfcount("all_bikes");
        System.out.println(res5); // >>> 6

        jedis.close();
    }
}
```

```go
package example_commands_test

import (
	"context"
	"fmt"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_pfadd() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	res1, err := rdb.PFAdd(ctx, "bikes", "Hyperion", "Deimos", "Phoebe", "Quaoar").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // 1

	res2, err := rdb.PFCount(ctx, "bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // 4

	res3, err := rdb.PFAdd(ctx, "commuter_bikes", "Salacia", "Mimas", "Quaoar").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // 1

	res4, err := rdb.PFMerge(ctx, "all_bikes", "bikes", "commuter_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // OK

	res5, err := rdb.PFCount(ctx, "all_bikes").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // 6

}
```

```c#

using NRedisStack.Tests;
using StackExchange.Redis;

public class HllTutorial
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        bool res1 = db.HyperLogLogAdd("{bikes}", ["Hyperion", "Deimos", "Phoebe", "Quaoar"]);
        Console.WriteLine(res1);    // >>> True

        long res2 = db.HyperLogLogLength("{bikes}");
        Console.WriteLine(res2);    // >>> 4

        bool res3 = db.HyperLogLogAdd("commuter_{bikes}", ["Salacia", "Mimas", "Quaoar"]);
        Console.WriteLine(res3);    // >>> True

        db.HyperLogLogMerge("all_{bikes}", "{bikes}", "commuter_{bikes}");
        long res4 = db.HyperLogLogLength("all_{bikes}");
        Console.WriteLine(res4);    // >>> 6

        // Tests for 'pfadd' step.

    }
}

```

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

class DtHllTest
{
    public function testDtHll() {
        $r = new PredisClient([
            'scheme'   => 'tcp',
            'host'     => '127.0.0.1',
            'port'     => 6379,
            'password' => '',
            'database' => 0,
        ]);

        $res1 = $r->pfadd('bikes', ['Hyperion', 'Deimos', 'Phoebe', 'Quaoar']);
        echo $res1 . PHP_EOL;
        // >>> 1

        $res2 = $r->pfcount('bikes');
        echo $res2 . PHP_EOL;
        // >>> 4

        $res3 = $r->pfadd('commuter_bikes', ['Salacia', 'Mimas', 'Quaoar']);
        echo $res3 . PHP_EOL;
        // >>> 1

        $res4 = $r->pfmerge('all_bikes', 'bikes', 'commuter_bikes');
        echo $res4 . PHP_EOL;
        // >>> OK

        $res5 = $r->pfcount('all_bikes');
        echo $res5 . PHP_EOL;
        // >>> 6
    }
}

```

Some examples of use cases for this data structure is counting unique queries performed by users in a search form every day, number of unique visitors to a web page and other similar cases.

Redis is also able to perform the union of HLLs, please check the [full documentation](/docs/latest/commands/#hyperloglog) for more information.

## Use cases

**Anonymous unique visits of a web page (SaaS, analytics tools)**

This application answers these questions:

*   How many unique visits has this page had on this day?
*   How many unique users have played this song?
*   How many unique users have viewed this video?

Note:

Storing the IP address or any other kind of personal identifier is against the law in some countries, which makes it impossible to get unique visitor statistics on your website.

One HyperLogLog is created per page (video/song) per period, and every IP/identifier is added to it on every visit.

## Performance

Writing ([`PFADD`](/docs/latest/commands/pfadd/)) to and reading from ([`PFCOUNT`](/docs/latest/commands/pfcount/)) the HyperLogLog is done in constant time and space. Merging HLLs is O(n), where _n_ is the number of sketches.

## Limits

The HyperLogLog can estimate the cardinality of sets with up to 18,446,744,073,709,551,616 (2^64) members.

## Learn more

*   [Redis new data structure: the HyperLogLog](http://antirez.com/news/75) has a lot of details about the data structure and its implementation in Redis.
*   [Redis HyperLogLog Explained](https://www.youtube.com/watch?v=MunL8nnwscQ) shows you how to use Redis HyperLogLog data structures to build a traffic heat map.

## On this page


