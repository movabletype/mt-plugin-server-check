The ServerCheck plugin for Movable Type provides a super basic CGI script that
when accessed will produce the output:

SERVER_CHECK_OK

This allows external monitors to confirm that the MT installation is in place,
the MT code base is loading, and it can connect to the database. It also
includes a plain text file to place in mt-static to confirm that mt-static
exists and is loading properly.
