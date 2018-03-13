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
avgchange = []
BestIncrease = int(max(revchange))
WorstDecrease = int(min(revchange))

#def BestIncrease():
    #print(int(max(revchange)))


#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------


with open(pybank_csv, encoding="UTF-8", newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Skip Headers
    next(csvreader, None)

    for i,row in enumerate(csvreader):
        #Count Total Months
        totalmonths += (int(row[1]))
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
        else:
            print(int(revchange(max)))
            print(int(revchange(min)))
            avgchange.append(int(revchange) /(int(totalmonths)))        

            #BestIncrease=max(revchange)
            #min(revchange)=worst_decrease



        #elif i==max(revchange):
            #max(revchange)
            #min(revchange)
        
            #best_increase = int(best_increase) + int(max(revchange))

            #worst_decrease = int(worst_decrease) + int(min(revchange))

#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------

#Financial Analysis

Total Months: print(int(totalmonths))
Total Revenue: print(int(totalrev))
Average Revenue Change: print(int(avgchange))
Greatest Increase In Revenue: print(BestIncrease)
Greatest Decrease In Revenue: print(WorstDecrease)


#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------
        
        
# Import
import os
import csv

# Name path
pybank_csv = os.path.join("..", "PyBank", "budget_data_2.csv")

#Lists to store data
#date = []
#revenue = []

#Total counts
totalmonths = 0
totalrev = 0
revchange = []
avgchange = []
BestIncrease = int(max(revchange))
WorstDecrease = int(min(revchange))

#def BestIncrease():
    #print(int(max(revchange)))


#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------


with open(pybank_csv, encoding="UTF-8", newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Skip Headers
    next(csvreader, None)

    for i,row in enumerate(csvreader):
        #Count Total Months
        totalmonths += (int(row[1]))
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
        else:
            print(int(revchange(max)))
            print(int(revchange(min)))
            avgchange.append(int(revchange) /(int(totalmonths)))        

            #BestIncrease=max(revchange)
            #min(revchange)=worst_decrease



        #elif i==max(revchange):
            #max(revchange)
            #min(revchange)
        
            #best_increase = int(best_increase) + int(max(revchange))

            #worst_decrease = int(worst_decrease) + int(min(revchange))

#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------

#Financial Analysis

Total Months: print(int(totalmonths))
Total Revenue: print(int(totalrev))
Average Revenue Change: print(int(avgchange))
Greatest Increase In Revenue: print(BestIncrease)
Greatest Decrease In Revenue: print(WorstDecrease)

    
        
        