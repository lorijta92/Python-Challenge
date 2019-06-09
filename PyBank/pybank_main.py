# Final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

csvpath = os.path.join("budget_data.csv")
months = []
net_total = []

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header = next(csvreader)

    for row in csvreader:
        months.append(row[0]) # Count months
        net_total.append(int(row[1])) # Net total

#sort, index 0 and -1, dictionary
#iterate through rows to zip them as a dictionary?
#unzip then sort

print(f"Total Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(net_total)/len(months), 2)}") # Average
#print(f"Greatest Increase in Proftis: Date: Amount")
#print(f"Greatest Decrease in Proftis: Date: Amount")