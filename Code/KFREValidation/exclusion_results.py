# imports
import pandas as pd
import numpy as np
from xlsxwriter import *
from datetime import datetime
from sklearn.metrics import roc_auc_score

# loading data
exclusion_data = pd.read_excel('Validation/five_yr_four_var.xlsx')
df = pd.DataFrame(exclusion_data)

# Count the occurrences of True and False
true_count = df['excluded'].sum()
false_count = len(df) - true_count

# Calculate the percentages
true_percentage = (true_count / len(df)) * 100
false_percentage = (false_count / len(df)) * 100

print(f"Number of Entries: {true_count + false_count}")
print(f"Number of True: {true_count}")
print(f"Number of False: {false_count}")
print(f"% True: {true_percentage:.2f}%")
print(f"% False: {false_percentage:.2f}%")

true_rows = df[df['excluded']]

# Count the occurrences of each exclusion premise
premise_counts = true_rows['exclusion_premise'].value_counts()

# Calculate the total number of excluded cases
total_excluded = len(true_rows)

# Calculate the percentage of each exclusion premise
premise_percentages = (premise_counts / total_excluded) * 100

print("Exclusion Premise Statistics:")
print("=============================")
print(f"Total Excluded: {total_excluded}")
print("Exclusion Premise Counts:")
print(premise_counts)
print("\nExclusion Premise Percentages:")
print(premise_percentages)
