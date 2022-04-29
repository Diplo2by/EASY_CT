from msilib.schema import Directory
from matplotlib import pyplot as plt
import numpy as np
import cv2
import easyocr
import os

rd = easyocr.Reader(['ch_sim'])
fh = open('./accuracy.txt','w')
directory = 'load'

for filename in os.scandir(directory):
    if filename.is_file():
        text = rd.readtext(filename.path)
        
        if text != []:
            
            fh.write(str(text[0][2]))
            fh.write("\n")
        else:
            fh.write("0.0"+"\n")
           

fh.close()
