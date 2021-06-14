for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/*/; do
	echo Processing structure $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/best_rmsd_holo.py $dir/comparaison_rmsd_holo.txt
done