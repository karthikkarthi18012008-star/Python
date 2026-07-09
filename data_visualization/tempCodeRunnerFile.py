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