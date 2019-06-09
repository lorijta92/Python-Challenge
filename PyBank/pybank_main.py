# The average of the changes in "Profit/Losses"
# Greatest increase in profits (date and amount) (sort)
# Greatest decrease in losses (date and amount) (sort)
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

    for row in csvreader:
        month_count = month_count + 1 # Count months
        net_total = net_total + int(row[1]) # Net total

#sort, index 0 and -1, dictionary
    
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(net_total/month_count, 2)}") # Average
print(f"Greatest Increase in Proftis: ")
print(f"Greatest Decrease in Proftis: ")