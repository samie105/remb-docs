---
title: "Run Bun as a daemon with systemd"
source: "https://bun.com/docs/guides/ecosystem/systemd"
canonical_url: "https://bun.com/docs/guides/ecosystem/systemd"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:53.932Z"
content_hash: "d968957851af253270b1fc2c7104c51cb8707533cecb1f3fd133ae60eafea940"
menu_path: ["Run Bun as a daemon with systemd"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/sveltekit/index.md", "title": "Build an app with SvelteKit and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/upstash/index.md", "title": "Bun Redis with Upstash"}
---

# describe the app
Description=My App
# start the app after the network is available
After=network.target

[Service]
# usually you'll use 'simple'
# one of https://www.freedesktop.org/software/systemd/man/systemd.service.html#Type=
Type=simple
# which user to use when starting the app
User=YOUR_USER
# path to your application's root directory
WorkingDirectory=/home/YOUR_USER/path/to/my-app
# the command to start the app
# requires absolute paths
ExecStart=/home/YOUR_USER/.bun/bin/bun run index.ts
# restart policy
# one of {no|on-success|on-failure|on-abnormal|on-watchdog|on-abort|always}
Restart=always

[Install]
# start the app automatically
WantedBy=multi-user.target
```

* * *

If your application starts a webserver, note that non-`root` users are not able to listen on ports 80 or 443 by default. To permanently allow Bun to listen on these ports when executed by a non-`root` user, use the following command. This step isn’t necessary when running as `root`.

terminal

```
setcap CAP_NET_BIND_SERVICE=+eip ~/.bun/bin/bun
```

* * *

With the service file configured, you can now _enable_ the service. Once enabled, it will start automatically on reboot. This requires `sudo` permissions.

terminal

```
systemctl enable my-app
```

* * *

To start the service without rebooting, you can manually _start_ it.

terminal

```
systemctl start my-app
```

* * *

Check the status of your application with `systemctl status`. If you’ve started your app successfully, you should see something like this:

terminal

```
systemctl status my-app
```

```
● my-app.service - My App
     Loaded: loaded (/lib/systemd/system/my-app.service; enabled; preset: enabled)
     Active: active (running) since Thu 2023-10-12 11:34:08 UTC; 1h 8min ago
   Main PID: 309641 (bun)
      Tasks: 3 (limit: 503)
     Memory: 40.9M
        CPU: 1.093s
     CGroup: /system.slice/my-app.service
             └─309641 /home/YOUR_USER/.bun/bin/bun run /home/YOUR_USER/application/index.ts
```

* * *

To update the service, edit the contents of the service file, then reload the daemon.

terminal

```
systemctl daemon-reload
```

* * *

For a complete guide on the service unit configuration, you can check [this page](https://www.freedesktop.org/software/systemd/man/systemd.service.html). Or refer to this cheatsheet of common commands:

terminal

```
systemctl daemon-reload # tell systemd that some files got changed
systemctl enable my-app # enable the app (to allow auto-start)
systemctl disable my-app # disable the app (turns off auto-start)
systemctl start my-app # start the app if is stopped
systemctl stop my-app # stop the app
systemctl restart my-app # restart the app
```

