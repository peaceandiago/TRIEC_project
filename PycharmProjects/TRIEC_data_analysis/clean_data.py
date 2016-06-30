"""
This program is to clean the data for dataset - mentees
"""
import csv


""" These three functions help solve: Who gets matched and who doesn't"""

data_out = open("mentees_all_attributes.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)

def participated(): #Participated in Mentorship
    part_counters = {}
    for line in reader:
        if int(line[6]) > 0:
            primary = line[7].strip()
            part_counters.setdefault(primary, 0)
            part_counters[primary] += 1
    return part_counters


def notParticipated():
    with open("mentees_all_attributes.csv", "rU") as data_out:
        reader = csv.reader(data_out)
        next(reader,None)
        notpart_counters = {}
        for line in reader:
            if int(line[6]) == 0:
                primary = line[7].strip()
                notpart_counters.setdefault(primary, 0)
                notpart_counters[primary] += 1
    return notpart_counters

def generalNumber(): #General number of mentees with their primary occupation
    with open("mentees_all_attributes.csv", "rU") as data_out:
        reader = csv.reader(data_out)
        next(reader,None)
        gen_counters = {}
        for line in reader:
            if int(line[6]) >= 0:
                primary = line[7].strip()
                gen_counters.setdefault(primary, 0)
                gen_counters[primary] += 1
    return gen_counters

counter_p = participated() #creates a mentee who participated/primary occupation dictionary
counter_np = notParticipated() #creates mentee who did not participate/primary occupation dictionary
counter_g = generalNumber() #creates general number of mentees/primary occupation dictionary
success_percentage = dict((k, counter_p[k] / float(counter_g[k])) for k in counter_p if k in counter_g) #calculates participants/general, returns dict
no_success_percentage = dict((k, counter_np[k] / float(counter_g[k])) for k in counter_np if k in counter_g) #calculates nonparticipants/general, returns dict

def convertPercentage(dictionary):          #converts into percentage
    for key, value in dictionary.items():
        dictionary[key] = value * 100

    return dictionary

# print convertPercentage(success_percentage)
# print convertPercentage(no_success_percentage)


data_out.close()
