import csv
import datetime


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


with open("new_mentor_attributes.csv", "r") as mentor_file:
    mentor_reader = csv.reader(mentor_file)
    next(mentor_file, None)
    start_date = datetime.date(2012, 04, 1)
    end_date = datetime.date(2016, 03, 31)
    for rows in mentor_reader:
        date = datetime.datetime.strptime(rows[3], '%m/%d/%Y').date()
        if start_date <= date <= end_date:
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
    new_dict = dict((key, value) for key, value in dictionary.iteritems())
    new_dict = sum(new_dict.values())
    nu_dict = dict((key, value) for key, value in dictionary.iteritems() if key == 'n/a' or key == ' ' or key == "Please Select" or key == '' or key == "\'\'")
    nu_dict = sum(nu_dict.values())
    percentage = (float(nu_dict) / float(new_dict)) * 100
    return round(100 - percentage, 2)



all_content = {}
all_content['employer_partner'] = calculate_completed_questions(employer_partner)
all_content['job title'] = calculate_completed_questions(job_title)
all_content['not listed employer'] = calculate_completed_questions(not_listed_employer)
all_content['years worked in profession'] = calculate_completed_questions(years_worked_in_profession)
all_content['detailed job description'] = calculate_completed_questions(detailed_job_description)
all_content['work_address'] = calculate_completed_questions(work_address)
all_content['linkedin'] = calculate_completed_questions(linkedin)
all_content['city'] = calculate_completed_questions(city)
all_content['postal code'] = calculate_completed_questions(postal_code)
all_content['alternate telephone'] = calculate_completed_questions(alternate_telephone)
all_content['gender'] = calculate_completed_questions(gender)
all_content['highest education'] = calculate_completed_questions(highest_education)
all_content['other highest education'] = calculate_completed_questions(other_highest_education)
all_content['degree name'] = calculate_completed_questions(degree_name)
all_content['partner association'] = calculate_completed_questions(partner_association)
all_content['professional association'] = calculate_completed_questions(professional_association)
all_content['place_meet_mentee'] = calculate_completed_questions(place_meet_mentee)
all_content['time meet mentee'] = calculate_completed_questions(time_meet_mentee)
all_content['find program'] = calculate_completed_questions(find_program)
all_content['pins'] = calculate_completed_questions(pins)
all_content['recruited'] = calculate_completed_questions(recruited)
all_content['person referred'] = calculate_completed_questions(person_referred)

print all_content

w = csv.writer(open("mentor_form.csv", "w"))
for key, val in all_content.items():
    w.writerow([key, val])
