---
title: "Create IAM resources for AWS cloud accounts"
source: "https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/iam-resources/"
canonical_url: "https://redis.io/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/iam-resources/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:16.283Z"
content_hash: "f5c07e883fa8e5f7d94d069afe75ad78441f9901dfd70e11bc39a0e162fb016e"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage subscriptions","→","Manage subscriptions","→\n      \n        Redis Cloud Bring your own Cloud","→","Redis Cloud Bring your own Cloud","→\n      \n        Create IAM resources for AWS cloud accounts","→","Create IAM resources for AWS cloud accounts"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Manage subscriptions","→","Manage subscriptions","→\n      \n        Redis Cloud Bring your own Cloud","→","Redis Cloud Bring your own Cloud","→\n      \n        Create IAM resources for AWS cloud accounts","→","Create IAM resources for AWS cloud accounts"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/management/optimization/cpu-profiling/index.md", "title": "Redis CPU profiling"}
nav_next: {"path": "redis/docs/latest/develop/get-started/data-store/index.md", "title": "Redis as an in-memory data structure store quick start guide"}
---

# Create IAM resources for AWS cloud accounts

Redis Cloud

For Redis Cloud Bring your Own Cloud (BYOC) on Amazon Web Services (AWS), we manage the supporting infrastructure for you in dedicated AWS accounts.

You can manage this infrastructure with your own AWS accounts.

You'll want these accounts to be separate from any AWS application accounts and you'll need to create dedicated [identity and access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) resources to allow us to manage the infrastructure.

In the new AWS account, you need to create:

*   An **instance role**
*   A user with an **access key**
*   A role that grants **AWS console access**

Save the access key in a secure location so that you can enter it when you [register the cloud account](/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/cloud-account-settings/) with your Redis Cloud subscription.

Warning:

We use the provided credentials to configure your AWS environment and provision required resources.

You **must not** change the configurations of provisioned resources or stop or terminate provisioned instances. If you do, your databases will be inaccessible and Redis will not be able to ensure database stability. See [Avoid service disruption](/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/cloud-account-settings/#avoid-service-disruption) for more details.

For help creating an AWS user, see the [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

You can use one of the following tools to create IAM resources:

*   [CloudFormation](/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/iam-resources/cloudformation/)
*   [Terraform](/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/iam-resources/terraform/)
*   The [AWS Console](/docs/latest/operate/rc/subscriptions/bring-your-own-cloud/iam-resources/aws-console/)
