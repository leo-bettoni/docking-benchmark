for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/*/; do
	echo Processing structure $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/num_modes_holo.py $dir/out_holo.pdbqt $dir/log_holo.txt
done