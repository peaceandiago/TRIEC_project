import csv
from collections import Counter
from itertools import izip_longest


address = {}
city = {}
postal_code = {}
alternate_telephone = {}
alternate_email = {}
gender = {}
date_of_birth = {}
country_of_origin = {}
languages_spoken = {}
immigration_status = {}
other_immigration_status = {}
date_of_arrival = {}
job_search= {}
yes_select_program = {}
employed_underemployed = {}
occupation_specific_program = {}
language_assessment = {}
score_level_assessment = {}
occupation_related_education = {}
services_resouces_find_employment = {}
not_listed_services_resources = {}
years_of_work_experience = {}
highest_level_education = {}
country_level_education= {}
professional_association = {}
outside_canada_professional_association = {}
profession_regulated = {}
pursue_planning_license = {}
licensure_pursuing = {}
licensure_pursuing_not_listed = {}
far_in_process = {}
bridge_traning_program = {}
date_registration_bridge = {}
name_program_participated = {}
bridge_program_not_listed = {}
length_of_program = {}
pursuing_education_skills = {}
years_worked_before_Canada = {}
last_job_before_Canada = {}
length_of_time = {}
short_term_goals = {}
long_term_goals = {}
income_security_benefits = {}
employed_within_field = {}
level_last_employment = {}
period_of_time = {}
current_job_title = {}
approximate_earnings = {}

with open("mentees_all_attributes.csv", "r") as mentee_file:
    menteer_reader = csv.reader(mentee_file)
    next(mentee_file, None)

    for rows in menteer_reader:
        address.setdefault(rows[26],0)
        address[rows[26]] += 1
        city.setdefault(rows[27],0)
        city[rows[27]] += 1
        postal_code.setdefault(rows[30],0)
        postal_code[rows[30]] += 1
        alternate_telephone.setdefault(rows[32],0)
        alternate_telephone[rows[32]] += 1
        gender.setdefault(rows[34],0)
        gender[rows[34]] += 1
        date_of_birth.setdefault(rows[33],0)
        date_of_birth[rows[33]] += 1
        country_of_origin.setdefault(rows[35], 0)
        country_of_origin[rows[35]] += 1
        languages_spoken.setdefault(rows[36], 0)
        languages_spoken[rows[36]] += 1
        immigration_status.setdefault(rows[37], 0)
        immigration_status[rows[37]] += 1
        other_immigration_status.setdefault(rows[38], 0)
        other_immigration_status[rows[38]] += 1
        date_of_arrival.setdefault(rows[39], 0)
        date_of_arrival[rows[39]] += 1
        job_search.setdefault(rows[40], 0)
        job_search[rows[40]] += 1
        yes_select_program.setdefault(rows[41], 0)
        yes_select_program[rows[41]] += 1
        employed_underemployed.setdefault(rows[42], 0)
        employed_underemployed[rows[42]] += 1
        occupation_specific_program.setdefault(rows[43], 0)
        occupation_specific_program[rows[43]] += 1
        language_assessment.setdefault(rows[44], 0)
        language_assessment[rows[44]] += 1
        score_level_assessment.setdefault(rows[45], 0)
        score_level_assessment[rows[45]] += 1
        occupation_related_education.setdefault(rows[46], 0)
        occupation_related_education[rows[46]] += 1
        services_resouces_find_employment.setdefault(rows[47], 0)
        services_resouces_find_employment[rows[47]] += 1
        not_listed_services_resources.setdefault(rows[48], 0)
        not_listed_services_resources[rows[48]] += 1
        years_of_work_experience.setdefault(rows[49], 0)
        years_of_work_experience[rows[49]] += 1
        highest_level_education.setdefault(rows[50], 0)
        highest_level_education[rows[50]] += 1
        country_level_education.setdefault(rows[51], 0)
        country_level_education[rows[51]] += 1
        professional_association.setdefault(rows[52], 0)
        professional_association[rows[52]] += 1
        outside_canada_professional_association.setdefault(rows[113], 0)
        outside_canada_professional_association[rows[113]] += 1
        profession_regulated.setdefault(rows[114], 0)
        profession_regulated[rows[114]] += 1
        pursue_planning_license.setdefault(rows[115], 0)
        pursue_planning_license[rows[115]] += 1
        licensure_pursuing.setdefault(rows[116], 0)
        licensure_pursuing[rows[116]] += 1
        licensure_pursuing_not_listed.setdefault(rows[117], 0)
        licensure_pursuing_not_listed[rows[117]] += 1
        far_in_process.setdefault(rows[118], 0)
        far_in_process[rows[118]] += 1
        bridge_traning_program.setdefault(rows[119], 0)
        bridge_traning_program[rows[119]] += 1
        date_registration_bridge.setdefault(rows[120], 0)
        date_registration_bridge[rows[120]] += 1
        name_program_participated.setdefault(rows[121], 0)
        name_program_participated[rows[121]] += 1
        bridge_program_not_listed.setdefault(rows[122], 0)
        bridge_program_not_listed[rows[122]] += 1
        length_of_program.setdefault(rows[123], 0)
        length_of_program[rows[123]] += 1
        pursuing_education_skills.setdefault(rows[124], 0)
        pursuing_education_skills[rows[124]] += 1
        years_worked_before_Canada.setdefault(rows[125], 0)
        years_worked_before_Canada[rows[125]] += 1
        last_job_before_Canada.setdefault(rows[126], 0)
        last_job_before_Canada[rows[126]] += 1
        length_of_time.setdefault(rows[127], 0)
        length_of_time[rows[127]] += 1
        short_term_goals.setdefault(rows[128], 0)
        short_term_goals[rows[128]] += 1
        long_term_goals.setdefault(rows[129], 0)
        long_term_goals[rows[129]] += 1
        income_security_benefits.setdefault(rows[130], 0)
        income_security_benefits[rows[130]] += 1
        employed_within_field.setdefault(rows[131], 0)
        employed_within_field[rows[131]] += 1
        level_last_employment.setdefault(rows[132], 0)
        level_last_employment[rows[132]] += 1
        period_of_time.setdefault(rows[133], 0)
        period_of_time[rows[133]] += 1
        current_job_title.setdefault(rows[134], 0)
        current_job_title[rows[134]] += 1
        approximate_earnings.setdefault(rows[135], 0)
        approximate_earnings[rows[135]] += 1



def calculate_completed_questions(dictionary):
    new_dict = dict((key, value) for key, value in dictionary.iteritems())
    new_dict = sum(new_dict.values())
    print new_dict
    nu_dict = dict((key, value) for key, value in dictionary.iteritems() if key == 'n/a' or key == ' ' or key == "Please Select" or key == '' or key == "\'\'")
    nu_dict = sum(nu_dict.values())
    print nu_dict
    percentage = (float(nu_dict) / float(new_dict)) * 100
    return round(percentage, 2)

CONTACT_INFORMATION = {}
CONTACT_INFORMATION['address'] = calculate_completed_questions(address)
CONTACT_INFORMATION['city'] = calculate_completed_questions(city)
CONTACT_INFORMATION['postal code'] = calculate_completed_questions(postal_code)
CONTACT_INFORMATION['alternate telephone'] = calculate_completed_questions(alternate_telephone)
# CONTACT_INFORMATION['alternate email'] = calculate_completed_questions(alternate_email)
CONTACT_INFORMATION['gender'] = calculate_completed_questions(gender)
PERSONAL_INFORMATION = {}
PERSONAL_INFORMATION['date of birth'] = calculate_completed_questions(date_of_birth)
PERSONAL_INFORMATION['country of origin'] = calculate_completed_questions(country_of_origin)
PERSONAL_INFORMATION['languages spoken'] = calculate_completed_questions(languages_spoken)
PROGRAM_ELIGIBILITY = {}
# immigration_status = {}
# other_immigration_status = {}
# date_of_arrival = {}
# job_search= {}
# yes_select_program = {}
# employed_underemployed = {}
# occupation_specific_program = {}
# language_assessment = {}
# score_level_assessment = {}
# occupation_related_education = {}
# services_resouces_find_employment = {}
# not_listed_services_resources = {}
# years_of_work_experience = {}
EDUCATION_PROFESSIONAL_CREDENTIALS = {}
# highest_level_education = {}
# country_level_education= {}
# professional_association = {}
# outside_canada_professional_association = {}
REGULATED_PROFESSIONS = {}
# profession_regulated = {}
# pursue_planning_license = {}
# licensure_pursuing = {}
# licensure_pursuing_not_listed = {}
# far_in_process = {}
BRIDGE_TRANING_PROGRAM = {}
# bridge_traning_program = {}
# date_registration_bridge = {}
# name_program_participated = {}
# bridge_program_not_listed = {}
# length_of_program = {}
# pursuing_education_skills = {}
HISTORY_GOALS = {}
# years_worked_before_Canada = {}
# last_job_before_Canada = {}
# length_of_time = {}
# short_term_goals = {}
# long_term_goals = {}
EMPLOYMENT_STATUS = {}
# income_security_benefits = {}
# employed_within_field = {}
# level_last_employment = {}
# period_of_time = {}
# current_job_title = {}
# approximate_earnings = {}
print CONTACT_INFORMATION
print PERSONAL_INFORMATION