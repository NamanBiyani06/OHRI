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
warnings.filterwarnings('ignore')

def calculate_kfre(row):
    gender = row['gender']
    race = row['race']
    age = row['age']
    spot_acr = row['acr']
    
    if gender == 2:
        g_cal = 0.2467 * (-0.5642)
    elif gender == 1:
        g_cal = 0.2467 * (1 - 0.5642)
    
    l_cal = 0.451 * (np.log(spot_acr * 8.84) - 5.137)
    
    kfre_calc = (1.0 - (0.975 ** (np.exp(g_cal + l_cal)))) * 100
    
    return kfre_calc

# loading data
data = pd.read_excel('KFRE/kfre_data.xlsx')
df = pd.DataFrame(data)

df['kfre'] = df.apply(calculate_kfre, axis=1)

df.to_excel('KFRE/kfre_predictions.xlsx', index=False, engine="xlsxwriter")