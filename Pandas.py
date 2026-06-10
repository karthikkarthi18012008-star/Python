import pandas as pd
data = {
    'Name':['Virat','Dhoni','Hardik','Rohit'],
    'Role':['first_down','fifth_down','sixth_down','opener'],
    'Age':[37,40,30,38],
    'Jetsey_number':[18,7,33,45]
}
#1-D labelled array
s = pd.Series(data['Name'])
print("\nSeries is",s)
print("="*30)

#DataFrame
df = pd.DataFrame(data,index = ['a','b','c','d'])
print("\nDataFrame is :\n",df)
print("="*30)

#creating DataFrame using numpy array
import numpy as np
arr = np.array([[1,'Rahul',1],[2,'Rajat',21],[3,'Sanju',9]])
df2 = pd.DataFrame(arr,columns =['sl.no','Name',"Jersey_number"])
print("\nDataFrame created using numpy array:\n")
print(df2) 

#Handle missing data

data = {
    'Name': ['Asha', 'Bala', 'Chand', 'Deepa'],
    'Marks': [85, np.nan, 78, np.nan],
    'Age': [20, 21, np.nan, 22]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Fill missing values
df_filled = df.fillna({'Marks': df['Marks'].mean(), 'Age': df['Age'].mean()})
print("\nAfter Filling Missing Values:\n", df_filled)
# Drop rows with missing values
df_dropped = df.dropna()
print("\nAfter Dropping Rows with Missing Values:\n", df_dropped)
