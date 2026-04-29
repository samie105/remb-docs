---
title: "RDI on Redis Cloud quick start"
source: "https://redis.io/docs/latest/operate/rc/databases/rdi/quick-start/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/rdi/quick-start/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:36.597Z"
content_hash: "4e5ac6d34d025300a13ef9968296f998938519c54c0d7602e43764e43519c3c9"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        RDI on Redis Cloud quick start","→","RDI on Redis Cloud quick start"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        RDI on Redis Cloud quick start","→","RDI on Redis Cloud quick start"]
nav_prev: {"path": "redis/docs/latest/operate/rc/databases/rdi/define/index.md", "title": "Define data pipeline"}
nav_next: {"path": "redis/docs/latest/operate/rc/databases/rdi/setup/index.md", "title": "Prepare source database"}
---

# RDI on Redis Cloud quick start

Learn how to create a data pipeline between a PostgreSQL source database created with Terraform and a Redis Cloud target database.

Redis Cloud

The [`rdi-cloud-automation` GitHub repository](https://github.com/redis/rdi-cloud-automation) contains a Terraform script that quickly sets up a PostgreSQL source database on an EC2 instance and all required permissions and network setup to connect it to a Redis Cloud target database.

Note:

This guide is for demonstration purposes only. It is not recommended for production use.

## Prerequisites

To follow this guide, you need to:

1.  Create a [Redis Cloud Pro database](/docs/latest/operate/rc/databases/create-database/create-pro-database-new/) hosted on Amazon Web Services (AWS).
    
    Turn on Multi-AZ replication and [manually select the availability zones](/docs/latest/operate/rc/databases/configuration/high-availability/#availability-zones) when creating the database.
    
2.  Install the [AWS CLI](https://aws.amazon.com/cli/) and set up [credentials for the CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).
    
3.  Install [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).
    

## Create a data pipeline

1.  On the [Redis Cloud console](https://cloud.redis.io/), go to your target database and select the **Data Pipeline** tab.
    
2.  Select **Create pipeline**. [![The create pipeline button.](/docs/latest/images/rc/rdi/rdi-create-data-pipeline.png)](/docs/latest/images/rc/rdi/rdi-create-data-pipeline.png)
    
3.  Select **PostgreSQL** as the source database type. [![The select source database type list.](/docs/latest/images/rc/rdi/rdi-select-source-db.png)](/docs/latest/images/rc/rdi/rdi-select-source-db.png)
    
4.  Under **Source database credentials and certificates**, save the provided ARN. This will be the `redis_secrets_arn` you will need later.
    
    [![The setup connectivity section containing the credentials ARN.](/docs/latest/images/rc/rdi/rdi-credentials-arn.png)](/docs/latest/images/rc/rdi/rdi-credentials-arn.png)
5.  Under **Setup connectivity**, save the provided ARN. This will be the `redis_privatelink_arn` you will need later.
    
    [![The setup connectivity section containing the private link ARN.](/docs/latest/images/rc/rdi/rdi-setup-connectivity-arn.png)](/docs/latest/images/rc/rdi/rdi-setup-connectivity-arn.png)

## Create the source database and network resources

1.  Clone or download the [`rdi-cloud-automation` GitHub repository](https://github.com/redis/rdi-cloud-automation).
    
2.  In a terminal window, go to the `examples/aws-ec2-privatelink` directory.
    
3.  Run `terraform init` to initialize the Terraform working directory.
    
4.  Open the `example.tfvars` file and edit the following variables:
    
    *   `region`: The AWS region where your Redis Cloud database is deployed.
    *   `azs`: The availability zone IDs where your Redis Cloud database is deployed.
    *   `port`: The port number for the new PostgreSQL source database.
    *   `name`: A prefix for all of the created AWS resources.
    *   `redis_secrets_arn`: The source database credentials and certificates ARN from the Redis Cloud console.
    *   `redis_privatelink_arn`: The PrivateLink ARN from the Redis Cloud console.
5.  To view the configuration, run:
    
    ```sh
    terraform plan -var-file=example.tfvars
    ```
    
6.  To create the AWS resources, run:
    
    ```sh
    terraform apply -var-file=example.tfvars
    ```
    
    This example creates the following resources on your AWS account:
    
    *   An AWS KMS key with the required permissions for RDI
    *   A VPC with a public and private subnet and all necessary route tables
    *   An EC2 instance running a PostgreSQL database with a security group that allows access from Redis Cloud
    *   An AWS Secrets Manager secret for the PostgreSQL database credentials
    *   A Network Load Balancer (NLB), a listener, and target group to route traffic to the EC2 instance with AWS PrivateLink
    *   An AWS PrivateLink endpoint service for the PostgreSQL database

Creating the AWS resources will take some time. After the resources are created, you'll be able to view them in the AWS management console.

Save the following outputs:

*   `database`: The name of the PostgreSQL database.
*   `port`: The port number for the PostgreSQL database.
*   `secret_arn`: The ARN of the AWS Secrets Manager secret for the PostgreSQL database credentials.
*   `vpc_endpoint_service_name`: The name of the AWS PrivateLink endpoint service for the PostgreSQL database.

If you lose any outputs, run `terraform output` to view them again.

## Define source connection

1.  Return to the [Redis Cloud console](https://cloud.redis.io/). Go to your target database and select the **Data Pipeline** tab.
2.  Select **Define source database**. [![The define source database button.](/docs/latest/images/rc/rdi/rdi-define-source-database.png)](/docs/latest/images/rc/rdi/rdi-define-source-database.png)
3.  Enter a **Pipeline name**. [![The pipeline name and deployment CIDR fields.](/docs/latest/images/rc/rdi/rdi-define-pipeline-cidr.png)](/docs/latest/images/rc/rdi/rdi-define-pipeline-cidr.png)
4.  A **Deployment CIDR** is automatically generated for you. If, for any reason, a CIDR is not generated, enter a valid CIDR that does not conflict with your applications or other databases.
5.  Enter the terraform outputs in the following fields:
    *   **PrivateLink service name**: `vpc_endpoint_service_name`
    *   **Database**: `database`
    *   **Port**: `port`
    *   **Source database secrets ARN**: `secret_arn`
6.  Select **Start pipeline setup**. [![The start pipeline setup button.](/docs/latest/images/rc/rdi/rdi-start-pipeline-setup.png)](/docs/latest/images/rc/rdi/rdi-start-pipeline-setup.png)

At this point, Redis Cloud will provision the pipeline infrastructure that will allow you to define your data pipeline.

[![The Pipeline setup in progress screen.](/docs/latest/images/rc/rdi/rdi-pipeline-setup-in-progress.png)](/docs/latest/images/rc/rdi/rdi-pipeline-setup-in-progress.png)

Pipelines are provisioned in the background. You aren't allowed to make changes to your data pipeline or to your database during provisioning. This process will take about an hour, so you can close the window and come back later.

When your pipeline is provisioned, select **Complete setup**.

[![The complete setup button.](/docs/latest/images/rc/rdi/rdi-complete-setup.png)](/docs/latest/images/rc/rdi/rdi-complete-setup.png)

## Define data pipeline

After your pipeline is provisioned, you will be able to define your pipeline. You will select the database schemas, tables, and columns that you want to import and synchronize with your primary database.

See [Define data pipeline](../define/index.md#define-data-pipeline) for detailed steps on defining your data pipeline.

After you define your data pipeline, it will ingest data from the source database to your target Redis database. This process will take time, especially if you have a lot of records in your source database.

After this initial sync is complete, the data pipeline enters the _change streaming_ phase, where changes are captured as they happen. Changes in the source database are added to the target within a few seconds of capture. You can see this by connecting to your source database and making changes to the data, and then connecting to your target Redis database and verifying that the changes are reflected there.

You can view the status of your data pipeline in the **Data pipeline** tab of your database. See [View and edit data pipeline](../view-edit/index.md) to learn more.

## Delete sample resources

Warning:

Make sure to [delete your data pipeline](../view-edit/index.md#delete-pipeline) before deleting the sample resources.

To delete the sample resources created by Terraform, run:

```sh
terraform destroy -var-file=example.tfvars
```

## On this page
