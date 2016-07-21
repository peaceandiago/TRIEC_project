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
    data_out = open("all_mentor_attributes.csv", "rU")
    reader = csv.reader(data_out)
    next(reader, None)
    job_count = {}
    start_date = datetime.date(YEARS, 04, 01)
    end_date = datetime.date(YEARS + 1, 03, 31)
    for rows in reader:
        date = datetime.datetime.strptime(rows[3], '%m/%d/%Y').date()
        if start_date <= date <= end_date:
            job_count.setdefault(rows[7], 0)
            job_count[rows[7]] += 1
    return job_count

fiscalyearmentees2005_2006_dict = createJobCountMentees(2005)
fiscalyearmentees2006_2007_dict = createJobCountMentees(2006)
fiscalyearmentees2007_2008_dict = createJobCountMentees(2007)
fiscalyearmentees2008_2009_dict = createJobCountMentees(2008)
fiscalyearmentees2009_2010_dict = createJobCountMentees(2009)
fiscalyearmentees2010_2011_dict = createJobCountMentees(2010)
fiscalyearmentees2011_2012_dict = createJobCountMentees(2011)
fiscalyearmentees2012_2013_dict = createJobCountMentees(2012)
fiscalyearmentees2013_2014_dict = createJobCountMentees(2013)
fiscalyearmentees2014_2015_dict = createJobCountMentees(2014)
fiscalyearmentees2015_2016_dict = createJobCountMentees(2015)

def writetoFile(dict, file_name):
    """
    :param dict: the dictionary for each fiscal year containing the job counts
    :param file_name: any name given to the written csv
    :return: csv file
    """
    writer = csv.writer(open(file_name, "wb"))
    for key, value in dict.iteritems():
        writer.writerow([key, value])
    return writer

fiscalyear2005mentorsfile = writetoFile(fiscalyearmentees2005_2006_dict, "fiscalyearmentors2005_2006_dict.csv")
fiscalyear2006mentorsfile = writetoFile(fiscalyearmentees2006_2007_dict, "fiscalyearmentors2006_2007_dict.csv")
fiscalyear2007mentorsfile = writetoFile(fiscalyearmentees2007_2008_dict, "fiscalyearmentors2007_2008_dict.csv")
fiscalyear2008mentorsfile = writetoFile(fiscalyearmentees2008_2009_dict, "fiscalyearmentors2008_2009_dict.csv")
fiscalyear2009mentorsfile = writetoFile(fiscalyearmentees2009_2010_dict, "fiscalyearmentors2009_2010_dict.csv")
fiscalyear2010mentorsfile = writetoFile(fiscalyearmentees2010_2011_dict, "fiscalyearmentors2010_2011_dict.csv")
fiscalyear2011mentorsfile = writetoFile(fiscalyearmentees2011_2012_dict, "fiscalyearmentors2011_2012_dict.csv")
fiscalyear2012mentorsfile = writetoFile(fiscalyearmentees2012_2013_dict, "fiscalyearmentors2012_2013_dict.csv")
fiscalyear2013mentorsfile = writetoFile(fiscalyearmentees2013_2014_dict, "fiscalyearmentors2013_2014_dict.csv")
fiscalyear2014mentorsfile = writetoFile(fiscalyearmentees2014_2015_dict, "fiscalyearmentors2014_2015_dict.csv")
fiscalyear2015mentorsfile = writetoFile(fiscalyearmentees2015_2016_dict, "fiscalyearmentors2015_2016_dict.csv")

