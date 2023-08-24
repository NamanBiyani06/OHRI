# this file is used to store the 8 different kidney failure risk equations

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

# ! 4 VARIABLE !

# 2 year, 2009
def kfre_4var_2y_2009(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2009_GFR']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR]):
        return np.nan
    
    if(race == 0): coefficient = 0.9751
    else: coefficient = 0.9832
    
    a = -0.2201 * ((age/10) - 7.036)
    b = 0
    if(male == 1): b = 0.2467 * (1 - 0.5642)
    if(male == 2): b = 0.2467 * (-0.5642)
    c = -0.5567 * ((eGFR/5.0) - 7.222)
    d = 0
    if(ACR > 0): d = 0.4510 * (math.log(ACR) - 5.137)
    else: return np.nan
    return (1.0 - (coefficient ** (math.exp(a + b + c + d)))) * 100

# 2 year, 2021
def kfre_4var_2y_2021(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2021_GFR']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR]):
        return np.nan
    
    if(race == 0): coefficient = 0.9751
    else: coefficient = 0.9832
    
    a = -0.2201 * ((age/10) - 7.036)
    b = 0
    if(male == 1): b = 0.2467 * (1 - 0.5642)
    if(male == 2): b = 0.2467 * (-0.5642)
    c = -0.5567 * ((eGFR/5.0) - 7.222)
    d = 0
    if(ACR > 0): d = 0.4510 * (math.log(ACR) - 5.137)
    else: return np.nan
    return (1.0 - (coefficient ** (math.exp(a + b + c + d)))) * 100

# # 5 year, 2009 13.51 25.90
def kfre_4var_5y_2009(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2009_GFR']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR]):
        return np.nan
    
    if(race == 0): coefficient = 0.924
    else: coefficient = 0.9365
    
    a = -0.2201 * ((age/10) - 7.036)
    b = 0
    if(male == 1): b = 0.2467 * (1 - 0.5642)
    if(male == 2): b = 0.2467 * (-0.5642)
    c = -0.5567 * ((eGFR/5.0) - 7.222)
    d = 0
    if(ACR > 0): d = 0.4510 * (math.log(ACR) - 5.137)
    else: return np.nan
    return (1.0 - (coefficient ** (math.exp(a + b + c + d)))) * 100

# # 5 year, 2021
def kfre_4var_5y_2021(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2021_GFR']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR]):
        return np.nan
    
    if(race == 0): coefficient = 0.924
    else: coefficient = 0.9365
    
    a = -0.2201 * ((age/10) - 7.036)
    b = 0
    if(male == 1): b = 0.2467 * (1 - 0.5642)
    if(male == 2): b = 0.2467 * (-0.5642)
    c = -0.5567 * ((eGFR/5.0) - 7.222)
    d = 0
    if(ACR > 0): d = 0.4510 * (math.log(ACR) - 5.137)
    else: return np.nan
    return (1.0 - (coefficient ** (math.exp(a + b + c + d)))) * 100

# # ! 8 VARIABLE !

# 2 year, 2009
def kfre_8var_2y_2009(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2009_GFR']
    alb = row['alb']
    phos = row['phos']
    bicarb = row['bicarb']
    calc = row['calc']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR, alb, phos, bicarb, calc]):
        return np.nan
    
    if(race == 0): coefficient = 0.978
    else: coefficient = 0.9827

    a = 0
    if(male == 1): a = 0.1602 * (1 - 0.5642)
    if(male == 2): a = 0.1602 * (-0.5642)
    b = -0.1992 * ((age/10) - 7.036)
    c = -0.4919 * ((eGFR/5) - 7.222)
    d = 0
    if(ACR > 0): d = 0.3364 * (math.log(ACR) - 5.137)
    e = -0.3441 * ((alb / 10.0) - 3.997)
    f = 0.2604 * ((phos * 3.1) - 3.916)
    g = -0.07354 * (bicarb - 25.57)
    h = -0.2228 * ((calc / 0.2495) - 9.355)
    return (1.0 - (coefficient ** (math.exp(a + b + c + d + e + f + g + h)))) * 100

# 2 year, 2021
def kfre_8var_2y_2021(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2021_GFR']
    alb = row['alb']
    phos = row['phos']
    bicarb = row['bicarb']
    calc = row['calc']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR, alb, phos, bicarb, calc]):
        return np.nan
    
    if(race == 0): coefficient = 0.978
    else: coefficient = 0.9827

    a = 0
    if(male == 1): a = 0.1602 * (1 - 0.5642)
    if(male == 2): a = 0.1602 * (-0.5642)
    b = -0.1992 * ((age/10) - 7.036)
    c = -0.4919 * ((eGFR/5) - 7.222)
    d = 0
    if(ACR > 0): d = 0.3364 * (math.log(ACR) - 5.137)
    e = -0.3441 * ((alb / 10.0) - 3.997)
    f = 0.2604 * ((phos * 3.1) - 3.916)
    g = -0.07354 * (bicarb - 25.57)
    h = -0.2228 * ((calc / 0.2495) - 9.355)
    return (1.0 - (coefficient ** (math.exp(a + b + c + d + e + f + g + h)))) * 100

# 5 year, 2009
def kfre_8var_5y_2009(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2009_GFR']
    alb = row['alb']
    phos = row['phos']
    bicarb = row['bicarb']
    calc = row['calc']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR, alb, phos, bicarb, calc]):
        return np.nan
    
    if(race == 0): coefficient = 0.9301
    else: coefficient = 0.9245

    a = 0
    if(male == 1): a = 0.1602 * (1 - 0.5642)
    if(male == 2): a = 0.1602 * (-0.5642)
    b = -0.1992 * ((age/10) - 7.036)
    c = -0.4919 * ((eGFR/5) - 7.222)
    d = 0
    if(ACR > 0): d = 0.3364 * (math.log(ACR) - 5.137)
    e = -0.3441 * ((alb / 10.0) - 3.997)
    f = 0.2604 * ((phos * 3.1) - 3.916)
    g = -0.07354 * (bicarb - 25.57)
    h = -0.2228 * ((calc / 0.2495) - 9.355)
    return (1.0 - (coefficient ** (math.exp(a + b + c + d + e + f + g + h)))) * 100

# 5 year, 2021
def kfre_8var_5y_2021(row):
    male = row['gender']
    race = row['race']
    age = row['age']
    ACR = row['acr']
    eGFR = row['2021_GFR']
    alb = row['alb']
    phos = row['phos']
    bicarb = row['bicarb']
    calc = row['calc']
    
    if any(pd.isna(val) for val in [male, race, age, ACR, eGFR, alb, phos, bicarb, calc]):
        return np.nan
    
    if(race == 0): coefficient = 0.9301
    else: coefficient = 0.9245

    a = 0
    if(male == 1): a = 0.1602 * (1 - 0.5642)
    if(male == 2): a = 0.1602 * (-0.5642)
    b = -0.1992 * ((age/10) - 7.036)
    c = -0.4919 * ((eGFR/5) - 7.222)
    d = 0
    if(ACR > 0): d = 0.3364 * (math.log(ACR) - 5.137)
    e = -0.3441 * ((alb / 10.0) - 3.997)
    f = 0.2604 * ((phos * 3.1) - 3.916)
    g = -0.07354 * (bicarb - 25.57)
    h = -0.2228 * ((calc / 0.2495) - 9.355)
    return (1.0 - (coefficient ** (math.exp(a + b + c + d + e + f + g + h)))) * 100
