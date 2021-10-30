# modules
import os
import csv

# file path
input_file = os.path.join('Resources', 'election_data.csv')

# open csv file
with open(input_file) as elections:

    csvreader = csv.reader(elections,delimiter=",")
    print(f"{csvreader}")
    header = next(csvreader)
    print(header)