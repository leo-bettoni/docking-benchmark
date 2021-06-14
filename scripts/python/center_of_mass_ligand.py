import sys
import math


fichier = sys.argv[1]
ele1, ele2 = fichier.split("//")

pdb_code = ele1[-4:]

coordonnees_X = []
coordonnees_Y = []
coordonnees_Z = []
distances = []
document = []
with open(fichier, 'r') as filin, open("centre_de_masse_ligand.txt", 'w') as filout:
	for line in filin:
		document.append(line)
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
	for line in document:
		if line[0:4] == "ATOM":
			X = line[30:38]
			Y = line[38:46]
			Z = line[46:54]
			d = math.sqrt((float(X_moyen)-float(X))**2 + (float(Y_moyen)-float(Y))**2 + (float(Z_moyen)-float(Z))**2)
			distances.append(d)
	print("Les coordonnées du centre de masse sont {:.3f}, {:.3f}, {:.3f}".format(X_moyen, Y_moyen, Z_moyen))
	filout.write("Les coordonnées du centre de masse sont {:.3f}, {:.3f}, {:.3f}".format(X_moyen, Y_moyen, Z_moyen))
	plus_grande_distance = max(distances)
	arete = plus_grande_distance*2
	print("La plus grande distance est {:.3f} angström".format(arete))
	filout.write("\nLa plus grande distance est {:.3f} angström".format(arete))
	

	


