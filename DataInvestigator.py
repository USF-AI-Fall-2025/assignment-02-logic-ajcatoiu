import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataInvestigator:
    """A helper class for exploring and analyzing a pandas DataFrame."""

    def __init__(self, df: pd.DataFrame):
        """
        Constructor initializes DataInvestigator.

        Args:
            df (pd.DataFrame): the DataFrame being investigated
        """
        self.df = df
        self.col_nums = {}
        key = 0
        for col in df.columns:
            self.col_nums[key] = col
            key += 1

    def baseline(self, col: int) -> int | float:
        """
        Get the most frequent value from a given column.

        Args:
            col (int): the integer index of the column

        Returns:
            int | float: the most frequent value in the column, or None if unavailable
        """
        try:
            values = self.get_values(col)
            most_freq_value = values.value_counts().first_valid_index()
            return most_freq_value
        except:
            return None

    def corr(self, col1: int, col2: int) -> float:
        """
        Compute the correlation between two columns.

        Args:
            col1 (int): the integer index of the first column
            col2 (int): the integer index of the second column

        Returns:
            float: the correlation coefficient between the two columns (-1 to 1), or None if computation fails
        """
        try:
            col1_label = self.col_nums[col1]
            col2_label = self.col_nums[col2]
            correlation = self.df[col1_label].corr(self.df[col2_label])
            return correlation
        except:
            return None

    def zeroR(self, col: int) -> int | float:
        """
        Compute the ZeroR baseline prediction for a column. Simply predicts the most frequent value,
        regardless of other features.

        Args:
            col (int): the integer index of the column

        Returns:
            int | float: the baseline value for the column, or None if unavailable
        """
        try:
            return self.baseline(col)
        except:
            return None
        
    def get_values(self, col: int) -> pd.Series:
        """
        Retrieve the values of a column as a pandas Series.

        Args:
            col (int): the integer index of the column

        Returns:
            pd.Series: a Series containing the column values, or None if not found
        """
        try:
            col_label = self.col_nums[col]
            col_values = self.df[col_label]
            return col_values
        except:
            return None
        
    def get_label_index(self, label: str) -> int:
        """
        Get the integer index of a column given its label.

        Args:
            label (str): the column name

        Returns:
            int: the integer index of the column, or None if not found
        """
        try:
            for index, trait in self.col_nums.items():
                if trait == label:
                    return index
        except:
            return None

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

print(di.baseline(1))
print(di.zeroR(1))