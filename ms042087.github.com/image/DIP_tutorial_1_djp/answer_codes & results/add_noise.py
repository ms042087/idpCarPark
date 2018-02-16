# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 10:38:41 2017

@author: DONG Jinping
"""

from scipy import misc
import matplotlib.pyplot as plt
from skimage.util import random_noise


# Main procedure
faceA = misc.imread('letterA.png')

faceA_noise1 = random_noise(faceA, mode='gaussian')
faceA_noise2 = random_noise(faceA, mode='s&p')

# Display images
plt.figure('A + gaussian noise')
plt.imshow(faceA_noise1,cmap='gray')

plt.figure('A + salt&pepper noise')
plt.imshow(faceA_noise1,cmap='gray')

# Output images
misc.imsave('img_A_gaussian_noise.png',faceA_noise1)
misc.imsave('img_A_saltpepper_noise.png',faceA_noise2)


