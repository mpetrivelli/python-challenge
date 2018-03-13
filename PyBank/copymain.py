# Import
import os
import csv

# Name path
pybank_csv = os.path.join("..", "PyBank", "budget_data_1.csv")

#Lists to store data
#date = []
#revenue = []

#Total counts
totalmonths = 0
totalrev = 0
revchange = []


#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------


with open(pybank_csv, encoding="UTF-8", newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Skip Headers
    next(csvreader, None)

    for i,row in enumerate(csvreader):
        #Count Total Months
        totalmonths += int(row[0])
        #print (totalmonths)
        
        #Count Total Revenue Gained Over Entire Period
        #totalrev.append(row[1])
        #totalrev=totalrev + int(row[1])
        totalrev += int(row[1])

        if i==0:
            rev=int(row[1])

        elif i!=0:
            revchange.append(int(row[1])-rev)
            rev=int(row[1])

                  
        #if i<0:
            #revchange.append(int(row[1])+rev)
            #rev=int(row[1])

        #elif i>0:
            #revchange.append(int(row[1])-rev)
            #rev=int(row[1])



    
        
        