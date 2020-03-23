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

#Creat new empty list for dates
    dates = []
    for row in budgetreader:
#Find total number of months in data    
        row[1] = int(row[1])
        month_count += 1
    
#Find net total amount of profit/losses
        total_p_and_l = total_p_and_l + int(row[1])
#Make new list of dates
        dates.append(row[0])
#Make new list of just P&L values    
        p_and_l_list.append(int(row[1]))


#Create new empty list for change in P&L
    p_and_l_change = [0]
#Make new list for P&L changes    
    for i in range(len(p_and_l_list)-1):
    #p_and_l_change.append([p_and_l_list[i+1] - p_and_l_list[i]])
        p_and_l_change.append(int(p_and_l_list[i+1]) - int(p_and_l_list[i]))

#Zip all columns together to make new list
    new_budget_data = zip(dates, p_and_l_list, p_and_l_change)
    new_budget_list = list(new_budget_data)
    #print(new_budget_list)
#Find max profit and max loss
    max_profit = max(p_and_l_change)
    #print(max_profit)
    max_loss = min(p_and_l_change)
    #print(max_loss)

#Total change (sum of all changes)
    total_change = 0

    for item in p_and_l_change:
        total_change = total_change + int(item)

    #print(total_change)
#Average change/total months-1
    avg_change = total_change / (month_count - 1)
    #print(avg_change)

#print(month_count)
#print(total_p_and_l)
#print(dates)
#print(p_and_l_list)
#print(p_and_l_change)
#print(new_budget_data)



    print("Financial Analysis: ")
    print("---------------------")
    print(f"Total Months: {month_count}")
    print(f"Average Change: {avg_change}")
    #print(f"Greatest Increase in Profits: {max_profit_date}  {max_profit}")
    #print(f"Greatest Decrease in Losses: {max_loss_date}  {max_loss}")