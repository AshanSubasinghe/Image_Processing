from scipy import ndimage
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os
im1 = cv.imread('C:\Image_Processing_2\einstein.png', cv.IMREAD_GRAYSCALE)
im1_float = im1.astype(np.float32)
sobel_h = ndimage.sobel(im1_float, axis=0) 
sobel_v = ndimage.sobel(im1_float, axis=1)  
magnitude = np.sqrt(sobel_h**2 + sobel_v**2)
magnitude *= 255.0 / np.max(magnitude) 
directory = 'Q6'
if not os.path.exists(directory):
    os.makedirs(directory)
f, axs = plt.subplots(2, 2, figsize=(8, 8))
plt.gray() 
axs[0, 0].imshow(im1, cmap='gray')
axs[0, 1].imshow(sobel_h, cmap='gray')
axs[1, 0].imshow(sobel_v, cmap='gray')
axs[1, 1].imshow(magnitude, cmap='gray')
titles = ["original", "horizontal", "vertical", "magnitude"]
for i, ax in enumerate(axs.ravel()):
    ax.set_title(titles[i])
    ax.axis("off")
plt.savefig(os.path.join(directory, "parta.png"))
plt.show()
