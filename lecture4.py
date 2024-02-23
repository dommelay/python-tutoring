import pandas as pd
import numpy as np

#1
df = pd.read_csv('/Users/dominiqueclark/ENGINEER/python_projects/python-tutoring/Inequality in Income 2 (1).csv')

#2
#first few rows
print(df.head())
#info about data, data types and missing values
print(df.info())
#descriptive statistics for numerical columns
print(df.describe())




