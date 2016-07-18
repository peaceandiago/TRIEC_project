import csv


directory = "mentor"
suffix =" question "
#WORKPLACE CONTACT INFORMATION
employer_partner = {}
job_title = {}
not_listed_employer = {}
years_worked_in_profession = {}
detailed_job_description = {}
work_address = {}
linkedin = {}
city = {}
postal_code = {}
alternate_telephone = {}
gender = {}
#EDUCATION AND CREDENTIALS
highest_education = {}
other_highest_education = {}
degree_name = {}
partner_association = {}
professional_association = {}
#MEETING PLACE PREFERENCE
place_meet_mentee = {}
time_meet_mentee = {}
#RECRUITED BY
find_program = {}
pins = {}
recruited = {}
person_referred = {}


with open("mentor_attributes.csv", "r") as mentor_file:
    mentor_reader = csv.reader(mentor_file)
    next(mentor_file, None)

    for rows in mentor_reader:
        employer_partner.setdefault(rows[11], 0)
        employer_partner[rows[11]] += 1
        years_worked_in_profession.setdefault(rows[12], 0)
        years_worked_in_profession[rows[12]] += 1
        person_referred.setdefault(rows[13], 0)
        person_referred[rows[13]] += 1
        not_listed_employer.setdefault(rows[14], 0)
        not_listed_employer[rows[14]] += 1
        other_highest_education.setdefault(rows[16], 0)
        other_highest_education[rows[16]] += 1
        highest_education.setdefault(rows[17], 0)
        highest_education[rows[17]] += 1
        degree_name.setdefault(rows[18], 0)
        degree_name[rows[18]] += 1
        job_title.setdefault(rows[19], 0)
        job_title[rows[19]] += 1
        professional_association.setdefault(rows[20], 0)
        professional_association[rows[20]] += 1
        detailed_job_description.setdefault(rows[21], 0)
        detailed_job_description[rows[21]] += 1
        partner_association.setdefault(rows[22], 0)
        partner_association[rows[22]] += 1
        linkedin.setdefault(rows[23], 0)
        linkedin[rows[23]] += 1
        work_address.setdefault(rows[24], 0)
        work_address[rows[24]] += 1
        time_meet_mentee.setdefault(rows[25], 0)
        time_meet_mentee[rows[25]] += 1
        city.setdefault(rows[27], 0)
        city[rows[27]] += 1
        recruited.setdefault(rows[28], 0)
        recruited[rows[28]] += 1
        place_meet_mentee.setdefault(rows[29], 0)
        place_meet_mentee[rows[29]] += 1
        postal_code.setdefault(rows[30], 0)
        postal_code[rows[30]] += 1
        find_program.setdefault(rows[31], 0)
        find_program[rows[31]] += 1
        alternate_telephone.setdefault(rows[32], 0)
        alternate_telephone[rows[32]] += 1
        gender.setdefault(rows[34], 0)
        gender[rows[34]] += 1
        pins.setdefault(rows[102], 0)
        pins[rows[102]] += 1

def calculate_completed_questions(dictionary):
    values_sum = sum(dictionary.values())
    no_answer_dict = dict((key, value) for key, value in dictionary.items() if key == 'n/a' or key == ' ' or key == "Please Select" or key == '' or key == "\'\'")
    no_answer = sum(no_answer_dict.values())
    percentage = (float(no_answer) / float(values_sum)) * 100
    return round(100 - percentage, 2)



WORKPLACE_CONTACT_INFORMATION = ["employer partner" + suffix + str(calculate_completed_questions(employer_partner)), "job title" + suffix + str(calculate_completed_questions(job_title)), "not listed employer" + suffix +str(calculate_completed_questions(not_listed_employer)),
                                 "years worked in profession" + suffix + str(calculate_completed_questions(years_worked_in_profession)), "years worked in profession" + suffix + str(calculate_completed_questions(years_worked_in_profession)),
                                 "detailed job description" + suffix + str(calculate_completed_questions(detailed_job_description)), "work address" + suffix + str(calculate_completed_questions(work_address)),
                                 "linkedin" + suffix + str(calculate_completed_questions(linkedin)), "city" + suffix + str(calculate_completed_questions(city)), "postal code" + suffix + str(calculate_completed_questions(postal_code)),
                                 "alternate_telephone" + suffix + str(calculate_completed_questions(alternate_telephone)), "gender" + suffix + str(calculate_completed_questions(gender))]


EDUCATION_AND_CREDENTIALS = ["highest_education" + suffix + str(calculate_completed_questions(highest_education)), "other_highest_education" + suffix + str(calculate_completed_questions(other_highest_education)),
                             "degree_name" + suffix + str(calculate_completed_questions(degree_name)), "partner_association" + suffix + str(calculate_completed_questions(partner_association)),
                             "professional_association" + suffix + str(calculate_completed_questions(professional_association))]

MEETING_PLACE_PREFERENCE = ["place_meet_mentee" + suffix + str(calculate_completed_questions(place_meet_mentee)), "time_meet_mentee" + suffix + str(calculate_completed_questions(time_meet_mentee))]

RECRUITED_BY = ["find_program" + suffix + str(calculate_completed_questions(find_program)), "pins" + suffix + str(calculate_completed_questions(pins)),
                "recruited" + suffix + str(calculate_completed_questions(recruited)), "person_referred" + suffix + str(calculate_completed_questions(person_referred))]



print WORKPLACE_CONTACT_INFORMATION
print EDUCATION_AND_CREDENTIALS
print MEETING_PLACE_PREFERENCE
print RECRUITED_BY

# myfile = open("workplace.csv", 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(RECRUITED_BY)
