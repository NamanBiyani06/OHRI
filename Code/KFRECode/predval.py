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

# loading data
prediction = pd.DataFrame(pd.read_excel('KFRE/prediction.xlsx'))
validation = pd.DataFrame(pd.read_excel('KFRE/validation.xlsx'))

predval = prediction.copy()

predval[['trans/dialysis', 'death', 'other', 'date']] = validation[['trans/dialysis', 'death', 'other', 'date']].copy()

predval.to_excel('KFRE/predval.xlsx', index=False, engine='xlsxwriter')