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
INCREASE_PROTEIN_INTAKE = "The protein intake is insufficient, increase protein intake through nutrition."
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
DIVIDE_FOOD_DRINK_INTAKE = "The patient does not separate food and water intake. The patient is advised to do so."
SLOW_DOWN_INTAKE = "The patient eats at a fast pace, a slower food intake is advised."
SOURCE_ALARM = "The patient suffers from one or more complaints (stomach ache, nausea, or vomiting). This complaint is most likely caused by a specific nutritient, further investigation is required."
LOWER_FAT_INTAKE = "The fat intake of the patient is too high, a lower fat intake is advised."
INCREASE_INTAKE = "The patient does not eat enough. A higher calorie intake is advised."
HEALTH_ALARM = "The patient suffers from one or more complaints which are not easily explained by the patient his/her food intake (feeling cold, fatigue, hair loss, or dumping). Additional investigation is required."

''' -| PROGRAM FUNCTIONS |- '''

def gather_general_info():
    success = True
    patient_name = input("First and nast name:\n")
    # check for existence of name or ID in a DB is possible here
    gender = input("Gender (MALE / FEMALE / OTHER):\n")
    height = input("Height in m:\n")
    weeks_after_surgery = input("Number of weeks since surgery:\n")
    weight_at_surgery = input("The patient's weight at time of surgery in kg:\n")
    current_weight = input("Current weight in kg:\n")

    if gender not in ALLOWED_GENDERS:
        print("Wrong gender provided. Please try again.")
        success = False
    try:
        height = float(height)
        weight_at_surgery = float(weight_at_surgery)
        weeks_after_surgery = float(weeks_after_surgery)
        current_weight = float(current_weight)
    except:
        print("Some of the values were not castable to the correct datatypes (ints of floats), please check input and try again.")
        success = False
    return success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight

def gather_lab_values():
    success = True
    lab_date = input("Please enter the date of the blood test:\n")
    protein = input("Please enter the protein levels (in g/l):\n")
    B11  = input("Please enter the vitamin B11 levels (in nmol/l):\n")
    B12  = input("Please enter te vitamin B12 levels (in pmol/l):\n")
    D  = input("Please enter the vitamin D levels (in nmol/l):\n")
    iron  = input("Please enter the iron levels (in mmol/l):\n")
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
    water = input("Please ask the patient how much water he drinks per day (in ml):\n")
    water_possibility = True if input("Is the patient able to drink water? (T or F)\n") in ["T", "t"] else False
    supplements_multivitamins = True if input("Does the patient take multivitamins? (T or F)\n") in ["T", "t"] else False
    supplements_B12 = True if input("Does the patient supplement additional B12? (T or F)\n") in ["T", "t"] else False
    protein_intake = input("Enter the daily protein intake of the patient (in grams):\n")
    protein_source = "ANIMAL" if input("What is the patient's main source of protein? (ANIMAL or PLANT)\n") == "ANIMAL" else "PLANT"
    protein_intake_spread = True if input("Is the patient's protein intake spread out over several meals? (T or F)\n") in ["T", "t"] else False
    carb_intake_valuable = True if input("Can the patient's carb intake type be considered valuable? (T or F)\n") in ["T", "t"] else False
    carb_intake_spread = True if input("Is the patient's carb intake spread out over several meals? (T or F)\n") in ["T", "t"] else False
    fat_intake = input("Enter the daily fat intake of the patient (in grams):\n")
    fat_intake_spread = True if input("Is the patient's fat intake spread out over several meals? (T or F)\n") in ["T", "t"] else False
    unsat_fat_intake_sufficient = True if input("Does the patient take in sufficient amounts of unsaturated fat? (T or F)\n") in ["T", "t"] else False
    enough_movement = True if input("Does the patient move at least 5 times per week? T or F)\n") in ["T", "t"] else False
    defecation_freq = input("Per week, how often does the patient defecate?\n")
    right_defecation_consistency = True if input("Does the patient's defecation appear to have the right consistency? (T or F)\n") in ["T", "t"] else False
    eating_moments = input("How often does the patient eat per day?\n")
    divided_food_water = True if input("Does the patient eat and drink separately? (T or F)\n") in ["T", "t"] else False
    slow_intake = True if input("Does the patient take sufficient time to take in food? (T or F)\n") in ["T", "t"] else False
    try:
        water = float(water)
        protein_intake = float(protein_intake)
        fat_intake = float(fat_intake)
        defecation_freq = float(defecation_freq)
        eating_moments = float(eating_moments)
    except:
        print("Some of the values entered could not be casted into floats, please check input and try again.")
        success=False
    return success, water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread, \
            carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake, \
            enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake

def gather_complaints():
    stomach_ache = True if input("Does the patient experience stomach aches? (T or F)\n") in ["T", "t"] else False
    vomiting = True if input("Does the patient vomit frequently? (T or F)\n") in ["T", "t"] else False
    feeling_cold = True if input("Does the patient feel constantly cold? (T or F)\n") in ["T", "t"] else False
    hair_loss = True if input("Has the patient lost considerable hair? (T or F)\n") in ["T", "t"] else False
    dumping = True if input("Does the patient mention problems which hint at gastric dumping syndrome? (T or F)\n") in ["T", "t"] else False
    fatigue = True if input("Does the patient feel continuously tired? (T or F)\n") in ["T", "t"] else False
    nausea = True if input("Does the patient feel dizzy or nauseous frequently? (T or F)\n") in ["T", "t"] else False
    return stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea


def create_advice(patient:Patient):
    general_advice_list = set()
    alarms = set()
    complaint_specific_advice = set()

    #all the rules
    if (patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery < 0.8:
        alarms.add(WEIGHT_LOSS_INSUFFICIENT_ALARM)
    elif (patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery > 1.5:
        alarms.add(WEIGHT_LOSS_HIGH_ALARM)

    if patient.current_weight / (patient.height ** 2) < 27:
        alarms.add(LOW_BMI_ALARM)

    if patient.protein < 60:
        general_advice_list.add(INCREASE_PROTEIN_INTAKE)

    if patient.B11 < 5.9:
        general_advice_list.add(SUPPLEMENT_B11)

    if patient.B12 < 200 and patient.supplements_B12 == False:
        general_advice_list.add(SUPPLEMENT_B12)
    elif patient.B12 < 200 and patient.supplements_B12 == True:
        alarms.add(SPECIALIST_ALARM_B12)

    if patient.D < 20:
        general_advice_list.add(SUPPLEMENT_D)

    if patient.iron < 14 and patient.gender == "MALE":
        general_advice_list.add(SUPPLEMENT_IRON)
    elif patient.iron < 10 and patient.gender == "FEMALE":
        general_advice_list.add(SUPPLEMENT_IRON)

    if  patient.protein_intake < (0.8 * (patient.height ** 2) * 27) and patient.protein_source == "ANIMAL":
        general_advice_list.add(INCREASE_PROTEIN_INTAKE)
    if patient.protein_source == "PLANT":
        general_advice_list.add(INCREASE_FOOD_PROTEIN_AMOUNT)

    if not patient.carb_intake_valuable:
        general_advice_list.add(INCREASE_VALUABLE_CARB_INTAKE)

    if not patient.unsat_fat_intake_sufficient:
        general_advice_list.add(INCREASE_UNSATURATED_FAT_INTAKE)

    #intake spreads
    if not patient.protein_intake_spread:
        general_advice_list.add(SPREAD_PROTEIN_INTAKE)
    if not patient.carb_intake_spread:
        general_advice_list.add(SPREAD_CARB_INTAKE)
    if not patient.fat_intake_spread:
        general_advice_list.add(SPREAD_FAT_INTAKE)

    if not patient.water_possibility:
        alarms.add(WATER_ALARM)

    if not patient.supplements_multivitamins:
        general_advice_list.add(SUPPLEMENT_MULTIVITAMINS)
    if not patient.supplements_B12:
        general_advice_list.add(SUPPLEMENT_B12)

    if not patient.enough_movement:
        general_advice_list.add(MOVE_ENOUGH)

    if patient.defecation_freq < 2:
        alarms.add(INSUFFICIENT_DEFECATION_ALARM)
    elif patient.defecation_freq > 14:
        alarms.add(HIGH_DEFECATION_ALARM)

    if patient.eating_moments < 6:
        general_advice_list.add(EATING_MOMENTS_6_11)
    if not patient.divided_food_water:
        general_advice_list.add(DIVIDE_FOOD_DRINK_INTAKE)
    if not patient.slow_intake:
        general_advice_list.add(SLOW_DOWN_INTAKE)

    #complaints
    if patient.stomach_ache:
        if not patient.slow_intake:
            complaint_specific_advice.add(SLOW_DOWN_INTAKE)
        if patient.eating_moments < 6:
            complaint_specific_advice.add(EATING_MOMENTS_6_11)
        alarms.add(SOURCE_ALARM)

    if patient.nausea:
        if not patient.slow_intake:
            complaint_specific_advice.add(SLOW_DOWN_INTAKE)
        if patient.eating_moments < 6:
            complaint_specific_advice.add(EATING_MOMENTS_6_11)
        if patient.fat_intake > 50:
            complaint_specific_advice.add(LOWER_FAT_INTAKE)
        alarms.add(SOURCE_ALARM)

    if patient.vomiting:
        if not patient.divided_food_water:
            complaint_specific_advice.add(DIVIDE_FOOD_DRINK_INTAKE)
        if not patient.slow_intake:
            complaint_specific_advice.add(SLOW_DOWN_INTAKE) #again, calm=false??
        if patient.eating_moments < 6:
            complaint_specific_advice.add(EATING_MOMENTS_6_11)
        alarms.add(SOURCE_ALARM)

    if patient.feeling_cold == True or patient.fatigue == True:
        if ((patient.weight_at_surgery - patient.current_weight) / patient.weeks_after_surgery) > 1.5:
            complaint_specific_advice.add(INCREASE_INTAKE)
        alarms.add(HEALTH_ALARM)

    if patient.hair_loss:
        if patient.protein < 60:
            complaint_specific_advice.add(INCREASE_PROTEIN_INTAKE)
        if not patient.supplements_multivitamins:
            complaint_specific_advice.add(SUPPLEMENT_MULTIVITAMINS)
        alarms.add(HEALTH_ALARM)

    if patient.dumping:
        if not patient.carb_intake_valuable:
            complaint_specific_advice.add(INCREASE_VALUABLE_CARB_INTAKE)
        alarms.add(HEALTH_ALARM)

    return general_advice_list, alarms, complaint_specific_advice


def display_advice(general_advice, alarms, complaint_specific_advice):
    advice = "\nTHE SYSTEM CONSTRUCTED THE FOLLOWING ADVICE FOR THE PATIENT: " + "\n" \
            + "ALL GENERAL ADVICE BASED ON GIVEN VALUES: " + "\n"
    for general_message in general_advice:
        advice += "- " + general_message + "\n"
    advice += "\nALL ALARMS RAISED DURING THE MEETING: " + "\n"
    for alarm in alarms:
        advice += "- " + alarm + "\n"
    advice += "\nALL COMPLAINT-SPECIFIC ADVICE: " + "\n"
    for complain_advice in complaint_specific_advice:
        advice += "- " + complain_advice + "\n"
    return advice


''' -| START OF PROGRAM |- '''
while True:

    print(WELCOME_STRING)
    success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    while not success:
        success, patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight = gather_general_info()
    else:
        #print("You have entered the following patient information:", patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight, sep="\n")
        patient = Patient(patient_name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight)


    print("\nBefore moving on to the patient-provided information, please enter the lab values.")
    success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    while not success:
        success, lab_date, protein, B11, B12, D, iron = gather_lab_values()
    else:
        #print("You have entered the following lab values:", lab_date, protein, B11, B12, D, iron, sep="\n")
        patient.enter_lab_values(lab_date, protein, B11, B12, D, iron)

        
    print("\nNext, please gather monitoring values of nutritional intake per day from the patient.")
    success, water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread, \
    carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake, \
    enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake \
    = gather_intake_information()
    while not success:
        success, water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread, \
        carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake, \
        enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake \
        = gather_intake_information()
    else:
        #print("You have entered the following intake variables given by the patient: ", water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread,
        #carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake,
        #enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake, sep="\n")

        patient.enter_intake(water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread,
                            carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake,
                            enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake)


    print("\nFinally, enter the complaints the patient mentions, after which all possibilities will be evaluated and advice will be constructed.")
    stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea = gather_complaints()
    while not success:
        stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea = gather_complaints()
    else:
        #print("You have provided us the information that the patient suffers from the following complaints: ", "Stomach ache: "+stomach_ache, "Vomiting: "+vomiting, "Feeling cold: "+feeling_cold, "Hair loss: "+hair_loss, "Dumping: "+dumping, "Fatigue: "+fatigue, "Nausea : "+nausea, sep="\n")
        patient.enter_complaints(stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea)

    general_advice, alarms, complaint_advice = create_advice(patient)
    printable_advice = display_advice(general_advice, alarms, complaint_advice)
    overview = patient.create_overview(printable_advice)
    print(overview)
    print("Overview stored in patientname_overview.txt!")
    print("-" * 30)