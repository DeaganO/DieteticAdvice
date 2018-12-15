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

    def enter_intake(self, water, water_possibility, enough_movement, defecation_freq, right_defecation_consistency, eating_moments, divided_food_water, slow_intake):
        #per day
        self.water = water
        self.water_possibility = water_possibility
        self.enough_movement = enough_movement
        self.defecation_freq = defecation_freq
        self.right_defecation_consistency = right_defecation_consistency
        self.eating_moments = eating_moments
        self.divided_intake = divided_food_water
        self.slow_intake = slow_intake

    def give_advice(self):
        print()
        #store advice in db along with patient and meeting information