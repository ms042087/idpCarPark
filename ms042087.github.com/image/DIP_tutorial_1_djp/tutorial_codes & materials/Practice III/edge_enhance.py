# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 02:55:09 2017

@author: DONG Jinping
"""

from scipy import misc,fftpack
import matplotlib.pyplot as plt
import numpy as np

def gaussian_kernel(N, sigma):
    '''Construct a blur kernel'''
    coord = np.arange(-N/2, N/2)
    xx,yy = np.meshgrid(coord,coord)
    rr = -0.5/????**2 * (????**2 + ????**2)
    return np.exp(rr)

def fft_convolve(img, H):
    '''Apply filter in spectral domain'''
    if img.shape != H.shape:
        return -1
    IMG = fftpack.fft2(img)
    power_spectrum = fftpack.fftshift(np.log(np.abs(IMG)))
    IMG *= fftpack.ifftshift(H)
    new_img = ????(IMG)
    return new_img.real, power_spectrum
    
# Load image
faceA = misc.imread('img_A_gaussian_noise.png',flatten=True)
faceA /= np.????(faceA)
N = faceA.shape[0]

# Bandpass filter
#H = 1.
H = gaussian_kernel(N, sigma=40)
H -= gaussian_kernel(N, sigma=5)
H /= np.linalg.norm(H,1)

# Apply filter
face_edge,FACE = fft_convolve(faceA, H)
face_edge[face_edge<0] = 0.

# Display image
plt.subplot(2,2,1)
plt.imshow(faceA,cmap='gray')
plt.title('Input')

plt.subplot(2,2,2)
plt.imshow(face_edge,cmap='gray')
plt.title('Output')

plt.subplot(2,2,3)
plt.imshow(FACE,cmap='gray')
plt.title('Power spectrum')

plt.subplot(2,2,4)
plt.imshow(H,cmap='gray')
plt.title('Filter')

plt.show()

misc.imsave('letterA_edge.png',face_edge)


