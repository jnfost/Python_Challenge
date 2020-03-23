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
#Create new list of just P&L values
    p_and_l_list = []
    for row in budgetreader:
#Find total number of months in data    
        month_count += 1
    
#Find net total amount of profit/losses
        total_p_and_l = total_p_and_l + int(row[1])
#Make new list of just P&L values    
        p_and_l_list.append(int(row[1]))

#print(month_count)
#print(total_p_and_l)
#print(p_and_l_list)

#Find max P&L
    max_profit = max(p_and_l_list)
    print(max_profit)

#Find min P&L
    max_loss = min(p_and_l_list)
    print(max_loss)   

#Find dates for max profit and loss
    for line in budgetreader:
        if line[1] == max_profit:
            max_profit_date = line[0]
            print(max_profit_date)
        elif line[1] == max_loss:
            max_loss_date = line[0]
            print(max_loss_date)
        else:
            break
            
#Find average of changes over entire period
#Individual change: P&L from i + 1 - P&L from i (don't include last row) - p_and_l_change

    p_and_l_change = []
    for i in range(len(p_and_l_list)-1):
    #p_and_l_change.append([p_and_l_list[i+1] - p_and_l_list[i]])
        p_and_l_change.append([int(p_and_l_list[i+1]) - int(p_and_l_list[i])])
#print(p_and_l_change)

#Total change (sum of all changes)
    #total_change = sum(p_and_l_change)
#Average change/total months-1
    #total_change = 0

    #for item in p_and_l_change:
        #total_change += item
    #print(total_change)
    print("Financial Analysis: ")
    print("---------------------")
    print(f"Total Months: {month_count}")
    print(f"Average Change: ")
    #print(f"Greatest Increase in Profits: {max_profit_date}  {max_profit}")
    #print(f"Greatest Decrease in Losses: {max_loss_date}  {max_loss}")