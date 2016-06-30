"""
This program aims to clean the dataset to answer the question "Occupations of mentees/mentors registered per fiscal year"
"""
import csv
from datetime import timedelta, date

def isolateDate(csv_file): #remove time element from dataset
    file_in = open(csv_file, "rU")
    reader = csv.reader(file_in)
    next(file_in,None)
    new_date = []
    for line in reader:
        date = line[3]
        date = date.split()
        new_date.append(date[0])
    return new_date

mentee_date = isolateDate("mentees_all_attributes.csv") #all dates in the mentee csv

#print mentee_date

def daterange(start_date, end_date):  #create range of dates
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2005, 4, 1)
end_date = date(2006, 4, 1)
for single_date in daterange(start_date, end_date):
    first_year = single_date

    print first_year

def compare(list1, list2):
    for value in list1:
        if value in list2:
            return value

first_fiscal_year = compare(mentee_date,first_year)
print first_fiscal_year


