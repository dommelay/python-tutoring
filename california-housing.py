import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api as sm

# Data Import and Initial Exploration (50 points):
df = pd.read_csv('/Users/dominiqueclark/ENGINEER/python_projects/python-tutoring/housing-1.csv')

# print(df.head())
# print(df.info())

target = df['median_house_value']

# print(target)

# Descriptive Statistics Study (50 points):
# print(df.describe())
missing_values = df.isnull().sum()
# print(missing_values)


# Train-Test Split (25 points):
X = df.drop(columns=['median_house_value'])  # Features
y = df['median_house_value']  # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print("Training set shape:", X_train.shape, y_train.shape)
# print("Testing set shape:", X_test.shape, y_test.shape)
# print(X_train.head())  # Print the first few rows of the training features
# print(y_train.head())  # Print the corresponding target values

# Exploratory Data Analysis (EDA) (75 points):
# distribution of key variables
# plt.figure(figsize=(12, 6))
# sns.boxplot(data=X_train)
# plt.title('Boxplot of Key Variables')
# plt.xticks(rotation=45)
# plt.show()
# relationship between features and target value
# for feature in X_train.columns:
#     plt.figure(figsize=(8, 6))
#     sns.scatterplot(x=X_train[feature], y=y_train)
#     plt.title(f'Scatter plot of {feature} vs Median House Value')
#     plt.xlabel(feature)
#     plt.ylabel('Median House Value')
    # plt.show()
# relationship between features
# sns.pairplot(data=X_train)
# plt.suptitle('Pairplot of Features', y=1.02)
# plt.show()

# Data Preprocessing (50 points):
df1 = df.dropna()
# print(df1.isnull().sum())

# Correlation Matrix and Feature Selection (50 points):
corr_matrix = df1.corr()
# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Simple Linear Regression (50 points):
X = df[['median_income']]  # Feature
y = df['median_house_value']  # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Testing Data')
plt.plot(X_train, model.predict(X_train), color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.legend()
plt.grid(True)
plt.show()

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Model Evaluation for Simple Linear Regression (25 points):
y_pred = model.predict(X_test)
r_squared = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R-squared:", r_squared)
print("RMSE:", rmse)

# Using statsmodels.api for Statistical Metrics (25 points):
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())