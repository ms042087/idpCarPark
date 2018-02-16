# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 01:42:58 2017

@author: DONG Jinping
"""

import matplotlib.pyplot as plt
from scipy import misc
from skimage.filters import gaussian_filter,median
from skimage.morphology import rectangle

# Main procedure
#A_noise=misc.imread('img_A_gaussian_noise.png')   # choose noise
A_noise=misc.imread('img_A_saltpepper_noise.png')

A_noise_filtered1=gaussian_filter(A_noise,sigma=5)
A_noise_filtered2=median(A_noise,rectangle(3,3))

# Display images
plt.figure('noisy image')
plt.imshow(A_noise,cmap='gray')
plt.figure('gaussian filter')
plt.imshow(A_noise_filtered1,cmap='gray')
plt.figure('median filter')
plt.imshow(A_noise_filtered2,cmap='gray')

misc.imsave('img_A_filtered.png',A_noise_filtered2)
