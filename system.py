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
    weight_at_surgery = input("The patient's weight at time of surgery in kg:\n")
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
    lab_date = input("Please enter the date of the blood test:\n")
    protein = input("Please enter the protein levels:\n")
    B11  = input("Please enter the vitamin B11 levels:\n")
    B12  = input("Please enter te vitamin B12 levels:\n")
    D  = input("Please enter the vitamin D levels:\n")
    iron  = input("Please enter the iron levels:\n")
    try:
        protein = float(protein)
        B11 = float(B11)
        B12 = float(B12)
        D = float(D)
        iron = float(iron)
    except:
        print("Some of the lab values entered could not be casted to float, please check input and try again.")
        success = False
    return success, lab_date, protein, B11, B12, D, iron

def gather_intake_information():
    success = True
    water = input("Please ask the patient how much water he drinks per day (in cl):\n")
    water_possibility = True if input("Is the patient able to drink water? (True or False)\n") in ["True", "true"] else False
    enough_movement = True if input("Does the patient move enough? (what is enough? True or False)\n") in ["True", "true"] else False
    defecation_freq = input("Per day, how often does the patient defecate?\n")
    right_defecation_consistency = True if input("Does the patient's defecation appear to have the right consistency? (True or False)\n") in ["True", "true"] else False
    eating_moments = input("How often does the patient eat per day?\n")
    divided_food_water = True if input("Does the patient eat and drink separately? (True or False)\n") in ["True", "true"] else False
    slow_intake = True if input("Does the patient take sufficient time to take in food? (True or False)\n") in ["True", "true"] else False
    try:
        water = int(water)
        defecation_freq = int(defecation_freq)
        eating_moments = int(eating_moments)
    except:
        print("Some of the values entered could not be casted into ints, please check input and try again.")
        success=False
    return success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake

def gather_complaints():
    stomach_ache = True if input("Does the patient experience stomach aches? (True or False)\n") in ["True", "true"] else False
    vomiting = True if input("Does the patient vomit frequently? (True or False)\n") in ["True", "true"] else False
    feeling_cold = True if input("Does the patient feel constantly cold? (True or False)\n") in ["True", "true"] else False
    hair_loss = True if input("Has the patient lost considerable hair? (True or False)\n") in ["True", "true"] else False
    dumping = True if input("Does the patient mention problems which hint at gastric dumping syndrome? (True or False)\n") in ["True", "true"] else False
    fatigue = True if input("Does the patient feel continuously tired? (True or False)\n") in ["True", "true"] else False
    nausea = True if input("Does the patient feel dizzy or nauseous frequently? (True or False)\n") in ["True", "true"] else False
    return stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea

def give_advice(patient:Patient):
    #all the rules
    if (patient.weight_at_surgery - patient.current_weight) /


''' -| START OF PROGRAM |- '''
while True:

    print(WELCOME_STRING)
    success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    while not success:
        success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    else:
        print("You have entered the following patient information:", patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight, sep="\n")
        patient = Patient(patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight)


    print("\nBefore moving on to the patient-provided information, please enter the lab values.")
    success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    while not success:
        success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    else:
        print("You have entered the following lab values:", lab_date, protein, B11, B12, D, iron, sep="\n")
        patient.enter_lab_values(lab_date, protein, B11, B12, D, iron)

        
    print("\nNext, please gather monitoring values of nutritional intake per day from the patient.")
    success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake = gather_intake_information()
    while not success:
        success, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake = gather_intake_information()
    else:
        print("You have entered the following intake variables given by the patient: ", water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake, sep="\n")
        patient.enter_intake(water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake)


    print("\nFinally, enter the complaints the patient mentions, after which all possibilities will be evaluated and advice will be constructed.")
    success, stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea = gather_complaints()
    while not success:
        success, stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea = gather_complaints()
    else:
        print("You have provided us the information that the patient suffers from the following complaints: ", "Stomach ache: "+stomach_ache, "Vomiting: "+vomiting, "Feeling cold: "+feeling_cold, "Hair loss: "+hair_loss, "Dumping: "+dumping, "Fatigue: "+fatigue, "Nausea : "+nausea, sep="\n")
        patient.enter_complaints(stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea)

    give_advice(patient)
    print("-" * 30)