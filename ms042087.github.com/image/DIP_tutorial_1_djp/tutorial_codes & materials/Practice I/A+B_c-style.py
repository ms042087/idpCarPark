# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:01:40 2017

@author: DONG Jinping
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

faceA = misc.imread('letterA.png')
faceB = misc.imread('letterB.png')

faceAB = np.zeros((500,500))
for i in range(500):
    for j in range(500):
        faceAB[i,j] = 0.5*faceA[i,j] + 0.5*faceB[i,j]
              

# Display images
faceAB=np.uint8(faceAB)
plt.figure('c-style code example')
plt.imshow(faceAB,cmap='gray')
