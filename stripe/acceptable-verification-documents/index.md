---
title: "Acceptable verification documents by country"
source: "https://docs.stripe.com/acceptable-verification-documents"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:37:03.925Z"
content_hash: "bd2bc4c65a132f3aefb2c0994e5dc5add233141a1fb877f506d907704cd9c38c"
---

See the following list of documents that Stripe accepts as proof of identity, address, and entity for each country Stripe supports.

## Common requirements

*   Identity documents (including but not limited to passports and driver’s licenses) must be no more than one step removed from the original document:
    *   Document copies and scans must be in PDF format and taken directly from the original document; they can’t be processed, converted, or embedded in other files
    *   A picture of a physical document must be the original, unprocessed picture in JPEG or PNG format
    *   Screenshots aren’t acceptable
*   When the back side of a document contains required information, and you submit it using the API, include an image of the back side using the `document_back` parameter
*   Photos and scans of the Photo IDs must be in color
*   Photos of paper documents must be in color, but scans of paper documents (not Photo IDs) may be black and white
*   Images must not be low-quality
*   Identity and legal entity documents must not be expired
*   Documents must be readable and in a valid upload file format
*   Documents must not be cropped or missing pages with crucial information, and all borders must be visible
*   If the country of residence differs from the country of the account, a passport is required for identity verification

## How to use this page

If you received a verification request from Stripe, follow these steps:

1.  Select your country from the dropdown below
2.  Choose the document type you need to provide:
    *   **Identity documents**: Passport, driver’s license, or government-issued ID
    *   **Address documents**: Utility bill, bank statement, or other proof of address
    *   **Company or entity documents**: Business registration, tax documents, or incorporation papers
    *   **Bank account documents**: Bank statements or account verification
    *   **Registration status**: Nonprofit or charity registration documents
    *   **Relationship documents**: Documents proving ownership or directorship

## Select a country to view its requirements

#### When a person linked to a Stripe account (such as the Business Representative or Owner) resides in a different country than the country of the Stripe account, a valid passport is the only accepted form of ID for identity verification. Other forms of ID are not accepted in this case.

Acceptable forms of identification:

*   Passport
*   Driver license (including provisional)
*   Citizen Card
*   Electoral ID

Required information:

*   Full legal name that matches the name in your settings
*   Date of birth (DOB) that matches what’s in your settings
*   Photo of person (except where exclusions apply)

If you don’t have any of the listed identity documents or your document was rejected, [contact Stripe support](https://support.stripe.com/contact) for alternative verification options.

### Support articles

## Why was my document rejected?

If Stripe rejected your document, it’s usually for one of these reasons:

*   **Document is expired**: Identity and legal entity documents must be current and not expired.
*   **Screenshot instead of original**: We need the original scan (PDF) or photo (JPEG/PNG), not a screenshot,
*   **Name mismatch**: The name on the document must exactly match the name in your Stripe account settings.
*   **Document is cropped or incomplete**: All borders must be visible and no pages can be missing.
*   **Poor image quality**: Document must be clear, readable, and in focus.
*   **Wrong file format**: Document copies must be PDF. Photos must be JPEG or PNG.
*   **Missing back side**: If your document is double-sided (like some IDs), you must include both sides.
*   **Black and white photo ID** - Photo IDs must be submitted in color

If your document was rejected:

1.  Review the rejection reason in your Dashboard.
2.  Check that your document meets all requirements listed above.
3.  Re-upload a corrected version through your Dashboard.

If you’re still having issues, contact [Stripe support](https://support.stripe.com/contact) for help with document verification.

## Identify your required documents

To see verification requests and what your account still needs to provide, go to [Account verifications](https://dashboard.stripe.com/account/verifications) in your Dashboard.

If your entity type isn’t listed, your document was rejected, or you’re unsure what to upload, [contact Stripe Support](https://support.stripe.com/contact) and describe your organization type and available documents.

## Upload your verification documents

Due to the sensitive nature of your verification documents, Stripe can only accept documents that are uploaded through the Dashboard. Don’t send documents by email.

To upload your document:

1.  Go to your [Stripe Dashboard](https://dashboard.stripe.com/).
2.  Navigate to [Account verifications](https://dashboard.stripe.com/account/verifications).
3.  Find the verification request banner or the document type you need to provide.
4.  Upload your document in the required format (PDF for scans, JPEG or PNG for photos)
