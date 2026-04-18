---
title: "Redis Insight"
source: "https://redis.io/docs/latest/develop/tools/insight/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:28.308Z"
content_hash: "bc59e33941cf42b00593e05eacf3b9be1706fdd0647d3563fab80c939b698fbc"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-data-integration/index.md", "title": "Redis Data Integration"}
nav_next: {"path": "redis/docs/latest/integrate/redisinsight/index.md", "title": "Redis Insight"}
---

# Redis Insight

Visualize and optimize Redis data, connect to RDI, and more.

[![Discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/QUkjSsk) [![Github](https://img.shields.io/static/v1?label=&message=repository&color=5961FF&logo=github)](https://github.com/redisinsight/redisinsight/)

Redis Insight is a powerful tool for visualizing and optimizing data in Redis, making real-time application development easier and more fun than ever before. Redis Insight lets you do both GUI- and CLI-based interactions in a fully-featured desktop GUI client.

### Installation and release notes

[

![Install Redis Insight icon](/docs/latest/images/redisinsight-desktop.svg)

Installation guides

](/docs/latest/operate/redisinsight/install/)[

![Download Redis Insight icon](/docs/latest/images/redisinsight-download.svg)

Download Redis Insight

](https://redis.io/downloads/#insight)[

![Release Notes Redis Insight icon](/docs/latest/images/redisinsight-aws.svg)

Release Notes

](/docs/latest/develop/tools/insight/release-notes/)

## Overview

### Connection management

*   Automatically discover and add your local Redis databases (that use standalone connection type and do not require authentication).
*   Discover your databases in Redis Software Cluster and databases with Flexible plans in Redis Cloud.
*   Use a form to enter your connection details and add any Redis database running anywhere (including Redis Open Source cluster or sentinel).
*   Connect to a Redis Data Integration (RDI) management plane, create, test, and deploy RDI pipelines, and view RDI statistics.

[![The databases screen](/docs/latest/images/ri/ri-databases.png)](/docs/latest/images/ri/ri-databases.png)

Note:

When you add a Redis database for a particular user using the `username` and `password` fields, that user must be able to run the `INFO` command. See the [access control list (ACL) documentation](/docs/latest/operate/oss_and_stack/management/security/acl/) for more information.

### Connect to Azure Managed Redis with ease

Automatically discover databases across subscriptions and connect using Microsoft Entra ID (OAuth) with passwordless authentication and background token refresh. Redis Insight supports both Azure Managed Redis and Azure Cache for Redis tiers, with:

*   Auto-discovery of subscriptions and databases
*   One-click import and connection
*   Multi-account support for switching between Azure accounts
*   Improved, user-friendly error handling

Note:

This feature requires Azure-side configuration. Please coordinate with your Azure administrator and follow [the setup guide](https://github.com/redis/RedisInsight/blob/main/docs/azure-setup.md) to configure the necessary permissions.

### Redis Copilot

Redis Copilot is an AI-powered developer assistant that helps you learn about Redis, explore your Redis data, and build search queries in a conversational manner. It is available in Redis Insight as well as within the Redis public documentation.

Currently, Redis Copilot provides two primary features: a general chatbot and a context-aware data chatbot.

**General chatbot**: the knowledge-based chatbot serves as an interactive and dynamic documentation interface to simplify the learning process. You can ask specific questions about Redis commands, concepts, and products, and get responses on the fly. The general chatbot is also available in our public docs.

**My data chatbot**: the context-aware chatbot available in Redis Insight lets you construct search queries using everyday language rather than requiring specific programming syntax. This feature lets you query and explore data easily and interactively without extensive technical knowledge.

Before you can use Redis Copilot, you must first sign in and accept the terms of use. Click on the Redis Copilot icon in the top right corner of the Redis Insight window to sign in and accept the terms of use.

 [![The Redis Copilot icon](/docs/latest/images/ri/ri-redis-copilot-icon.png)](/docs/latest/images/ri/ri-redis-copilot-icon.png)[![The Redis Copilot sign in screen](/docs/latest/images/ri/ri-redis-copilot-signin.png)](/docs/latest/images/ri/ri-redis-copilot-signin.png)

Here's an example of using Redis Copilot to search data using a simple, natural language prompt.

[![An example of using Redis Copilot to search data](/docs/latest/images/ri/ri-redis-copilot-query.png)](/docs/latest/images/ri/ri-redis-copilot-query.png)

See the [Redis Insight Copilot FAQ](/docs/latest/develop/tools/insight/copilot-faq/) for more information.

### RDI in Redis Insight

Redis Insight includes Redis Data Integration (RDI) connectivity, which allows you to connect to an RDI management plane, and create, test, and deploy RDI pipelines. Read more about this feature [here](/docs/latest/develop/tools/insight/rdi-connector/).

### Browser

Browse, filter and visualize your key-value Redis data structures.

*   [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) support for lists, hashes, strings, sets, sorted sets, and streams.
    
*   CRUD support for [JSON](/docs/latest/develop/data-types/json/).
    
*   Group keys according to their namespaces.
    
*   View, validate, and manage your key values in a human-readable format using formatters that prettify and highlight data in different formats (for example, Unicode, JSON, MessagePack, HEX, and ASCII) in the Browser tool.
    
    [![The Browser tool](/docs/latest/images/ri/ri-browser.png)](/docs/latest/images/ri/ri-browser.png)

### Profiler

Analyze every command sent to Redis in real time. To use the profiler, click **Profiler** at the bottom left of the screen. It should reveal the profiler window, and there you can start the profiler by clicking on **Start Profiler**.

[![The Profiler tool](/docs/latest/images/ri/ri-profiler.png)](/docs/latest/images/ri/ri-profiler.png)

### CLI

The CLI is accessible at any time within the application. To use the CLI, click **\>\_ CLI** at the bottom left of the screen. It should reveal the CLI window, and there you can start typing Redis [commands](/docs/latest/commands/).

The CLI includes the following features:

*   Employs integrated help to deliver intuitive assistance.
*   Use together with a convenient command helper that lets you search and read on Redis commands.

[![The CLI tool](/docs/latest/images/ri/ri-cli.png)](/docs/latest/images/ri/ri-cli.png)

### Workbench

Workbench is an advanced command line interface with intelligent command auto-complete and complex data visualization support.

*   Built-in guides: you can conveniently discover Redis and Redis Open Source features using the built-in guides.
*   Command auto-complete support for all features in Redis and Redis Open Source.
*   Advanced, schema-aware auto-complete for Redis Search, which provides for faster query building with context-sensitive suggestions that recognize indexes, schemas, and fields based on your current query. Start typing any Redis Search command in to try this feature. See below for an example of an in-progress `FT.SEARCH` command.

[![An example of an in-progress FT.SEARCH command](/docs/latest/images/ri/ri-workbench.png)](/docs/latest/images/ri/ri-workbench.png)

Workbench also includes:

*   Visualizations of your indexes, queries, and aggregations.
*   Visualizations of your [time series](/docs/latest/develop/data-types/timeseries/) data.

[![Visualizations of time series data](/docs/latest/images/ri/ri-workbench-timeseries.png)](/docs/latest/images/ri/ri-workbench-timeseries.png)

## Tools

### Database analysis

Use the database analysis tool to optimize the performance and memory usage of your Redis database. Check data type distribution and memory allocation and review the summary of key expiration time and memory to be freed over time. Inspect the top keys and namespaces sorted by consumed memory or key length and count of keys, respectively. Capture and track the changes in your database by viewing historical analysis reports. Next figure shows a sample database analysis report.

Note:

The database analysis tool will only analyze up to 10,000 keys. If more than 10,000 keys are present, the tool will attempt to use extrapolation in its analysis.

[![The database analysis tool](/docs/latest/images/ri/ri-analysis.png)](/docs/latest/images/ri/ri-analysis.png)

### Redis Streams support

Create and manage streams by adding, removing, and filtering entries per timestamp. To see and work with new entries, enable and customize the automatic refresh rate.

View and manage the list of consumer groups. See existing consumers in a given consumer name as well as the last messages delivered to them. Inspect the list of pending messages, explicitly acknowledge the processed items, or claim unprocessed messages via Redis Insight.

[![Redis Streams support](/docs/latest/images/ri/ri-streams.png)](/docs/latest/images/ri/ri-streams.png)

### Search features

If you're using the indexing, querying, or full-text search features of Redis Open Source, Redis Insight provides UI controls to quickly and conveniently run search queries against a preselected index. You can also create a secondary index of your data in a dedicated pane.

[![Search features](/docs/latest/images/ri/ri-search.png)](/docs/latest/images/ri/ri-search.png)

### Bulk actions

Easily and quickly delete multiple keys of the same type and/or with the same key name pattern in bulk. To do so, in the List or Tree view, set filters per key type or key names and open the Bulk Actions section. The section displays a summary of all the keys with the expected number of keys that will be deleted based on the set filters.

When the bulk deletion is completed, Redis Insight displays the results of this operation with the number of keys processed and the time taken to delete the keys in bulk. Use bulk deletion to optimize the usage of your database based on the results from the Redis database analysis.

[![Bulk actions](/docs/latest/images/ri/ri-bulk-actions.png)](/docs/latest/images/ri/ri-bulk-actions.png)

### Slow Log

The Slow Log tool displays the list of logs captured by the SLOWLOG command to analyze all commands that exceed a specified runtime, which helps with troubleshooting performance issues. Specify both the runtime and the maximum length of Slowlog (which are server configurations) to configure the list of commands logged and set the auto-refresh interval to automatically update the list of commands displayed.

[![Slow Log](/docs/latest/images/ri/ri-slow-log.png)](/docs/latest/images/ri/ri-slow-log.png)

## Plugins

With Redis Insight you can now also extend the core functionality by building your own data visualizations. See our [plugin documentation](https://github.com/Redis-Insight/Redis-Insight/wiki/Plugin-Documentation) for more information.

## Telemetry

Redis Insight includes an opt-in telemetry system. This help us improve the developer experience of the app. We value your privacy; all collected data is anonymized.

## Log files

You can review the Redis Insight log files (files with a `.log` extension) to get detailed information about system issues. These are the locations on supported platforms:

*   **Docker**: In the `/data/logs` directory _inside the container_.
*   **Mac**: In the `/Users/<your-username>/.redis-insight` directory.
*   **Windows**: In the `C:\Users\<your-username>\.redis-insight` directory.
*   **Linux**: In the `/home/<your-username>/.redis-insight` directory.

Note:

You can install Redis Insight on operating systems that are not officially supported, but it may not behave as expected.

## Redis Insight API (only for Docker)

If you are running Redis Insight from [Docker](/docs/latest/operate/redisinsight/install/install-on-docker/), you can access the API from `http://localhost:5540/api/docs`.

## Feedback

To provide your feedback, [open a ticket in our Redis Insight repository](https://github.com/Redis-Insight/Redis-Insight/issues/new).

## License

Redis Insight is licensed under [SSPL](https://github.com/Redis-Insight/Redis-Insight/blob/main/LICENSE) license.

## On this page
