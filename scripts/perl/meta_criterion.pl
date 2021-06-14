#!/usr/bin/env perl

use strict;
use warnings;

sub mean{
    my @array = @{$_[0]};
    my $sum = 0;
    foreach my $value (@array){
        chomp($value);
        $sum+=$value;
    }

    my $avg = "N/A";
    if ($#array+1 > 0){
        $avg = $sum/($#array+1);
    }
    return $avg;
}

my @AoA = (
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],

["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],

["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],

["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"],
["N/A", "N/A", "N/A", "N/A", "N/A","N/A"]
);

sub modify_AoA{
    my $index = shift;
    my $rank_apo = shift;
    my $rank_holo = shift;
    my $line = shift;

    if ($line =~ m/Autodock/ and $line =~ m/rigide/){
        if ($rank_apo ne "No"){
            $AoA[$index][0] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][1] = $rank_holo;
        }
    }
    if ($line =~ m/Autodock/ and $line =~ m/semi/){
        if ($rank_apo ne "No"){
            $AoA[$index][2] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][3] = $rank_holo;
        }
    }
    if ($line =~ m/Autodock/ and $line =~ m/full/){
        if ($rank_apo ne "No"){
            $AoA[$index][4] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][5] = $rank_holo;
        }
    }

################################################################################
    $index+=4;


    if ($line =~ m/Dkoes/ and $line =~ m/rigide/){
        if ($rank_apo ne "No"){
            $AoA[$index][0] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][1] = $rank_holo;
        }
    }
    if ($line =~ m/Dkoes/ and $line =~ m/semi/){
        if ($rank_apo ne "No"){
            $AoA[$index][2] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][3] = $rank_holo;
        }
    }
    if ($line =~ m/Dkoes/ and $line =~ m/full/){
        if ($rank_apo ne "No"){
            $AoA[$index][4] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][5] = $rank_holo;
        }
    }
################################################################################
    $index+=4;

    if ($line =~ m/Smina/ and $line =~ m/rigide/){
        if ($rank_apo ne "No"){
            $AoA[$index][0] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][1] = $rank_holo;
        }
    }
    if ($line =~ m/Smina/ and $line =~ m/semi/){
        if ($rank_apo ne "No"){
            $AoA[$index][2] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][3] = $rank_holo;
        }
    }
    if ($line =~ m/Smina/ and $line =~ m/full/){
        if ($rank_apo ne "No"){
            $AoA[$index][4] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][5] = $rank_holo;
        }
    }
################################################################################
    $index+=4;

    if ($line =~ m/Vina/ and $line =~ m/rigide/ and $line !~ m/Vinardo/){
        if ($rank_apo ne "No"){
            $AoA[$index][0] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][1] = $rank_holo;
        }
    }
    if ($line =~ m/Vina/ and $line =~ m/semi/ and $line !~ m/Vinardo/){
        if ($rank_apo ne "No"){
            $AoA[$index][2] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][3] = $rank_holo;
        }
    }
    if ($line =~ m/Vina/ and $line =~ m/full/ and $line !~ m/Vinardo/){
        if ($rank_apo ne "No"){
            $AoA[$index][4] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][5] = $rank_holo;
        }
    }
################################################################################
    $index+=4;

    if ($line =~ m/Vinardo/ and $line =~ m/rigide/){
        if ($rank_apo ne "No"){
            $AoA[$index][0] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][1] = $rank_holo;
        }
    }
    if ($line =~ m/Vinardo/ and $line =~ m/semi/){
        if ($rank_apo ne "No"){
            $AoA[$index][2] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][3] = $rank_holo;
        }
    }
    if ($line =~ m/Vinardo/ and $line =~ m/full/){
        if ($rank_apo ne "No"){
            $AoA[$index][4] = $rank_apo;
        }
        if ($rank_holo ne "No"){
            $AoA[$index][5] = $rank_holo;
        }
    }
}


my @file = `cat $ARGV[0]`;

# python3 compute_ranks.py txt/Smina_rigide_files.txt apo rmsd 3

foreach my $line (@file){
    chomp $line;
    my @A = `python3 compute_ranks.py $line apo $ARGV[1] 1`;
    my @B = `python3 compute_ranks.py $line holo $ARGV[1] 1`;
    my $rank_apo = mean(\@A);
    my $rank_holo = mean(\@B);
    modify_AoA(0, $rank_apo, $rank_holo, $line);
    @A = `python3 compute_ranks.py $line apo $ARGV[1] 3`;
    @B = `python3 compute_ranks.py $line holo $ARGV[1] 3`;
    $rank_apo = mean(\@A);
    $rank_holo = mean(\@B);
    modify_AoA(1, $rank_apo, $rank_holo, $line);
    @A = `python3 compute_ranks.py $line apo $ARGV[1] 5`;
    @B = `python3 compute_ranks.py $line holo $ARGV[1] 5`;
    $rank_apo = mean(\@A);
    $rank_holo = mean(\@B);
    modify_AoA(2, $rank_apo, $rank_holo, $line);
    @A = `python3 compute_ranks.py $line apo $ARGV[1] 10`;
    @B = `python3 compute_ranks.py $line holo $ARGV[1] 10`;
    $rank_apo = mean(\@A);
    $rank_holo = mean(\@B);
    modify_AoA(3, $rank_apo, $rank_holo, $line);
}


for (my $i=0; $i <= 19; $i++){
    for (my $j=0; $j <= 5; $j++){
        print "$AoA[$i][$j];";
    }
    print "\n";
}
