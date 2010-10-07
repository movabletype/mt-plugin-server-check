# Server Check, a plugin for Movable Type

* Author: Six Apart
* Copyright: 2009 Six Apart
* License: GPL


## Overview

The Server Check plugin for Movable Type provides a super basic CGI script that
when accessed will produce the output:

    SERVER_CHECK_OK

This allows external monitors to confirm that the MT installation is in place,
the MT code base is loading, and it can connect to the database. It also
includes a plain text file to place in `mt-static` to confirm that `mt-static`
exists and is loading properly.


## Installation

1. Move the `ServerCheck` plugin directory to the MT `plugins` directory.
2. Move the `ServerCheck` mt-static directory to the `mt-static/plugins` directory.

Should look like this when installed:

    $MT_HOME/
        plugins/
            ServerCheck/
                (plugin files here)
        mt-static/
            plugins/
                ServerCheck/
                    (plugin static files here)


## Support

This plugin is not an official Six Apart release, and as such support from Six Apart for this plugin is not available.
