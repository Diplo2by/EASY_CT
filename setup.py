import easyocr
from easyocr import imgproc
import cv2 


# pre processing 
rd = easyocr.Reader(['ch_sim'])

path = 'load/ten.png'
res1 = rd.readtext(path)

img = imgproc.loadImage(path)


res2 = rd.readtext(img)


print(res1[-1][2])
print(res2[-1][2])


# cv2.imshow('test',cv2.cvtColor(img,cv2.COLOR_BGR2RGB) )
# cv2.waitKey(0)
# cv2.destroyAllWindows
