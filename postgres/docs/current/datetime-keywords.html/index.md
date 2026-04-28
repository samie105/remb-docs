---
title: "PostgreSQL: Documentation: 18: B.3. Date/Time Key Words"
source: "https://www.postgresql.org/docs/current/datetime-keywords.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-keywords.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:50:01.034Z"
content_hash: "6422cf04fdb11dfd2f03020c4012cca46df8e9b152e96a1d01af7eb2aa0720b1"
menu_path: ["PostgreSQL: Documentation: 18: B.3. Date/Time Key Words"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/datetime-julian-dates.html/index.md", "title": "PostgreSQL: Documentation: 18: B.7.\u00a0Julian Dates"}
nav_next: {"path": "postgres/docs/current/datetime-posix-timezone-specs.html/index.md", "title": "PostgreSQL: Documentation: 18: B.5.\u00a0POSIX Time Zone Specifications"}
---

[Table B.1](https://www.postgresql.org/docs/current/datetime-keywords.html#DATETIME-MONTH-TABLE "Table B.1. Month Names") shows the tokens that are recognized as names of months.

**Table B.1. Month Names**

 
| Month | Abbreviations |
| --- | --- |
| January | Jan |
| February | Feb |
| March | Mar |
| April | Apr |
| May |   |
| June | Jun |
| July | Jul |
| August | Aug |
| September | Sep, Sept |
| October | Oct |
| November | Nov |
| December | Dec |

[Table B.2](https://www.postgresql.org/docs/current/datetime-keywords.html#DATETIME-DOW-TABLE "Table B.2. Day of the Week Names") shows the tokens that are recognized as names of days of the week.

**Table B.2. Day of the Week Names**

 
| Day | Abbreviations |
| --- | --- |
| Sunday | Sun |
| Monday | Mon |
| Tuesday | Tue, Tues |
| Wednesday | Wed, Weds |
| Thursday | Thu, Thur, Thurs |
| Friday | Fri |
| Saturday | Sat |

[Table B.3](https://www.postgresql.org/docs/current/datetime-keywords.html#DATETIME-MOD-TABLE "Table B.3. Date/Time Field Modifiers") shows the tokens that serve various modifier purposes.

**Table B.3. Date/Time Field Modifiers**

 
| Identifier | Description |
| --- | --- |
| `AM` | Time is before 12:00 |
| `AT` | Ignored |
| `JULIAN`, `JD`, `J` | Next field is Julian Date |
| `ON` | Ignored |
| `PM` | Time is on or after 12:00 |
| `T` | Next field is time |
