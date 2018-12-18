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
ALLOWED_GENDERS = ["MALE", "FEMALE", "OTHER"]

#ADVICES AND ALARMS
WEIGHT_LOSS_INSUFFICIENT_ALARM = "The patient is not losing enough weight, additional dietetic advice is required."
WEIGHT_LOSS_HIGH_ALARM = "The patient is losing too much weight, additional dietetic advice is required."
LOW_BMI_ALARM = "The BMI of the patient is below 27, dietetic supervision is required."
INCREASE_PROTEIN_INTAKE = "The protein blood value is insufficient, increase protein intake through nutrition."
SUPPLEMENT_B11 = "Vitamin B11 blood value is insufficient, additional vitamin B11 supplementation is required."
SUPPLEMENT_B12 = "Vitamin B12 blood value is insufficient, additional vitamin B12 supplementation is required."
SPECIALIST_ALARM_B12 = "Vitamin B12 blood value is insufficient, while vitamin B12 supplementation is taken. Additional B12 injections are required, refer to an internist."
SUPPLEMENT_D = "Vitamin D blood value is insufficient, more nutrition rich in vitamin D, or additional vitamin D supplementation is required."
SUPPLEMENT_IRON = "Iron blood value is insufficient. More nutrition, rich in iron, or additional iron supplementation is required."
INCREASE_FOOD_PROTEIN_AMOUNT = "The protein intake is insufficient, increase protein intake through nutrition."
INCREASE_VALUABLE_CARB_INTAKE = "The carbohydrate intake is mostly coming from a non-valuable carbohydrates, increase valuable carbohydrate sources."
INCREASE_UNSATURATED_FAT_INTAKE = "The fat intake is mostly coming from saturated fats, increase unsaturated fats intake."
SPREAD_PROTEIN_INTAKE = "The protein intake is not spread out throughout the day, spread it out more."
SPREAD_CARB_INTAKE = "The carbohydrate intake is not spread out throughout the day, spread it out more."
SPREAD_FAT_INTAKE = "The fat intake is not spread out throughout the day, spread it out more."
WATER_ALARM = "The patient can not drink water, additional examination is required."
SUPPLEMENT_MULTIVITAMINS = "The patient is not taking multivitamines, multivitamines supplementation is required."
MOVE_ENOUGH = "The patient does not exercise enough. The advice is to move 30 minutes to an hour, 5 times a week, with moderate intensity."
INSUFFICIENT_DEFECATION_ALARM = "The defecation frequency is too low, more fibres and/or water needs to be taken."
HIGH_DEFECATION_ALARM = "The defecation frequency is too high, a doctor needs to analyze the patient."
EATING_MOMENTS_6_11 = "The patient's eating moment frequency is too low. The patient needs to spread out his/her meals to at least 6 meals per day."
DIVIDE_FOOD_DRINK_INTAKE = "The patient does not separate food and water intake. The patient is adviced to do so."
SLOW_DOWN_INTAKE = "The patient eats at a fast pace, a slower food intake is adviced."
SOURCE_ALARM = "The patient suffers from one or more complaints (stomach ache, nausea, or vomiting). This complaint is most likely caused by a specific nutritient, further investigation is required."
LOWER_FAT_INTAKE = "The fat intake of the patient is too high, a lower fat intake is adviced."
INCREASE_INTAKE = "The patient does not eat enough. A higher calorie intake is adviced."
HEALTH_ALARM = "The patient suffers from one or more complaints which are not easily explained by the patient his/her food intake (feeling cold, fatigue, hair loss, or dumping). Additional investigation is required."

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
    if (patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery < 0.8:
        print(WEIGHT_LOSS_INSUFFICIENT_ALARM)
    elif (patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery > 1.5:
        print(WEIGHT_LOSS_HIGH_ALARM)

    if patient.current_weight / (patient.height ** 2) < 27:
        print(LOW_BMI_ALARM)

    if patient.protein < 60:
        print(INCREASE_PROTEIN_INTAKE)

    if patient.B11 < 5.9:
        print(SUPPLEMENT_B11)

    if patient.B12 < 200 and patient.supplements_B12 == False:
        print(SUPPLEMENT_B12)
    elif patient.B12 < 200 and patient.supplements_B12 == True:
        print(SPECIALIST_ALARM_B12)

    if patient.D < 20:
        print(SUPPLEMENT_D)

    if patient.iron < 14 and patient.gender == "MALE":
        print(SUPPLEMENT_IRON)
    elif patient.iron < 10 and patient.gender == "FEMALE":
        print(SUPPLEMENT_IRON)

    if  patient.protein_intake < (0.8 * (patient.length ** 2) * 27) and patient.protein_source == "ANIMAL":
        print(INCREASE_PROTEIN_INTAKE)
    if patient.protein_source == "PLANT": #vegetarian?
        print(INCREASE_FOOD_PROTEIN_AMOUNT)

    if patient.carb_intake_valuable == False:
        print(INCREASE_VALUABLE_CARB_INTAKE) #?????

    if patient.unsat_fat_intake_sufficient == False:
        print(INCREASE_UNSATURATED_FAT_INTAKE)

    #intake spreads
    if patient.protein_intake_spread == False:
        print(SPREAD_PROTEIN_INTAKE)
    if patient.carb_intake_spread == False:
        print(SPREAD_CARB_INTAKE)
    if patient.fat_intake_spread == False:
        print(SPREAD_FAT_INTAKE)

    if patient.water_possibility == False:
        print(WATER_ALARM)

    if patient.supplements_vitamins == False:
        print(SUPPLEMENT_MULTIVITAMINS)
    if patient.supplements_B12 == False:
        print(SUPPLEMENT_B12)

    if patient.enough_movement == False:
        print(MOVE_ENOUGH) #what is enough?

    if patient.defecation_freq < 2:
        print(INSUFFICIENT_DEFECATION_ALARM)
    elif patient.defecation_freq > 14:
        print(HIGH_DEFECATION_ALARM)

    if patient.eating_moments < 6:
        print(EATING_MOMENTS_6_11)
    if patient.divided_intake == False:
        print(DIVIDE_FOOD_DRINK_INTAKE)
    if patient.slow_intake == False:
        print(SLOW_DOWN_INTAKE)

    #complaints
    if patient.stomach_ache == True:
        if patient.slow_intake == False:
            print(SLOW_DOWN_INTAKE)
            #also add why?
        if patient.eating_moments < 6:
            print(EATING_MOMENTS_6_11)
        print(SOURCE_ALARM) #?????

    if patient.nausea == True:
        if patient.slow_intake == False:
            print(SLOW_DOWN_INTAKE) #says calm = false??
        if patient.eating_moments < 6:
            print(EATING_MOMENTS_6_11)
        if patient.fat_intake > 50:
            print(LOWER_FAT_INTAKE) #to below 50g?
        print(SOURCE_ALARM)

    if patient.vomiting == True:
        if patient.divided_intake == False:
            print(DIVIDE_FOOD_DRINK_INTAKE)
        if patient.slow_intake == False:
            print(SLOW_DOWN_INTAKE) #again, calm=false??
        if patient.eating_moments < 6:
            print(EATING_MOMENTS_6_11)
        print(SOURCE_ALARM)

    if patient.feeling_cold == True or patient.fatigue == True:
        if ((patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery) > 1.5:
            print(INCREASE_INTAKE)
        print(HEALTH_ALARM)

    if patient.hair_loss == True:
        if patient.protein < 60:
            print(INCREASE_PROTEIN_INTAKE)
        if patient.supplements_multivitamins == False:
            print(SUPPLEMENT_MULTIVITAMINS)
        print(HEALTH_ALARM)

    if patient.dumping == True:
        if patient.carb_intake_valuable == False:
            print(INCREASE_VALUABLE_CARB_INTAKE)
        print(HEALTH_ALARM)




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