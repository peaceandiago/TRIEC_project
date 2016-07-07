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

fiscalyear2005menteesfile = writetoFile(fiscalyearmentees2005_2006_dict, "fiscalyearmentees2005_2006_dict.csv")
fiscalyear2006menteesfile = writetoFile(fiscalyearmentees2006_2007_dict, "fiscalyearmentees2006_2007_dict.csv")
fiscalyear2007menteesfile = writetoFile(fiscalyearmentees2007_2008_dict, "fiscalyearmentees2007_2008_dict.csv")
fiscalyear2008menteesfile = writetoFile(fiscalyearmentees2008_2009_dict, "fiscalyearmentees2008_2009_dict.csv")
fiscalyear2009menteesfile = writetoFile(fiscalyearmentees2009_2010_dict, "fiscalyearmentees2009_2010_dict.csv")
fiscalyear2010menteesfile = writetoFile(fiscalyearmentees2010_2011_dict, "fiscalyearmentees2010_2011_dict.csv")
fiscalyear2011menteesfile = writetoFile(fiscalyearmentees2011_2012_dict, "fiscalyearmentees2011_2012_dict.csv")
fiscalyear2012menteesfile = writetoFile(fiscalyearmentees2012_2013_dict, "fiscalyearmentees2012_2013_dict.csv")
fiscalyear2013menteesfile = writetoFile(fiscalyearmentees2013_2014_dict, "fiscalyearmentees2013_2014_dict.csv")
fiscalyear2014menteesfile = writetoFile(fiscalyearmentees2014_2015_dict, "fiscalyearmentees2014_2015_dict.csv")
fiscalyear2015menteesfile = writetoFile(fiscalyearmentees2015_2016_dict, "fiscalyearmentees2015_2016_dict.csv")
