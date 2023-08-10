# this file will be used to calculate the prediction percent of kidney failure using the kidney failure risk equation provided by the OHRI

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
import xlsxwriter
import math
warnings.filterwarnings('ignore')

def calculate_kfre_2021(row, years):
    gender = row['gender']
    race = row['race']
    age = row['age']
    spot_acr = row['acr']
    egfr_cal = row['2021_GFR']
    
    e_cal = -0.2201 * ((age / 10.0) - 7.036)
    
    g_cal = 0
    
    if gender == "Female":
        g_cal = 0.2467 * (-0.5642)
    elif gender == "Male":
        g_cal = 0.2467 * (1 - 0.5642)
    
    m_cal = -0.5567 * ((egfr_cal / 5.0) - 7.2222)
    
    l_cal = 0.451 * (np.log(spot_acr * 8.84) - 5.137)
    
    if years == 2:
        kfre_calc = (1.0 - (0.975 ** (math.exp(e_cal + g_cal + m_cal + l_cal)))) * 100
    elif years == 5:
        kfre_calc = (1.0 - (0.9240 ** (math.exp(e_cal + g_cal + m_cal + l_cal)))) * 100

    return kfre_calc

def calculate_kfre_2009(row, years):
    gender = row['gender']
    race = row['race']
    age = row['age']
    spot_acr = row['acr']
    egfr_cal = row['2009_GFR']
    
    e_cal = -0.2201 * ((age / 10.0) - 7.036)
    
    g_cal = 0
    
    if gender == "Female":
        g_cal = 0.2467 * (-0.5642)
    elif gender == "Male":
        g_cal = 0.2467 * (1 - 0.5642)
    
    m_cal = -0.5567 * ((egfr_cal / 5.0) - 7.2222)
    
    l_cal = 0.451 * (np.log(spot_acr * 8.84) - 5.137)
    
    if years == 2:
        kfre_calc = (1.0 - (0.975 ** (math.exp(e_cal + g_cal + m_cal + l_cal)))) * 100
    elif years == 5:
        kfre_calc = (1.0 - (0.9240 ** (math.exp(e_cal + g_cal + m_cal + l_cal)))) * 100   
         
    return kfre_calc

# loading data
data = pd.read_excel('KFRE/kfre_data.xlsx')
df = pd.DataFrame(data)

df['2yr_kfre_2009'] = df.apply(calculate_kfre_2009, axis=1, args=(2,))
df['2yr_kfre_2021'] = df.apply(calculate_kfre_2021, axis=1, args=(2,))
df['5yr_kfre_2009'] = df.apply(calculate_kfre_2009, axis=1, args=(5,))
df['5yr_kfre_2021'] = df.apply(calculate_kfre_2021, axis=1, args=(5,))

df.to_excel('KFRE/prediction.xlsx', index=False, engine="xlsxwriter")