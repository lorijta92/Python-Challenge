import csv

csvpath = ("budget_data.csv")
months = []
net_total = []
change = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    prev = 0

    for row in csvreader:
        months.append(row[0]) # Count months
        net_total.append(int(row[1])) # Net total

        # Calculate changes between months and store in list
        curr = int(row[1])
        val1 = curr - prev
        change.append(val1)
        prev = curr

avgchange = sum(change[1:])/len(change[1:]) #Calculate average of monthly changes

# Find the greatest increase and corresponding month
max = max(change[1:])
max_index = change.index(max)

# Find the greatest decrease and corresponding month
min = min(change[1:])
min_index = change.index(min)

# Print to Terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(avgchange, 2)}")
print(f"Greatest Increase in Profits: {months[max_index]} (${max})")
print(f"Greatest Decrease in Profits: {months[min_index]} (${min})")

# Write text file
file = open("Bank_Analysis_Summary.txt", "w" )
file.write("Financial Analysis\n")
file.write("-----------------------------\n")
file.write(f"Total Months: {len(months)}\n")
file.write(f"Total: ${sum(net_total)}\n")
file.write(f"Average Change: ${round(avgchange, 2)}\n")
file.write(f"Greatest Increase in Profits: {months[max_index]} (${max})\n")
file.write(f"Greatest Decrease in Profits: {months[min_index]} (${min})\n")
file.close()