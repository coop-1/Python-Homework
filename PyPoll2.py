import os
import csv

csvpath = os.path.join('..','LearnPython','election_data.csv')

results = []
unique = []

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        results.append(row[2])

#identify unique names in raw data
unique = list(set(results))

#use agg dictionary to create running total for each name
agg = {x: 0 for x in unique}

#running total for each name
for x in range(0,len(results)):
    agg[str(results[x])]+=1

#initialize total counter
total = 0

#loop through agg dictionary to get total votes
for key in agg:
    total = total + agg[key]

#print results
with open("Election Results.txt","w") as f:
    f.write("\n")
    f.write("Election Results")
    f.write("\n___________________________________")
    f.write("\n")
    f.write(f"\nTotal Votes: {total:,d}")
    f.write("\n___________________________________")
    f.write("\n")
    f.write("\nParticipants:")
    f.write("\n")
    for key in agg:
        num = agg[key]
        f.write(f"\n{key}: {round((agg[key]/total)*100)}% | Total Votes: {num:,d}")
    f.write("\n___________________________________")
    f.write("\n")

    #finding winner
    maxvotes = []
    for key in agg:
        maxvotes.append(agg[key])
    for key in agg:
        if agg[key] == max(maxvotes):
            winner = key

    f.write(f"\nWinner: {winner} with {max(maxvotes):,d} votes!")
    f.write("\n")




    


