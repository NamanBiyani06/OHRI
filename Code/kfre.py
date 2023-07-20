# this file will be used in order to calculate the kidney failure risk equation for a 5 year period
# the equation is sourced from the university of manitoba
# http://mchp-appserv.cpe.umanitoba.ca/viewDefinition.php?printer=Y&definitionID=104785

import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

# kidney failure risk equation function
# NOTE: this equation has some bugs regarding outputs (negative values)
# TODO: ask OHRI for updated formula 
def kfre(eGFR, male, ACR, age):
    if eGFR is np.nan or male is np.nan or ACR is np.nan or age is np.nan:
        return 'No Value'
    
    a = -0.55418 * ((eGFR/5) - 7.22) + 0.26940 * (male - 0.56) + 0.45608 * (np.log(ACR) - 5.2774) - 0.21670 * ((age/10) - 7.04)
    prob = 1.0 - (pow(0.929, a))
    
    return (prob * 100)

# converts gender type to boolean
# male = 1
# female = 0
def gender_to_bool(gender):
    gender = gender.lower()
    if gender == 'male': return 1
    else: return 0

# loading data
data = pd.read_excel("CleanData\data.xlsx")
df = pd.DataFrame(data)

# list to contain all the risk probabilities
# NOTE: these percentage values are not tied to the pt_id or OHN
probs = []

# iterate through all data and call kfre
for i in range(df.shape[0]):
    eGFR = df.at[i, 'c_g_gfr']
    male = gender_to_bool(df.at[i, 'gender'])
    ACR = df.at[i, 'spot_acr']
    age = 2023 - df.at[i, 'dob'].year
    
    # filtering out the np.NaN values
    # NOTE: These values are caused by a lack of data in the original data.xlsx
    risk = kfre(eGFR, male, ACR, age).round(2)
    if risk != 'No Value': probs.append(kfre(eGFR, male, ACR, age).round(2))
    else: pass

# printing out all data
print("5-year Risk of Kidney Failure: ", probs, sep="")

