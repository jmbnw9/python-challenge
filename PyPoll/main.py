import os
import csv

#Path to Election dataset in resource folder
csvpath = os.path.join("Resources", "election_data.csv")

#Define how to pull the total votes
total_votes = 0

# Counting the options for candidates and their votes
different_candidates = []
votes_per_candidate = []


#Import and read csv file
with open(csvpath, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    #Find the total number of votes
    for row in csv_reader:
        total_votes += 1
        candidates = (row[2])
        if candidates in different_candidates:
            candidate_index = different_candidates.index(candidates)
            votes_per_candidate[candidate_index] = votes_per_candidate[candidate_index] + 1
        else:
            different_candidates.append(candidates)
            votes_per_candidate.append(1)

percent = []
max_votes = votes_per_candidate[0]
max_index = 0

for x in range(len(different_candidates)):
    vote_percent = round(votes_per_candidate[x]/total_votes*100, 2)
    percent.append(vote_percent)
    if votes_per_candidate[x] > max_votes:
        max_votes = votes_per_candidate[x]
        max_index = x

election_winner = different_candidates[max_index]

#print the results terminal
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"----------------")
for x in range(len(different_candidates)):
    print(f"{different_candidates[x]} : {percent[x]}% ({votes_per_candidate[x]})")
print(f"----------------")
print(f"Winner: {election_winner.upper()}")
print(f"----------------")

#print results to text file
output_file = os.path.join("Results.txt")

with open(output_file, "w", newline= "") as datafile:

    datafile.write("Election Results\n")
    datafile.write("----------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("----------------\n")
    for x in range(len(different_candidates)):
        datafile.write(f"{different_candidates[x]} : {percent[x]}% ({votes_per_candidate[x]})\n")
    datafile.write("----------------\n")
    datafile.write(f"Winner: {election_winner.upper()}\n")
    datafile.write("----------------\n")