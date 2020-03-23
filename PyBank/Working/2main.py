import os
import csv

#Path to collect data from csv file
budgetpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Read in the csv file
with open(budgetpath, 'r') as budgetfile:
#Split data on commas and skip header row
    budgetreader = csv.reader(budgetfile, delimiter= ',')
    budget_header = next(budgetreader)
    
#Find total number of months in data, set count to 0 and add 1 for each row in the file
    month_count = 0
    total_p_and_l = 0
#Create new empty list of just P&L values
    p_and_l_list = []
#Create new empty list for change in P&L
    p_and_l_change = 0
    for row in budgetreader:
#Find total number of months in data    
        row[1] = int(row[1])
        month_count += 1
    
#Find net total amount of profit/losses
        total_p_and_l = total_p_and_l + int(row[1])
#Make new list of just P&L values    
        p_and_l_list.append(int(row[1]))
        #p_and_l_change = int([row+ 1][1]) - int([row[1]])

        max_profit = max(p_and_l_list)
        max_loss = min(p_and_l_list)

        if row[1] == max_profit:
            max_profit_date = row[0]
            print(row[0])
        elif row[1] == max_loss:
            max_loss_date = row[0]
            print(row[0])
        
print(month_count)
print(total_p_and_l)
#print(p_and_l_list)
print(p_and_l_change)
print(max_profit)
print(max_loss)
print(max_profit_date)
print(max_loss_date)
