# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:00:20 2016

@author: antony
"""

import numpy as np
from skimage.morphology import disk
import cv2


threshold = 190
def change_threshold(thresh):
    global threshold
    threshold = thresh
    
def find_blue(frame,blue_threshold = 20):
    
    #blur = cv2.blur(frame,(2,2))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([120-blue_threshold, threshold, 50])
    upper_blue = np.array([120+blue_threshold, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    return mask
    
if __name__ == '__main__':
    #cap = cv2.VideoCapture(0)
    frame = cv2.imread('blue-screen.jpg')
    background = cv2.imread('campus.jpg')
    background = cv2.resize(background,(frame.shape[1], frame.shape[0]))
    mask = find_blue(frame)
    
    cv2.namedWindow('Video')
    cv2.createTrackbar('Saturation threshold', 'Video', threshold, 255, change_threshold)
    
    #while cv2.waitKey(1000/3) & 255 != 27:
    #ret, frame = cap.read()
    
    # Find blue object
    mask = find_blue(frame)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, disk(3))
    #mask = cv2.dilate(mask, disk(3))
    
    # Blur all the blue objects
    #blur = cv2.blur(frame,(21,21))
    #blur = cv2.bitwise_and(blur, blur, mask=mask2)
    
    chroma_key = cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
    chroma_key |= cv2.bitwise_and(background,background,mask=mask)
    
    # Show all frames
    #fused = np.hstack( (frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), censored) )
    
    #cv2.imshow('Video', chroma_key)
    cv2.imwrite('fused.jpg', chroma_key)

    #cap.release()
    cv2.destroyAllWindows()