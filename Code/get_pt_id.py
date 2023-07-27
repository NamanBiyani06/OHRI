# This file is to get the pt_id of any patients that have outlier data. This includes:
# Any patients that have a followup date after todays date
# BMI < 18, BMI > 40
# PTH > 100
# These pt_id's will be outputted to a designated txt file.

# imports
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_datetime64_any_dtype
from datetime import datetime
import numpy as np
import matplotlib as plt
import seaborn as sb # seaborn provides high level functions for creating statistical charts - built on plt
import warnings
warnings.filterwarnings('ignore')

data = pd.read_excel("CleanData/data.xlsx")
df = pd.DataFrame(data)

# loading outliers.txt as the output file, f 
f = open("Output/outliers.txt", "w")

# NOTE: BMI Outliers
outlier_bmi = df[(df['bmi'] < 18) | (df['bmi'] > 40)].index.tolist()
print("BMI Outliers: ", file=f)
print(outlier_bmi.__len__(), "Outlier(s)", file=f)
print(outlier_bmi, file=f)
print("\n", file=f)

# NOTE: PTH Outliers
outlier_pth = df[(df['pth'] > 100)].index.tolist()
print("PTH Outliers: ", file=f)
print(outlier_pth.__len__(), "Outlier(s)", file=f)
print(outlier_pth, file=f)
print("\n", file=f)

# NOTE: Followup Outliers
outlier_fup = df[(df['fup_date'] > datetime.today())].index.tolist() # NOTE: datetime.today() is todays date
print("Followup Outliers: ", file=f)
print(outlier_fup.__len__(), "Outlier(s)", file=f)
print(outlier_fup, file=f)
print("\n", file=f)
