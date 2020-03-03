import os
import csv

poll_csv = os.path.join('.', 'Resources', 'election_data.csv')

#let's declare variables to keep track of what we are measuring
total_votes=0
#all_candidates=[]
votedict = dict()

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #move past header row
    csv_header = next(csvreader)
    
    #Print data rows
    for row in csvreader:
        total_votes=total_votes+1
        candidate = row[2]+' '+row[1]
        #if candidate not in all_candidates:
            #all_candidates.append(candidate)
        #increment vote if candidate is recognized
        if candidate in votedict: 
            votedict[candidate] = votedict[candidate] + 1
        else: 
            #Add candidate with one vote
            votedict[candidate] = 1
    winner=key
    for key in list(votedict.keys()): 
        print(key, "received", votedict[key],'votes which is', 100*round((votedict[key]/total_votes),3),'% of the total')
        if votedict[key] > votedict[winner]:
            winner=key
    print(winner, 'is the winner of the election')
    
pollpy_output = open("pollpy_output.txt","a")#append mode
pollpy_output.write("Election Results \n") 
pollpy_output.write("---------------------------- \n") 
pollpy_output.write(f"{total_votes} total votes \n") 
pollpy_output.write("---------------------------- \n") 
for key in list(votedict.keys()):
    pollpy_output.write(f"{key} received {votedict[key]} votes which is {100*round((votedict[key]/total_votes),3)}% of the total \n") 
pollpy_output.write("---------------------------- \n") 
pollpy_output.write(f"{winner} wins the election \n") 
pollpy_output.write("---------------------------- \n") 
pollpy_output.close()