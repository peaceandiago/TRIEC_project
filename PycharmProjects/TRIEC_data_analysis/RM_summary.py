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


def rejectionSummary(csv_file):#Counts the number of occurence for each rejected reason
    file = open(csv_file, "r")
    reader = csv.reader(file)
    next(reader,None)
    rej_summary = {}
    for line in reader:
        if line[16] == 'Rejected':
            rejection = line[18]
            rej_summary.setdefault(rejection, 0)
            rej_summary[rejection] += 1

    return rej_summary

print rejectionSummary("pastRMs.csv")


for another_line in reader:
    objectify_date_list = []
    new = another_line[15]
    objectify_date = datetime.datetime.strptime(new, '%d/%m/%Y').date()
    objectify_date_list.append(objectify_date) #convert the string date into object date
    another_line = [another_line[0:15] + objectify_date_list + another_line[16:]] #put it back to the csv file
    for things in another_line:
        print things[15]

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
for result in perdelta(date(2011, 10, 10), date(2011, 12, 12), timedelta(days=1)):
    print type(result)
