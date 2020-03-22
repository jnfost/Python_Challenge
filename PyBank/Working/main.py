import os
import csv

#Path to collect data from csv file
budgetpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Read in the csv file
with open(budgetpath, 'r') as budgetfile:
#Split data on commas and skip header row
    budgetreader = csv.reader(budgetfile, delimiter= ',')
    budget_header = next(budgetreader)

    #print(budgetreader)
    #for row in budgetreader:
    #    print(row)

#find total number of months in data, set count to 0 and add 1 for each row in the file
    month_count = 0
    total_p_and_l = 0
    for row in budgetreader:
        month_count += 1
    
    #print(month_count)

#Find net total amount of profit/losses
        total_p_and_l = total_p_and_l + int(row[1])

    print(total_p_and_l)

    #while row[1] != 'None'
#Find average of changes over entire period
#Individual change: P&L from r + 1 - P&L from r (don't include last row)
#Total change (sum of all changes)
#Average change/total months-1
        total_change = 0
        p_and_l = row[1]
        for row in budgetreader:
            total_change = total_change + p_and_l

        print(total_change)