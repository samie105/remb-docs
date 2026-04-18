---
title: "Amazon Bedrock"
source: "https://redis.io/docs/latest/integrate/amazon-bedrock/"
canonical_url: "https://redis.io/docs/latest/integrate/amazon-bedrock/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:53.535Z"
content_hash: "b930bd1620fbeafa43fcf3aee043a9ca8bd9779e04364fe743ec103df5ba4140"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Amazon Bedrock","→","Amazon Bedrock"]
nav_prev: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-15-july2025/index.md", "title": "Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes"}
nav_next: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-8-2-releases/7-8-2-6-nov24/index.md", "title": "Redis Enterprise for Kubernetes 7.8.2-6 (Nov 2024) release notes"}
---

# Amazon Bedrock

Shows how to use your Redis database with Amazon Bedrock to customize foundational models.

[Amazon Bedrock](https://aws.amazon.com/bedrock/) streamlines GenAI deployment by offering foundational models (FMs) as a unified API, eliminating complex infrastructure management. It lets you create AI-powered [Agents](https://aws.amazon.com/bedrock/agents/) that execute complex tasks. Through [Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) within Amazon Bedrock, you can seamlessly tether FMs to your proprietary data sources using retrieval-augmented generation (RAG). This direct integration amplifies the FM's intelligence based on your organization's resources.

Amazon Bedrock lets you choose Redis Cloud as the [vector database](https://redis.io/solutions/vector-search/) for your agent's Knowledge Base. Once Redis Cloud is integrated with Amazon Bedrock, it automatically reads text documents from your Amazon Simple Storage Service (S3) buckets. This process lets the large language model (LLM) pinpoint and extract pertinent context in response to user queries, ensuring your AI agents are well-informed and grounded in their responses.

For more information about the Redis integration with Amazon Bedrock, see the [Amazon Bedrock integration blog post](https://redis.io/blog/amazon-bedrock-integration-with-redis-enterprise/).

To fully set up Bedrock with Redis Cloud, you will need to do the following:

1.  [Set up a Redis Cloud subscription and vector database](/docs/latest/integrate/amazon-bedrock/set-up-redis/) for Bedrock.
    
2.  [Create a knowledge base](/docs/latest/integrate/amazon-bedrock/create-knowledge-base/) connected to your vector database.
    
3.  [Create an agent](/docs/latest/integrate/amazon-bedrock/create-agent/) connected to your knowledge base.
    

## More info

*   [Amazon Bedrock integration blog post](https://redis.io/blog/amazon-bedrock-integration-with-redis-enterprise/)
*   [Detailed steps](https://github.com/redis-applied-ai/aws-redis-bedrock-stack/blob/main/README.md)

## On this page

