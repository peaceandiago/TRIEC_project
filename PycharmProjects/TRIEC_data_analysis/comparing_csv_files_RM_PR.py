import csv
import datetime

def findAcceptance():
    """
    This function identifies the mentors, mentees, and RMdates under the condition 'Acceptance'
    :return: an array for mentors, mentees, RMdate
    """
    with open ("pastRMs.csv", "r") as RM_file:
        RM_reader = csv.reader(RM_file)
        next(RM_reader, None)
        RM = []
        for rows in RM_reader:
            if rows[16] == "Accepted":
                reports_mentors = rows[0].title()
                reports_mentees = rows[7].title()
                RM_date = rows[15]
                Accepted_Cases = reports_mentors, reports_mentees, RM_date
                RM_list = list(Accepted_Cases)
                RM.append(RM_list)
        return RM
    RM_file.close()

RM_lists = findAcceptance()

def neededData():
    """
    This function takes the identified list from the findAcceptance() and compare it with another csv to get the necessary data
    :return: list [Start_date, partnership_mentors, partnership_mentees, rmrows[2]]
    """
    with open("partnership_report.csv", "r") as PR_file:
        PR_reader = csv.reader(PR_file)
        next(PR_file, None)
        DATA = []
        for rows in PR_reader:
            partnership_mentors = rows[2].title()
            partnership_mentees = rows[5].title()
            for rmrows in RM_lists:
                if partnership_mentees in rmrows[1] and partnership_mentors in rmrows[0]:
                    start_date = rows[0]
                    data = start_date, partnership_mentees, partnership_mentors, rmrows[2]
                    data_list = list(data)
                    DATA.append(data_list)
        return DATA
    PR_file.close()


data = neededData()
# print data

def isolateDate():
    """
    This function isolates the two dates that are needed and puts them into a consistent format and converts them into objects instead of string
    then subtract the start date from the RM date and convert it back to the string to make it a list of strings
    :return: days between RM and Start_dates
    """
    DAYS = []
    for rows in data:
        if rows[0] and rows[1] and rows[2] and rows[3] is not None:  # remove the rows with missing data
            format_2 = '%d %m %Y'
            start_date = datetime.datetime.strptime(rows[0], '%d-%b-%y')
            rm_date = datetime.datetime.strptime(rows[3], '%d/%m/%Y')
            delta = start_date - rm_date
            number_of_days_rm_pr = delta.days
            numbers = str(number_of_days_rm_pr)
            DAYS.append(numbers)
    return DAYS

DAYS = isolateDate()

def countDays():
    days_summary = {}
    for rows in DAYS:
        days_summary.setdefault(rows, 0)
        days_summary[rows] += 1
    return days_summary

print countDays()


#This function is to check whether two documents match - or the functions are working properly
# with open("partnership_report.csv", "r") as PR_file:
#     PR_reader = csv.reader(PR_file)
#     next(PR_file, None)
#     count = {}
#     new_count = {}
#     for rows in PR_reader:
#         partnership_mentors = rows[2].title()
#         partnership_mentees = rows[5].title()
#         sdate = rows[0]
#         count.setdefault(sdate, 0)
#         count[sdate] += 1
#         for rows in RM_lists:
#             if partnership_mentees in rows[1] and partnership_mentors in rows[0]:
#                 # RM_date = rows[15]
#                 Start_date = rows[0]
#                 new_count.setdefault(Start_date, 0)
#                 new_count[Start_date] += 1
#         print new_count
#         print count
