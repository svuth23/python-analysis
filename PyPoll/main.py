import os
import csv

csv_path= os.path.join("C:\\Users\\swapn\\OneDrive\\Desktop\\Starter_Code (2)\\Starter_Code\\PyPoll\\Resources\\election_data.csv")
total_votes=0
candidate_votes={}
# Initialize variables to keep track of the total number of votes and the winner
winner = ""
winner_votes = 0
percentage_votes =0

with open(csv_path, 'r') as csv_file:

     csv_reader = csv.reader(csv_file, delimiter=',')

     csv_header=next(csv_reader)

     print(f"CSV Header: {csv_header}")
     # total number of votes cast
     for row in csv_reader:
        total_votes+=1
        candidate_name=row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] +=1
        else:
            candidate_votes[candidate_name]=1

     for candidate,votes in candidate_votes.items():
         percentage_votes =( votes/ total_votes)*100

         if votes > winner_votes:
            winner_votes = votes
            winner = candidate
    




output = f'''
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''

print(output)

    
        #  with open("results.txt", "w") as results_file:
        #   results_file.write("Election Results\n")
        #   results_file.write("-------------------------\n")
        #   results_file.write(f"Total Votes: {total_votes}\n")
        #   results_file.write("-------------------------\n")
        #   results_file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")
    
        #  results_file.write("-------------------------\n")
        #  results_file.write(f"Winner: {winner}\n")
        #  results_file.write("-------------------------\n")

        # # Print a message to indicate that the results have been written to "results.txt"
        #  print("Results have been written to results.txt")

       
    



