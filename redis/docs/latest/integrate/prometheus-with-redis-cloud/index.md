---
title: "Prometheus and Grafana with Redis Cloud"
source: "https://redis.io/docs/latest/integrate/prometheus-with-redis-cloud/"
canonical_url: "https://redis.io/docs/latest/integrate/prometheus-with-redis-cloud/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:28.249Z"
content_hash: "dcded5cb0111251a95b9be1d724a84345a384f2cd088d2244e725f64d610c367"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Prometheus and Grafana with Redis Cloud","→","Prometheus and Grafana with Redis Cloud"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Prometheus and Grafana with Redis Cloud","→","Prometheus and Grafana with Redis Cloud"]
nav_prev: {"path": "redis/docs/latest/operate/rs/installing-upgrading/install/prepare-install/index.md", "title": "Prepare to install Redis Software"}
nav_next: {"path": "redis/docs/latest/commands/redis-6-2-commands/index.md", "title": "Redis 6.2 Commands Reference"}
---

# Prometheus and Grafana with Redis Cloud

Use Prometheus and Grafana to collect and visualize Redis Cloud metrics.

You can use Prometheus and Grafana to collect and visualize your Redis Cloud metrics.

*   [Prometheus](https://prometheus.io/) is an open source systems monitoring and alerting toolkit that can scrape metrics from different sources.
*   [Grafana](https://grafana.com/) is an open source metrics visualization tool that can process Prometheus data.

Redis Cloud exposes its metrics through a Prometheus endpoint. You can configure your Prometheus server to scrape metrics from your Redis Cloud subscription on port 8070.

The Redis Cloud Prometheus endpoint is exposed on Redis Cloud's internal network. To access this network, enable [VPC peering](/docs/latest/operate/rc/security/vpc-peering/), [Private Service Connect](/docs/latest/operate/rc/security/private-service-connect/), [AWS Transit Gateway](/docs/latest/operate/rc/security/aws-transit-gateway/), or [AWS PrivateLink](/docs/latest/operate/rc/security/aws-privatelink/). Private connectivity options are only available with Redis Cloud Pro. You cannot use Prometheus and Grafana with Redis Cloud Essentials.

Note:

The Prometheus endpoint's metrics cover all databases within a subscription. Any database added to or removed from the subscription is reflected automatically.

For more information on how Prometheus communicates with Redis Software clusters, see [Prometheus integration with Redis Software](/docs/latest/integrate/prometheus-with-redis-enterprise/).

## Quick start

You can quickly set up Prometheus and Grafana for testing using the Prometheus and Grafana Docker images.

### Prerequisites

1.  Create a [Redis Cloud Pro database](/docs/latest/operate/rc/databases/create-database/create-pro-database-new/).
    
2.  Set up [VPC peering](/docs/latest/operate/rc/security/vpc-peering/).
    
3.  Extract the Prometheus endpoint from the private endpoint to your database. The private endpoint is in the [Redis Cloud console](https://cloud.redis.io/) under the [Configuration tab](/docs/latest/operate/rc/databases/view-edit-database/#configuration-tab) of your database. The Prometheus endpoint is on port 8070 of the internal server.
    
    For example, if your private endpoint is:
    
    ```sh
    redis-12345.internal.<cluster_address>:12345
    ```
    
    The Prometheus endpoint is:
    
    ```sh
    internal.<cluster_address>:8070
    ```
    
4.  Create an instance to run Prometheus and Grafana on the same cloud provider as your Redis Cloud subscription (for example, Amazon Web Services or Google Cloud). This instance must:
    
    *   Exist in the same region as your Redis Cloud subscription.
        
    *   Connect to the VPC subnet that is peered with your Redis Cloud subscription.
        
    *   Allow outbound connections to port 8070, so that Prometheus can scrape the Redis Cloud server for data.
        
    *   Allow inbound connections to port 9090 for Prometheus and port 3000 for Grafana.
        
    *   Be located in one of the CIDR ranges of the RFC-1918 internal IP standard, which is comprised of three CIDR ranges:
        
        *   10.0.0.0/8
        *   172.16.0.0/12
        *   192.168.0.0/16
        
        The Prometheus endpoint is subject to a whitelist according to this standard.
        

### Set up Prometheus

To get started with custom monitoring with Prometheus on Docker:

1.  Create a directory on the Prometheus instance called `prometheus` and create a `prometheus.yml` file in that directory.
    
2.  Add the following contents to `prometheus.yml`. Replace `<prometheus_endpoint>` with the Prometheus endpoint.
    
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
    
        # scrape Redis Cloud
        - job_name: redis-cloud
        scrape_interval: 30s
        scrape_timeout: 30s
        metrics_path: /  # For v2, use /v2
        scheme: https
        static_configs:
          - targets: ["<prometheus_endpoint>:8070"]
    ```
    
3.  Create a `docker-compose.yml` file with instructions to set up the Prometheus and Grafana Docker images.
    
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
    
4.  To start the containers, run:
    
    ```sh
    $ docker compose up -d
    ```
    
5.  To check that all the containers are up, run: `docker ps`
    
6.  In your browser, sign in to Prometheus at `http://localhost:9090` to make sure the server is running.
    
7.  Select **Status** and then **Targets** to check that Prometheus is collecting data from the Redis Cloud cluster.
    
    [![The Redis Software target showing that Prometheus is connected to the Redis Software Cluster.](/docs/latest/images/rs/prometheus-target.png)](/docs/latest/images/rs/prometheus-target.png)
    
    If Prometheus is connected to the cluster, you can type **node\_up** in the Expression field on the Prometheus home page to see the cluster metrics.
    

See [Prometheus Metrics](/docs/latest/integrate/prometheus-with-redis-enterprise/prometheus-metrics-definitions/) for a list of metrics that Prometheus collects from Redis Software clusters.

### Set up Grafana

Once the Prometheus and Grafana Docker containers are running, and Prometheus is connected to your Redis Cloud subscription, you can set up your Grafana dashboards.

1.  Sign in to Grafana. If you installed Grafana with Docker, go to `http://localhost:3000` and sign in with:
    
    *   Username: `admin`
    *   Password: `secret`
2.  In the Grafana configuration menu, select **Data Sources**.
    
3.  Select **Add data source**.
    
4.  Select **Prometheus** from the list of data source types.
    
    [![The Prometheus data source in the list of data sources on Grafana.](/docs/latest/images/rs/prometheus-datasource.png)](/docs/latest/images/rs/prometheus-datasource.png)
5.  Enter the Prometheus configuration information:
    
    *   Name: `redis-cloud`
    *   URL: `http://prometheus-server:9090`
    *   Access: `Server`
    
    [![The Prometheus connection form in Grafana.](/docs/latest/images/rc/prometheus-connection.png)](/docs/latest/images/rc/prometheus-connection.png)
    
    Note:
    
    *   If the network port is not accessible to the Grafana server, select the **Browser** option from the Access menu.
    *   In a testing environment, you can select **Skip TLS verification**.
    
6.  Add dashboards for your subscription and database metrics. To add preconfigured dashboards:
    
    1.  In the Grafana dashboards menu, select **Manage**.
    2.  Select **Import**.
    3.  Add the [subscription status](https://grafana.com/grafana/dashboards/18406-subscription-status-dashboard/) and [database status](https://grafana.com/grafana/dashboards/18407-database-status-dashboard/) dashboards.

### Grafana dashboards for Redis Cloud

Redis publishes preconfigured dashboards for Redis Cloud and Grafana:

*   The [subscription status dashboard](https://grafana.com/grafana/dashboards/18406-subscription-status-dashboard/) provides an overview of your Redis Cloud subscriptions.
*   The [database status dashboard](https://grafana.com/grafana/dashboards/18407-database-status-dashboard/) displays specific database metrics, including latency, memory usage, ops/second, and key count.
*   The [Active-Active dashboard](https://github.com/redis-field-engineering/redis-enterprise-observability/blob/main/grafana/dashboards/grafana_v9-11/cloud/basic/redis-cloud-active-active-dashboard_v9-11.json) displays metrics specific to [Active-Active databases](/docs/latest/operate/rc/databases/active-active/).

These dashboards are open source. For additional dashboard options, or to file an issue, see the [Redis Enterprise observability Github repository](https://github.com/redis-field-engineering/redis-enterprise-observability/tree/main/grafana).

For more information about configuring Grafana dashboards, see the [Grafana documentation](https://grafana.com/docs/).

## On this page


