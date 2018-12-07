import os
import csv

#create a path to a file 
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#open the file 
with open(csvpath) as csvfile:

    #read the file 
    csvreader = csv.reader(csvfile,delimiter=(","))

    #skip the header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidate_dict = {}
    votes_cast = 0 
    won_votes = 0
    for row in csvreader:
        votes_cast = votes_cast + 1
    
        candidate = row[2]
        if candidate not in candidate_dict:
            # this has Khan 1 
            candidate_dict[candidate] = 1 
        else: 
            candidate_dict[candidate] = candidate_dict[candidate] + 1
    print(candidate_dict)


        #The percentage of votes each candidate won

            # once it reaches the end, print candidate name + won_votes/votes_cast + won_votes
            #how to I get the 3 zeros after the decimal place 
            #print(f"{candidate} won {won_votes/votes_cast*100} % of votes ({won_votes}")

        # The winner of the election based on popular vote.

    
print(votes_cast)
print('the end')

        


    