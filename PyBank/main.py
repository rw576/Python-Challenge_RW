#import data file
import os
import csv

#connect directory
csvpath = PyBank/Resources/budget_data.csv
with open(csvpath, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
    print(reader)

#set variables
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    print(f"Header: {csv_header}")

#Print Months      
    for row in reader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

 #Print Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

#Average change in "Profit/Losses"
i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
        Total = sum(revenue_change)

    #print(revenue_change)

    monthly_change = Total / len(revenue_change)
    print(monthly_change)

#Greatest increase in profits
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]

#Greates decrease in losses
     profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]

#Print to get final analysis
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total number of months: " + str(len(month)))
print("Total Revenue in period: $ " + str(total_revenue))
print("Average monthly change in Revenue : $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

