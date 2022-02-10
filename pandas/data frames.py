import numpy as np
import pandas as pd
from  numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])

print(df[['w','x']])
# print(type(df))
k=df['new']= df['w']+ df['x']
print(df)
df.drop('new',axis=1,inplace=True) # to permanantly remove the new col we use inplace
print(df)
print(df.shape)
print(df.loc['a'])

# print(df>0)

print(df[df>0])

boolser=df['w']>0
print(boolser)


