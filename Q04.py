import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
im = cv.imread('C:\Image_Processing_2\shells.tif', cv.IMREAD_GRAYSCALE)
h, _ = np.histogram(im.flatten(), 256, [0, 256])
c = h.cumsum()
cn = c * h.max() / c.max()
eq = cv.equalizeHist(im)
f, ax = plt.subplots(1, 3, figsize=(20, 5))
ax[0].imshow(im, cmap='gray')
ax[0].set_title('Original Image')
ax[0].axis('off')
ax[1].imshow(eq, cmap='gray')
ax[1].set_title('Vibrance-enhanced Image')
ax[1].axis('off')
ax[2].plot(cn, color='r')
ax[2].set_xlim([0, 256])
ax[2].set_title('Histogram')
ax[2].legend(('histogram',), loc='upper left')
output_dir = 'Q4'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'Histogram.png')
plt.savefig(output_path)
plt.show()
