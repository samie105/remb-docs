---
title: "Run Redis Stack on Docker"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/docker/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/docker/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:17.567Z"
content_hash: "e4c4bed1af0d1dea68997aa17156b29f53eca5eed4cae194f4e704fe24aaa1ea"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Run Redis Stack on Docker","→","Run Redis Stack on Docker"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Run Redis Stack on Docker","→","Run Redis Stack on Docker"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/development/index.md", "title": "Development"}
nav_next: {"path": "redis/docs/latest/integrate/riot/docs/index.md", "title": "Documentation"}
---

# Run Redis Stack on Docker

How to install Redis Stack using Docker

Redis Open Source

To get started with Redis Stack using Docker, you first need to select a Docker image:

*   `redis/redis-stack` contains both Redis Stack server and Redis Insight. This container is best for local development because you can use the embedded Redis Insight to visualize your data.
    
*   `redis/redis-stack-server` provides Redis Stack server only. This container is best for production deployment.
    

## Getting started

### redis/redis-stack-server

To start Redis Stack server using the `redis-stack-server` image, run the following command in your terminal:

```bash
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

### redis/redis-stack

To start a Redis Stack container using the `redis-stack` image, run the following command in your terminal:

```bash
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

The `docker run` command above also exposes Redis Insight on port 8001. You can use Redis Insight by pointing your browser to `localhost:8001`.

## Connect with redis-cli

You can then connect to the server using `redis-cli`, just as you connect to any Redis instance.

If you don’t have `redis-cli` installed locally, you can run it from the Docker container:

```bash
$ docker exec -it redis-stack redis-cli
```

## Configuration

### Persistence in Docker

To mount directories or files to your Docker container, specify `-v` to configure a local volume. This command stores all data in the local directory `local-data`:

```bash
$ docker run -v /local-data/:/data redis/redis-stack:latest
```

### Ports

If you want to expose Redis Stack server or Redis Insight on a different port, update the left hand of portion of the `-p` argument. This command exposes Redis Stack server on port `10001` and Redis Insight on port `13333`:

```bash
$ docker run -p 10001:6379 -p 13333:8001 redis/redis-stack:latest
```

### Config files

By default, the Redis Stack Docker containers use internal configuration files for Redis. To start Redis with local configuration file, you can use the `-v` volume options:

```bash
$ docker run -v `pwd`/local-redis-stack.conf:/redis-stack.conf -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

### Environment variables

To pass in arbitrary configuration changes, you can set any of these environment variables:

*   `REDIS_ARGS`: extra arguments for Redis
    
*   `REDISEARCH_ARGS`: arguments for the search and query features (RediSearch)
    
*   `REDISJSON_ARGS`: arguments for JSON (RedisJSON)
    
*   `REDISTIMESERIES_ARGS`: arguments for time series (RedisTimeSeries)
    
*   `REDISBLOOM_ARGS`: arguments for the probabilistic data structures (RedisBloom)
    

For example, here's how to use the `REDIS_ARGS` environment variable to pass the `requirepass` directive to Redis:

```bash
docker run -e REDIS_ARGS="--requirepass redis-stack" redis/redis-stack:latest
```

An example of setting [Redis persistence](/docs/latest/operate/oss_and_stack/management/persistence/):

```bash
docker run -e REDIS_ARGS="--save 60 1000 --appendonly yes" redis/redis-stack:latest
```

Here's how to set a retention policy for time series:

```bash
docker run -e REDISTIMESERIES_ARGS="RETENTION_POLICY=20" redis/redis-stack:latest
```

## On this page


