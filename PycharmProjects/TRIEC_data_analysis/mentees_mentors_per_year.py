"""
This program aims to clean the dataset to answer the question "Occupations of mentees/mentors registered per fiscal year"
"""
import csv
from datetime import timedelta, date
import datetime

data_out = open("mentees_all_attributes.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)


def create_dates(year):
    start_date = datetime.date(year, 04, 01)
    end_date = datetime.date(year, 03, 31)
    return start_date, end_date



def createJobCount():
    """
    Function to take start and end date and compare to file to return the occupation
    :return: counts for each occupation for each job
    """
    job_count = {}
    for rows in reader:
        date = datetime.datetime.strptime(rows[3], '%Y-%m-%d %H:%M:%S').date()
        if start_date <= date <= end_date:
            job_count.setdefault(rows[7], 0)
            job_count[rows[7]] += 1
    print job_count