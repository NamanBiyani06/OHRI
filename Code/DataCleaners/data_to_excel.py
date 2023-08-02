# this file is used to calculate statistics on the compiled datasets prepared in convert.py --> merge.py
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

# filling the df 'exel' in preparation for export
def fill_excel():
    shape = df.shape[0]
    nulls = df[column].isna().sum()
    
    if is_bool_dtype(df[column]):
        excel.at[0, column] = 'boolean'

        excel.at[13, column] = df[column].values.sum()
        excel.at[14, column] = (shape - nulls) - df[column].values.sum()
        excel.at[15, column] = (df[column].mean() * 100).round(1)
        excel.at[16, column] = ((1 - df[column].mean()) * 100).round(1)
          
    elif is_numeric_dtype(df[column]):
        # calculating the IQR of pandas column
        quartiles = df[column].quantile([0.25, 0.75])
        iqr = quartiles[0.75] - quartiles[0.25]
    
        excel.at[0, column] = 'numeric64'
        excel.at[1, column] = shape - nulls
        excel.at[2, column] = nulls
        excel.at[3, column] = (((shape - nulls)/shape ) * 100).round(1)
        excel.at[4, column] = round( df[column].mean(), 3)
        excel.at[5, column] = round(df[column].median(), 3)
        excel.at[6, column] = round(df[column].mode().values[0], 3)
        excel.at[7, column] = round(df[column].max() - df[column].min(), 3)
        excel.at[8, column] = quartiles[0.25].round(3)
        excel.at[9, column] = quartiles[0.75].round(3)
        excel.at[10, column] = iqr.round(3)
        excel.at[11, column] = round(df[column].std(), 3)
        excel.at[12, column] = round(df[column].var(), 3)

# importing the data and inserting it into a dataframe
data = pd.read_excel("CleanData/data.xlsx")
df = pd.DataFrame(data)

# the df that will be exported
excel = pd.DataFrame()

stats = ['Dtype',
         'Values',
         'Null',
         'Values%',
         'Mean',
         'Median',
         'Mode',
         'Range',
         '25%',
         '75%',
         'IQR',
         'Std',
         'Var',
         'True',
         'False',
         'True%',
         'False%']

excel['Statistics'] = stats

numerics = []
bools = []
columns = []

# categorizing columns into sorted pyLists
for col in data.columns:
    if is_bool_dtype(df[col]) and df.shape[0] - df[col].isna().sum() != 0:
        bools.append(col)
    elif is_numeric_dtype(df[col]) and df.shape[0] - df[col].isna().sum() != 0:
        numerics.append(col)
print(numerics)
print()
print(bools)
print()

columns = numerics + bools

print(columns)

# data cleaning
for column in columns:
    if df.shape[0] - df[column].isna().sum() != 0:
        excel[column] = np.nan

# for column in df:
#     if ~is_bool_dtype(df[column]) & is_numeric_dtype(df[column]):
#         if df.shape[0] - df[column].isna().sum() != 0:
#             excel[column] = np.nan

# for column in df:
#     if is_bool_dtype(df[column]) & ~is_numeric_dtype(df[column]):
#         if df.shape[0] - df[column].isna().sum() != 0:
#             excel[column] = np.nan

# data filling
for column in excel:
    if column != 'Statistics':
        fill_excel()
    else: pass
    
print(excel.head(15))

# data export
excel.to_excel("Output/data_stats_new.xlsx", index=False, engine="xlsxwriter")

