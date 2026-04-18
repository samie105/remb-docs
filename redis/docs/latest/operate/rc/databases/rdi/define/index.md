---
title: "Define data pipeline"
source: "https://redis.io/docs/latest/operate/rc/databases/rdi/define/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/rdi/define/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:15.275Z"
content_hash: "ef0df3e631b6fb7d61de150d73c0b3275ec6aab3718e48dc911823b0b6d1b459"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        Define data pipeline","→","Define data pipeline"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        Define data pipeline","→","Define data pipeline"]
---
# Define data pipeline

Define the source connection and data pipeline.

Redis Cloud

After you have [prepared your source database](/docs/latest/operate/rc/databases/rdi/setup/) and connection information, you can set up your new pipeline. To do this:

1.  [Define the source connection](#define-source-connection) by entering all required source database information.
2.  [Define the data pipeline](#define-data-pipeline) by selecting the data that you want to sync from your source database to the target database.

## Define source connection

1.  In the [Redis Cloud console](https://cloud.redis.io/), go to your target database and select the **Data Pipeline** tab.
    
2.  Select **Define source database**. [![The define source database button.](/docs/latest/images/rc/rdi/rdi-define-source-database.png)](/docs/latest/images/rc/rdi/rdi-define-source-database.png)
    
3.  Enter a **Pipeline name**. [![The pipeline name and deployment CIDR fields.](/docs/latest/images/rc/rdi/rdi-define-pipeline-cidr.png)](/docs/latest/images/rc/rdi/rdi-define-pipeline-cidr.png)
    
4.  A **Deployment CIDR** is automatically generated for you. If, for any reason, a CIDR is not generated, enter a valid CIDR that does not conflict with your applications or other databases.
    
5.  In the **Source database connectivity** section, enter the **PrivateLink service name** of the [PrivateLink connected to your source database](/docs/latest/operate/rc/databases/rdi/setup/#set-up-connectivity). [![The Source database connectivity section, with database connection details and connectivity options.](/docs/latest/images/rc/rdi/rdi-define-connectivity.png)](/docs/latest/images/rc/rdi/rdi-define-connectivity.png)
    
6.  Enter your database details. This depends on your database type, and includes:
    
    *   **Port**: The database's port
    *   **Database**: Your database's name, or the root database _(PostgreSQL, Oracle only)_, or a comma-separated list of one or more databases you want to connect to _(SQL Server only)_
    *   **Database Server ID**: Unique ID for the replication client. Enter a number that is not used by any existing replication clients _(mySQL and mariaDB only)_
    *   **PDB**: Name of the Oracle pluggable database _(Oracle only)_
7.  Enter the ARN of your [database credentials secret](/docs/latest/operate/rc/databases/rdi/setup/#create-database-credentials-secrets) in the **Source database secrets ARN** field.
    
8.  If your database requires TLS, select **Use TLS**. Enter the ARN of your [CA certificate secret](/docs/latest/operate/rc/databases/rdi/setup/#create-database-credentials-secrets) in the **CA Cert Secret ARN** field. [![The Source database connectivity section, with Use TLS selected and the CA Cert Secret ARN field.](/docs/latest/images/rc/rdi/rdi-define-tls.png)](/docs/latest/images/rc/rdi/rdi-define-tls.png)
    
9.  If your database requires mTLS, select **Use mTLS**. Enter the ARN of your [Client certificate secret](/docs/latest/operate/rc/databases/rdi/setup/#create-database-credentials-secrets) in the **Client Certificate Secret ARN** field and the ARN of your [Client key secret](/docs/latest/operate/rc/databases/rdi/setup/#create-database-credentials-secrets) in the **Client Key Secret ARN** field. [![The Source database connectivity section, with Use TLS selected and the Client Certificate Secret ARN and Client Key Secret ARN fields.](/docs/latest/images/rc/rdi/rdi-define-mtls.png)](/docs/latest/images/rc/rdi/rdi-define-mtls.png)
    
10.  If your database requires mTLS with a client key passphrase, enter the ARN of your [Client key passphrase secret](/docs/latest/operate/rc/databases/rdi/setup/#create-database-credentials-secrets) in the **Please add a secret ARN for the password to use with the secret store** field.
     
11.  Select **Advanced properties** to configure additional optional properties for your pipeline. [![The advanced properties section.](/docs/latest/images/rc/rdi/rdi-advanced-properties.png) ](/docs/latest/images/rc/rdi/rdi-advanced-properties.png)You can add any [Debezium source property](https://debezium.io/documentation/reference/stable/connectors/) for your source database type in the **Collector source properties** section and any [Redis server Debezium sink property](https://debezium.io/documentation/reference/stable/operations/debezium-server.html#_redis_stream) in the **Collector sink properties** section.
     
12.  Select **Start pipeline setup**. [![The start pipeline setup button.](/docs/latest/images/rc/rdi/rdi-start-pipeline-setup.png)](/docs/latest/images/rc/rdi/rdi-start-pipeline-setup.png)
     
13.  Redis Cloud will attempt to connect to PrivateLink. If your PrivateLink does not allow automatic acceptance of incoming connections, accept the incoming connection on AWS PrivateLink to proceed. See [Accept or Reject PrivateLink connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests).
     
     If Redis Cloud can't find your PrivateLink connection, make sure that the PrivateLink service name is correct and that Redis Cloud is listed as an Allowed Principal for your VPC. See [Set up connectivity](/docs/latest/operate/rc/databases/rdi/setup/#set-up-connectivity) for more info.
     

At this point, Redis Cloud will provision the pipeline infrastructure that will allow you to define your data pipeline.

[![The Pipeline setup in progress screen.](/docs/latest/images/rc/rdi/rdi-pipeline-setup-in-progress.png)](/docs/latest/images/rc/rdi/rdi-pipeline-setup-in-progress.png)

Pipelines are provisioned in the background. You aren't allowed to make changes to your data pipeline or to your database during provisioning. This process will take about an hour, so you can close the window and come back later.

When your pipeline is provisioned, select **Complete setup**. You will then [define your data pipeline](#define-data-pipeline).

[![The complete setup button.](/docs/latest/images/rc/rdi/rdi-complete-setup.png)](/docs/latest/images/rc/rdi/rdi-complete-setup.png)

## Define data pipeline

After your pipeline is provisioned, you will be able to define your pipeline. You will select the database schemas, tables, and columns that you want to import and synchronize with your primary database.

### Configure a new pipeline

1.  In the [Redis Cloud console](https://cloud.redis.io/), go to your target database and select the **Data Pipeline** tab. If your pipeline is already provisioned, select **Complete setup** to go to the **Data modeling** section. [![The complete setup button.](/docs/latest/images/rc/rdi/rdi-complete-setup.png)](/docs/latest/images/rc/rdi/rdi-complete-setup.png)
    
2.  Select the Schema and Tables you want to migrate to the target database from the list. [![The data modeling section. ](/docs/latest/images/rc/rdi/rdi-select-source-data.png)](/docs/latest/images/rc/rdi/rdi-select-source-data.png)
    
    Select **Manage Columns** to choose which columns you want to import.
    
    [![The manage columns button.](/docs/latest/images/rc/rdi/rdi-manage-columns.png)](/docs/latest/images/rc/rdi/rdi-manage-columns.png)
    
    You can select any number of columns from a table.
    
    [![The manage columns screen, with a few columns selected from one table](/docs/latest/images/rc/rdi/rdi-select-columns.png)](/docs/latest/images/rc/rdi/rdi-select-columns.png)
    
    If any tables are missing a unique constraint, a warning will appear in the **Data modeling** section. Select **Manage columns** to select the columns that define a unique constraint for those tables.
    
    Select **Save** to save your column changes and go back to schema selection.
    
    [![The save button.](/docs/latest/images/rc/button-save.png)](/docs/latest/images/rc/button-save.png)
    
    Select **Add schema** to add more database schemas.
    
    [![The add schema button.](/docs/latest/images/rc/rdi/rdi-add-schema.png)](/docs/latest/images/rc/rdi/rdi-add-schema.png)
    
    Select **Delete** to delete a schema. You must have at least one schema to continue.
    
    [![The delete schema button.](/docs/latest/images/rc/rdi/rdi-delete-schema.png)](/docs/latest/images/rc/rdi/rdi-delete-schema.png)
    
    After you've selected the schemas and tables you want to sync, select **Continue**.
    
    [![The continue button.](/docs/latest/images/rc/rdi/rdi-continue-button.png)](/docs/latest/images/rc/rdi/rdi-continue-button.png)
3.  Select the Redis data type to write keys to the target. You can choose **Hash key** or **JSON key** if the target database supports JSON. [![The data modeling section, with Hash Key selected.](/docs/latest/images/rc/rdi/rdi-configure-new-pipeline.png)](/docs/latest/images/rc/rdi/rdi-configure-new-pipeline.png)
    
    You can also supply one or more [transformation job files](/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/) that specify how you want to transform the captured data before writing it to the target. Select **Upload jobs** to upload your job files.
    
    [![The transformation jobs section. Select Upload jobs to upload transformation jobs.](/docs/latest/images/rc/rdi/rdi-transformation-jobs.png)](/docs/latest/images/rc/rdi/rdi-transformation-jobs.png)
    
    When you upload job files, Redis Cloud will validate the job files to check for errors.
    
    Select **Continue**. [![The continue button.](/docs/latest/images/rc/rdi/rdi-continue-button.png)](/docs/latest/images/rc/rdi/rdi-continue-button.png)
    
4.  In the **Advanced properties** section, you can add any processor properties to control how the data is processed. See the [RDI configuration file reference](/docs/latest/integrate/redis-data-integration/reference/config-yaml-reference/#processors) for all available processor properties.
    
    [![The advanced properties section with processor properties.](/docs/latest/images/rc/rdi/rdi-processor-properties.png)](/docs/latest/images/rc/rdi/rdi-processor-properties.png)
    
    Select **Continue**. [![The continue button.](/docs/latest/images/rc/rdi/rdi-continue-button.png)](/docs/latest/images/rc/rdi/rdi-continue-button.png)
    
5.  Review the tables you selected in the **Review and deploy** section. If everything looks correct, select **Confirm & Deploy** to start ingesting data from your source database.
    
    [![The Confirm & Deploy button.](/docs/latest/images/rc/rdi/rdi-confirm-deploy.png)](/docs/latest/images/rc/rdi/rdi-confirm-deploy.png)

At this point, the data pipeline will ingest data from the source database to your target Redis database. This process will take time, especially if you have a lot of records in your source database.

After this initial sync is complete, the data pipeline enters the _change streaming_ phase, where changes are captured as they happen. Changes in the source database are added to the target within a few seconds of capture.

You can view the status of your data pipeline in the **Data pipeline** tab of your database. See [View and edit data pipeline](/docs/latest/operate/rc/databases/rdi/view-edit/) to learn more.

## On this page
