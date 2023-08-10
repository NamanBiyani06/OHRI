# NOTE: ARCHIVE
# this file will be used in order to create custom plots using plotly for correlation checking

# imports
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_datetime64_any_dtype
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # seaborn provides high level functions for creating statistical charts - built on plt
import warnings
import xlsxwriter
import math
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
warnings.filterwarnings('ignore')

# Assuming df_outcomes is your DataFrame containing patient outcomes
df_outcomes = pd.read_excel('KFRE/validation.xlsx')

# Assuming df_kfre is your DataFrame containing KFRE data
df_kfre = pd.read_excel('KFRE/prediction.xlsx')

# Merge the DataFrames based on a common identifier, e.g., patient ID
df = pd.merge(df_outcomes, df_kfre, on='pt_id', how='inner')

df['trans/dialysis'] = df['trans/dialysis'].replace(1, 'trans/dialysis')
df['trans/dialysis'] = df['trans/dialysis'].replace(0, np.nan)

df['death'] = df['death'].replace(1, 'death')
df['death'] = df['death'].replace(0, np.nan)

df['other'] = df['other'].replace(1, 'other')
df['other'] = df['other'].replace(0, np.nan)

df['outcome'] = df['trans/dialysis'].fillna('') + df['death'].fillna('') + df['other'].fillna('')

# # Create a scatter matrix (pair plot) using Plotly Express
# fig = px.scatter_matrix(df, dimensions=['2yr_kfre_2009', '2yr_kfre_2021', '5yr_kfre_2009', '5yr_kfre_2021'],
#                          title='Scatter Matrix of Four KFREs')


# # Create a scatter plot matrix using Plotly Express
# fig = px.scatter_matrix(df, dimensions=['2yr_kfre_2009', '2yr_kfre_2021', '5yr_kfre_2009', '5yr_kfre_2021'], color='outcome',
#                          title='Scatter Plot Matrix with Categorical Outcome', opacity=0.6)

fig = px.scatter(df, x='2yr_kfre_2009', y='2yr_kfre_2021', color='outcome', title='Scatter')

fig.show()