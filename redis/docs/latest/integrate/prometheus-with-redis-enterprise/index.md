---
title: "Prometheus and Grafana with Redis Software"
source: "https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise/"
canonical_url: "https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:13.338Z"
content_hash: "a6f853ba32c842fc8590299099da0b4c71805c210a741f57734a3013edec0444"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Prometheus and Grafana with Redis Software","→","Prometheus and Grafana with Redis Software"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Prometheus and Grafana with Redis Software","→","Prometheus and Grafana with Redis Software"]
nav_prev: {"path": "redis/docs/latest/integrate/prometheus-with-redis-cloud/index.md", "title": "Prometheus and Grafana with Redis Cloud"}
nav_next: {"path": "redis/docs/latest/integrate/pulumi-provider-for-redis-cloud/index.md", "title": "Pulumi provider for Redis Cloud"}
---

# Prometheus and Grafana with Redis Software

Use Prometheus and Grafana to collect and visualize Redis Software metrics.

You can use Prometheus and Grafana to collect and visualize your Redis Software metrics.

Metrics are exposed at the cluster, node, database, shard, and proxy levels.

*   [Prometheus](https://prometheus.io/) is an open source systems monitoring and alerting toolkit that aggregates metrics from different sources.
*   [Grafana](https://grafana.com/) is an open source metrics visualization tool that processes Prometheus data.

You can use Prometheus and Grafana to:

*   Collect and display metrics not available in the Cluster Manager UI
    
*   Set up automatic alerts for all resources
    
*   Display Redis Software metrics alongside data from other systems
    

[![Graphic showing how Prometheus and Grafana collect and display data from a Redis Software Cluster. Prometheus collects metrics from the Redis Software cluster, and Grafana queries those metrics for visualization.](/docs/latest/images/rs/grafana-prometheus.png)](/docs/latest/images/rs/grafana-prometheus.png)

To get started with Prometheus and Grafana, see the following [quick start](#quick-start) or see [Redis Software Observability with Prometheus and Grafana](https://redis.io/learn/operate/observability/redis-software-prometheus-and-grafana) for a more detailed tutorial.

## Quick start

To get started with Prometheus and Grafana:

1.  Create a directory called 'prometheus' on your local machine.
    
2.  Within that directory, create a configuration file called `prometheus.yml`.
    
3.  Add the following contents to the configuration file and replace `<cluster_name>` with your Redis Software cluster's FQDN:
    
     v2 (metrics stream engine)  v1
    
    ```yml
    global:
      scrape_interval: 15s
      evaluation_interval: 15s
    
    # Attach these labels to any time series or alerts when communicating with
    # external systems (federation, remote storage, Alertmanager).
      external_labels:
        monitor: "prometheus-stack-monitor"
    
    # Load and evaluate rules in this file every 'evaluation_interval' seconds.
    #rule_files:
    # - "first.rules"
    # - "second.rules"
    
    scrape_configs:
    # scrape Prometheus itself
      - job_name: prometheus
        scrape_interval: 10s
        scrape_timeout: 5s
        static_configs:
          - targets: ["localhost:9090"]
    
    # scrape Redis Software
      - job_name: redis-enterprise
        scrape_interval: 30s
        scrape_timeout: 30s
        metrics_path: /v2
        scheme: https
        tls_config:
          insecure_skip_verify: true
        static_configs:
          - targets: ["<cluster_name>:8070"]
    ```
    
4.  Set up your Prometheus and Grafana servers.
    
    Note:
    
    We recommend running Prometheus in Docker only for development and testing.
    
    To set up Prometheus and Grafana on Docker:
    
    1.  Create a _docker-compose.yml_ file:
        
        ```yml
        version: '3'
        services:
            prometheus-server:
                image: prom/prometheus
                ports:
                    - 9090:9090
                volumes:
                    - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
        
            grafana-ui:
                image: grafana/grafana
                ports:
                    - 3000:3000
                environment:
                    - GF_SECURITY_ADMIN_PASSWORD=secret
                links:
                    - prometheus-server:prometheus
        ```
        
    2.  To start the containers, run:
        
        ```sh
        $ docker compose up -d
        ```
        
    3.  To check that all of the containers are up, run:
        
        ```sh
        docker ps
        ```
        
    4.  In your browser, sign in to Prometheus at `http://localhost:9090` to make sure the server is running.
        
    5.  Select **Status** and then **Targets** to check that Prometheus is collecting data from your Redis Software cluster.
        
        [![The Redis Software target showing that Prometheus is connected to the Redis Software Cluster.](/docs/latest/images/rs/prometheus-target.png)](/docs/latest/images/rs/prometheus-target.png)
        
        If Prometheus is connected to the cluster, you can type **node\_up** in the Expression field on the Prometheus home page to see the cluster metrics.
        
5.  Configure the Grafana datasource:
    
    1.  Sign in to Grafana. If you installed Grafana locally, go to `http://localhost:3000` and sign in with:
        
        *   Username: admin
        *   Password: secret
    2.  In the Grafana configuration menu, select **Data Sources**.
        
    3.  Select **Add data source**.
        
    4.  Select **Prometheus** from the list of data source types.
        
        [![The Prometheus data source in the list of data sources on Grafana.](/docs/latest/images/rs/prometheus-datasource.png)](/docs/latest/images/rs/prometheus-datasource.png)
    5.  Enter the Prometheus configuration information:
        
        *   Name: `redis-enterprise`
        *   URL: `http://<your prometheus server name>:9090`
        
        [![The Prometheus connection form in Grafana.](/docs/latest/images/rs/prometheus-connection.png)](/docs/latest/images/rs/prometheus-connection.png)
    
    Note:
    
    *   If the network port is not accessible to the Grafana server, select the **Browser** option from the Access menu.
    *   In a testing environment, you can select **Skip TLS verification**.
    
6.  Add dashboards for cluster, database, node, and shard metrics. To add preconfigured dashboards:
    
    1.  In the Grafana dashboards menu, select **Manage**.
    2.  Click **Import**.
    3.  Upload one or more [Grafana dashboards](#grafana-dashboards-for-redis-enterprise).

## Grafana dashboards for Redis Software

Redis publishes preconfigured dashboards for Redis Software and Grafana.

Note:

V1 dashboards are not compatible with the v2 metrics exporter endpoint. Make sure to use the correct dashboard version for your metrics endpoint.

These dashboards are open source. For additional dashboard options, or to file an issue, see the [Redis Software observability Github repository](https://github.com/redis-field-engineering/redis-enterprise-observability/).

For more information about configuring Grafana dashboards, see the [Grafana documentation](https://grafana.com/docs/).

### V1 metrics dashboards

Use the following dashboards when connecting to the v1 metrics endpoint (`https://<cluster_name>:8070/`):

*   The [cluster status dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/software/basic/redis-software-cluster-dashboard_v9-11.json) provides an overview of your Redis Software clusters.
*   The [database status dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/software/basic/redis-software-database-dashboard_v9-11.json) displays specific database metrics, including latency, memory usage, ops/second, and key count.
*   The [node metrics dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/software/basic/redis-software-node-dashboard_v9-11.json) provides metrics for each of the nodes hosting your cluster.
*   The [shard metrics dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/software/basic/redis-software-shard-dashboard_v9-11.json) displays metrics for the individual Redis processes running on your cluster nodes.
*   The [Active-Active dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/software/basic/redis-software-active-active-dashboard_v9-11.json) displays metrics specific to [Active-Active databases](/docs/latest/operate/rs/databases/active-active/).

### V2 metrics dashboards

Use the following dashboards when connecting to the v2 metrics endpoint (`https://<cluster_name>:8070/v2`):

*   The [cluster status dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/software/basic/redis-software-cluster-dashboard_v9-11.json) provides an overview of your Redis Software clusters.
*   The [database status dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/software/basic/redis-software-database-dashboard_v9-11.json) displays specific database metrics, including latency, memory usage, ops/second, and key count.
*   The [node metrics dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/software/basic/redis-software-node-dashboard_v9-11.json) provides metrics for each of the nodes hosting your cluster.
*   The [shard metrics dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/software/basic/redis-software-shard-dashboard_v9-11.json) displays metrics for the individual Redis processes running on your cluster nodes.
*   The [Active-Active dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/software/basic/redis-software-active-active-dashboard_v9-11.json) displays metrics specific to [Active-Active databases](/docs/latest/operate/rs/databases/active-active/).
*   The [QPS dashboard - Redis Search metrics](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana_v2/dashboards/grafana_v9-11/search/RediSearchQPS.json) displays metrics specific to Redis Search, showcasing QPS, Query Latency, Indexing performance, and more.
*   The [OPS dashboards](https://github.com/redis-field-engineering/redis-enterprise-observability/tree/main/grafana_v2/dashboards/grafana_v9-11/software/ops) are advanced operational dashboards for on-premises deployments.

## On this page
