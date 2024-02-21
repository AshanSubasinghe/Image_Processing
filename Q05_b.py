import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
im = cv.imread(r'C:\Image_Processing_2\rice_salt_pepper_noise.png')
if im is None:
    print("Error: Unable to read the image.")
else:
    blurred_image = cv.GaussianBlur(im, (5, 5), 0)
    image_rgb = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    blurred_rgb = cv.cvtColor(blurred_image, cv.COLOR_BGR2RGB)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(blurred_rgb)
    plt.title('Blurred Image')
    plt.axis('off')
    plt.show()

