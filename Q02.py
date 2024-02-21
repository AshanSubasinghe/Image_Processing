import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('C:\Image_Processing\Video_01\highlights_and_shadows.jpg', cv.IMREAD_COLOR)
lab_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
l_channel, a_channel, b_channel = cv.split(lab_img)
gamma_value = 2.0
corrected_l_channel = np.power(l_channel / 255.0, gamma_value) * 255.0
corrected_l_channel = np.clip(corrected_l_channel, 0, 255).astype(np.uint8)
corrected_lab_img = cv.merge((corrected_l_channel, a_channel, b_channel))
corrected_rgb_img = cv.cvtColor(corrected_lab_img, cv.COLOR_LAB2RGB)
plt.figure(figsize=(15, 6))
plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256], color='b')
plt.title('Histogram of Original Image')
plt.subplot(2, 2, 3)
plt.imshow(corrected_rgb_img)
plt.title('Corrected Image (Gamma = 2.0)')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.hist(corrected_rgb_img.ravel(), 256, [0, 256], color='r')
plt.title('Histogram of Corrected Image')
plt.tight_layout()
plt.show()
