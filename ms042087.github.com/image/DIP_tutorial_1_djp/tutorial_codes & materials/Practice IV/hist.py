# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:21:42 2017

@author: DONG Jinping
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure,data

def plot_img_hist(img,img_name='',bins=256):
    '''plot image and its histogram'''
    plt.figure(img_name)
    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.subplot(1,2,2)
    plt.hist(img.ravel(),bins)
    plt.show
    
# Main procedure
img_moon = data.moon()  # Load data

# Low contrast image
????  

# Contrast stretching
????

# Histogram equalization
????

# Adaptive Equalization
????





