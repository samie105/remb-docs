---
title: "Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-mysql/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-mysql/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:40.679Z"
content_hash: "ff4d017ffcf24f25e09eab3ecbea9bda10bcc6481928c80798e7598c4ab3dbc1"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare AWS RDS and Aurora databases for RDI","→","Prepare AWS RDS and Aurora databases for RDI","→\n      \n        Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI","→","Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare AWS RDS and Aurora databases for RDI","→","Prepare AWS RDS and Aurora databases for RDI","→\n      \n        Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI","→","Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI"]
nav_prev: {"path": "../index.md", "title": "Prepare AWS RDS and Aurora databases for RDI"}
nav_next: {"path": "../aws-aur-pgsql/index.md", "title": "Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI"}
---

# Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI

Enable CDC features in your source databases

Follow the steps in the sections below to prepare an [AWS Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html) or [AWS RDS MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) database. database to work with RDI.

Select the steps for your database type.

 AWS Aurora MySQL  AWS RDS MySQL

## Add an Aurora reader node

RDI requires that your Aurora MySQL database has at least one replica or reader node.

To add a reader node to an existing database, select **Add reader** from the **Actions** menu of the database and [add a reader node](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.html).

You can also create one during database creation by selecting **Create an Aurora Replica or Reader node in a different AZ (recommended for scaled availability)** under **Availability & durability > Multi-AZ deployment**.

## Create and apply parameter group

RDI requires some changes to database parameters. On AWS Aurora, you change these parameters via a parameter group.

1.  In the [Relational Database Service (RDS) console](https://console.aws.amazon.com/rds/), navigate to **Parameter groups**.
    
    If you have no existing parameter group, [create a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html) with the following settings:
    
    Name
    
    Value
    
    **Parameter group name**
    
    Enter a suitable parameter group name, like `rdi-mysql`
    
    **Description**
    
    (Optional) Enter a description for the parameter group
    
    **Engine Type**
    
    Choose **Aurora MySQL**.
    
    **Parameter group family**
    
    Choose **aurora-mysql8.0**.
    
    **Type**
    
    Select **DB Parameter Group**.
    
    Select **Create** to create the parameter group.
    
    If you _do_ have an existing parameter group, select it and then either:
    
    *   Select **Edit** from **Parameter group actions** to [modify the parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html) with the settings shown in the table above.
    *   Select **Copy** from **Parameter group actions** to [copy the existing parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CopyingCluster.html) and then modify the copy with the settings shown in the table above.
2.  Ensure that the parameter group you have just created or modified is selected and then select **Edit**. Change the following parameters:
    
    Name
    
    Value
    
    `binlog_format`
    
    `ROW`
    
    `binlog_row_image`
    
    `FULL`
    
    `gtid_mode`
    
    `ON`
    
    `enforce_gtid_consistency`
    
    `ON`
    
    Select **Save Changes** to apply the changes to the parameter group.
    
3.  Go back to your target database on the RDS console, select **Modify** and then scroll down to **Additional Configuration**. Set the **DB Cluster Parameter Group** to the group you just created.
    
    Select **Save changes** to apply the parameter group to the new database.
    
4.  Reboot your database instance. See [Rebooting a DB instance within an Aurora cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-db-instance.html) for more information.
    

## Create Debezium user

The Debezium connector needs a user account to connect to MySQL. This user must have appropriate permissions on all databases where you want Debezium to capture changes.

1.  Connect to your database as an admin user and create a new user for the connector:
    
    ```sql
    CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';
    ```
    
    Replace `<username>` and `<password>` with a username and password for the new user.
    
    The `%` means that the user can connect from any client. If you want to restrict the user to connect only from the RDI host, replace `%` with the IP address of the RDI host.
    
2.  Grant the user the necessary permissions:
    
    ```sql
    GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    ```
    
    Replace `<username>` with the username of the Debezium user.
    
    You can also grant SELECT permissions for specific tables only. The other permissions are global and cannot be restricted to specific tables.
    
    ```sql
    GRANT RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    GRANT SELECT ON <database>.<table> TO '<username>'@'%';
    ```
    
3.  Finalize the user's permissions:
    
    ```sql
    FLUSH PRIVILEGES;
    ```
