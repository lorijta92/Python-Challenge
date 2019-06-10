# Final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

csvpath = os.path.join("budget_data.csv")
months = []
net_total = []

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        months.append(row[0]) # Count months
        net_total.append(int(row[1])) # Net total

max = max(net_total)
max_index = net_total.index(max)

min = min(net_total)
min_index = net_total.index(min)

print(f"Total Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(net_total)/len(months), 2)}")
print(f"Greatest Increase in Profits: {months[max_index]} $({max})")
print(f"Greatest Decrease in Profits: {months[min_index]} $({min})")