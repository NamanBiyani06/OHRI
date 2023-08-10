# this file is used for printing customized outputs when I don't have the correct data for a report
import pandas as pd
import numpy as np

data = pd.read_excel("CleanData/data.xlsx")
df = pd.DataFrame(data)

transfers = df['patransf_where'].value_counts()
print(transfers.sort_index())

# getting the frequency values for patransf_where that are normalized and rounded
freq_percent = df.patransf_where.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'

pt_dead = (df[(df['patransf_where'] == 0) & (df['cs_pt_alive'] != 1)].pt_id.tolist())
print(pt_dead)
print(pt_dead.__len__())

print(freq_percent.sort_index())

