# this file is used for printing customized outputs when I don't have the correct data for a report
import pandas as pd

data = pd.read_excel("CleanData/data.xlsx")
df = pd.DataFrame(data)

transfers = df['patransf_where'].value_counts()
print(transfers.sort_index())

# getting the frequency values for patransf_where that are normalized and rounded
freq_percent = df.patransf_where.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'

print(freq_percent.sort_index())

