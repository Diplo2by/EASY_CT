import matplotlib.pyplot as plt
# from matplotlib import pylab
import math
import numpy as np

y=[]
w=[]
f = open("accuracy.txt", "r")
for each in f:
    # TO IGNORE VALUES STARTING FROM 0.0
    # if each[0:3] != "0.0":       
    each = float(each)*100
    each1 = round(each,2)
    w.append(each1)
    math.floor(each)
    each = int(each)
    y.append(each)
    
f.close()

# w.sort()
# y.sort()

q=len(y)+1
fig ,ax = plt.subplots(figsize=(14,10))

x=np.arange(0,10,0.1)
z=[]
for i in range(len(y)):
    z.append(i+1)

plt.scatter(z,y)
plt.plot(z,y)
plt.ylim([0,100])
plt.xlim([0,q])

# FOR CO-ORDINATES
# for i,j in zip(z,w):
#     plt.text(i,j+0.5,'({},{})'.format(i,j),fontdict={'fontsize':12})

plt.xlabel('Accuracy',fontdict={'fontsize':20})
plt.ylabel('Test-cases',fontdict={'fontsize':20})
plt.title('Accuracy Trends',fontsize=25,color="blue")
plt.show()

