import os
import csv

def poll_analysis(csvpath=''):
    candidate_list = []
    candidate_dict = {}
    vote_count = 0
    max_vote_count = 0
    total_votes = -1
    
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            total_votes += 1
            if row[2] in candidate_list: continue
            else:
                candidate_list.append(row[2])
##        print(candidate_list)
        
    
        for i in range(1, len(candidate_list)):
            with open(csvpath, newline='') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                for row in csvreader:
                    if candidate_list[i] in row:
                        vote_count += 1
                    else:
                        vote_percent = (((vote_count+1)/total_votes)*100)
                        candidate_dict[candidate_list[i]] = [vote_count+1, round(vote_percent,2)]
                        if vote_count >= max_vote_count:
                            max_vote_count = vote_count + 1
                            winner = candidate_list[i]
                vote_count = 0
                
        print("Election Results")
        print("------------------------------")
        print("Total Votes: {}".format(total_votes))
        print("------------------------------")
        for key in candidate_dict.keys():
            print("{}: {}% ({})".format(key, candidate_dict[key][1], candidate_dict[key][0]))
        print("------------------------------")
        print("Winner: {}".format(winner))
        print("---------------END OF REPORT---------------")

    get_report_filepath = input("Please enter the file path for saving Financial Analysis Report: ")
    try:
        report = open(os.path.join(get_report_filepath, "Election_Results_PyPoll.txt"), "w")
        report.write("Election Results\n")
        report.write("---------------------------\n")
        report.write("Total Votes: {}\n".format(total_votes))
        report.write("------------------------------\n")
        for key in candidate_dict.keys():
            report.write("{}: {}% ({})\n".format(key, candidate_dict[key][1], candidate_dict[key][0]))
        report.write("------------------------------\n")
        report.write("Winner: {}\n".format(winner))
        report.write("------------------------------\n")
        print("-------- REPORT SUCCESSFULLY SAVED IN TEXT FILE @ {} ----------".format(os.path.join(get_report_filepath, "Election_Results_PyPoll.txt")))
    except IOError:
        print('An error occured trying to write the file.')
        
def get_results():
    csv_filepath = input("Please enter the file path with Election data to view results: ")
    return poll_analysis(csv_filepath)

get_results()
            
#poll_analysis("/Users/niyatidesai/code/UCBBEL201801DATA5-Class-Repository-DATA/03-Python/Homework/Instructions/PyPoll/raw_data/election_data_1.csv")
