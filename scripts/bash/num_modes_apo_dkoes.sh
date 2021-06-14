for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/*/; do
	echo Processing structure $dir
	python3 /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/num_modes_apo.py $dir/out_apo.pdbqt $dir/log_apo.txt
done