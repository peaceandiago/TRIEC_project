"""
This program aims follows up on the outcome report
"""
import csv
from _collections import defaultdict

# general_outcome = {}
# with open("outcomereport2.csv", "r") as data1:
#     outcome_reader = csv.reader(data1)
#     for rows in outcome_reader:
#         general_outcome.setdefault(rows[2],0)
#         general_outcome[rows[2]] += 1
# print general_outcome

job_list =[]
with open("outcomereport4.csv", "r") as data1:
    outcome_reader = csv.reader(data1)
    for rows in outcome_reader:
        needed_data = rows[0], rows[2]
        needed_data_list = list(needed_data)
        job_list.append(needed_data_list)


# print job_list

fulltime = {}
parttime = {}
education = {}
lostContact = {}
unemployed = {}
leftCanada = {}
for rows in job_list:
    if rows[1] == "Employed Full-Time":
        fulltime.setdefault(rows[0], 0)
        fulltime[rows[0]] += 1
    elif rows[1] == "Education or training program":
        education.setdefault(rows[0], 0)
        education[rows[0]] += 1
    elif rows[1] == "Employed Part-Time":
        parttime.setdefault(rows[0], 0)
        parttime[rows[0]] += 1
    elif rows[1] == "Lost Contact with Mentee":
        lostContact.setdefault(rows[0], 0)
        lostContact[rows[0]] += 1
    elif rows[1] == "Unemployed":
        unemployed.setdefault(rows[0], 0)
        unemployed[rows[0]] += 1
    elif rows[1] == "Left Canada":
        leftCanada.setdefault(rows[0], 0)
        leftCanada[rows[0]] += 1

full_part = []
for fkey, fvalue in fulltime.iteritems():
    for pkey, pvalue in parttime.iteritems():
        if fkey == pkey:
            data = fkey, fvalue, pvalue
            data_list = list(data)
            full_part.append(data_list)

type_list = []
with open("outcomereport4.csv", "r") as data1:
    outcome_reader = csv.reader(data1)
    for rows in outcome_reader:
        needed_data = rows[0], rows[2], rows[3]
        needed_data_list = list(needed_data)
        type_list.append(needed_data_list)

not_related_field_full = {}
appropriate_level_in_field = {}
entry_or_other_level_in_field = {}
appropriate_level_in_related_field = {}
entry_or_other_level_in_related_field ={}
for rows in type_list:
    if rows[1] =="Employed Full-Time" and rows[2] == "Employed - not in related field":
        not_related_field_full.setdefault(rows[0], 0)
        not_related_field_full[rows[0]] += 1
    if rows[1] == "Employed Full-Time" and rows[2] == "Employed in field - at appropriate professional level":
        appropriate_level_in_field.setdefault(rows[0], 0)
        appropriate_level_in_field[rows[0]] += 1
    if rows[1] == "Employed Full-Time" and rows[2] == "Employed in field - entry or other level":
        entry_or_other_level_in_field.setdefault(rows[0], 0)
        entry_or_other_level_in_field[rows[0]] += 1
    if rows[1] == "Employed Full-Time" and rows[2] == "Employed in related field - at appropriate professional level":
        appropriate_level_in_related_field.setdefault(rows[0], 0)
        appropriate_level_in_related_field[rows[0]] += 1
    if rows[1] == "Employed Full-Time" and rows[2] == "Employed in related field - at entry or other level":
        entry_or_other_level_in_related_field.setdefault(rows[0], 0)
        entry_or_other_level_in_related_field[rows[0]] += 1

appropriate_level = []
for inkey, invalue in appropriate_level_in_field.iteritems():
    for rltdkey, rltdvalue in appropriate_level_in_related_field.iteritems():
        if inkey == rltdkey:
            data = inkey, invalue, rltdvalue
            data_list = list(data)
            appropriate_level.append(data_list)
print appropriate_level

resultFile = open("example.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(appropriate_level)


#
#
# writer = csv.writer(open("not_related_field_full.csv", "wb"))
# for key, value in not_related_field_full.items():
#     writer.writerow([key, value])
# writer = csv.writer(open("appropriate_level_in_field.csv", "wb"))
# for key, value in appropriate_level_in_field.items():
#     writer.writerow([key, value])
# writer = csv.writer(open("entry_or_other_level_in_field.csv", "wb"))
# for key, value in entry_or_other_level_in_field.items():
#     writer.writerow([key, value])
# writer = csv.writer(open("appropriate_level_in_related_field.csv", "wb"))
# for key, value in appropriate_level_in_related_field.items():
#     writer.writerow([key, value])
# writer = csv.writer(open("entry_or_other_level_in_related_field.csv", "wb"))
# for key, value in entry_or_other_level_in_related_field.items():
#     writer.writerow([key, value])


