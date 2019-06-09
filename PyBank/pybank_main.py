# The average of the changes in "Profit/Losses"
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)
# Final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

csvpath = os.path.join("budget_data.csv")
month_count = 0
net_total = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header = next(csvreader)

# Count total months
    for row in csvreader:
        month_count = month_count + 1

# Net total of "Profit/Losses   
        net_total = net_total + int(row[1])
   
    print(month_count)
    print(net_total)