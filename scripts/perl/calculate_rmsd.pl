#!/usr/bin/env perl

use strict;
use warnings;

my @file0 = `cat $ARGV[0]`;
my @file1 = `cat $ARGV[1]`;

foreach my $line0 (@file0){
    chomp $line0;
    my @A = split('/', $line0);
    my $root0 = $line0;
    $root0 =~ s/$A[$#A]//;
    #print "$root0\n";
    foreach my $line1 (@file1){
        chomp $line1;
        my @B = split('/', $line1);
        my $root1 = $line1;
        $root1 =~ s/$B[$#B]//;
        if ($root0 eq $root1){
            print "python3 compute_rmsd_v1.py $line1 $line0 > $root0/comparaison_rmsd_holo.txt\n";
        }
    }
}


