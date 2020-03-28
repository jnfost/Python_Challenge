#Import modules
import os
import csv

#Set path for csv file
electionpath = os.path.join(".", "Resources", "election_data.csv")

#Read in the csv file
with open(electionpath, 'r') as electionfile:
    #Split data with on commas and skip header row
    electionreader = csv.reader(electionfile, delimiter= ',')
    election_header = next(electionreader)

# Set initial value for voter count
    voter_count = 0
# Create empty list to hold names of candidates
    candidates = []
# Set initial value for counts of each candidates vote totals
    cand_0 = 0
    cand_1 = 0
    cand_2 = 0
    cand_3 = 0
#Total Votes cast
    for row in electionreader:
        voter_count += 1

#List of candidates (if candidate name not in list, add to list using append)
        if row[2] not in candidates:
            candidates.append(row[2])
        
# Total number of votes for each candidate  
# Add one for each occurence of the name in the 3rd column of source data  
        if row[2] == candidates[0]:
            cand_0 += 1
        elif row[2] == candidates[1]:
            cand_1 += 1
        elif row[2] == candidates[2]:
            cand_2 += 1
        elif row[2] == candidates[3]:
            cand_3 += 1

# Percentage of votes for each candidate (total for each candidate / total votes)
# Format to percentage using format(  , '.3%') rounding to 3 decimal places
    percent_Khan = format((cand_0 / voter_count), '.3%' )
    percent_Correy = format((cand_1 / voter_count), '.3%')
    percent_Li = format((cand_2 / voter_count), '.3%')
    percent_OTooley = format((cand_3 / voter_count), '.3%')



# Winner of election based on popular vote
    # Create list of candidate vote totals
    # Zip together with list of candidate names    

    cand_votes = [cand_0, cand_1, cand_2, cand_3]
    tally_data = zip(candidates, cand_votes)
    tally_list = list(tally_data)
    
#Winner is name associated with greatest total  (max of cand_votes)   
    winner_total = max(cand_votes)
    for item in tally_list:
        if item[1] == winner_total:
            winner = item[0]

  
print("Election Results")
print("------------------------")
print(f"Total Votes:  {voter_count}")
print("------------------------")
print(f"{candidates[0]}: {percent_Khan}  ({cand_0})")
print(f"{candidates[1]}: {percent_Correy}  ({cand_1})")
print(f"{candidates[2]}: {percent_Li}  ({cand_2})")
print(f"{candidates[3]}: {percent_OTooley}  ({cand_3})")
print("------------------------")
print(f"Winner: {winner} ")


output_path = os.path.join('.', 'Resources', 'election_results.txt')

with open(output_path, 'w') as textfile:
    textfile.write("Election Results")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write(f"Total Votes:  {voter_count}")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write(f"{candidates[0]}: {percent_Khan}  ({cand_0})")
    textfile.write("\n")
    textfile.write(f"{candidates[1]}: {percent_Correy}  ({cand_1})")
    textfile.write("\n")
    textfile.write(f"{candidates[2]}: {percent_Li}  ({cand_2})")
    textfile.write("\n")
    textfile.write(f"{candidates[3]}: {percent_OTooley}  ({cand_3})")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write(f"Winner: {winner} ")