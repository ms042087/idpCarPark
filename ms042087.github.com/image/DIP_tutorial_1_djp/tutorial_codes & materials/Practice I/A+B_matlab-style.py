# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:53:36 2017

@author: DONG Jinping
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

faceA = misc.imread('letterA.png')
faceB = misc.imread('letterB.png')

faceAB = 0.5*faceA + 0.5*faceB


# Display images
faceAB=np.uint8(faceAB)
plt.figure('matlab-style code example')
plt.imshow(faceAB,cmap='gray')