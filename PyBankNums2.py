import os
import csv

csvpath = os.path.join('..','LearnPython','PyBank.csv')

results = []

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        results.append(row)

x = 0
PnL = 0
jump = ['Month',0]
dip = ['Month',0]
lastmonth = 0
average = []

totaldiff = 0

for x in range(0,len(results)):
    temp = results[x][1]
    temp = int(temp)
    PnL = temp + PnL
    lastmonth = results[x-1][1]
    lastmonth = int(lastmonth)

    if x >= 1:
        if jump[1] < temp - lastmonth:
            jump[1] = temp - lastmonth
            jump[0] = results[x][0]

        if dip[1] < lastmonth - temp:
            dip[1] = lastmonth - temp
            dip[0] = results[x][0]
        
        difference = int(temp - lastmonth)
        average.append(difference)

finalaverage = sum(average)/(len(average))

with open("Financial Report.txt","w") as f:
    f.write("\nFINANCIAL ANALYSIS")
    f.write ("\n_______________________________________________________")
    f.write (f"\n")
    f.write (f"\nTotal Months: {len(results)}")
    f.write(f"\nTotal: ${PnL}")
    f.write(f"\nAverage Change: ${round(finalaverage,2)}")
    f.write(f"\nGreatest Increase in Profits: ${jump[1]} | Month: {jump[0]}")
    f.write(f"\nGreatest Decrease in Profits: -${dip[1]} | Month: {dip[0]}")
    f.write ("\n_______________________________________________________")
    f.write("\n")
