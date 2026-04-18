---
title: "Use Redis Insight on Redis Cloud"
source: "https://redis.io/docs/latest/operate/rc/databases/connect/insight-cloud/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/connect/insight-cloud/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:37.187Z"
content_hash: "822db0a3af9b923b3f421a822f7aa122c3df75fb42164ea3d80d4446b761fd48"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Connect to a Redis Cloud database","→","Connect to a Redis Cloud database","→\n      \n        Use Redis Insight on Redis Cloud","→","Use Redis Insight on Redis Cloud"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Connect to a Redis Cloud database","→","Connect to a Redis Cloud database","→\n      \n        Use Redis Insight on Redis Cloud","→","Use Redis Insight on Redis Cloud"]
nav_prev: {"path": "redis/docs/latest/integrate/redisinsight/index.md", "title": "Redis Insight"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/best-practices/scalable-query-best-practices/index.md", "title": "Best practices for Redis Search performance"}
---

# Use Redis Insight on Redis Cloud

Shows how to open your database in a browser-based version of Redis Insight and lists the features that are available.

Redis Cloud

Redis Insight

[Redis Insight](/docs/latest/develop/tools/insight/) is a free Redis GUI that lets you visualize your Redis data and learn more about Redis.

You can either [install Redis Insight](/docs/latest/develop/tools/insight/) on your computer, or you can open your database in Redis Insight directly on Redis Cloud.

Note:

Opening your database with Redis Insight in your browser is only available for Essentials databases. For all other databases, [install Redis Insight](/docs/latest/develop/tools/insight/) on your computer and [open Redis Insight](/docs/latest/operate/rc/databases/connect/#ri-app) from the database page.

To open your database with Redis Insight on Redis Cloud, select **Open with Redis Insight** on the [database screen](/docs/latest/operate/rc/databases/view-edit-database/).

[![Open with Redis Insight](/docs/latest/images/rc/rc-ri-open.png)](/docs/latest/images/rc/rc-ri-open.png)

Redis Insight will open in a new tab.

This browser-based version of Redis Insight has a subset of the features of Redis Insight. For other Redis Insight features, [install Redis Insight](/docs/latest/develop/tools/insight/) on your computer and [open Redis Insight](/docs/latest/operate/rc/databases/connect/#ri-app) from the database page.

## Browse

The **Browse** tab lets you browse, filter, and visualize your Redis data structures.

*   Create, read, update, and delete lists, hashes, strings, sets, sorted sets, streams, and [JSON](/docs/latest/develop/data-types/json/)
*   Filter keys by key name or pattern, and by key type
*   Group keys according to their namespaces [![Keys in a database grouped by namespace.](/docs/latest/images/rc/rc-ri-browser-group.png)](/docs/latest/images/rc/rc-ri-browser-group.png)
*   View, validate, and manage your key values in a human-readable format using formatters that prettify and highlight data in different formats (for example, Unicode, JSON, MessagePack, HEX, and ASCII) [![Human-readable view of a hash key.](/docs/latest/images/rc/rc-ri-browser-view.png)](/docs/latest/images/rc/rc-ri-browser-view.png)
*   Search by key values using your [search indexes](/docs/latest/develop/ai/search-and-query/) [![Search for keys using a search index.](/docs/latest/images/rc/rc-ri-browser-search.png)](/docs/latest/images/rc/rc-ri-browser-search.png)

If you don't have any Redis data yet, you can select **Load sample data** to add sample data into your database.

[![Load Sample Data button](/docs/latest/images/rc/rc-ri-load-data.png)](/docs/latest/images/rc/rc-ri-load-data.png)

## CLI and Command Helper

The **CLI** lets you run Redis commands directly.

[![The CLI and command helper](/docs/latest/images/rc/rc-ri-cli.png)](/docs/latest/images/rc/rc-ri-cli.png)

The CLI integrates with a **Command Helper** that lets you search and read information about Redis commands.

## Workbench

The **Workbench** is an advanced command line interface with intelligent command auto-complete and complex data visualization support.

[![The Workbench](/docs/latest/images/rc/rc-ri-workbench.png)](/docs/latest/images/rc/rc-ri-workbench.png)

## Insights

The **Insights** panel provides interactive tutorials and recommendations to help you optimize your database performance and memory usage.

[![The Insights panel](/docs/latest/images/rc/rc-ri-insights.png)](/docs/latest/images/rc/rc-ri-insights.png)

From the **Workbench** of an empty database, select **Explore** to view the **Insights** panel.

[![The Explore button](/docs/latest/images/rc/rc-ri-explore-button.png)](/docs/latest/images/rc/rc-ri-explore-button.png)

You can also select the **Insights** button in the top-right corner to view the **Insights** panel.

[![The Insights button](/docs/latest/images/rc/rc-ri-insights-button.png)](/docs/latest/images/rc/rc-ri-insights-button.png)

## On this page

