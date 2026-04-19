---
title: "Datadog with Redis Software"
source: "https://redis.io/docs/latest/integrate/datadog-with-redis-enterprise/"
canonical_url: "https://redis.io/docs/latest/integrate/datadog-with-redis-enterprise/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:09:32.768Z"
content_hash: "53a4aa8e6d6def5ba178b70cfddacf2f2696d3c9078327516a9508e4876a1ab7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Datadog with Redis Software","→","Datadog with Redis Software"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Datadog with Redis Software","→","Datadog with Redis Software"]
nav_prev: {"path": "redis/docs/latest/integrate/datadog-with-redis-cloud/index.md", "title": "Datadog with Redis Cloud"}
nav_next: {"path": "redis/docs/latest/integrate/dynatrace-with-redis-cloud/index.md", "title": "Dynatrace with Redis Cloud"}
---

# Datadog with Redis Software

To collect, view, and monitor metrics data from your databases and other cluster components, you can connect Datadog to your Redis Software cluster using the Redis Datadog Integration.

[Datadog](https://www.datadoghq.com/) is used by organizations of all sizes and across a wide range of industries to enable digital transformation and cloud migration, drive collaboration among development, operations, security and business teams, accelerate time to market for applications, reduce time to problem resolution, secure applications and infrastructure, understand user behavior, and track key business metrics.

The Datadog Integration for Redis Software uses Datadog's Integration API to connect to Redis metrics exporters. The integration is based on the Datadog [OpenMetrics integration](https://datadoghq.dev/integrations-core/base/openmetrics/) in their core API. This integration enables Redis Software users to export metrics directly to Datadog for analysis, and includes Redis-designed dashboards for use in monitoring Redis Software clusters.

This integration makes it possible to:

*   Collect and display metrics not available in the admin console
*   Set up automatic alerts for node or cluster events
*   Display these metrics alongside data from other systems

[![](/docs/latest/images/rc/redis-cloud-datadog.png)](/docs/latest/images/rc/redis-cloud-datadog.png)

## Install Redis' Datadog Integration for Redis Software

Installing the Datadog integration is a two-step process. Firstly, the installation must be part of your configuration. Select 'Integrations' from the menu in the Datadog portal and then enter 'Redis' in the search bar, then select 'Redis Software by Redis, Inc.'. Next click 'Install Integration' in the top-right corner of the overview page. Once it has been installed follow the instructions for adding an instance to the conf.yaml in /etc/datadog-agent/conf.d/redis\_cloud.d.

After you have edited the conf.yaml file please restart the service and check its status:

```shell
sudo service datadog-agent restart
```

followed by:

```shell
sudo service datadog-agent status
```

to be certain that the service itself is running and did not encounter any problems. Next, check the output of the service; in the terminal on the Datadog agent host run the following command:

```shell
tail -f /var/log/datadog/agent.log
```

It will take several minutes for data to reach Datadog. Finally, check the Datadog console by selecting Infrastructure -> Host Map from the menu and then finding the host that is monitoring the Redis Software instance. The host should be present, and in its list of components there should be a section called 'rdse', which is the namespace used by the Redis Software integration, although this can take several minutes to appear. It is also possible to verify the metrics by choosing Metrics -> Explorer from the menu and entering 'rdse.bdb\_up'.

## View metrics

The Redis Software Integration for Datadog contains pre-defined dashboards to aid in monitoring your Redis Software deployment.

The following dashboards are currently available:

*   Overview
*   Database
*   Node
*   Shard
*   Active-Active
*   Proxy
*   Proxy Threads

## Monitor metrics

See [Observability and monitoring guidance](/docs/latest/integrate/prometheus-with-redis-enterprise/observability/) for monitoring details.

## On this page
