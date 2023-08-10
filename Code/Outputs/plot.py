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

# Create separate DataFrames for each patient outcome category
trans_dialysis_df = df[df['trans/dialysis'] == 1]
death_df = df[df['death'] == 1]
other_df = df[df['other'] == 1]

# Create box plots using Plotly Express for each patient outcome category with different colors
fig_trans_dialysis = go.Figure()
fig_trans_dialysis.add_trace(go.Box(x=trans_dialysis_df['5yr_kfre_2009'], name='Trans/Dialysis', marker_color='blue'))

fig_death = go.Figure()
fig_death.add_trace(go.Box(x=death_df['5yr_kfre_2009'], name='Death', marker_color='red'))

fig_other = go.Figure()
fig_other.add_trace(go.Box(x=other_df['5yr_kfre_2009'], name='Other', marker_color='green'))

# Combine the plots using subplots
fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                    subplot_titles=("Trans/Dialysis", "Death", "Other"))

fig.add_trace(fig_trans_dialysis.data[0], row=1, col=1)
fig.add_trace(fig_death.data[0], row=2, col=1)
fig.add_trace(fig_other.data[0], row=3, col=1)

# Update layout
fig.update_layout(title_text="Distribution of 5-year 2009 KFRE Predictions by Patient Outcome",
                  xaxis_title="",
                  showlegend=False,
                  title_font=dict(size=18),
                  title_x=0.5, title_xanchor='center',
                  xaxis_title_font=dict(size=16),
                  xaxis=dict(showline=True, showgrid=False, zeroline=False),
                  yaxis_title_font=dict(size=16))

# Add x-axis title at the bottom of the page
fig.add_annotation(text="2-Year KFRE Prediction", xref="paper", yref="paper",
                   x=0.5, y=-0.15, showarrow=False, font=dict(size=16))

fig.show()