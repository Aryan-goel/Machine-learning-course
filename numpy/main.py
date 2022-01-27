myList=[[1,2,3],[4,5,6],[7,8,9]]
import numpy as np
arr=np.array(myList)

ak=np.random.rand(5,5)
#print(ak)
ae=np.random.randint(1,100,10) ## prints 10 random int's form 1 to 100
#print(ae)
te=arr.reshape(3,3) #to change the shape of the array without changing the data
#print(te)
randArr=np.random.randint(0,50,10)
print(randArr)
max=randArr.max() ## to get the maximum value from the array
print(max)
print(randArr.argmax()) # returns the index of the max value
print(randArr.argmin()) # returns the index of the min value
print(arr.shape)
print(arr.dtype)
