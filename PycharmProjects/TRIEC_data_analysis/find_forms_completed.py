import csv

directory = "mentor"
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
# print "Employer Partner: " + str(employer_partner)
# print "How many years have you worked in your profession? " + str(years_worked_in_profession)
# print "Name of the person at the service delivery partner who referred you: " + str(person_referred)
# print "If your employer is not listed above, please enter the name of your workplace here " + str(not_listed_employer)
# print "If you selected 'other' in the above, please specify your highest degree completed here: " + str(other_highest_education)
# print "Highest level of education completed " + str(highest_education)
# print "Please enter name of your degree and any professional license or designation " + str(degree_name)
# print "Job Title " + str(job_title)
# print "Please enter the name of any Professional Associations in Canada which you currently are a member of: " + str(professional_association)
# print "Please provide a detailed description of your current / recent job role(s). " + str(detailed_job_description)
# print "If you are a member of one of our partner associations, you may be able to claim PD credits. " + str(partner_association)
# print "LinkedIn profile:" + str(linkedin)
# print "Work Address" + str(work_address)
# print "At what time of day do you prefer to meet with your mentee? " + str(time_meet_mentee)
# print "City " + str(city)
# print "If you were recruited directly by one of our a service delivery partners: " + str(recruited)
# print "Where would you prefer to meet your mentee? " + str(place_meet_mentee)
# print "Postal Code " + str(postal_code)
# print "How did you first find out about the program? " + str(find_program)
# print "Alternate Telephone Number" + str(alternate_telephone)
# print "Gender" + str(gender)
# print "If you selected Professional Immigrant Network (PINs) in the above, please enter the name of the PINs here: " + str(pins)

