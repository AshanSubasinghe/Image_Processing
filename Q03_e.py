import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
original_img = cv.imread('C:\Image_Processing\Video_01\spider.png', cv.IMREAD_COLOR)
original_hsv_img = cv.cvtColor(original_img, cv.COLOR_BGR2HSV)
hue_channel, saturation_channel, value_channel = cv.split(original_hsv_img)
def intensity_transformation(x, a, b):
    return np.minimum(x + (a * 128 * np.exp(-((x - 128)**2) / (2 * b**2))), 255).astype(np.uint8)
a = 0.5  
b = 70
transformed_saturation_channel = intensity_transformation(saturation_channel, a, b)
recombined_hsv_img = cv.merge((hue_channel, transformed_saturation_channel, value_channel))
recombined_bgr_img = cv.cvtColor(recombined_hsv_img, cv.COLOR_HSV2BGR)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv.cvtColor(original_img, cv.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(cv.cvtColor(recombined_bgr_img, cv.COLOR_BGR2RGB))
axes[1].set_title('Vibrance-enhanced Image')
axes[1].axis('off')
axes[2].imshow(cv.cvtColor(recombined_hsv_img, cv.COLOR_HSV2RGB))
axes[2].set_title('Intensity Transformation (a = {})'.format(a))
axes[2].axis('off')
plt.show()
