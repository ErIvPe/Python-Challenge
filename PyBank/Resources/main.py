#Importing dependencies
import os
import csv

#add variables
totalmonths = 0
profitlosstotal = 0
value = 0
change = 0
dates = []
profits = []

#read CSV file
csvpath = os.path.join("budget_data.csv")

#Opening and reading the CSV file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    
    csv_header = next(csvreader)

    
    firstrow = next(csvreader)
    totalmonths += 1
    profitlosstotal += int(firstrow[1])
    value = int(firstrow[1])
    
    #Go through every row
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months will print
    
        totalmonths += 1

        #Total net amount of "Profit/Losses over entire period"
        profitlosstotal = profitlosstotal + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)

#Test Print

print(f"Financial Analysis")
print(f"---------------------")
print(f"Total Months:", totalmonths)
print(f"Total: " , profitlosstotal)
print(f"Average Change:" , avg_change)
print(f"Greatest Increase in Profits: ",greatest_date , greatest_increase)
print(f"Greatest Decrease in Profits:", worst_date, greatest_decrease)

#text file
fh = open("PyBankTxt.txt",'w')
l1= "Financial Analysis"
l2= "---------------------"
l3= "Total Months:", totalmonths
l4= "Total: " , profitlosstotal
l5= "Average Change:" , avg_change
l6= "Greatest Increase in Profits: ",greatest_date , greatest_increase
l7= "Greatest Decrease in Profits:", worst_date, greatest_decrease

fh.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7))