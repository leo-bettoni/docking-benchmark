import sys
from scipy.stats.stats import pearsonr
import math

# python3 compute_stats.py txt/Smina_semi_files.txt 5 apo 20

def compute_accuracy(input_file):
    #list_ranks = []
    list_rmsds = []

    liste_scores = []
    ele = input_file.split('/')
    pathname = input_file.replace(ele[-1], '')
    logfile = pathname+'log_'+sys.argv[3]+'.txt'

    start = False
    with open(logfile, 'r') as filein:
        for line in filein:
            if start:
                cols = line.split()
                liste_scores.append(float(cols[1]))
            if line[0:2] == '--':
                start = True
    
    with open(input_file, 'r') as filein:
        for line in filein:
            stripped = line.strip("\n")
            rank, rmsd = stripped.split(' ')
            #list_ranks.append(rank)
            list_rmsds.append(float(rmsd))

    if len(list_rmsds) != len(liste_scores):
        #print(input_file) # XXX XXX XXX XXX XXX
        return (0, 0)
    else:
        #print(list_rmsds, liste_scores)
        return pearsonr(list_rmsds, liste_scores)
        #return (1, 1)
    
#    correct = 0
#    total = 0
#    
#    for i in range(0, len(list_ranks), 1):
#        for j in range(i+1, len(list_ranks), 1):
#            #print(list_ranks[i], ":", list_rmsds[i], "vs", list_ranks[j], ":", list_rmsds[j])
#            diff = float(list_rmsds[i])-float(list_rmsds[j])
#            if diff < 0:
#                diff*=-1
#            if diff > delta and float(list_rmsds[i]) < max_rmsd and float(list_rmsds[j]) < max_rmsd:
#                if float(list_rmsds[i]) < float(list_rmsds[j]):
#                    correct+=1
#                    #print("^correct!")
#                total+=1
#
#    if (total > 0):    
#        accuracy = (correct/total)*100
#    else:
#        accuracy = "n/a"
#    
#    return accuracy, total, input_file

################################################################################

list_of_files = sys.argv[1]

acc_sum = 0
n = 0

# python3 compute_stats2.py txt/Autodock4_rigide_files.txt 1 apo 30 2> errz

with open(list_of_files, 'r') as filein:
    for line in filein:
        if sys.argv[3] in line and not '2xs1' in line:
            (acc, pvalue) = compute_accuracy(line.strip("\n"))
            #print(acc)
            #if acc != "n/a" and tot > float(sys.argv[4]):
            if not math.isnan(acc) and acc != 0:
                acc_sum+=acc
                n+=1
            else:
                #sys.stderr.write("Discard: "+filename+" "+str(acc)+" "+str(tot)+"\n")
                sys.stderr.write("Discard: "+" "+str(acc)+" "+"\n")

if n > 0:
    result = acc_sum/n
    print(result, n)
else:
    print("No accuracy")
