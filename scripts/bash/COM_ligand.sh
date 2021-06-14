for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/*/*/; do
	echo processing ligand $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/center_of_mass_ligand.py $dir/pep_b_protone.pdbqt
	mv centre_de_masse_ligand.txt $dir
done