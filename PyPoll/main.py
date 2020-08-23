#import data file
import os
import csv

#Setting Variables
Votes = []
County = []
Candidates = []
Khan = []
Correy = []
Li = []
OTooley = []

#connect directory
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

#setting the loop
    for row in csvreader:
    
#Setting Votes, Candidates, and County
        Votes.append(int(row[0]))
        County.append(row[1])
        Candidates.append(row[2])

#Calculating Total Votes
Total_Votes = (len(Votes))
print(Total_Votes)

#Calculating Votes per Person
for Candidate in Candidates:
    if Candidate == "Khan":
        Khan.append(Candidates)
        Khan_Votes = len(Khan)
    elif Candidate == "Correy":
        Correy.append(Candidates)
        Correy_Votes = len(Correy)
    elif Candidate == "Li":
        Li.append(Candidates)
        Li_Votes = len(Li)
    else:
        OTooley.append(Candidates)
        OTooley_Votes = len(OTooley)
print(Khan_Votes)
print(Correy_Votes)
print(Li_Votes)
print(OTooley_Votes)

#Calculating The Percentage of Votes Each Candidate Won
Khan_Percent = round(((Khan_Votes / Total_Votes) * 100), 2)
Correy_Percent = round(((Correy_Votes / Total_Votes) * 100), 2)
Li_Percent = round(((Li_Votes / Total_Votes) * 100), 2)
OTooley_Percent = round(((OTooley_Votes / Total_Votes) * 100), 2)
print(Khan_Percent)
print(Correy_Percent)
print(Li_Percent)
print(OTooley_Percent)

#Calculating The Winner of The Election
if Khan_Percent > max(Correy_Percent, Li_Percent, OTooley_Percent):
    winner = "Khan"
elif Correy_Percent > max(Khan_Percent, Li_Percent, OTooley_Percent):
    winner = "Correy"  
elif Li_Percent > max(Correy_Percent, Khan_Percent, OTooley_Percent):
    winner = "Li"
else:
    winner = "O'Tooley"

#Print To Get Final Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")
print(f"Khan: {Khan_Percent}% ({Khan_Votes}")
print(f"Correy: {Correy_Percent}% ({Correy_Votes}")
print(f"Li: {Li_Percent}% ({Li_Votes}")
print(f"OTooley: {OTooley_Percent}% ({OTooley_Votes}")
print("-------------------------")
print(f"winner: {winner}")
print("-------------------------")
