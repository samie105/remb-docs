---
title: "Create an Essentials database"
source: "https://redis.io/docs/latest/operate/rc/databases/create-database/create-essentials-database/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/create-database/create-essentials-database/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:46.462Z"
content_hash: "43957de12c413b0274ff5a19edf79c3d731dff02b6b20d5113cfff06c83341d2"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Create a database","→","Create a database","→\n      \n        Create an Essentials database","→","Create an Essentials database"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Create a database","→","Create a database","→\n      \n        Create an Essentials database","→","Create an Essentials database"]
---
# Create an Essentials database

Shows how to create an Essentials database.

Redis Cloud

Redis Cloud Essentials is cost-efficient and designed for low-throughput scenarios. You can quickly scale up your Essentials database as your application grows.

Before creating a Redis Cloud database, you need to [create an account](/docs/latest/operate/rc/rc-quickstart/).

To create a database in your Redis Cloud account:

1.  Sign in to the [Redis Cloud console](https://cloud.redis.io).
    
2.  Select the **New database** button.
    
    [![The New Database button creates a new database.](/docs/latest/images/rc/button-database-new.png)](/docs/latest/images/rc/button-database-new.png)
    
    This displays the **Create database** screen.
    

3.  Select the type of [subscription](/docs/latest/operate/rc/subscriptions/) you need. For this guide, select **Essentials**.
    
    [![The Subscription selection panel with Essentials selected.](/docs/latest/images/rc/create-database-subscription-essentials.png)](/docs/latest/images/rc/create-database-subscription-essentials.png)
    
    Note:
    
    This guide shows how to create a paid Essentials database.
    
    *   If you want to create a free Essentials database, see [Create a free database](/docs/latest/operate/rc/rc-quickstart/). You can only have one free database per account.
    *   If you'd rather create a Pro database, see [Create a Pro database with a new subscription](/docs/latest/operate/rc/databases/create-database/create-pro-database-new/).
    *   If you already have a Pro subscription and want to add a database to it, see [Create a Pro database in an existing subscription](/docs/latest/operate/rc/databases/create-database/create-pro-database-existing/).
    
    After you select **Essentials**, the rest of the database details will appear.
    
    [![The database name, cloud vendor, version, region, type, and durability settings.](/docs/latest/images/rc/create-database-essentials-cloud-vendor.png)](/docs/latest/images/rc/create-database-essentials-cloud-vendor.png)
4.  Select **RAM** or **Flex** to choose between a database that uses only RAM or one that uses both RAM and Flash memory.
    
    Choose Flex for larger datasets and cost-efficient scale when you can tolerate single-digit millisecond latency for warm data. Choose RAM when you need the absolute lowest latency for all data. To learn more about Flex, see [Create a Flex database](/docs/latest/operate/rc/databases/create-database/create-flex-database/).
    
5.  Redis will generate a database name for you. If you want to change it, you can do so in the **Name** field.
    
6.  Choose a **Cloud vendor** for your database from the list. You can choose between **Amazon Web Services (AWS)**, **Google Cloud**, and **Microsoft Azure** for the Cloud Vendor.
    
    [![The list of available cloud vendors.](/docs/latest/images/rc/create-database-essentials-cloud-vendor-list.png)](/docs/latest/images/rc/create-database-essentials-cloud-vendor-list.png)
7.  Choose a **Region** from the list. See [Supported regions](/docs/latest/operate/rc/supported-regions/) for a list of supported regions by cloud vendor.
    
8.  Select the **Database version** you want to use.
    
9.  The **Type** of database controls the protocol and advanced capabilities. Leave this as **Redis** unless you have a legacy application that uses **Memcached**.
    
10.  Select your desired memory limit.
     
     [![Available Essentials plans.](/docs/latest/images/rc/subscription-new-fixed-tiers.png)](/docs/latest/images/rc/subscription-new-fixed-tiers.png)
     
     For a comparison of available plans, see [Redis Cloud Essentials plans](/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details/).
     
11.  Choose your **High availability (replication)** settings.
     
     Redis Cloud supports the following high availability settings:
     
     *   **None**: You will have a single copy of your database without replication.
     *   **Single-Zone**: Your database will have a primary and a replica located in the same cloud zone. If anything happens to the primary, the replica takes over and becomes the new primary.
     *   **Multi-Zone**: The primary and its replicas are stored in different zones. This means that your database can remain online even if an entire zone becomes unavailable.
     
     See [High availability](/docs/latest/operate/rc/databases/configuration/high-availability/) for more information about these settings.
     
12.  Choose your **Data persistence** settings from the list.
     
     Redis Cloud supports the following data persistence options:
     
     *   An **Append-Only File** maintains a record (sometimes called a _redo log_ or _journal_) of write operations. This allows the data to be restored by using the record to reconstruct the database up to the point of failure. For Essentials databases, Redis updates the Append-Only file every second.
         
     *   A **Snapshot** is a copy of the in-memory database, taken at periodic intervals (one, six, or twelve hours). You can restore data to the snapshot's point in time.
         
     
     See [Data persistence](/docs/latest/operate/rc/databases/configuration/data-persistence/) for more information about these settings.
     
13.  Enter your payment details.
     
     If you haven't previously entered a payment method, use the **Add Credit Card** button to add one.
     
     [![The Add credit card icon.](/docs/latest/images/rc/icon-add.png)](/docs/latest/images/rc/icon-add.png)
     
     If you have not already added a business address to your account, you must enter one. Redis uses your business address for communication, invoicing, and tax purposes.
     
     [![The Add credit card screen before a business address has already been added.](/docs/latest/images/rc/billing-add-first-card.png)](/docs/latest/images/rc/billing-add-first-card.png)
     
     If you already have a business address, you don't need to enter one here. See [Account settings](/docs/latest/operate/rc/accounts/account-settings/) to learn how to update your business address.
     
     [![The Add credit card screen after a business address has already been added.](/docs/latest/images/rc/billing-add-credit-card.png)](/docs/latest/images/rc/billing-add-credit-card.png)
     
     If the card's billing address is the same as your account's business address, select **Same as business address** to fill the billing address with your business address details.
     
14.  Select **Confirm & pay** to create your database.
     

[![Select Confirm & Pay to create your new database.](/docs/latest/images/rc/button-create-db-confirm-pay.png)](/docs/latest/images/rc/button-create-db-confirm-pay.png)

When you create your database, there's a brief pause while your request is processed and then the **Database details** page appears.

You can now [connect to your database](/docs/latest/operate/rc/databases/connect/) and start working with Redis.
