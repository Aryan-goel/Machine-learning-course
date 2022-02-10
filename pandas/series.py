import numpy as np
import pandas as pd
lables=['a','b','c']
my_data=[10,20,30]
arr= np.array(my_data)
d={'a':10,'b':20,'c':30}

ans=pd.Series(data=my_data)
#print(ans)
res=pd.Series(data=my_data,index=lables) # another way of creating a series
#print(res)f
#print(pd.Series(lables,arr )) # wide variety of data types can be stored in a series
ser1=pd.Series([1,2,3,4],['ind','usa','nz','jp'])
#print(ser1)
ser2=pd.Series([1,2,5,4],['ind','usa','uk','jp'])
ans=ser1+ser2 # adds the value of same lables in both the series
print(ans)
