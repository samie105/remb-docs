---
title: "Create a Bedrock knowledge base"
source: "https://redis.io/docs/latest/integrate/amazon-bedrock/create-knowledge-base/"
canonical_url: "https://redis.io/docs/latest/integrate/amazon-bedrock/create-knowledge-base/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:16.517Z"
content_hash: "44e17f07083de227766628dcab608320e25a9a5d113b52d760900cff5bb40d20"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock","→\n      \n        Create a Bedrock knowledge base","→","Create a Bedrock knowledge base"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock","→\n      \n        Create a Bedrock knowledge base","→","Create a Bedrock knowledge base"]
nav_prev: {"path": "redis/docs/latest/develop/clients/lettuce/amr/index.md", "title": "Connect to Azure Managed Redis"}
nav_next: {"path": "redis/docs/latest/develop/clients/nodejs/amr/index.md", "title": "Connect to Azure Managed Redis"}
---

# Create a Bedrock knowledge base

Shows how to set up your Knowledge base in Amazon Bedrock.

After you have set up a vector database with Redis Cloud, you can use it to create a knowledge base for your models.

Before you begin this guide, you will need:

*   An [AWS S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) with text data that you want to use to train your models.
    
*   An [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) with permissions for the Bedrock knowledge base.
    
*   A Redis database that is [set up for Amazon Bedrock](/docs/latest/integrate/amazon-bedrock/set-up-redis/)
    

## Create knowledge base

To use your Redis database to create a knowledge base on Amazon Bedrock:

1.  Sign in to the [AWS console](https://console.aws.amazon.com/).
    
2.  Use the **Services** menu to locate and select **Machine Learning** > **Amazon Bedrock**. This takes you to the Amazon Bedrock admin panel.
    
3.  Select **Knowledge base** > **Create knowledge base** to create your knowledge base.
    
    [![The Create knowledge base button.](/docs/latest/images/rc/bedrock-aws-button-create-knowledge-base.png)](/docs/latest/images/rc/bedrock-aws-button-create-knowledge-base.png)
4.  In the **Knowledge base details** section, enter a name and description for your knowledge base.
    
5.  Select the IAM role for the Bedrock knowledge base in the **IAM Permissions** section. Select **Next** to add the data source.
    
6.  Enter a name for the data source and connect your S3 bucket in the **Data source** section.
    
7.  In the **Vector database** section, select **Redis Cloud** and select the checkbox to agree with the legal disclaimer.
    
    [![The Redis Cloud selection for your vector database.](/docs/latest/images/rc/bedrock-aws-select-redis-vector-db.png)](/docs/latest/images/rc/bedrock-aws-select-redis-vector-db.png)
    
    Fill in the fields with the following information:
    
    *   **Endpoint URL**: Public endpoint of your database. This can be found in the [Redis Cloud console](https://cloud.redis.io/) from the database list or from the **General** section of the **Configuration** tab for the source database.
    *   **Credentials Secret ARN**: [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources) of your [database credentials secret](/docs/latest/integrate/amazon-bedrock/set-up-redis/#store-secret).
    *   **Vector Index name**: Name of the [vector index](/docs/latest/integrate/amazon-bedrock/set-up-redis/#create-vector-index)
    *   **Vector field**: Name of the [vector field](/docs/latest/integrate/amazon-bedrock/set-up-redis/#create-vector-index) of the vector index
    *   **Text field**: Name of the [text field](/docs/latest/integrate/amazon-bedrock/set-up-redis/#create-vector-index) of the vector index
    *   **Metadata field**: Name of the [metadata field](/docs/latest/integrate/amazon-bedrock/set-up-redis/#create-vector-index) of the vector index
    
    Select **Next** to review your settings.
    
8.  Review your knowledge base before you create it. Select **Create knowledge base** to finish creation.
    
    [![The Create knowledge base button.](/docs/latest/images/rc/bedrock-aws-button-create-knowledge-base.png)](/docs/latest/images/rc/bedrock-aws-button-create-knowledge-base.png)

Amazon Bedrock will sync the data from the S3 bucket and load it into your Redis database. This will take some time.

Your knowledge base will have a status of **Ready** when it is ready to be connected to an Agent.

[![A Bedrock knowledge base with a Ready status.](/docs/latest/images/rc/bedrock-aws-status-knowledge-base-ready.png)](/docs/latest/images/rc/bedrock-aws-status-knowledge-base-ready.png)

Select the name of your knowledge base to view the syncing status of your data sources. The data source will have a status of **Ready** when it is synced to the vector database.

[![A Bedrock data source with a Ready status.](/docs/latest/images/rc/bedrock-aws-status-data-source-ready.png)](/docs/latest/images/rc/bedrock-aws-status-data-source-ready.png)

After the knowledge base is ready, you can use it to [Create an agent](/docs/latest/integrate/amazon-bedrock/create-agent/).

## On this page
