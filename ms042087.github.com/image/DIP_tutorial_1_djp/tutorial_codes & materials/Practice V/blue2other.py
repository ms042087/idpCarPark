# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 20:29:29 2017

@author: DONG Jinping
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def blue2other(img,Hue=60,range=10):
    '''change blue background to green'''
    
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # H of blue is 120, green 60
    lower_blue = np.array([120-range,50,50])
    upper_blue = np.array([120+range,255,255])
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    mask[mask==255]=1
    
    img_new_hsv=img_hsv
    H=img_new_hsv[:,:,0]   # the first layer is 0!
    H=H-(120-Hue)*mask
    
    img_new_hsv[:,:,0]=H
    img_new=cv2.cvtColor(img_new_hsv, cv2.COLOR_HSV2BGR)
    
    return img_new
    
img_b = cv2.imread('blue-screen.jpg')
img_n = blue2other(img_b,60,10)

# plot and save image
plt.figure('what color is the backgroud?')
plt.imshow(img_n)
plt.imsave('green-screen.jpg',img_n)








