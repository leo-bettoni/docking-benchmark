import sys

def compute_top(input_list, topnum, index):
    sum_var=0
    for i in range(0, topnum, 1):
        sum_var+=input_list[i][index]
    avg_var = sum_var/topnum
    print(avg_var)

################################################################################

def main(input_file, criterion, top):
    list_2d = []
    
    with open(input_file, 'r') as filein:
        for line in filein:
            stripped = line.strip("\n")
            rank, rmsd = stripped.split(' ')
            list_2d.append([int(rank), float(rmsd)])

    if len(list_2d) >= top:    
        #print(list_2d)
        if criterion == "rmsd":
            compute_top(list_2d, int(top), 1)
        
        list_sorted = sorted(list_2d, key=lambda x: x[1])
        #print(list_sorted)
        
        if criterion == "rank":
            compute_top(list_sorted, int(top), 0)


mylist = sys.argv[1]
apo_holo = sys.argv[2]
crit = sys.argv[3]
mytop = sys.argv[4]

with open(mylist, 'r') as filein:
    for line in filein:
        if apo_holo in line:
            main(line.strip("\n"), crit, int(mytop))
