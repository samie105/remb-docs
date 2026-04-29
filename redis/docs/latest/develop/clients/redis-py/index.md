---
title: "redis-py guide (Python)"
source: "https://redis.io/docs/latest/develop/clients/redis-py/"
canonical_url: "https://redis.io/docs/latest/develop/clients/redis-py/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:09.035Z"
content_hash: "880c22961dad0976d7cea4797b9fde0b7306a49c261f3fb2fe43cebc523ae624"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        redis-py guide (Python)","→","redis-py guide (Python)"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        redis-py guide (Python)","→","redis-py guide (Python)"]
nav_prev: {"path": "../php/index.md", "title": "Predis guide (PHP)"}
nav_next: {"path": "../redis-vl/index.md", "title": "Redis vector library guide (Python)"}
---

# redis-py guide (Python)

Connect your Python application to a Redis database

[redis-py](https://github.com/redis/redis-py) is the Python client for Redis. The sections below explain how to install `redis-py` and connect your application to a Redis database.

`redis-py` requires a running Redis server. See [here](/docs/latest/operate/oss_and_stack/install/) for Redis Open Source installation instructions.

You can also access Redis with an object-mapping client interface. See [RedisOM for Python](/docs/latest/integrate/redisom-for-python/) for more information.

## Install

To install `redis-py`, enter:

```bash
pip install redis
```

For faster performance, install Redis with [`hiredis`](https://github.com/redis/hiredis) support. This provides a compiled response parser, and for most cases requires zero code changes. By default, if `hiredis` >= 1.0 is available, `redis-py` attempts to use it for response parsing.

Note:

The Python `distutils` packaging scheme is no longer part of Python 3.12 and greater. If you're having difficulties getting `redis-py` installed in a Python 3.12 environment, consider updating to a recent release of `redis-py`.

```bash
pip install redis[hiredis]
```

## Connect and test

Connect to localhost on port 6379, set a value in Redis, and retrieve it. All responses are returned as bytes in Python. To receive decoded strings, set `decode_responses=True`. For more connection options, see [these examples](https://redis.readthedocs.io/en/stable/examples.html).

Ctrl+Enter to run

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

```python
r.set('foo', 'bar')
r.get('foo')
```

```python
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

r.hgetall('user-session:123')
```

```python
r.close()
```

Store and retrieve a simple string.

Ctrl+Enter to run

```python
r.set('foo', 'bar')
r.get('foo')
```

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

```python
r.set('foo', 'bar')
r.get('foo')
```

```python
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

r.hgetall('user-session:123')
```

```python
r.close()
```

Store and retrieve a dict.

Ctrl+Enter to run

```python
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

r.hgetall('user-session:123')
```

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

```python
r.set('foo', 'bar')
r.get('foo')
```

```python
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

r.hgetall('user-session:123')
```

```python
r.close()
```

Close the connection when you're done.

Ctrl+Enter to run

```python
r.close()
```

```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
```

```python
r.set('foo', 'bar')
r.get('foo')
```

```python
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

r.hgetall('user-session:123')
```

```python
r.close()
```

## More information

The [`redis-py`](https://redis.readthedocs.io/en/stable/index.html) website has a [command reference](https://redis.readthedocs.io/en/stable/commands.html) and some [tutorials](https://redis.readthedocs.io/en/stable/examples.html) for various tasks. There are also some examples in the [GitHub repository](https://github.com/redis/redis-py) for `redis-py`.

See also the other pages in this section for more information and examples:

## On this page
