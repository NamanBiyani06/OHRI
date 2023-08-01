# this is a file for merging excel files onto the central file: demo.xlsx
# imports
import pandas as pd # pandas for data processing and cleaning
import numpy as np # numpy (unused)
import openpyxl # openpyxl is used as a secondary export engine
import re # regex expressions
import xlsxwriter # xlsxwriter is used as an export engine

# loading the datasets
demo = pd.read_excel("CleanData/Demo.xlsx")
lab = pd.read_excel("CleanData/Lab_i.xlsx")
measurements = pd.read_excel("CleanData/Measurements.xlsx")
meds = pd.read_excel("CleanData/Meds_i.xlsx")
hist = pd.read_excel("CleanData/PR_hist.xlsx")
status = pd.read_excel("CleanData/status.xlsx")

# This can be uncommented in order to view all the columns in the data no matter the data size when the df is printed (unneeded)
# pd.set_option('display.max_columns', None)

# creating the base dataframe which will be added onto with other dfs
data = pd.DataFrame(demo)

# merging the datasets onto demo using the primary key --> pt_id
# withheld status data as it requires further cleaning
data = pd.merge(data, lab, on='pt_id')
data = pd.merge(data, measurements, on='pt_id')
data = pd.merge(data, meds, on='pt_id')
data = pd.merge(data, hist, on='pt_id')

# cleaning status.xlsx in preparation to merge in with the main dataset
status = pd.DataFrame(status)
# drops the duplicates from the primary key subset
# keep parameter specifies to keep the last entry of each duplicate
clean_status = status.drop_duplicates(subset='pt_id', keep="last", inplace=False)
# cleaning up the indexing on the dropped duplicates
clean_status.reset_index(drop=True, inplace=True)

data = pd.merge(data, clean_status, on='pt_id')

# dropping the column 'Unnamed: 0' from the dataset
# NOTE: this is not required anymore because of fixes in data IO
# data.drop(data.filter(regex="Uname"), axis=1, inplace=True)

# modifying the data to correct dtypes
# NOTE: this function should be checked to see if it correctly formats the objects
data['dob'] = pd.to_datetime(data["dob"])
data['firstpri_date'] = pd.to_datetime(data['firstpri_date'])
data['race'] = data['race'].replace('-- Select One --', 'Unknown')

# NOTE: xlsxwriter is used as the export engine in order to avoid the illegal characters in the dataset
# NOTE: set index to false to prevent creating an unnamed column
data.to_excel("CleanData/data.xlsx", index=False, engine="xlsxwriter")

print(data.head())