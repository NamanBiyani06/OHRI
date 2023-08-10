# this file is used to clean status data, only taking the last value for each duplicate

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
# warnings.filterwarnings('ignore')

# loading data as df
data = pd.read_excel("CleanData/status.xlsx")
status = pd.DataFrame(data)

# drops the duplicates from the primary key subset
# keep parameter specifies to keep the last entry of each duplicate
clean_status = status.drop_duplicates(subset='pt_id', keep="last", inplace=False)
# cleaning up the indexing on the dropped duplicates
clean_status.reset_index(drop=True, inplace=True)

values = clean_status['patransf_where'].value_counts(dropna=False)
originalValues = status['patransf_where'].value_counts(dropna=False)

print(clean_status.head(15))

print(values)
print(originalValues)
