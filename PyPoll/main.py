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
    #print(f"CSV Header: {csv_header}")

    print("-------------------------")
    print("Election Results")
    print("-------------------------")

    candidate_dict = {}
    votes_cast = 0 
    for row in csvreader:
        votes_cast = votes_cast + 1
    
        candidate = row[2]
        if candidate not in candidate_dict:
            # this sets the value of the candidate at 1. 
            candidate_dict[candidate] = 1 
            #variable = 1 ("string" , 1)
        else: 
            candidate_dict[candidate] = candidate_dict[candidate] + 1

    print(f"Total Votes: {votes_cast}")
    print("-------------------------")

    #The percentage of votes each candidate won
    for candidate in candidate_dict:
        print(f"{candidate} {candidate_dict[candidate]/votes_cast*100:.3f}% ({candidate_dict[candidate]}) ")
    
    print("-------------------------")

    # The winner of the election based on popular vote.
    winner_value = max(candidate_dict.values())
    for candidate in candidate_dict:
        if winner_value == candidate_dict[candidate]:
            print(f"Winner: {candidate}")
    
    print("-------------------------")

output_path = os.path.join("..", "PyPoll", "PyPoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

  
#     ##text=List of strings to be written to file
    text = ["Election Results",
            "Total Votes: 3521001", 
            "Khan 63.000% (2218231)",
            "Correy 20.000% (704200)", 
            "Li 14.000% (492940)",
            "O'Tooley 3.000% (105630)",
            "Winner: Khan"]

    for line in text:
        csvfile.write(line)
        csvfile.write('\n')


    