---
title: "User functions"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/triggers/user_functions/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/triggers/user_functions/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:50.439Z"
content_hash: "e4d71fb8c4e225e58939fd7a674a04ed6d6c702f9855a2c83021cda33ffe63a8"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Concepts","→","Concepts","→\n      \n        Triggers","→","Triggers","→\n      \n        User functions","→","User functions"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Concepts","→","Concepts","→\n      \n        Triggers","→","Triggers","→\n      \n        User functions","→","User functions"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/triggers/stream_triggers/index.md", "title": "Stream triggers"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/configuration/index.md", "title": "Configuration"}
---

# User functions

Execute JavaScript functions via `TFCALL` or `TFCALLASYNC`

Redis Open Source

Redis Software

Redis Cloud

Redis Open Source

Redis Enterprise for Kubernetes

clients

All `TFCALL` command arguments that follow the function name are passed to the function callback. The following example shows how to implement a simple function that returns the value of a key of type string or hash:

```js
#!js api_version=1.0 name=lib

redis.registerFunction('my_get', function(client, key_name){
    if (client.call('type', key_name) == 'string') {
        return client.call('get', key_name);
    }
    if (client.call('type', key_name) == 'hash') {
        return client.call('hgetall', key_name);
    }
    throw "Unsupported type";
});
```

Example of running the preceding function:

```bash
127.0.0.1:6379> set x 1
OK
127.0.0.1:6379> TFCALL lib.my_get 1 x
"1"
127.0.0.1:6379> hset h a b x y
(integer) 2
127.0.0.1:6379> TFCALL lib.my_get 1 h
1) "a"
2) "b"
3) "x"
4) "y"
```

It is also possible to get all the function arguments as a `JS` array. This is how we can extend the above example to accept multiple keys and return their values:

```js
#!js api_version=1.0 name=lib

redis.registerFunction('my_get', function(client, ...keys){
    var results = [];
    keys.forEach((key_name)=> {
            if (client.call('type', key_name) == 'string') {
                results.push(client.call('get', key_name));
                return;
            }
            if (client.call('type', key_name) == 'hash') {
                results.push(client.call('hgetall', key_name));
                return;
            }
            results.push("Unsupported type");
        }
    );
    return results;

});
```

Run example:

```bash
127.0.0.1:6379> TFCALL foo.my_get 2 x h
1) "1"
2) 1) "a"
   2) "b"
   3) "x"
   4) "y"
```
