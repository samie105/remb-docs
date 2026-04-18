---
title: "Prepare source database"
source: "https://redis.io/docs/latest/operate/rc/databases/rdi/setup/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/rdi/setup/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:02.183Z"
content_hash: "c29d2409120d3019b3c2172c82b4f84a4f86fa252c432fb6219e057b8806e39f"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        Prepare source database","→","Prepare source database"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        Prepare source database","→","Prepare source database"]
nav_prev: {"path": "redis/docs/latest/operate/rc/databases/rdi/quick-start/index.md", "title": "RDI on Redis Cloud quick start"}
nav_next: {"path": "redis/docs/latest/operate/rc/databases/rdi/view-edit/index.md", "title": "View and edit data pipeline"}
---

# Prepare source database

Prepare your source database, network setup, and database credentials for Data integration.

Redis Cloud

## Create new data pipeline

1.  In the [Redis Cloud console](https://cloud.redis.io/), go to your target database and select the **Data Pipeline** tab.
    
2.  Select **Create pipeline**. [![The create pipeline button.](/docs/latest/images/rc/rdi/rdi-create-data-pipeline.png)](/docs/latest/images/rc/rdi/rdi-create-data-pipeline.png)
    
3.  Select your source database type. The following database types are supported:
    
    *   MySQL
    *   mariaDB
    *   Oracle
    *   SQL Server
    *   PostgreSQL [![The select source database type list.](/docs/latest/images/rc/rdi/rdi-select-source-db.png)](/docs/latest/images/rc/rdi/rdi-select-source-db.png)
4.  If you know the size of your source database, enter it into the **Source dataset size** field. [![Enter the amount of source data you plan to ingest.](/docs/latest/images/rc/rdi/rdi-source-dataset-size.png)](/docs/latest/images/rc/rdi/rdi-source-dataset-size.png)
    
5.  Under **Setup connectivity**, save the provided ARN and extract the AWS account ID for the account associated with your Redis Cloud cluster from it.
    
    [![The select source database type list.](/docs/latest/images/rc/rdi/rdi-setup-connectivity-arn.png)](/docs/latest/images/rc/rdi/rdi-setup-connectivity-arn.png)
    
    The AWS account ID is the string of numbers after `arn:aws:iam::` in the ARN. For example, if the ARN is `arn:aws:iam::123456789012:role/redis-data-pipeline`, the AWS account ID is `123456789012`.
    

## Prepare source database

Before using the pipeline, you must first prepare your source database to use the Debezium connector for change data capture (CDC). See [Prerequisites](/docs/latest/operate/rc/databases/rdi/#prerequisites) to find a list of supported source databases and database versions.

See [Prepare source databases](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/) to find steps for your database type:

*   Hosted on an AWS EC2 instance:
    *   [MySQL and mariaDB](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/my-sql-mariadb/)
    *   [Oracle](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/oracle/)
    *   [SQL Server](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/sql-server/)
    *   [PostgreSQL](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/postgresql/)
*   Hosted on AWS RDS or AWS Aurora:
    *   [AWS Aurora PostgreSQL and AWS RDS PostgreSQL](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-pgsql/)
    *   [AWS Aurora MySQL and AWS RDS MySQL](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-mysql/)
    *   [AWS RDS SQL Server](/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-rds-sqlserver/)

See the [RDI architecture overview](/docs/latest/integrate/redis-data-integration/architecture/#overview) for more information about CDC.

## Set up connectivity

To ensure that you can connect your Redis Cloud database to the source database, you need to set up an endpoint service through AWS PrivateLink.

The following diagrams show the network setup for the different database setups:

*   Database hosted on an AWS EC2 instance:
    
    [![The network setup for a database hosted on an AWS EC2 instance.](/docs/latest/images/rc/rdi/rdi-setup-diagram-ec2.png)](/docs/latest/images/rc/rdi/rdi-setup-diagram-ec2.png)
*   Database hosted on AWS RDS or AWS Aurora:
    
    [![The network setup for a database hosted on AWS RDS or AWS Aurora.](/docs/latest/images/rc/rdi/rdi-setup-diagram-aurora.png)](/docs/latest/images/rc/rdi/rdi-setup-diagram-aurora.png)

Select the steps for your database setup.

 EC2 instance  AWS RDS or Aurora

To set up PrivateLink for a database hosted on an EC2 instance:

1.  [Create a network load balancer](#create-network-load-balancer-ec2) that will route incoming HTTP requests to your database.
2.  [Create an endpoint service](#create-endpoint-service-ec2) through AWS PrivateLink.

### Create network load balancer

In the [AWS Management Console](https://console.aws.amazon.com/), use the **Services** menu to locate and select **Compute** > **EC2**. [Create a network load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html#configure-load-balancer) with the following settings:

1.  In **Basic configuration**:
    
    *   **Scheme**: Select **Internal**.
    *   **Load balancer IP address type**: Select **IPv4**.
2.  In **Network mapping**, select the VPC and availability zone associated with your source database.
    
3.  In **Security groups**, select the security group associated with your source database, or another security group that allows traffic from PrivateLink and allows traffic to the database.
    
4.  In **Listeners and routing**:
    
    1.  Select **Create target group** to [create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html) with the following settings:
        1.  In **Specify group details**:
            *   **Target type**: Select **Instances**.
            *   **Protocol : Port**: Select **TCP**, and then enter the port number where your database is exposed.
            *   The **IP address type** and **VPC** should be selected already and match the VPC you selected earlier.
        2.  In **Register targets**, select the EC2 instance that runs your source database, enter the port, and select **Include as pending below**. Then, select **Create target group** to create your target group. Return to **Listeners and routing** in the Network Load Balancer setup.
    2.  Set the following **Listener** properties:
        *   **Protocol**: Select **TCP**.
        *   **Port**: Enter your source database's port.
        *   **Default action**: Select the target group you created in the previous step.
5.  Review the network load balancer settings, and then select **Create load balancer** to continue.
    
6.  After the network load balancer is active, select **Security**.
    
    If you selected the same security group as your source database, you must not enforce security group rules on PrivateLink traffic. Select **Edit** and then deselect **Enforce inbound rules on PrivateLink traffic**, and then select **Save changes**.
    
7.  Select the security group ID to open the Security group settings.
    
8.  Select **Edit inbound rules**, then **Add rule** to add a rule with the following settings:
    
    *   **Type**: Select **HTTP**.
    *   **Source**: Select **Anywhere - IPv4**. Select **Save rules** to save your changes.
9.  Select **Actions** > **Edit Load Balancer Attributes**.
    
    *   Under **Load balancer targets selection policy** select **Enable cross-zone load balancing**. Click the **Save Changes** button.

### Create endpoint service

In the [AWS Management Console](https://console.aws.amazon.com/), use the **Services** menu to locate and select **Networking & Content Delivery** > **VPC**. There, select **PrivateLink and Lattice** > **Endpoint services**. [Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html) with the following settings:

1.  In **Available load balancers**, select the [network load balancer](#create-network-load-balancer-ec2) you created.
2.  In **Additional settings**, choose the following settings:
    *   **Require acceptance for endpoint**: Select **Acceptance required**.
    *   **Supported IP address types**: Select **IPv4**.
3.  Select **Create** to create the endpoint service.

After you create the endpoint service, you need to add Redis Cloud as an Allowed Principal on your [endpoint service VPC permissions](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#add-remove-permissions).

1.  In the Redis Cloud Console, copy the Amazon Resource Name (ARN) provided in the **Setup connectivity** section.
2.  Return to the endpoint service list on the [Amazon VPC console](https://console.aws.amazon.com/vpc/). Select the endpoint service you just created.
3.  Navigate to **Allow principals** tab.
4.  Add the Redis Cloud ARN you copied and choose **Allow principals**.
5.  Save the service name for later.

For more details on AWS PrivateLink, see [Share your services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html).

## Share source database credentials

You need to share your source database credentials and certificates in an Amazon secret with Redis Cloud so that the pipeline can connect to your database.

To do this, you need to:

1.  [Create an encryption key](#create-encryption-key) using AWS Key Management Service with the right permissions.
2.  [Create secrets](#create-database-credentials-secrets) containing the source database credentials encrypted using that key.

### Create encryption key

In the [AWS Management Console](https://console.aws.amazon.com/), use the **Services** menu to locate and select **Security, Identity, and Compliance** > **Key Management Service**. [Create an encryption key](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html) with the following settings:

1.  In **Step 1 - Configure key**:
    *   **Key type**: Select **Symmetric**.
    *   **Key usage**: Select **Encrypt and decrypt**.
    *   Under **Advanced options**, set the following:
        *   **Key material origin**: Select **KMS - recommended**.
        *   **Regionality**: Select **Single-Region key**.
2.  In **Step 2 - Add labels**, add an alias and description for the key.
3.  In **Step 3 - Define key administrative permissions**, under **Key deletion**, select **Allow key administrators to delete this key**.
4.  In **Step 4 - Define key usage permissions**, under **Other AWS accounts**, select **Add another AWS account**. Enter the AWS account ID for the Redis Cloud cluster that you saved earlier.

Review the key policy and key settings, and then select **Finish** to create the key.

### Create database credentials secrets

To let Redis Cloud access your source database, you need to create AWS secrets for the source database's credentials and certificates.

The required secrets depend on your source database's security configuration. The following table shows the required secrets for each configuration:

Security configuration

Required secrets

Username and password only

*   Credentials secret (username and password for the RDI pipeline user)

TLS connection

*   Credentials secret (username and password for the RDI pipeline user)
*   CA Certificate secret (server certificate)

mTLS connection

*   Credentials secret (username and password for the RDI pipeline user)
*   CA Certificate secret (server certificate)
*   Client certificate secret
*   Client key secret

mTLS connection with client key passphrase

*   Credentials secret (username and password for the RDI pipeline user)
*   CA Certificate secret (server certificate)
*   Client certificate secret
*   Client key secret
*   Client key passphrase secret

Note:

When creating secrets for TLS or mTLS, ensure that all certificates and keys are in `PEM` format. The only exception to this is that for PostgreSQL, the private key `SOURCE_DB_KEY` secret must be in `DER` format. If you have a key in `PEM` format, you must convert it to `DER` before creating the `SOURCE_DB_KEY` secret using the command:

```bash
openssl pkcs8 -topk8 -inform PEM -outform DER \
    -in /path/to/myclient.pem \
    -out /path/to/myclient.pk8 -nocrypt
```

This command assumes that the private key is not encrypted. See the [`openssl` documentation](https://docs.openssl.org/master/) to learn how to convert an encrypted private key.

Select a tab to learn how to create the required secret.

 Credentials secret  CA Certificate secret  Client certificate secret  Client key secret  Client key passphrase secret

In the [AWS Management Console](https://console.aws.amazon.com/), use the **Services** menu to locate and select **Security, Identity, and Compliance** > **Secrets Manager**. [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) of type **Other type of secret** with the following settings:

*   **Key/value pairs**: Enter the following key/value pairs.
    
    *   `username`: Database username for the RDI pipeline user
    *   `password`: Database password for the RDI pipeline user
    
*   **Encryption key**: Select the [encryption key](#create-encryption-key) you created earlier.
    
*   **Resource permissions**: Add the following permissions to your secret to allow the Redis data pipeline to access your secret. Replace `<AWS ACCOUNT ID>` with the AWS account ID for the Redis Cloud cluster that you saved earlier.
    

```json
{
    "Version" : "2012-10-17",
    "Statement" : [ {
        "Sid" : "RedisDataIntegrationRoleAccess",
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : [ "secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret" ],
        "Resource" : "*",
        "Condition" : {
            "StringLike" : {
                "aws:PrincipalArn" : "arn:aws:iam::<AWS ACCOUNT ID>:role/redis-data-pipeline-secrets-role"
            }
        }
    } ]
}
```

After you store this secret, you can view and copy the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources) of your secret on the secret details page. Save the secret ARN to use when you [define your source database](/docs/latest/operate/rc/databases/rdi/define/).

## Next steps

After you have set up your source database and prepared connectivity and credentials, select **Define source database** to [define your source connection and data pipeline](/docs/latest/operate/rc/databases/rdi/define/).

[![The define source database button.](/docs/latest/images/rc/rdi/rdi-define-source-database.png)](/docs/latest/images/rc/rdi/rdi-define-source-database.png)

## On this page
