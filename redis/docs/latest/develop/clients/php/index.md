---
title: "Predis guide (PHP)"
source: "https://redis.io/docs/latest/develop/clients/php/"
canonical_url: "https://redis.io/docs/latest/develop/clients/php/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:38.032Z"
content_hash: "eead975363cc8f29ba0f93b7b02b7e0b179b782a1b4b1c1d37a753213e6ebc97"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Predis guide (PHP)","→","Predis guide (PHP)"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Predis guide (PHP)","→","Predis guide (PHP)"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/management/optimization/index.md", "title": "Optimizing Redis"}
nav_next: {"path": "redis/docs/latest/develop/clients/nodejs/produsage/index.md", "title": "Production usage"}
---

# Predis guide (PHP)

Connect your PHP application to a Redis database

[`Predis`](https://github.com/predis/predis) is the recommended [PHP](https://php.net/) client for Redis. The sections below explain how to install `Predis` and connect your application to a Redis database.

Note:

Although we provide basic documentation for `Predis`, it is a third-party client library and is not developed or supported directly by Redis.

`Predis` requires a running Redis server. See [here](/docs/latest/operate/oss_and_stack/install/) for Redis Open Source installation instructions.

## Install

Use [Composer](https://getcomposer.org/) to install the `Predis` library with the following command line:

```bash
composer require predis/predis
```

## Connect and test

Connect to a locally-running server on the standard port (6379) with the following code:

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

$r = new PredisClient([
                'scheme'   => 'tcp',
                'host'     => '127.0.0.1',
                'port'     => 6379,
                'password' => '',
                'database' => 0,
            ]);

echo $r->set('foo', 'bar'), PHP_EOL;
// >>> OK

echo $r->get('foo'), PHP_EOL;
// >>> bar

$r->hset('user-session:123', 'name', 'John');
$r->hset('user-session:123', 'surname', 'Smith');
$r->hset('user-session:123', 'company', 'Redis');
$r->hset('user-session:123', 'age', 29);

echo var_export($r->hgetall('user-session:123')), PHP_EOL;
/* >>>
array (
  'name' => 'John',
  'surname' => 'Smith',
  'company' => 'Redis',
  'age' => '29',
)
*/
```

Store and retrieve a simple string to test the connection:

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

$r = new PredisClient([
                'scheme'   => 'tcp',
                'host'     => '127.0.0.1',
                'port'     => 6379,
                'password' => '',
                'database' => 0,
            ]);

echo $r->set('foo', 'bar'), PHP_EOL;
// >>> OK

echo $r->get('foo'), PHP_EOL;
// >>> bar

$r->hset('user-session:123', 'name', 'John');
$r->hset('user-session:123', 'surname', 'Smith');
$r->hset('user-session:123', 'company', 'Redis');
$r->hset('user-session:123', 'age', 29);

echo var_export($r->hgetall('user-session:123')), PHP_EOL;
/* >>>
array (
  'name' => 'John',
  'surname' => 'Smith',
  'company' => 'Redis',
  'age' => '29',
)
*/
```

Store and retrieve a [hash](/docs/latest/develop/data-types/hashes/) object:

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

$r = new PredisClient([
                'scheme'   => 'tcp',
                'host'     => '127.0.0.1',
                'port'     => 6379,
                'password' => '',
                'database' => 0,
            ]);

echo $r->set('foo', 'bar'), PHP_EOL;
// >>> OK

echo $r->get('foo'), PHP_EOL;
// >>> bar

$r->hset('user-session:123', 'name', 'John');
$r->hset('user-session:123', 'surname', 'Smith');
$r->hset('user-session:123', 'company', 'Redis');
$r->hset('user-session:123', 'age', 29);

echo var_export($r->hgetall('user-session:123')), PHP_EOL;
/* >>>
array (
  'name' => 'John',
  'surname' => 'Smith',
  'company' => 'Redis',
  'age' => '29',
)
*/
```

## More information

The [Predis wiki on Github](https://github.com/predis/predis/wiki) has information about the different connection options you can use.

See also the pages in this section for more information and examples:

## On this page

