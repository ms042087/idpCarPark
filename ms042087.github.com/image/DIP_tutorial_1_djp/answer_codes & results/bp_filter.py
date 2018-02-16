# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 10:48:43 2017

@author: DONG Jinping
"""

runfile('edge_enhance.py')

# bandpass filter design procedure

kernel1=gaussian_kernel(N, sigma=40)
kernel2=gaussian_kernel(N, sigma=5)
kernel1_2=kernel1-kernel2


# 2d plot
plt.figure('gaussian kernel 1')
plt.imshow(kernel1,cmap='gray')

plt.figure('gaussian kernel 2')
plt.imshow(kernel2,cmap='gray')

plt.figure('gaussian kernel 1-2')
plt.imshow(kernel1_2,cmap='gray')

plt.figure('Bandpass filter')
plt.imshow(H,cmap='gray')


# 3d plot
from mpl_toolkits.mplot3d import Axes3D

coord = np.arange(-N/2, N/2)
xx,yy = np.meshgrid(coord,coord)

fig = plt.figure('gaussian kernel 1 (3d)')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,kernel1,cmap=plt.cm.coolwarm,linewidth=0, antialiased=False)
plt.show()

fig = plt.figure('gaussian kernel 2 (3d)')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,kernel2,cmap=plt.cm.coolwarm,linewidth=0, antialiased=False)
plt.show()

fig = plt.figure('gaussian kernel 1-2 (3d)')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,kernel1_2,cmap=plt.cm.coolwarm,linewidth=0, antialiased=False)
plt.show()

fig = plt.figure('Bandpass filter (3d)')
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,H,cmap=plt.cm.coolwarm,linewidth=0, antialiased=False)
plt.show()

plt.figure('A_spectral')
plt.imshow(fftpack.fft2(misc.imread('img_A_gaussian_noise.png')),cmap='gray')




