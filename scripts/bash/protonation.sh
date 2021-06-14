for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_semi_flexible/*/*/; do
	echo processing ligand $dir
	pdb2pqr --ff=AMBER --ffout=AMBER --noopt --with-ph=7.0 $dir/pep_b.pdb pep_b_protone.pqr
	mv pep_b_protone.pqr $dir
done
