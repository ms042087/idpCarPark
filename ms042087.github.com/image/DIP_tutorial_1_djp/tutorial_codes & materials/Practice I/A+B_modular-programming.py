# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:19:05 2017

@author: DONG Jinping
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

def ????:
    '''Perform elemenrwise average of two images'''
    return ????

# Main procedure
faceA = misc.imread('letterA.png')
faceB = misc.imread('letterB.png')
faceAB = ????

# Display images
faceAB=np.uint8(faceAB)
plt.figure('modular programming example')
plt.imshow(faceAB,cmap='gray')
misc.imsave('letterA+B.png',faceAB)