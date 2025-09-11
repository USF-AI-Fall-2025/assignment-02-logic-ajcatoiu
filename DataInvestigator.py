import pandas as pd
import numpy as np

class DataInvestigator:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.col_nums = {}
        key = 0
        for col in df.columns:
            self.col_nums[key] = col
            key += 1

    def baseline(self, col: int):
        if col not in self.col_nums:
            return None
        col_label = self.col_nums[col]
        col_values = self.df[col_label]
        most_freq_value = col_values.value_counts().first_valid_index()
        return most_freq_value

    def corr(self, col1: int, col2: int):
        pass

    def zeroR(self, col: int):
        pass

df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)
print(di.baseline(80))