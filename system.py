"""
@Author: Deagan Otterspeer
@Contact: d<dot>d<dot>otterspeer<dot>vu<at>gmail<dot>com
@Author: Skip Overgoor
@Contact: skip<at>overgoor<dot>nl

This code represent a dietetic advice construction system for patients which had a stomach reduction.
Structure of code: constants and import classes, system input functions and main program flow.
"""


''' -| CONSTANTS AND IMPORTS |- '''
from patient import Patient

WELCOME_STRING = '''Welcome to the dietetic advisory aiding system!
This system is made to aid during the second meeting after a stomach reduction.
To start, please enter the general patient information first.'''
ALLOWED_GENDERS = ["male", "Male", "female", "Female", "other", "Other"]


''' -| PROGRAM FUNCTIONS |- '''

def gather_general_info():
    success = True
    patient_name = input("First and nast name:\n")
    # check for existence of name or ID in a DB is possible here
    gender = input("Gender (Male / Female / Other):\n")
    height = input("Height in cm:\n")
    weeks_after_surgery = input("Number of weeks since surgery:\n")
    weight_at_surgery = input("The patient's weight at time of surgery in kg:")
    current_weight = input("Current weight in kg:\n")

    if gender not in ALLOWED_GENDERS:
        print("Wrong gender provided. Please try again.")
        success = False
    try:
        height = int(height)
        weight_at_surgery = float(weight_at_surgery)
        weeks_after_surgery = int(weeks_after_surgery)
        current_weight = float(current_weight)
    except:
        print("Some of the values were not castable to the correct datatypes (ints of floats), please check input and try again.")
        success = False
    return success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight

def gather_lab_values():
    success = True
    return success, lab_date, protein, B11, B12, D, iron

def gather_intake_information():
    success = True
    return success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake

''' -| START OF PROGRAM |- '''
while True:

    print(WELCOME_STRING)
    success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    while not success:
        success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    else:
        print("You have entered the following patient information:", patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight, sep="\n")
        patient = Patient(patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight)


    print("Before moving on to the patient-provided information, please enter the lab values.\n")
    success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    while not success:
        success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    else:
        print("You have entered the following lab values:", lab_date, protein, B11, B12, D, iron, sep="\n")
        patient.enter_lab_values()

        
    print("Next, please gather monitoring values of nutritional intake per day from the patient.")
    success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake = gather_intake_information()
    while not success:
        success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake = gather_intake_information()
        patient.enter_intake(water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake)
    else:
        print("You have entered the following intake variables given by the patient: ", water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake, sep="\n")

    print("-" * 30)