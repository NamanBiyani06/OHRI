# this file is used for plotting information found in data.xlsx through statistics.py
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pygwalker as pyg
import psutil

# importing the data and inserting it into a dataframe
data = pd.read_excel("CleanData\data.xlsx")
data = pd.DataFrame(data)

gwalker = pyg.walk(data)