import csv

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
                Accepted_Cases = reports_mentors, reports_mentees, RM_date         #Put this all in one list
                RM_list = list(Accepted_Cases)
                RM.append(RM_list)
        return RM

RM_lists = findAcceptance()

def neededData():
    """
    This function takes the identified list from the findAcceptance() and compare it with another csv to get the necessary data
    :return: Start_date, partnership_mentors, partnership_mentees, rmrows[2]
    """

    with open("partnership_report.csv", "r") as PR_file:
        PR_reader = csv.reader(PR_file)
        next(PR_file, None)
        for rows in PR_reader:
            partnership_mentors = rows[2].title()
            partnership_mentees = rows[5].title()
            for rmrows in RM_lists:
                if partnership_mentees in rmrows[1] and partnership_mentors in rmrows[0]:
                    Start_date = rows[0]
                return Start_date, partnership_mentors, partnership_mentees, rmrows[2]







# with open ("pastRMs.csv", "r") as RM_file:
#     RM_reader = csv.reader(RM_file)
#     next(RM_reader, None)
#     RM_Mentor_List = []
#     RM_Mentee_List = []
#     for rows in RM_reader:
#         if rows[16] == "Accepted":
#             reports_mentors = rows[0].title()
#             reports_mentees = rows[7].title()
#             RM_date = rows[15]
#             print reports_mentees, reports_mentors, RM_date
#
#


#             RM_Mentor_List.append(reports_mentors)
#             RM_Mentee_List.append(reports_mentees)
#
#
# past_reports_mentees = RM_Mentee_List
# past_reports_mentors = RM_Mentor_List
# print past_reports_mentees
# print past_reports_mentors
#
# RM_file.close()
#
#
# # with open("partnership_report.csv", "r") as PR_file:
# #     PR_reader = csv.reader(PR_file)
# #     next(PR_file, None)
# #     count = {}
# #     new_count = {}
# #     for rows in PR_reader:
# #         partnership_mentors = rows[2].title()
# #         partnership_mentees = rows[5].title()
# #         sdate = rows[0]
# #         count.setdefault(sdate, 0)
# #         count[sdate] += 1
# #         if partnership_mentees in past_reports_mentees and partnership_mentors in past_reports_mentors:
# #             # RM_date = rows[15]
# #             Start_date = rows[0]
# #             new_count.setdefault(Start_date, 0)
# #             new_count[Start_date] += 1
# #     print new_count
# #     print count
# with open ("pastRMs.csv", "r") as RM_file:
#     with open("partnership_report.csv", "r") as PR_file:
#         PR_reader = csv.reader(PR_file)
#         RM_reader = csv.reader(RM_file)
#         next(PR_file, None)
#         next(RM_reader, None)
#         for rows in PR_reader:
#             partnership_mentors = rows[2].title()
#             partnership_mentees = rows[5].title()
#             if partnership_mentees in past_reports_mentees and partnership_mentors in past_reports_mentors:
#                 Start_date = rows[0]
#
#                 # print Start_date, partnership_mentors, partnership_mentees
#                     # if partnership_mentees == reports_mentees and partnership_mentors == reports_mentors:
#                     #     print lines[15]
#                     #