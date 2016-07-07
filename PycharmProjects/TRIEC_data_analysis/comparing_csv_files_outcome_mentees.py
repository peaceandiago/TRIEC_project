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
        next(mentees_reader, None)
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

