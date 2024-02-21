from scipy import datasets, ndimage
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os
im1 = cv.imread('C:\Image_Processing_2\einstein.png', cv.IMREAD_GRAYSCALE)
sobel_h = ndimage.sobel(im1, axis=0) 
sobel_v = ndimage.sobel(im1, axis=1)  
magnitude = np.sqrt(sobel_h**2 + sobel_v**2)
magnitude *= 255.0 / np.max(magnitude) 
directory = 'Q6'
if not os.path.exists(directory):
    os.makedirs(directory)
f, ax = plt.subplots(2, 2, figsize=(8, 8))
plt.gray() 
ax[0, 0].imshow(im1)
ax[0, 1].imshow(sobel_h)
ax[1, 0].imshow(sobel_v)
ax[1, 1].imshow(magnitude)
titles = ["original", "horizontal", "vertical", "magnitude"]
for i, ax in enumerate(ax.ravel()):
    ax.set_title(titles[i])
    ax.axis("off")
plt.savefig(os.path.join(directory, "parta.png"))
plt.show()
