---
title: "Install Redis Stack on Linux"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/linux/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/linux/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:41.219Z"
content_hash: "264f458d5ca2064346877f6ca579e21f0949321b6154777756f210c213b2a030"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack on Linux","→","Install Redis Stack on Linux"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack on Linux","→","Install Redis Stack on Linux"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/install/archive/install-stack/docker/index.md", "title": "Run Redis Stack on Docker"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/install/archive/install-stack/mac-os/index.md", "title": "Install Redis Stack on macOS"}
---

# Install Redis Stack on Linux

How to install Redis Stack on Linux

Redis Open Source

Learn how to install Redis Stack on Linux from the official APT repository or RPM feed, or with Snap or AppImage.

## From the official Ubuntu/Debian APT Repository

See [this page](https://redis.io/downloads/#redis-stack-downloads) for a complete list of supported Ubuntu/Debian platforms. Add the repository to the APT index, update it, and install Redis Stack:

```bash
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis-stack-server
```

Redis will not start automatically, nor will it start at boot time. To do this, run the following commands.

```bash
sudo systemctl enable redis-stack-server
sudo systemctl start redis-stack-server
```

## From the official Red Hat/Rocky RPM Feeds

See [this page](https://redis.io/downloads/#redis-stack-downloads) for a complete list of supported Red Hat/Rocky platforms. Follow these steps to install Redis Stack.

1.  Create the file `/etc/yum.repos.d/redis.repo` with the following contents.
    
    ```bash
    [Redis]
    name=Redis
    baseurl=http://packages.redis.io/rpm/rhel9 # replace rhel9 with the appropriate value for your platform
    enabled=1
    gpgcheck=1
    ```
    
2.  Run the following commands:
    
    ```bash
    curl -fsSL https://packages.redis.io/gpg > /tmp/redis.key
    sudo rpm --import /tmp/redis.key
    sudo yum install epel-release
    sudo yum install redis-stack-server
    ```
    

Redis will not start automatically, nor will it start at boot time. To do this, run the following commands.

```bash
sudo systemctl enable redis-stack-server
sudo systemctl start redis-stack-server
```

## On Ubuntu with Snap

First, download the latest Redis Stack snap package from [this page](https://redis.io/downloads/).

To install, run:

```bash
sudo apt update
sudo apt install redis-tools
sudo snap install --dangerous --classic <snapname.snap>
```

Redis will not start automatically, nor will it start at boot time. To start `redis-stack-server` in the foreground, run the command:

```bash
sudo snap run redis-stack-server
```

To stop Redis, enter `Ctrl-C`.

Follow these steps to integrate Redis Stack with `systemd` so you can start/stop in/from the background:

1.  Edit the `/etc/systemd/system/redis-stack-server.service` file and enter the following information:
    
    ```text
    [Unit]
    Description=Redis Stack Server
    After=network.target
    
    [Service]
    ExecStart=/usr/bin/snap run redis-stack-server
    Restart=always
    User=root
    Group=root
    
    [Install]
    WantedBy=multi-user.target
    ```
    
2.  Run the following commands.
    
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start redis-stack-server
    sudo systemctl enable redis-stack-server
    ```
    

If your Linux distribution does not currently have Snap installed, you can install it using the instructions described [here](https://snapcraft.io/docs/installing-snapd). Then, download the appropriate from the [downloads page](https://redis.io/downloads/).

## On Ubuntu with AppImage

Fuse needs to be installed before proceeding. Install it as follows.

```bash
sudo apt update
sudo apt install fuse
```

Next, download the latest Redis Stack AppImage package from [this page](https://redis.io/downloads/).

To run the image, execute these commands:

```bash
sudo apt update
sudo apt install redis-tools
chmod a+x <AppImageFile> # replace AppImageFile with the name of your downloaded file
./<AppImageFile>
```

This will start Redis in the foreground. To stop Redis, enter `Ctrl-C`.

Follow these steps to integrate Redis Stack with `systemd` so you can start/stop in/from the background:

1.  Edit the `/etc/systemd/system/redis-appimage.service` file and enter the following information:
    
    ```text
    [Unit]
    Description=Redis Server (AppImage)
    After=network.target
    
    [Service]
    ExecStart=/path/to/your/<AppImageFile> --daemonize no
    Restart=always
    User=redis-user   # replace with an existing user or create a new one
    Group=redis-group # replace with an existing group or create a new one
    
    [Install]
    WantedBy=multi-user.target
    ```
    
2.  Run the following commands.
    
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start redis-appimage
    sudo systemctl enable redis-appimage
    ```
    

## Starting and stopping Redis Stack in the background

You can start the Redis server as a background process using the `systemctl` command. This only applies to Ubuntu/Debian when installed using `apt`, and Red Hat/Rocky when installed using `yum`.

```bash
sudo systemctl start redis-stack-server
```

To stop the service, use:

```bash
sudo systemctl stop redis-stack-server
```

## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:

```bash
redis-cli
```

Test the connection with the `ping` command:

```bash
127.0.0.1:6379> ping
PONG
```

You can also test that your Redis server is running using [Redis Insight](/docs/latest/develop/tools/insight/).

## Next steps

Once you have a running Redis instance, you may want to:

*   Try the [Redis CLI tutorial](/docs/latest/develop/tools/cli/)
*   Connect using one of the [Redis clients](/docs/latest/develop/clients/)
*   [Install Redis properly](/docs/latest/operate/oss_and_stack/install/archive/install-redis/#install-redis-properly) for production use.

## On this page
