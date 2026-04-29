---
title: "Install on AWS EC2"
source: "https://redis.io/docs/latest/operate/redisinsight/install/install-on-aws/"
canonical_url: "https://redis.io/docs/latest/operate/redisinsight/install/install-on-aws/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:53.440Z"
content_hash: "66e1b3632227676c4fe28457b4e0a1f18eac8314b0a9d3fa071cdc3c5ad919af"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Install Redis Insight","→","Install Redis Insight","→\n      \n        Install on AWS EC2","→","Install on AWS EC2"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Install Redis Insight","→","Install Redis Insight","→\n      \n        Install on AWS EC2","→","Install on AWS EC2"]
nav_prev: {"path": "../index.md", "title": "Install Redis Insight"}
nav_next: {"path": "../install-on-desktop/index.md", "title": "Install on desktop"}
---

# Install on AWS EC2

How to install Redis Insight on AWS EC2

Redis Insight

This tutorial shows you how to install Redis Insight on an AWS EC2 instance and manage ElastiCache Redis instances using Redis Insight. To complete this tutorial you must have access to the AWS Console and permissions to launch EC2 instances.

## Step 1: Launch EC2 Instance

Next, launch an EC2 instance.

1.  Navigate to EC2 under AWS Console.
2.  Click Launch Instance.
3.  Choose 64-bit Amazon Linux AMI.
4.  Choose at least a t2.medium instance. The size of the instance depends on the memory used by your ElastiCache instance that you want to analyze.
5.  Under Configure Instance:
    *   Choose the VPC that has your ElastiCache instances.
    *   Choose a subnet that has network access to your ElastiCache instances.
    *   Ensure that your EC2 instance has a public IP Address.
    *   Assign the IAM role that you created in Step 1.
6.  Under the storage section, allocate at least 100 GiB storage.
7.  Under security group, ensure that:
    *   Incoming traffic is allowed on port 5540
    *   Incoming traffic is allowed on port 22 only during installation
8.  Review and launch the ec2 instance.

## Step 2: Verify permissions and connectivity

Next, verify that the EC2 instance has the required IAM permissions and can connect to ElastiCache Redis instances.

1.  SSH into the newly launched EC2 instance.
2.  Open a command prompt.
3.  Run the command `aws s3 ls`. This should list all S3 buckets.
    1.  If the `aws` command cannot be found, make sure your EC2 instance is based of Amazon Linux.
4.  Next, find the hostname of the ElastiCache instance you want to analyze and run the command `echo info | nc <redis host> 6379`.
5.  If you see some details about the ElastiCache Redis instance, you can proceed to the next step.
6.  If you cannot connect to redis, you should review your VPC, subnet, and security group settings.

## Step 3: Install Docker on EC2

Next, install Docker on the EC2 instance. Run the following commands:

1.  `sudo yum update -y`
2.  `sudo yum install -y docker`
3.  `sudo service docker start`
4.  `sudo usermod -a -G docker ec2-user`
5.  Log out and log back in again to pick up the new docker group permissions.
6.  To verify, run `docker ps`. You should see some output without having to run `sudo`.

## Step 4: Run Redis Insight in the Docker container

Finally, install Redis Insight using one of the options described below.

1.  If you do not want to persist your Redis Insight data:

```bash
docker run -d --name redisinsight -p 5540:5540 redis/redisinsight:latest
```

2.  If you want to persist your Redis Insight data, first attach the Docker volume to the `/data` path and then run the following command:

```bash
docker run -d --name redisinsight -p 5540:5540 redis/redisinsight:latest -v redisinsight:/data
```

If the previous command returns a permission error, ensure that the user with `ID = 1000` has the necessary permission to access the volume provided (`redisinsight` in the command above).

Find the IP Address of your EC2 instances and launch your browser at `http://<EC2 IP Address>:5540`. Accept the EULA and start using Redis Insight.

Redis Insight also provides a health check endpoint at `http://<EC2 IP Address>:5540/api/health/` to monitor the health of the running container.

## Summary

In this guide, we installed Redis Insight on an AWS EC2 instance running Docker. As a next step, you should add an ElastiCache Redis Instance and then run the memory analysis.

## On this page
