import os
import csv
budgetdata_csv="../Resources/budget_data.csv"
with open(budgetdata_csv,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        if (len(row[0])==0):
            total=0
            total=total+ int(row[1])
            average=total/(len(row[0])
            maximum=max(int(row[1])for row in csvreader)
            minimum=min(int(row[1])for row in csvreader)
    print("Financial Analysis")
    print("----------------------------------------------")
    print("Total Months:" + str(len(row[0]))
    print ("$"+total)
    print("Average Change: $"+ average)
    print("Greatest increase in profits:"+row[0]+"$"+maximum)
    print("Greatest decrease in losses:"+row[0]+"$"+minimum)


