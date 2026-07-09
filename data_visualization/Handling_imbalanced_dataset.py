import numpy as np
import pandas as pd

df = np.random.seed(123)

#creating two classes
n_classes = 1000
class_0_ratio = 0.9
n_class_0 = int((n_classes*class_0_ratio))
n_class_1 =n_classes - n_class_0
print(n_class_0,n_class_1)

print('='*90)

## CREATE MY DATAFRAME WITH IMBALANCED DATASET
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})
print(class_0['feature_1'])

print('='*90)
print(class_1)
df = pd.concat([class_0,class_1]).reset_index(drop = True)
print(df)

## upsampling
df_minority=df[df['target']==1]
df_majority=df[df['target']==0]

from sklearn.utils import resample
df_minority_upsampled=resample(df_minority,replace=True, #Sample With replacement
         n_samples=len(df_majority),
         random_state=42
        )
print(df_minority_upsampled.shape)
print('='*90)
print(df_minority_upsampled.head())
print('='*90)
df_upsampled=pd.concat([df_majority,df_minority_upsampled])

print(df_upsampled['target'].value_counts())
print('='*90)


#downsampling
from sklearn.utils import resample

# Separate classes
df_majority = df[df['target'] == 0]
df_minority = df[df['target'] == 1]

# Downsample majority class
df_majority_downsampled = resample(
    df_majority,
    replace=False,              # No duplicate rows
    n_samples=len(df_minority), # Reduce to 100 rows
    random_state=42
)

# Combine minority class with downsampled majority class
df_downsampled = pd.concat([df_majority_downsampled, df_minority])

# Shuffle rows (optional but recommended)
df_downsampled = df_downsampled.sample(frac=1, random_state=42).reset_index(drop=True)

# Check class distribution
print(df_downsampled['target'].value_counts())


#comarision of upsampling and downsampling.
# | Aspect            | Upsampling                                                     | Downsampling                                                         |
# | ----------------- | -------------------------------------------------------------- | -------------------------------------------------------------------- |
# | What it does      | Increases minority samples                                     | Reduces majority samples                                             |
# | Dataset size      | Increases                                                      | Decreases                                                            |
# | Information loss  | No                                                             | Yes (some majority data is discarded)                                |
# | Duplicate samples | Yes (random oversampling)                                      | No                                                                   |
# | Risk              | Can overfit due to repeated samples                            | Can underfit if too much data is removed                             |
# | Best for          | Small minority class when you want to retain all majority data | Very large datasets where losing some majority samples is acceptable |


#SMOTE
from sklearn.datasets import make_classification

x,y = make_classification(n_redundant=0,n_features=2,n_clusters_per_class=1,weights=[0.90],n_samples=1000,random_state=12)
import pandas as pd
df1 = pd.DataFrame(x,columns = ['f1','f2'])
print(df1)
print('='*90)
df2 = pd.DataFrame(y,columns = ['target'])
print(df2)
print('='*90)
final_df=pd.concat([df1,df2],axis=1)
print(final_df)
print('='*90)

import matplotlib.pyplot as plt
plt.scatter(final_df['f1'],final_df['f2'],c = final_df['target'])
plt.show()

from imblearn.over_sampling import SMOTE

oversample = SMOTE()
X,y=oversample.fit_resample(final_df[['f1','f2']],final_df['target'])
print(len(y[y==0]))
print(len(y[y==1]))

df1=pd.DataFrame(X,columns=['f1','f2'])
df2=pd.DataFrame(y,columns=['target'])
oversample_df=pd.concat([df1,df2],axis=1)
plt.scatter(oversample_df['f1'],oversample_df['f2'],c = oversample_df['target'])
plt.show()