import pandas as pd

class DataInvestigator:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.col_nums = {}
        key = 0
        for col in df.columns:
            self.col_nums[key] = col
            key += 1

    def baseline(self, col: int) -> int | float:
        try:
            values = self.get_values(col)
            most_freq_value = values.value_counts().first_valid_index()
            return most_freq_value
        except:
            return None

    def corr(self, col1: int, col2: int) -> float:
        try:
            col1_label = self.col_nums[col1]
            col2_label = self.col_nums[col2]
            correlation = self.df[col1_label].corr(self.df[col2_label])
            return correlation
        except:
            return None

    def zeroR(self, col: int) -> int | float:
        try:
            return self.baseline(col)
        except:
            return None
        
    def get_values(self, col: int) -> pd.Series:
        try:
            col_label = self.col_nums[col]
            col_values = self.df[col_label]
            return col_values
        except:
            return None
        
    def get_label_index(self, label: str) -> int:
        try:
            for index, trait in self.col_nums.items():
                if trait == label:
                    return index
        except:
            return None
        

# height, weight, lean mass (lm), muscle mass (mm), visceral muscle area (vma), bone mass, visceral fat rating, protein content %
# body fat % (tfc, tbfr, obesity %)

df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)

gender = di.get_label_index("Gender")

height = di.get_label_index("Height")
weight = di.get_label_index("Weight")
lean_mass = di.get_label_index("Lean Mass (LM) (%)")
muscle_mass = di.get_label_index("Muscle Mass (MM)")
visceral_muscle_area = di.get_label_index("Visceral Muscle Area (VMA) (Kg)")

tfc = di.get_label_index("Total Fat Content (TFC)")
tbfr = di.get_label_index("Total Body Fat Ratio (TBFR) (%)")
obesity = di.get_label_index("Obesity (%)")

print("Height: ", di.corr(gender, height))
print("Weight: ", di.corr(gender, weight))
print("Lean Mass (LM) (%): ", di.corr(gender, lean_mass))
print("Muscle Mass (MM): ", di.corr(gender, muscle_mass))
print("Visceral Muscle Area (VMA) (Kg): ", di.corr(gender, visceral_muscle_area))
print("Total Fat Content (TFC): ", di.corr(gender, tfc))
print("Total Body Fat Ratio (TBFR) (%): ", di.corr(gender, tbfr))
print("Obesity (%): ", di.corr(gender, obesity))
"""I believe the gender encoded as 0 is male and 1 is female"""