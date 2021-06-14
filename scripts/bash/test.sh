for dir in /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_semi_flexible/Autodock4/*/; do
	echo processing ligand $dir
	/home/etudiant/Programmes/Programme_docking/mgltools_x86_64Linux2_1.5.6/bin/pythonsh /home/etudiant/Programmes/Programme_docking/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l $dir/pep_b_protone.pqr -B none
	mv pep_b_protone.pdbqt $dir
done