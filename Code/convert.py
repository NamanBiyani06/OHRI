# this is a file that converts all of the files into .xslx
#imports 
import pandas as pd
import openpyxl
import xlsxwriter

# processing the data
# NOTE: index column 0 is used because of poor data formatting
demo_1_csv = pd.read_csv("RawData/Demo_1.csv", index_col=[0])
PR_hist_1_csv = pd.read_csv("RawData/PR_hist_1.csv", index_col=[0])

# exporting the data to the clean data folder for further processing
demo_1_csv.to_excel("CleanData/Demo.xlsx", engine='xlsxwriter')
PR_hist_1_csv.to_excel("CleanData/PR_hist.xlsx", engine='xlsxwriter')
