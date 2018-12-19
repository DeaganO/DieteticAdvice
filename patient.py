"""
@Author: Deagan Otterspeer
@Contact: d<dot>d<dot>otterspeer<dot>vu<at>gmail<dot>com
@Author: Skip Overgoor
@Contact: skip<at>overgoor<dot>nl

"""


class Patient:
    def __init__(self, name, gender, height, weeks_after_surgery, weight_at_surgery, current_weight):
        self.name = name
        self.gender = gender
        self.height = height
        self.weeks_after_surgery = weeks_after_surgery
        self.weight_at_surgery = weight_at_surgery
        self.current_weight = current_weight

    def enter_lab_values(self, lab_date, protein, B11, B12, D, iron):
        self.lab_date = lab_date
        self.protein = protein
        self.B11 = B11
        self.B12 = B12
        self.D = D
        self.iron = iron

    def enter_complaints(self, stomach_ache, vomiting, feeling_cold, hair_loss, dumping, fatigue, nausea):
        self.stomach_ache = stomach_ache
        self.vomiting = vomiting
        self.feeling_cold = feeling_cold
        self.hair_loss = hair_loss
        self.dumping = dumping
        self.fatigue = fatigue
        self.nausea = nausea

    def enter_intake(self, water, water_possibility, supplements_B12, protein_intake, protein_source, protein_intake_spread,
                     carb_intake_valuable, carb_intake_spread, unsat_fat_intake_sufficient, fat_intake_spread, supplements_multivitamins, fat_intake,
                     enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake):

        #per day or week or generally
        self.water = water
        self.water_possibility = water_possibility
        self.supplements_B12 = supplements_B12
        self.protein_intake = protein_intake
        self.protein_source = protein_source
        self.protein_intake_spread = protein_intake_spread
        self.carb_intake_valuable = carb_intake_valuable
        self.carb_intake_spread = carb_intake_spread
        self.unsat_fat_intake_sufficient = unsat_fat_intake_sufficient
        self.fat_intake_spread = fat_intake_spread
        self.supplements_multivitamins = supplements_multivitamins
        self.fat_intake = fat_intake
        self.enough_movement = enough_movement
        self.defecation_freq = defecation_freq
        self.right_defecation_consistency = right_defecation_consistency
        self.eating_moments = eating_moments
        self.divided_food_water = divided_food_water
        self.slow_intake = slow_intake

    def create_overview(self, advice):
        general_info = "OVERVIEW OF DIETICIAN MEETING\n" \
                    + "GENERAL PATIENT INFORMATION:\n" \
                    + "- Name: " + self.name + ", " + self.gender + ", height: " + str(self.height) + "\n" \
                    + "- Weeks since surgery: " + str(self.weeks_after_surgery) + "\n" \
                    + "- Weight at surgery: " + str(self.weight_at_surgery) + ", current weight: " + str(self.current_weight) + "\n"

        lab_values = "\nLAB VALUES OF " + self.lab_date + ":\n" \
                    + "- Protein (g/L): " + str(self.protein) + "\n" \
                    + "- Vitamin B11 (nmol/L): " + str(self.B11) + "\n" \
                    + "- Vitamin B12 (pmol/L): " + str(self.B12) + "\n" \
                    + "- Vitamin D (nmol/L): " + str(self.D) + "\n" \
                    + "- Iron (mmol/L): " + str(self.iron) + "\n"

        intake_info = "\nINTAKE OR MEETING VARIABLES GIVEN BY THE PATIENT: " + "\n" \
                    + "- Water p/d (ml): " + str(self.water) + ", able to drink: " + str(self.water_possibility) + "\n" \
                    + "- Supplements multivitamins: " + str(self.supplements_multivitamins) + ", supplements extra B12: " + str(self.supplements_B12) + "\n" \
                    + "- Protein intake p/d (g): " + str(self.protein_intake) + ", source: " + self.protein_source + ", spread: " + str(self.protein_intake_spread) + "\n" \
                    + "- Fat intake p/d (g): " + str(self.fat_intake) + ", sufficient unsaturated: " + str(self.unsat_fat_intake_sufficient) + ", spread: " + str(self.fat_intake_spread) + "\n" \
                    + "- Carb intake valuable: " + str(self.carb_intake_valuable) + ", spread: " + str(self.carb_intake_spread) + "\n" \
                    + "- Slow intake: " + str(self.slow_intake) + ", nr eating moments p/d: " + str(self.eating_moments) + ", divided: " + str(self.divided_food_water) + "\n" \
                    + "- Defecation frequency p/w: " + str(self.defecation_freq) + ", right consistency: " + str(self.right_defecation_consistency) + "\n" \
                    + "- Enough movement: " + str(self.enough_movement) + "\n"

        complaints = "\nTHE PATIENT MENTIONS THE FOLLOWING COMPLAINTS: " + "\n" \
                    + "- Stomach ache: " + str(self.stomach_ache) + "\n" \
                    + "- Vomiting: " + str(self.vomiting) + "\n" \
                    + "- Feeling cold: " + str(self.feeling_cold) + ", Fatigue: " + str(self.fatigue) + "\n" \
                    + "- Hair loss: " + str(self.hair_loss) + "\n" \
                    + "- Gastric Dumping Syndrome: " + str(self.dumping) + "\n" \
                    + "- Nausea: " + str(self.nausea) + "\n"

        overview = general_info + lab_values + intake_info + complaints + advice
        with open(self.name+"_overview.txt", "w") as file:
            file.write(overview)

        return overview