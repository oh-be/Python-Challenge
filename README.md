# Analyzing Financial and Election Datasets with Python

## Financial Dataset

* The first dataset I chose to inspect with Python was the financial records file. This dataset [budget_data.csv](PyBank/Resources/budget_data.csv) is composed of two columns: `Date` and `Profit/Losses`.

* My script calculates each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The changes in "Profit/Losses" over the entire period, then the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* Here's the output of the final analysis report:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
- - -
## Election Dataset

* The second dataset consists of poll data [election_data.csv](PyPoll/Resources/election_data.csv). This dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.*

This dataset analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on the popular vote.

* Here is the final analysis report (output):

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
- - -
Both files were scripted with data pipelining in mind. I wanted the results to print in a terminal friendly format, hence the simplicity of the outputs!
