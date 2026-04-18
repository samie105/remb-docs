---
title: "Redis Software quickstart"
source: "https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart/"
canonical_url: "https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:53.673Z"
content_hash: "a031c13fd3f93baff06440b94f9d59fafb1190e741ed35c5747802172a12e852"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Redis Software quickstarts","→","Redis Software quickstarts","→\n      \n        Redis Software quickstart","→","Redis Software quickstart"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Redis Software quickstarts","→","Redis Software quickstarts","→\n      \n        Redis Software quickstart","→","Redis Software quickstart"]
---
# Redis Software quickstart

Set up a test deployment of Redis Software for Linux.

Redis Software

This guide helps you install Redis Software on a Linux host to test its capabilities.

When finished, you'll have a simple cluster with a single node:

1.  [Ensure port availability](#ensure-port-availability)
    
2.  [Install Redis Software](#install-redis-enterprise-software)
    
3.  [Set up a Redis Software cluster](#set-up-a-cluster)
    
4.  [Create a new Redis database](#create-a-database)
    
5.  [Connect to your Redis database](#connect-to-your-database)
    

Note:

**This quickstart is designed for local testing only.** For production environments, see the [install and setup](/docs/latest/operate/rs/installing-upgrading/#install-redis-enterprise-software) guide for deployment options and instructions.

## Ensure port availability

If ports that Redis assigns to the database are being used by the operating system or other processes, the installation fails.

Follow the relevant sections to configure required ports.

For recommended and optional port configuration, see [Network port configurations](/docs/latest/operate/rs/networking/port-configurations/).

### Update `sysctl.conf` to avoid port collisions

To avoid port collision, update `/etc/sysctl.conf` to include:

```sh
net.ipv4.ip_local_port_range = 30000 65535
```

### OS conflicts with port 53

If port 53 is in use, the installation fails. This issue can occur in default installations of certain operating systems in which `systemd-resolved` (DNS server) or `dnsmasq` is running.

To prevent this issue, change the system configuration to make this port available before installation.

To prevent `systemd-resolved` from using port 53:

1.  Edit `/etc/systemd/resolved.conf`:
    
    ```sh
    sudo vi /etc/systemd/resolved.conf
    ```
    
2.  Add `DNSStubListener=no` as the last line in the file and save the file.
    
3.  Rename the current `/etc/resolv.conf` file:
    
    ```sh
    sudo mv /etc/resolv.conf /etc/resolv.conf.orig
    ```
    
4.  Create a symbolic link for `/etc/resolv.conf`:
    
    ```sh
    sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
    ```
    
    Note:
    
    You might encounter a temporary name resolution error (`sudo: unable to resolve host {hostname}: Temporary failure in name resolution`), which should be fixed when you restart `systemd-resolved` in the next step.
    
5.  Restart the DNS service:
    
    ```sh
    sudo service systemd-resolved restart
    ```
    

To prevent `dnsmasq` from using port 53:

1.  Stop the `dnsmasq` service if it's running:
    
    ```sh
    sudo systemctl stop dnsmasq
    ```
    
2.  Prevent `dnsmasq` from starting automatically at system boot:
    
    ```sh
    sudo systemctl disable dnsmasq
    ```
    
3.  Mask `dnsmasq` to prevent it from being started manually or by other services:
    
    ```sh
    sudo systemctl mask dnsmasq
    ```
    
4.  Verify `dnsmasq` is no longer active and won't start at system boot:
    
    ```sh
    sudo systemctl status dnsmasq
    ```
    

### Configuration for AWS and GCP

For detailed configuration instructions, see your cloud provider's documentation.

1.  Create a VPC that you can use with regional subnets.
    
2.  Within this VPC, create firewall rules that allow external and internal access for Redis Software.
    

Ingress/Egress

Source

Protocol

Ports

Other protocols

Ingress

0.0.0.0/0

TCP

21, 22, 53, 8001, 8443, 9443, 8070, 10000-19999

ICMP

Ingress

0.0.0.0/0

UDP

53, 5353

Ingress

10.0.0.0/8 (if subnets use 10. ranges)

all

all

## Install Redis Software

To install Redis Software:

1.  Download the installation files from the [Redis Software Download Center](https://redis.io/downloads/#Redis_Software) and copy the download package to a machine with a Linux-based OS.
    
    Note:
    
    You are required to create a free account to access the download center.
    
2.  Extract the installation files:
    
    ```sh
    tar vxf <downloaded tar file name>
    ```
    
3.  Run the `install.sh` script in the current directory:
    
    ```sh
    sudo ./install.sh -y
    ```
    

## Set up a cluster

To set up your machine as a Redis Software cluster:

1.  In a browser, go to `https://<name-or-IP-address-of-the-machine-with-Redis-Enterprise-Software-installed>:8443` to access the Cluster Manager UI. If you use a browser on the host machine, you can also access the Cluster Manager UI at `https://localhost:8443`.
    
    The cluster generates self-signed TLS certificates to secure the connection. Because these self-signed certificates are unknown to the browser, you must accept them before you proceed.
    
    If the server does not show the sign-in screen, try again after a few minutes.
    
2.  Select **Create new cluster**.
    
    [![When you first install Redis Software, you need to set up a cluster.](/docs/latest/images/rs/screenshots/cluster/setup/create-cluster.png)](/docs/latest/images/rs/screenshots/cluster/setup/create-cluster.png)
3.  Enter an email and password for the administrator account, then select **Next** to proceed to cluster setup.
    
    [![Set the credentials for your admin user.](/docs/latest/images/rs/screenshots/cluster/setup/admin-credentials.png)](/docs/latest/images/rs/screenshots/cluster/setup/admin-credentials.png)
    
    You can also use these credentials to connect to the [REST API](/docs/latest/operate/rs/references/rest-api/).
    
4.  Enter your cluster license key if you have one. Otherwise, a trial version is installed.
    
    [![Enter your cluster license key if you have one.](/docs/latest/images/rs/screenshots/cluster/setup/cluster-license-key.png)](/docs/latest/images/rs/screenshots/cluster/setup/cluster-license-key.png)
5.  In the **Configuration** section, enter a cluster FQDN such as `cluster.local`, then select **Next**.
    
    [![Configure the cluster FQDN.](/docs/latest/images/rs/screenshots/cluster/setup/config-cluster.png)](/docs/latest/images/rs/screenshots/cluster/setup/config-cluster.png)
    
    Warning:
    
    If the FQDN is `cluster.local`, you cannot configure DNS. You cannot change the FQDN after cluster creation.
    
6.  On the node setup screen, select **Create cluster** to accept the defaults.
    
    [![Configure the node specific settings.](/docs/latest/images/rs/screenshots/cluster/setup/node-settings.png)](/docs/latest/images/rs/screenshots/cluster/setup/node-settings.png)
7.  Select **OK** to acknowledge the replacement of the HTTPS TLS certificate on the node. If you receive a browser warning, you can proceed safely.
    
    [![Modal shown when a page refresh is needed because the certificates have been updated.](/docs/latest/images/rs/screenshots/cluster/setup/https-page-refresh-modal.png)](/docs/latest/images/rs/screenshots/cluster/setup/https-page-refresh-modal.png)

## Create a database

1.  On the **Databases** screen, select **Quick database**.
    
    [![Select Quick database on the Databases screen.](/docs/latest/images/rs/screenshots/databases/db-screen.png)](/docs/latest/images/rs/screenshots/databases/db-screen.png)
2.  Enter 12000 for the **Port**.
    
    If port 12000 is not available, enter any available port number between 10000 to 19999 or leave it blank to let the cluster assign a port number for you. You will use this port number to connect to the database.
    
    [![Create a quick database.](/docs/latest/images/rs/screenshots/databases/quick-db-7-8-2.png)](/docs/latest/images/rs/screenshots/databases/quick-db-7-8-2.png)
3.  Select **Create** to create your database.
    

When you see **Database active** appear on the database configuration screen, the database is activated and ready for you to use.

[![Database active icon.](/docs/latest/images/rs/icons/db-active-icon.png)](/docs/latest/images/rs/icons/db-active-icon.png)

You now have a Redis database!

## Connect to your database

After you create the Redis database, you can connect to it and store data. See [Test client connection](/docs/latest/operate/rs/databases/connect/test-client-connectivity/) for connection options and examples.

## Supported web browsers

To use the Redis Software Cluster Manager UI, you need a modern browser with JavaScript enabled.

The Cluster Manager UI is officially supported for the latest version of [Google Chrome](https://www.google.com/chrome/), as well as the three previous and three subsequent versions.

## Continue learning with Redis University

See the [Get started with Redis Software learning path](https://university.redis.io/learningpath/an0mgw5bjpjfbe) for courses.

## On this page
