import sys
import math


fichier_1 = sys.argv[1] #pour ouvrir rec_b_protone.pdbqt
fichier_2 = sys.argv[2] #pour ouvrir centre_masse_ligand.txt
ele1=""
ele2=fichier_1
if "//" in fichier_1:
	#print("Ok")
	ele1, ele2 = fichier_1.split("//")

pdb_code = ele1[-4:]

coordonnees_X = []
coordonnees_Y = []
coordonnees_Z = []
distances = []
fichier = []
with open(fichier_1, 'r') as filin, open("centre_de_masse.txt", 'w') as filout, open("Commandes_docking.txt", "a") as sortie, open (fichier_2, "r") as dale:
	for line in filin:
		fichier.append(line)
		if line[0:4] == "ATOM":
			X = line[30:38]
			Y = line[38:46]
			Z = line[46:54]
			coordonnees_X.append(float(X))
			coordonnees_Y.append(float(Y))
			coordonnees_Z.append(float(Z))
	X_moyen = sum(coordonnees_X)/len(coordonnees_X)
	Y_moyen = sum(coordonnees_Y)/len(coordonnees_Y)
	Z_moyen = sum(coordonnees_Z)/len(coordonnees_Z)
	for line in fichier:
		if line[0:4] == "ATOM":
			X = line[30:38]
			Y = line[38:46]
			Z = line[46:54]
			d = math.sqrt((X_moyen-float(X))**2 + (Y_moyen-float(Y))**2 + (Z_moyen-float(Z))**2)
			distances.append(d)
	print("Les coordonnées du centre de masse sont {:.3f}, {:.3f}, {:.3f}".format(X_moyen, Y_moyen, Z_moyen))
	filout.write("Les coordonnées du centre de masse sont {:.3f}, {:.3f}, {:.3f}".format(X_moyen, Y_moyen, Z_moyen))
	plus_grande_distance = max(distances)
	arete = plus_grande_distance*2
	print("La plus grande distance est {:.3f} angström".format(plus_grande_distance))
	filout.write("\nLa plus grande distance est {:.3f} angström".format(plus_grande_distance))
	for line in dale:
		if line[0:2] == "La":
			d_ligand = float(line[27:34])
			size = arete + d_ligand + 4
	#préparation des lignes de commandes pour le docking
	sortie.write("smina --scoring ad4_scoring -r /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/{}/rec_b_protone.pdbqt -l /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/{}/pep_b_protone.pdbqt --center_x {:.3f} --center_y {:.3f} --center_z {:.3f} --size_x {:.3f} --size_y {:.3f} --size_z {:.3f} --out /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/{}/out_holo.pdbqt --log /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Autodock4/{}/log_holo.txt --num_modes 50 --cpu 32\n".format(pdb_code, pdb_code, X_moyen, Y_moyen, Z_moyen, size, size, size, pdb_code, pdb_code))
	sortie.write("smina --scoring dkoes_scoring -r /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/{}/rec_b_protone.pdbqt -l /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/{}/pep_b_protone.pdbqt --center_x {:.3f} --center_y {:.3f} --center_z {:.3f} --size_x {:.3f} --size_y {:.3f} --size_z {:.3f} --out /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/{}/out_holo.pdbqt --log /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Dkoes/{}/log_holo.txt --num_modes 50 --cpu 32\n".format(pdb_code, pdb_code, X_moyen, Y_moyen, Z_moyen, size, size, size, pdb_code, pdb_code))
	sortie.write("smina --scoring default -r /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Smina/{}/rec_b_protone.pdbqt -l /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Smina/{}/pep_b_protone.pdbqt --center_x {:.3f} --center_y {:.3f} --center_z {:.3f} --size_x {:.3f} --size_y {:.3f} --size_z {:.3f} --out /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Smina/{}/out_holo.pdbqt --log /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Smina/{}/log_holo.txt --num_modes 50 --cpu 32\n".format(pdb_code, pdb_code, X_moyen, Y_moyen, Z_moyen, size, size, size, pdb_code, pdb_code))
	sortie.write("smina --scoring vina -r /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vina/{}/rec_b_protone.pdbqt -l /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vina/{}/pep_b_protone.pdbqt --center_x {:.3f} --center_y {:.3f} --center_z {:.3f} --size_x {:.3f} --size_y {:.3f} --size_z {:.3f} --out /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vina/{}/out_holo.pdbqt --log /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vina/{}/log_holo.txt --num_modes 50 --cpu 32\n".format(pdb_code, pdb_code, X_moyen, Y_moyen, Z_moyen, size, size, size, pdb_code, pdb_code))
	sortie.write("smina --scoring vinardo -r /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vinardo/{}/rec_b_protone.pdbqt -l /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vinardo/{}/pep_b_protone.pdbqt --center_x {:.3f} --center_y {:.3f} --center_z {:.3f} --size_x {:.3f} --size_y {:.3f} --size_z {:.3f} --out /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vinardo/{}/out_holo.pdbqt --log /home/etudiant/Léo/Stage_M2/Banques_de_donnees/Banque_rigide/Vinardo/{}/log_holo.txt --num_modes 50 --cpu 32\n".format(pdb_code, pdb_code, X_moyen, Y_moyen, Z_moyen, size, size, size, pdb_code, pdb_code))




