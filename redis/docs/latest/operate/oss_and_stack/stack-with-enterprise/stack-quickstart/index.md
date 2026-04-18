---
title: "Redis Open Source quick start"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/stack-quickstart/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/stack-quickstart/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:21.116Z"
content_hash: "61bd5970cebec696f2b4445d47056fb0356c8cd628d1cbcdb772474945e14235"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Redis Open Source quick start","→","Redis Open Source quick start"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Redis Open Source quick start","→","Redis Open Source quick start"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/index.md", "title": "Prepare source databases"}
nav_next: {"path": "redis/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/oracle/index.md", "title": "Prepare Oracle and Oracle RAC for RDI"}
---

# Redis Open Source quick start

To quickly set up a database with Redis Stack (Redis Open Source) features, you can sign up for a free [Redis Cloud](https://cloud.redis.io/#/sign-up) subscription and create a Redis Stack database.

Alternatively, you can use one of these methods:

*   [Redis Software](/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart/)
*   Redis Software in a [Docker container](/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart/)
*   [Other platforms](/docs/latest/operate/kubernetes/) for Redis Software

## Set up a Redis Cloud database

To set up a Redis Cloud database with Redis Stack features, follow these steps:

1.  [Create a new Redis Cloud subscription](#create-a-subscription).
    
2.  [Create a Redis Stack database](#create-a-redis-stack-database).
    
3.  [Connect to the database](#connect-to-the-database).
    

For more details, see the Redis Cloud [quick start](/docs/latest/operate/rc/rc-quickstart/).

### Create a subscription

To create a new subscription:

1.  Sign in to the Redis Cloud [admin console](http://cloud.redis.io) or create a new account.
    
2.  Select the **New subscription** button:
    
    [![The New subscriptions button in the admin console menu.](/docs/latest/images/rc/button-subscription-new.png)](/docs/latest/images/rc/button-subscription-new.png)
3.  Configure your subscription:
    
    1.  Select **Fixed plans**.
    2.  For the cloud vendor, select **Amazon Web Services** (AWS), **Google Cloud** (GCP), or **Microsoft Azure**.
    3.  Select a region to deploy the subscription to.
    4.  From the dataset size list, select the Free tier (30MB).
    5.  Enter a name for the subscription.
4.  Select the **Create subscription** button:
    
    [![The Create Subscription button.](/docs/latest/images/rc/button-subscription-create.png)](/docs/latest/images/rc/button-subscription-create.png)

### Create a Redis Stack database

After you create a subscription, follow these steps to create a Redis Stack database:

1.  Select the **New database** button:
    
    [![The New Database button creates a new database for your subscription.](/docs/latest/images/rc/button-database-new.png)](/docs/latest/images/rc/button-database-new.png)
2.  In **General** settings, enter a **Database name**.
    
3.  For database **Type**, select **Redis Stack**.
    
4.  Select the **Activate database** button:
    
    [![Use the Activate database button to create and activate your database.](/docs/latest/images/rc/button-database-activate.png)](/docs/latest/images/rc/button-database-activate.png)

### Connect to the database

After creating the database, you can view its **Configuration** settings. You will need the following information to connect to your new database:

*   **Public endpoint**: The host address of the database
*   **Redis password**/**Default user password**: The password used to authenticate with the database

With this information, you can connect to your database with the [`redis-cli`](/docs/latest/operate/rs/references/cli-utilities/redis-cli/) command-line tool, an application, or [Redis Insight](https://redislabs.com/redisinsight/).

## Try Redis Open Source features

To try out Redis Open Source features, follow the examples provided by the corresponding guides:

*   [Redis Search quick start](/docs/latest/develop/get-started/document-database/)
*   [JSON quick start](/docs/latest/develop/data-types/json/#use-redisjson)
*   [Time series quick start](/docs/latest/develop/data-types/timeseries/)
*   [Probabilistic data structures quick start](/docs/latest/develop/data-types/probabilistic/)

## On this page

