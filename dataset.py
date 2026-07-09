import pandas as pd 

import seaborn as sns 

df=sns.load_dataset("iris") 

#Inspect the first few rows with df.head() 

print("First 5 rows of dataset:\n",df.head()) 

#Check shape and column types with df.info() 

print("\nDataset Info:") 

print(df.info()) 

#DATA CLEANING 

#Checking missing values 

print("\nMissing values in dataset:") 

print(df.isnull().sum()) 

#Since there is no null value..No requirement of using fillna() or dropna 

# #EXPLORATORY DATA ANALYSIS
print("\nSummary Statistics:") 

print(df.describe()) 

#DATA VISUALIZATION 

# importing matplot library for graphs 

import matplotlib.pyplot as plt 

#Univariate Analysis 

sns.histplot(df["sepal_length"],kde=True,bins=20,color="blue") 

plt.title("Distribution of Sepal Length") 

plt.show() 

#Bivariate Analysis 

sns.scatterplot(x="sepal_length",y="petal_length",hue="species",data=df) 

plt.title("Sepal vs Petal Length by Species") 

plt.show() 
# #Multivariate Analysis 

sns.pairplot(df,hue="species") 

plt.suptitle("Pair plot of iris features",y=1.02) 

plt.show() 
numeric_df=df.select_dtypes(include='number')
corr=numeric_df.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
#PREDICTIVE MODELING
#LOGISTIC REGRESSION
#Classification Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# # Features and target
# X = df.drop("species", axis=1)
# y = df["species"]
# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # Build model
# log_reg = LogisticRegression(max_iter=200)
# log_reg.fit(X_train, y_train)
# # Predictions
# y_pred = log_reg.predict(X_test)
# # Evaluation
# print("\nClassification Results")
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Build model
x = df[['sepal_width','petal_length','petal_width']]
y = df['sepal_length']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# lin_reg = LinearRegression()
# lin_reg.fit(X_train, y_train)
# # Predictions
# y_pred = lin_reg.predict(X_test)
# # Evaluation
# print("Linear Regression Results")
# print("Intercept:", lin_reg.intercept_)
# print("Coefficient:", lin_reg.coef_)
# print("Mean Squared Error:",mean_squared_error(y_test, y_pred))
# mse = mean_squared_error(y_test, y_pred)
# print("Root Mean Squared Error:",np.sqrt(mse) )
# print("R² Score:",r2_score(y_test, y_pred))
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Model training
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Predictions
y_pred = lin_reg.predict(X_test)

# Evaluation
print("Linear Regression Results")
print("Intercept:", lin_reg.intercept_)
print("Coefficient:", lin_reg.coef_)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Root Mean Squared Error
print("Root Mean Squared Error:", np.sqrt(mse))

# R² Score
print("R² Score:", r2_score(y_test, y_pred))


