---
title: "PostgreSQL: Documentation: 18: B.6. History of Units"
source: "https://www.postgresql.org/docs/current/datetime-units-history.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-units-history.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:21.851Z"
content_hash: "09d3371b5407e02e1bbe0afb1ad1ff8ed7265ec36a372a538fdfcc3cf23da812"
menu_path: ["PostgreSQL: Documentation: 18: B.6. History of Units"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/datetime-posix-timezone-specs.html/index.md", "title": "PostgreSQL: Documentation: 18: B.5.\u00a0POSIX Time Zone Specifications"}
nav_next: {"path": "postgres/docs/current/dblink.html/index.md", "title": "PostgreSQL: Documentation: 18: F.11.\u00a0dblink \u2014 connect to other PostgreSQL databases"}
---

The SQL standard states that “Within the definition of a ‘datetime literal’, the ‘datetime values’ are constrained by the natural rules for dates and times according to the Gregorian calendar”. PostgreSQL follows the SQL standard's lead by counting dates exclusively in the Gregorian calendar, even for years before that calendar was in use. This rule is known as the _proleptic Gregorian calendar_.

The Julian calendar was introduced by Julius Caesar in 45 BC. It was in common use in the Western world until the year 1582, when countries started changing to the Gregorian calendar. In the Julian calendar, the tropical year is approximated as 365 1/4 days = 365.25 days. This gives an error of about 1 day in 128 years.

The accumulating calendar error prompted Pope Gregory XIII to reform the calendar in accordance with instructions from the Council of Trent. In the Gregorian calendar, the tropical year is approximated as 365 + 97 / 400 days = 365.2425 days. Thus it takes approximately 3300 years for the tropical year to shift one day with respect to the Gregorian calendar.

The approximation 365+97/400 is achieved by having 97 leap years every 400 years, using the following rules:

<table summary="Simple list"><tbody><tr><td>Every year divisible by 4 is a leap year.</td></tr><tr><td>However, every year divisible by 100 is not a leap year.</td></tr><tr><td>However, every year divisible by 400 is a leap year after all.</td></tr></tbody></table>

So, 1700, 1800, 1900, 2100, and 2200 are not leap years. But 1600, 2000, and 2400 are leap years. By contrast, in the older Julian calendar all years divisible by 4 are leap years.

The papal bull of February 1582 decreed that 10 days should be dropped from October 1582 so that 15 October should follow immediately after 4 October. This was observed in Italy, Poland, Portugal, and Spain. Other Catholic countries followed shortly after, but Protestant countries were reluctant to change, and the Greek Orthodox countries didn't change until the start of the 20th century. The reform was observed by Great Britain and its dominions (including what is now the USA) in 1752. Thus 2 September 1752 was followed by 14 September 1752. This is why Unix systems that have the `cal` program produce the following:

$ **`cal 9 1752`**
   September 1752
 S  M Tu  W Th  F  S
       1  2 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30

But, of course, this calendar is only valid for Great Britain and dominions, not other places. Since it would be difficult and confusing to try to track the actual calendars that were in use in various places at various times, PostgreSQL does not try, but rather follows the Gregorian calendar rules for all dates, even though this method is not historically accurate.

Different calendars have been developed in various parts of the world, many predating the Gregorian system. For example, the beginnings of the Chinese calendar can be traced back to the 14th century BC. Legend has it that the Emperor Huangdi invented that calendar in 2637 BC. The People's Republic of China uses the Gregorian calendar for civil purposes. The Chinese calendar is used for determining festivals.
