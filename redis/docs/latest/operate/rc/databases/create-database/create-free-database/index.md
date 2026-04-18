---
title: "Create a free database"
source: "https://redis.io/docs/latest/operate/rc/databases/create-database/create-free-database/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/create-database/create-free-database/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:35.292Z"
content_hash: "b34bee63346308e55df10475f7253fbaad539c35c32a73787bae7e040a6ffbb3"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Create a database","→","Create a database","→\n      \n        Create a free database","→","Create a free database"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Create a database","→","Create a database","→\n      \n        Create a free database","→","Create a free database"]
nav_prev: {"path": "redis/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/cloud-account-settings/index.md", "title": "Create and edit Cloud accounts"}
nav_next: {"path": "redis/docs/latest/develop/get-started/document-database/index.md", "title": "Redis as a document database quick start guide"}
---

# Create a free database

Shows how to create a free database.

Redis Cloud

Free databases are perfect for learning and exploring Redis. You get 30 MB of space for you to learn Redis concepts and develop application prototypes.

Note:

You can only have one free database per account. If you already have a free database, you can [delete it](/docs/latest/operate/rc/databases/delete-database/) or [upgrade it to a paid Essentials plan](/docs/latest/operate/rc/subscriptions/view-essentials-subscription/#upgrade-plan) before creating a new one.

Before creating a Redis Cloud database, you need to [create an account](/docs/latest/operate/rc/rc-quickstart/).

To create a database in your Redis Cloud account:

1.  Sign in to the [Redis Cloud console](https://cloud.redis.io).
    
2.  Select the **New database** button.
    
    [![The New Database button creates a new database.](/docs/latest/images/rc/button-database-new.png)](/docs/latest/images/rc/button-database-new.png)
    
    This displays the **Create database** screen.
    

3.  Select the type of [subscription](/docs/latest/operate/rc/subscriptions/) you need. For this guide, select **Free**.
    
    [![The Subscription selection panel with Free selected.](/docs/latest/images/rc/create-database-subscription-free.png)](/docs/latest/images/rc/create-database-subscription-free.png)
    
    After you select **Free**, the rest of the database settings will appear.
    
    [![The database name, cloud vendor, and region settings.](/docs/latest/images/rc/create-database-free-settings.png)](/docs/latest/images/rc/create-database-free-settings.png)
4.  Redis will generate a database name for you. If you want to change it, you can do so in the **Database name** field.
    
5.  Select the **Database version** you want to use.
    
6.  Choose your **Cloud vendor** and **Region**. You can choose between **Amazon Web Services (AWS)**, **Google Cloud**, and **Microsoft Azure** for the Cloud Vendor.
    
    [![The list of available cloud vendors.](/docs/latest/images/rc/create-database-essentials-cloud-vendor-list.png)](/docs/latest/images/rc/create-database-essentials-cloud-vendor-list.png)
    
    See [Supported regions](/docs/latest/operate/rc/supported-regions/) for a list of supported regions by cloud vendor.
    
7.  Select **Create database**.
    
    [![Select the Create database button to create your new database.](/docs/latest/images/rc/button-create-db.png)](/docs/latest/images/rc/button-create-db.png)
    
    When you create your database, there's a brief pause while your request is processed and then the **Database details** page appears.
    

You can now [connect to your database](/docs/latest/operate/rc/databases/connect/) and start working with Redis. Once your app is ready to scale up, you can [upgrade to a paid Essentials plan](/docs/latest/operate/rc/subscriptions/view-essentials-subscription/#upgrade-plan) at any time.

