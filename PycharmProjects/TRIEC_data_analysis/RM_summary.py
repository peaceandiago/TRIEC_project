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


def rejectionSummary(line_status):
    """Counts the number of occurence for each rejected reason - returns count of rejected reasons"""
    file = open("pastRMs.csv", "r")
    reader = csv.reader(file)
    next(reader,None)
    rej_summary = {}
    for line in reader:
        if line_status == 'Rejected':
            rejection = line[18]
            rej_summary.setdefault(rejection, 0)
            rej_summary[rejection] += 1

    return rej_summary


def dateRanges(YYYY, MM, D):
    """compares the date ranges that are inputted with the date in the csv file - returns status"""
    start_date = datetime.date(YYYY, MM, D)
    end_date = datetime.date(YYYY, MM, D)
    file = open("pastRMs.csv", "r")
    reader = csv.reader(file)
    next(reader, None)
    for line in reader:
        date = datetime.datetime.strptime(line[15], '%d/%m/%Y').date()
        if start_date <= date <= end_date:
            return line[18]



