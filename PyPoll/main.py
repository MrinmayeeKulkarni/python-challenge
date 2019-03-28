import os
import csv
from collections import defaultdict, Counter
electiondata_csv="../LearnPython/Hw/election_data.csv"
with open(electiondata_csv,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    data = defaultdict(list)
    for row in csvreader:
        totalvotes=len(row[0]-1)
        data[row[2]]
        for k in data.items():
             name=k
             count=Counter(k)
        print(name)
        print(count)
        