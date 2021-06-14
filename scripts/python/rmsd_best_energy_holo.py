import sys

fichier = sys.argv[1] #pour ouvrir le fichier des RMSD

ele1=""
ele2=fichier
if "//" in fichier:
	#print("Ok")
	ele1, ele2 = fichier.split("//")

pdb_code = ele1[-4:]

with open(fichier, 'r') as filin, open("RMSD_associé_à_la_meilleure_affinité_holo.txt", "a") as filout:
	ligne = filin.readline()
	RMSD = float(ligne[2:])
	filout.write("{:.3f}\n".format(RMSD))
