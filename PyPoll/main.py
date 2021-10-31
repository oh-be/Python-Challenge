### PyPoll - Python Challenge - Week 3

# modules
import os
import csv
# from collections import Counter, defaultdict, OrderedDict 
###^^^^(used to find candidates)

# file path
input_file = os.path.join('Resources', 'election_data.csv')

# variables / vote counters
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open csv file
with open(input_file) as elections:

    # create variable for contents of file
    csvreader = csv.reader(elections,delimiter=",")
    header = next(csvreader)

    # print(header) 'checked what index candidates is on
    ### used code below to filter candidates:Khan, Correy, Li, O'Tooley
    # seen = defaultdict(set)
    # counts = Counter(row[2] 
    # for row in csvreader)
    # print(counts) 
    # also pulled number of votes per candidate (used to verify final print result and winner = Khan)

    # iterate through rows
    for row in csvreader:

            # sum up total votes / per unique voter ID
            total_votes += 1

            # conditional to find and add up votes per candidate ## added to vote counter list -lines 11-14
            if row[2] == "Khan":
                khan_votes += 1
            elif row[2] == "Correy":
                correy_votes += 1
            elif row[2] == "Li":
                li_votes += 1
            elif row[2] == "O'Tooley":
                otooley_votes += 1

# variables to convert totals into percentage format
khan_percent = (khan_votes/total_votes) * 100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes) * 100
otooley_percent = (otooley_votes/total_votes) * 100

# find winner
# create dictionary
candidates_votes = {"Khan":khan_votes, "Correy":correy_votes, "Li":li_votes, "O'Tooley":otooley_votes}
# find winner using max function on candidates vote dictionary
winner = max(candidates_votes, key=candidates_votes.get)

# copy pasted summary table from readme guide
# and converted to f'strings plugging in results
print(f"****Election Results****")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {khan_percent:.0f}% ({khan_votes})")
print(f"Correy: {correy_percent:.0f}% ({correy_votes})")
print(f"Li: {li_percent:.0f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.0f}% ({otooley_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Output files
output_file = os.path.join('analysis', 'poll_analysis.txt')

#  Open the output file
with open(output_file, "w") as file:
    
    # write data into text file
    file.write(f"****Election Results****\n")
    file.write(f"-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"-------------------------\n")
    file.write(f"Khan: {khan_percent:.0f}% ({khan_votes})\n")
    file.write(f"Correy: {correy_percent:.0f}% ({correy_votes})\n")
    file.write(f"Li: {li_percent:.0f}% ({li_votes})\n")
    file.write(f"O'Tooley: {otooley_percent:.0f}% ({otooley_votes})\n")
    file.write(f"-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"-------------------------\n")