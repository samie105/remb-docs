---
title: "Install on Docker"
source: "https://redis.io/docs/latest/operate/redisinsight/install/install-on-docker/"
canonical_url: "https://redis.io/docs/latest/operate/redisinsight/install/install-on-docker/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:00.387Z"
content_hash: "b8ccd2b202a7164dd96e46f7cf07ff85005de440091ab5fe455c5783bc25085b"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Install Redis Insight","→","Install Redis Insight","→\n      \n        Install on Docker","→","Install on Docker"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Install Redis Insight","→","Install Redis Insight","→\n      \n        Install on Docker","→","Install on Docker"]
nav_prev: {"path": "redis/docs/latest/operate/redisinsight/install/install-on-desktop/index.md", "title": "Install on desktop"}
nav_next: {"path": "redis/docs/latest/operate/redisinsight/install/install-on-k8s/index.md", "title": "Install on Kubernetes"}
---

# Install on Docker

How to install Redis Insight on Docker

Redis Insight

This tutorial shows how to install Redis Insight on [Docker](https://www.docker.com/) so you can use Redis Insight in development. See a separate guide for installing [Redis Insight on AWS](/docs/latest/operate/redisinsight/install/install-on-aws/).

## Install Docker

The first step is to [install Docker for your operating system](https://docs.docker.com/install/).

## Run Redis Insight Docker image

You can install Redis Insight using one of the options described below.

1.  If you do not want to persist your Redis Insight data:

```bash
docker run -d --name redisinsight -p 5540:5540 redis/redisinsight:latest
```

2.  If you want to persist your Redis Insight data, first attach the Docker volume to the `/data` path and then run the following command:

```bash
docker run -d --name redisinsight -p 5540:5540 -v redisinsight:/data redis/redisinsight:latest
```

If the previous command returns a permission error, ensure that the user with `ID = 1000` has the necessary permissions to access the volume provided (`redisinsight` in the command above).

Next, point your browser to `http://localhost:5540`.

Redis Insight also provides a health check endpoint at `http://localhost:5540/api/health/` to monitor the health of the running container.

## On this page
