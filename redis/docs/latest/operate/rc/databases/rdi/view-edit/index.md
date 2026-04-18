---
title: "View and edit data pipeline"
source: "https://redis.io/docs/latest/operate/rc/databases/rdi/view-edit/"
canonical_url: "https://redis.io/docs/latest/operate/rc/databases/rdi/view-edit/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:16.476Z"
content_hash: "25bb7ee24fdfac78e57f6daa7650f287a4f030c59c6ceda5b8f32b69b93a8747"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        View and edit data pipeline","→","View and edit data pipeline"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage databases","→","Manage databases","→\n      \n        Data Integration","→","Data Integration","→\n      \n        View and edit data pipeline","→","View and edit data pipeline"]
nav_prev: {"path": "redis/docs/latest/develop/whats-new/8-2/index.md", "title": "Redis 8.2"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v1.14.0/index.md", "title": "RedisInsight v1.14, may 2023"}
---

# View and edit data pipeline

Observe and change your data pipeline.

Redis Cloud

Use the **Data pipeline** tab in your database to view and edit your data pipeline.

The **Data pipeline** tab gives an overview of your data pipeline and lets you view your data stream metrics.

[![The select source database type list.](/docs/latest/images/rc/rdi/rdi-status-metrics-tables.png)](/docs/latest/images/rc/rdi/rdi-status-metrics-tables.png)

The **Status** table shows statistics for the whole data pipeline:

*   **Status**: The status of the data pipeline. Possible statuses include:
    
    Status
    
    Description
    
    **Initial Sync**
    
    The data pipeline is ingesting all records from the source database into the target database.
    
    **Streaming**
    
    The data pipeline is capturing new changes from the source database as they happen. Changes in the source database are added to the target database within a few seconds.
    
    **Stopped**
    
    The data pipeline has been [stopped](#stop-and-restart-data-pipeline).
    
    **Error**
    
    There is an error in the data pipeline. [Reset the pipeline](#reset-data-pipeline) and contact support if the issue persists.
    
*   **Total ingested**: Total number of records ingested from the source database.
*   **Total inserted**: Total number of records inserted into the target database.
*   **Total filtered**: Total number of records filtered from being inserted into the target database.
*   **Total rejected**: Total number of records that could not be parsed or inserted into the target database.

The **Data stream metrics** table shows the following metrics for each data stream:

Metric

Description

**Name**

Name of the data stream. Each stream corresponds to a table from the source database.

**Total**

Total number of records that arrived from the source table.

**Pending**

Number of records from the source table that are waiting to be processed.

**Inserted**

Number of new records from the source table that have been written to the target database.

**Updated**

Number of updated records from the source table that have been updated in the target database.

**Deleted**

Number of deleted records from the source table that have been deleted in the target database.

**Filtered**

Number of records from the source table that were filtered from being inserted into the target database.

**Rejected**

Number of records from the source table that could not be parsed or inserted into the target database.

## Edit data pipeline

To change the data you want to ingest from the data pipeline:

1.  From the **Data pipeline** tab, select **Edit**.
    
    [![The edit pipeline button.](/docs/latest/images/rc/rdi/rdi-edit-button.png)](/docs/latest/images/rc/rdi/rdi-edit-button.png)
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
3.  Select the Redis data type to write keys to the target. You can choose **Hash** or **JSON** if the target database supports JSON. [![The pipeline definition screen.](/docs/latest/images/rc/rdi/rdi-configure-new-pipeline.png)](/docs/latest/images/rc/rdi/rdi-configure-new-pipeline.png)
    
    You can also supply one or more [transformation job files](/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/) that specify how you want to transform the captured data before writing it to the target. Select **Upload jobs** to upload your job files.
    
    [![The transformation jobs section. Select Upload jobs to upload transformation jobs.](/docs/latest/images/rc/rdi/rdi-transformation-jobs.png)](/docs/latest/images/rc/rdi/rdi-transformation-jobs.png)
    
    When you upload job files, Redis Cloud will validate the job files to check for errors.
    
    Select **Continue**. [![The continue button.](/docs/latest/images/rc/rdi/rdi-continue-button.png)](/docs/latest/images/rc/rdi/rdi-continue-button.png)
    
4.  In the **Advanced properties** section, you can add any processor properties to control how the data is processed. See the [RDI configuration file reference](/docs/latest/integrate/redis-data-integration/reference/config-yaml-reference/#processors) for all available processor properties.
    
    [![The advanced properties section with processor properties.](/docs/latest/images/rc/rdi/rdi-processor-properties.png)](/docs/latest/images/rc/rdi/rdi-processor-properties.png)
    
    Select **Continue**. [![The continue button.](/docs/latest/images/rc/rdi/rdi-continue-button.png)](/docs/latest/images/rc/rdi/rdi-continue-button.png)
    
5.  Review the tables you selected in and select how you want to update the data pipeline:
    
    [![The Select update preferences section.](/docs/latest/images/rc/rdi/rdi-update-preferences.png)](/docs/latest/images/rc/rdi/rdi-update-preferences.png)
    *   **Apply to new data changes only**: The data pipeline will only synchronize new updates to the schema and tables selected. The data pipeline will not ingest any data from new schemas or tables that are selected.
    *   **Reset pipeline (re-process all data)**: The data pipeline will re-ingest all of the selected data.
    *   **Flush cached data and reset pipeline**: The data pipeline will flush the target Redis database, and then re-ingest all of the selected data from the source database.
6.  Select **Apply changes**.
    
    [![The apply changes button.](/docs/latest/images/rc/rdi/rdi-apply-changes.png)](/docs/latest/images/rc/rdi/rdi-apply-changes.png)

At this point, the data pipeline will apply the changes. If you selected **Reset pipeline** or **Flush cached data and reset pipeline**, the data pipeline will ingest data from the source database to the target database. After this initial sync is complete, the data pipeline enters the _change streaming_ phase, where changes are captured as they happen.

If you selected **Apply to new data changes only**, the data pipeline will enter the _change streaming_ phase without ingesting data.

## View metrics endpoints

You can use [Prometheus and Grafana](/docs/latest/integrate/prometheus-with-redis-cloud/) to track and display metrics for the data pipeline.

To view the metrics endpoints for the source collector and pipeline processor, go to the **Data pipeline** tab and select **More actions**, and then **Show metrics**. You can add these endpoints as Prometheus targets to start tracking your RDI metrics.

Prometheus endpoints are exposed on Redis Cloud's internal network. To access this network, enable [VPC peering](/docs/latest/operate/rc/security/vpc-peering/) or [AWS Transit Gateway](/docs/latest/operate/rc/security/aws-transit-gateway/). See [Prometheus and Grafana with Redis Cloud](/docs/latest/integrate/prometheus-with-redis-cloud/) for more information.

For more information about available RDI metrics, see [Observability](/docs/latest/integrate/redis-data-integration/observability/).

## Reset data pipeline

Resetting the data pipeline creates a new baseline snapshot from the current state of your source database, and re-processes the data from the source database to the target Redis database. You may want to reset the pipeline if the source and target databases were disconnected or you made large changes to the data pipeline.

To reset the data pipeline and restart the ingest process:

1.  From the **Data pipeline** tab, select **More actions**, and then **Reset pipeline**.
    
2.  If you want to flush the database, check **Flush target database**.
    
3.  Select **Reset data pipeline**.
    

At this point, the data pipeline will re-ingest data from the source database to your target Redis database.

## Stop and restart data pipeline

To stop the data pipeline from synchronizing new data:

1.  From the **Data pipeline** tab, select **More actions**, and then **Stop pipeline**.
    
2.  Select **Stop data pipeline** to confirm.
    

Stopping the data pipeline will suspend data processing. To restart the pipeline from the **Data pipeline** tab, select **More actions**, and then **Start pipeline**.

## Delete pipeline

To delete the data pipeline:

1.  From the **Data pipeline** tab, select **More actions**, and then **Delete pipeline**.
    
2.  Select **Delete data pipeline** to confirm.
    

Deleted data pipelines cannot be recovered.

## On this page


