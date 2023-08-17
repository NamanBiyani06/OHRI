# this file will be used in order to create 4 different validation datasets, which will be different based on the data that they exclude

# The datasets will be classified as:
# 2 year, 4 variable
# 5 year, 4 variable
# 2 year. 8 variable
# 5 year, 8 variable

# imports
import pandas as pd
import numpy as np
from xlsxwriter import *
from datetime import datetime

# loading data
validation_data = pd.read_excel('KFRE/validation.xlsx')
validation = pd.DataFrame(validation_data)

validation['date_difference'] = validation['date'] - validation['firstpri_date']
validation['date_difference'] = validation['date_difference'].dt.days

validation['excluded'] = False
validation['exclusion_premise'] = ''

two_yr_four_var = validation.copy()
five_yr_four_var = validation.copy()
two_yr_eight_var = validation.copy()
five_yr_eight_var = validation.copy()

exclude_condition = (two_yr_four_var['date_difference'] <= 730)
two_yr_four_var.loc[exclude_condition, 'excluded'] = True
two_yr_four_var.loc[exclude_condition, 'exclusion_premise'] = 'Tracked less than 2 years'

print(two_yr_four_var.head(15))
# export to validation folder
