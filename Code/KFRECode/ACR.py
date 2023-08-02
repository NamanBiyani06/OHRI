# this file is to calculate the alb-creat ratio (ACR)

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

# loading the data
gfr = pd.DataFrame(pd.read_excel('KFRE\gfr.xlsx', index_col=False))
df = pd.DataFrame(pd.read_excel('CleanData\data.xlsx', index_col=False))

acr = df[['pt_id', 'alb']].copy()
acr['creat'] = gfr['creat'].copy()

acr.set_index('pt_id', inplace=True)

# print(acr.head(50))
