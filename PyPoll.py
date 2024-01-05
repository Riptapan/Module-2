import csv
import os
total_votes=0                   #The total number of votes cast
candidate_all =[]               #List for candidate column in .csv file
candidates=set()                #For unique candidate names in candidate column
candidate_list=[]               #Unique list of candidates
sum_each=[]                     #The total number of votes each candidate won
each_perc=[]                    #The percentage of votes each candidate won
result=[]                       #Final Result  of Elections
winner=0
i=0
print(os.getcwd())
with open('election_data.csv',newline='')as election_data:
    next(election_data)
    for x in csv.reader(election_data):
        total_votes=total_votes+1  #The total number of votes cast
        candidate_name=x[2]         
        candidates.add(candidate_name)#Set containing unique candidates name
        candidate_list=list(candidates)#List of Unique candidates name
        no_of_candidates=len(candidate_list)
        candidate_all.append(candidate_name) #List for candidate column in .csv file
    for i in range(no_of_candidates):
        sum_each.append(candidate_all.count(candidate_list[i]))
        #Count of number of voteseach candidate won
        each_perc.append(f'{round((sum_each[i]/total_votes*100), 4)}%')
        #Percentage votes each candidate won
    max=sum_each[0]   #Maximum number of votes 
    for j in range(1,no_of_candidates):
        if(sum_each[j]>max):
            max=sum_each[j]
            winner=candidate_list[j]
for k in range(no_of_candidates):
    result.append(f'{candidate_list[k]}: {each_perc[k]} ({sum_each[k]})')
final_result='\n'.join(result)

print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
print(f"{final_result}")
print("-" * 30)
print(f"Winner:{winner}")
print("-" * 30)

with open("Result_poll.txt","w") as file1:
    file1.write("Election Results\n")
    file1.write("-" *50)
    file1.write(f"\n Total Votes: {total_votes}\n")
    file1.write("-" *50)
    file1.write(f"\n{final_result}\n")
    file1.write("-" * 50)
    file1.write(f"\n Winner:{winner}\n")
    file1.write("-" * 50)
