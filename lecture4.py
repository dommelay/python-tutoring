import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1
df = pd.read_csv('/Users/dominiqueclark/ENGINEER/python_projects/python-tutoring/Inequality in Income 2 (1).csv')

#2
#first few rows
# print(df.head())
#info about data, data types and missing values
# print(df.info())
#descriptive statistics for numerical columns
# print(df.describe())

#3
#histogram to to visualize the income distribution
# plt.figure()
# sns.histplot(df['Inequality in income (2010)'])
# plt.title('Income Distribution')
# plt.xlabel('Income')
# plt.ylabel('Frequency')
# plt.show()
#scatter plots to visualize the relationship between variable pairs.
# sns.pairplot(df)
# plt.title('relationship between variable pais')
# plt.show()






