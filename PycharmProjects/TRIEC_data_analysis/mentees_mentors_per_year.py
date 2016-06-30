"""
This program aims to clean the dataset to answer the question "Occupations of mentees/mentors registered per fiscal year"
"""
import csv

# file_in = open("mentees_all_attributes.csv", "rU")
# reader = csv.reader(file_in)
# next(file_in,None)
#
def isolateDate(csv_file): #remove time element from data
    file_in = open(csv_file, "rU")
    reader = csv.reader(file_in)
    next(file_in,None)
    new_date = []
    for line in reader:
        date = line[3]
        date = date.split()
        new_date.append(date[0])
    return new_date

mentee_date = isolateDate("mentees_all_attributes.csv")
print mentee_date

