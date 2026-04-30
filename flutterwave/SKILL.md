## Overview

Flutterwave is a payment infrastructure platform that enables businesses to collect payments, disburse funds, and manage financial operations across Africa and globally. An agent needs to know it to integrate payment gateways, handle transfers, encrypt sensitive data, and troubleshoot errors using the provided API documentation.

## Mental Model

The Flutterwave documentation is organized around a secure payment gateway API where all requests are authenticated via headers and sensitive data is encrypted before transit. Integrators typically progress from environment configuration and authentication to product-specific flows—charging cards, processing card payments, and orchestrating bank transfers—while using testing environments and error references to harden their implementation. Canonical starting points are `flutterwave/docs/environments/index.md`, `flutterwave/docs/authentication/index.md`, `flutterwave/docs/encryption/index.md`, and `flutterwave/docs/direct-transfer-flow/index.md`.

## Learning Paths

**Getting Started**
1. `flutterwave/docs/environments/index.md`
2. `flutterwave/docs/authentication/index.md`
3. `flutterwave/docs/api-headers/index.md`
4. `flutterwave/docs/testing/index.md`

**Production Payments & Transfers**
1. `flutterwave/docs/encryption/index.md`
2. `flutterwave/docs/charging-a-card/index.md`
3. `flutterwave/docs/card/index.md`
4. `flutterwave/docs/bank-transfer/index.md`
5. `flutterwave/docs/direct-transfer-flow/index.md`
6. `flutterwave/docs/best-practices/index.md`

**Reference Deep-Dive**
1. `flutterwave/docs/general-transfer-flow/index.md`
2. `flutterwave/docs/chargebacks-1/index.md`
3. `flutterwave/docs/common-errors/index.md`
4. `flutterwave/docs/e-commerce/index.md`
5. `flutterwave/docs/fintechs/index.md`
6. `flutterwave/docs/banks-and-ofis/index.md`

## Concept Map

- **API Foundation**
  - Authentication & Headers
    - `flutterwave/docs/authentication/index.md`
    - `flutterwave/docs/api-headers/index.md`
  - Environments & Credentials
    - `flutterwave/docs/environments/index.md`
  - Errors & Best Practices
    - `flutterwave/docs/common-errors/index.md`
    - `flutterwave/docs/best-practices/index.md`
- **Payments**
  - Card Operations
    - `flutterwave/docs/card/index.md`
    - `flutterwave/docs/charging-a-card/index.md`
  - Security & Chargebacks
    - `flutterwave/docs/encryption/index.md`
    - `flutterwave/docs/chargebacks-1/index.md`
- **Transfers**
  - Bank Transfers
    - `flutterwave/docs/bank-transfer/index.md`
  - Transfer Flows
    - `flutterwave/docs/direct-transfer-flow/index.md`
    - `flutterwave/docs/general-transfer-flow/index.md`
- **Business Verticals**
  - E-Commerce & Fintech
    - `flutterwave/docs/e-commerce/index.md`
    - `flutterwave/docs/fintechs/index.md`
  - Banks and OFIs
    - `flutterwave/docs/banks-and-ofis/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Authenticate API requests | `flutterwave/docs/authentication/index.md` |
| Set request headers | `flutterwave/docs/api-headers/index.md` |
| Configure environments | `flutterwave/docs/environments/index.md` |
| Encrypt sensitive payloads | `flutterwave/docs/encryption/index.md` |
| Charge a card | `flutterwave/docs/charging-a-card/index.md` |
| Process card payments | `flutterwave/docs/card/index.md` |
| Handle chargebacks | `flutterwave/docs/chargebacks-1/index.md` |
| Transfer to bank accounts | `flutterwave/docs/bank-transfer/index.md` |
| Orchestrate transfers | `flutterwave/docs/direct-transfer-flow/index.md` |
| Test integrations | `flutterwave/docs/testing/index.md` |
| Troubleshoot errors | `flutterwave/docs/common-errors/index.md` |
| Follow best practices | `flutterwave/docs/best-practices/index.md` |

## Top Must-Know Pages

1. `flutterwave/docs/authentication/index.md` — Covers API authentication with sample cURL requests in multiple languages.
2. `flutterwave/docs/api-headers/index.md` — Lists supported request headers required for every API call.
3. `flutterwave/docs/encryption/index.md` — Explains payload encryption using JavaScript, Python, and Java examples.
4. `flutterwave/docs/environments/index.md` — Describes how to retrieve test API credentials and configure environments.
5. `flutterwave/docs/charging-a-card/index.md` — Provides the flow and code samples for charging a card securely.
6. `flutterwave/docs/card/index.md` — Details card payment integration options and sample requests.
7. `flutterwave/docs/bank-transfer/index.md` — Guides you through bank account transfers and cross-currency options.
8. `flutterwave/docs/direct-transfer-flow/index.md` — Documents the transfer orchestrator and direct transfer workflows.
9. `flutterwave/docs/general-transfer-flow/index.md` — Outlines the general transfer flow and related integration steps.
10. `flutterwave/docs/common-errors/index.md` — Helps troubleshoot and resolve common integration errors quickly.