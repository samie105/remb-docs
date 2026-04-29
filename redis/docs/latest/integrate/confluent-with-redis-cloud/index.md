---
title: "Confluent with Redis Cloud"
source: "https://redis.io/docs/latest/integrate/confluent-with-redis-cloud/"
canonical_url: "https://redis.io/docs/latest/integrate/confluent-with-redis-cloud/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:03.231Z"
content_hash: "ea5cb934aa70e81b2e5edde7dc7af038fb20dbe74435337d54e043d953e7dae5"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Confluent with Redis Cloud","→","Confluent with Redis Cloud"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Confluent with Redis Cloud","→","Confluent with Redis Cloud"]
nav_prev: {"path": "redis/docs/latest/integrate/amazon-bedrock/set-up-redis/index.md", "title": "Set up Redis for Bedrock"}
nav_next: {"path": "redis/docs/latest/integrate/datadog-with-redis-cloud/index.md", "title": "Datadog with Redis Cloud"}
---

# Confluent with Redis Cloud

Describes how to integrate Redis Cloud into Confluent Cloud.

You can send data from [Confluent Cloud](https://confluent.cloud/) to your Redis Cloud database using the [Redis Sink connector for Confluent Cloud](https://docs.confluent.io/cloud/current/connectors/cc-redis-sink.html).

## Prerequisites

Before you add the Redis Sink Confluent connector to your Confluent Cloud cluster:

1.  [Create a database](/docs/latest/operate/rc/databases/create-database/) in the same region as your Confluent Cloud cluster.
    
2.  If you decide to [enable Transport Layer Security (TLS)](/docs/latest/operate/rc/security/database-security/tls-ssl/) for your Redis database, [download the server certificate](/docs/latest/operate/rc/security/database-security/tls-ssl/#download-certificates) from the Redis Cloud console and [encode it](#encode-server-certificate) to be used with Confluent Cloud.
    
3.  Ensure you meet the prerequisites in the [Redis Sink connector documentation](https://docs.confluent.io/cloud/current/connectors/cc-redis-sink.html#quick-start) to set up your Redis Sink with Confluent Cloud.
    

### Encode server certificate

If you decide to enable Transport Layer Security (TLS) for your database, you will need to encode the [server certificate](/docs/latest/operate/rc/security/database-security/tls-ssl/#download-certificates) (`redis_ca.pem`) for use as the Confluent Cloud Truststore file. To do this:

1.  Use a base64 utility to encode `redis_ca.pem` into base64 in a new file. For example, using the [`base64` command-line utility](https://linux.die.net/man/1/base64):
    
    ```sh
    $ base64 -i redis_ca.pem -o <truststore_file_name>
    ```
    
2.  Using a text editor, add the following text to the beginning of the truststore file:
    
    ```text
    data:text/plain;base64
    ```
    
3.  Save and close the truststore file.
    

## Connect the Redis Sink connector to Redis Cloud

To add the Redis Sink connector to your Confluent Cloud environment from the Redis Cloud console:

1.  From the [Redis Cloud console](https://cloud.redis.io/), select **Account Settings** and then select the **Integrations** tab.
    
2.  Select the **Configure** button in the **Confluent** tile.
    
    [![The Confluent integration tile.](/docs/latest/images/rc/account-settings-integrations-confluent.png)](/docs/latest/images/rc/account-settings-integrations-confluent.png)
3.  This will take you to [New Sink Connector](https://confluent.cloud/go/new-sink-connector/RedisSink) on Confluent Cloud. If you have more than one Confluent Cloud environment or Cluster, select your environment and cluster from the lists and select **Continue**.
    
    [![Select your environment and cluster from the Create a Connector selector.](/docs/latest/images/rc/confluent-create-connector.png)](/docs/latest/images/rc/confluent-create-connector.png)
4.  From there, follow the steps to [Enter the connector details](https://docs.confluent.io/cloud/current/connectors/cc-redis-sink.html#step-4-enter-the-connector-details) on the Confluent documentation.
    
    When you get to the **Authentication** step, fill in the fields with the following information:
    
    *   **Redis hostname**: The Public endpoint of your database, without the port number. This can be found in the [Redis Cloud console](https://cloud.redis.io/) from the database list or from the **General** section of the **Configuration** tab for the source database.
    *   **Redis port number**: The database's port. This is the number at the end of your database's Public endpoint.
    *   **Redis database index**: Set this to 0 for a Redis Cloud database.
    *   **Redis server password**: Enter the database password. If you have not set your own database user and password, use the [default user password](../../operate/rc/security/access-control/data-access-control/default-user/index.md), which appears in the **Security** section of the **Configuration** tab of the database details screen.
    *   **SSL mode**: Set depending on what type of [TLS authentication](/docs/latest/operate/rc/security/database-security/tls-ssl/) is set for your database.
        *   If TLS authentication is turned off, select **disabled**.
        *   If TLS authentication is turned on, select **server**.
    *   **Trustore file**: If the **SSL mode** is set to **server**, upload the truststore file created when you [encoded the server certificate](#encode-server-certificate).
    *   **Redis Server mode**: If [OSS Cluster API](/docs/latest/operate/rc/databases/configuration/clustering/#oss-cluster-api) is enabled, select **Cluster**. Otherwise, select **Standalone**.
    
    Select **Continue** once you have entered the database information. Enter the rest of the [connector details](https://docs.confluent.io/cloud/current/connectors/cc-redis-sink.html#step-4-enter-the-connector-details) from the **Configuration** step.
    
5.  [Connect to your database](/docs/latest/operate/rc/rc-quickstart/#connect-to-a-database) to verify that data is being stored.
    

## On this page
