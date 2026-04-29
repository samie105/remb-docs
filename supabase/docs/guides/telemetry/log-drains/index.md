---
title: "Log Drains"
source: "https://supabase.com/docs/guides/telemetry/log-drains"
canonical_url: "https://supabase.com/docs/guides/telemetry/log-drains"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:06.814Z"
content_hash: "efd145eb9d895227bfd0b8b7480a975f9a77174ed5a96cfb4fcbd15b72db61bb"
menu_path: ["Telemetry","Telemetry","Logging & observability","Logging & observability","Log drains","Log drains"]
section_path: ["Telemetry","Telemetry","Logging & observability","Logging & observability","Log drains","Log drains"]
nav_prev: {"path": "supabase/docs/guides/telemetry/advanced-log-filtering/index.md", "title": "Advanced Log Filtering"}
nav_next: {"path": "supabase/docs/guides/telemetry/logs/index.md", "title": "Logging"}
---

# Supported destinations

The following table lists the supported destinations and the required setup configuration:

Destination

Transport Method

Configuration

Generic HTTP endpoint

HTTP

URL  
HTTP Version  
Gzip  
Headers

Datadog

HTTP

API Key  
Region

Loki

HTTP

URL  
Headers

Sentry

HTTP

DSN

Amazon S3

AWS SDK

S3 Bucket  
Region  
Access Key ID  
Secret Access Key  
Batch Timeout

OTLP

HTTP

Endpoint  
Protocol  
Gzip  
Headers

HTTP requests are batched with a max of 250 logs or 1 second intervals, whichever happens first. Logs are compressed via Gzip if the destination supports it.

## Generic HTTP endpoint[#](#generic-http-endpoint)

Logs are sent as a POST request with a JSON body. Both HTTP/1 and HTTP/2 protocols are supported. Custom headers can optionally be configured for all requests.

Note that requests are **unsigned**.

Unsigned requests to HTTP endpoints are temporary and all requests will signed in the near future.

## Datadog logs[#](#datadog-logs)

Logs sent to Datadog have the name of the log source set on the `service` field of the event and the source set to `Supabase`. Logs are gzipped before they are sent to Datadog.

The payload message is a JSON string of the raw log event, prefixed with the event timestamp.

To setup Datadog log drain, generate a Datadog API key [here](https://app.datadoghq.com/organization-settings/api-keys) and the location of your Datadog site.

If you are interested in other log drains, upvote them [here](https://github.com/orgs/supabase/discussions/28324)

## Loki[#](#loki)

Logs sent to the Loki HTTP API are specifically formatted according to the HTTP API requirements. See the official Loki HTTP API documentation for [more details](https://grafana.com/docs/loki/latest/reference/loki-http-api/#ingest-logs).

Events are batched with a maximum of 250 events per request.

The log source and product name will be used as stream labels.

The `event_message` and `timestamp` fields will be dropped from the events to avoid duplicate data.

Loki must be configured to accept **structured metadata**, and it is advised to increase the default maximum number of structured metadata fields to at least 500 to accommodate large log event payloads of different products.

## Sentry[#](#sentry)

Logs are sent to Sentry as part of [Sentry's Logging Product](https://docs.sentry.io/product/explore/logs/). Ingesting Supabase logs as Sentry errors is currently not supported.

To setup the Sentry log drain, you need to do the following:

1.  Grab your DSN from your [Sentry project settings](https://docs.sentry.io/concepts/key-terms/dsn-explainer/). It should be of the format `{PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}{PATH}/{PROJECT_ID}`.
2.  Create log drain in [Supabase dashboard](/dashboard/project/_/settings/log-drains)
3.  Watch for events in the [Sentry Logs page](https://sentry.io/explore/logs/)

All fields from the log event are attached as attributes to the Sentry log, which can be used for filtering and grouping in the Sentry UI. There are no limits to cardinality or the number of attributes that can be attached to a log.

If you are self-hosting Sentry, Sentry Logs are only supported in self-hosted version [25.9.0](https://github.com/getsentry/self-hosted/releases/tag/25.9.0) and later.

## Axiom[#](#axiom)

Logs sent to a specified Axiom's dataset as JSON of a raw log event, with timestamp modified to be parsed by ingestion endpoint.

To set up the Axiom log drain, you have to:

1.  Create a dataset for ingestion in Axiom Console -> Datasets
2.  Generate an Axiom API Token with permission to ingest into the created dataset (see [Axiom docs](https://axiom.co/docs/reference/tokens#create-basic-api-token))
3.  Create log drain in [Supabase dashboard](/dashboard/project/_/settings/log-drains), providing:
    *   Name of the dataset
    *   API token
4.  Watch for events in the Stream panel of Axiom Console

## Amazon S3[#](#amazon-s3)

Logs are written to an existing S3 bucket that you own.

Required configuration when creating an S3 Log Drain:

*   S3 Bucket: the name of an existing S3 bucket.
*   Region: the AWS region where the bucket is located.
*   Access Key ID: used for authentication.
*   Secret Access Key: used for authentication.
*   Batch Timeout (ms): maximum time to wait before flushing a batch. Recommended 2000-5000ms.

Ensure the AWS account tied to the Access Key ID has permissions to write to the specified S3 bucket.

## OpenTelemetry protocol (OTLP)[#](#opentelemetry-protocol-otlp)

Logs are sent to any OTLP-compatible endpoint using the OpenTelemetry Protocol over HTTP with Protocol Buffers encoding.

OTLP is an open-standard protocol for telemetry data, making it compatible with many observability platforms including:

*   OpenTelemetry Collector
*   Grafana Cloud
*   New Relic
*   Honeycomb
*   Datadog (OTLP ingestion)
*   Elastic
*   And many more

Required configuration when creating an OTLP Log Drain:

*   Endpoint: The full URL of your OTLP HTTP endpoint (typically ending in `/v1/logs`)
*   Protocol: Currently only `http/protobuf` is supported
*   Gzip: Enable compression to reduce bandwidth (recommended: enabled)
*   Headers: Optional authentication headers (e.g., `Authorization`, `X-API-Key`)

Logs are sent as OTLP log record messages using Protocol Buffers encoding, following the [OpenTelemetry Logs specification](https://opentelemetry.io/docs/specs/otel/logs/).

Ensure your OTLP endpoint is configured to accept logs at the `/v1/logs` path with `application/x-protobuf` content type.

## Pricing[#](#pricing)

For a detailed breakdown of how charges are calculated, refer to [Manage Log Drain usage](../../platform/manage-your-usage/log-drains/index.md).
