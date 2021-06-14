import sys

fichier = sys.argv[1] #pour ouvrir le fichier comparaison_rmsd_holo.txt

liste_rmsd = []
with open(fichier, 'r') as filin, open("Bilan RMSD holo", "a") as sortie_1, open("Bilan classement holo", "a") as sortie_2:
	for ligne in filin:
		if ligne.startswith("100"):
			rmsd = ligne[3:]
		else:
			rmsd = ligne[2:]
		liste_rmsd.append(float(rmsd))
	best_rmsd = min(liste_rmsd)
	indice_best_rmsd = liste_rmsd.index(best_rmsd) + 1
	sortie_1.write("{:.3f}\n".format(best_rmsd))
	sortie_2.write("{}\n".format(indice_best_rmsd))
		

