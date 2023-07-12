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

# importing the data and inserting it into a dataframe
data = pd.read_excel("CleanData\data.xlsx")
df = pd.DataFrame(data)

# clearing the file before performing the script
with open("Output\output.txt", "a") as f: f.truncate(0)

# simple formatting function
def space():
    print("", file=f)
    
# stats functions prints useful information to an output.txt file
def continuous_stats():
    shape = df.shape[0]
    nulls = df[column].isna().sum()
    print("Values: ", (((shape - nulls)/shape) * 100).round(1).astype(str) + '%, ', shape - nulls, " Values, ", nulls, " Null Values", file=f, sep="")
    print("Mean:", df[column].mean().round(3), file=f)
    print("Median:", df[column].median().round(3), file=f)
    print("Mode:", df[column].mode()[0].round(3), file=f)
    print("Range:", (df[column].max() - df[column].min()).round(3), file=f)

    # calculating the IQR of pandas column
    quartiles = df[column].quantile([0.25, 0.75])
    iqr = quartiles[0.75] - quartiles[0.25]

    print("25%:", quartiles[0.25].round(3), file=f)
    print("75%:", quartiles[0.75].round(3), file=f)
    print("IQR:", iqr.round(3), file=f)

def bool_stats():
    shape = df.shape[0]
    nulls = df[column].isna().sum()
    print("Values: ", (((shape - nulls)/shape) * 100).round(1).astype(str) + '%, ', shape - nulls, " Values, ", nulls, " Null Values", file=f, sep="")
    print("True: ", (df[column].mean() * 100).round(1).astype(str) + '%, ', df[column].values.sum(), " Values", file=f, sep="")
    print("False: ", ((1 - df[column].mean()) * 100).round(1).astype(str) + '%, ', (shape - nulls) - df[column].values.sum(), " Values", file=f, sep="")
    
def date_stats():
    min = df[column].min()
    max = df[column].max()
    diff = (max - min).days
    print("Earliest Entry: ", min, file=f, sep="")
    print("Latest Entry: ", max, file=f, sep="")
    print("Entry Range: ", diff, " Days", file=f, sep="")
    
def gender_stats():
    freq = df.gender.str.split(expand=True).stack().value_counts()
    male = freq.to_string(index=False)[0:4]
    female = freq.to_string(index=False)[5:10]
    nulls = df[column].isna().sum()
    print("Male: ", male, file=f, sep="")
    print("Female: ", female, file=f, sep="")
    print("Null: ", nulls, file=f, sep="")
    print("Percent: ", ((int(male)/(int(male) + int(female) + nulls)) * 100).round(1).astype(str) + '% Male, ', ((int(female)/(int(male) + int(female) + nulls)) * 100).round(1).astype(str) + f'% Female', file=f, sep="")
    
def race_stats():
    freq = df.race.str.split(expand=True).stack().value_counts()
    print("Frequency", file=f)
    print(freq.to_string(), file=f)
    freq_percent = df.race.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
    print("Frequency Percentages", file=f)
    print(freq_percent, file=f)

with open('Output\output.txt', 'a') as f:
    for column in df:
        print("Name:", column, file=f)
        print("Datatype: ", df[column].dtype, file=f)
        if df.shape[0] - df[column].isna().sum() == 0:
            print("This column has no values!", file=f)
        else:
            if(is_bool_dtype(df[column])):
                bool_stats()
            elif(is_datetime64_any_dtype(df[column])):
                date_stats()
            elif(is_numeric_dtype(df[column])):
                continuous_stats()
            elif(column == 'gender'):
                gender_stats()
            elif(column == 'race'):
                race_stats()
        space()
                
