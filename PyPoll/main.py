# Import
import os
import csv

# Name path
pypoll_csv = os.path.join("..", "PyPoll", "election_data_1.csv")

# Lists to store data
totalv = []
candidates = []
vote_percent = []
Vestal_votes = []
Torres_votes = []
Seth_votes = []
Cordin_votes = []

#def candidates(csvreader)
    #print("The values within the list are...")
#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------

with open(pypoll_csv, encoding="UTF-8", newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Skip Headers
    next(csvreader, None)

    for i,row in csvreader:
        #Count Total Votes Cast
        totalv.append(row[0])

        #print (totalvotes)
        print(str(len(totalv)))

        #List of Candidates Receiving Votes
        candidates.append(row[2])

        #Percentage of votes each candidate won

        if i==Torres:
            Torres_votes += (int(row[2]))

        elif i==Vestal 
            Vestal_votes += (int(row[2])
        
        elif i==Seth
            Seth_votes += (int(row[2]))
        else:
            Cordin_votes += (int(row[2])) 

Election Results

Total Votes: print(int(totalv))
Candidates: print(str(candidates))

#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------
     
# Import
import os
import csv

# Name path
pypoll_csv = os.path.join("..", "PyPoll", "election_data_2.csv")

# Lists to store data
totalv = []
candidates = []
vote_percent = []
Li_votes = []
OTooley_votes = []
Khan_votes = []
Correy_votes = []

#def candidates(csvreader)
    #print("The values within the list are...")
#------------------------------------------------------------------
###################################################################
#------------------------------------------------------------------

with open(pypoll_csv, encoding="UTF-8", newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #Skip Headers
    next(csvreader, None)

    for i,row in csvreader:
        #Count Total Votes Cast
        totalv.append(row[0])

        #print (totalvotes)
        print(str(len(totalv)))

        #List of Candidates Receiving Votes
        candidates.append(row[2])

        #Percentage of votes each candidate won

        if i==Li:
            Li_votes += (int(row[2]))

        elif i==O'Tooley
            O'Tooley_votes += (int(row[2])
        
        elif i==Khan
            Khan_votes += (int(row[2]))
        else:
            Correy_votes += (int(row[2])) 

Election Results

Total Votes: print(int(totalv))
Candidates: print(str(candidates))
         



