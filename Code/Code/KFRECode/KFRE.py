# this file is used to assemble all the data required to calculate the kfre and perform the operation

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

# loading the data
gfr = pd.DataFrame(pd.read_excel('KFRE/gfr.xlsx'))
df = pd.DataFrame(pd.read_excel('CleanData/data.xlsx'))

# loading low level data
data = pd.read_excel("CleanData/data.xlsx")
lowLevelData = pd.DataFrame(data)

# NOTE: 
# Race: 0 --> Caucasian-White, 1 --> Other
kfre = gfr[['pt_id', 'gender', 'race', 'age', '2009_GFR', '2021_GFR']].copy()

# NOTE: Unsure of conversions and units
kfre['acr'] = df['spot_acr']
kfre['bicarb'] = lowLevelData['total_co2']
kfre['alb'] = df['alb']
kfre['calc'] = df['calc']
kfre['phos'] = df['phos']

kfre.to_excel('KFRE/kfre_data.xlsx', index=False, engine='xlsxwriter')
