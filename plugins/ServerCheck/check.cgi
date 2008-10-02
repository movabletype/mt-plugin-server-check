#!/usr/bin/perl -w

use strict;
use warnings;

use lib "./lib", ($ENV{MT_HOME} ? "$ENV{MT_HOME}/lib" : "../../lib");
use lib "./extlib", ($ENV{MT_HOME} ? "$ENV{MT_HOME}/extlib" : "../../extlib");

use MT;
use MT::Author;

sub send_headers {
    print <<END;
Content-type: text/plain

END
}

sub test_connection {
    my $mt = MT->new;
    my $author = MT::Author->load(undef, { limit => 1 });
    if (!$author) {
	die "Author not found.\n";
    }
    print "OK\n";
}

send_headers();
test_connection();
