"""
This program aims to clean the dataset to answer the question "Occupations of mentees/mentors registered per fiscal year"
"""
import csv
from datetime import timedelta, date
import datetime

def createJobCountMentees(YEARS):
    """
    Function to take start and end date and compare to file to return the occupation
    :return: counts for each occupation for each job
    """
    data_out = open("mentees_all_attributes.csv", "rU")
    reader = csv.reader(data_out)
    next(reader, None)
    job_count = {}
    start_date = datetime.date(YEARS, 04, 01)
    end_date = datetime.date(YEARS + 1, 03, 31)
    for rows in reader:
        date = datetime.datetime.strptime(rows[3], '%Y-%m-%d %H:%M:%S').date()
        if start_date <= date <= end_date:
            job_count.setdefault(rows[7], 0)
            job_count[rows[7]] += 1
    return job_count


fiscalyear2010_2011_dict = createJobCountMentees(2010)

def writetoFile(dict, file_name):
    """
    :param dict: the dictionary for each fiscal year containing the job counts
    :param file_name: any name given to the written csv
    :return: csv file
    """
    writer = csv.writer(open(file_name, "wb"))
    for key, value in dict.items():
        writer.writerow([key, value])
    return writer

fiscalyear2010_2011 = writetoFile(fiscalyear2010_2011_dict, "example.csv")