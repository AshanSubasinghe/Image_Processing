import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
im1 = cv.imread("C:\Image_Processing\Video_01\margot_golden_gray.jpg", cv.IMREAD_GRAYSCALE)
assert im1 is not None
t = np.zeros(256, dtype = np.uint8)
t[0:222] = np.array([int(x*200/255) for x in range(222)])
t[222:256] = np.array([int(x*200/255 + 48) for x in range(222,256)])
im2 = t[im1]
fig, ax = plt.subplots(1,2,figsize = (10,10))
ax[0].imshow(im1 , vmin = 0, vmax = 255, cmap = 'gray')
ax[0].set_title('original')
ax[1].imshow(im2, vmin = 0, vmax = 255, cmap = 'gray')
ax[1].set_title('Intensity transformed')
plt.show()
