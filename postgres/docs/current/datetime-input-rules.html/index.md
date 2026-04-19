---
title: "PostgreSQL: Documentation: 18: B.1. Date/Time Input Interpretation"
source: "https://www.postgresql.org/docs/current/datetime-input-rules.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-input-rules.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:23.575Z"
content_hash: "b60fff2b5fe2002fef9f961f2ef45a47cb537bfc09f2ee398e8aa8c80b30ad77"
menu_path: ["PostgreSQL: Documentation: 18: B.1. Date/Time Input Interpretation"]
section_path: []
nav_prev: {"path": "postgres/docs/current/datetime-config-files.html/index.md", "title": "PostgreSQL: Documentation: 18: B.4.\u00a0Date/Time Configuration Files"}
nav_next: {"path": "postgres/docs/current/datetime-invalid-input.html/index.md", "title": "PostgreSQL: Documentation: 18: B.2.\u00a0Handling of Invalid or Ambiguous Timestamps"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/datetime-input-rules.html "PostgreSQL 18 - B.1. Date/Time Input Interpretation") ([18](/docs/18/datetime-input-rules.html "PostgreSQL 18 - B.1. Date/Time Input Interpretation")) / [17](/docs/17/datetime-input-rules.html "PostgreSQL 17 - B.1. Date/Time Input Interpretation") / [16](/docs/16/datetime-input-rules.html "PostgreSQL 16 - B.1. Date/Time Input Interpretation") / [15](/docs/15/datetime-input-rules.html "PostgreSQL 15 - B.1. Date/Time Input Interpretation") / [14](/docs/14/datetime-input-rules.html "PostgreSQL 14 - B.1. Date/Time Input Interpretation")

Development Versions: [devel](/docs/devel/datetime-input-rules.html "PostgreSQL devel - B.1. Date/Time Input Interpretation")

Unsupported versions: [13](/docs/13/datetime-input-rules.html "PostgreSQL 13 - B.1. Date/Time Input Interpretation") / [12](/docs/12/datetime-input-rules.html "PostgreSQL 12 - B.1. Date/Time Input Interpretation") / [11](/docs/11/datetime-input-rules.html "PostgreSQL 11 - B.1. Date/Time Input Interpretation") / [10](/docs/10/datetime-input-rules.html "PostgreSQL 10 - B.1. Date/Time Input Interpretation") / [9.6](/docs/9.6/datetime-input-rules.html "PostgreSQL 9.6 - B.1. Date/Time Input Interpretation") / [9.5](/docs/9.5/datetime-input-rules.html "PostgreSQL 9.5 - B.1. Date/Time Input Interpretation") / [9.4](/docs/9.4/datetime-input-rules.html "PostgreSQL 9.4 - B.1. Date/Time Input Interpretation") / [9.3](/docs/9.3/datetime-input-rules.html "PostgreSQL 9.3 - B.1. Date/Time Input Interpretation") / [9.2](/docs/9.2/datetime-input-rules.html "PostgreSQL 9.2 - B.1. Date/Time Input Interpretation") / [9.1](/docs/9.1/datetime-input-rules.html "PostgreSQL 9.1 - B.1. Date/Time Input Interpretation") / [9.0](/docs/9.0/datetime-input-rules.html "PostgreSQL 9.0 - B.1. Date/Time Input Interpretation") / [8.4](/docs/8.4/datetime-input-rules.html "PostgreSQL 8.4 - B.1. Date/Time Input Interpretation") / [8.3](/docs/8.3/datetime-input-rules.html "PostgreSQL 8.3 - B.1. Date/Time Input Interpretation")

## B.1. Date/Time Input Interpretation [#](#DATETIME-INPUT-RULES)

Date/time input strings are decoded using the following procedure.

1.  Break the input string into tokens and categorize each token as a string, time, time zone, or number.
    
    1.  If the numeric token contains a colon (`:`), this is a time string. Include all subsequent digits and colons.
        
    2.  If the numeric token contains a dash (`-`), slash (`/`), or two or more dots (`.`), this is a date string which might have a text month. If a date token has already been seen, it is instead interpreted as a time zone name (e.g., `America/New_York`).
        
    3.  If the token is numeric only, then it is either a single field or an ISO 8601 concatenated date (e.g., `19990113` for January 13, 1999) or time (e.g., `141516` for 14:15:16).
        
    4.  If the token starts with a plus (`+`) or minus (`-`), then it is either a numeric time zone or a special field.
        
2.  If the token is an alphabetic string, match up with possible strings:
    
    1.  See if the token matches any known time zone abbreviation. These abbreviations are determined by the configuration settings described in [Section B.4](datetime-config-files.html "B.4. Date/Time Configuration Files").
        
    2.  If not found, search an internal table to match the token as either a special string (e.g., `today`), day (e.g., `Thursday`), month (e.g., `January`), or noise word (e.g., `at`, `on`).
        
    3.  If still not found, throw an error.
        
3.  When the token is a number or number field:
    
    1.  If there are eight or six digits, and if no other date fields have been previously read, then interpret as a “concatenated date” (e.g., `19990118` or `990118`). The interpretation is `YYYYMMDD` or `YYMMDD`.
        
    2.  If the token is three digits and a year has already been read, then interpret as day of year.
        
    3.  If four or six digits and a year has already been read, then interpret as a time (`HHMM` or `HHMMSS`).
        
    4.  If three or more digits and no date fields have yet been found, interpret as a year (this forces yy-mm-dd ordering of the remaining date fields).
        
    5.  Otherwise the date field ordering is assumed to follow the `DateStyle` setting: mm-dd-yy, dd-mm-yy, or yy-mm-dd. Throw an error if a month or day field is found to be out of range.
        
4.  If BC has been specified, negate the year and add one for internal storage. (There is no year zero in the Gregorian calendar, so numerically 1 BC becomes year zero.)
    
5.  If BC was not specified, and if the year field was two digits in length, then adjust the year to four digits. If the field is less than 70, then add 2000, otherwise add 1900.
    
    ### Tip
    
    Gregorian years AD 1–99 can be entered by using 4 digits with leading zeros (e.g., `0099` is AD 99).
    

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/datetime-input-rules.html/) to report a documentation issue.
