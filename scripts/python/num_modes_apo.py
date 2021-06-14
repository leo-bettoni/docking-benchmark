import sys

fichier_1 = sys.argv[1] #pour ouvrir le fichier out
fichier_2 = sys.argv[2] #pour ouvrir le fichier log
ele1=""
ele2=fichier_1
if "//" in fichier_1:
	#print("Ok")
	ele1, ele2 = fichier_1.split("//")

pdb_code = ele1[-4:]

num_modes = 0
with open(fichier_1, 'r') as filin_1, open(fichier_2, "r") as filin_2, open("Bilan_dockings_apo.txt", "a") as sortie_1, open("Poses_apo.txt", "a") as sortie_2, open("Energies_apo.txt", "a") as sortie_3, open("RMSD_apo.txt", "a") as sortie_4:
	for line in filin_1:
		if line.startswith("MODEL"):
			num_modes += 1
	for ligne in filin_2:
		if ligne.startswith("1 "):
			energie = float(ligne[7:16])
		if num_modes > 1:
			if ligne.startswith("2 "):
				rmsd = float(ligne[18:26])
		else:
				rmsd = 0
	print("La structure holo {} comporte {} modes, la plus basse énergie est {:.3f} kcal/mol et le meilleur RMSD est {:.3f}".format(pdb_code, num_modes, energie, rmsd))
	sortie_1.write("La structure holo {} comporte {} modes, la plus basse énergie est {:.3f} kcal/mol et le meilleur RMSD est {:.3f}\n".format(pdb_code, num_modes, energie, rmsd))
	sortie_2.write("{}\n".format(num_modes))
	sortie_3.write("{:.3f}\n".format(energie))
	sortie_4.write("{:.3f}\n".format(rmsd))	

