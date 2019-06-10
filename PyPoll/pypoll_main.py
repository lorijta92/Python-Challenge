from collections import Counter
import os
import csv

csvpath = ("election_data.csv")
votes = []

with open(csvpath) as csvfile:
    voteinfo = csv.reader(csvfile)
    next(voteinfo)

    for row in voteinfo:
        votes.append(row[2])

counts = Counter(votes) #Grab candidate names and number of vote per

keys = counts.keys() #Separate candidate names from votes
cand_names = list(keys)

values = counts.values() #Separate votes from candidate names
cand_votes = list(values)

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {len(votes)}")
print(f"{cand_names[0]}: {round((cand_votes[0]/len(votes)*100), 2)}% ({cand_votes[0]})") #brute force, need to refine
print(f"{cand_names[1]}: {round((cand_votes[1]/len(votes)*100), 2)}% ({cand_votes[1]})")
print(f"{cand_names[2]}: {round((cand_votes[2]/len(votes)*100), 2)}% ({cand_votes[2]})")
print(f"{cand_names[3]}: {round((cand_votes[3]/len(votes)*100), 2)}% ({cand_votes[3]})")
print("--------------------------------")
#print(f"Winner: {Winner}")