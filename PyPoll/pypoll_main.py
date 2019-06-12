from collections import Counter
import csv

csvpath = ("election_data.csv")
candidates = []

with open(csvpath) as csvfile:
    voteinfo = csv.reader(csvfile)
    next(voteinfo)

    for row in voteinfo:
        candidates.append(row[2]) # Store all votes in a list

results = Counter(candidates) # Grab candidate names and number of vote per candidate
keys = results.keys() # Separate candidate names from votes
unique_candidates = list(keys) # Store candidate names as a list

# Print to Terminal
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {len(candidates)}") # Total votes
print("--------------------------------")
for candidate_name, candidate_votes in results.items(): # Candidate name, percentage of votes won, total votes won
    print(f"{candidate_name}: {round((candidate_votes/len(candidates) * 100), 2)}% ({candidate_votes})") #file.write
print("--------------------------------")
print(f"Winner: {unique_candidates[0]}") # Winner by popular vote
print("--------------------------------")

# Write text file
file = open("Election_Analysis_Summary.txt", "w")
file.write("Election Results\n")
file.write("--------------------------------\n")
file.write(f"Total Votes: {len(candidates)}\n") # Total votes
file.write("--------------------------------\n")
for candidate_name, candidate_votes in results.items(): # Candidate name, percentage of votes won, total votes won
    file.write(f"{candidate_name}: {round((candidate_votes/len(candidates) * 100), 2)}% ({candidate_votes})\n") #file.write
file.write("--------------------------------\n")
file.write(f"Winner: {unique_candidates[0]}\n") # Winner by popular vote
file.write("--------------------------------\n")
file.close()
