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
recombined_hsv_img = cv.merge((hue_channel, transformed_saturation_channel, value_channel))
recombined_bgr_img = cv.cvtColor(recombined_hsv_img, cv.COLOR_HSV2BGR)
plt.imshow(cv.cvtColor(recombined_bgr_img, cv.COLOR_BGR2RGB))
plt.title('Recombined HSV Image')
plt.axis('off')
plt.show()
