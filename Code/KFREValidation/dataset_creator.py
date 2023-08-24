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
from sklearn.metrics import roc_auc_score

# loading data
validation_data = pd.read_excel('KFRE/validation.xlsx')
validation = pd.DataFrame(validation_data)
kfre_data = pd.read_excel('KFRE/predictions.xlsx')
kfre = pd.DataFrame(kfre_data)

validation = validation.drop(columns=['ohn', 'patransf_where', 'patransf_pri'])

validation['date_difference'] = validation['fup_date'] - validation['firstpri_date']
validation['date_difference'] = validation['date_difference'].dt.days

validation['excluded'] = False
validation['exclusion_premise'] = ''
validation['outcome'] = np.nan

cols = validation.columns.tolist()
print(cols)

validation['fup_date'] = validation['fup_date'].dt.strftime('%b %d, %Y')
validation['date'] = validation['date'].dt.strftime('%b %d, %Y')
validation['dotransf_pri'] = validation['dotransf_pri'].dt.strftime('%b %d, %Y')
validation['firstpri_date'] = validation['firstpri_date'].dt.strftime('%b %d, %Y')
validation['cs_dod'] = validation['cs_dod'].dt.strftime('%b %d, %Y')

two_yr_four_var = validation.copy()
five_yr_four_var = validation.copy()
two_yr_eight_var = validation.copy()
five_yr_eight_var = validation.copy()

two_yr_four_var['kfre_2009'] = kfre['kfre_4var_2y_2009']
five_yr_four_var['kfre_2009'] = kfre['kfre_4var_5y_2009']
two_yr_eight_var['kfre_2009'] = kfre['kfre_8var_2y_2009']
five_yr_eight_var['kfre_2009'] = kfre['kfre_8var_5y_2009']

two_yr_four_var['kfre_2021'] = kfre['kfre_4var_2y_2021']
five_yr_four_var['kfre_2021'] = kfre['kfre_4var_5y_2021']
two_yr_eight_var['kfre_2021'] = kfre['kfre_8var_2y_2021']
five_yr_eight_var['kfre_2021'] = kfre['kfre_8var_5y_2021']

# ! two yr four var
exclude_condition_1 = ((two_yr_four_var['date_difference'] <= 730) & (two_yr_four_var['other'] == 1))
exclude_condition_2 = (two_yr_four_var['kfre_2009'].isnull() | two_yr_four_var['kfre_2021'].isnull())
exclude_condition_3 = (two_yr_four_var['date_difference'] < 0)

two_yr_four_var.loc[exclude_condition_1, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Tracked less than 2 years', np.nan, np.nan]
two_yr_four_var.loc[exclude_condition_2, ['excluded', 'exclusion_premise']] = [True, 'No KFRE Data']
two_yr_four_var.loc[exclude_condition_3, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Negative Dates', np.nan, np.nan]

outcome_condition_1 = ((two_yr_four_var['date_difference'] < 731) & (two_yr_four_var['trans/dialysis'] == 1) & (two_yr_four_var['excluded'] == False))
two_yr_four_var.loc[outcome_condition_1, 'outcome'] = 1

# FIXME: The Issue with this code is that I am allocating a 0 to everything that does not have a 1. This allows for logic holes.
outcome_condition_2 = ((two_yr_four_var['outcome'].isnull()) & (two_yr_four_var['excluded'] == False))
two_yr_four_var.loc[outcome_condition_2, 'outcome'] = 0

# ! two yr eight var
exclude_condition_1 = ((two_yr_eight_var['date_difference'] <= 730) & (two_yr_eight_var['other'] == 1))
exclude_condition_2 = (two_yr_eight_var['kfre_2009'].isnull() | two_yr_eight_var['kfre_2021'].isnull())
exclude_condition_3 = (two_yr_eight_var['date_difference'] < 0)

two_yr_eight_var.loc[exclude_condition_1, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Tracked less than 2 years', np.nan, np.nan]
two_yr_eight_var.loc[exclude_condition_2, ['excluded', 'exclusion_premise']] = [True, 'No KFRE Data']
two_yr_eight_var.loc[exclude_condition_3, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Negative Dates', np.nan, np.nan]

outcome_condition_1 = ((two_yr_eight_var['date_difference'] < 730) & (two_yr_eight_var['trans/dialysis'] == 1) & (two_yr_eight_var['excluded'] == False))
two_yr_eight_var.loc[outcome_condition_1, 'outcome'] = 1

# FIXME: The Issue with this code is that I am allocating a 0 to everything that does not have a 1. This allows for logic holes.
outcome_condition_2 = ((two_yr_eight_var['outcome'].isnull()) & (two_yr_eight_var['excluded'] == False))
two_yr_eight_var.loc[outcome_condition_2, 'outcome'] = 0

# ! five yr four var
exclude_condition_1 = ((five_yr_four_var['date_difference'] <= 1825) & (five_yr_four_var['other'] == 1))
exclude_condition_2 = (five_yr_four_var['kfre_2009'].isnull() | five_yr_four_var['kfre_2021'].isnull())
exclude_condition_3 = (five_yr_four_var['date_difference'] < 0)

five_yr_four_var.loc[exclude_condition_1, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Tracked less than 5 years', np.nan, np.nan]
five_yr_four_var.loc[exclude_condition_2, ['excluded', 'exclusion_premise']] = [True, 'No KFRE Data']
five_yr_four_var.loc[exclude_condition_3, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Negative Dates', np.nan, np.nan]

outcome_condition_1 = ((five_yr_four_var['date_difference'] < 1825) & (five_yr_four_var['trans/dialysis'] == 1) & (five_yr_four_var['excluded'] == False))
five_yr_four_var.loc[outcome_condition_1, 'outcome'] = 1

# FIXME: The Issue with this code is that I am allocating a 0 to everything that does not have a 1. This allows for logic holes.
outcome_condition_2 = ((five_yr_four_var['outcome'].isnull()) & (five_yr_four_var['excluded'] == False))
five_yr_four_var.loc[outcome_condition_2, 'outcome'] = 0

# ! five yr eight var
exclude_condition_1 = ((five_yr_eight_var['date_difference'] <= 1825) & (five_yr_eight_var['other'] == 1))
exclude_condition_2 = (five_yr_eight_var['kfre_2009'].isnull() | five_yr_eight_var['kfre_2021'].isnull())
exclude_condition_3 = (five_yr_eight_var['date_difference'] < 0)

five_yr_eight_var.loc[exclude_condition_1, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Tracked less than 5 years', np.nan, np.nan]
five_yr_eight_var.loc[exclude_condition_2, ['excluded', 'exclusion_premise']] = [True, 'No KFRE Data']
five_yr_eight_var.loc[exclude_condition_3, ['excluded', 'exclusion_premise', 'kfre_2009', 'kfre_2021']] = [True, 'Negative Dates', np.nan, np.nan]

outcome_condition_1 = ((five_yr_eight_var['date_difference'] < 1825) & (five_yr_eight_var['trans/dialysis'] == 1) & (five_yr_eight_var['excluded'] == False))
five_yr_eight_var.loc[outcome_condition_1, 'outcome'] = 1

# FIXME: The Issue with this code is that I am allocating a 0 to everything that does not have a 1. This allows for logic holes.
outcome_condition_2 = ((five_yr_eight_var['outcome'].isnull()) & (five_yr_eight_var['excluded'] == False))
five_yr_eight_var.loc[outcome_condition_2, 'outcome'] = 0


# print(two_yr_four_var.head(15))

# two_yr_four_var = two_yr_four_var.dropna(subset=['outcome', 'kfre_2021'])

# c_statistic = roc_auc_score(two_yr_four_var['outcome'], two_yr_four_var['kfre_2021'])
# print(c_statistic)

# print(two_yr_four_var['kfre_2021'].corr(two_yr_four_var['outcome']))

# export to validation folder
two_yr_four_var.to_excel('Validation/two_yr_four_var.xlsx', index=False ,engine='xlsxwriter')
two_yr_eight_var.to_excel('Validation/two_yr_eight_var.xlsx', index=False ,engine='xlsxwriter')
five_yr_four_var.to_excel('Validation/five_yr_four_var.xlsx', index=False ,engine='xlsxwriter')
five_yr_eight_var.to_excel('Validation/five_yr_eight_var.xlsx', index=False ,engine='xlsxwriter')
