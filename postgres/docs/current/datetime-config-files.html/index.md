---
title: "PostgreSQL: Documentation: 18: B.4. Date/Time Configuration Files"
source: "https://www.postgresql.org/docs/current/datetime-config-files.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-config-files.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:02.356Z"
content_hash: "79a991f101d5de15b04d13b8c3a0a373848961295c6e2277edc08b6deccc04f4"
menu_path: ["PostgreSQL: Documentation: 18: B.4. Date/Time Configuration Files"]
section_path: []
nav_prev: {"path": "postgres/docs/current/logical-replication-publication.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.1.\u00a0Publication"}
nav_next: {"path": "postgres/docs/current/app-reindexdb.html/index.md", "title": "PostgreSQL: Documentation: 18: reindexdb"}
---

Since timezone abbreviations are not well standardized, PostgreSQL provides a means to customize the set of abbreviations accepted in datetime input. There are two sources for these abbreviations:

1.  The [TimeZone](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE) run-time parameter is usually set to the name of an entry in the IANA time zone database. If that zone has widely-used zone abbreviations, they will appear in the IANA data, and PostgreSQL will preferentially recognize those abbreviations with the meanings given in the IANA data. For example, if `timezone` is set to `America/New_York` then `EST` will be understood as UTC-5 and `EDT` will be understood as UTC-4. (These IANA abbreviations will also be used in datetime output, if [DateStyle](postgres/docs/current/runtime-config-client.html/index.md#GUC-DATESTYLE) is set to a style that prefers non-numeric zone abbreviations.)
    
2.  If an abbreviation is not found in the current IANA time zone, it is sought in the list specified by the [timezone\_abbreviations](postgres/docs/current/runtime-config-client.html/index.md#GUC-TIMEZONE-ABBREVIATIONS) run-time parameter. The `timezone_abbreviations` list is primarily useful for allowing datetime input to recognize abbreviations for time zones other than the current zone. (These abbreviations will not be used in datetime output.)
    

While the `timezone_abbreviations` parameter can be altered by any database user, the possible values for it are under the control of the database administrator — they are in fact names of configuration files stored in `.../share/timezonesets/` of the installation directory. By adding or altering files in that directory, the administrator can set local policy for timezone abbreviations.

`timezone_abbreviations` can be set to any file name found in `.../share/timezonesets/`, if the file's name is entirely alphabetic. (The prohibition against non-alphabetic characters in `timezone_abbreviations` prevents reading files outside the intended directory, as well as reading editor backup files and other extraneous files.)

A timezone abbreviation file can contain blank lines and comments beginning with `#`. Non-comment lines must have one of these formats:

_`zone_abbreviation`_ _`offset`_
_`zone_abbreviation`_ _`offset`_ D
_`zone_abbreviation`_ _`time_zone_name`_
@INCLUDE _`file_name`_
@OVERRIDE

A _`zone_abbreviation`_ is just the abbreviation being defined. An _`offset`_ is an integer giving the equivalent offset in seconds from UTC, positive being east from Greenwich and negative being west. For example, -18000 would be five hours west of Greenwich, or North American east coast standard time. `D` indicates that the zone name represents local daylight-savings time rather than standard time.

Alternatively, a _`time_zone_name`_ can be given, referencing a zone name defined in the IANA timezone database. The zone's definition is consulted to see whether the abbreviation is or has been in use in that zone, and if so, the appropriate meaning is used — that is, the meaning that was currently in use at the timestamp whose value is being determined, or the meaning in use immediately before that if it wasn't current at that time, or the oldest meaning if it was used only after that time. This behavior is essential for dealing with abbreviations whose meaning has historically varied. It is also allowed to define an abbreviation in terms of a zone name in which that abbreviation does not appear; then using the abbreviation is just equivalent to writing out the zone name.

### Tip

Using a simple integer _`offset`_ is preferred when defining an abbreviation whose offset from UTC has never changed, as such abbreviations are much cheaper to process than those that require consulting a time zone definition.

The `@INCLUDE` syntax allows inclusion of another file in the `.../share/timezonesets/` directory. Inclusion can be nested, to a limited depth.

The `@OVERRIDE` syntax indicates that subsequent entries in the file can override previous entries (typically, entries obtained from included files). Without this, conflicting definitions of the same timezone abbreviation are considered an error.

In an unmodified installation, the file `Default` contains all the non-conflicting time zone abbreviations for most of the world. Additional files `Australia` and `India` are provided for those regions: these files first include the `Default` file and then add or modify abbreviations as needed.

For reference purposes, a standard installation also contains files `Africa.txt`, `America.txt`, etc., containing information about every time zone abbreviation known to be in use according to the IANA timezone database. The zone name definitions found in these files can be copied and pasted into a custom configuration file as needed. Note that these files cannot be directly referenced as `timezone_abbreviations` settings, because of the dot embedded in their names.

### Note

If an error occurs while reading the time zone abbreviation set, no new value is applied and the old set is kept. If the error occurs while starting the database, startup fails.

### Caution

Time zone abbreviations defined in the configuration file override non-timezone meanings built into PostgreSQL. For example, the `Australia` configuration file defines `SAT` (for South Australian Standard Time). When this file is active, `SAT` will not be recognized as an abbreviation for Saturday.

### Caution

If you modify files in `.../share/timezonesets/`, it is up to you to make backups — a normal database dump will not include this directory.


