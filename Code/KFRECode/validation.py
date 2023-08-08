# this file is going to be used to format validation.xlsx
# validation.xlsx is used as a validation dataset for the KFRE predictions

# imports
import pandas as pd
import numpy as np
import xlsxwriter
import datetime
import warnings
# warnings.filterwarnings("ignore")

validationData = pd.read_excel('CleanData/status.xlsx')
validation = pd.DataFrame(validationData)

# drops the duplicates from the primary key subset
# keep parameter specifies to keep the last entry of each duplicate
validation = validation.drop_duplicates(subset='pt_id', keep="last", inplace=False)
# cleaning up the indexing on the dropped duplicates
validation.reset_index(drop=True, inplace=True)

# dropping columns that are not useful to creating the validation set
validation = validation.drop(['cs_pt_alive', 'cs_cod', 'period', 'cs_codoth', 'patransf_other', 'access_iod'], axis=1)

# creating new columns to set the validation data
validation[['trans/dialysis', 'death', 'other', 'date']] = np.nan

# death column
validation.loc[validation['cs_dod'].notnull(), 'death'] = 1
validation.loc[validation['cs_dod'].notnull(), 'date'] = validation['cs_dod']

# trans/dialysis column
# NOTE: Clean up this code
validation.loc[(validation['patransf_where'] == 2) | (validation['patransf_where'] == 3) | (validation['patransf_where'] == 4) | (validation['patransf_where'] == 5) | (validation['patransf_where'] == 6) | (validation['patransf_where'] == 7), 'trans/dialysis'] = 1
validation.loc[(validation['patransf_where'] == 2) | (validation['patransf_where'] == 3) | (validation['patransf_where'] == 4) | (validation['patransf_where'] == 5) | (validation['patransf_where'] == 6) | (validation['patransf_where'] == 7), 'date'] = validation['dotransf_pri']

# other column
validation.loc[(validation['death'].isnull()) & (validation['trans/dialysis'].isnull()), 'other'] = 1
validation.loc[(validation['death'].isnull()) & (validation['trans/dialysis'].isnull()), 'date'] = validation['fup_date']

# chaning all other values to false
validation.loc[(validation['death'].isnull()), 'death'] = 0
validation.loc[(validation['trans/dialysis'].isnull()), 'trans/dialysis'] = 0
validation.loc[(validation['other'].isnull()), 'other'] = 0

# printing some stats
print(validation['date'].isnull().sum())
percent_death = (validation['death'].sum() / len(validation)) * 100
percent_transdialysis = (validation['trans/dialysis'].sum() / len(validation)) * 100
percent_other = (validation['other'].sum() / len(validation)) * 100

print("%Death ", percent_death, sep='')
print("%Transplace/Dialysis ", percent_transdialysis, sep='')
print("%Other ", percent_other, sep='')

print(percent_other + percent_death + percent_transdialysis)

# outputting validation set to validation.xlsx
validation.to_excel('KFRE/validation.xlsx', index=False, engine='xlsxwriter')

