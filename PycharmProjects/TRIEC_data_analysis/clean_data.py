"""
This program is to clean the data for dataset
"""
import csv


data_out = open("mentees_all_attributes.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)

counters = {}

""" These three functions help solve: Occupation of mentees/mentors registered per fiscal year"""
def participated():
    for line in reader: 
        if int(line[6]) > 0:
            primary = line[7].strip('[]')
            counters.setdefault(primary, 0)
            counters[primary] += 1

    for k, v in counters.items():
        print(k, v)

participated()

data_out.seek(0)
reader = csv.reader(data_out)
next(reader,None)

def notParticipated():
    for line in reader:
        if int(line[6]) == 0:
            primary = line[7].strip('[]')
            counters.setdefault(primary, 0)
            counters[primary] += 1

    for k, v in counters.items():
        print(k, v)
notParticipated()

data_out.seek(0)
reader = csv.reader(data_out)
next(reader,None)


def generalNumber():
    for line in reader:
        primary = line[7].strip('[]')
        counters.setdefault(primary, 0)
        counters[primary] += 1

    for k, v in counters.items():
        print(k, v)

notParticipated()


data_out.close()
