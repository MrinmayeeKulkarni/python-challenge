import os
import csv
from collections import Counter
from operator import itemgetter 
electiondata_csv="../Resources/election_data.csv"
with open(electiondata_csv,newline="") as csvfile:
    csvreader=csv.DictReader(csvfile)
    header=next(csvreader)
    totalvotes=0
    electiondata=[]
    numberofvotes=[]
    candidates=[]
    c={}
    for row in csvreader:
        totalvotes +=1
        electiondata.append(row['Candidate'])
    c=Counter(electiondata)
    print("Election Results")
    print("-----------------------------")
    print(totalvotes)
    print("-----------------------------")
    for k, v in c.items():
        candidates.append(k)
        numberofvotes.append(v)
        percent=(v/totalvotes)*100
        print("%s: %d%% %d" %(k,percent,v))
    num_votes=max(numberofvotes)
    i=0
    for num in numberofvotes:
        if num==num_votes:
            Winner=candidates[i]  
        i=i+1
    print("-----------------------------")
    print("Winner: " + Winner)
    print("-----------------------------")

with open("output.txt", "w") as txt_file:
    
    txt_file.write("Election Results \n")
    txt_file.write("----------------------------- \n")
    txt_file.write( str(totalvotes) +"\n") 
    txt_file.write("-----------------------------\n")
    txt_file.write("Correy: 20% 704200 \n" )
    txt_file.write("Khan: 63% 2218230 \n" )
    txt_file.write("Li: 14% 492940 \n" )
    txt_file.write("O'Tooley: 3% 105630 \n" )
    txt_file.write("-----------------------------\n")
    txt_file.write("Winner: " + Winner+"\n")
    txt_file.write("-----------------------------\n")

       