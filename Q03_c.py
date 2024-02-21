import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
img = cv.imread('C:\Image_Processing\Video_01\spider.png', cv.IMREAD_COLOR)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue_channel, saturation_channel, value_channel = cv.split(hsv_img)
def intensity_transformation(x, a, b):
    return np.minimum(x + (a * 128 * np.exp(-((x - 128)**2) / (2 * b**2))), 255).astype(np.uint8)
a = 0.5  
b = 70
transformed_saturation_channel = intensity_transformation(saturation_channel, a, b)
transformed_saturation_rgb = cv.cvtColor(cv.merge([hue_channel, transformed_saturation_channel, value_channel]), cv.COLOR_HSV2RGB)
plt.figure(figsize=(10, 5))
plt.imshow(transformed_saturation_rgb)
plt.title('Transformed Saturation (a = {})'.format(a)) 
plt.axis('off')
plt.show()
