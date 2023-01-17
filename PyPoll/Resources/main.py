import os
import csv

csvpath = os.path.join("election_data.csv")

#candidates
candidates=[]
#candidate votes
vote_per= []
# vote percentage
percent_vote=[]
#Total vote
totalvotes= 0
with open (csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Total Vote gather
        totalvotes +=1

        #list of candidates with vote counter
        if row[2] not in candidates:
            candidates.append(row[2])
            index= candidates.index(row[2])
            vote_per.append(1)
        else:
            index = candidates.index(row[2])
            vote_per[index] +=1
    #percentage of total votes for each candidate
    for votes in vote_per:
        percent= (votes/totalvotes)*100
        percent_vote.append(percent)
    #Find the winner
    winner= max(vote_per)
    index= vote_per.index (winner)
    nameofwin= candidates[index]








#Print Test
print(f'Election Results')
print(f'-------------------------')
print(f' Total Votes: ', totalvotes)
print(f'--------------------------')
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_vote[i])} ({str(vote_per[i])})")
print("--------------------------")
print('Winner: ',nameofwin)

#text file write
fh= open('PyPoll.txt','w')
l1= 'Election Results'
l2= '-------------------------'
l3=  'Total Votes: ', totalvotes
l4= '--------------------------'
fh.write('{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_vote[i])} ({str(vote_per[i])})")
    fh.write('{}\n'.format(line))
l5= "--------------------------"
l6= 'Winner: ',nameofwin
fh.write('{}\n{}\n'.format(l5, l6,))




