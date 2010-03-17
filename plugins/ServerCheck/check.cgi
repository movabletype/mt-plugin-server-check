#!/usr/bin/perl
############################################################################
## Copyright © 2010 Six Apart Ltd.
## This program is free software: you can redistribute it and/or modify it
## under the terms of version 2 of the GNU General Public License as published
## by the Free Software Foundation, or (at your option) any later version.
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
## version 2 for more details. You should have received a copy of the GNU
## General Public License version 2 along with this program. If not, see
## <http://www.gnu.org/licenses/>.

use strict;
use warnings;

use FindBin;
use Cwd 'abs_path';

use lib "$FindBin::Bin/../../lib";
use lib "$FindBin::Bin/../../extlib";
use MT;
use MT::Author;

sub send_headers {
    print <<END;
Content-type: text/plain

END
}

sub test_connection {
    my $path = "$FindBin::Bin/../../mt-config.cgi";
    my %args = (Config => abs_path($path));
    my $mt = MT->new(%args);
    my $author = MT::Author->load(undef, { limit => 1 });
    if (!$author) {
        die "Author not found.\n";
    }
    print "SERVER_CHECK_OK\n";
}

send_headers();
test_connection();
