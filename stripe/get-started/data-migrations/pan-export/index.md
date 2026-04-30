---
title: "Request a payment data export"
source: "https://docs.stripe.com/get-started/data-migrations/pan-export"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:39:40.159Z"
content_hash: "2d12af767900cbaf5f626a79b83c496322b7bb37b26105890f0bcc04d58fe10f"
---

## Securely export sensitive payment data.

We believe our customers own the sensitive data they entrust to Stripe. We make sure that you have access to this data—even if you’re moving elsewhere. If you decide to leave Stripe for another payment processor, we’ll work with your new processor’s team to securely transfer your credit card data.

To meet [PCI compliance](https://docs.stripe.com/security/guide#validating-pci-compliance) obligations, we can only transfer your card data to another PCI DSS Level 1-compliant payment processor. Stripe requires the following information about the processor receiving the data:

*   The processor’s current PCI Attestation of Compliance (AOC), or their listing on [Visa’s Global Registry of Service Providers](https://usa.visa.com/splisting/splistingindex.html).
    
*   The processor’s PGP public encryption key, which must be 4096 bits or greater in length. This key must be hosted over HTTPS on one of the processor’s domain names referenced in their AOC or Visa Registry listing.
    

After you [let us know](https://support.stripe.com/contact?email=true&subject=Migration+away+from+Stripe) who your new payment processor is, we can usually confirm if they meet these requirements.

#### Link transactions

You can’t transfer the payment credentials saved with Link between payment processors. We exclude any credentials saved through Link from our exports.

## Migratable data

Stripe can help you migrate your customer card information to a new payment processor. To do this securely, Stripe prepares an encrypted JSON export file containing your data, including the card details of your customers, email addresses, and any attached [metadata](https://docs.stripe.com/api#metadata). We then arrange a secure transfer with your new processor, who uses this file to import the data into their system. You can start the migration process by [contacting us](https://support.stripe.com/contact?email=true&subject=Migration+away+from+Stripe) with the name of your new payment processor.

`{   "customers": [     {       "id": "cus_abc123def456",       "email": "jenny.rosen@example.com",       "description": "Jenny Rosen",       "default_source": "card_edf214abc789",       "metadata": {         "color_preference": "turquoise",         ...       },       "cards": [         {           "id": "card_edf214abc789",           "number":"4242424242424242",           "name": "Jenny Rosen",           "exp_month": 1,           "exp_year": 2020,           "address_line1": "123 Main St.",           "address_line2": null,           "address_city": "Springfield",           "address_state": "MA",           "address_zip": "01101",           "address_country": "US"         },         ...       ]     },     ...   ] }`

Stripe doesn’t export your account’s payment history, subscriptions, or other objects. Instead, use the API or Dashboard to retrieve this information. You can continue to access your data through the Dashboard and API after you stop processing payments with us, as long as you don’t close or delete your account.
