---
title: "Export file formats"
source: "https://docs.stripe.com/get-started/data-migrations/export-file-formats"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:38:42.259Z"
content_hash: "f3cf9efc88cf658cf992759469aa5da013850f9d783935bd81ca1ff40cf19664"
---

## Review the exported data for different payment types.

Stripe won’t change our export format. New processors can filter, map, and adjust the format of export files as needed. Our standard service level agreement (SLA) is 10 days to complete an export after we receive all valid data (excluding BACS).

We export ACH, SEPA, BACS, and PADs/ACSS as a CSV. We can also export card data in both CSV and JSON formats.

## Card export fields

Card exports include the following fields.

*   CSV exports don’t include unique metadata fields by default, but we can include them if you provide an exact list of field names.
*   Small JSON exports include the customer metadata by default.

Field

Description

`description`

Text attached to the customer object

`name`

Name associated with the customer

`email`

Customer’s email

`id`

Stripe unique identifier of the customer (cus\_XXXXX format)

`card.address_city`

City associated with the card

`card.address_country`

Country associated with the card

`card.address_line1`

First address line associated with the card

`card.address_line2`

Second address line associated with the card

`card.address_state`

State or province associated with the card

`card.address_zip`

Postal code associated with the card

`card.exp_month`

The month the card expires

`card.exp_year`

The year the card expires

`card.id`

The Stripe card ID object (card\_XXXXX format)

`card.name`

Customer’s name on the card

`card.number`

The PAN (credit card number)

`default_source`

Stripe object associated with the customer’s default payment method (could be card\_ID, pm\_ID, src\_ID, or ba\_ID)

`card.transaction_ids`

Network transaction ID status for SCA compliance

### Example card data export

DESCRIPTION

NAME

EMAIL

ID

CARD.ADDRESS\_CITY

CARD.ADDRESS\_COUNTRY

CARD.ADDRESS\_LINE1

CARD.ADDRESS\_LINE2

CARD.ADDRESS\_STATE

CARD.ADDRESS\_ZIP

CARD.EXP\_MONTH

CARD.EXP\_YEAR

CARD.ID

CARD.NAME

CARD.NUMBER

DEFAULT\_SOURCE

CARD.TRANSACTION\_IDS

User description

Stripey McStripe

test@example.com

cus\_JeGmWqYRVUNu44

Anytown

US

101 1st Ave

Apt 1

CA

90210

9

2021

card\_1J0yEyH65PkfON7E6pXEeoyZ

Stripey McStripe

5555551BT8Gs4444

card\_1J0yEyH65PkfON7EQ0Owsy3Q

012345678901234

User description

Stripey McStripe

test@example.com

cus\_JeGmWqYRVUNu44

Anytown

US

101 1st Ave

Apt 1

CA

90210

9

2021

card\_1J0yEyH65PkfON7EQ0Owsy3Q

Stripey McStripe

424242TPSa0L4242

card\_1J0yEyH65PkfON7EQ0Owsy3Q

012345678901234

User description

Stripey McStripe

test@example.com

cus\_JeGmJLltEqM9jd

Anytown

US

101 1st Ave

Apt 1

CA

90210

9

2021

card\_1J0yEyH65PkfON7EzGiGLo9c

Stripey McStripe

424242TPSa0L4242

card\_1J0yEyH65PkfON7EzGiGLo9c

012345678901234

User description

Stripey McStripe

test@example.com

cus\_JeGmdHOz48B3XA

Anytown

US

101 1st Ave

Apt 1

CA

90210

9

2021

card\_1J0yExH65PkfON7E7ZHA0keF

Stripey McStripe

424242TPSa0L4242

card\_1J0yExH65PkfON7E7ZHA0keF

012345678901234

## ACH Export Fields

ACH exports include the following fields.

Field

Description

`customer_id`

Stripe unique identifier of the customer (cus\_XXXXX format)

`customer_created`

Date that the customer object was created in Stripe

`email`

Customer’s email

`description`

Description text attached to the customer object

`default_source`

Stripe object associated with the customer’s default payment method (could be card\_ID, pm\_ID, src\_ID, or ba\_ID)

`bank_account_id`

The Stripe bank account object ID (ba\_XXXXX format)

`routing_number`

Bank routing number

`account_number`

Customer’s bank account number

`account_holder_name`

Customer name associated with the bank account

`account_holder_type`

Boolean value that marks whether the account is owned by an individual or company

`country`

Country associated with the bank account

`use`

Enum value identifying the account type as either `checking` or `savings`

### Example ACH data export

customer\_id

customer\_created

name

email

description

default\_source

bank\_account\_id

routing\_number

account\_number

account\_holder\_name

account\_holder\_type

country

use

cus\_JdW0ZauDFfHkfi

2021-06-09T00:08:59.062Z

Stripey McStripe

test@example.com

User description

ba\_1J0EydH65PkfON7EQIkjVJUb

ba\_1J0EydH65PkfON7EQIkjVJUb

110000000

000123456789

Stripey McStripe

individual

US

checking

cus\_JdW0wbOcikkCIK

2021-06-09T00:08:59.659Z

Stripey McStripe

test@example.com

User description

ba\_1J0EydH65PkfON7EuWIUgHnw

ba\_1J0EydH65PkfON7EuWIUgHnw

110000000

000123456789

Stripey McStripe

individual

US

checking

cus\_JdW05ASZDyr9mS

2021-06-09T00:09:00.161Z

Stripey McStripe

test@example.com

User description

ba\_1J0EyeH65PkfON7E98oBUhwD

ba\_1J0EyeH65PkfON7E98oBUhwD

110000000

000123456789

Stripey McStripe

individual

US

checking

cus\_JdW02JwM87cx9r

2021-06-09T00:09:00.711Z

Stripey McStripe

test@example.com

User description

ba\_1J0EyeH65PkfON7EfaUw4Exc

ba\_1J0EyeH65PkfON7EfaUw4Exc

110000000

000123456789

Stripey McStripe

individual

US

checking

cus\_JdW02JwM87cx9r

2021-06-09T00:09:00.711Z

Stripey McStripe

test@example.com

User description

ba\_1J0EyeH65PkfON7EfaUw4Exc

ba\_1J0EyfH65PkfON7EyHeoTbF9

110000000

000444444440

Stripey McStripe

individual

US

checking

## SEPA export fields

SEPA exports include the following fields.

Field

Description

`customer_id`

Stripe unique identifier of the customer (cus\_XXXXX format)

`email`

Customer’s email

`description`

Description text attached to the customer object

`source_id`

Stripe source ID associated with the customer’s payment method

`payment_method_id`

Stripe payment method ID associated with the customer’s payment method

`owner_name`

Customer name associated with the direct debit account

`iban`

IBAN associated with the mandate

`mandate_reference`

Unique identifier of the direct debit mandate on Stripe

`currency`

Currency associated with the payment method

### Example SEPA data export

CUSTOMER\_ID

EMAIL

DESCRIPTION

SOURCE\_ID

PAYMENT\_METHOD\_ID

OWNER\_NAME

IBAN

MANDATE\_REFERENCE

CURRENCY

cus\_111111111

test@example.com

Description1

src\_1111111

Stripey McStripe

GB22TESTBB20201555555555

mandate\_xxxx

eur

cus\_222222222

test@example.com

Description2

pm\_2222222

Rory O’D

DE22TESTBB20201555555555

mandate\_yyyy

eur

cus\_333333333

test2@example.com

Description3

pm\_3333333

Frankie C

IE22TESTBB20201555555555

mandate\_zzzz

eur

## UK Bacs export fields

UK Bacs exports include the following fields.

Field

Description

`merchant`

The unique identifier of the Stripe account we’re exporting from (acct\_XXXXX format)

`customer_id`

The Stripe unique identifier of the customer (cus\_XXXXX format)

`bacs_id`

Stripe payment method object associated with the customer’s direct debit mandate (in the format pm\_XXXXX)

`mandate_reference`

Unique identifier of the direct debit mandate on Stripe

`sort_code`

Customer’s bank account sort code (6 digits in length and might include leading zeros)

`account_number`

Customer’s bank account number (8 digits in length and might include leading zeros)

`effective_date`

Date the mandate was activated on Stripe

`recipient_name`

Customer’s name on the bank account

`recipient_address_street`

Customer’s street address associated with the customer’s bank account

`recipient_address_city`

Customer’s city address associated with the customer’s bank account

`recipient_address_state`

Customer’s state address associated with the customer’s bank account

`recipient_address_zip`

Customer’s postal code associated with their bank account

`recipient_address_country`

Country associated with the bank account

### Example BACS data export

MERCHANT

CUSTOMER\_ID

BACS\_ID

MANDATE\_REFERENCE

TOKEN

SORT\_CODE

ACCOUNT\_NUMBER

EFFECTIVE\_DATE

RECIPIENT\_\_NAME

RECIPIENT\_\_ADDRESS\_\_STREET

RECIPIENT\_\_ADDRESS\_\_CITY

RECIPIENT\_\_ADDRESS\_\_STATE

RECIPIENT\_\_ADDRESS\_\_ZIP

RECIPIENT\_\_ADDRESS\_\_COUNTRY

acct\_111111

cus\_1111

pm\_111

xxx\*USER

xxx\*USER

111111

11111111

2022_06_09T00:00:00Z

JOHN DOE

25 Avenue

LONDON

LONDON

EXXXXX

GB

acct\_111111

cus\_2222

pm\_222

yyy\*USER

yyy\*USER

111111

11111111

2022_06_09T00:00:00Z

Stripe McStripe

26 Street

LONDON

LONDON

EXXXXX

GB

acct\_111111

cus\_3333

pm\_333

zzz\*USER

zzz\*USER

111111

11111111

2022_06_09T00:00:00Z

Rory C

27 Way

LONDON

LONDON

EXXXXX

GB

## AU BECS export fields

AU BECS exports include the following fields.

Field

Description

`customer_id`

The Stripe unique identifier of the customer (cus\_XXXXX format)

`name`

Name associated with the customer

`email`

Customer’s email

`description`

Text attached to the customer object

`source_id`

Stripe payment method ID associated with the customer’s payment method

`owner_name`

Customer name associated with the bank account

`bsb_number`

The 6 digit bank state branch number of the bank account

`account_number`

Customer’s bank account number

### Example AU BECS data export

CUSTOMER\_ID

NAME

EMAIL

DESCRIPTION

SOURCE\_ID

OWNER\_NAME

BSB\_NUMBER

ACCOUNT\_NUMBER

cus\_1111

JOHN DOE

test@example.com

yyy\*USER

pm\_111

JOHN DOE

111111

21212121

cus\_2222

JANE SMITH

jane@example.com

xxx\*USER

pm\_222

JANE SMITH

222222

43434343

cus\_3333

ALEX JOHNSON

alex@example.com

zzz\*USER

pm\_333

ALEX JOHNSON

333333

65656565
