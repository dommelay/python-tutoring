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

categorical_columns = df1.select_dtypes(include=['object']).columns
df1[categorical_columns] = df1[categorical_columns].fillna(df1[categorical_columns].mode().iloc[0])

# print(df1.info())

numeric_summary = df1.describe()


summary_stats = df1.groupby('Continent')['Inequality in income (2021)'].describe()


average_inequality_by_continent = df1.groupby('Continent')[['Inequality in income (2010)', 'Inequality in income (2011)', 'Inequality in income (2012)', 'Inequality in income (2013)', 'Inequality in income (2014)', 'Inequality in income (2015)', 'Inequality in income (2016)', 'Inequality in income (2017)', 'Inequality in income (2018)', 'Inequality in income (2019)', 'Inequality in income (2020)', 'Inequality in income (2021)']].mean()

# print(average_inequality_by_continent)

grouped_data = df1.groupby('Continent')
aggregate_data_mean = grouped_data[[f'Inequality in income ({year})' for year in range(2010, 2022)]].mean()


average_inequality_by_continent = df1.groupby('Continent')[[f'Inequality in income ({year})' for year in range(2010, 2022)]].mean().mean(axis=1)

plt.figure()
sns.barplot(x=average_inequality_by_continent.index, y=average_inequality_by_continent.values)
plt.title('Average Inequality Distribution by Continent')
plt.xlabel('Average Inequality')
plt.ylabel('Level of Inequality')
# plt.show()

# plt.figure()
# sns.scatterplot(x='Income', y='Education Level', data=df1)
# plt.title('Income vs. Education Level')
# plt.xlabel('Income')
# plt.ylabel('Education Level')
# plt.show()


plt.figure()
df2 = average_inequality_by_continent.index
df3 = average_inequality_by_continent.values
sns.scatterplot(x=df2, y=df3)
plt.show()


# plt.figure()
# sns.histplot(data=aggregate_data_mean, bins=20, hue=aggregate_data_mean.index)
# plt.title('Income Inequality Distribution by Continent (2010-2021)')
# plt.xlabel('Mean Income Inequality')
# plt.ylabel('Frequency')
# plt.legend(title='Continent')
# plt.show()







