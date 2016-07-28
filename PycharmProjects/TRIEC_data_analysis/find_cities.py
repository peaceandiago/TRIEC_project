# coding=utf-8
"""
Author: Paola Santiago

This program follows through exploring the cause of no response for mentors/mentees – look at the cities for different mentors and mentees from 3 different datasets


"""
import csv
import datetime

mentees_mentors_data = []

input_file= open("pastRMs.csv", "r")
match_readers = csv.reader(input_file)
next(input_file, None)
start_date = datetime.date(2012, 04, 1)
end_date = datetime.date(2016, 03, 31)
for rows in match_readers:
    date = datetime.datetime.strptime(rows[15], '%d/%m/%Y').date()
    if rows[18] == "Location" and start_date <= date <= end_date:
        mentors_name = rows[0].title()
        mentors_occupation = rows[3]
        mentees_name = rows[7].title()
        mentees_occupation = rows[10]
        all_data = mentors_name, mentors_occupation, mentees_name, mentees_occupation
        all_data = list(all_data)
        mentees_mentors_data.append(all_data)

menteedata = []
with open("mentees_all_attributes.csv", "r") as PR_file:
    PR_reader = csv.reader(PR_file)
    next(PR_file, None)
    for rows in PR_reader:
        mentee_names = rows[0].title()
        primary_occupation = rows[7]
        for rmrows in mentees_mentors_data:
            if mentee_names == rmrows[2] and primary_occupation == rmrows[3]:
                mentee_city = rows[27]
                mentee_names = rmrows[2]
                mentor_names = rmrows[0]
                mentors_occupation =rmrows[1]
                mentee_data = mentee_names, mentee_city, mentor_names, mentors_occupation
                mentee_data = list(mentee_data)
                menteedata.append(mentee_data)

all_cities = []
with open("new_mentor_attributes.csv", "r") as RR_file:
    RR_reader = csv.reader(RR_file)
    next(RR_file, None)
    for rows in RR_reader:
        mentor_name = rows[0].title()
        primary_occupation = rows[7]
        for rmrows in menteedata:
            if mentor_name == rmrows[2] and primary_occupation == rmrows[3]:
                mentor_city = rows[15]
                mentee_city = rmrows[1]
                city = mentor_city, mentee_city
                city = list(city)
                all_cities.append(city)

print all_cities

resultFile = open("location.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(all_cities)