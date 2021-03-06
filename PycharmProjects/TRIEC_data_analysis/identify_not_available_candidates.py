# coding=utf-8
"""
Author: Paola Santiago

This program follows through exploring the cause of no response for mentors/mentees – look at the 16% no response for mentees and mentors
(no response and not available)

"""
import csv
import datetime
# mentee_occupation = {}
# mentee_industry = {}
# mentor_occupation = {}
# mentor_industry = {}
#
# with open("pastRMs.csv", "r") as input_file:
#     match_readers = csv.reader(input_file)
#     next(input_file, None)
#     start_date = datetime.date(2012, 04, 1)
#     end_date = datetime.date(2016, 03, 31)
#     for rows in match_readers:
#         date = datetime.datetime.strptime(rows[15], '%d/%m/%Y').date()
#         if rows[18] == "Mentee not available" and start_date <= date <= end_date:
#         # if rows[18] == "Incompatibility of occupation" and start_date <= date <= end_date:
#             mentee_occupation.setdefault(rows[9], 0)
#             mentee_occupation[rows[9]] += 1
#             mentee_industry.setdefault(rows[11], 0)
#             mentee_industry[rows[11]] += 1
#         if rows[18] == "Mentor not available":
#         # if rows[18] == "Incompatibility of occupation" and start_date <= date <= end_date:
#             mentor_occupation.setdefault(rows[3], 0)
#             mentor_occupation[rows[3]] += 1
#             mentor_industry.setdefault(rows[5], 0)
#             mentor_industry[rows[5]] += 1
#
# mentee = {}
# mentee['mentee_occupation'] = mentee_occupation
# mentee['mentee_industry'] = mentee_industry
# print mentee

#
# w = csv.writer(open("rejection_characters.csv", "w"))
# for key, val in mentor_industry.items():
#     w.writerow([key, val])

first_sample = [] #Recommended Matches
input_file= open("pastRMs.csv", "r")
match_readers = csv.reader(input_file)
next(input_file, None)
start_date = datetime.date(2012, 04, 1)
end_date = datetime.date(2016, 03, 31)
for rows in match_readers:
    date = datetime.datetime.strptime(rows[15], '%d/%m/%Y').date()
    if rows[16] == "Accepted" and start_date <= date <= end_date:
    # if rows[18] == "MENTOR \x89\xdb\xd2 No response" and start_date <= date <= end_date:
        past_example = rows[15], rows[0].title(), rows[3] #RM Date, Names, Mentee NOC
        first_sample.append(past_example)
# print first_sample

second_sample = [] #Mentor Attributes
new_input_file = open("new_mentor_attributes.csv", "r")
mentees_readers = csv.reader(new_input_file)
next(new_input_file, None)
start_date = datetime.date(2012, 04, 1)
end_date = datetime.date(2016, 03, 31)
for rows in mentees_readers:
    date = datetime.datetime.strptime(rows[3], '%Y-%m-%d %H:%M:%S').date()
    if start_date <= date <= end_date:
        f = '%Y-%m-%d %H:%M:%S'
        new_date = datetime.datetime.strptime(rows[3], f).date()
        new_date = new_date.strftime('%d/%m/%Y')
        new_example = rows[0].title(), new_date, rows[7] #name, registration date, occupation
        second_sample.append(new_example)
# print second_sample
DAYS = []
for rms in first_sample:
    rms = list(rms)
    for mentees in second_sample:
        mentees = list(mentees)
        if rms[1] == mentees[0] and rms[2] == mentees[2]:
            recommended_match = datetime.datetime.strptime(rms[0], '%d/%m/%Y').date()
            registration_date = datetime.datetime.strptime(mentees[1], '%d/%m/%Y').date()
            print recommended_match, registration_date
            delta = recommended_match - registration_date
            number_of_days_rm_registration = delta.days
            numbers = str(number_of_days_rm_registration)
            DAYS.append(numbers)
# print DAYS

days_summary = {}
for rows in DAYS:
    days_summary.setdefault(rows, 0)
    days_summary[rows] += 1
print days_summary


writer = csv.writer(open("RM_Registration_Rejected_Mentor.csv", "wb"))
for key, value in days_summary.items():
    writer.writerow([key, value])


# same_occupation_counts = {}
# different_occupation_counts = {}
# same_industry_counts = {}
# different_industry_counts = {}
#
# input_file= open("pastRMs.csv", "r")
# match_readers = csv.reader(input_file)
# next(input_file, None)
# start_date = datetime.date(2012, 04, 1)
# end_date = datetime.date(2016, 03, 31)
# for rows in match_readers:
#     date = datetime.datetime.strptime(rows[15], '%d/%m/%Y').date()
#     # if rows[16] == "Accepted" and start_date <= date <= end_date:
#     if rows[18] == "Incompatibility of industry" and start_date <= date <= end_date:
#         if rows[5] == rows[11]:
#             # same_occupation = rows[3], rows[9] #MENTOR NOC, MENTEE NOC
#             # same_occupation_counts.setdefault(same_occupation, 0)
#             # same_occupation_counts[same_occupation] += 1
#             same_industry = rows[5], rows[11] #MENTOR NAIC, MENTEE NAIC
#             same_industry_counts.setdefault(same_industry,0)
#             same_industry_counts[same_industry] += 1
#         if rows[5] != rows[11]:
#             # different_occupation = rows[3], rows[9]
#             # different_occupation_counts.setdefault(different_occupation, 0)
#             # different_occupation_counts[different_occupation] += 1
#             different_industry = rows[5], rows[11] #MENTOR NAIC, MENTEE NAIC
#             different_industry_counts.setdefault(different_industry,0)
#             different_industry_counts[different_industry] += 1
#
# w = csv.writer(open("rejection_characters.csv", "w"))
# for key, val in different_industry_counts.items():
#     w.writerow([key, val])