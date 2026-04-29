---
title: "Video Search with Mixpeek Multimodal Embeddings"
source: "https://supabase.com/docs/guides/ai/examples/mixpeek-video-search"
canonical_url: "https://supabase.com/docs/guides/ai/examples/mixpeek-video-search"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:41.167Z"
content_hash: "e21011242229a9b062495c01ef86394d25a5e90459b53790d9c03e49285c5116"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Mixpeek","Mixpeek"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Mixpeek","Mixpeek"]
nav_prev: {"path": "supabase/docs/guides/ai/examples/image-search-openai-clip/index.md", "title": "Image Search with OpenAI CLIP"}
nav_next: {"path": "supabase/docs/guides/ai/examples/nextjs-vector-search/index.md", "title": "Vector search with Next.js and OpenAI"}
---

# 

Video Search with Mixpeek Multimodal Embeddings

## 

Implement video search with the Mixpeek Multimodal Embed API and Supabase Vector.

* * *

The [Mixpeek Embed API](https://docs.mixpeek.com/api-documentation/inference/embed) allows you to generate embeddings for various types of content, including videos and text. You can use these embeddings for:

*   Text-to-Video / Video-To-Text / Video-to-Video / Text-to-Text Search
*   Fine-tuning on your own video and text data

This guide demonstrates how to implement video search using Mixpeek Embed for video processing and embedding, and Supabase Vector for storing and querying embeddings.

## Create a new Python project with Poetry[#](#create-a-new-python-project-with-poetry)

[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:

```
1pip install poetry
```

Then initialize a new project:

```
1poetry new video-search
```

## Setup Supabase project[#](#setup-supabase-project)

If you haven't already, [install the Supabase CLI](../../../cli/index.md), then initialize Supabase in the root of your newly created poetry project:

```
1supabase init
```

Next, start your local Supabase stack:

```
1supabase start
```

This will start up the Supabase stack locally and print out a bunch of environment details, including your local `DB URL`. Make a note of that for later use.

## Install the dependencies[#](#install-the-dependencies)

Add the following dependencies to your project:

*   [`supabase`](https://github.com/supabase-community/supabase-py): Supabase Python Client
*   [`mixpeek`](https://github.com/mixpeek/python-sdk): Mixpeek Python Client for embedding generation

```
1poetry add supabase mixpeek
```

## Import the necessary dependencies[#](#import-the-necessary-dependencies)

At the top of your main Python script, import the dependencies and store your environment variables:

```
1from supabase import create_client, Client2from mixpeek import Mixpeek3import os45SUPABASE_URL = os.getenv("SUPABASE_URL")6SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")7MIXPEEK_API_KEY = os.getenv("MIXPEEK_API_KEY")
```

## Create embeddings for your videos[#](#create-embeddings-for-your-videos)

Next, create a `seed` method, which will create a new Supabase table, generate embeddings for your video chunks, and insert the embeddings into your database:

```
1def seed():2    # Initialize Supabase and Mixpeek clients3    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)4    mixpeek = Mixpeek(MIXPEEK_API_KEY)56    # Create a table for storing video chunk embeddings7    supabase.table("video_chunks").create({8        "id": "text",9        "start_time": "float8",10        "end_time": "float8",11        "embedding": "extensions.vector(768)",12        "metadata": "jsonb"13    })1415    # Process and embed video16    video_url = "https://example.com/your_video.mp4"17    processed_chunks = mixpeek.tools.video.process(18        video_source=video_url,19        chunk_interval=1,  # 1 second intervals20        resolution=[720, 1280]21    )2223    for chunk in processed_chunks:24        print(f"Processing video chunk: {chunk['start_time']}")2526        # Generate embedding using Mixpeek27        embed_response = mixpeek.embed.video(28            model_id="vuse-generic-v1",29            input=chunk['base64_chunk'],30            input_type="base64"31        )3233        # Insert into Supabase34        supabase.table("video_chunks").insert({35            "id": f"chunk_{chunk['start_time']}",36            "start_time": chunk["start_time"],37            "end_time": chunk["end_time"],38            "embedding": embed_response['embedding'],39            "metadata": {"video_url": video_url}40        }).execute()4142    print("Video processed and embeddings inserted")4344    # Create index for fast search performance45    supabase.query("CREATE INDEX ON video_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)").execute()46    print("Created index")
```

Add this method as a script in your `pyproject.toml` file:

```
1[tool.poetry.scripts]2seed = "video_search.main:seed"3search = "video_search.main:search"
```

After activating the virtual environment with `poetry shell`, you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your local database by visiting the local Supabase dashboard at [localhost:54323](http://localhost:54323/project/default/editor).

## Perform a video search from a text query[#](#perform-a-video-search-from-a-text-query)

With Supabase Vector, you can query your embeddings. You can use either a video clip as search input or alternatively, you can generate an embedding from a string input and use that as the query input:

```
1def search():2    # Initialize Supabase and Mixpeek clients3    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)4    mixpeek = Mixpeek(MIXPEEK_API_KEY)56    # Generate embedding for text query7    query_string = "a car chase scene"8    text_emb = mixpeek.embed.video(9        model_id="vuse-generic-v1",10        input=query_string,11        input_type="text"12    )1314    # Query the collection15    results = supabase.rpc(16        'match_video_chunks',17        {18            'query_embedding': text_emb['embedding'],19            'match_threshold': 0.8,20            'match_count': 521        }22    ).execute()2324    # Display the results25    if results.data:26        for result in results.data:27            print(f"Matched chunk from {result['start_time']} to {result['end_time']} seconds")28            print(f"Video URL: {result['metadata']['video_url']}")29            print(f"Similarity: {result['similarity']}")30            print("---")31    else:32        print("No matching video chunks found")
```

This query will return the top 5 most similar video chunks from your database.

You can now test it out by running `poetry run search`, and you will be presented with the most relevant video chunks to the query "a car chase scene".

## Conclusion[#](#conclusion)

With just a couple of Python scripts, you are able to implement video search as well as reverse video search using Mixpeek Embed and Supabase Vector. This approach allows for powerful semantic search capabilities that can be integrated into various applications, enabling you to search through video content using both text and video queries.
