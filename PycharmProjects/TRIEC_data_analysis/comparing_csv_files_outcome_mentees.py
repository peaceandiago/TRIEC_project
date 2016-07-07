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

def OutcomeInformation():
    with open("MenteeOutcomeReport.csv", "r") as outcome_file:
        outcome_reader = csv.reader(outcome_file)
        next(outcome_file, None)
        outcome1_data = []
        for rows in outcome_reader:
            mentees_name = rows[0].title()
            mentees_email = rows[1].lower()
            completion_date = rows[3]
            mentee_outcome_1 = rows[9]
            mentee_employment_1 = rows[12]
            mentee_outcome_2 = rows[23]
            mentee_employment_2 = rows[26]
            mentee_outcome_3 = rows[37]
            mentee_employment_3 = rows[40]
            outcome1 = mentees_name, mentees_email, completion_date, mentee_outcome_1, mentee_employment_1
            outcome1_list = list(outcome1)
            outcome1_data.append(outcome1_list)
        return outcome1_data

outcome1_data = OutcomeInformation()
# print outcome1_data

for rows in mentees_data:
    for new_rows in outcome1_data:
        print new_rows[1]
        # if new_rows[0] in rows[0] and new_rows[1] in rows[1]:
        #     print rows[0]
        # print completion_date, mentee_outcome_1, mentee_employment_1
        # print completion_date, mentee_outcome_2, mentee_employment_2
        # print completion_date, mentee_outcome_3, mentee_employment_3

        # for rmrows in mentees_data:
        #     if mentees_name in rmrows[0] and mentees_email in rmrows[1]:
        #         print mentee_employment_2
                # outcome1 = completion_date, rmrows[7], mentee_outcome_1, mentee_employment_1
                # print outcome1
    #             data_list = list(needed_data)
    #             outcome_data.append(data_list)
    # #
    # print outcome_data
