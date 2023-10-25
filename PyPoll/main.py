import csv

my_report = open('./analysis/Poll_Report.txt','w')
data = csv.reader(open('./Resources/election_data.csv'))

header = next(data)
votes = 0
list_of_candidates = {}
winner = ['',0]

for row in data:
    votes += 1

    candidate = row[2]

    if candidate not in list_of_candidates.keys():
        list_of_candidates[candidate] = 0
    
    list_of_candidates[candidate] += 1
        
output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

for candidate in list_of_candidates.keys():
    candidate_votes = list_of_candidates[candidate]

    output += f'{candidate}: {candidate_votes/votes*100:.3f}% ({candidate_votes})\n'

    if candidate_votes > winner[1]:
      winner[0] = candidate
      winner[1] = candidate_votes

output += f'''
-------------------------
Winner: {winner[0]}
-------------------------
'''
print(output)
my_report.write(output)
    



