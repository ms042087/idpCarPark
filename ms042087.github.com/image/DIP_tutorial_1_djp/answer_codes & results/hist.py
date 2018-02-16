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
plot_img_hist(img_moon,'Low contrast image')  

# Contrast stretching
p1, p2 = np.percentile(img_moon, (2, 98))  
img_moon_ctrststre= exposure.rescale_intensity(img_moon, in_range=(p1, p2))
plot_img_hist(img_moon_ctrststre,'Contrast stretching')

# Histogram equalization
img_moon_eqhist = exposure.equalize_hist(img_moon)  
plot_img_hist(img_moon_eqhist,'Histogram equalization')

# Adaptive Equalization
img_moon_adapteq = exposure.equalize_adapthist(img_moon, clip_limit=0.03)
plot_img_hist(img_moon_adapteq,'Adaptive Equalization')





