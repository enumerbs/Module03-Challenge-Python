# --------------------------------------------------------------------------------------
# PyPoll - main.py
# --------------------------------------------------------------------------------------

import os
import csv

# --------------------------------------------------------------------------------------

# Path to collect data from this project's Resources folder
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Path to election analysis tally file
election_analysis_txt = os.path.join("PyPoll", "analysis", "election_results.txt")

# --------------------------------------------------------------------------------------

# Intermediate data store for election votes tally
tally = {}

# --------------------------------------------------------------------------------------

# Function that tallys the votes
def analyse_election(datarow, tally):
    # Interpret / retrieve data values
    candidate = datarow[2]
    ballot_id = datarow[0]
    if (ballot_id != ""):
        # Add the candidate to the list of candidates who received votes (if not already listed).
        if candidate not in tally:
            tally[candidate] = 0   # Initialise this candidate's vote count
        # Increment the number of votes for this candidate
        tally[candidate] += 1

# --------------------------------------------------------------------------------------

# Read in and process the CSV data file
with open(election_data_csv, 'r') as csvfile:

    # Parse the data fields based on comma delimiters
    csvreader = csv.reader(csvfile, delimiter=',')

    # Consume (skip) the data file header row
    header = next(csvreader)

    # Iterate over the data
    for datarow in csvreader:
        analyse_election(datarow, tally)

# --------------------------------------------------------------------------------------

# Analyse election tally to determine the winner
winner = ""
winner_votes = 0
total_votes = 0
for candidate, candidate_votes in tally.items():
    # Update the total number of votes
    total_votes += candidate_votes
    # Determine the candidate who won
    if (candidate_votes > winner_votes):
        winner_votes = candidate_votes
        winner = candidate

# Calculate and save each candidate's results summary (count and proportion of votes)
candidate_summary = {}
for candidate, candidate_votes in tally.items():
    candidate_summary[candidate] = (candidate_votes, candidate_votes / total_votes)

# --------------------------------------------------------------------------------------

# Format then output election analysis / votes tally summary
str_total_votes = f"Total Votes: {total_votes}"
str_candidate_summary = [f"{candidate}: {candidate_stats[1]:.3%} ({candidate_stats[0]})" for candidate, candidate_stats in candidate_summary.items()]
str_winner = f"Winner: {winner}"

# Output to the console...

print("Election Results")
print("-------------------------")
print(str_total_votes)
print("-------------------------")
for str_result in str_candidate_summary:
    print(str_result)
print("-------------------------")
print(str_winner)
print("-------------------------")

# ..and to a file.

with open(election_analysis_txt, 'w') as txtfile:
    # Output results header
    print("Election Results", file=txtfile)
    print("-------------------------", file=txtfile)
    # Output results statistics
    print(str_total_votes, file=txtfile)
    print("-------------------------", file=txtfile)
    for str_result in str_candidate_summary:
        print(str_result, file=txtfile)
    print("-------------------------", file=txtfile)
    print(str_winner, file=txtfile)
    print("-------------------------", file=txtfile)

# --------------------------------------------------------------------------------------
