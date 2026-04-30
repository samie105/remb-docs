---
title: "File upload guide"
source: "https://docs.stripe.com/file-upload"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:51:35.622Z"
content_hash: "8bef2ab224d689bd5a9a5973f2bc6720cb5810969a2522830b417e4dfc88a004"
---

When you upload a file to Stripe using the API, it returns a file token and other information about the file. You can then use the token in other API calls. This guide describes this process.

## Upload a file

To upload a file, send a `multipart/form-data` request to **https://files.stripe.com/v1/files**. The subdomain **files.stripe.com** is different than most Stripe API endpoints. Specify a `purpose` and a `file` in the request. The following example uploads a file located at **/path/to/a/file.jpg** on your local file system with the purpose `dispute_evidence`:

`curl https://files.stripe.com/v1/files \   -u` 

`sk_test_REDACTED`

`: \   -F "file"="@/path/to/a/file.jpg" \   -F "purpose"="dispute_evidence"`

The following example uploads a file using our Android SDK with the purpose `dispute_evidence`:

`class CheckoutActivity : AppCompatActivity() {     private val stripe: Stripe by lazy {         Stripe(this,` 

`"pk_test_REDACTED"`

`)     }      private fun uploadFile(file: File) {         stripe.createFile(             StripeFileParams(                 file,                 StripeFilePurpose.DisputeEvidence             ),             callback = object : ApiResultCallback<StripeFile> {                 override fun onSuccess(result: StripeFile) {                     // File upload succeeded                 }                  override fun onError(e: Exception) {                     // File upload failed                 }              }         )     } }`

There are [several valid purpose](https://docs.stripe.com/api#create_file-purpose) values, each with file format and size requirements.

Purpose

Description

Supported mimetypes

Max size

Expiry

Downloadable

`account_requirement`

Additional documentation requirements that can be requested for an account.

PDF  
JPEG  
PNG  

64MB

NEVER

No

`business_icon`

A business icon.

JPEG  
PNG  
GIF  

512KB

NEVER

Yes

`business_logo`

A business logo.

JPEG  
PNG  
GIF  

512KB

NEVER

Yes

`customer_signature`

Customer signature image.

JPEG  
PNG  
SVG  

4MB

7 days

Yes

`dispute_evidence`

Evidence to submit with a dispute response.

PDF  
JPEG  
PNG  

5MB

9 months

Yes

`platform_terms_of_service`

A copy of the platform's Terms of Service.

PDF  
TXT  
MARKDOWN  

64MB

NEVER

No

`issuing_regulatory_reporting`

Additional regulatory reporting requirements for Issuing.

JSON  

256KB

2 years

Yes

`pci_document`

A self-assessment PCI questionnaire.

PDF  

16MB

NEVER

Yes

`tax_document_user_upload`

A user-uploaded tax document.

PDF  
CSV  
JPEG  
PNG  
XLSX  
DOCX  

16MB

NEVER

Yes

`additional_verification`

Additional verification for custom accounts.

PDF  
JPEG  
PNG  

16MB

NEVER

No

`terminal_android_apk`

Android POS apps to be deployed on Stripe smart readers.

APK  

200MB

6 months

Yes

`terminal_reader_splashscreen`

Splashscreen to be displayed on Terminal readers.

PNG  
JPEG  
GIF  

4.194304MB

1 year

Yes

`terminal_wifi_certificate`

Certificate used for Enterprise WiFi on Terminal readers.

PEM  

100KB

NEVER

No

`terminal_wifi_private_key`

Private key used for Enterprise WiFi on Terminal readers.

PEM  

100KB

NEVER

No

`identity_document`

A document to verify the identity of an account owner during account provisioning.

PDF  
JPEG  
PNG  

32MB

NEVER

When uploaded by Connect platform

#### Caution

`identity_document` images also need to be smaller than 8,000px by 8,000px.

The MIME type of the file you want to upload must correspond to its file format.

File format

MIME type

APK

**application/vnd.android.package-archive**

CSV

**text/csv**

DOCX

**application/vnd.openxmlformats-officedocument.wordprocessingml.document**

GIF

**image/gif**

HTML

**text/html**

ICO

**image/vnd.microsoft.icon**

JPEG

**image/jpeg**

JSON

**application/json**

JSONL

**application/jsonl**

MARKDOWN

**text/markdown**

PDF

**application/pdf**

PEM

**application/x-pem-file**

PNG

**image/png**

SVG

**image/svg+xml**

TIFF

**image/tiff**

TSV

**text/tab-separated-values**

TXT

**text/plain**

WEBP

**image/webp**

XLS

**application/vnd.ms-excel**

XLSM

**application/vnd.ms-excel.sheet.macroEnabled.12**

XLSX

**application/vnd.openxmlformats-officedocument.spreadsheetml.sheet**

XML

**application/xml**

ZIP

**application/zip**

#### Caution

Any Microsoft Office documents containing VBA macros will be rejected because of security concerns.

A successful request returns a [File](https://docs.stripe.com/api/files/object) object.

## Retrieving a File API resource

To retrieve the API resource for a file, make a GET request to the **/v1/files** endpoint of the **files.stripe.com** subdomain providing the file upload ID:

`curl https://files.stripe.com/v1/files/`

`{{FILE_ID}}`

 `\   -u sk_test_REDACTED`

When using restricted API keys, you must receive prior access to the `Files` resource.

## Download the file contents

If the file purpose allows downloading the file contents, then the [file](https://docs.stripe.com/api/files/object) includes a non-null `url` field indicating how to access the contents. This url requires authentication with your Stripe API keys.

`curl https://files.stripe.com/v1/files/`

`{{FILE_ID}}`

`/contents   -u sk_test_REDACTED`

If you want unauthenticated access to a file whose purpose allows downloading, then you can produce anonymous download links by creating a [file\_link](https://docs.stripe.com/api#file_links).

`curl https://api.stripe.com/v1/file_links \   -u` 

`sk_test_REDACTED`

  `-d file=  {{FILE_ID}}`

The file\_link resource has a `url` field that allows unauthenticated access to the contents of the file.

## Using a file

After you upload a file, you can use the file upload ID in other API requests. For example, to attach an uploaded file to a particular dispute as evidence:

`curl https://api.stripe.com/v1/disputes/`

`{{DISPUTE_ID}}`

  `-u sk_test_REDACTED -d "evidence[receipt]"=  {{FILE_ID}}`

You can only use an uploaded file in a single API request.

## Handle Upload Errors

When you use the File API to upload a PDF document, we run it through a series of checks to validate that it’s correctly formatted and meets PDF specifications. We return an error for uploads that fail any of our checks.

Try the following to fix errors that we detect:

*   Remove annotations or additional media you added to the document.
*   If you can’t remove your annotations or media, or if you combined several PDFs into one, try using your computer’s “Print to PDF” function to create a fresh document.
    *   [Print to PDF with macOS](https://support.apple.com/guide/mac-help/save-a-document-as-a-pdf-on-mac-mchlp1531/mac)
    *   [Print to PDF with Adobe Acrobat](https://helpx.adobe.com/acrobat/using/print-to-pdf.html)
