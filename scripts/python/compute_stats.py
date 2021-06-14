import sys

# python3 compute_stats.py txt/Smina_semi_files.txt 5 apo 20

def compute_accuracy(input_file, delta, max_rmsd):
    list_ranks = []
    list_rmsds = []
    
    with open(input_file, 'r') as filein:
        for line in filein:
            stripped = line.strip("\n")
            rank, rmsd = stripped.split(' ')
            list_ranks.append(rank)
            list_rmsds.append(rmsd)
    
    correct = 0
    total = 0
    
    for i in range(0, len(list_ranks), 1):
        for j in range(i+1, len(list_ranks), 1):
            #print(list_ranks[i], ":", list_rmsds[i], "vs", list_ranks[j], ":", list_rmsds[j])
            diff = float(list_rmsds[i])-float(list_rmsds[j])
            if diff < 0:
                diff*=-1
            if diff > delta and float(list_rmsds[i]) < max_rmsd and float(list_rmsds[j]) < max_rmsd:
                if float(list_rmsds[i]) < float(list_rmsds[j]):
                    correct+=1
                    #print("^correct!")
                total+=1

    if (total > 0):    
        accuracy = (correct/total)*100
    else:
        accuracy = "n/a"
    
    return accuracy, total, input_file

################################################################################

list_of_files = sys.argv[1]

acc_sum = 0
n = 0

with open(list_of_files, 'r') as filein:
    for line in filein:
        if sys.argv[3] in line:
            (acc, tot, filename) = compute_accuracy(line.strip("\n"), float(sys.argv[2]), float(sys.argv[5]))
            if acc != "n/a" and tot > float(sys.argv[4]):
                acc_sum+=acc
                n+=1
            else:
                sys.stderr.write("Discard: "+filename+" "+str(acc)+" "+str(tot)+"\n")

if n > 0:
    result = acc_sum/n
    print(result, n)
else:
    print("No accuracy")
