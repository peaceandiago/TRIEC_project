"""
This program aims to summarize the RM dataset to gather insights:
summary of the reject reasons for the last 3 years
# of days between RM date and the date when RM accept/reject *
% of expired RMs compare to the total number of RM generated
Average length of time for matches in NOCS that TMP matches *
The # of days between RM accept and partnership start date *
"""

import csv
import datetime
from datetime import timedelta, date


def rejectionSummary(start_year, start_month, start_dates, end_year, end_month, end_dates):
    """Counts the number of occurence for each rejected reason - returns count of rejected reasons
    compares the date ranges that are inputted with the date in the csv file - returns status
    Function to answer the 'summary of the reject reasons for the last 3 years' """
    rej_summary = {}
    start_date = datetime.date(start_year, start_month, start_dates)
    end_date = datetime.date(end_year, end_month, end_dates)
    file = open("pastRMs.csv", "r")
    reader = csv.reader(file)
    next(reader, None)
    for line in reader:
        date = datetime.datetime.strptime(line[15], '%d/%m/%Y').date()
        if start_date <= date <= end_date:
            if line[16] == 'Rejected':
                rejection = line[18]
                rej_summary.setdefault(rejection, 0)
                rej_summary[rejection] += 1
    return rej_summary

def overallSummary():
    overall_summary = {}
    start_date = datetime.date(2011, 04, 1)
    end_date = datetime.date(2016, 03, 31)
    file = open("pastRMs.csv", "r")
    reader = csv.reader(file)
    next(reader, None)
    for line in reader:
        date = datetime.datetime.strptime(line[15], '%d/%m/%Y').date()
        if start_date <= date <= end_date:
            if line[16] == 'Expired' or 'Rejected' or 'Accepted' or 'Cancelled':
                overall_summary.setdefault(line[16],0)
                overall_summary[line[16]] += 1

    return overall_summary


reject_summary = rejectionSummary(2014, 04, 1, 2015, 03, 31)
overall = sum(reject_summary.values())







def summaryPercentage(dict):
    """Converts values from each dictionary into percentages"""
    for key, value in dict.items():
        dict[key] = (value/float(overall)) * 100
    return dict

rejection_summary = summaryPercentage(reject_summary)
print rejection_summary


