---
title: "Roboflow"
source: "https://supabase.com/docs/guides/ai/integrations/roboflow"
canonical_url: "https://supabase.com/docs/guides/ai/integrations/roboflow"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:03.918Z"
content_hash: "78026a05920393e5a099ea6cfd8c95979021ea5f9ba2d2f6feed23c661e7d066"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Roboflow","Roboflow"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Roboflow","Roboflow"]
nav_prev: {"path": "supabase/docs/guides/ai/integrations/llamaindex/index.md", "title": "Learn how to integrate Supabase with LlamaIndex, a data framework for your LLM applications."}
nav_next: {"path": "supabase/docs/guides/ai/quickstarts/face-similarity/index.md", "title": "Face similarity search"}
---

# 

Roboflow

## 

Learn how to integrate Supabase with Roboflow, a tool for running fine-tuned and foundation vision models.

* * *

In this guide, we will walk through two examples of using [Roboflow Inference](https://inference.roboflow.com) to run fine-tuned and foundation models. We will run inference and save predictions using an object detection model and [CLIP](https://github.com/openai/CLIP).

## Project setup[#](#project-setup)

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and publishable keys.

## Save computer vision predictions[#](#save-computer-vision-predictions)

Once you have a trained vision model, you need to create business logic for your application. In many cases, you want to save inference results to a file.

The steps below show you how to run a vision model locally and save predictions to Supabase.

### Preparation: Set up a model[#](#preparation-set-up-a-model)

Before you begin, you will need an object detection model trained on your data.

You can [train a model on Roboflow](https://blog.roboflow.com/getting-started-with-roboflow/), leveraging end-to-end tools from data management and annotation to deployment, or [upload custom model weights](https://docs.roboflow.com/deploy/upload-custom-weights) for deployment.

All models have an infinitely scalable API through which you can query your model, and can be run locally.

For this guide, we will use a demo [rock, paper, scissors](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw) model.

### Step 1: Install and start Roboflow Inference[#](#step-1-install-and-start-roboflow-inference)

You will deploy our model locally using Roboflow Inference, a computer vision inference server.

To install and start Roboflow Inference, first install Docker on your machine.

Then, run:

```
1pip install inference inference-cli inference-sdk && inference server start
```

An inference server will be available at `http://localhost:9001`.

### Step 2: Run inference on an image[#](#step-2-run-inference-on-an-image)

You can run inference on images and videos. Let's run inference on an image.

Create a new Python file and add the following code:

```
1from inference_sdk import InferenceHTTPClient23image = "example.jpg"4MODEL_ID = "rock-paper-scissors-sxsw/11"56client = InferenceHTTPClient(7    api_url="http://localhost:9001",8    api_key="ROBOFLOW_API_KEY"9)10with client.use_model(MODEL_ID):11    predictions = client.infer(image)1213print(predictions)
```

Above, replace:

1.  The image URL with the name of the image on which you want to run inference.
2.  `ROBOFLOW_API_KEY` with your Roboflow API key. [Learn how to retrieve your Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key).
3.  `MODEL_ID` with your Roboflow model ID. [Learn how to retrieve your model ID](https://docs.roboflow.com/api-reference/workspace-and-project-ids).

When you run the code above, a list of predictions will be printed to the console:

```
1{'time': 0.05402109300121083, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}
```

### Step 3: Save results in Supabase[#](#step-3-save-results-in-supabase)

To save results in Supabase, add the following code to your script:

```
1import os2from supabase import create_client, Client34url: str = os.environ.get("SUPABASE_URL")5key: str = os.environ.get("SUPABASE_KEY")6supabase: Client = create_client(url, key)78result = supabase.table('predictions') \9    .insert({"filename": image, "predictions": predictions}) \10    .execute()
```

You can then query your predictions using the following code:

```
1result = supabase.table('predictions') \2    .select("predictions") \3    .filter("filename", "eq", image) \4    .execute()56print(result)
```

Here is an example result:

```
1data=[{'predictions': {'time': 0.08492901099998562, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}}, {'predictions': {'time': 0.08818970100037404, 'image': {'width': 640, 'height': 480}, 'predictions': [{'x': 312.5, 'y': 392.0, 'width': 255.0, 'height': 110.0, 'confidence': 0.8620790839195251, 'class': 'Paper', 'class_id': 0}]}}] count=None
```

## Calculate and save CLIP embeddings[#](#calculate-and-save-clip-embeddings)

You can use the Supabase vector database functionality to store and query CLIP embeddings.

Roboflow Inference provides an HTTP interface through which you can calculate image and text embeddings using CLIP.

### Step 1: Install and start Roboflow Inference[#](#step-1-install-and-start-roboflow-inference)

See [Step #1: Install and Start Roboflow Inference](#step-1-install-and-start-roboflow-inference) above to install and start Roboflow Inference.

### Step 2: Run CLIP on an image[#](#step-2-run-clip-on-an-image)

Create a new Python file and add the following code:

```
1import cv22import supervision as sv3import requests4import base645import os67IMAGE_DIR = "images/train/images/"8API_KEY = ""9SERVER_URL = "http://localhost:9001"1011results = []1213for i, image in enumerate(os.listdir(IMAGE_DIR)):14    print(f"Processing image {image}")15    infer_clip_payload = {16        "image": {17            "type": "base64",18            "value": base64.b64encode(open(IMAGE_DIR + image, "rb").read()).decode("utf-8"),19        },20    }2122    res = requests.post(23        f"{SERVER_URL}/clip/embed_image?api_key={API_KEY}",24        json=infer_clip_payload,25    )2627    embeddings = res.json()['embeddings']2829    results.append({30        "filename": image,31        "embeddings": embeddings32    })
```

This code will calculate CLIP embeddings for each image in the directory and print the results to the console.

Above, replace:

1.  `IMAGE_DIR` with the directory containing the images on which you want to run inference.
2.  `ROBOFLOW_API_KEY` with your Roboflow API key. [Learn how to retrieve your Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key).

You can also calculate CLIP embeddings in the cloud by setting `SERVER_URL` to `https://infer.roboflow.com`.

### Step 3: Save embeddings in Supabase[#](#step-3-save-embeddings-in-supabase)

You can store your image embeddings in Supabase using the Supabase `vecs` Python package:

First, install `vecs`:

```
1pip install vecs
```

Next, add the following code to your script to create an index:

```
1import vecs23DB_CONNECTION = "postgresql://postgres:[password]@[host]:[port]/[database]"45vx = vecs.create_client(DB_CONNECTION)67# create a collection of vectors with 3 dimensions8images = vx.get_or_create_collection(name="image_vectors", dimension=512)910for result in results:11    image = result["filename"]12    embeddings = result["embeddings"][0]1314    # insert a vector into the collection15    images.upsert(16        records=[17            (18                image,19                embeddings,20                {} # metadata21            )22        ]23    )2425images.create_index()
```

Replace `DB_CONNECTION` with the authentication information for your database. You can retrieve this from the Supabase dashboard in `Project Settings > Database Settings`.

You can then query your embeddings using the following code:

```
1infer_clip_payload = {2    "text": "cat",3}45res = requests.post(6    f"{SERVER_URL}/clip/embed_text?api_key={API_KEY}",7    json=infer_clip_payload,8)910embeddings = res.json()['embeddings']1112result = images.query(13    data=embeddings[0],14    limit=115)1617print(result[0])
```

## Resources[#](#resources)

*   [Roboflow Inference documentation](https://inference.roboflow.com)
*   [Roboflow Getting Started guide](https://blog.roboflow.com/getting-started-with-roboflow/)
*   [How to Build a Semantic Image Search Engine with Supabase and OpenAI CLIP](https://blog.roboflow.com/how-to-use-semantic-search-supabase-openai-clip/)
