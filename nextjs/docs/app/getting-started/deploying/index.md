---
title: "Deploying"
source: "https://nextjs.org/docs/app/getting-started/deploying"
canonical_url: "https://nextjs.org/docs/app/getting-started/deploying"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:11:46.065Z"
content_hash: "3faa6998df13a265d7a6684b2bd279a3c70143ec628fd561280ba1ca0ad3af94"
menu_path: ["Deploying"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/getting-started/proxy/index.md", "title": "Proxy"}
nav_next: {"path": "nextjs/docs/app/getting-started/upgrading/index.md", "title": "Upgrading"}
---

# Deploying

Last updated April 23, 2026

Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms.

| Deployment Option | Feature Support |
| --- | --- |
| [Node.js server](#nodejs-server) | All |
| [Docker container](#docker) | All |
| [Static export](#static-export) | Limited |
| [Adapters](#adapters) | Varies ([verified](#verified-adapters) adapters run the test suite) |

## Node.js server[](#nodejs-server)

Next.js can be deployed to any provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

Then, run `npm run build` to build your application and `npm run start` to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a [custom server](../../guides/custom-server/index.md).

Node.js deployments support all Next.js features. Learn how to [configure them](../../guides/self-hosting/index.md) for your infrastructure.

### Templates[](#templates)

-   [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
-   [Railway](https://github.com/nextjs/deploy-railway)
-   [Replit](https://github.com/nextjs/deploy-replit)
-   [Hostinger](https://github.com/hostinger/deploy-nextjs)

## Docker[](#docker)

Next.js can be deployed to any provider that supports [Docker](https://www.docker.com/) containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker. For containerization best practices, see the [Docker guide for React.js](https://docs.docker.com/guides/reactjs/).

Docker deployments support all Next.js features. Learn how to [configure them](../../guides/self-hosting/index.md) for your infrastructure.

> **Note for development:** While Docker is excellent for production deployments, consider using local development (`npm run dev`) instead of Docker during development on Mac and Windows for better performance. [Learn more about optimizing local development](../../guides/local-development/index.md).

### Templates[](#templates-1)

The following examples demonstrate best practices for containerizing Next.js applications:

-   [Docker Standalone Output](https://github.com/vercel/next.js/tree/canary/examples/with-docker) - Deploy a Next.js application using `output: "standalone"` to generate a minimal, production-ready Docker image with only the required runtime files and dependencies.
-   [Docker Export Output](https://github.com/vercel/next.js/tree/canary/examples/with-docker-export-output) - Deploy a fully static Next.js application using `output: "export"` to generate optimized HTML files that can be served from a lightweight container or any static hosting environment.
-   [Docker Multi-Environment](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env) - Manage separate Docker configurations for development, staging, and production environments with different environment variables.

Additionally, hosting providers offer guidance on deploying Next.js:

-   [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
-   [Fly.io](https://github.com/nextjs/deploy-fly)
-   [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
-   [Render](https://github.com/nextjs/deploy-render)
-   [SST](https://github.com/nextjs/deploy-sst)

## Static export[](#static-export)

Next.js enables starting as a static site or [Single-Page Application (SPA)](../../guides/single-page-applications/index.md), then later optionally upgrading to use features that require a server.

Since Next.js supports [static exports](../../guides/static-exports/index.md), it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a [static export](../../guides/static-exports/index.md) **does not** support Next.js features that require a server. [Learn more](../../guides/static-exports/index.md#unsupported-features).

### Templates[](#templates-2)

-   [GitHub Pages](https://github.com/nextjs/deploy-github-pages)

## Adapters[](#adapters)

Next.js can be adapted to run on different platforms to support their infrastructure capabilities. The [Deployment Adapter API](../../api-reference/config/next-config-js/adapterPath/index.md) lets platforms customize how Next.js applications are built and deployed.

### Verified Adapters[](#verified-adapters)

Verified adapters are open source, run the full [Next.js compatibility test suite](../../api-reference/adapters/testing-adapters/index.md), and are hosted under the [Next.js GitHub organization](https://github.com/nextjs). The Next.js team coordinates testing with these platforms before major releases. Publicly visible test results for each adapter are coming soon. [Learn more about verified adapters](../../guides/deploying-to-platforms/index.md#verified-adapters).

-   [Vercel](https://vercel.com/docs/frameworks/nextjs)
-   [Bun](https://bun.sh/docs/frameworks/nextjs)

Cloudflare and Netlify are working on verified adapters built on the Adapter API. In the meantime, they offer their own Next.js integrations (see below).

### Other Platforms[](#other-platforms)

The following platforms offer their own Next.js integrations. These are not built on the public [Adapter API](../../api-reference/config/next-config-js/adapterPath/index.md) and are not verified by the Next.js team, so feature support and compatibility may vary. Refer to each provider's documentation for details:

-   [Appwrite Sites](https://appwrite.io/docs/products/sites/quick-start/nextjs)
-   [AWS Amplify Hosting](https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components)
-   [Cloudflare](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs)
-   [Deno Deploy](https://docs.deno.com/examples/next_tutorial)
-   [Firebase App Hosting](https://firebase.google.com/docs/app-hosting/get-started)
-   [Netlify](https://docs.netlify.com/frameworks/next-js/overview/#next-js-support-on-netlify)

For details on which Next.js features require specific platform capabilities, see [Deploying to Platforms](../../guides/deploying-to-platforms/index.md).

Was this helpful?
