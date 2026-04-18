---
title: "Serverless"
source: "https://fastify.dev/docs/latest/Guides/Serverless/"
canonical_url: "https://fastify.io/docs/latest/Guides/Serverless/"
docset: "fastify"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:41.134Z"
content_hash: "d27e7a0c768484093e06a3f73181c596796d8ea87bce68258b3cb06c4aacb40c"
menu_path: ["Serverless"]
section_path: []
nav_prev: {"path": "fastify/docs/latest/Guides/Style-Guide/index.md", "title": "Fastify Style Guide"}
---

# Use the official Node.js 10 image.# https://hub.docker.com/_/nodeFROM node:10# Create and change to the app directory.WORKDIR /usr/src/app# Copy application dependency manifests to the container image.# A wildcard is used to ensure both package.json AND package-lock.json are copied.# Copying this separately prevents re-running npm install on every code change.COPY package*.json ./# Install production dependencies.RUN npm i --production# Copy local code to the container image.COPY . .# Run the web service on container startup.CMD [ "npm", "start" ]
```

### Add a .dockerignore[​](#add-a-dockerignore "Direct link to Add a .dockerignore")

To keep build artifacts out of your container (which keeps it small and improves build times) add a `.dockerignore` file like the one below:

```
DockerfileREADME.mdnode_modulesnpm-debug.log
```

### Submit build[​](#submit-build "Direct link to Submit build")

Next, submit your app to be built into a Docker image by running the following command (replacing `PROJECT-ID` and `APP-NAME` with your GCP project id and an app name):

```
gcloud builds submit --tag gcr.io/PROJECT-ID/APP-NAME
```

### Deploy Image[​](#deploy-image "Direct link to Deploy Image")

After your image has built, you can deploy it with the following command:

```
gcloud beta run deploy --image gcr.io/PROJECT-ID/APP-NAME --platform managed
```

Your app will be accessible from the URL GCP provides.

## netlify-lambda[​](#netlify-lambda "Direct link to netlify-lambda")

First, please perform all preparation steps related to **AWS Lambda**.

Create a folder called `functions`, then create `server.js` (and your endpoint path will be `server.js`) inside the `functions` folder.

### functions/server.js[​](#functionsserverjs "Direct link to functions/server.js")

```
export { handler } from '../lambda.js'; // Change `lambda.js` path to your `lambda.js` path
```

### netlify.toml[​](#netlifytoml "Direct link to netlify.toml")

```
[build]  # This will be run the site build  command = "npm run build:functions"  # This is the directory is publishing to netlify's CDN  # and this is directory of your front of your app  # publish = "build"  # functions build directory  functions = "functions-build" # always appends `-build` folder to your `functions` folder for builds
```

### webpack.config.netlify.js[​](#webpackconfignetlifyjs "Direct link to webpack.config.netlify.js")

**Do not forget to add this Webpack config, or else problems may occur**

```
const nodeExternals = require('webpack-node-externals');const dotenv = require('dotenv-safe');const webpack = require('webpack');const env = process.env.NODE_ENV || 'production';const dev = env === 'development';if (dev) {  dotenv.config({ allowEmptyValues: true });}module.exports = {  mode: env,  devtool: dev ? 'eval-source-map' : 'none',  externals: [nodeExternals()],  devServer: {    proxy: {      '/.netlify': {        target: 'http://localhost:9000',        pathRewrite: { '^/.netlify/functions': '' }      }    }  },  module: {    rules: []  },  plugins: [    new webpack.DefinePlugin({      'process.env.APP_ROOT_PATH': JSON.stringify('/'),      'process.env.NETLIFY_ENV': true,      'process.env.CONTEXT': env    })  ]};
```

### Scripts[​](#scripts "Direct link to Scripts")

Add this command to your `package.json` _scripts_

```
"scripts": {  ...  "build:functions": "netlify-lambda build functions --config ./webpack.config.netlify.js"  ...}
```

Then it should work fine.

## Vercel[​](#vercel "Direct link to Vercel")

[Vercel](https://vercel.com) fully supports deploying Fastify applications. Additionally, with Vercel's [Fluid compute](https://vercel.com/docs/functions/fluid-compute), you can combine server-like concurrency with the autoscaling properties of traditional serverless functions.

Get started with the [Fastify template on Vercel](https://vercel.com/templates/backend/fastify-on-vercel).

[Fluid compute](https://vercel.com/docs/functions/fluid-compute) currently requires an explicit opt-in. Learn more about enabling Fluid compute [here](https://vercel.com/docs/fluid-compute#enabling-fluid-compute).


