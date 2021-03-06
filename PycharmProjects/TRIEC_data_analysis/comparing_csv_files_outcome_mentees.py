"""
This program aims to answer the question "Compare mentee occupation to employee outcome - do some occupations have better outcomes?"
-this needs to compare two rows from each csv to make sure it is the same row - then take the necessary rows for data analysis
"""
import csv
import datetime

def MenteeInformation():
    """
    This function takes the necessary information from the mentees_all_attribute.csv and make the primary IDs consistent and taking the occupation
    roles
    :return: list of mentees data
    """
    with open("mentees_all_attributes.csv", "r") as mentees_file:
        mentees_reader = csv.reader(mentees_file)
        next(mentees_file, None)
        mentees_data = []
        for rows in mentees_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[2].lower()
            mentees_occupation = rows[7]
            needed_data = mentees_name, mentees_email, mentees_occupation
            mentees_list = list(needed_data)
            mentees_data.append(mentees_list)

        return mentees_data

mentees_data = MenteeInformation()
# print mentees_data

def OutcomeInformation1():
    """
    This function finds and modifies the necessary information from the outcome dataset for report 1
    :return:
    """
    with open("MenteeOutcomeReport.csv", "r") as outcome_file:
        outcome_reader = csv.reader(outcome_file)
        next(outcome_file, None)
        outcome1_data = []
        for rows in outcome_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[1].lower()
            improved_mentees_email = mentees_email.replace(' ','') #remove unwanted spaces in string present in the dataset
            completion_date = rows[3]
            mentee_outcome_1 = rows[9]
            mentee_employment_1 = rows[12]
            outcome1 = mentees_name, improved_mentees_email, completion_date, mentee_outcome_1, mentee_employment_1
            outcome1_list = list(outcome1)
            outcome1_data.append(outcome1_list)
        return outcome1_data

def OutcomeInformation2():
    """
    This function finds and modifies the necessary information from the outcome dataset for report 2
    :return:
    """
    with open("MenteeOutcomeReport.csv", "r") as outcome_file:
        outcome_reader = csv.reader(outcome_file)
        next(outcome_file, None)
        outcome2_data = []
        for rows in outcome_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[1].lower()
            improved_mentees_email = mentees_email.replace(' ','') #remove unwanted spaces in string present in the dataset
            completion_date = rows[3]
            mentee_outcome_2 = rows[23]
            mentee_employment_2 = rows[26]
            outcome2 = mentees_name, improved_mentees_email, completion_date, mentee_outcome_2, mentee_employment_2
            outcome2_list = list(outcome2)
            outcome2_data.append(outcome2_list)
        return outcome2_data

def OutcomeInformation3():
    """
    This function finds and modifies the necessary information from the outcome dataset for report 3
    :return:
    """
    with open("MenteeOutcomeReport.csv", "r") as outcome_file:
        outcome_reader = csv.reader(outcome_file)
        next(outcome_file, None)
        outcome3_data = []
        for rows in outcome_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[1].lower()
            improved_mentees_email = mentees_email.replace(' ','') #remove unwanted spaces in string present in the dataset
            completion_date = rows[3]
            mentee_outcome_3 = rows[37]
            mentee_employment_3 = rows[40]
            outcome3 = mentees_name, improved_mentees_email, completion_date, mentee_outcome_3, mentee_employment_3
            outcome3_list = list(outcome3)
            outcome3_data.append(outcome3_list)
        return outcome3_data

def OutcomeInformation4():
    """
    This function finds and modifies the necessary information from the outcome dataset for report 4
    :return:
    """
    with open("MenteeOutcomeReport.csv", "r") as outcome_file:
        outcome_reader = csv.reader(outcome_file)
        next(outcome_file, None)
        outcome4_data = []
        for rows in outcome_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[1].lower()
            improved_mentees_email = mentees_email.replace(' ','') #remove unwanted spaces in string present in the dataset
            completion_date = rows[3]
            mentee_outcome_4 = rows[51]
            mentee_employment_4 = rows[54]
            outcome4 = mentees_name, improved_mentees_email, completion_date, mentee_outcome_4, mentee_employment_4
            outcome4_list = list(outcome4)
            outcome4_data.append(outcome4_list)
        return outcome4_data

outcome1_data = OutcomeInformation1()
outcome2_data = OutcomeInformation2()
outcome3_data = OutcomeInformation3()
outcome4_data = OutcomeInformation4()

# print outcome1_data

new_dataset_1 = []
new_dataset_2 = []
new_dataset_3 = []
new_dataset_4 = []

def CombineInformation(iterated_data, empty_list):
    """
    This function combines two separate lists from 2 CSV files to get the necessary data
    :param iterated_data:
    :param empty_list:
    :return: list of necessary data
    """
    for rows in mentees_data:
        for new_rows in iterated_data:
            if new_rows[0] in rows[0] and new_rows[1] in rows[1]:
                occupation = rows[2]
                completion_date = new_rows[2]
                outcome = new_rows[3]
                employment_type = new_rows[4]
                necessary_data = occupation, completion_date, outcome, employment_type
                necessary_data_list = list(necessary_data)
                empty_list.append(necessary_data_list)
    return empty_list

data1 = CombineInformation(outcome1_data, new_dataset_1)
data2 = CombineInformation(outcome2_data, new_dataset_2)
data3 = CombineInformation(outcome3_data, new_dataset_3)
data4 = CombineInformation(outcome4_data, new_dataset_4)

resultFile = open("outcomereport4.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(data4)

"""
This part follows up on the outcome report
"""

# general_outcome = {}
# with open("outcomereport1.csv", "r") as data1:
#     outcome_reader = csv.reader(data1)
#     for rows in outcome_reader:
#         general_outcome.setdefault(rows[2],0)
#         general_outcome[rows[2]] += 1
# print general_outcome

# d = {'job': {'general_types': None}}
# d['job'] ={}
# d['general_types'] ={}
# with open("outcomereport1.csv", "r") as data1:
#     outcome_reader = csv.reader(data1)
#     for rows in outcome_reader:
#         needed_data = rows[0], rows[3]
#         needed_data_list = list(needed_data)
#         for new_rows in needed_data_list:
#             print new_rows

        # d['job'] = rows[0]
        # d['general_types'].setdefault(rows[3],0)
        # d['general_types'][rows[3]] += 1
        # print d
# with open("outcomereport1.csv", "r") as data1:
#     outcome_reader = csv.reader(data1)
#     d = {}
#     d['job']['type'] = 1
#     for rows in outcome_reader:
#         d['job'] = rows[0]
#         print d
        # for new_rows in needed_data_list:
        #     # print new_rows