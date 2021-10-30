# modules
import os
import csv

# file path
input_file = os.path.join('Resources', 'budget_data.csv')

# empty lists
total_months = []
total_profit = []
monthly_profit_change = []

# open csv file in read mode
with open(input_file) as budget:

    # create variable for contents of file
    csvreader = csv.reader(budget,delimiter=",")

    # skip header for iteration
    header = next(csvreader)

    # iterate through rows
    for row in csvreader:

        # add (append) totals to corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # iterate through profits
    for i in range(len(total_profit)-1):

        # append difference of 2 months to monthly profit change list
        monthly_profit_change.append(total_profit[i+1] - total_profit[i])

# max and minimum variables from monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# assign month index for max and min
# added + 1 to reflect the next month because the change would show on the following month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# summary table / print statements
print("Financial Analysis")
print("_____________________________")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files