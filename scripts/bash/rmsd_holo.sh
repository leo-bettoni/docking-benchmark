for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/*/; do
	echo Processing structure $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/compute_rmsd_v1.py $dir/out_holo.pdbqt $dir/pep_b_protone.pdbqt > comparaison_rmsd_holo.txt
	mv comparaison_rmsd_holo.txt $dir
done