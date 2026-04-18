---
title: "Vault"
source: "https://supabase.com/docs/guides/database/vault"
canonical_url: "https://supabase.com/docs/guides/database/vault"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:48.278Z"
content_hash: "9093fd8fdad05a352f053e97d7ca2ff5f497f7e9f059c816f69c966fde2bb0db"
menu_path: ["Database","Database","Access and security","Access and security","Managing secrets with Vault","Managing secrets with Vault"]
section_path: ["Database","Database","Access and security","Access and security","Managing secrets with Vault","Managing secrets with Vault"]
---
# 

Vault

## 

Managing secrets in Postgres.

* * *

Vault is a Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and other data in your database. This opens up a lot of possibilities to use Postgres in ways that go beyond what is available in a stock distribution.

Under the hood, the Vault is a table of Secrets that are stored using [Authenticated Encryption](https://en.wikipedia.org/wiki/Authenticated_encryption) on disk. They are then available in decrypted form through a Postgres view so that the secrets can be used by applications from SQL. Because the secrets are stored on disk encrypted and authenticated, any backups or replication streams also preserve this encryption in a way that can't be decrypted or forged.

Supabase provides a dashboard UI for the Vault that makes storing secrets easy. Click a button, type in your secret, and save.

You can use Vault to store secrets - everything from Environment Variables to API Keys. You can then use these secrets anywhere in your database: Postgres [Functions](/docs/guides/database/functions), Triggers, and [Webhooks](/docs/guides/database/webhooks). From a SQL perspective, accessing secrets is as easy as querying a table (or in this case, a view). The underlying secrets tables will be stored in encrypted form.

## Using Vault[#](#using-vault)

You can manage secrets from the UI or using SQL.

### Adding secrets[#](#adding-secrets)

There is also a handy function for creating secrets called `vault.create_secret()`:

```
1select vault.create_secret('my_s3kre3t');
```

The function returns the UUID of the new secret.

Show Result

```
1-[ RECORD 1 ]-+-------------------------------------2create_secret | c9b00867-ca8b-44fc-a81d-d20b8169be17
```

Secrets can also have an optional _unique_ name and an optional description. These are also arguments to `vault.create_secret()`:

```
1select vault.create_secret('another_s3kre3t', 'unique_name', 'This is the description');
```

Show Result

```
1-[ RECORD 1 ]-----------------------------------------------------------------2id          | 7095d222-efe5-4cd5-b5c6-5755b451e2233name        | unique_name4description | This is the description5secret      | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=6key_id      |7nonce       | \x9f2d60954ba5eb566445736e0760b0e38created_at  | 2022-12-14 02:34:23.85159+009updated_at  | 2022-12-14 02:34:23.85159+00
```

### Viewing secrets[#](#viewing-secrets)

If you look in the `vault.secrets` table, you will see that your data is stored encrypted. To decrypt the data, there is an automatically created view `vault.decrypted_secrets`. This view will decrypt secret data on the fly:

```
1select * 2from vault.decrypted_secrets 3order by created_at desc 4limit 3;
```

Show Result

```
1-[ RECORD 1 ]----+-----------------------------------------------------------------2id               | 7095d222-efe5-4cd5-b5c6-5755b451e2233name             | unique_name4description      | This is the description5secret           | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=6decrypted_secret | another_s3kre3t7key_id           |8nonce            | \x9f2d60954ba5eb566445736e0760b0e39created_at       | 2022-12-14 02:34:23.85159+0010updated_at       | 2022-12-14 02:34:23.85159+0011-[ RECORD 2 ]----+-----------------------------------------------------------------12id               | c9b00867-ca8b-44fc-a81d-d20b8169be1713name             |14description      |15secret           | a1CE4vXwQ53+N9bllJj1D7fasm59ykohjb7K90PPsRFUd9IbBdxIGZNoSQLIXl4=16decrypted_secret | another_s3kre3t17key_id           |18nonce            | \x1d3b2761548c4efb2d29ca11d44aa22f19created_at       | 2022-12-14 02:32:50.58921+0020updated_at       | 2022-12-14 02:32:50.58921+0021-[ RECORD 3 ]----+-----------------------------------------------------------------22id               | d91596b8-1047-446c-b9c0-66d98af6d00123name             |24description      |25secret           | S02eXS9BBY+kE3r621IS8beAytEEtj+dDHjs9/0AoMy7HTbog+ylxcS22A==26decrypted_secret | s3kre3t_k3y27key_id           |28nonce            | \x3aa2e92f9808e496aa4163a59304b89529created_at       | 2022-12-14 02:29:21.3625+0030updated_at       | 2022-12-14 02:29:21.3625+00
```

Notice how this view has a `decrypted_secret` column that contains the decrypted secrets. Views are not stored on disk, they are only run at query time, so the secret remains encrypted on disk, and in any backup dumps or replication streams.

You should ensure that you protect access to this view with the appropriate SQL privilege settings at all times, as anyone that has access to the view has access to decrypted secrets.

### Updating secrets[#](#updating-secrets)

A secret can be updated with the `vault.update_secret()` function, this function makes updating secrets easy, just provide the secret UUID as the first argument, and then an updated secret, updated optional unique name, or updated description:

```
1select2  vault.update_secret(3    '7095d222-efe5-4cd5-b5c6-5755b451e223',4    'n3w_upd@ted_s3kret',5    'updated_unique_name',6    'This is the updated description'7  );
```

Show Result

```
1-[ RECORD 1 ]-+-2update_secret |34postgres=> select * from vault.decrypted_secrets where id = '7095d222-efe5-4cd5-b5c6-5755b451e223';5-[ RECORD 1 ]----+---------------------------------------------------------------------6id               | 7095d222-efe5-4cd5-b5c6-5755b451e2237name             | updated_unique_name8description      | This is the updated description9secret           | lhb3HBFxF+qJzp/HHCwhjl4QFb5dYDsIQEm35DaZQOovdkgp2iy6UMufTKJGH4ThMrU=10decrypted_secret | n3w_upd@ted_s3kret11key_id           |12nonce            | \x9f2d60954ba5eb566445736e0760b0e313created_at       | 2022-12-14 02:34:23.85159+0014updated_at       | 2022-12-14 02:51:13.938396+00
```

## Deep dive[#](#deep-dive)

As we mentioned, Vault uses Transparent Column Encryption (TCE) to store secrets in an authenticated encrypted form. There are some details around that you may be curious about. What does authenticated mean? Where is the encryption key stored? This section explains those details.

### Authenticated encryption with associated data[#](#authenticated-encryption-with-associated-data)

The first important feature of TCE is that it uses an [Authenticated Encryption with Associated Data](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data_\(AEAD\)) encryption algorithm (based on `libsodium`).

### Encryption key location[#](#encryption-key-location)

**Authenticated Encryption** means that in addition to the data being encrypted, it is also signed so that it cannot be forged. You can guarantee that the data was encrypted by someone you trust, which you wouldn't get with encryption alone. The decryption function verifies that the signature is valid _before decrypting the value_.

**Associated Data** means that you can include any other columns from the same row as part of the signature computation. This doesn't encrypt those other columns - rather it ensures that your encrypted value is only associated with columns from that row. If an attacker were to copy an encrypted value from another row to the current one, the signature would be rejected (assuming you used a unique column in the associated data).

Another important feature is that the encryption key is never stored in the database alongside the encrypted data. Even if an attacker can capture a dump of your entire database, they will see only encrypted data, _never the encryption key itself_.

This is an important safety precaution - there is little value in storing the encryption key in the database itself as this would be like locking your front door but leaving the key in the lock! Storing the key outside the database fixes this issue.

Where is the key stored? Supabase creates and manages the encryption key in our secured backend systems. We keep this key safe and separate from your data. You remain in control of your key - a separate API endpoint is available that you can use to access the key if you want to decrypt your data outside of Supabase.

Which roles should have access to the `vault.secrets` table should be carefully considered. There are two ways to grant access, the first is that the `postgres` user can explicitly grant access to the vault table itself.

### Resources[#](#resources)

*   Read more about Supabase Vault in the [blog post](/blog/vault-now-in-beta)
*   [Supabase Vault on GitHub](https://github.com/supabase/vault)
*   [Column Encryption](/docs/guides/database/column-encryption)
