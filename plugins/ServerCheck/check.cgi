#!/usr/bin/perl -w

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
