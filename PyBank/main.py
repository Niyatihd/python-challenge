#Create a function to loop through all the rows 
import os
import csv
import re

def financial_records_analysis(csvpath=''):
    total_months, total_revenue = 0, 0
    revenue_permonth = {}
    revenue_change_monthly = [0]
    revenue_change = 0
    i = 0
    value_change = []
    string_pat = re.compile(r'\w\w\w-\d\d')
    with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

    #  Each row is read as a row
        for row in csvreader:
            #print(row)
            if string_pat.search(row[0]):
                #print(string_pat.search(row[0]))
                total_months += 1
                total_revenue += int(row[1])
                revenue_permonth[row[0]] = int(row[1])
        #print(revenue_permonth)
        value_change.extend(revenue_permonth.values())
        #print(value_change)
        while i != (len(value_change)-1):
            revenue_change = value_change[i+1] - value_change[i]
            #print(revenue_change)
            i += 1
            revenue_change_monthly.append(revenue_change)
        #print(revenue_change_monthly)
        j = 0
        for key , value in revenue_permonth.items():
            revenue_permonth[key] = [value_change[j], revenue_change_monthly[j]] 
            j += 1
        #print(revenue_permonth)
                       
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: %d" % total_months)
    print("Total Revenue: $%d" % total_revenue)

    average_revenue_change = sum(revenue_change_monthly)/(len(revenue_change_monthly)-1)
    print("Average Revenue Change: $%d" % average_revenue_change)
    
    greatest_revenue_inc = 0
    greatest_revenue_dec = 0
    for key in revenue_permonth.keys():
        #print(revenue_permonth[key][1])
        if revenue_permonth[key][1] >= greatest_revenue_inc:
            greatest_revenue_inc = revenue_permonth[key][1]
            greatest_revenue_inc_month = key
        elif revenue_permonth[key][1] <= greatest_revenue_dec:
            greatest_revenue_dec = revenue_permonth[key][1]
            greatest_revenue_dec_month = key
    #print(greatest_revenue_inc)

    print("Greatest Revenue Increase: %s ($%d)" % (greatest_revenue_inc_month, greatest_revenue_inc))
    print("Greatest Revenue Decrease: %s ($%d)" % (greatest_revenue_dec_month, greatest_revenue_dec))
    print("---------------END OF REPORT---------------")
    get_report_filepath = input("Please enter the file path for saving Financial Analysis Report: ")
    try:
        report = open(os.path.join(get_report_filepath, "Financial_Analysis_Report_PyBank.txt"), "w")
        report.write("Financial Analysis\n")
        report.write("---------------------------\n")
        report.write("Total Months: %d\n" % total_months)
        report.write("Total Revenue: $%d\n" % total_revenue)
        report.write("Average Revenue Change: $%d\n" % average_revenue_change)
        report.write("Greatest Revenue Increase: %s ($%d)\n" % (greatest_revenue_inc_month, greatest_revenue_inc))
        report.write("Greatest Revenue Decrease: %s ($%d)\n" % (greatest_revenue_dec_month, greatest_revenue_dec))
        print("-------- REPORT SUCCESSFULLY SAVED IN TEXT FILE @ {} ----------".format(os.path.join(get_report_filepath, "Financial_Analysis_Report_PyBank.txt")))
    except IOError:
        print('An error occured trying to write the file.') 
        
    
def get_filepath_and_run_analysis():
    filepath = input("Please enter the file path with Data for Financial Analysis: ")
    return financial_records_analysis(filepath)
    

get_filepath_and_run_analysis()

