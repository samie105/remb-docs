---
title: "Default user"
source: "https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user/"
canonical_url: "https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:03.405Z"
content_hash: "e49ba303a8225031ac40f37cdaec27a01c02ea8bf9eed9dbc66e3963b00c7bb2"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Security","→","Security","→\n      \n        Access control","→","Access control","→\n      \n        Data access control","→","Data access control","→\n      \n        Default user","→","Default user"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Security","→","Security","→\n      \n        Access control","→","Access control","→\n      \n        Data access control","→","Data access control","→\n      \n        Default user","→","Default user"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/debugging/index.md", "title": "Debugging"}
nav_next: {"path": "redis/docs/latest/integrate/google-adk/examples/index.md", "title": "adk-redis examples"}
---

# Default user

Learn how to change your default user password or turn off access using the default user password.

Redis Cloud

Password-based authentication is a basic but essential Redis security feature. When you create a Redis Cloud database, your database is given a randomly generated password called the **Default user password**.

This password appears in the **Security** section of the **Configuration** tab of the database details screen.

[![The Default user password appears in the Security section of the Configuration tab on the database details screen.](/docs/latest/images/rc/database-fixed-configuration-security.png)](/docs/latest/images/rc/database-fixed-configuration-security.png)

Use the copy button to copy the password to the clipboard:

[![Use the Copy button to copy the default user password.](/docs/latest/images/rc/button-copy.png)](/docs/latest/images/rc/button-copy.png)

You'll need to use this password whenever you connect to your database using a Redis client. See [Connect to a database](/docs/latest/operate/rc/databases/connect/) for more info.

If you have [blocked the public endpoint](/docs/latest/operate/rc/security/database-security/block-public-endpoints/) for your Redis Cloud Pro subscription, you can also turn on passwordless authentication for the default user. See [Block public endpoints](/docs/latest/operate/rc/security/database-security/block-public-endpoints/#turn-on-passwordless-authentication-for-the-default-user) for more info.

See your [Redis client's documentation](/docs/latest/develop/clients/) to learn how to provide your password when connecting.

## Change password

To change the default user password for your database:

1.  From the database **Configuration** tab, select **Edit**.
    
    [![The Edit button lets you change the database's default user password.](/docs/latest/images/rc/button-database-edit.png)](/docs/latest/images/rc/button-database-edit.png)
2.  Under the **Security** section, enter the new password in the **Default user password** field. Database passwords must be less than 50 characters long.
    
3.  Select **Save database** to update the password.
    
    [![Use the Save database button to save the new password.](/docs/latest/images/rc/button-database-save.png)](/docs/latest/images/rc/button-database-save.png)

## Turn off default user

After you set up [role-based access control](/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control/) to limit who can access your database, we recommend that you turn off default user access.

To turn off the default user for a database:

1.  From the database **Configuration** tab, select **Edit**.
    
    [![The Edit database button lets you change the database's default user password.](/docs/latest/images/rc/button-database-edit.png)](/docs/latest/images/rc/button-database-edit.png)
2.  Under the **Security** section, select the **Default User** switch to turn it off.
    
3.  Select **Save database**.
    
    [![Use the Save database button to save the new password.](/docs/latest/images/rc/button-database-save.png)](/docs/latest/images/rc/button-database-save.png)

## On this page


