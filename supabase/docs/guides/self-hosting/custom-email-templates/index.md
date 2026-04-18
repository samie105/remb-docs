---
title: "Custom Email Templates"
source: "https://supabase.com/docs/guides/self-hosting/custom-email-templates"
canonical_url: "https://supabase.com/docs/guides/self-hosting/custom-email-templates"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:17.857Z"
content_hash: "950cc07e2442f19df3bb4ed24d83a69945bb012df3abc47e7606595d5cc2ba2c"
menu_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Custom Email Templates","Custom Email Templates"]
section_path: ["Self-Hosting","Self-Hosting","How-to Guides","How-to Guides","Custom Email Templates","Custom Email Templates"]
---
# 

Custom Email Templates

## 

Configure custom email templates with self-hosted Supabase instance

* * *

When running a self-hosted Supabase instance, you can fully customize emails sent by Supabase Auth.

## Overview[#](#overview)

Supabase Auth does not read email templates from mounted Docker volumes. Instead, it expects each template to be available at a URL that returns a valid HTML template.

This URL:

*   Does not need to be public
*   Must be reachable from `auth` service
*   Must return a valid Golang HTML template

To provide templates to Supabase Auth, you need a service that serves static HTML files. This can be any server of your choice. You can even use `kong` service which is included with the default Supabase docker configuration. The only requirement is that the `auth` service must be able to reach it via a HTTP GET request.

This guide uses [Caddy](https://github.com/caddyserver/caddy) for serving templates.

If Supabase Auth cannot fetch the template or if the fetched template is invalid, it falls back to the default template.

## Authentication email templates[#](#authentication-email-templates)

Authentication email templates can be configured using the following environment variables:

*   `GOTRUE_MAILER_TEMPLATES_<AUTH_FLOW>`: Provide a custom template URL. Falls back to the default template if not set.
*   `GOTRUE_MAILER_SUBJECTS_<AUTH_FLOW>`: Customize the email subject. Falls back to the default subject if not set.

Auth flow

Sent

`CONFIRMATION`

When a user signs up and needs to verify their email address

`RECOVERY`

When a user requests a password reset

`MAGIC_LINK`

When a user requests a magic link for password-less authentication

`INVITE`

When a user is invited to join your application via email invitation

`EMAIL_CHANGE`

When a user requests to change their email address

`REAUTHENTICATION`

When a user needs to re-authenticate for sensitive operations

For example:

```
1GOTRUE_MAILER_TEMPLATES_MAGIC_LINK='<template_url>'2GOTRUE_MAILER_SUBJECTS_MAGIC_LINK='<custom_subject>'
```

### Example[#](#example)

Below is an example configuration for setting up a custom invite template.

### Step 1: Create a templates directory[#](#step-1-create-a-templates-directory)

Create a `templates` directory inside the existing `volumes` directory and add your email templates to it.

Your directory structure should look like this:

```
1volumes/2  templates/3    invite.html
```

### Step 2: Update `docker-compose.yml`[#](#step-2-update-docker-composeyml)

Update the `auth` service to depend on `templates-server`, and pass the email template environment variables. Then add a `templates-server` service to serve the templates from `./volumes/templates`.

```
1services:2  auth:3    depends_on:4      db:5        condition: service_healthy6      templates-server: # 👈 new dependency7        condition: service_started8    environment:9      GOTRUE_MAILER_TEMPLATES_INVITE: 'http://templates-server/invite.html'10      GOTRUE_MAILER_SUBJECTS_INVITE: 'You have been invited'1112  templates-server:13    image: caddy:2-alpine14    command: ['caddy', 'file-server', '-r', '/templates', '--listen', ':80']15    volumes:16      - ./volumes/templates:/templates
```

#### What this configuration does[#](#what-this-configuration-does)

*   Adds a `templates-server`service that runs alongside the Supabase services in the same docker network.
*   Serves your custom email template files from the `./volumes/templates` directory.
*   Keeps the templates-server private to the Docker network (no published ports), so it is not accessible from outside.
*   Allows the `auth` service to fetch templates via `http://templates-server/<template>.html`.

### Step 3: Restart containers[#](#step-3-restart-containers)

```
1docker compose up -d --force-recreate --no-deps auth templates-server
```

## Notification email templates[#](#notification-email-templates)

Notification email templates can be configured using the following environment variables:

*   `GOTRUE_MAILER_NOTIFICATIONS_<NOTIFICATION_TYPE>_ENABLED`: Enable the notification email
*   `GOTRUE_MAILER_TEMPLATES_<NOTIFICATION_TYPE>_NOTIFICATION`: Provide a custom template URL. Falls back to the default template if not set.
*   `GOTRUE_MAILER_SUBJECTS_<NOTIFICATION_TYPE>_NOTIFICATION`: Customize the email subject. Falls back to the default subject if not set.

Notification Type

Sent

`PASSWORD_CHANGED`

When a user's password is changed

`EMAIL_CHANGED`

When a user's email address is changed

`PHONE_CHANGED`

When a user's phone number is changed

`MFA_FACTOR_ENROLLED`

When a new MFA factor is added to the user's account

`MFA_FACTOR_UNENROLLED`

When an MFA factor is removed from the user's account

`IDENTITY_LINKED`

When a new identity is linked to the account

`IDENTITY_UNLINKED`

When an identity is unlinked from the account

For example:

```
1GOTRUE_MAILER_NOTIFICATIONS_EMAIL_CHANGED_ENABLED='true'2GOTRUE_MAILER_TEMPLATES_EMAIL_CHANGED_NOTIFICATION='<template_url>'3GOTRUE_MAILER_SUBJECTS_EMAIL_CHANGED_NOTIFICATION='<custom_subject>'
```

### Example[#](#example)

Below is an example configuration for setting up a custom password changed notification template.

### Step 1: Create the templates directory[#](#step-1-create-the-templates-directory)

This example reuses the directory created in **Auth Email Templates – Step 1** (`volumes/templates`). Add your notification email templates to this directory.

Your directory structure should look like this:

```
1volumes/2  templates/3    invite.html4    password_changed_notification.html
```

### Step 2: Update `docker-compose.yml`[#](#step-2-update-docker-composeyml)

Update the `auth` service in `docker-compose.yml` to enable password changed notification

```
1services:2  auth:3    depends_on:4      db:5        condition: service_healthy6      templates-server:7        condition: service_started8    environment:9      GOTRUE_MAILER_NOTIFICATIONS_PASSWORD_CHANGED_ENABLED: 'true' # 👈 enabling the notification is required10      GOTRUE_MAILER_TEMPLATES_PASSWORD_CHANGED_NOTIFICATION: 'http://templates-server/password_changed_notification.html'11      GOTRUE_MAILER_SUBJECTS_PASSWORD_CHANGED_NOTIFICATION: 'Your password has been changed'1213  templates-server:14    image: caddy:2-alpine15    command: ['caddy', 'file-server', '-r', '/templates', '--listen', ':80']16    volumes:17      - ./volumes/templates:/templates
```

### Step 3: Restart containers[#](#step-3-restart-containers)

```
1docker compose up -d --force-recreate --no-deps auth templates-server
```
