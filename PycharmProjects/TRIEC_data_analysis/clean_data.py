"""
This program is to clean the data for dataset
"""
import csv


""" These three functions help solve: Occupation of mentees/mentors registered per fiscal year"""

data_out = open("mentees_all_attributes.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)


def participated():
    counters = {}
    for line in reader:
        if int(line[6]) > 0:
            primary = line[7].strip('[]')
            counters.setdefault(primary, 0)
            counters[primary] += 1

    # for k, v in counters.items():
    #     print k,v
    return counters


data_out.seek(0)
reader = csv.reader(data_out)
next(reader,None)

def notParticipated():
    counters = {}
    for line in reader:
        if int(line[6]) == 0:
            primary = line[7].strip('[]')
            counters.setdefault(primary, 0)
            counters[primary] += 1

    # for k, v in counters.items():
    #     print k,v
    return counters

data_out.seek(0)
reader = csv.reader(data_out)
next(reader,None)


def generalNumber():
    counters = {}
    for line in reader:
        if int(line[6]) >= 0:
            primary = line[7].strip('[]')
            counters.setdefault(primary, 0)
            counters[primary] += 1

    # for k, v in counters.items():
    #     print k, v
    return counters

counter_p = participated()
#print counter_p
counter_g = generalNumber()
print counter_g
#success_percentage = [counter_p.get(primary)/counter_g.get(primary, 1) for primary in counter_p]
#print success_percentage


data_out.close()
