import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head())
print('='*30)
#check for missing values
print(df.isnull().sum())

#check for shape
print(df.shape)

print(df.dropna().shape)

print('='*30)

#drop rows containig missing values
print(df.dropna(axis = 1))


#mean value imputation
## Mean Imputation Works Well when we have normally distributed data
df = sns.load_dataset("titanic")
sns.histplot(df['age'],kde = True)

df['mean_age'] = df['age'].fillna(df['age'].mean())
print(df[['mean_age','age']])
print('='*90)


#median value imputation - if we have outliers in data
df['age_median']=df['age'].fillna(df['age'].median())
print(df[['age_median','mean_age','age']])

print('='*90)

#mode imputation-categorcal distribution
print(df[df['embarked'].isnull()])

print(df['embarked'].unique)
print('='*90)
mode_value=df[df['embarked'].notna()]['embarked'].mode()[0]
print("mode value id:",mode_value)
df['embarked_mode']=df['embarked'].fillna(mode_value)
print(df[['embarked_mode','embarked']])
print('='*90)