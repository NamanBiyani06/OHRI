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
from pandas.plotting import table
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

# loading data  
data = pd.read_excel('KFRE/prediction.xlsx')
df = pd.DataFrame(data)

# doing basic statistics on the KFRE columns using pandas describe function
print(df['2yr_kfre_2009'].describe())
print(df['5yr_kfre_2009'].describe())
print(df['2yr_kfre_2021'].describe())
print(df['5yr_kfre_2021'].describe())

