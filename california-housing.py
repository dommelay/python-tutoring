import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

california_housing = fetch_california_housing()

df = pd.read_csv('/Users/dominiqueclark/ENGINEER/python_projects/python-tutoring/california-housing.py')

print(df.head())
print(df.info())



# target = df['median_house_value']

# print(target)



