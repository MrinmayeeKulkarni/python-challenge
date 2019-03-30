import os
import csv
from collections import OrderedDict 
budgetdata_csv="../Resources/budget_data.csv"
profitloss=[]
with open(budgetdata_csv,newline="") as csvfile:
    csvreader=csv.DictReader(csvfile)
    header=next(csvreader)
    totalrows=0
    total=0
    for row in csvreader:
        totalrows +=1
        total=total+ float(row['Profit/Losses'])
        profitloss.append(float(row['Profit/Losses']))
        
    averagechange=total/totalrows
    maxvalue=max(profitloss)
    minvalue=min(profitloss)
    print("Financial Analysis")
    print("----------------------------------------------")
    print("Total Months: " + str(totalrows))
    print ("Total: $ "+str(total))
    print("Average Change: $ "+ str(round(averagechange,2)))
    csvfile.seek(0)
    header=next(csvreader)
    for row in csvreader:
       
        if float(row['Profit/Losses'])==maxvalue:
            print("Greatest increase in profits: "+row['Date']+" ($ "+str(maxvalue)+")")    
        if float(row['Profit/Losses'])==minvalue:
            print("Greatest decrease in losses: "+row['Date']+" ($ "+str(minvalue)+")")
            with open("output.txt", "w") as txt_file:
    
                txt_file.write("Financial Analysis \n")
                txt_file.write("---------------------------------------------- \n")
                txt_file.write("Total Months: " + str(totalrows) +"\n") 
                txt_file.write("Total: $ "+str(total)+"\n")
                txt_file.write("Average Change: $ "+ str(round(averagechange,2)) +"\n" )    
                txt_file.write("Greatest increase in profits: "+row['Date']+" ($ "+str(maxvalue)+") \n" )
                txt_file.write("Greatest decrease in losses: "+row['Date']+" ($ "+str(minvalue)+") \n" )

  
      
           
           
    
           
            
            

   

