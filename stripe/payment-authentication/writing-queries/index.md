---
title: "Querying authentication conversion"
source: "https://docs.stripe.com/payment-authentication/writing-queries"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:02:31.217Z"
content_hash: "dddbdafdb40bb915ee8515d4b2a6692226d6d7b7f65c0301b3b6492552adc163"
---

## Use Stripe Sigma to retrieve information about authentication, conversion, and the SCA exemptions used.

See the `authentication_report_attempts` table under the **Analytics Tables** section of the Sigma schema. Each row within the `authentication_report_attempts` table represents data about an individual attempt object. Our [full-page documentation](https://dashboard.stripe.com/stripe-schema?tableName=authentication_report_attempts) also shows the schema in a split-view format.

## Attempt conversion information

You can get a report for every attempt, with each [PaymentIntent](https://docs.stripe.com/api/payment_intents) or [SetupIntent](https://docs.stripe.com/api/payment_intents) having possibly more than one attempt.

#### Note

In some cases there are multiple attempts for a single transaction, such as when a payment is declined and then retried. To filter to a specific transaction, use the `is_final_attempt` column. This column is eventually consist after a few days.

The following example query uses the `authentication_report_attempts` table to retrieve a list of PaymentIntents that were successfully authenticated using the challenge flow.

`select   attempt_id,   intent_id,   payment_method,   threeds_reason as step_up_reason,   charge_outcome from authentication_report_attempts where intent_type = 'payment'   and threeds_outcome_result = 'authenticated'   and authentication_flow = 'challenge'   and is_final_attempt limit 5`

attempt\_id

intent\_id

payment\_method

step\_up\_reason

charge\_outcome

payatt\_1IRdZ9F…

pi\_1Hn8d…

card\_charge

requested\_by\_radar\_rule

authorized

payatt\_1I4AFxF…

pi\_1J8Ljt…

card\_charge

requested\_by\_radar\_rule

authorized

payatt\_1HvmxU…

pi\_1HhsH…

card\_charge

requested\_by\_radar\_rule

authorized

payatt\_1I5npGF…

pi\_1IdKak…

card\_charge

requested\_by\_radar\_rule

authorized

payatt\_1HcbWZ…

pi\_1IAhBh…

card\_charge

requested\_by\_radar\_rule

authorized

## SCA exemption information

You can also query information on the [SCA exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication) used by Stripe or the issuing bank. See [Exemptions to Strong Customer Authentication](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication).

The following query shows the payments that used a low risk direct authorization SCA exemption that was declined for a reason unrelated to the requested exemption.

`select   attempt_id,   intent_id,   charge_outcome,   charge_outcome_reason from authentication_report_attempts where intent_type = 'payment'   and sca_exemption_requested = 'low_risk'   and sca_exemption_mechanism = 'authorization' -- direct to authorization   and sca_exemption_status = 'non_sca_decline'   and is_final_attempt limit 5`

attempt\_id

intent\_id

charge\_outcome

charge\_outcome\_reason

payatt\_3JeL…

pi\_3JeL…

issuer\_declined

insufficient\_funds

payatt\_1Itw…

pi\_1Itw…

issuer\_declined

do\_not\_honor

payatt\_1Ini3…

pi\_1Ini3…

issuer\_declined

do\_not\_honor

payatt\_1IiO7…

pi\_1IiO7…

issuer\_declined

do\_not\_honor

payatt\_1I0hGm…

pi\_1I0hGk…

issuer\_declined

insufficient\_funds

## Impact of deduplication

The following query shows how removing duplicates with `is_final_attempt` affects the calculation of the authentication rate for setups.

#### Note

Our deduplication logic looks for groups of declined transactions (except for the last, potentially) with the same `customer_id​`, `currency`, and `amount​`, appearing close together in time. Such groups are treated as a single unit for conversion calculations. In the Sigma table, we include all raw data, but also include a column, `is_final_attempt​`, that you can use to filter to a representative transaction from each group.

`with setup_attempts as (   select     created,     is_final_attempt,     threeds_outcome_result in (       'attempt_acknowledged',       'authenticated',       'delegated',       'exempted'     ) as threeds_succeeded   from authentication_report_attempts   where created between date'2021-10-29' and date'2021-11-03'     and intent_type = 'setup'     and is_threeds_triggered ) select   date_trunc('day', created) as day,   1. * count_if(threeds_succeeded)     / count(*) as authentication_rate__raw,   2. * count_if(threeds_succeeded and is_final_attempt)     / nullif(count_if(is_final_attempt), 0) as authentication_rate__deduped from setup_attempts group by 1 order by 1`

day

authentication\_rate\_\_raw

authentication\_rate\_\_deduped

2021-10-29

0.59

0.80

2021-10-30

0.60

0.81

2021-10-31

0.59

0.81

2021-11-01

0.61

0.83

2021-11-02

0.62

0.83
