import csv
import datetime

def find_rejected_dates():
    """
    This function identifies the mentors, mentees, and RMdates under the condition 'Acceptance'
    :return: an array for mentors, mentees, RMdate
    """
    with open ("pastRMs.csv", "r") as RM_file:
        RM_reader = csv.reader(RM_file)
        next(RM_reader, None)
        RM = []
        start_date = datetime.date(2013, 04, 1)
        end_date = datetime.date(2014, 03, 31)
        for rows in RM_reader:
            date = datetime.datetime.strptime(rows[15], '%d/%m/%Y').date()
            if rows[16] == "Rejected" and start_date <= date <= end_date:
                reports_mentors = rows[0].title()
                reports_mentees = rows[7].title()
                RM_date = rows[15]
                Accepted_Cases = reports_mentors, reports_mentees, RM_date
                RM_list = list(Accepted_Cases)
                RM.append(RM_list)
        return RM
    RM_file.close()

RM_lists = find_rejected_dates()

def get_registration_date():
    """
    This function takes the identified list from the findAcceptance() and compare it with another csv to get the necessary data
    :return: list [Start_date, partnership_mentors, partnership_mentees, rmrows[2]]
    """
    with open("mentees_all_attributes.csv", "r") as PR_file:
        PR_reader = csv.reader(PR_file)
        next(PR_file, None)
        DATA = []
        for rows in PR_reader:
            mentee_names = rows[0].title()
            for rmrows in RM_lists:
                if mentee_names in rmrows[1]:
                    registration_date = rows[3]
                    data = mentee_names, registration_date, rmrows[2]
                    data_list = list(data)
                    DATA.append(data_list)
        return DATA
    PR_file.close()


data = get_registration_date()
# print data

def get_registration_date():
    DAYS = []
    for rows in data:
        if rows[0] and rows[1] and rows[2] is not None:  # remove the rows with missing data
            format_2 = '%d/%m/%Y'
            registration_date = datetime.datetime.strptime(rows[1], '%Y-%m-%d %H:%M:%S').date()
            rm_date = datetime.datetime.strptime(rows[2], '%d/%m/%Y').date()
            delta = rm_date - registration_date
            number_of_days_rm_registration = delta.days
            numbers = str(number_of_days_rm_registration)
            DAYS.append(numbers)

    return DAYS

DAYS = get_registration_date()
# print DAYS

days_summary = {}
for rows in DAYS:
    days_summary.setdefault(rows, 0)
    days_summary[rows] += 1
print days_summary

writer = csv.writer(open("RM_Registration_days.csv", "wb"))
for key, value in days_summary.items():
    writer.writerow([key, value])
