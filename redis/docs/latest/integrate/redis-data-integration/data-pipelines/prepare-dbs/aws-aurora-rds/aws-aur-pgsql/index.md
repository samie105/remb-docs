---
title: "Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-pgsql/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/aws-aurora-rds/aws-aur-pgsql/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:57.739Z"
content_hash: "fba31522561ac64fe29cddee2bc1556f7cd49875e2b7ec7c0219a75e6bec7d03"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare AWS RDS and Aurora databases for RDI","→","Prepare AWS RDS and Aurora databases for RDI","→\n      \n        Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI","→","Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration","→\n      \n        Data pipelines","→","Data pipelines","→\n      \n        Prepare source databases","→","Prepare source databases","→\n      \n        Prepare AWS RDS and Aurora databases for RDI","→","Prepare AWS RDS and Aurora databases for RDI","→\n      \n        Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI","→","Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI"]
nav_prev: {"path": "redis/docs/latest/develop/reference/modules/modules-native-types/index.md", "title": "Modules API for native types"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/management/optimization/memory-optimization/index.md", "title": "Memory optimization"}
---

# Prepare AWS Aurora PostgreSQL/AWS RDS PostgreSQL for RDI

Prepare AWS Aurora PostgreSQL databases to work with RDI

Follow the steps in the sections below to prepare an [AWS Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html) or [AWS RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html) database to work with RDI.

## Create and apply parameter group

RDI requires some changes to database parameters. On AWS RDS and AWS Aurora, you change these parameters via a parameter group.

1.  In the [Relational Database Service (RDS) console](https://console.aws.amazon.com/rds/), navigate to **Parameter groups**.
    
    If you have no existing parameter group, [create a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html) with the following settings:
    
    Name
    
    Value
    
    **Parameter group name**
    
    Enter a suitable parameter group name, like `rdi-aurora-pg` or `rdi-rds-pg`
    
    **Description**
    
    (Optional) Enter a description for the parameter group
    
    **Engine Type**
    
    Choose **Aurora PostgreSQL** for Aurora PostgreSQL or **PostgreSQL** for AWS RDS PostgreSQL.
    
    **Parameter group family**
    
    Choose **aurora-postgresql15** for Aurora PostgreSQL or **postgresql13** for AWS RDS PostgreSQL.
    
    Select **Create** to create the parameter group.
    
    If you _do_ have an existing parameter group, select it and then either:
    
    *   Select **Edit** from **Parameter group actions** to [modify the parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html) with the settings shown in the table above.
    *   Select **Copy** from **Parameter group actions** to [copy the existing parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CopyingCluster.html) and then modify the copy with the settings shown in the table above.
2.  Ensure that the parameter group you have just created or modified is selected and then select **Edit**. Change the following parameter:
    
    Name
    
    Value
    
    `rds.logical_replication`
    
    `1`
    
    Select **Save Changes** to apply the changes to the parameter group.
    
3.  Go back to your database on the RDS console, select **Modify** and then scroll down to **Additional Configuration**. Set the **DB Cluster Parameter Group** to the group you just created.
    
    Select **Save changes** to apply the parameter group to your database.
    
4.  Reboot your database instance. See [Rebooting a DB instance within an Aurora cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-db-instance.html) or [Rebooting a DB instance (RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html) for more information.
    

## Create Debezium user

The Debezium connector needs a user account to connect to PostgreSQL. This user must have appropriate permissions on all databases where you want Debezium to capture changes.

1.  Connect to PostgreSQL as the `postgres` user and create a new user for the connector:
    
    ```sql
    CREATE ROLE <username> WITH LOGIN PASSWORD '<password>' VALID UNTIL 'infinity';
    ```
    
    Replace `<username>` and `<password>` with a username and password for the new user.
    
2.  Grant the user the necessary replication permissions:
    
    ```sql
    GRANT rds_replication TO <username>;
    ```
    
    Replace `<username>` with the username of the Debezium user.
    
3.  Connect to your database as the `postgres` user and grant the new user access to one or more schemas in the database:
    
    ```sql
    GRANT SELECT ON ALL TABLES IN SCHEMA <schema> TO <username>;
    ```
    
    Replace `<username>` with the username of the Debezium user and `<schema>` with the schema name.
    
4.  Connect to your database as the `postgres` user and allow the Debezium user to connect to the database:
    
    ```sql
    GRANT CONNECT ON DATABASE <database> TO <username>;
    ```
    
    Replace `<database>` with the name of the database and `<username>` with the username of the Debezium user.
    
5.  Connect to your database as the `postgres` user and grant the new user usage on the schema:
    
    ```sql
    GRANT USAGE ON SCHEMA <schema> TO <username>;
    ```
    
    Replace `<schema>` with the schema name and `<username>` with the username of the Debezium user.">
    
6.  Connect to your database as the `postgres` user and grant the new user the necessary privileges for the future:
    
    ```sql
    ALTER DEFAULT PRIVILEGES IN SCHEMA <schema>
        GRANT SELECT ON TABLES TO <username>;
    ```
    
    Replace `<schema>` with the schema name and `<username>` with the username of the Debezium user.
    
7.  Connect to your database as the `postgres` user and create a publication for the database:
    
    ```sql
    CREATE PUBLICATION dbz_publication FOR ALL TABLES;
    ```
    

## On this page


