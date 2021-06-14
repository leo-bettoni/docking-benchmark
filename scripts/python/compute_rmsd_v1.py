import sys

def compare_two_files(list1, list2):
    square = 0.0 # sum of squared distances
    for i in range(0, len(list1), 1):
        x1 = float(list1[i][30:38])
        y1 = float(list1[i][38:46])
        z1 = float(list1[i][46:54])

        x2 = float(list2[i][30:38])
        y2 = float(list2[i][38:46])
        z2 = float(list2[i][46:54])

        square += ( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )

    mean_square = square/len(list1)
    rmsd = mean_square**0.5
    return rmsd

################################################################################

if len(sys.argv) < 2:
    sys.exit("Error: missing arguments\nUse: python3 "+sys.argv[0]+" NATIVE.pdbqt MODELS.pdbqt")

allposes_file = sys.argv[1]
nativepose_file = sys.argv[2]

models = [] # will be a list of sublists (each sublist = a "MODEL", each element of the sublist = "ATOM" line)
sub_list = []
model_num_list = []

with open(allposes_file, 'r') as filein:
    for line in filein:
        if (line[0:5] == "MODEL"):
            model_number = line[6:9].strip("\n")
            model_num_list.append(model_number)
            sub_list = []
        elif (line[0:4] == "ATOM"):
            sub_list.append(line)
        elif (line[0:6] == "ENDMDL"):
            models.append(sub_list)

native_list = []

with open(nativepose_file, 'r') as filein:
    for line in filein:
        if (line[0:4] == "ATOM"):
            native_list.append(line)

for i in range(0, len(models), 1):
    rmsd = compare_two_files(native_list, models[i])
    print(model_num_list[i], rmsd)

