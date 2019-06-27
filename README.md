# Python-Challenge
### Part 1: PyBank
#### Goal:
Create a Python script that analyzes the financial records of a company by calculating the following:
- The total number of months included in the data set.
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

#### Process:
First, I read in the budget data contained in a separate csv file and created empty lists (`months`, `net_total`, `change`) to store interim data. Then, in a for loop, I appended the `months` list with the values of the first column in the csv file and took the length of that list to get the total number of months included in the data set.

In the same for loop, I calculated the net total amount of "Profit/Losses," by appending the `net_total` list with all the values in the second column of the csv file and then took the sum of that list. 

To calculate the average of the changes in "Profit/Losses" over the entire period, I declared 3 variables (`prev`, `curr`, `val1`) and used the for loop to get the difference between two values, `curr` and `prev` while iterating through each row. I appended the `change` list with those differences (`val1`). I then divided the sum of the `change` list by its length to get the average. 

To obtain the greatest increase and decrease, I used the `max()` and `min()` functions on the `change` list, being sure to skip the first value in the list, which was only a placeholder. I stored the respective values into the aptly named variables, `max` and `min`, and took the index of those values to find the corresponding months.

I then printed my findings in Terminal as well as exported those findings to a separate text file. 

### Part 2: PyPoll
#### Goal:
Create a Python script that analyzes votes casted in a local election by calculating the following:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

#### Process:
