for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/*/*/; do
	echo processing ligand $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/center_of_mass.py $dir/rec_b_protone.pdbqt $dir/centre_de_masse_ligand.txt
	mv centre_de_masse.txt $dir
done