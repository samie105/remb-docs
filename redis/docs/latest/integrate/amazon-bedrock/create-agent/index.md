---
title: "Create a Bedrock agent"
source: "https://redis.io/docs/latest/integrate/amazon-bedrock/create-agent/"
canonical_url: "https://redis.io/docs/latest/integrate/amazon-bedrock/create-agent/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:22.404Z"
content_hash: "22a35ca6e1ed561a1d14b7056a836ea02e735ebb9a66b0511deeb08d16bc31f8"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock","→\n      \n        Create a Bedrock agent","→","Create a Bedrock agent"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock","→\n      \n        Create a Bedrock agent","→","Create a Bedrock agent"]
nav_prev: {"path": "redis/docs/latest/operate/rc/databases/rdi/define/index.md", "title": "Define data pipeline"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/deprecated/development/index.md", "title": "Developer notes"}
---

# Create a Bedrock agent

Shows how to set up your Agent in Amazon Bedrock.

After you have [created a knowledge base](/docs/latest/integrate/amazon-bedrock/create-knowledge-base/), you can use it to create an agent on Amazon Bedrock.

Before you begin this guide, you will need:

*   An [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) with [permissions for the Bedrock agent](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html).
    
*   A [Bedrock knowledge base](/docs/latest/integrate/amazon-bedrock/create-knowledge-base/) connected to a [Redis Cloud vector database](/docs/latest/integrate/amazon-bedrock/set-up-redis/).
    

## Create an agent

1.  Sign in to the [AWS console](https://console.aws.amazon.com/).
    
2.  Use the **Services** menu to locate and select **Machine Learning** > **Amazon Bedrock**. This takes you to the Amazon Bedrock admin panel.
    
3.  Select **Agents** > **Create Agent** to create your knowledge base.
    
    [![The Create Agent button.](/docs/latest/images/rc/bedrock-aws-button-create-agent.png)](/docs/latest/images/rc/bedrock-aws-button-create-agent.png)
4.  In the **Agent name** section, enter a name and description for your agent.
    
5.  Select whether or not you want the agent to be able to ask for additional information in the **User input** section.
    
6.  Select the IAM role for the Bedrock agent in the **IAM Permissions** section.
    
7.  Choose how long you want your idle session timeout to be in the **Idle session timeout** section. Select **Next** to continue.
    
8.  In the **Model details** section, choose which model you want to use and enter the instructions for your agent. Select **Next** to continue.
    
9.  In the **Action groups** section, you may specify any tasks you would like the agent to perform. Select **Next** to continue.
    
10.  Select the [knowledge base](#create-a-knowledge-base) you created and summarize the information in the knowledge base in the **Knowledge base instructions for Agent** form. Select **Add another knowledge base** if you would like to add multiple knowledge bases.
     
     [![The Add another knowledge base button.](/docs/latest/images/rc/bedrock-aws-button-add-knowledge-base.png)](/docs/latest/images/rc/bedrock-aws-button-add-knowledge-base.png)
     
     Select **Next** to continue.
     
11.  Review your agent before you create it. Select **Create Agent** to finish creation.
     
     [![The Create Agent button.](/docs/latest/images/rc/bedrock-aws-button-create-agent.png)](/docs/latest/images/rc/bedrock-aws-button-create-agent.png)

Amazon Bedrock will create your agent and link it to your knowledge base. This will take some time.

Your agent will have a status of **Ready** when it is ready to be tested.

[![A Bedrock agent with a Ready status.](/docs/latest/images/rc/bedrock-aws-status-agent-ready.png)](/docs/latest/images/rc/bedrock-aws-status-agent-ready.png)

Select the name of your agent to view the versions and draft aliases of your agent. You can also test your agent by entering prompts in the **Enter your message here** field.

## On this page


