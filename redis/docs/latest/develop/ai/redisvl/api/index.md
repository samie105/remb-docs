---
title: "RedisVL API"
source: "https://redis.io/docs/latest/develop/ai/redisvl/api/"
canonical_url: "https://redis.io/docs/latest/develop/ai/redisvl/api/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:02.070Z"
content_hash: "08c16e4a5e15b5fbf322320a115391b397bbe33cf4c4da5927e76154d0357292"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        RedisVL","→","RedisVL","→\n      \n        RedisVL API","→","RedisVL API"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        RedisVL","→","RedisVL","→\n      \n        RedisVL API","→","RedisVL API"]
nav_prev: {"path": "redis/docs/latest/develop/tools/redis-for-vscode/index.md", "title": "Redis for VS Code"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/management/replication/index.md", "title": "Redis replication"}
---

# RedisVL API

Reference documentation for the RedisVL API.

*   [Schema](schema/)
    *   [IndexSchema](schema/#indexschema)
    *   [Index-Level Stopwords Configuration](schema/#index-level-stopwords-configuration)
    *   [Defining Fields](schema/#defining-fields)
    *   [Basic Field Types](schema/#basic-field-types)
    *   [Vector Field Types](schema/#vector-field-types)
    *   [SVS-VAMANA Configuration Utilities](schema/#svs-vamana-configuration-utilities)
    *   [Vector Algorithm Comparison](schema/#vector-algorithm-comparison)
*   [Search Index Classes](searchindex/)
    *   [SearchIndex](searchindex/#searchindex)
    *   [AsyncSearchIndex](searchindex/#asyncsearchindex)
*   [Vector](vector/)
    *   [Vector](vector/#id1)
*   [Query](query/)
    *   [VectorQuery](query/#vectorquery)
    *   [VectorRangeQuery](query/#vectorrangequery)
    *   [HybridQuery](query/#hybridquery)
    *   [TextQuery](query/#textquery)
    *   [FilterQuery](query/#filterquery)
    *   [CountQuery](query/#countquery)
    *   [MultiVectorQuery](query/#multivectorquery)
*   [Filter](filter/)
    *   [FilterExpression](filter/#filterexpression)
    *   [Tag](filter/#tag)
    *   [Text](filter/#text)
    *   [Num](filter/#num)
    *   [Geo](filter/#geo)
    *   [GeoRadius](filter/#georadius)
*   [Vectorizers](vectorizer/)
    *   [HFTextVectorizer](vectorizer/#hftextvectorizer)
    *   [OpenAITextVectorizer](vectorizer/#openaitextvectorizer)
    *   [AzureOpenAITextVectorizer](vectorizer/#azureopenaitextvectorizer)
    *   [VertexAITextVectorizer](vectorizer/#vertexaitextvectorizer)
    *   [CohereTextVectorizer](vectorizer/#coheretextvectorizer)
    *   [BedrockTextVectorizer](vectorizer/#bedrocktextvectorizer)
    *   [CustomTextVectorizer](vectorizer/#customtextvectorizer)
    *   [VoyageAITextVectorizer](vectorizer/#voyageaitextvectorizer)
*   [Rerankers](reranker/)
    *   [CohereReranker](reranker/#coherereranker)
    *   [HFCrossEncoderReranker](reranker/#hfcrossencoderreranker)
    *   [VoyageAIReranker](reranker/#voyageaireranker)
*   [LLM Cache](cache/)
    *   [SemanticCache](cache/#semanticcache)
*   [Embeddings Cache](cache/#embeddings-cache)
    *   [EmbeddingsCache](cache/#embeddingscache)
*   [LLM Message History](message_history/)
    *   [SemanticMessageHistory](message_history/#semanticmessagehistory)
    *   [MessageHistory](message_history/#messagehistory)
*   [Semantic Router](router/)
    *   [Semantic Router](router/#semantic-router-api)
    *   [Routing Config](router/#routing-config)
    *   [Route](router/#route)
    *   [Route Match](router/#route-match)
    *   [Distance Aggregation Method](router/#distance-aggregation-method)
