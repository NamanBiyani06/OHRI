# This file is used to clean the data after it has already been heavily parsed. It completes a few different tasks which will be indicated by comments.

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
# warnings.filterwarnings('ignore')

# importing the data and inserting it into a dataframe
data = pd.read_excel("CleanData/data.xlsx")
df = pd.DataFrame(data)

# NOTE: Removing all PRI dates that are before 2010 (this is when the data starts to become more reliable)
filter_date = datetime.datetime(2010, 1, 1)

df_filtered = df[df['firstpri_date'] > filter_date]

# NOTE: Treating cs_pt_alive as a boolean value instead of integer --> 0 = Dead, 1 = Alive
df_filtered['cs_pt_alive'] = df['cs_pt_alive'].astype(bool)

# NOTE: Creating a new column that is the difference between the firstpri_date and the age. 
# This is calculated by subtracting the dob from the firstpri_date
# Age is measured in years, as an integer
df_filtered['age'] = df_filtered['firstpri_date'].dt.year - df_filtered['dob'].dt.year

# outputting the data to an excel file
df_filtered.to_excel("CleanData/data.xlsx", index=False)