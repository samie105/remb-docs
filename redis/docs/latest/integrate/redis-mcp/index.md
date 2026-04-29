---
title: "Redis MCP"
source: "https://redis.io/docs/latest/integrate/redis-mcp/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-mcp/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:48.329Z"
content_hash: "63b9671c945a117b65bd234b3bd90d641f4527d04bb617eb3277628c6e9a64bb"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis MCP","→","Redis MCP"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis MCP","→","Redis MCP"]
nav_prev: {"path": "../redis-data-integration/when-to-use/index.md", "title": "When to use RDI"}
nav_next: {"path": "../redis-py/index.md", "title": "Python client for Redis"}
---

# Redis MCP

Access a Redis server using any MCP client.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is a standard that lets AI agents access data and perform actions. Using MCP, your server can publish a set of commands that are usable by any MCP-compatible client app (such as [Claude Desktop](https://claude.ai/download) or [VS Code](https://code.visualstudio.com/)). These commands can retrieve whatever data you wish to provide and you can also let the agent make changes to the data. For example, you could publish a feed of news items that an agent can use in its responses, and also let the agent add the user's comments to those items.

Redis MCP is a general-purpose implementation that lets agents read, write, and query data in Redis and also has some basic commands to manage the Redis server. With this enabled, you can use an LLM client as a very high-level interface to Redis. Add, query, and analyze any Redis data set directly from an LLM chat using instructions and questions like the following:

*   "Store the entire conversation in the 'recent\_chats' stream"
*   "Cache this item"
*   "How many keys does my database have?"
*   "What is user:1's email?"

See the other pages in this section to learn how to set up and use Redis MCP. See also the [GitHub repository](https://github.com/redis/mcp-redis) for the latest changes.
