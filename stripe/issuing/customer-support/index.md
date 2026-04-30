---
title: "Customer support for Issuing and Treasury for platforms"
source: "https://docs.stripe.com/issuing/customer-support"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:02:50.686Z"
content_hash: "78b438c2736b438dec9faddf096464896d50c27d8083a0348200d54020c5e4db"
---

Ordering and replacing cards Lost or stolen cards[Make an API call](https://docs.stripe.com/issuing/cards/replacements#replacements-for-lost-or-stolen-cards) to immediately cancel and replace any physical or virtual cards reported as compromised.

If any authorizations were approved on a compromised card, you might [dispute the transactions](https://docs.stripe.com/issuing/purchases/disputes) as fraud.

Expired or damaged physical cards[Make an API call](https://docs.stripe.com/issuing/cards/replacements) to replace physical cards that are expired or damaged.Delayed physical cardsDelays in card manufacturing can occur if you have a pending [cardholder watchlist screening](https://support.stripe.com/questions/issuing-watchlist-reviews). Make sure that the cardholder is active and has fulfilled all necessary requirements. If you chose the Standard shipping method (which doesn’t provide tracking), and the cardholder hasn’t received the card within 10 business days, we recommend that you cancel and order a replacement (Stripe credits the creation and shipment cost back to you).  
Alternatively, if you selected Express or Priority shipping methods (which include tracking) you can retrieve the tracking number from the Dashboard or [through the API](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-tracking_number).Cardholder experience Authorization declined[Make an API call](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason) to retrieve the authorization and review the request\_history.reason.Cancel pending authorizationInform the cardholder that it isn’t possible to cancel pending authorizations. Only the acquiring merchant can void an authorization.

Advise customers that the authorization will automatically expire 7 days after creation (31 days if hotels, airlines, and car rental companies) and the held funds will be released at that time.

Missing refund[Make an API call](https://docs.stripe.com/api/issuing/transactions/list#list_issuing_transactions-type) to retrieve a list of transactions associated with the card where the type is `refund`.

Stripe attempts to link refunds to original transactions. If this doesn’t happen, you can review the amount and merchant data across all results to identify a match.

Disputing a transactionEnsure that the cardholder has exhausted other means of resolving the issue, and obtain documentation of these attempts to use as evidence when filing the dispute.

Make an API call to [create](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api) and [submit](https://docs.stripe.com/issuing/purchases/disputes?dashboard-or-api=api#submission) a dispute on behalf of the cardholder.

Dispute loss reasonIf you’re interested in the ability to retrieve a dispute loss reason through API, apply for the beta by [submitting your interest](https://docs.stripe.com/issuing/purchases/disputes) while logged into your platform account. If you don’t have access to the beta, [contact support](https://support.stripe.com/) for more information that you can relay to the cardholder regarding why a dispute was lost.Excessive PIN retriesIf a card’s PIN is entered incorrectly three consecutive times, the PIN becomes blocked and the card becomes inactive. In most countries, cardholders can [unblock a card’s PIN at an ATM](https://docs.stripe.com/issuing/cards/pin-management#changing-a-cards-pin-at-an-atm).

Users who are gated into the encrypted PIN management feature might also [change the PIN](https://docs.stripe.com/issuing/cards/pin-management#changing-a-pin-with-the-cards-api) for an issued card using the Card Update API. However, depending on the region the card is used in, the new PIN might not be immediately usable.

Once the pin is unblocked, you’ll need to [make an API call](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-status) to update the card status to active. If you would like to request access to encrypted PIN management, [contact support](https://support.stripe.com/).

Cardholder inactive[Make an API call](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-requirements) to retrieve the cardholder requirements array so that you can review the disabled\_reason and confirm whether any information is past\_due.can’t add card to digital walletEnsure you’ve already [configured digital wallets](https://docs.stripe.com/issuing/cards/digital-wallets). If configured, request screenshots from the cardholder of the error message being surfaced. [Contact support](https://support.stripe.com/) for in-depth troubleshooting assistance once you have obtained documentation from the cardholder.Fraud management Turning on 3DSConfirm your customer understands that 3DS can only be turned on at the connected account level, meaning they won’t be able to toggle the feature on or off for individual cardholders.

After the feature is enabled, acquiring merchants might immediately start challenging card-not-present authorization requests for any users that have linked a phone number or email address to the card or cardholder.

Once you’re ready, [contact support](https://support.stripe.com/) to request 3DS be enabled and provide the Stripe ID of the connected account.

Update spending controlsMake an API call to update the spending controls on the [cardholder object](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls) or the [card object](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls) itself.Enabling fraud challenges betaIf you’re providing cardholders with notice of suspected fraud and the ability to override this warning, [apply for enrollment in the beta](https://docs.stripe.com/issuing/controls/fraud-challenges) by submitting your interest while logged into your platform account.Issuing balance Top-ups from external bank account[Make an API call](https://docs.stripe.com/issuing/connect/funding) to add funds to a connected account’s Issuing balance. Set appropriate expectations with cardholders for settlement timing based on your region. If top-ups are reportedly delayed, you can [make an API call](https://docs.stripe.com/api/topups/retrieve) to retrieve a list of top-ups associated with the connected account.Balance transfer (to fund from Stripe balance)You must sign up for the [Balance Transfer API private beta](https://docs.stripe.com/issuing/connect/funding#request-early-access) to transfer funds from a connected account’s Stripe balance into their Issuing balance.Payouts[Make an API call](https://docs.stripe.com/issuing/connect/funding#pay-out-an-issuing-balance) to pay out funds from a connected account’s issuing balance to their external bank account.Complaints Operational complaintsStripe expects you to acknowledge all operational complaints within 5 business days and resolve them within 15 business days from complaint submission date.

In addition, you must [report an aggregated list of complaints](https://docs.stripe.com/treasury/connect/handling-complaints) to Stripe on a monthly basis.

Executive complaintsPromptly notify Stripe within 1 business day of complaint submission date. Executive complaints include any threats of litigation and complaints received from regulators and complaints that allege Unfair or Deceptive Acts and Practices (UDAP), discrimination, consumer harm or legal concerns.

Upon receipt of an Executive Complaint, refrain from further interaction with the customer until Stripe reviews the complaint. Stripe works closely with you to resolve all Executive Complaints. In addition, you must [report an aggregated list of complaints](https://docs.stripe.com/treasury/connect/handling-complaints) to Stripe on a monthly basis.
