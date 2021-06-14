#!/usr/bin/env perl

use strict;
use warnings;

my @file = `cat $ARGV[0]`;

# ./meta_corr.pl INPUT 1 30 2> err

my @AoA = (
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"]
);

foreach my $line (@file){
    chomp $line;
    my @A = `python3 compute_stats2.py $line $ARGV[1] apo $ARGV[2]`;
    print "python3 compute_stats2.py $line $ARGV[1] apo $ARGV[2] -> ";
    print "$A[0]";
    my @B = `python3 compute_stats2.py $line $ARGV[1] holo $ARGV[2]`;
    print "python3 compute_stats2.py $line $ARGV[1] holo $ARGV[2] -> ";
    print "$B[0]";

    my ($acc_apo, $rest_apo) = split(' ', $A[0]);
    my ($acc_holo, $rest_holo) = split(' ', $B[0]);

    if ($line =~ m/Autodock/ and $line =~ m/rigide/){
        if ($acc_apo ne "No"){
            $AoA[0][0] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[0][1] = $acc_holo;
        }
    }
    if ($line =~ m/Autodock/ and $line =~ m/semi/){
        if ($acc_apo ne "No"){
            $AoA[0][2] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[0][3] = $acc_holo;
        }
    }
    if ($line =~ m/Autodock/ and $line =~ m/full/){
        if ($acc_apo ne "No"){
            $AoA[0][4] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[0][5] = $acc_holo;
        }
    }

################################################################################

    if ($line =~ m/Dkoes/ and $line =~ m/rigide/){
        if ($acc_apo ne "No"){
            $AoA[1][0] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[1][1] = $acc_holo;
        }
    }
    if ($line =~ m/Dkoes/ and $line =~ m/semi/){
        if ($acc_apo ne "No"){
            $AoA[1][2] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[1][3] = $acc_holo;
        }
    }
    if ($line =~ m/Dkoes/ and $line =~ m/full/){
        if ($acc_apo ne "No"){
            $AoA[1][4] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[1][5] = $acc_holo;
        }
    }
################################################################################

    if ($line =~ m/Smina/ and $line =~ m/rigide/){
        if ($acc_apo ne "No"){
            $AoA[2][0] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[2][1] = $acc_holo;
        }
    }
    if ($line =~ m/Smina/ and $line =~ m/semi/){
        if ($acc_apo ne "No"){
            $AoA[2][2] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[2][3] = $acc_holo;
        }
    }
    if ($line =~ m/Smina/ and $line =~ m/full/){
        if ($acc_apo ne "No"){
            $AoA[2][4] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[2][5] = $acc_holo;
        }
    }
################################################################################

    if ($line =~ m/Vina/ and $line =~ m/rigide/ and $line !~ m/Vinardo/){
        if ($acc_apo ne "No"){
            $AoA[3][0] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[3][1] = $acc_holo;
        }
    }
    if ($line =~ m/Vina/ and $line =~ m/semi/ and $line !~ m/Vinardo/){
        if ($acc_apo ne "No"){
            $AoA[3][2] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[3][3] = $acc_holo;
        }
    }
    if ($line =~ m/Vina/ and $line =~ m/full/ and $line !~ m/Vinardo/){
        if ($acc_apo ne "No"){
            $AoA[3][4] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[3][5] = $acc_holo;
        }
    }
################################################################################

    if ($line =~ m/Vinardo/ and $line =~ m/rigide/){
        if ($acc_apo ne "No"){
            $AoA[4][0] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[4][1] = $acc_holo;
        }
    }
    if ($line =~ m/Vinardo/ and $line =~ m/semi/){
        if ($acc_apo ne "No"){
            $AoA[4][2] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[4][3] = $acc_holo;
        }
    }
    if ($line =~ m/Vinardo/ and $line =~ m/full/){
        if ($acc_apo ne "No"){
            $AoA[4][4] = $acc_apo;
        }
        if ($acc_holo ne "No"){
            $AoA[4][5] = $acc_holo;
        }
    }

}


for (my $i=0; $i <= 4; $i++){
    for (my $j=0; $j <= 5; $j++){
        print "$AoA[$i][$j];";
    }
    print "\n";
}
