# this file will be used in order to calculate the kidney failure risk equation for a 5 year period
# the equation is sourced from the university of manitoba
# http://mchp-appserv.cpe.umanitoba.ca/viewDefinition.php?printer=Y&definitionID=104785

import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

def kfre(eGFR, male, ACR, age):
    if eGFR is np.nan or male is np.nan or ACR is np.nan or age is np.nan:
        return np.nan
    
    a = -0.55418 * ((eGFR/5) - 7.22) + 0.26940 * (male - 0.56) + 0.45608 * (np.log(ACR) - 5.2774) - 0.21670 * ((age/10) - 7.04)
    prob = 1.0 - (pow(0.929, a))
    
    return (prob * 100)

# loading data
data = pd.read_excel("CleanData\data.xlsx")
df = pd.DataFrame(data)

print(df.head())
print(type(df.at[1, 'dob']))

probs = []

for i in range(10):
    eGFR = df.at[i, 'c_g_gfr']
    male = df.at[i, 'gender']
    ACR = df.at[i, 'spot_acr']
    age = 2023 - datetime.fromtimestamp(df.at[i, 'dob']).datetime.year
    probs += kfre(eGFR, male, ACR, age).round(2)

# prob = (kfre(26, True, 39.80, 58)).round(3)

print("5-year Risk of Kidney Failure: ", probs, sep="")
