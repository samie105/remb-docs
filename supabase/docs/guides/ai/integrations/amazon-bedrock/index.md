---
title: "Amazon Bedrock"
source: "https://supabase.com/docs/guides/ai/integrations/amazon-bedrock"
canonical_url: "https://supabase.com/docs/guides/ai/integrations/amazon-bedrock"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:00.031Z"
content_hash: "fca032a7fde2f495c97ed44731f4517f77d5a671d5cc447ca2ae12d99f6f5f0e"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Amazon Bedrock","Amazon Bedrock"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Amazon Bedrock","Amazon Bedrock"]
nav_prev: {"path": "supabase/docs/guides/ai/hybrid-search/index.md", "title": "Hybrid search"}
nav_next: {"path": "supabase/docs/guides/ai/integrations/llamaindex/index.md", "title": "Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications."}
---

# 

Amazon Bedrock

* * *

[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.

This guide will walk you through an example using Amazon Bedrock SDK with `vecs`. We will create embeddings using the Amazon Titan Embeddings G1 – Text v1.2 (amazon.titan-embed-text-v1) model, insert these embeddings into a Postgres database using vecs, and then query the collection to find the most similar sentences to a given query sentence.

## Create an environment[#](#create-an-environment)

First, you need to set up your environment. You will need Python 3.7+ with the `vecs` and `boto3` libraries installed.

You can install the necessary Python libraries using pip:

```
1pip install vecs boto3
```

You'll also need:

*   [Credentials to your AWS account](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
*   [A Postgres Database with the pgvector extension](hosting.md)

## Create embeddings[#](#create-embeddings)

Next, we will use Amazon’s Titan Embedding G1 - Text v1.2 model to create embeddings for a set of sentences.

```
1import boto32import vecs3import json45client = boto3.client(6    'bedrock-runtime',7    region_name='us-east-1',8	# Credentials from your AWS account9    aws_access_key_id='<replace_your_own_credentials>',10    aws_secret_access_key='<replace_your_own_credentials>',11    aws_session_token='<replace_your_own_credentials>',12)1314dataset = [15    "The cat sat on the mat.",16    "The quick brown fox jumps over the lazy dog.",17    "Friends, Romans, countrymen, lend me your ears",18    "To be or not to be, that is the question.",19]2021embeddings = []2223for sentence in dataset:24    # invoke the embeddings model for each sentence25    response = client.invoke_model(26        body= json.dumps({"inputText": sentence}),27        modelId= "amazon.titan-embed-text-v1",28        accept = "application/json",29        contentType = "application/json"30    )31    # collect the embedding from the response32    response_body = json.loads(response["body"].read())33    # add the embedding to the embedding list34    embeddings.append((sentence, response_body.get("embedding"), {}))
```

### Store the embeddings with vecs[#](#store-the-embeddings-with-vecs)

Now that we have our embeddings, we can insert them into a Postgres database using vecs.

```
1import vecs23DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"45# create vector store client6vx = vecs.Client(DB_CONNECTION)78# create a collection named 'sentences' with 1536 dimensional vectors9# to match the default dimension of the Titan Embeddings G1 - Text model10sentences = vx.get_or_create_collection(name="sentences", dimension=1536)1112# upsert the embeddings into the 'sentences' collection13sentences.upsert(records=embeddings)1415# create an index for the 'sentences' collection16sentences.create_index()
```

### Querying for most similar sentences[#](#querying-for-most-similar-sentences)

Now, we query the `sentences` collection to find the most similar sentences to a sample query sentence. First need to create an embedding for the query sentence. Next, we query the collection we created earlier to find the most similar sentences.

```
1query_sentence = "A quick animal jumps over a lazy one."23# create vector store client4vx = vecs.Client(DB_CONNECTION)56# create an embedding for the query sentence7response = client.invoke_model(8        body= json.dumps({"inputText": query_sentence}),9        modelId= "amazon.titan-embed-text-v1",10        accept = "application/json",11        contentType = "application/json"12    )1314response_body = json.loads(response["body"].read())1516query_embedding = response_body.get("embedding")1718# query the 'sentences' collection for the most similar sentences19results = sentences.query(20    data=query_embedding,21    limit=3,22    include_value = True23)2425# print the results26for result in results:27    print(result)
```

This returns the most similar 3 records and their distance to the query vector.

```
1('The quick brown fox jumps over the lazy dog.', 0.27600620558852)2('The cat sat on the mat.', 0.609986272479202)3('To be or not to be, that is the question.', 0.744849503688346)
```

## Resources[#](#resources)

*   [Amazon Bedrock](https://aws.amazon.com/bedrock)
*   [Amazon Titan](https://aws.amazon.com/bedrock/titan)
*   [Semantic Image Search with Amazon Titan](../../examples/semantic-image-search-amazon-titan/index.md)
