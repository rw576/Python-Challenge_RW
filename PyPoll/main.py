#import data file
import os
import csv

#connect directory
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    print(reader)

#set variables
Votes = []
County = []
Candidates = []
Khan = []
Correy = []
Li = []
OTooley = []

#Setting Votes, Candidates, and County
for row in csvreader:
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
Li_Percent = round(((Li_votes / Total_votes) * 100), 2)
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
print(f"Election Results", file=text_file)
print(f"-----------------------------------", file=text_file) 
print(f"Total Votes: {Total_Votes}", file=text_file)
print(f"-----------------------------------", file=text_file) 
print(f"Khan: {Khan_Percent}% ({Khan_Votes})"), file=text_file)
print(f"Correy: {Correy_Percent}% ({Correy_Votes})"), file=text_file)
print(f"Li: {Li_Percent}% ({Li_Votes})"), file=text_file)
print(f"OTooley: {OTooley_Percent}% ({OTooley_Votes})"), file=text_file)
print(f"-----------------------------------", file=text_file)
print(f"winner: {winner}"), file=text_file)
print(f"-----------------------------------")

