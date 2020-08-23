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

    
