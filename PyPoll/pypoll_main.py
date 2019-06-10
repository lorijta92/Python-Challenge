from collections import Counter
import csv

csvpath = ("election_data.csv")
candidates = []

with open(csvpath) as csvfile:
    voteinfo = csv.reader(csvfile)
    next(voteinfo)

    for row in voteinfo:
        candidates.append(row[2]) #store all votes in list

results = Counter(candidates) #Grab candidate names and number of vote per candidate
keys = results.keys() #Separate candidate names from votes
unique_candidates = list(keys) #Store candidate names as a list

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {len(candidates)}") #total votes
print("--------------------------------")
for candidate_name, candidate_votes in results.items():
    print(f"{candidate_name}: {round((candidate_votes/len(candidates) * 100), 2)}% ({candidate_votes})")
print("--------------------------------")
print(f"Winner: {unique_candidates[0]}")
print("--------------------------------")