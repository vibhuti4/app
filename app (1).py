# -*- coding: utf-8 -*-
"""App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kuqcbS0wFBkJCYWz34B7lMGifXAef7Wo
"""

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
#import matplotlib.image as mpimg 
#from matplotlib.pyplot import imshow
#%matplotlib inline

img = np.zeros((100,100,3), np.uint8)
#cv2_imshow(img)
#@title Color Palatte

B = 0 #@param {type:"slider",min:0, max:255, step:1}
G = 124 #@param {type:"slider",min:0, max:255, step:1}
R = 0 #@param {type:"slider",min:0, max:255, step:1}
CB = True #@param {type:"boolean"}
print(B)
print(R)
print(G)
print(CB)

if CB == False:
  img[:] = 0
else:
  img[:] = [B, G, R]

cv2_imshow(img)