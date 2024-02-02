Explanation:
**Importing Libraries and Initializing Variables:**
o	The script starts by importing the csv module which provides functionality for reading and writing CSV files.
o	It then initializes some variables to hold important information:
total_votes     :   The total number of votes cast
candidate_all =[]:   List for candidate column in .csv file
candidates=set() :   For unique candidate names in candidate column
candidate_list=[]:   Unique list of candidates
sum_each=[]:          The total number of votes each candidate won
each_perc=[]:         The percentage of votes each candidate won
result=[]             Final Result  of Elections
**Reading the CSV File:**
o	The script opens and reads the CSV file named election_data.csv.
	with open('election_data.csv',newline='')as election_data
o	It uses a csv.reader to iterate through the rows of the file.
for x in csv.reader(election_data):
**Counting Votes and Populating Candidates ****
o	For each row in the CSV file, the script:
Number of Candidates are first calculated : no_of_candidates
To  Count of number of votes each candidate won sum_each list is created.

sum_each.append(candidate_all.count(candidate_list[i]))
Then Percentage of votes by each candidate is calculated 
each_perc.append(f'{round((sum_each[i]/total_votes*100), 4)}%')
        
	Increments total_votes to keep track of the total number of votes.
	Retrieves the candidate's name from the row (index 2).
	Checks if the candidate is already in the candidates dictionary.
	If the candidate is in the dictionary, it increments their vote count. If not, it adds them to the dictionary with one vote.
**	Finding the Winner:**
o	The script iterrate through the sum_each list to find the candidate with the most votes (winner based on popular vote).
**Printing Results:**
o	The script prints out the election results to the console.
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
print(f"{final_result}")
print("-" * 30)
print(f"Winner:{winner}")
print("-" * 30)
**Writing Results to a Text File:**
o	The script defines the output file path as Result_poll.txt.
with open("Result_poll.txt","w") as file1:
    file1.write("Election Results\n")
    file1.write("-" *50)
    file1.write(f"\n Total Votes: {total_votes}\n")
    file1.write("-" *50)
    file1.write(f"\n{final_result}\n")
    file1.write("-" * 50)
    file1.write(f"\n Winner:{winner}\n")
    file1.write("-" * 50).
