import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1
df = pd.read_csv('/Users/dominiqueclark/ENGINEER/python_projects/python-tutoring/Inequality in Income 2 (1).csv')

#2
#first few rows
# print(df['Human Development Groups'])
# print(df.head())
#info about data, data types and missing values
# print(df.info())
#descriptive statistics for numerical columns
# print(df.describe())

#3
#histogram to to visualize the income distribution
# plt.figure()
# sns.histplot(df['Inequality in income (2020)'])
# plt.title('Income Distribution')
# plt.xlabel('Income')
# plt.ylabel('Frequency')
# plt.show()
#scatter plots to visualize the relationship between variable pairs.
# sns.pairplot(df)
# plt.title('relationship between variable pais')
# plt.show()

#4 
# income_columns = [col for col in df.columns if col.startswith("Inequality in income")]
# fig, axes = plt.subplots(nrows=1, ncols=len(income_columns), figsize=(15, 5))

# for i, col in enumerate(income_columns):
#     sns.histplot(df[col], ax=axes[i])
#     # axes[i].set_title(f'{col}')
#     axes[i].set_xlabel('Income Inequality')
#     axes[i].set_ylabel('Frequency')

# plt.tight_layout()
# plt.show()

df1 = df.copy()
numerical_columns = df1.select_dtypes(include=['float64']).columns
df1[numerical_columns] = df1[numerical_columns].fillna(df1[numerical_columns].median())
# print(df1.info())

# categorical_columns = df1.select_dtypes(include=['object']).columns
# df1[categorical_columns] = df1[categorical_columns].fillna([categorical_columns].mode().iloc[0])





