# Total months
# Net total of "Profit/Losses"
# The average of the changes in "Profit/Losses"
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)
# Final script should both print the analysis to the terminal and export a text file with the results.

# Read in csv, skip header, COUNT TOTAL MONTHS
import os
import csv

csvpath = os.path.join("budget_data.csv")
month_count = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header = next(csvreader)

    for row in csvreader:
        month_count = month_count + 1
    
    print(month_count)