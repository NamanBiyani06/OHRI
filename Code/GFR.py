# This file is used to create a new dataframe called kfre_data that will hold all the data required to calculate a kfre for a patient
# this df is a higher priority level over data.xlsx and will be considered high level

# imports
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_datetime64_any_dtype
import datetime
import numpy as np
import matplotlib as plt
import seaborn as sb # seaborn provides high level functions for creating statistical charts - built on plt
import warnings
warnings.filterwarnings('ignore')

# functions

# NOTE: The code is still unsure of whether '1' is 'caucasian-white' or 'other'

# Define the CKD-EPI Creatinine GFR 2009 formula function
def calculate_gfr_2009(row):
    if row['race'] == 1 and row['gender'] == 2 and row['creat'] <= 0.7:
        return 166 * (row['creat'] / 0.7) ** -0.329 * (0.993) ** row['age']
    elif row['race'] == 1 and row['gender'] == 2 and row['creat'] > 0.7:
        return 166 * (row['creat'] / 0.7) ** -1.209 * (0.993) ** row['age']
    elif row['race'] == 1 and row['gender'] == 1 and row['creat'] <= 0.9:
        return 163 * (row['creat'] / 0.9) ** -0.411 * (0.993) ** row['age']
    elif row['race'] == 1 and row['gender'] == 1 and row['creat'] > 0.9:
        return 163 * (row['creat'] / 0.9) ** -1.209 * (0.993) ** row['age']
    elif row['race'] == 0 and row['gender'] == 2 and row['creat'] <= 0.7:
        return 144 * (row['creat'] / 0.7) ** -0.329 * (0.993) ** row['age']
    elif row['race'] == 0 and row['gender'] == 2 and row['creat'] > 0.7:
        return 144 * (row['creat'] / 0.7) ** -1.209 * (0.993) ** row['age']
    elif row['race'] == 0 and row['gender'] == 1 and row['creat'] <= 0.9:
        return 141 * (row['creat'] / 0.9) ** -0.411 * (0.993) ** row['age']
    elif row['race'] == 0 and row['gender'] == 1 and row['creat'] > 0.9:
        return 141 * (row['creat'] / 0.9) ** -1.209 * (0.993) ** row['age']
    else:
        return None  # Return None if the conditions are not met

# Define the CKD-EPI Creatinine GFR 2021 formula function
def calculate_gfr_2021(row):
    if row['gender'] == 2 and row['creat'] <= 0.7:
        return 143 * (row['creat'] / 0.7) ** -0.241 * (0.9938) ** row['age']
    elif row['gender'] == 2 and row['creat'] > 0.7:
        return 143 * (row['creat'] / 0.7) ** -1.2 * (0.9938) ** row['age']
    elif row['gender'] == 1 and row['creat'] <= 0.9:
        return 142 * (row['creat'] / 0.9) ** -0.302 * (0.9938) ** row['age']
    elif row['gender'] == 1 and row['creat'] > 0.9:
        return 142 * (row['creat'] / 0.9) ** -1.2 * (0.9938) ** row['age']
    else:
        return None  # Return None if the conditions are not met

# loading low level data
data = pd.read_excel("CleanData\data.xlsx")
lowLevelData = pd.DataFrame(data)

# creating a high level df
gfr = lowLevelData[['pt_id', 'gender', 'race', 'age', 'creat']].copy()

# adding 2009 and 2021 GFR Columns to high level
gfr[['2009_GFR', '2021_GFR']] = np.nan

# changing all gender values to bool
# NOTE: 0 --> Female, 1 --> Male
gfr.gender[data['gender'] == 'Female'] = 2
gfr.gender[data['gender'] == 'Male'] = 1

# Use 'replace' to map 'Caucasian-White' to 0 and any other value to 1 in the 'race' column
gfr['race'] = gfr['race'].replace('Caucasian-White', 0).replace({pd.NA: 1, None: 1})

# Use 'apply' with a lambda function to map non-zero values to 1 in the 'race' column
gfr['race'] = gfr['race'].apply(lambda x: 1 if x != 0 else x)

# changing all the creatinine from umol/L --> mg/dL (metric to imperial)
gfr['creat'] = gfr['creat'] / 88.42

# Apply the formula to calculate the GFR and update the '2009_GFR' column with the calculated values
gfr['2009_GFR'] = gfr.apply(calculate_gfr_2009, axis=1)

# Apply 2021 formula and update the 2009_GFR
gfr['2021_GFR'] = gfr.apply(calculate_gfr_2021, axis=1)

gfr.to_excel('KFRE/gfr.xlsx', index=False, engine="xlsxwriter")
