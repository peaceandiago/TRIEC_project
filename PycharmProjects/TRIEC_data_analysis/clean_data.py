"""
This program is to clean the data for dataset - mentees
"""
import csv


""" These three functions help solve: Occupation of mentees/mentors registered per fiscal year"""

data_out = open("mentees_all_attributes.csv", "rU")
reader = csv.reader(data_out)
next(reader,None)

def participated(): #Participated in Mentorship
    part_counters = {}
    for line in reader:
        if int(line[6]) > 0:
            primary = line[7].strip()
            part_counters.setdefault(primary, 0)
            part_counters[primary] += 1

    # for k, v in part_counters.items():
    #     print k,v
    return part_counters


# data_out.seek(0)
# reader = csv.reader(data_out)
# next(reader,None)

# def notParticipated():
#     notpart_counters = {}
#     for line in reader:
#         if int(line[6]) == 0:
#             primary = line[7].strip()
#             notpart_counters.setdefault(primary, 0)
#             notpart_counters[primary] += 1
#
#     for k, v in notpart_counters.items():
#         print k,v
#     return notpart_counters
#
# def generalNumber(): #General number of mentees with their primary occupation
#     with open("mentees_all_attributes.csv", "rU") as data_out:
#         reader = csv.reader(data_out)
#         next(reader,None)
#         gen_counters = {}
#         for line in reader:
#             if int(line[6]) >= 0:
#                 primary = line[7].strip()
#                 gen_counters.setdefault(primary, 0)
#                 gen_counters[primary] += 1
#
#         for k, v in gen_counters.items():
#             print k, v
    #return gen_counters
#
# counter_p = participated()
# print counter_p #dictionary
# counter_g = generalNumber()
# print counter_g #dictionary
#
# for key in counter_p.iteritems():
#     print key
#
# def divide(divedends, divisors):
#     new_dict = ()
#     for key, counter_g in counter_p.iteritems():
#         print key
#         if key in counter_g:
#             new_dict[key] = counter_p/counter_g
#         else:
#             new_dict[key] = counter_p
#     print new_dict



# # dict([(k, d2[k] / float(d1[k])) for k in d1 if k in d2])
# success_percentage = dict([k, counter_p[k] / float(counter_g[k] for k in counter_g if k in counter_p)])



    #     success_percentage = counter_p[values]/counter_g[values]
    #     print success_percentage


data_out.close()
