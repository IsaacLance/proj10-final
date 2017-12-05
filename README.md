# proj10-final
Setup meetings with log ins for meeting organizers (per-meeting login) and for invitees (per-invitee login)

## What is here
pendulum objects cannot be held in MongDB.
Instead we output them into the db as RFC3339 strings, the same used by google.
When we retrive them from the db they can be parsed back into pendulum objects.

This flask app gives free/busy times within a given date/time range.
Times are listed from start to finish of the given range.
Default day range is 9am to 5pm. After this value is changed and accepted the values will return to their default.
##Warnings
Does not run in IE9 or earlier due to new HTML5 stuff
