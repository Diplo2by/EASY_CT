import easyocr
from easyocr import imgproc
import cv2 

import numpy as np
import matplotlib.pyplot as plt
 

# pre processing 
rd = easyocr.Reader(['ch_sim'])

path = 'load/darshan.png'
res1 = rd.readtext(path)

img = imgproc.loadImage(path)


res2 = rd.readtext(img)


print(res1[-1][2])
print(res2[-1][2])
data = {'Raw Image':res1[-1][2]*100, 'PreProcessed Image':res2[-1][2]*100, }
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(courses, values, color ='maroon',
        width = 0.2,)
plt.xlabel("Types of Images")
plt.ylabel("Accuracy")
plt.title("Confidence Level")
plt.ylim(95, 100)

# plt.plot(res1[-1][2],res2[-1][2])
# plt.xticksmin(res1[-1][2], max(res1[-1][2])+1, 1.0)
# plt.yticks([99,res2[-1][2]*100])
plt.show()

# cv2.imshow('test',cv2.cvtColor(img,cv2.COLOR_BGR2RGB) )
# cv2.waitKey(0)
# cv2.destroyAllWindows