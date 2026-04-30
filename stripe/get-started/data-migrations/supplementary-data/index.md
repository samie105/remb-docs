---
title: "Upload supplementary  data"
source: "https://docs.stripe.com/get-started/data-migrations/supplementary-data"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:40:19.314Z"
content_hash: "b4ae3da93b4cbe87ac0ea8cccc9b838c77e36355f5d2e5ef96b01ecb14790000"
---

## Provide additional data to Stripe when migrating payment data.

## Data encryption

For PCI data such as credit data, make sure you first encrypt the data with the Stripe PGP key.

1.  If you’re unfamiliar with the OpenPGP standard used in these encryption steps, [download the GnuPG software](https://www.gnupg.org/).
    
    #### Note
    
    You can use Terminal or iTerm on Mac or Windows Terminal on PC instead for the command-line interface.
    
2.  Save the non-encrypted data file on your desktop.
    
3.  Zip the data file (we only support .zip or .tar.gz compression).
    
4.  [Download the Stripe public key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key) by copying and pasting the key into a .txt file. Save the .txt file with the filename **Stripe\_Import\_Key.txt** on your desktop.
    
5.  Add the key to your list of known keys using your command-line interface:
    
    1.  Navigate to your desktop: `cd ~/Desktop`.
    2.  Type the command: `gpg --import "Stripe Import Key"`.
    3.  Confirm the output matches:
    
    `cd ~/Desktop  gpg --import Stripe_Import_Key.txt gpg: key 9C78B7620C1E99AD: public key "Stripe Import Key (PCI) <support-migrations@stripe.com>" imported gpg: Total number processed: 1 gpg:               imported: 1`
    
6.  Verify the key with the command: `gpg --list-keys`.
    
7.  Encrypt the non-encrypted data file with that key: `gpg --recipient "Stripe Import Key (PCI)" --encrypt 20240418_rocket_rides_cards.csv`. The action returns an encrypted GPG file, such as **20240418\_rocket\_rides\_cards.csv.gpg**. The output looks like:
    
    `gpg --recipient "Stripe Import Key (PCI)" --encrypt 20240418_rocket_rides_cards.csv  gpg: 8A3B0AC7944266D9: There is no assurance this key belongs to the named user  sub  rsa4096/8A3B0AC7944266D9 2023-04-11 Stripe Import Key (PCI) <support-migrations@stripe.com>      Primary key fingerprint: AEBF 7C48 38C4 4D2F DC99  A3F9 9C78 B762 0C1E 99AD      Subkey fingerprint: 2100 F77A 7937 9D29 9C96  420B 8A3B 0AC7 9442 66D9  It is NOT certain that the key belongs to the person named in the user ID. If you *really* know what you are doing, you may answer the next question with yes.  Use this key anyway? (y/N) y`
    

## Upload your encrypted file

The Stripe Data Migration team securely emails or texts your SFTP access credentials to you. You must log into your Stripe account and submit your migration request using the [secure intake request form](https://support.stripe.com/contact/email?topic=migrations) to obtain access credentials.

1.  Save the file to upload on your desktop.
    
2.  Navigate to the desktop in your command-line: `cd ~/Desktop`.
    
3.  Connect to the Stripe SFTP server with the command: `sftp -P 22 <username>@sftp.stripe.com` (where `<username>` is the username provided by the Stripe Data Migrations Team).
    
4.  Provide your password when prompted, then press **Enter**.
    
5.  Upload the file to the SFTP account with the command: `put <file name>`, where `<file name>` is the name of the data file to upload, such as `20240418_rocket_rides_cards.csv.gpg`.
    
6.  After you upload the file, you might not see the file in the folder, though it transferred successfully. You can view a successful status file under the upload-success directory.
    
    `sftp -P 22 username@sftp.stripe.com   username@sftp.stripe.com's password: Connected to sftp.stripe.com. sftp> put 20240418_rocket_rides_cards.csv.gpg Uploading 20240418_rocket_rides_cards.csv.gpg to /20240418_rocket_rides_cards.csv.gpg  20240418_rocket_rides_cards.csv.gpg                                                                  100%  663    26.5KB/s   00:00`
