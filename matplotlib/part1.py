import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
print(x)

#functional method of creating plots
t=plt.plot(y,x,'b-')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('demo')
#plt.show()
# print(t)

plt.subplot(1,2,1)
plt.plot(x,y,'b')
plt.subplot(1,2,2)
plt.plot(y,x,'r')
#plt.show()
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
